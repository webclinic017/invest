# encoding: utf-8
# 量化选股流程  思路来源: 陶博士
import os
import pandas as pd
import tushare as ts
from datetime import date, timedelta
import logging
from RPS.foreign_capital_increase import foreign_capital_filter, foreignCapitalHoldingV2
from security import get_interval_yield
pro = ts.pro_api("b625f0b90069039346d199aa3c0d5bc53fd47212437337b45ba87487")


def get_fund_holdings(quarter, year=date.today().year):
    # 基金持股
    # from RPS.bak_stock_pool import fund_pool as pool
    # return pool
    logging.warning("查询基金持股数据")
    pool = set()
    data = ts.fund_holdings(year=year, quarter=quarter)
    for i in data.values:
        code = i[7]
        name = i[3]
        fundHoldingdRatio = float(i[6])
        if fundHoldingdRatio >= 3:
            pool.add((code, name))
    logging.warning(f"机构持股: {pool}")
    return pool


def get_RPS_stock_pool():
    # 根据RPS值进行第一步筛选
    os.chdir("../RPS")
    logging.warning("根据RPS查询股池")
    pool = set()
    files = ['RPS_50_V2.csv', 'RPS_120_V2.csv', 'RPS_250_V2.csv']
    for file in files:
        df = pd.read_csv(file, encoding='utf-8')
        for i in df.values:
            if i[-1] >= 90:
                pool.add((i[0].split('.')[0], i[1]))
    # 增加一个50日RPS不低于70的条件, 避免长期RPS高但短期RPS开始下降的情况
    rps50_pool = set()
    rps50 = pd.read_csv('RPS_50_V2.csv', encoding='utf-8')
    for i in rps50.values:
        if i[-1] >= 70:
            rps50_pool.add((i[0].split('.')[0], i[1]))
    pool = [i for i in pool if i in rps50_pool]
    return pool


def get_close(code):
    # 按照日期范围获取股票交易日期,收盘价
    start = int(str(date.today() - timedelta(days=365)).replace('-', ''))
    end = int(str(date.today()).replace('-', ''))
    df = pro.daily(ts_code=code, start_date=start, end_date=end, fields='trade_date,close')
    # 将交易日期设置为索引值
    df.index = pd.to_datetime(df.trade_date)
    df = df.sort_index()
    closes = []
    [closes.append(i[1]) for i in df.values]
    if len(closes) < 1:
        logging.error(code, closes)
    close = closes[-1]
    highest = max(closes[:-1])
    momentum = round(close / highest, 3)
    interval_yield = round((closes[-1] - closes[0]) / closes[0] * 100, 2)
    return {'code': code, 'interval_yield': interval_yield, 'momentum': momentum}


def close_one_year_high(pool):
    # 接近一年新高
    logging.warning("股价接近一年新高")
    result = []
    for i in pool:
        data = get_interval_yield(i['code'])
        if data['momentum'] > 0.9:
            result.append(i)
    return result


def stock_pool_filter_process():
    rps_pool = get_RPS_stock_pool()     # 股价相对强度RPS优先一切
    fund_pool = get_fund_holdings(quarter=2)
    foreign_capital_pool = foreignCapitalHoldingV2()
    pool = fund_pool.union(foreign_capital_pool)    # 基金持股3% + 北向持股三千万
    pool = [i for i in pool if i in rps_pool]
    pool = [{'code': i[0], 'name': i[1]} for i in pool]
    logging.warning(f"基金持股3% + 北向持股三千万: {pool}")
    fc_add = foreign_capital_filter()  # 外资增仓
    pool = [i for i in pool if i in fc_add]
    logging.warning(f"外资最近一个月增持超过一亿或1%流通股: {pool}")
    pool = close_one_year_high(pool)    # 股价接近一年新高
    logging.warning(f"基金持股3% + 北向持股三千万 + 外资增持 + 股价接近一年新高: {pool}")
    return pool


if __name__ == '__main__':
    stock_pool_filter_process()


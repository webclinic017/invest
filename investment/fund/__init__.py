# encoding: utf-8
from fundrank import get_fund_detail_list

funds = [{'code': '002190', 'name': '农银新能源主题', 2016: -1.81, 2017: 22.07, 2018: -34.41, 2019: 34.63, 2020: 163.49, 2021: 54.83, '3y': 423.74, '5y': 336.4}, {'code': '000209', 'name': '信诚新兴产业混合A', 2016: -28.06, 2017: -12.7, 2018: -30.47, 2019: 42.03, 2020: 102.88, 2021: 102.53, '3y': 424.56, '5y': 239.67}, {'code': '001704', 'name': '国投瑞银进宝灵活配置混合', 2016: -0.69, 2017: 5.88, 2018: -24.41, 2019: 85.51, 2020: 92.43, 2021: 93.1, '3y': 539.46, '5y': 431.36}, {'code': '540008', 'name': '汇丰晋信低碳先锋股票', 2016: -22.82, 2017: -3.64, 2018: -36.68, 2019: 45.87, 2020: 134.41, 2021: 50.44, '3y': 358.48, '5y': 185.17}, {'code': '400015', 'name': '东方新能源汽车混合', 2016: -21.17, 2017: -4.21, 2018: -20.21, 2019: 27.42, 2020: 116.3, 2021: 71.8, '3y': 349.4, '5y': 164.52}, {'code': '000336', 'name': '农银研究精选混合', 2016: -20.68, 2017: 3.19, 2018: -36.61, 2019: 55.94, 2020: 154.88, 2021: 40.49, '3y': 354.4, '5y': 245.73}, {'code': '001643', 'name': '汇丰晋信智造先锋股票A', 2016: -5.9, 2017: 7.45, 2018: -27.16, 2019: 73.88, 2020: 128.65, 2021: 41.4, '3y': 403.56, '5y': 342.79}, {'code': '001245', 'name': '工银生态环境股票', 2016: -14.33, 2017: -12.23, 2018: -30.56, 2019: 48.07, 2020: 122.51, 2021: 64.34, '3y': 407.77, '5y': 225.58}, {'code': '001644', 'name': '汇丰晋信智造先锋股票C', 2016: -6.44, 2017: 7.06, 2018: -27.52, 2019: 73.12, 2020: 127.52, 2021: 40.91, '3y': 396.43, '5y': 332.71}, {'code': '001606', 'name': '农银工业4.0混合', 2016: -22.29, 2017: 48.2, 2018: -35.74, 2019: 37.6, 2020: 166.56, 2021: 38.73, '3y': 359.17, '5y': 377.53}, {'code': '001298', 'name': '金鹰民族新兴混合', 2016: -1.76, 2017: 7.76, 2018: -22.71, 2019: 44.92, 2020: 88.62, 2021: 93.79, '3y': 417.39, '5y': 343.84}, {'code': '001156', 'name': '申万菱信新能源汽车混合', 2016: -5.88, 2017: 13.36, 2018: -25.41, 2019: 48.06, 2020: 110.76, 2021: 45.91, '3y': 351.22, '5y': 277.55}, {'code': '000828', 'name': '泰达转型机遇股票A', 2016: -13.72, 2017: 12.1, 2018: -24.1, 2019: 71.23, 2020: 104.9, 2021: 65.91, '3y': 449.63, '5y': 345.6}, {'code': '002083', 'name': '新华鑫动力灵活配置混合A', 2016: 0.3, 2017: 0.1, 2018: -30.98, 2019: 51.52, 2020: 121.43, 2021: 50.03, '3y': 359.57, '5y': 248.11}, {'code': '002084', 'name': '新华鑫动力灵活配置混合C', 2016: 0.1, 2017: 0.1, 2018: -31.14, 2019: 51.59, 2020: 121.13, 2021: 49.92, '3y': 358.07, '5y': 246.76}, {'code': '165516', 'name': '信诚周期轮动混合(LOF)', 2016: -13.93, 2017: 13.45, 2018: -23.3, 2019: 64.45, 2020: 90.66, 2021: 55.18, '3y': 336.64, '5y': 250.11}, {'code': '001569', 'name': '泰信国策驱动灵活配置混合', 2016: -18.92, 2017: -9.36, 2018: -31.77, 2019: 63.26, 2020: 89.53, 2021: 58.03, '3y': 303.4, '5y': 202.8}, {'code': '398051', 'name': '中海环保新能源混合', 2016: -27.81, 2017: 18.78, 2018: -21.35, 2019: 29.83, 2020: 109.07, 2021: 50.24, '3y': 302.15, '5y': 268.21}, {'code': '090018', 'name': '大成新锐产业混合', 2016: 8.9, 2017: -0.82, 2018: -14.65, 2019: 47.43, 2020: 79.41, 2021: 82.98, '3y': 357.2, '5y': 235.47}, {'code': '161028', 'name': '富国中证新能源汽车指数(LOF)A', 2016: -18.82, 2017: 3.69, 2018: 4.47, 2019: 39.42, 2020: 62.0, 2021: 45.99, '3y': 157.21, '5y': 78.37}, {'code': '001951', 'name': '金鹰改革红利混合', 2016: 7.68, 2017: 4.91, 2018: -25.44, 2019: 30.81, 2020: 99.28, 2021: 68.45, '3y': 305.47, '5y': 244.42}, {'code': '000409', 'name': '鹏华环保产业股票', 2016: -5.84, 2017: 17.36, 2018: -19.57, 2019: 34.55, 2020: 116.68, 2021: 41.69, '3y': 308.51, '5y': 283.82}, {'code': '167001', 'name': '平安鼎泰混合(LOF)', 2016: -0.03, 2017: -20.12, 2018: -26.07, 2019: 41.97, 2020: 60.45, 2021: 91.78, '3y': 302.75, '5y': 157.87}, {'code': '550009', 'name': '信诚中小盘混合', 2016: -27.04, 2017: 7.75, 2018: -28.61, 2019: 75.48, 2020: 86.24, 2021: 59.0, '3y': 337.73, '5y': 271.41}, {'code': '210008', 'name': '金鹰策略配置混合', 2016: -15.29, 2017: 10.65, 2018: -16.39, 2019: 26.22, 2020: 99.83, 2021: 63.56, '3y': 266.73, '5y': 234.15}, {'code': '002669', 'name': '华商万众创新混合', 2016: -2.4, 2017: -19.06, 2018: -21.27, 2019: 68.81, 2020: 116.67, 2021: 37.63, '3y': 363.17, '5y': 218.84}, {'code': '000689', 'name': '前海开源新经济混合A', 2016: -12.74, 2017: 11.65, 2018: -18.63, 2019: 20.73, 2020: 60.15, 2021: 96.66, '3y': 266.41, '5y': 210.94}, {'code': '001300', 'name': '大成睿景灵活配置混合A', 2016: -14.17, 2017: 9.08, 2018: -28.88, 2019: 43.97, 2020: 77.59, 2021: 78.09, '3y': 336.73, '5y': 241.94}, {'code': '481010', 'name': '工银中小盘混合', 2016: -21.86, 2017: -11.49, 2018: -25.89, 2019: 61.21, 2020: 134.73, 2021: 29.21, '3y': 333.36, '5y': 211.98}, {'code': '400032', 'name': '东方主题精选混合', 2016: -22.0, 2017: -1.7, 2018: -34.74, 2019: 35.68, 2020: 108.42, 2021: 48.9, '3y': 267.32, '5y': 154.29}, {'code': '210003', 'name': '金鹰行业优势混合', 2016: -17.72, 2017: 18.98, 2018: -18.4, 2019: 42.83, 2020: 80.37, 2021: 72.07, '3y': 294.64, '5y': 280.57}, {'code': '001476', 'name': '中银智能制造股票A', 2016: -28.16, 2017: 13.71, 2018: -38.98, 2019: 53.69, 2020: 109.09, 2021: 39.5, '3y': 297.52, '5y': 203.1}, {'code': '001301', 'name': '大成睿景灵活配置混合C', 2016: -14.85, 2017: 8.09, 2018: -29.42, 2019: 42.78, 2020: 76.31, 2021: 77.2, '3y': 326.57, '5y': 228.84}, {'code': '000126', 'name': '招商安润混合', 2016: -4.92, 2017: 1.59, 2018: 0.59, 2019: 33.9, 2020: 97.9, 2021: 50.99, '3y': 300.1, '5y': 306.81}, {'code': '610006', 'name': '信达澳银产业升级混合', 2016: -18.72, 2017: -5.28, 2018: -22.24, 2019: 53.23, 2020: 72.65, 2021: 76.46, '3y': 300.97, '5y': 206.01}, {'code': '700003', 'name': '平安策略先锋混合', 2016: -28.91, 2017: 10.72, 2018: -28.79, 2019: 75.33, 2020: 67.25, 2021: 65.85, '3y': 332.33, '5y': 250.96}, {'code': '519126', 'name': '浦银安盛新经济结构混合A', 2016: -16.73, 2017: -0.43, 2018: -35.0, 2019: 62.63, 2020: 87.55, 2021: 50.76, '3y': 293.7, '5y': 204.41}, {'code': '001858', 'name': '建信鑫利灵活配置混合', 2016: -0.59, 2017: 2.38, 2018: -21.24, 2019: 34.92, 2020: 104.45, 2021: 35.65, '3y': 245.63, '5y': 202.32}, {'code': '166301', 'name': '华商新趋势优选灵活配置混合', 2016: -7.87, 2017: 14.63, 2018: -14.83, 2019: 69.6, 2020: 77.42, 2021: 52.21, '3y': 316.21, '5y': 352.61}, {'code': '162202', 'name': '泰达宏利周期混合', 2016: -4.49, 2017: 10.41, 2018: -11.6, 2019: 47.81, 2020: 68.76, 2021: 56.0, '3y': 272.22, '5y': 211.88}, {'code': '001702', 'name': '东方创新科技混合', 2016: -18.37, 2017: 4.76, 2018: -29.94, 2019: 56.03, 2020: 112.38, 2021: 37.21, '3y': 315.24, '5y': 211.04}, {'code': '000739', 'name': '平安新鑫先锋A', 2016: -42.49, 2017: 17.58, 2018: -34.21, 2019: 46.9, 2020: 68.16, 2021: 58.24, '3y': 240.78, '5y': 180.96}, {'code': '000592', 'name': '建信改革红利股票', 2016: -17.3, 2017: 26.84, 2018: -33.64, 2019: 60.75, 2020: 101.88, 2021: 34.02, '3y': 276.49, '5y': 254.12}, {'code': '610004', 'name': '信达澳银中小盘混合', 2016: -13.13, 2017: 5.35, 2018: -15.15, 2019: 62.06, 2020: 61.94, 2021: 72.97, '3y': 339.55, '5y': 315.13}, {'code': '001515', 'name': '平安新鑫先锋C', 2016: -42.41, 2017: 17.13, 2018: -34.44, 2019: 46.34, 2020: 67.57, 2021: 57.81, '3y': 237.26, '5y': 175.88}, {'code': '000729', 'name': '建信中小盘先锋股票', 2016: -19.68, 2017: 7.14, 2018: -28.07, 2019: 29.19, 2020: 81.21, 2021: 58.43, '3y': 229.65, '5y': 167.51}, {'code': '519642', 'name': '银河智造混合', 2016: -2.0, 2017: 33.98, 2018: -27.34, 2019: 60.06, 2020: 108.84, 2021: 27.72, '3y': 279.59, '5y': 314.34}, {'code': '481015', 'name': '工银主题策略混合A', 2016: -30.42, 2017: 13.51, 2018: -37.54, 2019: 57.7, 2020: 129.57, 2021: 21.1, '3y': 274.58, '5y': 184.48}, {'code': '000793', 'name': '工银高端制造股票', 2016: -26.28, 2017: 1.45, 2018: -41.81, 2019: 48.28, 2020: 128.81, 2021: 20.21, '3y': 244.2, '5y': 149.7}, {'code': '001822', 'name': '华商智能生活灵活配置混合', 2016: -12.14, 2017: -7.64, 2018: -5.72, 2019: 34.97, 2020: 75.53, 2021: 54.14, '3y': 249.81, '5y': 209.29}, {'code': '519095', 'name': '新华行业周期轮换混合', 2016: -9.21, 2017: 0.64, 2018: -16.35, 2019: 49.72, 2020: 84.12, 2021: 36.98, '3y': 263.32, '5y': 211.65}, {'code': '000541', 'name': '华商创新成长混合发起式', 2016: -25.71, 2017: -7.38, 2018: -29.02, 2019: 66.32, 2020: 101.4, 2021: 33.19, '3y': 308.1, '5y': 125.58}, {'code': '001933', 'name': '华商新兴活力混合', 2016: 1.1, 2017: 6.73, 2018: -29.66, 2019: 34.78, 2020: 71.36, 2021: 55.96, '3y': 206.5, '5y': 168.04}, {'code': '001959', 'name': '华商乐享互联灵活配置混合A', 2016: -13.29, 2017: -2.52, 2018: -39.91, 2019: 84.18, 2020: 79.96, 2021: 42.66, '3y': 312.44, '5y': 160.32}, {'code': '206012', 'name': '鹏华价值精选股票', 2016: -11.35, 2017: 7.22, 2018: -32.48, 2019: 60.12, 2020: 87.68, 2021: 31.91, '3y': 267.68, '5y': 188.27}, {'code': '000924', 'name': '宝盈先进制造混合A', 2016: -18.95, 2017: -2.01, 2018: -12.02, 2019: 71.05, 2020: 77.34, 2021: 32.93, '3y': 238.01, '5y': 213.08}, {'code': '519196', 'name': '万家新兴蓝筹灵活配置混合', 2016: 12.66, 2017: 31.15, 2018: -14.06, 2019: 41.91, 2020: 82.3, 2021: 33.01, '3y': 201.6, '5y': 191.06}, {'code': '040015', 'name': '华安动态灵活配置混合', 2016: -5.43, 2017: 13.2, 2018: -18.89, 2019: 68.59, 2020: 53.02, 2021: 69.79, '3y': 275.82, '5y': 199.27}, {'code': '377240', 'name': '上投摩根新兴动力混合A', 2016: -19.81, 2017: 42.21, 2018: -35.65, 2019: 70.27, 2020: 78.24, 2021: 43.22, '3y': 278.56, '5y': 276.66}, {'code': '001487', 'name': '宝盈优势产业混合A', 2016: -13.08, 2017: 29.57, 2018: -22.13, 2019: 63.06, 2020: 33.84, 2021: 87.72, '3y': 295.88, '5y': 278.57}, {'code': '240022', 'name': '华宝资源优选混合A', 2016: 16.34, 2017: 24.56, 2018: -17.14, 2019: 31.18, 2020: 60.23, 2021: 68.19, '3y': 244.17, '5y': 258.82}, {'code': '530001', 'name': '建信恒久价值混合', 2016: -11.05, 2017: 5.24, 2018: -16.03, 2019: 48.98, 2020: 92.86, 2021: 19.46, '3y': 183.36, '5y': 119.79}, {'code': '310368', 'name': '申万菱信竞争优势混合', 2016: -16.96, 2017: 21.78, 2018: -16.83, 2019: 43.0, 2020: 57.2, 2021: 66.09, '3y': 254.33, '5y': 142.74}, {'code': '001279', 'name': '中海积极增利混合', 2016: -12.41, 2017: 17.58, 2018: -30.01, 2019: 66.91, 2020: 64.18, 2021: 59.77, '3y': 295.05, '5y': 228.99}, {'code': '001339', 'name': '兴银鼎新灵活配置混合', 2016: -8.91, 2017: 6.69, 2018: -20.92, 2019: 22.2, 2020: 60.88, 2021: 57.88, '3y': 186.28, '5y': 162.37}, {'code': '020023', 'name': '国泰事件驱动策略混合', 2016: -5.0, 2017: 33.71, 2018: -34.13, 2019: 65.98, 2020: 97.83, 2021: 24.91, '3y': 257.05, '5y': 255.17}, {'code': '519702', 'name': '交银趋势混合A', 2016: 2.67, 2017: 21.76, 2018: -16.47, 2019: 46.16, 2020: 61.53, 2021: 63.18, '3y': 265.28, '5y': 290.09}, {'code': '519918', 'name': '华夏兴和混合', 2016: -10.42, 2017: 6.12, 2018: -8.46, 2019: 43.78, 2020: 65.47, 2021: 50.71, '3y': 232.43, '5y': 185.95}, {'code': '377530', 'name': '上投摩根行业轮动混合A', 2016: -25.2, 2017: 31.96, 2018: -27.25, 2019: 56.89, 2020: 72.47, 2021: 48.38, '3y': 251.39, '5y': 208.4}, {'code': '370024', 'name': '上投摩根核心优选混合', 2016: -28.67, 2017: 38.9, 2018: -32.18, 2019: 61.25, 2020: 78.26, 2021: 41.1, '3y': 234.27, '5y': 235.75}, {'code': '519909', 'name': '华安安顺混合', 2016: -4.16, 2017: 12.38, 2018: -11.12, 2019: 28.08, 2020: 83.93, 2021: 38.12, '3y': 212.39, '5y': 241.83}, {'code': '202027', 'name': '南方高端装备灵活配置混合A', 2016: -11.18, 2017: 22.83, 2018: -19.56, 2019: 54.37, 2020: 72.42, 2021: 45.04, '3y': 249.18, '5y': 249.44}, {'code': '001410', 'name': '信达澳银新能源产业股票', 2016: -5.91, 2017: 39.27, 2018: -15.81, 2019: 94.11, 2020: 59.88, 2021: 49.62, '3y': 335.75, '5y': 430.7}, {'code': '001471', 'name': '融通新能源灵活配置混合', 2016: 3.59, 2017: 5.75, 2018: -15.79, 2019: 57.36, 2020: 60.58, 2021: 45.21, '3y': 239.2, '5y': 213.86}, {'code': '001809', 'name': '中信建投智信物联网A', 2016: -1.2, 2017: 13.76, 2018: -30.34, 2019: 71.39, 2020: 54.97, 2021: 52.77, '3y': 263.44, '5y': 219.28}, {'code': '001811', 'name': '中欧明睿新常态混合A', 2016: -8.0, 2017: 35.98, 2018: -11.03, 2019: 56.51, 2020: 57.08, 2021: 52.47, '3y': 242.03, '5y': 301.03}, {'code': '165520', 'name': '信诚中证800有色指数(LOF)A', 2016: -2.99, 2017: 24.49, 2018: -20.9, 2019: 24.2, 2020: 39.61, 2021: 73.21, '3y': 168.4, '5y': 127.15}, {'code': '000584', 'name': '新华鑫益灵活配置混合', 2016: -5.47, 2017: 13.75, 2018: -6.43, 2019: 47.19, 2020: 72.68, 2021: 36.91, '3y': 237.51, '5y': 284.91}, {'code': '002168', 'name': '嘉实智能汽车股票', 2016: 24.0, 2017: 20.16, 2018: -24.83, 2019: 65.62, 2020: 93.91, 2021: 24.38, '3y': 316.57, '5y': 270.98}, {'code': '001808', 'name': '银华互联网主题灵活配置混合', 2016: -22.21, 2017: 17.31, 2018: -30.95, 2019: 60.93, 2020: 96.63, 2021: 26.76, '3y': 270.94, '5y': 202.28}, {'code': '540003', 'name': '汇丰晋信动态策略混合A', 2016: -9.24, 2017: 19.18, 2018: -17.32, 2019: 44.65, 2020: 71.75, 2021: 45.24, '3y': 244.97, '5y': 230.36}, {'code': '000603', 'name': '易方达创新驱动灵活配置混合', 2016: -29.25, 2017: -0.22, 2018: -24.62, 2019: 41.11, 2020: 73.04, 2021: 44.3, '3y': 223.99, '5y': 147.9}, {'code': '375010', 'name': '上投摩根中国优势混合', 2016: -10.93, 2017: 26.18, 2018: -8.78, 2019: 57.81, 2020: 57.79, 2021: 41.31, '3y': 208.15, '5y': 167.41}, {'code': '000462', 'name': '农银主题轮动混合', 2016: -24.59, 2017: 46.68, 2018: -43.34, 2019: 54.25, 2020: 93.94, 2021: 30.58, '3y': 240.93, '5y': 218.42}, {'code': '519089', 'name': '新华优选成长混合', 2016: -13.82, 2017: -3.76, 2018: -3.32, 2019: 43.77, 2020: 66.04, 2021: 34.06, '3y': 172.07, '5y': 127.83}, {'code': '000242', 'name': '景顺长城策略精选灵活配置混合', 2016: 0.36, 2017: 6.18, 2018: -13.61, 2019: 44.03, 2020: 63.21, 2021: 51.67, '3y': 238.91, '5y': 140.62}, {'code': '001753', 'name': '红土创新新兴产业混合', 2016: -16.67, 2017: 10.85, 2018: -26.6, 2019: 27.1, 2020: 71.49, 2021: 46.08, '3y': 184.95, '5y': 151.95}, {'code': '002296', 'name': '长城行业轮动混合A', 2016: 2.0, 2017: 4.31, 2018: 0.68, 2019: 13.38, 2020: 19.34, 2021: 104.78, '3y': 178.33, '5y': 190.42}, {'code': '519997', 'name': '长信银利精选混合', 2016: -3.16, 2017: 7.2, 2018: -4.93, 2019: 24.96, 2020: 45.57, 2021: 18.51, '3y': 87.6, '5y': 82.18}, {'code': '001677', 'name': '中银战略新兴产业股票A', 2016: 4.4, 2017: 27.49, 2018: -24.34, 2019: 57.6, 2020: 66.16, 2021: 40.92, '3y': 237.21, '5y': 259.73}, {'code': '002537', 'name': '平安安盈灵活配置混合', 2016: 0.3, 2017: 1.79, 2018: 1.18, 2019: 22.81, 2020: 70.87, 2021: 39.35, '3y': 195.28, '5y': 198.78}, {'code': '200015', 'name': '长城优化升级混合A', 2016: -12.66, 2017: 19.41, 2018: -18.16, 2019: 45.38, 2020: 58.58, 2021: 43.54, '3y': 212.18, '5y': 208.67}, {'code': '000756', 'name': '建信潜力新蓝筹股票', 2016: -7.21, 2017: 15.17, 2018: -26.8, 2019: 32.28, 2020: 65.21, 2021: 46.71, '3y': 193.06, '5y': 169.86}, {'code': '519091', 'name': '新华泛资源优势混合', 2016: 6.67, 2017: 18.57, 2018: -9.95, 2019: 40.26, 2020: 67.65, 2021: 32.1, '3y': 199.24, '5y': 278.07}, {'code': '000308', 'name': '建信创新中国混合', 2016: -0.95, 2017: 13.6, 2018: -20.98, 2019: 49.44, 2020: 64.07, 2021: 39.44, '3y': 242.24, '5y': 201.16}, {'code': '720001', 'name': '财通价值动量混合', 2016: -18.59, 2017: 15.39, 2018: -16.63, 2019: 70.96, 2020: 51.29, 2021: 58.69, '3y': 304.2, '5y': 202.87}, {'code': '690011', 'name': '民生加银积极成长混合发起式', 2016: -18.04, 2017: 9.04, 2018: -16.15, 2019: 48.75, 2020: 69.77, 2021: 28.77, '3y': 215.96, '5y': 198.26}, {'code': '001070', 'name': '建信信息产业股票', 2016: -13.71, 2017: 18.59, 2018: -30.14, 2019: 63.83, 2020: 70.55, 2021: 36.92, '3y': 262.06, '5y': 211.9}, {'code': '000390', 'name': '华商优势行业混合', 2016: -0.95, 2017: 6.28, 2018: -7.94, 2019: 39.26, 2020: 22.3, 2021: 23.78, '3y': 83.71, '5y': 76.02}, {'code': '290008', 'name': '泰信发展主题混合', 2016: -13.95, 2017: 7.31, 2018: -14.98, 2019: 48.38, 2020: 54.79, 2021: 39.17, '3y': 199.9, '5y': 177.08}, {'code': '673060', 'name': '西部利得景瑞灵活配置混合A', 2016: -0.6, 2017: -2.72, 2018: -18.72, 2019: 72.26, 2020: 63.38, 2021: 42.73, '3y': 283.67, '5y': 203.1}, {'code': '001480', 'name': '财通成长优选混合', 2016: -25.46, 2017: 15.18, 2018: -23.06, 2019: 72.93, 2020: 48.96, 2021: 56.35, '3y': 296.2, '5y': 235.56}, {'code': '288001', 'name': '华夏经典混合', 2016: -9.19, 2017: 2.15, 2018: -4.22, 2019: 26.17, 2020: 66.57, 2021: 40.97, '3y': 181.15, '5y': 149.12}, {'code': '519115', 'name': '浦银安盛红利精选混合', 2016: -19.65, 2017: 11.29, 2018: -25.09, 2019: 65.54, 2020: 50.97, 2021: 45.62, '3y': 225.82, '5y': 196.67}, {'code': '460001', 'name': '华泰柏瑞盛世中国混合', 2016: -14.35, 2017: 18.2, 2018: -9.27, 2019: 39.44, 2020: 68.28, 2021: 6.39, '3y': 95.04, '5y': 68.2}, {'code': '001267', 'name': '泰达宏利蓝筹混合', 2016: -26.64, 2017: 28.49, 2018: -25.65, 2019: 52.63, 2020: 56.58, 2021: 34.18, '3y': 191.15, '5y': 200.18}, {'code': '519158', 'name': '新华趋势领航混合', 2016: -5.17, 2017: 5.1, 2018: -17.51, 2019: 57.34, 2020: 52.61, 2021: 28.45, '3y': 195.79, '5y': 129.85}]
# 最近半年，一年，两年，三年，五年排行榜前五百名的基金列表
funds_v2 = [{'code': '002190', 'name': '农银新能源主题', 2016: -1.81, 2017: 22.07, 2018: -34.41, 2019: 34.63, 2020: 163.49, 2021: 54.13, '3y': 413.88, '5y': 334.29}, {'code': '001704', 'name': '国投瑞银进宝灵活配置混合', 2016: -0.69, 2017: 5.88, 2018: -24.41, 2019: 85.51, 2020: 92.43, 2021: 95.13, '3y': 548.27, '5y': 436.41}, {'code': '000209', 'name': '信诚新兴产业混合A', 2016: -28.06, 2017: -12.7, 2018: -30.47, 2019: 42.03, 2020: 102.88, 2021: 102.33, '3y': 422.17, '5y': 237.96}, {'code': '540008', 'name': '汇丰晋信低碳先锋股票A', 2016: -22.82, 2017: -3.64, 2018: -36.68, 2019: 45.87, 2020: 134.41, 2021: 52.62, '3y': 357.55, '5y': 187.86}, {'code': '400015', 'name': '东方新能源汽车混合', 2016: -21.17, 2017: -4.21, 2018: -20.21, 2019: 27.42, 2020: 116.3, 2021: 71.89, '3y': 344.71, '5y': 162.28}, {'code': '001643', 'name': '汇丰晋信智造先锋股票A', 2016: -5.9, 2017: 7.45, 2018: -27.16, 2019: 73.88, 2020: 128.65, 2021: 43.13, '3y': 401.91, '5y': 344.98}, {'code': '001245', 'name': '工银生态环境股票', 2016: -14.33, 2017: -12.23, 2018: -30.56, 2019: 48.07, 2020: 122.51, 2021: 64.45, '3y': 404.63, '5y': 226.16}, {'code': '000336', 'name': '农银研究精选混合', 2016: -20.68, 2017: 3.19, 2018: -36.61, 2019: 55.94, 2020: 154.88, 2021: 39.38, '3y': 338.65, '5y': 244.54}, {'code': '001644', 'name': '汇丰晋信智造先锋股票C', 2016: -6.44, 2017: 7.06, 2018: -27.52, 2019: 73.12, 2020: 127.52, 2021: 42.62, '3y': 394.84, '5y': 334.81}, {'code': '001606', 'name': '农银工业4.0混合', 2016: -22.29, 2017: 48.2, 2018: -35.74, 2019: 37.6, 2020: 166.56, 2021: 37.59, '3y': 360.98, '5y': 373.41}, {'code': '000828', 'name': '泰达转型机遇股票A', 2016: -13.72, 2017: 12.1, 2018: -24.1, 2019: 71.23, 2020: 104.9, 2021: 66.13, '3y': 455.26, '5y': 341.98}, {'code': '001298', 'name': '金鹰民族新兴混合', 2016: -1.76, 2017: 7.76, 2018: -22.71, 2019: 44.92, 2020: 88.62, 2021: 89.69, '3y': 408.2, '5y': 333.57}, {'code': '001156', 'name': '申万菱信新能源汽车混合', 2016: -5.88, 2017: 13.36, 2018: -25.41, 2019: 48.06, 2020: 110.76, 2021: 44.38, '3y': 335.84, '5y': 273.58}, {'code': '090018', 'name': '大成新锐产业混合', 2016: 8.9, 2017: -0.82, 2018: -14.65, 2019: 47.43, 2020: 79.41, 2021: 88.25, '3y': 367.45, '5y': 243.2}, {'code': '002083', 'name': '新华鑫动力灵活配置混合A', 2016: 0.3, 2017: 0.1, 2018: -30.98, 2019: 51.52, 2020: 121.43, 2021: 48.07, '3y': 354.17, '5y': 243.57}, {'code': '002084', 'name': '新华鑫动力灵活配置混合C', 2016: 0.1, 2017: 0.1, 2018: -31.14, 2019: 51.59, 2020: 121.13, 2021: 47.96, '3y': 352.7, '5y': 242.24}, {'code': '001569', 'name': '泰信国策驱动灵活配置混合', 2016: -18.92, 2017: -9.36, 2018: -31.77, 2019: 63.26, 2020: 89.53, 2021: 57.27, '3y': 298.23, '5y': 200.97}, {'code': '165516', 'name': '信诚周期轮动混合(LOF)', 2016: -13.93, 2017: 13.45, 2018: -23.3, 2019: 64.45, 2020: 90.66, 2021: 54.74, '3y': 335.66, '5y': 248.5}, {'code': '167001', 'name': '平安鼎泰混合(LOF)', 2016: -0.03, 2017: -20.12, 2018: -26.07, 2019: 41.97, 2020: 60.45, 2021: 95.33, '3y': 308.87, '5y': 162.65}, {'code': '001951', 'name': '金鹰改革红利混合', 2016: 7.68, 2017: 4.91, 2018: -25.44, 2019: 30.81, 2020: 99.28, 2021: 67.14, '3y': 299.24, '5y': 241.09}, {'code': '161028', 'name': '富国中证新能源汽车指数(LOF)A', 2016: -18.82, 2017: 3.69, 2018: 4.47, 2019: 39.42, 2020: 62.0, 2021: 44.86, '3y': 151.77, '5y': 76.84}, {'code': '398051', 'name': '中海环保新能源混合', 2016: -27.81, 2017: 18.78, 2018: -21.35, 2019: 29.83, 2020: 109.07, 2021: 47.97, '3y': 292.62, '5y': 263.08}, {'code': '000409', 'name': '鹏华环保产业股票', 2016: -5.84, 2017: 17.36, 2018: -19.57, 2019: 34.55, 2020: 116.68, 2021: 39.7, '3y': 297.81, '5y': 278.18}, {'code': '001300', 'name': '大成睿景灵活配置混合A', 2016: -14.17, 2017: 9.08, 2018: -28.88, 2019: 43.97, 2020: 77.59, 2021: 82.52, '3y': 344.59, '5y': 249.54}, {'code': '550009', 'name': '信诚中小盘混合', 2016: -27.04, 2017: 7.75, 2018: -28.61, 2019: 75.48, 2020: 86.24, 2021: 56.74, '3y': 328.86, '5y': 264.7}, {'code': '210008', 'name': '金鹰策略配置混合', 2016: -15.29, 2017: 10.65, 2018: -16.39, 2019: 26.22, 2020: 99.83, 2021: 61.54, '3y': 262.08, '5y': 229.35}, {'code': '001301', 'name': '大成睿景灵活配置混合C', 2016: -14.85, 2017: 8.09, 2018: -29.42, 2019: 42.78, 2020: 76.31, 2021: 81.55, '3y': 334.03, '5y': 236.02}, {'code': '002669', 'name': '华商万众创新混合', 2016: -2.4, 2017: -19.06, 2018: -21.27, 2019: 68.81, 2020: 116.67, 2021: 36.13, '3y': 361.55, '5y': 215.06}, {'code': '210003', 'name': '金鹰行业优势混合', 2016: -17.72, 2017: 18.98, 2018: -18.4, 2019: 42.83, 2020: 80.37, 2021: 75.12, '3y': 305.53, '5y': 286.06}, {'code': '481010', 'name': '工银中小盘混合', 2016: -21.86, 2017: -11.49, 2018: -25.89, 2019: 61.21, 2020: 134.73, 2021: 29.13, '3y': 331.49, '5y': 210.33}, {'code': '400032', 'name': '东方主题精选混合', 2016: -22.0, 2017: -1.7, 2018: -34.74, 2019: 35.68, 2020: 108.42, 2021: 48.75, '3y': 269.56, '5y': 152.83}, {'code': '000126', 'name': '招商安润混合', 2016: -4.92, 2017: 1.59, 2018: 0.59, 2019: 33.9, 2020: 97.9, 2021: 50.34, '3y': 298.78, '5y': 305.07}, {'code': '610006', 'name': '信达澳银产业升级混合', 2016: -18.72, 2017: -5.28, 2018: -22.24, 2019: 53.23, 2020: 72.65, 2021: 78.08, '3y': 316.42, '5y': 206.56}, {'code': '000689', 'name': '前海开源新经济混合A', 2016: -12.74, 2017: 11.65, 2018: -18.63, 2019: 20.73, 2020: 60.15, 2021: 93.71, '3y': 259.72, '5y': 206.15}, {'code': '001476', 'name': '中银智能制造股票A', 2016: -28.16, 2017: 13.71, 2018: -38.98, 2019: 53.69, 2020: 109.09, 2021: 37.2, '3y': 289.59, '5y': 198.11}, {'code': '001716', 'name': '工银新趋势灵活配置混合A', 2016: 1.9, 2017: 17.88, 2018: -9.25, 2019: 25.8, 2020: 121.31, 2021: 34.14, '3y': 276.23, '5y': 307.11}, {'code': '002132', 'name': '广发鑫享混合', 2016: -5.1, 2017: 14.33, 2018: -32.53, 2019: 55.74, 2020: 109.3, 2021: 29.38, '3y': 280.17, '5y': 213.08}, {'code': '001997', 'name': '工银新趋势灵活配置混合C', 2016: 1.1, 2017: 13.37, 2018: -9.96, 2019: 25.12, 2020: 119.84, 2021: 33.57, '3y': 269.2, '5y': 281.09}, {'code': '700003', 'name': '平安策略先锋混合', 2016: -28.91, 2017: 10.72, 2018: -28.79, 2019: 75.33, 2020: 67.25, 2021: 64.8, '3y': 331.42, '5y': 248.16}, {'code': '166301', 'name': '华商新趋势优选灵活配置混合', 2016: -7.87, 2017: 14.63, 2018: -14.83, 2019: 69.6, 2020: 77.42, 2021: 56.71, '3y': 328.16, '5y': 366.23}, {'code': '001858', 'name': '建信鑫利灵活配置混合', 2016: -0.59, 2017: 2.38, 2018: -21.24, 2019: 34.92, 2020: 104.45, 2021: 35.76, '3y': 245.52, '5y': 202.57}, {'code': '519126', 'name': '浦银安盛新经济结构混合A', 2016: -16.73, 2017: -0.43, 2018: -35.0, 2019: 62.63, 2020: 87.55, 2021: 49.6, '3y': 295.56, '5y': 199.42}, {'code': '000739', 'name': '平安新鑫先锋A', 2016: -42.49, 2017: 17.58, 2018: -34.21, 2019: 46.9, 2020: 68.16, 2021: 59.71, '3y': 243.6, '5y': 181.86}, {'code': '001515', 'name': '平安新鑫先锋C', 2016: -42.41, 2017: 17.13, 2018: -34.44, 2019: 46.34, 2020: 67.57, 2021: 59.27, '3y': 240.02, '5y': 176.49}, {'code': '000592', 'name': '建信改革红利股票', 2016: -17.3, 2017: 26.84, 2018: -33.64, 2019: 60.75, 2020: 101.88, 2021: 34.1, '3y': 278.23, '5y': 254.34}, {'code': '610004', 'name': '信达澳银中小盘混合', 2016: -13.13, 2017: 5.35, 2018: -15.15, 2019: 62.06, 2020: 61.94, 2021: 74.39, '3y': 346.4, '5y': 315.35}, {'code': '001702', 'name': '东方创新科技混合', 2016: -18.37, 2017: 4.76, 2018: -29.94, 2019: 56.03, 2020: 112.38, 2021: 36.08, '3y': 313.62, '5y': 206.96}, {'code': '001822', 'name': '华商智能生活灵活配置混合', 2016: -12.14, 2017: -7.64, 2018: -5.72, 2019: 34.97, 2020: 75.53, 2021: 55.01, '3y': 255.31, '5y': 209.35}, {'code': '162202', 'name': '泰达宏利周期混合', 2016: -4.49, 2017: 10.41, 2018: -11.6, 2019: 47.81, 2020: 68.76, 2021: 55.38, '3y': 266.63, '5y': 209.17}, {'code': '001959', 'name': '华商乐享互联灵活配置混合A', 2016: -13.29, 2017: -2.52, 2018: -39.91, 2019: 84.18, 2020: 79.96, 2021: 46.43, '3y': 325.51, '5y': 168.07}, {'code': '481015', 'name': '工银主题策略混合A', 2016: -30.42, 2017: 13.51, 2018: -37.54, 2019: 57.7, 2020: 129.57, 2021: 20.62, '3y': 272.4, '5y': 182.54}, {'code': '519642', 'name': '银河智造混合', 2016: -2.0, 2017: 33.98, 2018: -27.34, 2019: 60.06, 2020: 108.84, 2021: 27.38, '3y': 281.77, '5y': 308.65}, {'code': '000729', 'name': '建信中小盘先锋股票', 2016: -19.68, 2017: 7.14, 2018: -28.07, 2019: 29.19, 2020: 81.21, 2021: 59.42, '3y': 231.99, '5y': 167.57}, {'code': '001933', 'name': '华商新兴活力混合', 2016: 1.1, 2017: 6.73, 2018: -29.66, 2019: 34.78, 2020: 71.36, 2021: 56.82, '3y': 211.68, '5y': 168.72}, {'code': '000793', 'name': '工银高端制造股票', 2016: -26.28, 2017: 1.45, 2018: -41.81, 2019: 48.28, 2020: 128.81, 2021: 19.63, '3y': 240.19, '5y': 147.75}, {'code': '000541', 'name': '华商创新成长混合发起式', 2016: -25.71, 2017: -7.38, 2018: -29.02, 2019: 66.32, 2020: 101.4, 2021: 31.8, '3y': 306.87, '5y': 122.26}, {'code': '519095', 'name': '新华行业周期轮换混合', 2016: -9.21, 2017: 0.64, 2018: -16.35, 2019: 49.72, 2020: 84.12, 2021: 35.84, '3y': 258.57, '5y': 208.68}, {'code': '240022', 'name': '华宝资源优选混合A', 2016: 16.34, 2017: 24.56, 2018: -17.14, 2019: 31.18, 2020: 60.23, 2021: 73.2, '3y': 248.94, '5y': 270.49}, {'code': '206012', 'name': '鹏华价值精选股票', 2016: -11.35, 2017: 7.22, 2018: -32.48, 2019: 60.12, 2020: 87.68, 2021: 33.38, '3y': 269.67, '5y': 191.04}, {'code': '519196', 'name': '万家新兴蓝筹灵活配置混合', 2016: 12.66, 2017: 31.15, 2018: -14.06, 2019: 41.91, 2020: 82.3, 2021: 34.73, '3y': 198.81, '5y': 196.24}, {'code': '550015', 'name': '信诚至远A', 2016: 3.08, 2017: 2.0, 2018: -1.89, 2019: 13.1, 2020: 110.44, 2021: 27.26, '3y': 216.29, '5y': 203.73}, {'code': '550016', 'name': '信诚至远C', 2016: -3.48, 2017: 6.04, 2018: 39.08, 2019: 12.84, 2020: 109.72, 2021: 26.95, '3y': 213.54, '5y': 316.65}, {'code': '377240', 'name': '上投摩根新兴动力混合A', 2016: -19.81, 2017: 42.21, 2018: -35.65, 2019: 70.27, 2020: 78.24, 2021: 42.92, '3y': 280.22, '5y': 274.0}, {'code': '310368', 'name': '申万菱信竞争优势混合', 2016: -16.96, 2017: 21.78, 2018: -16.83, 2019: 43.0, 2020: 57.2, 2021: 68.72, '3y': 260.19, '5y': 145.56}, {'code': '530001', 'name': '建信恒久价值混合', 2016: -11.05, 2017: 5.24, 2018: -16.03, 2019: 48.98, 2020: 92.86, 2021: 19.37, '3y': 183.94, '5y': 118.59}, {'code': '040015', 'name': '华安动态灵活配置混合', 2016: -5.43, 2017: 13.2, 2018: -18.89, 2019: 68.59, 2020: 53.02, 2021: 69.46, '3y': 269.71, '5y': 196.76}, {'code': '000924', 'name': '宝盈先进制造混合A', 2016: -18.95, 2017: -2.01, 2018: -12.02, 2019: 71.05, 2020: 77.34, 2021: 31.77, '3y': 238.67, '5y': 207.72}, {'code': '001339', 'name': '兴银鼎新灵活配置混合', 2016: -8.91, 2017: 6.69, 2018: -20.92, 2019: 22.2, 2020: 60.88, 2021: 59.06, '3y': 189.06, '5y': 162.97}, {'code': '001487', 'name': '宝盈优势产业混合A', 2016: -13.08, 2017: 29.57, 2018: -22.13, 2019: 63.06, 2020: 33.84, 2021: 87.59, '3y': 296.01, '5y': 273.24}, {'code': '519702', 'name': '交银趋势混合A', 2016: 2.67, 2017: 21.76, 2018: -16.47, 2019: 46.16, 2020: 61.53, 2021: 63.81, '3y': 270.73, '5y': 290.2}, {'code': '001054', 'name': '工银新金融股票A', 2016: -5.84, 2017: 11.99, 2018: -20.28, 2019: 54.3, 2020: 103.97, 2021: 27.43, '3y': 275.0, '5y': 252.48}, {'code': '020023', 'name': '国泰事件驱动策略混合', 2016: -5.0, 2017: 33.71, 2018: -34.13, 2019: 65.98, 2020: 97.83, 2021: 23.99, '3y': 259.95, '5y': 251.03}, {'code': '202027', 'name': '南方高端装备灵活配置混合A', 2016: -11.18, 2017: 22.83, 2018: -19.56, 2019: 54.37, 2020: 72.42, 2021: 47.27, '3y': 255.88, '5y': 251.67}, {'code': '001616', 'name': '嘉实环保低碳股票', 2016: 16.5, 2017: 33.13, 2018: -32.95, 2019: 53.37, 2020: 113.67, 2021: 19.4, '3y': 302.47, '5y': 238.52}, {'code': '370024', 'name': '上投摩根核心优选混合', 2016: -28.67, 2017: 38.9, 2018: -32.18, 2019: 61.25, 2020: 78.26, 2021: 40.48, '3y': 237.9, '5y': 235.2}, {'code': '165520', 'name': '信诚中证800有色指数(LOF)A', 2016: -2.99, 2017: 24.49, 2018: -20.9, 2019: 24.2, 2020: 39.61, 2021: 77.99, '3y': 171.59, '5y': 132.48}, {'code': '001410', 'name': '信达澳银新能源产业股票', 2016: -5.91, 2017: 39.27, 2018: -15.81, 2019: 94.11, 2020: 59.88, 2021: 50.89, '3y': 331.96, '5y': 432.14}, {'code': '377530', 'name': '上投摩根行业轮动混合A', 2016: -25.2, 2017: 31.96, 2018: -27.25, 2019: 56.89, 2020: 72.47, 2021: 47.11, '3y': 253.57, '5y': 206.65}, {'code': '001279', 'name': '中海积极增利混合', 2016: -12.41, 2017: 17.58, 2018: -30.01, 2019: 66.91, 2020: 64.18, 2021: 55.6, '3y': 285.77, '5y': 219.33}, {'code': '001471', 'name': '融通新能源灵活配置混合', 2016: 3.59, 2017: 5.75, 2018: -15.79, 2019: 57.36, 2020: 60.58, 2021: 44.75, '3y': 238.12, '5y': 213.8}, {'code': '001158', 'name': '工银新材料新能源股票', 2016: -24.01, 2017: 6.96, 2018: -28.32, 2019: 42.72, 2020: 83.58, 2021: 37.88, '3y': 222.26, '5y': 158.24}, {'code': '519909', 'name': '华安安顺混合', 2016: -4.16, 2017: 12.38, 2018: -11.12, 2019: 28.08, 2020: 83.93, 2021: 39.37, '3y': 215.44, '5y': 242.87}, {'code': '519918', 'name': '华夏兴和混合', 2016: -10.42, 2017: 6.12, 2018: -8.46, 2019: 43.78, 2020: 65.47, 2021: 48.57, '3y': 224.33, '5y': 181.5}, {'code': '001809', 'name': '中信建投智信物联网A', 2016: -1.2, 2017: 13.76, 2018: -30.34, 2019: 71.39, 2020: 54.97, 2021: 51.73, '3y': 259.63, '5y': 216.77}, {'code': '002213', 'name': '中海顺鑫灵活配置混合', 2016: 0.0, 2017: 3.3, 2018: -20.86, 2019: 52.68, 2020: 77.23, 2021: 28.46, '3y': 208.6, '5y': 175.46}, {'code': '519195', 'name': '万家品质', 2016: -5.64, 2017: 31.55, 2018: -16.62, 2019: 47.74, 2020: 70.71, 2021: 33.23, '3y': 166.4, '5y': 197.4}, {'code': '001811', 'name': '中欧明睿新常态混合A', 2016: -8.0, 2017: 35.98, 2018: -11.03, 2019: 56.51, 2020: 57.08, 2021: 50.55, '3y': 236.43, '5y': 297.14}, {'code': '540003', 'name': '汇丰晋信动态策略混合A', 2016: -9.24, 2017: 19.18, 2018: -17.32, 2019: 44.65, 2020: 71.75, 2021: 47.23, '3y': 248.55, '5y': 233.94}, {'code': '002168', 'name': '嘉实智能汽车股票', 2016: 24.0, 2017: 20.16, 2018: -24.83, 2019: 65.62, 2020: 93.91, 2021: 23.88, '3y': 307.69, '5y': 268.57}, {'code': '001808', 'name': '银华互联网主题灵活配置混合', 2016: -22.21, 2017: 17.31, 2018: -30.95, 2019: 60.93, 2020: 96.63, 2021: 25.6, '3y': 264.86, '5y': 198.44}, {'code': '375010', 'name': '上投摩根中国优势混合', 2016: -10.93, 2017: 26.18, 2018: -8.78, 2019: 57.81, 2020: 57.79, 2021: 41.82, '3y': 213.58, '5y': 167.56}, {'code': '000584', 'name': '新华鑫益灵活配置混合', 2016: -5.47, 2017: 13.75, 2018: -6.43, 2019: 47.19, 2020: 72.68, 2021: 34.42, '3y': 229.26, '5y': 276.3}, {'code': '519181', 'name': '万家和谐增长混合', 2016: -6.79, 2017: 16.92, 2018: -16.31, 2019: 52.14, 2020: 69.82, 2021: 31.41, '3y': 189.5, '5y': 141.01}, {'code': '163807', 'name': '中银优选灵活配置混合A', 2016: -18.07, 2017: 28.58, 2018: -11.14, 2019: 55.4, 2020: 48.13, 2021: 16.74, '3y': 116.52, '5y': 114.35}, {'code': '000242', 'name': '景顺长城策略精选灵活配置混合', 2016: 0.36, 2017: 6.18, 2018: -13.61, 2019: 44.03, 2020: 63.21, 2021: 51.48, '3y': 238.49, '5y': 139.45}, {'code': '000547', 'name': '建信健康民生混合', 2016: -5.38, 2017: 9.52, 2018: -23.89, 2019: 68.27, 2020: 65.8, 2021: 40.02, '3y': 261.99, '5y': 228.14}, {'code': '519997', 'name': '长信银利精选混合', 2016: -3.16, 2017: 7.2, 2018: -4.93, 2019: 24.96, 2020: 45.57, 2021: 19.25, '3y': 90.51, '5y': 84.71}, {'code': '002296', 'name': '长城行业轮动混合A', 2016: 2.0, 2017: 4.31, 2018: 0.68, 2019: 13.38, 2020: 19.34, 2021: 107.18, '3y': 181.61, '5y': 193.82}, {'code': '001753', 'name': '红土创新新兴产业混合', 2016: -16.67, 2017: 10.85, 2018: -26.6, 2019: 27.1, 2020: 71.49, 2021: 47.01, '3y': 186.77, '5y': 152.4}, {'code': '160421', 'name': '华安智增精选混合', 2016: -3.23, 2017: -1.35, 2018: -21.15, 2019: 75.75, 2020: 54.97, 2021: 51.75, '3y': 281.25, '5y': 211.1}, {'code': '040035', 'name': '华安逆向策略混合', 2016: -3.84, 2017: 1.1, 2018: -20.33, 2019: 65.53, 2020: 81.0, 2021: 26.86, '3y': 270.88, '5y': 205.2}, {'code': '002537', 'name': '平安安盈灵活配置混合', 2016: 0.3, 2017: 1.79, 2018: 1.18, 2019: 22.81, 2020: 70.87, 2021: 39.89, '3y': 196.43, '5y': 199.95}, {'code': '450004', 'name': '国富深化价值混合', 2016: -28.59, 2017: 23.89, 2018: -14.88, 2019: 51.57, 2020: 81.6, 2021: 26.88, '3y': 221.93, '5y': 203.74}, {'code': '519089', 'name': '新华优选成长混合', 2016: -13.82, 2017: -3.76, 2018: -3.32, 2019: 43.77, 2020: 66.04, 2021: 31.66, '3y': 164.36, '5y': 123.02}, {'code': '000803', 'name': '工银研究精选股票', 2016: -19.01, 2017: 12.4, 2018: -25.21, 2019: 54.81, 2020: 88.84, 2021: 21.46, '3y': 209.19, '5y': 196.65}, {'code': '001366', 'name': '金鹰产业整合混合', 2016: -26.14, 2017: 4.29, 2018: -29.69, 2019: 48.08, 2020: 91.73, 2021: 23.95, '3y': 200.78, '5y': 144.6}, {'code': '000756', 'name': '建信潜力新蓝筹股票', 2016: -7.21, 2017: 15.17, 2018: -26.8, 2019: 32.28, 2020: 65.21, 2021: 47.7, '3y': 197.5, '5y': 171.69}, {'code': '200015', 'name': '长城优化升级混合A', 2016: -12.66, 2017: 19.41, 2018: -18.16, 2019: 45.38, 2020: 58.58, 2021: 43.77, '3y': 212.49, '5y': 212.22}, {'code': '001677', 'name': '中银战略新兴产业股票A', 2016: 4.4, 2017: 27.49, 2018: -24.34, 2019: 57.6, 2020: 66.16, 2021: 40.01, '3y': 235.33, '5y': 257.06}, {'code': '720001', 'name': '财通价值动量混合', 2016: -18.59, 2017: 15.39, 2018: -16.63, 2019: 70.96, 2020: 51.29, 2021: 61.82, '3y': 307.7, '5y': 207.97}, {'code': '001718', 'name': '工银物流产业股票', 2016: 10.0, 2017: 21.82, 2018: -14.78, 2019: 50.09, 2020: 76.37, 2021: 25.37, '3y': 221.46, '5y': 258.22}, {'code': '519091', 'name': '新华泛资源优势混合', 2016: 6.67, 2017: 18.57, 2018: -9.95, 2019: 40.26, 2020: 67.65, 2021: 29.97, '3y': 192.57, '5y': 270.13}, {'code': '001827', 'name': '富国研究优选沪港深混合', 2016: 8.2, 2017: 24.21, 2018: -25.89, 2019: 43.17, 2020: 78.4, 2021: 29.64, '3y': 200.09, '5y': 204.81}, {'code': '582003', 'name': '东吴配置优化混合A', 2016: -0.43, 2017: 20.33, 2018: -24.87, 2019: 45.58, 2020: 38.35, 2021: 65.62, '3y': 182.51, '5y': 157.06}, {'code': '000390', 'name': '华商优势行业混合', 2016: -0.95, 2017: 6.28, 2018: -7.94, 2019: 39.26, 2020: 22.3, 2021: 27.29, '3y': 88.91, '5y': 78.43}, {'code': '001009', 'name': '上投摩根安全战略股票', 2016: -19.27, 2017: 15.34, 2018: -30.34, 2019: 72.28, 2020: 79.43, 2021: 21.25, '3y': 233.43, '5y': 184.8}, {'code': '001070', 'name': '建信信息产业股票', 2016: -13.71, 2017: 18.59, 2018: -30.14, 2019: 63.83, 2020: 70.55, 2021: 35.75, '3y': 261.58, '5y': 208.14}, {'code': '750001', 'name': '安信灵活配置混合', 2016: -15.19, 2017: 10.27, 2018: -12.83, 2019: 55.23, 2020: 70.8, 2021: 26.84, '3y': 215.57, '5y': 122.02}, {'code': '001480', 'name': '财通成长优选混合', 2016: -25.46, 2017: 15.18, 2018: -23.06, 2019: 72.93, 2020: 48.96, 2021: 59.41, '3y': 299.6, '5y': 241.72}, {'code': '690011', 'name': '民生加银积极成长混合发起式', 2016: -18.04, 2017: 9.04, 2018: -16.15, 2019: 48.75, 2020: 69.77, 2021: 28.12, '3y': 211.51, '5y': 194.21}, {'code': '000308', 'name': '建信创新中国混合', 2016: -0.95, 2017: 13.6, 2018: -20.98, 2019: 49.44, 2020: 64.07, 2021: 38.82, '3y': 242.81, '5y': 198.76}, {'code': '290008', 'name': '泰信发展主题混合', 2016: -13.95, 2017: 7.31, 2018: -14.98, 2019: 48.38, 2020: 54.79, 2021: 40.35, '3y': 200.68, '5y': 176.43}, {'code': '673060', 'name': '西部利得景瑞灵活配置混合A', 2016: -0.6, 2017: -2.72, 2018: -18.72, 2019: 72.26, 2020: 63.38, 2021: 44.19, '3y': 281.67, '5y': 206.1}, {'code': '165313', 'name': '建信优势动力混合(LOF)', 2016: -8.76, 2017: 4.8, 2018: -22.08, 2019: 52.67, 2020: 74.72, 2021: 23.89, '3y': 214.5, '5y': 171.85}, {'code': '288001', 'name': '华夏经典混合', 2016: -9.19, 2017: 2.15, 2018: -4.22, 2019: 26.17, 2020: 66.57, 2021: 42.91, '3y': 188.88, '5y': 152.31}, {'code': '161611', 'name': '融通内需驱动混合', 2016: -25.98, 2017: 7.25, 2018: -13.96, 2019: 61.16, 2020: 48.97, 2021: 34.93, '3y': 200.57, '5y': 172.23}, {'code': '519115', 'name': '浦银安盛红利精选混合', 2016: -19.65, 2017: 11.29, 2018: -25.09, 2019: 65.54, 2020: 50.97, 2021: 45.46, '3y': 227.82, '5y': 194.42}, {'code': '001924', 'name': '华夏国企改革混合', 2016: -13.45, 2017: 13.23, 2018: -29.1, 2019: 49.71, 2020: 71.43, 2021: 21.96, '3y': 178.76, '5y': 142.01}, {'code': '001236', 'name': '博时丝路主题股票A', 2016: -11.81, 2017: 14.5, 2018: -18.24, 2019: 49.08, 2020: 76.58, 2021: 19.99, '3y': 198.27, '5y': 204.68}, {'code': '460001', 'name': '华泰柏瑞盛世中国混合', 2016: -14.35, 2017: 18.2, 2018: -9.27, 2019: 39.44, 2020: 68.28, 2021: 6.08, '3y': 94.96, '5y': 64.92}, {'code': '002556', 'name': '博时丝路主题股票C', 2016: 11.28, 2017: 14.04, 2018: -18.74, 2019: 48.48, 2020: 75.69, 2021: 19.55, '3y': 194.04, '5y': 198.11}, {'code': '002844', 'name': '金鹰多元策略混合', 2016: -4.81, 2017: 9.89, 2018: -16.64, 2019: 48.51, 2020: 49.29, 2021: 41.48, '3y': 206.58, '5y': 173.47}, {'code': '001267', 'name': '泰达宏利蓝筹混合', 2016: -26.64, 2017: 28.49, 2018: -25.65, 2019: 52.63, 2020: 56.58, 2021: 35.32, '3y': 197.31, '5y': 201.09}, {'code': '001887', 'name': '中欧价值智选混合E', 2016: 3.55, 2017: -4.88, 2018: -6.37, 2019: 46.54, 2020: 60.92, 2021: 38.12, '3y': 219.1, '5y': 155.78}, {'code': '166019', 'name': '中欧价值智选混合A', 2016: -5.73, 2017: -4.8, 2018: -6.63, 2019: 46.32, 2020: 60.94, 2021: 38.12, '3y': 218.48, '5y': 153.85}, {'code': '550002', 'name': '中信保诚精萃成长混合', 2016: -12.96, 2017: 13.65, 2018: -14.42, 2019: 18.71, 2020: 41.91, 2021: 30.11, '3y': 90.34, '5y': 62.63}]
# 最近一年，两年，三年，五年排行榜前五百名的基金列表
print(f"funds: {len(funds)}\tfunds_v2: {len(funds_v2)}")
sorted_3y = sorted(funds, key=lambda x: x['3y'], reverse=True)
# sorted_5y = sorted(funds, key=lambda x: x['5y'], reverse=True)
sorted_3y = get_fund_detail_list(sorted_3y)
for i in sorted_3y:
    print(i)
    print(f"http://fundf10.eastmoney.com/jjjl_{i['code']}.html")


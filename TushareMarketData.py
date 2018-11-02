#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建时间：Fri Nov  2 09:45:29 2018
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder 3.2.6
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：TushareMarketData.py
"""

import tushare as ts
pro = ts.pro_api()


class TushareMarketData(object):
    #  行情数据
    def daily(self):
        '''日线行情
        更新时间：交易日每天15点～16点之间
        描述：获取股票行情数据，或通过通用行情接口获取数据，包含了前后复权数据．
        输入参数
        ts_code	str	N	股票代码（二选一）
        trade_date	str	N	交易日期（二选一）
        start_date	str	N	开始日期(YYYYMMDD)
        end_date	str	N	结束日期(YYYYMMDD)
        注：日期都填YYYYMMDD格式，比如20181010
        输出参数
        ts_code	str	股票代码
        trade_date	str	交易日期
        open	float	开盘价
        high	float	最高价
        low	float	最低价
        close	float	收盘价
        pre_close	float	昨收价
        change	float	涨跌额
        pct_change	float	涨跌幅
        vol	float	成交量 （手）
        amount	float	成交额 （千元）
        '''
        data = pro.daily(ts_code='002027.SZ')
        return data

    def adj_factor(self):
        '''复权因子
        更新时间：早上9点30分
        描述：获取股票复权因子，可提取单只股票全部历史复权因子，也可以提取单日全部股票的复权因子。
        输入参数
        ts_code	str	Y	股票代码
        trade_date	str	N	交易日期(YYYYMMDD，下同)
        start_date	str	N	开始日期
        end_date	str	N	结束日期
        注：日期都填YYYYMMDD格式，比如20181010
        输出参数
        ts_code	str	股票代码
        trade_date	str	交易日期
        adj_factor	float	复权因子
        start_date	str	开始日期
        end_date	str	结束日期
        '''
        data = pro.adj_factor(ts_code='002027.SZ', trade_date='')
        return data

    def suspend(self):
        '''停复牌信息
        更新时间：不定期
        描述：获取股票每日停复牌信息
        输入参数
        ts_code	str	N	股票代码(三选一)
        suspend_date	str	N	停牌日期(三选一)
        resume_date	str	N	复牌日期(三选一)
        输出参数
        ts_code	str	股票代码
        suspend_date	str	停牌日期
        resume_date	str	复牌日期
        ann_date	str	公告日期
        suspend_reason	str	停牌原因
        reason_type	str	停牌原因类别
        '''
        data = pro.suspend(ts_code='002027.SZ', suspend_date='', resume_date='', fiedls='')
        return data

    def daily_basic(self):
        '''每日指标
        更新时间：交易日每日15点～17点之间
        描述：获取全部股票每日重要的基本面指标，可用于选股分析、报表展示等。
        输入参数
        ts_code	str	Y	股票代码（二选一）
        trade_date	str	N	交易日期 （二选一）
        start_date	str	N	开始日期(YYYYMMDD)
        end_date	str	N	结束日期(YYYYMMDD)
        注：日期都填YYYYMMDD格式，比如20181010
        输出参数
        ts_code	str	TS股票代码
        trade_date	str	交易日期
        close	float	当日收盘价
        turnover_rate	float	换手率
        turnover_rate_f	float	换手率（自由流通股）
        volume_ratio	float	量比
        pe	float	市盈率（总市值/净利润）
        pe_ttm	float	市盈率（TTM）
        pb	float	市净率（总市值/净资产）
        ps	float	市销率
        ps_ttm	float	市销率（TTM）
        total_share	float	总股本 （万）
        float_share	float	流通股本 （万）
        free_share	float	自由流通股本 （万）
        total_mv	float	总市值 （万元）
        circ_mv	float	流通市值（万元）
        '''
        data = pro.daily_basic(ts_code='002027.SZ', trade_date='20181101')
        return data

    def pro_bar(self):
        '''通用行情接口
        更新时间：股票和指数通常在15点～17点之间，数字货币实时更新，具体请参考各接口文档明细。
        描述：目前整合了股票（未复权、前复权、后复权）、指数、数字货币的行情数据，未来还将整合包括期货期权、基金、外汇在内的所有交易行情数据，同时提供分钟数据。
        输入参数
        ts_code	str	Y	证券代码
        pro_api	str	N	pro版api对象
        start_date	str	N	开始日期 (格式：YYYYMMDD)
        end_date	str	N	结束日期 (格式：YYYYMMDD)
        asset	str	Y	资产类别：E股票 I沪深指数 C数字货币 F期货 O期权，默认E
        adj	str	N	复权类型(只针对股票)：None未复权 qfq前复权 hfq后复权 , 默认None
        freq	str	Y	数据频度 ：1MIN表示1分钟（1/5/15/30/60分钟） D日线 ，默认D
        ma	list	N	均线，支持任意合理int数值
        '''
        data = ts.pro_bar(pro_api=pro, ts_code='002027.SZ', adj='qfq', start_date='20180101', end_date='20181011')
        # 取上证指数行情数据
        sh = ts.pro_bar(pro_api=pro, ts_code='000001.SH', asset='I', start_date='20180101', end_date='20181011')
        # 均线
        ma = ts.pro_bar(pro_api=pro, ts_code='000001.SZ', start_date='20180101', end_date='20181011', ma=[5, 20, 50])
        return data, sh, ma


'''
debug = TushareMarketData()
daily = debug.daily()
adj = debug.adj_factor()
suspend = debug.suspend()
basic = debug.daily_basic()
pro_bar = debug.pro_bar()
'''

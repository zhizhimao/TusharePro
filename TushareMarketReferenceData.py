#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建时间：Fri Nov  2 13:46:33 2018
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder 3.2.6
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：file.py
"""

import tushare as ts
pro = ts.pro_api()


class TushareMarketReferenceData(object):
    # 市场参考数据
    def moneyflow_hsgt(self):
        '''沪深港通资金流向
        描述：获取沪股通、深股通、港股通每日资金流向数据
        输入参数
        trade_date	str	N	交易日期 (二选一)
        start_date	str	N	开始日期 (二选一)
        end_date	str	N	结束日期
        输出参数
        trade_date	str	交易日期
        ggt_ss	str	港股通（上海）
        ggt_sz	str	港股通（深圳）
        hgt	str	沪股通（百万元）
        sgt	str	深股通（百万元）
        north_money	str	北向资金（百万元）
        south_money	str	南向资金（百万元）
        '''
        data = pro.moneyflow_hsgt(start_date='20180125', end_date='20180808')
        return data

    def hsgt_top10(self):
        '''沪深股通十大成交股
        描述：获取沪股通、深股通每日前十大成交详细数据
        输入参数
        ts_code	str	N	股票代码（二选一）
        trade_date	str	N	交易日期（二选一）
        start_date	str	N	开始日期
        end_date	str	N	结束日期
        market_type	str	N	市场类型（1：沪市 3：深市）
        输出参数
        trade_date	str	交易日期
        ts_code	str	股票代码
        name	str	股票名称
        close	float	收盘价
        change	float	涨跌额
        rank	int	资金排名
        market_type	str	市场类型（1：沪市 3：深市）
        amount	float	成交金额（元）
        net_amount	float	净成交金额（元）
        buy	float	买入金额（元）
        sell	float	卖出金额（元）
        '''
        data = pro.hsgt_top10(trade_date='20180725', market_type='1')
        return data

    def ggt_top10(self):
        '''港股通十大成交股
        描述：获取港股通每日成交数据，其中包括沪市、深市详细数据
        输入参数
        ts_code	str	N	股票代码（二选一）
        trade_date	str	N	交易日期（二选一）
        start_date	str	N	开始日期
        end_date	str	N	结束日期
        market_type	str	N	市场类型 2：港股通（沪） 4：港股通（深）
        输出参数
        trade_date	str	交易日期
        ts_code	str	股票代码
        name	str	股票名称
        close	float	收盘价
        p_change	float	涨跌幅
        rank	str	资金排名
        market_type	str	市场类型 2：港股通（沪） 4：港股通（深）
        amount	float	累计成交金额（元）
        net_amount	float	净买入金额（元）
        sh_amount	float	沪市成交金额（元）
        sh_net_amount	float	沪市净买入金额（元）
        sh_buy	float	沪市买入金额（元）
        sh_sell	float	沪市卖出金额
        sz_amount	float	深市成交金额（元）
        sz_net_amount	float	深市净买入金额（元）
        sz_buy	float	深市买入金额（元）
        sz_sell	float	深市卖出金额（元）
        '''
        data = pro.ggt_top10(trade_date='20180727')
        return data

    def margin(self):
        '''融资融券交易汇总
        描述：获取融资融券每日交易汇总数据
        输入参数
        trade_date	str	Y	交易日期
        exchange_id	str	N	交易所代码
        输出参数
        trade_date	str	交易日期
        exchange_id	str	交易所代码（SSE上交所SZSE深交所）
        rzye	float	融资余额(元)
        rzmre	float	融资买入额(元)
        rzche	float	融资偿还额(元)
        rqye	float	融券余额(元)
        rqmcl	float	融券卖出量(股,份,手)
        rzrqye	float	融资融券余额(元)
        '''
        data = pro.margin(trade_date='20180802')
        return data

    def margin_detail(self):
        '''融资融券交易明细
        描述：获取沪深两市每日融资融券明细
        输入参数
        trade_date	str	Y	交易日期
        ts_code	str	N	TS代码
        输出参数
        trade_date	str	交易日期
        ts_code	str	TS股票代码
        rzye	float	融资余额(元)
        rqye	float	融券余额(元)
        rzmre	float	融资买入额(元)
        rqyl	float	融券余量（手）
        rzche	float	融资偿还额(元)
        rqchl	float	融券偿还量(手)
        rqmcl	float	融券卖出量(股,份,手)
        rzrqye	float	融资融券余额(元)
        说明：
        本报表基于证券公司报送的融资融券余额数据汇总生成，其中：
        本日融资余额(元)=前日融资余额＋本日融资买入-本日融资偿还额
        本日融券余量(股)=前日融券余量＋本日融券卖出量-本日融券买入量-本日现券偿还量
        本日融券余额(元)=本日融券余量×本日收盘价
        本日融资融券余额(元)=本日融资余额＋本日融券余额
        2014年9月22日起，“融资融券交易总量”数据包含调出标的证券名单的证券的融资融券余额。
        '''
        data = pro.margin_detail(trade_date='20180802')
        return data

    def top10_holders(self):
        '''前十大股东
        描述：获取上市公司前十大股东数据，包括持有数量和比例等信息。
        输入参数
        ts_code	str	Y	TS代码
        period	str	N	报告期
        ann_date	str	N	公告日期
        strat_date	str	N	报告期开始日期
        end_date	str	N	报告期结束日期
        注：一次取100行记录
        输出参数
        ts_code	str	TS股票代码
        ann_date	str	公告日期
        end_date	str	报告期
        holder_name	str	股东名称
        hold_amount	float	持有数量（股）
        hold_ratio	float	持有比例
        '''
        data = pro.top10_holders(ts_code='600000.SH', start_date='20170101', end_date='20171231')
        return data

    def top_list(self):
        '''龙虎榜每日明细
        描述：龙虎榜每日交易明细
        数据历史： 2005年至今
        限量：单次最大10000
        输入参数
        trade_date	str	Y	交易日期
        ts_code	str	N	股票代码
        输出参数
        trade_date	str	Y	交易日期
        ts_code	str	Y	TS代码
        name	str	Y	名称
        close	float	Y	收盘价
        pct_change	float	Y	涨跌幅
        turnover_rate	float	Y	换手率
        amount	float	Y	总成交额
        l_sell	float	Y	龙虎榜卖出额
        l_buy	float	Y	龙虎榜买入额
        l_amount	float	Y	龙虎榜成交额
        net_amount	float	Y	龙虎榜净买入额
        net_rate	float	Y	龙虎榜净买额占比
        amount_rate	float	Y	龙虎榜成交额占比
        float_values	float	Y	当日流通市值
        reason	str	Y	上榜理由
        '''
        data = pro.top_list(trade_date='20180928')
        return data

    def top_inst(self):
        '''龙虎榜机构明细
        描述：龙虎榜机构成交明细
        限量：单次最大10000
        输入参数
        trade_date	str	Y	交易日期
        ts_code	str	N	TS代码
        输出参数
        trade_date	str	Y	交易日期
        ts_code	str	Y	TS代码
        exalter	str	Y	营业部名称
        buy	float	Y	买入额（万）
        buy_rate	float	Y	买入占总成交比例
        sell	float	Y	卖出额（万）
        sell_rate	float	Y	卖出占总成交比例
        net_buy	float	Y	净成交额（万）
        '''
        data = pro.top_inst(trade_date='20180928')
        return data

    def pledge_stat(self):
        '''股权质押统计数据
        描述：获取股权质押统计数据
        限量：单次最大1000
        输入参数
        ts_code	str	Y	股票代码
        输出参数
        ts_code	str	Y	TS代码
        end_date	str	Y	截至日期
        pledge_count	int	Y	质押次数
        unrest_pledge	float	Y	无限售股质押数量（万）
        rest_pledge	float	Y	限售股份质押数量（万）
        total_share	float	Y	总股本
        pledge_ratio	float	Y	质押比例
        '''
        data = pro.pledge_stat(ts_code='000014.SZ')
        return data

    def pledge_detail(self):
        '''股权质押明细
        描述：获取股权质押明细数据
        限量：单次最大1000
        输入参数
        ts_code	str	Y	股票代码
        输出参数
        ts_code	str	Y	TS股票代码
        ann_date	str	Y	公告日期
        holder_name	str	Y	股东名称
        pledge_amount	float	Y	质押数量
        start_date	str	Y	质押开始日期
        end_date	str	Y	质押结束日期
        is_release	str	Y	是否已解押
        release_date	str	Y	解押日期
        pledgor	str	Y	质押方
        holding_amount	float	Y	持股总数
        pledged_amount	float	Y	质押总数
        p_total_ratio	float	Y	本次质押占总股本比例
        h_total_ratio	float	Y	持股总数占总股本比例
        is_buyback	str	Y	是否回购
        '''
        data = pro.pledge_detail(ts_code='000014.SZ')
        return data

    def repurchase(self):
        '''股票回购
        描述：获取上市公司回购股票数据
        输入参数
        ann_date	str	N	公告日期（任意填参数，如果都不填，单次默认返回2000条）
        start_date	str	N	公告开始日期
        end_date	str	N	公告结束日期
        以上日期格式为：YYYYMMDD，比如20181010
        输出参数
        ts_code	str	Y	TS代码
        ann_date	str	Y	公告日期
        end_date	str	Y	截止日期
        proc	str	Y	进度
        exp_date	str	Y	过期日期
        vol	float	Y	回购数量
        amount	float	Y	回购金额
        high_limit	float	Y	回购最高价
        low_limit	float	Y	回购最低价
        '''
        data = pro.repurchase(ann_date='', start_date='20180101', end_date='20180510')
        return data

    def concept(self):
        '''概念股分类
        描述：获取概念股分类，目前只有ts一个来源，未来将逐步增加来源
        输入参数
        src	str	N	来源，默认为ts
        输出参数
        code	str	Y	概念分类ID
        name	str	Y	概念分类名称
        src	str	Y	来源
        '''
        data = pro.concept()
        return data

    def concept_detail(self):
        '''概念股列表
        描述：获取概念股分类明细数据
        输入参数
        id	str	Y	概念分类ID （id来自概念股分类接口）
        输出参数
        id	str	Y	概念代码
        ts_code	str	Y	股票代码
        name	str	Y	股票名称
        in_date	str	N	纳入日期
        out_date	str	N	剔除日期
        '''
        data = pro.concept_detail(id='0', fields='ts_code,name')
        return data


'''
debug = TushareMarketReferenceData()
moneyflow_hsgt = debug.moneyflow_hsgt()
hsgt_top10 = debug.hsgt_top10()
ggt_top10 = debug.ggt_top10()
margin = debug.margin()
margin_detail = debug.margin_detail()
top10_holders = debug.top10_holders()
top_list = debug.top_list()
top_inst = debug.top_inst()
pledge_stat = debug.pledge_stat()
pledge_detail = debug.pledge_detail()
repurchase = debug.repurchase()  # 600
concept = debug.concept()
concept_detail = debug.concept_detail()
'''

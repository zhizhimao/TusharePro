#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建时间：Fri Nov  2 16:50:38 2018
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder 3.2.6
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：TushareFundData.py
"""

import tushare as ts
pro = ts.pro_api()


class TushareFundData(object):
    #  基金数据
    def fund_basic(self):
        '''公募基金列表
        描述：获取公募基金数据列表，包括场内和场外基金
        输入参数
        market	str	N	交易市场: E场内 O场外（默认E）
        输出参数
        ts_code	str	Y	基金代码
        name	str	Y	简称
        management	str	Y	管理人
        custodian	str	Y	托管人
        fund_type	str	Y	投资类型
        found_date	str	Y	成立日期
        due_date	str	Y	到期日期
        list_date	str	Y	上市时间
        issue_date	str	Y	发行日期
        delist_date	str	Y	退市日期
        issue_amount	float	Y	发行份额(亿)
        m_fee	float	Y	管理费
        c_fee	float	Y	托管费
        duration_year	float	Y	存续期
        p_value	float	Y	面值
        min_amount	float	Y	起点金额(万元)
        exp_return	float	Y	预期收益率
        benchmark	str	Y	业绩比较基准
        status	str	Y	存续状态D摘牌 I发行 L已上市
        invest_type	str	Y	投资风格
        type	str	Y	基金类型
        trustee	str	Y	受托人
        purc_startdate	str	Y	日常申购起始日
        redm_startdate	str	Y	日常赎回起始日
        market	str	Y	E场内O场外
        '''
        data = pro.fund_basic(market='E')
        return data

    def fund_company(self):
        '''公募基金公司
        描述：获取公募基金管理人列表
        输出参数
        name	str	Y	基金公司名称
        shortname	str	Y	简称
        short_enname	str	N	英文缩写
        province	str	Y	省份
        city	str	Y	城市
        address	str	Y	注册地址
        phone	str	Y	电话
        office	str	Y	办公地址
        website	str	Y	公司网址
        chairman	str	Y	法人代表
        manager	str	Y	总经理
        reg_capital	float	Y	注册资本
        setup_date	str	Y	成立日期
        end_date	str	Y	公司终止日期
        employees	float	Y	员工总数
        main_business	str	Y	主要产品及业务
        org_code	str	Y	组织机构代码
        credit_code	str	Y	统一社会信用代码
        '''
        data = pro.fund_company()
        return data

    def fund_nav(self):
        '''公募基金净值
        描述：获取公募基金净值数据
        输入参数
        ts_code	str	N	TS基金代码 （二选一）
        end_date	str	N	净值日期 （二选一）
        输出参数
        ts_code	str	Y	TS代码
        ann_date	str	Y	公告日期
        end_date	str	Y	截止日期
        unit_nav	float	Y	单位净值
        accum_nav	float	Y	累计净值
        accum_div	float	Y	累计分红
        net_asset	float	Y	资产净值
        total_netasset	float	Y	合计资产净值
        adj_nav	float	Y	复权单位净值
        '''
        data = pro.fund_nav(ts_code='165509.SZ')
        return data

    def fund_div(self):
        '''公募基金分红
        描述：获取公募基金分红数据
        输入参数
        ann_date	str	N	公告日（以下参数四选一）
        ex_date	str	N	公告日
        pay_date	str	N	公告日
        ts_code	str	N	公告日
        输出参数
        ts_code	str	Y	TS代码
        ann_date	str	Y	公告日期
        imp_anndate	str	Y	分红实施公告日
        base_date	str	Y	分配收益基准日
        div_proc	str	Y	方案进度
        record_date	str	Y	权益登记日
        ex_date	str	Y	除息日
        pay_date	str	Y	派息日
        earpay_date	str	Y	收益支付日
        net_ex_date	str	Y	净值除权日
        div_cash	float	Y	每股派息(元)
        base_unit	float	Y	基准基金份额(万份)
        ear_distr	float	Y	可分配收益(元)
        ear_amount	float	Y	收益分配金额(元)
        account_date	str	Y	红利再投资到账日
        base_year	str	Y	份额基准年度
        '''
        data = pro.fund_div(ann_date='20181018')
        return data

    def fund_portfolio(self):
        '''公募基金持仓数据
        描述：获取公募基金持仓数据，季度更新
        输入参数
        ts_code	str	Y	基金代码
        输出参数
        ts_code	str	Y	TS基金代码
        ann_date	str	Y	公告日期
        end_date	str	Y	截止日期
        symbol	str	Y	股票代码
        mkv	float	Y	持有股票市值(元)
        amount	float	Y	持有股票数量（股）
        stk_mkv_ratio	float	Y	占股票市值比
        stk_float_ratio	float	Y	占流通股本比例
        '''
        data = pro.fund_portfolio(ts_code='001753.OF')
        return data

    def fund_daily(self):
        '''场内基金日线行情
        描述：获取场内基金日线行情，类似股票日行情
        更新：每日收盘后2小时内
        限量：单次最大800行记录，总量不限制
        输入参数
        ts_code	str	N	基金代码（二选一）
        trade_date	str	N	交易日期（二选一）
        start_date	str	N	开始日期
        end_date	str	N	结束日期
        输出参数
        ts_code	str	Y	TS代码
        trade_date	str	Y	交易日期
        open	float	Y	开盘价(元)
        high	float	Y	最高价(元)
        low	float	Y	最低价(元)
        close	float	Y	收盘价(元)
        pre_close	float	Y	昨收盘价(元)
        change	float	Y	涨跌额(元)
        pct_change	float	Y	涨跌幅(%)
        vol	float	Y	成交量(手)
        amount	float	Y	成交额(千元)
        '''
        data = pro.fund_daily(ts_code='150018.SZ', start_date='20180101', end_date='20181029')
        return data


'''
debug = TushareFundData()
fund_basic = debug.fund_basic()
fund_company = debug.fund_company()
fund_nav = debug.fund_nav()
fund_div = debug.fund_div()
fund_portfolio = debug.fund_portfolio()  # 1000
fund_daily = debug.fund_daily()  # 500
'''

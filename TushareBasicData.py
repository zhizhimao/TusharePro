# -*- coding: utf-8 -*-
"""
创建时间：Sun Aug  5 09:42:55 2018
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：TushareBasicData.py
"""

import tushare as ts
pro = ts.pro_api()


class TushareBasicData(object):
    #  基础数据
<<<<<<< HEAD
    def stock_basic(self):
=======
    def stock_basic():
>>>>>>> d9010ada373c24e3c40422f7411815f7c3353c6d
        '''股票列表
        描述：获取基础信息数据，包括股票代码、名称、上市日期、退市日期等
        输入参数
        is_hs	str	N	是否沪深港通标的，N否 H沪股通 S深股通
        list_status	str	N	上市状态： L上市 D退市 P暂停上市
        exchange_id	str	N	交易所 SSE上交所 SZSE深交所 HKEX港交所
        输出参数
        ts_code	str	TS代码
        symbol	str	股票代码
        name	str	股票名称
        area	str	所在地域
        industry	str	所属行业
        fullname	str	股票全称
        enname	str	英文全称
        market	str	市场类型 （主板/中小板/创业板）
        exchange_id	str	交易所代码
        curr_type	str	交易货币
        list_status	str	上市状态： L上市 D退市 P暂停上市
        list_date	str	上市日期
        delist_date	str	退市日期
        is_hs	str	是否沪深港通标的，N否 H沪股通 S深股通
        '''
        data = pro.stock_basic(exchange_id='', list_status='L', fields='symbol,name,area,industry,list_date,is_hs')
        return data

<<<<<<< HEAD
    def trade_cal(self):
=======
    def trade_cal():
>>>>>>> d9010ada373c24e3c40422f7411815f7c3353c6d
        '''交易日历
        描述：获取各大交易所交易日历数据,默认提取的是上交所
        输入参数
        exchange_id	str	N	交易所 SSE上交所 SZSE深交所
        start_date	str	N	开始日期
        end_date	str	N	结束日期
        is_open	int	N	是否交易 0休市 1交易
        输出参数
        exchange_id	str	交易所 SSE上交所 SZSE深交所
        cal_date	str	日历日期
        is_open	int	是否交易 0休市 1交易
        pretrade_date	str	上一个交易日
        '''
        cal = pro.trade_cal(exchange_id='', start_date='20180101', end_date='20181231')
        return cal

<<<<<<< HEAD
    def stock_company(self):
=======
    def stock_company():
>>>>>>> d9010ada373c24e3c40422f7411815f7c3353c6d
        '''上市公司基本信息
        描述：获取上市公司基础信息
        输出参数
        ts_code	str	Y	股票代码
        chairman	str	Y	法人代表
        manager	str	Y	总经理
        secretary	str	Y	董秘
        reg_capital	float	Y	注册资本
        setup_date	str	Y	注册日期
        province	str	Y	所在省份
        city	str	Y	所在城市
        introduction	str	Y	公司介绍
        website	str	Y	公司主页
        email	str	Y	电子邮件
        office	str	Y	办公室
        employees	int	Y	员工人数
        main_business	str	Y	主要业务及产品
        business_scope	str	Y	经营范围
        '''
        data = pro.stock_company(fields='ts_code,reg_capital,business_scope')
        return data

<<<<<<< HEAD
    def hs_const(self):
=======
    def hs_const():
>>>>>>> d9010ada373c24e3c40422f7411815f7c3353c6d
        '''沪深股通成份股
        描述：获取沪股通、深股通成分数据
        输入参数
        hs_type	str	Y	类型SH沪股通SZ深股通
        is_new	str	N	是否最新 1 是 0 否 (默认1)
        输出参数
        ts_code	str	Y	TS代码
        hs_type	str	Y	沪深港通类型SH沪SZ深
        in_date	str	Y	纳入日期
        out_date	str	Y	剔除日期
        is_new	str	Y	是否最新 1是0否
        '''
        data = pro.hs_const(hs_type='SH') 
        return data

<<<<<<< HEAD
    def namechange(self):
=======
    def namechange():
>>>>>>> d9010ada373c24e3c40422f7411815f7c3353c6d
        '''股票曾用名
        描述：历史名称变更记录
        输入参数
        ts_code	str	N	TS代码
        start_date	str	N	公告开始日期
        end_date	str	N	公告结束日期
        输出参数
        ts_code	str	Y	TS代码
        name	str	Y	证券名称
        start_date	str	Y	开始日期
        end_date	str	Y	结束日期
        ann_date	str	Y	公告日期
        change_reason	str	Y	变更原因
        '''
        data = pro.namechange(ts_code='002027.SZ', fields='ts_code,name,start_date,end_date,change_reason')
        return data

<<<<<<< HEAD
    def new_share(self):
=======
    def new_share():
>>>>>>> d9010ada373c24e3c40422f7411815f7c3353c6d
        '''IPO新股列表
        描述：获取新股上市列表数据
        限量：单次最大2000条，总量不限制
        积分：用户需要至少120积分才可以调取，具体请参阅积分获取办法
        输入参数
        start_date	str	N	上网发行开始日期
        end_date	str	N	上网发行结束日期
        输出参数
        ts_code	str	Y	TS股票代码
        sub_code	str	Y	申购代码
        name	str	Y	名称
        ipo_date	str	Y	上网发行日期
        issue_date	str	Y	上市日期
        amount	float	Y	发行总量（万股）
        market_amount	float	Y	上网发行总量（万股）
        price	float	Y	发行价格
        pe	float	Y	市盈率
        limit_amount	float	Y	个人申购上限（万股）
        funds	float	Y	募集资金（亿元）
        ballot	float	Y	中签率
        '''
        data = pro.new_share(start_date='20180901', end_date='20181018')
        return data
<<<<<<< HEAD


'''
debug = TushareBasicData()
basic = debug.stock_basic()
cal = debug.trade_cal()
company = debug.stock_company()
hs = debug.hs_const()
nchange = debug.namechange()
new = debug.new_share()
'''
=======
>>>>>>> d9010ada373c24e3c40422f7411815f7c3353c6d

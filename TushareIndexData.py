#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建时间：Fri Nov  2 16:34:47 2018
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder 3.2.6
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：TushareIndexData.py
"""

import tushare as ts
pro = ts.pro_api()


class TushareIndexData(object):
    #  指数数据
    def index_basic(self):
        '''指数基本信息
        描述：获取指数基础信息。
        输入参数
        market	str	Y	交易所或服务商
        publisher	str	N	发布商
        category	str	N	指数类别
        输出参数
        ts_code	str	TS代码
        name	str	简称
        fullname	str	指数全称
        market	str	市场
        publisher	str	发布方
        index_type	str	指数风格
        category	str	指数类别
        base_date	str	基期
        base_point	float	基点
        list_date	str	发布日期
        weight_rule	str	加权方式
        desc	str	描述
        exp_date	str	终止日期
        市场说明(market)

        市场代码	说明
        MSCI	MSCI指数
        CSI	中证指数
        SSE	上交所指数
        SZSE	深交所指数
        CICC	中金所指数
        SW	申万指数
        CNI	国证指数
        OTH	其他指数

        指数列表
        主题指数,规模指数,策略指数,风格指数,综合指数,成长指数,价值指数,有色指数,化工指数
        能源指数,其他指数,外汇指数,基金指数,商品指数,债券指数,行业指数,贵金属指数,农副产品指数
        软商品指数,油脂油料指数,非金属建材指数,煤焦钢矿指数,谷物指数,一级行业指数,二级行业指数
        三级行业指数
        '''
        data = pro.index_basic(market='SW')
        return data

    def index_daily(self):
        '''指数日线行情
        描述：获取指数每日行情，还可以通过bar接口获取。由于服务器压力，目前规则是单次调取最多取2800行记录，可以设置start和end日期补全。指数行情也可以通过通用行情接口获取数据．
        输入参数
        ts_code	str	N	指数代码
        trade_date	str	N	交易日期 （日期格式：YYYYMMDD，下同）
        start_date	str	N	开始日期
        end_date	None	N	结束日期
        输出参数
        ts_code	str	TS指数代码
        trade_date	str	交易日
        close	float	收盘点位
        open	float	开盘点位
        high	float	最高点位
        low	float	最低点位
        pre_close	float	昨日收盘点
        change	float	涨跌点
        pct_change	float	涨跌幅
        vol	float	成交量（手）
        amount	float	成交额（千元）
        '''
        data = pro.index_daily(ts_code='399300.SZ')
        return data

    def index_weight(self):
        '''指数成分和权重
        描述：获取各类指数成分和权重，月度数据 ，如需日度指数成分和权重，请联系 waditu@163.com
        来源：指数公司网站公开数据
        输入参数
        index_code	str	Y	指数代码 (二选一)
        trade_date	str	Y	交易日期 （二选一）
        start_date	str	N	开始日期
        end_date	None	N	结束日期
        输出参数
        index_code	str	指数代码
        con_code	str	成分代码
        trade_date	str	交易日期
        weight	float	权重
        '''
        data = pro.index_weight(index_code='399300.SZ', start_date='20180901', end_date='20180930')
        return data


'''
debug = TushareIndexData()
index_basic = debug.index_basic()
index_daily = debug.index_daily()
index_weight = debug.index_weight()
'''

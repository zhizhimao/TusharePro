#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
创建时间：Fri Nov  2 11:32:28 2018
作者: 星空飘飘
平台：Anaconda 3-5.1.0
语言版本：Python 3.6.4
编辑器：Spyder 3.2.6
分析器：Pandas: 0.22.0
解析器：lxml: 4.1.1
数据库：MongoDB 2.6.12
程序名：TushareFinancialData.py
"""

import tushare as ts
pro = ts.pro_api()


class TushareFinancialData(object):
    # 财务数据
    def income(self):
        '''利润表
        描述：获取上市公司财务利润表数据
        输入参数
        ts_code	str	Y	股票代码
        ann_date	str	N	公告日期
        start_date	str	N	报告期开始日期
        end_date	str	N	报告期结束日期
        period	str	N	报告期(每个季度最后一天的日期，比如20171231表示年报)
        report_type	str	N	报告类型： 参考下表说明
        comp_type	str	N	公司类型：1一般工商业 2银行 3保险 4证券
        输出参数
        ts_code	str	TS股票代码
        ann_date	str	公告日期
        f_ann_date	str	实际公告日期，即发生过数据变更的最终日期
        end_date	str	报告期
        report_type	str	报告类型： 参考下表说明
        comp_type	str	公司类型：1一般工商业 2银行 3保险 4证券
        basic_eps	float	基本每股收益
        diluted_eps	float	稀释每股收益
        total_revenue	float	营业总收入 (元，下同)
        revenue	float	营业收入
        int_income	float	利息收入
        prem_earned	float	已赚保费
        comm_income	float	手续费及佣金收入
        n_commis_income	float	手续费及佣金净收入
        n_oth_income	float	其他经营净收益
        n_oth_b_income	float	加:其他业务净收益
        prem_income	float	保险业务收入
        out_prem	float	减:分出保费
        une_prem_reser	float	提取未到期责任准备金
        reins_income	float	其中:分保费收入
        n_sec_tb_income	float	代理买卖证券业务净收入
        n_sec_uw_income	float	证券承销业务净收入
        n_asset_mg_income	float	受托客户资产管理业务净收入
        oth_b_income	float	其他业务收入
        fv_value_chg_gain	float	加:公允价值变动净收益
        invest_income	float	加:投资净收益
        ass_invest_income	float	其中:对联营企业和合营企业的投资收益
        forex_gain	float	加:汇兑净收益
        total_cogs	float	营业总成本
        oper_cost	float	减:营业成本
        int_exp	float	减:利息支出
        comm_exp	float	减:手续费及佣金支出
        biz_tax_surchg	float	减:营业税金及附加
        sell_exp	float	减:销售费用
        admin_exp	float	减:管理费用
        fin_exp	float	减:财务费用
        assets_impair_loss	float	减:资产减值损失
        prem_refund	float	退保金
        compens_payout	float	赔付总支出
        reser_insur_liab	float	提取保险责任准备金
        div_payt	float	保户红利支出
        reins_exp	float	分保费用
        oper_exp	float	营业支出
        compens_payout_refu	float	减:摊回赔付支出
        insur_reser_refu	float	减:摊回保险责任准备金
        reins_cost_refund	float	减:摊回分保费用
        other_bus_cost	float	其他业务成本
        operate_profit	float	营业利润
        non_oper_income	float	加:营业外收入
        non_oper_exp	float	减:营业外支出
        nca_disploss	float	其中:减:非流动资产处置净损失
        total_profit	float	利润总额
        income_tax	float	所得税费用
        n_income	float	净利润(含少数股东损益)
        n_income_attr_p	float	净利润(不含少数股东损益)
        minority_gain	float	少数股东损益
        oth_compr_income	float	其他综合收益
        t_compr_income	float	综合收益总额
        compr_inc_attr_p	float	归属于母公司(或股东)的综合收益总额
        compr_inc_attr_m_s	float	归属于少数股东的综合收益总额
        ebit	float	息税前利润
        ebitda	float	息税折旧摊销前利润
        insurance_exp	float	保险业务支出
        undist_profit	float	年初未分配利润
        distable_profit	float	可分配利润
        主要报表类型说明
        1	合并报表	上市公司最新报表（默认）
        2	单季合并	单一季度的合并报表
        3	调整单季合并表	调整后的单季合并报表（如果有）
        4	调整合并报表	本年度公布上年同期的财务报表数据，报告期为上年度
        5	调整前合并报表	数据发生变更，将原数据进行保留，即调整前的原数据
        6	母公司报表	该公司母公司的财务报表数据
        7	母公司单季表	母公司的单季度表
        8	母公司调整单季表	母公司调整后的单季表
        9	母公司调整表	该公司母公司的本年度公布上年同期的财务报表数据
        10	母公司调整前报表	母公司调整之前的原始财务报表数据
        11	调整前合并报表	调整之前合并报表原数据
        12	母公司调整前报表	母公司报表发生变更前保留的原数据
        '''
        data = pro.income(ts_code='600000.SH', start_date='20180101', end_date='20180730')
        return data

    def balancesheet(self):
        '''资产负债表
        描述：获取上市公司资产负债表
        输入参数
        ts_code	str	Y	股票代码
        ann_date	str	N	公告日期
        start_date	str	N	报告期开始日期
        end_date	str	N	报告期结束日期
        period	str	N	报告期(每个季度最后一天的日期，比如20171231表示年报)
        report_type	str	N	报告类型：见下方详细说明
        comp_type	str	N	公司类型：1一般工商业 2银行 3保险 4证券
        输出参数
        ts_code	str	TS股票代码
        ann_date	str	公告日期
        f_ann_date	str	实际公告日期
        end_date	str	报告期
        report_type	str	报表类型：见下方详细说明
        comp_type	str	公司类型：1一般工商业 2银行 3保险 4证券
        total_share	float	期末总股本
        cap_rese	float	资本公积金 (元，下同)
        undistr_porfit	float	未分配利润
        surplus_rese	float	盈余公积金
        special_rese	float	专项储备
        money_cap	float	货币资金
        trad_asset	float	交易性金融资产
        notes_receiv	float	应收票据
        accounts_receiv	float	应收账款
        oth_receiv	float	其他应收款
        prepayment	float	预付款项
        div_receiv	float	应收股利
        int_receiv	float	应收利息
        inventories	float	存货
        amor_exp	float	长期待摊费用
        nca_within_1y	float	一年内到期的非流动资产
        sett_rsrv	float	结算备付金
        loanto_oth_bank_fi	float	拆出资金
        premium_receiv	float	应收保费
        reinsur_receiv	float	应收分保账款
        reinsur_res_receiv	float	应收分保合同准备金
        pur_resale_fa	float	买入返售金融资产
        oth_cur_assets	float	其他流动资产
        total_cur_assets	float	流动资产合计
        fa_avail_for_sale	float	可供出售金融资产
        htm_invest	float	持有至到期投资
        lt_eqt_invest	float	长期股权投资
        invest_real_estate	float	投资性房地产
        time_deposits	float	定期存款
        oth_assets	float	其他资产
        lt_rec	float	长期应收款
        fix_assets	float	固定资产
        cip	float	在建工程
        const_materials	float	工程物资
        fixed_assets_disp	float	固定资产清理
        produc_bio_assets	float	生产性生物资产
        oil_and_gas_assets	float	油气资产
        intan_assets	float	无形资产
        r_and_d	float	研发支出
        goodwill	float	商誉
        lt_amor_exp	float	长期待摊费用
        defer_tax_assets	float	递延所得税资产
        decr_in_disbur	float	发放贷款及垫款
        oth_nca	float	其他非流动资产
        total_nca	float	非流动资产合计
        cash_reser_cb	float	现金及存放中央银行款项
        depos_in_oth_bfi	float	存放同业和其它金融机构款项
        prec_metals	float	贵金属
        deriv_assets	float	衍生金融资产
        rr_reins_une_prem	float	应收分保未到期责任准备金
        rr_reins_outstd_cla	float	应收分保未决赔款准备金
        rr_reins_lins_liab	float	应收分保寿险责任准备金
        rr_reins_lthins_liab	float	应收分保长期健康险责任准备金
        refund_depos	float	存出保证金
        ph_pledge_loans	float	保户质押贷款
        refund_cap_depos	float	存出资本保证金
        indep_acct_assets	float	独立账户资产
        client_depos	float	其中：客户资金存款
        client_prov	float	其中：客户备付金
        transac_seat_fee	float	其中:交易席位费
        invest_as_receiv	float	应收款项类投资
        total_assets	float	资产总计
        lt_borr	float	长期借款
        st_borr	float	短期借款
        cb_borr	float	向中央银行借款
        depos_ib_deposits	float	吸收存款及同业存放
        loan_oth_bank	float	拆入资金
        trading_fl	float	交易性金融负债
        notes_payable	float	应付票据
        acct_payable	float	应付账款
        adv_receipts	float	预收款项
        sold_for_repur_fa	float	卖出回购金融资产款
        comm_payable	float	应付手续费及佣金
        payroll_payable	float	应付职工薪酬
        taxes_payable	float	应交税费
        int_payable	float	应付利息
        div_payable	float	应付股利
        oth_payable	float	其他应付款
        acc_exp	float	预提费用
        deferred_inc	float	递延收益
        st_bonds_payable	float	应付短期债券
        payable_to_reinsurer	float	应付分保账款
        rsrv_insur_cont	float	保险合同准备金
        acting_trading_sec	float	代理买卖证券款
        acting_uw_sec	float	代理承销证券款
        non_cur_liab_due_1y	float	一年内到期的非流动负债
        oth_cur_liab	float	其他流动负债
        total_cur_liab	float	流动负债合计
        bond_payable	float	应付债券
        lt_payable	float	长期应付款
        specific_payables	float	专项应付款
        estimated_liab	float	预计负债
        defer_tax_liab	float	递延所得税负债
        defer_inc_non_cur_liab	float	递延收益-非流动负债
        oth_ncl	float	其他非流动负债
        total_ncl	float	非流动负债合计
        depos_oth_bfi	float	同业和其它金融机构存放款项
        deriv_liab	float	衍生金融负债
        depos	float	吸收存款
        agency_bus_liab	float	代理业务负债
        oth_liab	float	其他负债
        prem_receiv_adva	float	预收保费
        depos_received	float	存入保证金
        ph_invest	float	保户储金及投资款
        reser_une_prem	float	未到期责任准备金
        reser_outstd_claims	float	未决赔款准备金
        reser_lins_liab	float	寿险责任准备金
        reser_lthins_liab	float	长期健康险责任准备金
        indept_acc_liab	float	独立账户负债
        pledge_borr	float	其中:质押借款
        indem_payable	float	应付赔付款
        policy_div_payable	float	应付保单红利
        total_liab	float	负债合计
        treasury_share	float	减:库存股
        ordin_risk_reser	float	一般风险准备
        forex_differ	float	外币报表折算差额
        invest_loss_unconf	float	未确认的投资损失
        minority_int	float	少数股东权益
        total_hldr_eqy_exc_min_int	float	股东权益合计(不含少数股东权益)
        total_hldr_eqy_inc_min_int	float	股东权益合计(含少数股东权益)
        total_liab_hldr_eqy	float	负债及股东权益总计
        lt_payroll_payable	float	长期应付职工薪酬
        oth_comp_income	float	其他综合收益
        oth_eqt_tools	float	其他权益工具
        oth_eqt_tools_p_shr	float	其他权益工具(优先股)
        lending_funds	float	融出资金
        acc_receivable	float	应收款项
        st_fin_payable	float	应付短期融资款
        payables	float	应付款项
        hfs_assets	float	持有待售的资产
        hfs_sales	float	持有待售的负债
        主要报表类型说明
        1	合并报表	上市公司最新报表（默认）
        2	单季合并	单一季度的合并报表
        3	调整单季合并表	调整后的单季合并报表（如果有）
        4	调整合并报表	本年度公布上年同期的财务报表数据，报告期为上年度
        5	调整前合并报表	数据发生变更，将原数据进行保留，即调整前的原数据
        6	母公司报表	该公司母公司的财务报表数据
        7	母公司单季表	母公司的单季度表
        8	母公司调整单季表	母公司调整后的单季表
        9	母公司调整表	该公司母公司的本年度公布上年同期的财务报表数据
        10	母公司调整前报表	母公司调整之前的原始财务报表数据
        11	调整前合并报表	调整之前合并报表原数据
        12	母公司调整前报表	母公司报表发生变更前保留的原数据
        '''
        data = pro.balancesheet(ts_code='600000.SH', start_date='20180101', end_date='20180730')
        return data

    def cashflow(self):
        '''现金流量表
        描述：获取上市公司现金流量表
        输入参数
        ts_code	str	Y	股票代码
        ann_date	str	N	公告日期
        start_date	str	N	报告期开始日期
        end_date	str	N	报告期结束日期
        period	str	N	报告期(每个季度最后一天的日期，比如20171231表示年报)
        report_type	str	N	报告类型：见下方详细说明
        comp_type	str	N	公司类型：1一般工商业 2银行 3保险 4证券
        输出参数
        ts_code	str	TS股票代码
        ann_date	str	公告日期
        f_ann_date	str	实际公告日期
        end_date	str	报告期
        comp_type	str	公司类型：1一般工商业 2银行 3保险 4证券
        report_type	str	报表类型：见下方详细说明
        net_profit	float	净利润 (元，下同)
        finan_exp	float	财务费用
        c_fr_sale_sg	float	销售商品、提供劳务收到的现金
        recp_tax_rends	float	收到的税费返还
        n_depos_incr_fi	float	客户存款和同业存放款项净增加额
        n_incr_loans_cb	float	向中央银行借款净增加额
        n_inc_borr_oth_fi	float	向其他金融机构拆入资金净增加额
        prem_fr_orig_contr	float	收到原保险合同保费取得的现金
        n_incr_insured_dep	float	保户储金净增加额
        n_reinsur_prem	float	收到再保业务现金净额
        n_incr_disp_tfa	float	处置交易性金融资产净增加额
        ifc_cash_incr	float	收取利息和手续费净增加额
        n_incr_disp_faas	float	处置可供出售金融资产净增加额
        n_incr_loans_oth_bank	float	拆入资金净增加额
        n_cap_incr_repur	float	回购业务资金净增加额
        c_fr_oth_operate_a	float	收到其他与经营活动有关的现金
        c_inf_fr_operate_a	float	经营活动现金流入小计
        c_paid_goods_s	float	购买商品、接受劳务支付的现金
        c_paid_to_for_empl	float	支付给职工以及为职工支付的现金
        c_paid_for_taxes	float	支付的各项税费
        n_incr_clt_loan_adv	float	客户贷款及垫款净增加额
        n_incr_dep_cbob	float	存放央行和同业款项净增加额
        c_pay_claims_orig_inco	float	支付原保险合同赔付款项的现金
        pay_handling_chrg	float	支付手续费的现金
        pay_comm_insur_plcy	float	支付保单红利的现金
        oth_cash_pay_oper_act	float	支付其他与经营活动有关的现金
        st_cash_out_act	float	经营活动现金流出小计
        n_cashflow_act	float	经营活动产生的现金流量净额
        oth_recp_ral_inv_act	float	收到其他与投资活动有关的现金
        c_disp_withdrwl_invest	float	收回投资收到的现金
        c_recp_return_invest	float	取得投资收益收到的现金
        n_recp_disp_fiolta	float	处置固定资产、无形资产和其他长期资产收回的现金净额
        n_recp_disp_sobu	float	处置子公司及其他营业单位收到的现金净额
        stot_inflows_inv_act	float	投资活动现金流入小计
        c_pay_acq_const_fiolta	float	购建固定资产、无形资产和其他长期资产支付的现金
        c_paid_invest	float	投资支付的现金
        n_disp_subs_oth_biz	float	取得子公司及其他营业单位支付的现金净额
        oth_pay_ral_inv_act	float	支付其他与投资活动有关的现金
        n_incr_pledge_loan	float	质押贷款净增加额
        stot_out_inv_act	float	投资活动现金流出小计
        n_cashflow_inv_act	float	投资活动产生的现金流量净额
        c_recp_borrow	float	取得借款收到的现金
        proc_issue_bonds	float	发行债券收到的现金
        oth_cash_recp_ral_fnc_act	float	收到其他与筹资活动有关的现金
        stot_cash_in_fnc_act	float	筹资活动现金流入小计
        free_cashflow	float	企业自由现金流量
        c_prepay_amt_borr	float	偿还债务支付的现金
        c_pay_dist_dpcp_int_exp	float	分配股利、利润或偿付利息支付的现金
        incl_dvd_profit_paid_sc_ms	float	其中:子公司支付给少数股东的股利、利润
        oth_cashpay_ral_fnc_act	float	支付其他与筹资活动有关的现金
        stot_cashout_fnc_act	float	筹资活动现金流出小计
        n_cash_flows_fnc_act	float	筹资活动产生的现金流量净额
        eff_fx_flu_cash	float	汇率变动对现金的影响
        n_incr_cash_cash_equ	float	现金及现金等价物净增加额
        c_cash_equ_beg_period	float	期初现金及现金等价物余额
        c_cash_equ_end_period	float	期末现金及现金等价物余额
        c_recp_cap_contrib	float	吸收投资收到的现金
        incl_cash_rec_saims	float	其中:子公司吸收少数股东投资收到的现金
        uncon_invest_loss	float	未确认投资损失
        prov_depr_assets	float	加:资产减值准备
        depr_fa_coga_dpba	float	固定资产折旧、油气资产折耗、生产性生物资产折旧
        amort_intang_assets	float	无形资产摊销
        lt_amort_deferred_exp	float	长期待摊费用摊销
        decr_deferred_exp	float	待摊费用减少
        incr_acc_exp	float	预提费用增加
        loss_disp_fiolta	float	处置固定、无形资产和其他长期资产的损失
        loss_scr_fa	float	固定资产报废损失
        loss_fv_chg	float	公允价值变动损失
        invest_loss	float	投资损失
        decr_def_inc_tax_assets	float	递延所得税资产减少
        incr_def_inc_tax_liab	float	递延所得税负债增加
        decr_inventories	float	存货的减少
        decr_oper_payable	float	经营性应收项目的减少
        incr_oper_payable	float	经营性应付项目的增加
        others	float	其他
        im_net_cashflow_oper_act	float	经营活动产生的现金流量净额(间接法)
        conv_debt_into_cap	float	债务转为资本
        conv_copbonds_due_within_1y	float	一年内到期的可转换公司债券
        fa_fnc_leases	float	融资租入固定资产
        end_bal_cash	float	现金的期末余额
        beg_bal_cash	float	减:现金的期初余额
        end_bal_cash_equ	float	加:现金等价物的期末余额
        beg_bal_cash_equ	float	减:现金等价物的期初余额
        im_n_incr_cash_equ	float	现金及现金等价物净增加额(间接法)
        主要报表类型说明
        1	合并报表	上市公司最新报表（默认）
        2	单季合并	单一季度的合并报表
        3	调整单季合并表	调整后的单季合并报表（如果有）
        4	调整合并报表	本年度公布上年同期的财务报表数据，报告期为上年度
        5	调整前合并报表	数据发生变更，将原数据进行保留，即调整前的原数据
        6	母公司报表	该公司母公司的财务报表数据
        7	母公司单季表	母公司的单季度表
        8	母公司调整单季表	母公司调整后的单季表
        9	母公司调整表	该公司母公司的本年度公布上年同期的财务报表数据
        10	母公司调整前报表	母公司调整之前的原始财务报表数据
        11	调整前合并报表	调整之前合并报表原数据
        12	母公司调整前报表	母公司报表发生变更前保留的原数据
        '''
        data = pro.cashflow(ts_code='600000.SH', start_date='20180101', end_date='20180730')
        return data

    def forecast(self):
        '''业绩预告
        描述：获取业绩预告数据
        输入参数
        ts_code	str	N	股票代码(二选一)
        ann_date	str	N	公告日期
        start_date	str	N	公告开始日期
        end_date	str	N	公告结束日期
        period	str	N	报告期 (二选一) (每个季度最后一天的日期，比如20171231表示年报)
        type	str	N	预告类型(预增/预减/扭亏/首亏/续亏/续盈/略增/略减)
        输出参数
        ts_code	str	TS股票代码
        ann_date	str	公告日期
        end_date	str	报告期
        type	str	业绩预告类型(预增/预减/扭亏/首亏/续亏/续盈/略增/略减)
        p_change_min	float	预告净利润变动幅度下限（%）
        p_change_max	float	预告净利润变动幅度上限（%）
        net_profit_min	float	预告净利润下限（万元）
        net_profit_max	float	预告净利润上限（万元）
        last_parent_net	float	上年同期归属母公司净利润
        first_ann_date	str	首次公告日
        summary	str	业绩预告摘要
        change_reason	str	业绩变动原因
        '''
        data = pro.forecast(ts_code='600000.SH')
        return data

    def express(self):
        '''业绩快报
        描述：获取上市公司业绩快报
        输入参数
        ts_code	str	N	股票代码 (二选一)
        ann_date	str	N	公告日期 (二选一)
        start_date	str	N	公告开始日期
        end_date	str	N	公告结束日期
        period	str	N	报告期(每个季度最后一天的日期,比如20171231表示年报)
        输出参数
        ts_code	str	TS股票代码
        ann_date	str	公告日期
        end_date	str	报告期
        revenue	float	营业收入(元)
        operate_profit	float	营业利润(元)
        total_profit	float	利润总额(元)
        n_income	float	净利润(元)
        total_assets	float	总资产(元)
        total_hldr_eqy_exc_min_int	float	股东权益合计(不含少数股东权益)(元)
        diluted_eps	float	每股收益(摊薄)(元)
        diluted_roe	float	净资产收益率(摊薄)(%)
        yoy_net_profit	float	去年同期修正后净利润
        bps	float	每股净资产
        yoy_sales	float	同比增长率:营业收入
        yoy_op	float	同比增长率:营业利润
        yoy_tp	float	同比增长率:利润总额
        yoy_dedu_np	float	同比增长率:归属母公司股东的净利润
        yoy_eps	float	同比增长率:基本每股收益
        yoy_roe	float	同比增减:加权平均净资产收益率
        growth_assets	float	比年初增长率:总资产
        yoy_equity	float	比年初增长率:归属母公司的股东权益
        growth_bps	float	比年初增长率:归属于母公司股东的每股净资产
        or_last_year	float	去年同期营业收入
        op_last_year	float	去年同期营业利润
        tp_last_year	float	去年同期利润总额
        np_last_year	float	去年同期净利润
        eps_last_year	float	去年同期每股收益
        open_net_assets	float	期初净资产
        open_bps	float	期初每股净资产
        perf_summary	str	业绩简要说明
        is_audit	int	是否审计： 1是 0否
        remark	str	备注
        '''
        data = pro.express(ts_code='600000.SH', start_date='20180101', end_date='20180701')
        return data

    def dividend(self):
        '''分红送股
        描述：分红送股数据
        输入参数
        ts_code	str	N	TS代码
        ann_date	str	N	公告日
        record_date	str	N	股权登记日期
        ex_date	str	N	除权除息日
        以上参数至少有一个不能为空
        输出参数
        ts_code	str	Y	TS代码
        end_date	str	Y	分红年度
        ann_date	str	Y	预案公告日
        div_proc	str	Y	实施进度
        stk_div	float	Y	每股送转
        stk_bo_rate	float	Y	每股送股比例
        stk_co_rate	float	Y	每股转增比例
        cash_div	float	Y	每股分红（税后）
        cash_div_tax	float	Y	每股分红（税前）
        record_date	str	Y	股权登记日
        ex_date	str	Y	除权除息日
        pay_date	str	Y	派息日
        div_listdate	str	Y	红股上市日
        imp_ann_date	str	Y	实施公告日
        base_date	str	N	基准日
        base_share	float	N	基准股本（万）
        '''
        data = pro.dividend(ts_code='600848.SH', fields='ts_code,div_proc,stk_div,record_date,ex_date')
        return data

    def fina_indicator(self):
        '''财务指标数据
        描述：获取上市公司财务指标数据，为避免服务器压力，现阶段每次请求最多返回30条记录，可通过设置日期多次请求获取更多数据。
        输入参数
        ts_code	str	N	TS股票代码,e.g. 600001.SH/000001.SZ
        ann_date	str	N	公告日期
        start_date	str	N	报告期开始日期
        end_date	str	N	报告期结束日期
        period	str	N	报告期(每个季度最后一天的日期,比如20171231表示年报)
        输出参数
        ts_code	str	TS代码
        ann_date	str	公告日期
        end_date	str	报告期
        eps	float	基本每股收益
        dt_eps	float	稀释每股收益
        total_revenue_ps	float	每股营业总收入
        revenue_ps	float	每股营业收入
        capital_rese_ps	float	每股资本公积
        surplus_rese_ps	float	每股盈余公积
        undist_profit_ps	float	每股未分配利润
        extra_item	float	非经常性损益
        profit_dedt	float	扣除非经常性损益后的净利润
        gross_margin	float	毛利
        current_ratio	float	流动比率
        quick_ratio	float	速动比率
        cash_ratio	float	保守速动比率
        invturn_days	float	存货周转天数
        arturn_days	float	应收账款周转天数
        inv_turn	float	存货周转率
        ar_turn	float	应收账款周转率
        ca_turn	float	流动资产周转率
        fa_turn	float	固定资产周转率
        assets_turn	float	总资产周转率
        op_income	float	经营活动净收益
        valuechange_income	float	价值变动净收益
        interst_income	float	利息费用
        daa	float	折旧与摊销
        ebit	float	息税前利润
        ebitda	float	息税折旧摊销前利润
        fcff	float	企业自由现金流量
        fcfe	float	股权自由现金流量
        current_exint	float	无息流动负债
        noncurrent_exint	float	无息非流动负债
        interestdebt	float	带息债务
        netdebt	float	净债务
        tangible_asset	float	有形资产
        working_capital	float	营运资金
        networking_capital	float	营运流动资本
        invest_capital	float	全部投入资本
        retained_earnings	float	留存收益
        diluted2_eps	float	期末摊薄每股收益
        bps	float	每股净资产
        ocfps	float	每股经营活动产生的现金流量净额
        retainedps	float	每股留存收益
        cfps	float	每股现金流量净额
        ebit_ps	float	每股息税前利润
        fcff_ps	float	每股企业自由现金流量
        fcfe_ps	float	每股股东自由现金流量
        netprofit_margin	float	销售净利率
        grossprofit_margin	float	销售毛利率
        cogs_of_sales	float	销售成本率
        expense_of_sales	float	销售期间费用率
        profit_to_gr	float	净利润/营业总收入
        saleexp_to_gr	float	销售费用/营业总收入
        adminexp_of_gr	float	管理费用/营业总收入
        finaexp_of_gr	float	财务费用/营业总收入
        impai_ttm	float	资产减值损失/营业总收入
        gc_of_gr	float	营业总成本/营业总收入
        op_of_gr	float	营业利润/营业总收入
        ebit_of_gr	float	息税前利润/营业总收入
        roe	float	净资产收益率
        roe_waa	float	加权平均净资产收益率
        roe_dt	float	净资产收益率(扣除非经常损益)
        roa	float	总资产报酬率
        npta	float	总资产净利润
        roic	float	投入资本回报率
        roe_yearly	float	年化净资产收益率
        roa2_yearly	float	年化总资产报酬率
        roe_avg	float	平均净资产收益率(增发条件)
        opincome_of_ebt	float	经营活动净收益/利润总额
        investincome_of_ebt	float	价值变动净收益/利润总额
        n_op_profit_of_ebt	float	营业外收支净额/利润总额
        tax_to_ebt	float	所得税/利润总额
        dtprofit_to_profit	float	扣除非经常损益后的净利润/净利润
        salescash_to_or	float	销售商品提供劳务收到的现金/营业收入
        ocf_to_or	float	经营活动产生的现金流量净额/营业收入
        ocf_to_opincome	float	经营活动产生的现金流量净额/经营活动净收益
        capitalized_to_da	float	资本支出/折旧和摊销
        debt_to_assets	float	资产负债率
        assets_to_eqt	float	权益乘数
        dp_assets_to_eqt	float	权益乘数(杜邦分析)
        ca_to_assets	float	流动资产/总资产
        nca_to_assets	float	非流动资产/总资产
        tbassets_to_totalassets	float	有形资产/总资产
        int_to_talcap	float	带息债务/全部投入资本
        eqt_to_talcapital	float	归属于母公司的股东权益/全部投入资本
        currentdebt_to_debt	float	流动负债/负债合计
        longdeb_to_debt	float	非流动负债/负债合计
        ocf_to_shortdebt	float	经营活动产生的现金流量净额/流动负债
        debt_to_eqt	float	产权比率
        eqt_to_debt	float	归属于母公司的股东权益/负债合计
        eqt_to_interestdebt	float	归属于母公司的股东权益/带息债务
        tangibleasset_to_debt	float	有形资产/负债合计
        tangasset_to_intdebt	float	有形资产/带息债务
        tangibleasset_to_netdebt	float	有形资产/净债务
        ocf_to_debt	float	经营活动产生的现金流量净额/负债合计
        ocf_to_interestdebt	float	经营活动产生的现金流量净额/带息债务
        ocf_to_netdebt	float	经营活动产生的现金流量净额/净债务
        ebit_to_interest	float	已获利息倍数(EBIT/利息费用)
        longdebt_to_workingcapital	float	长期债务与营运资金比率
        ebitda_to_debt	float	息税折旧摊销前利润/负债合计
        turn_days	float	营业周期
        roa_yearly	float	年化总资产净利率
        roa_dp	float	总资产净利率(杜邦分析)
        fixed_assets	float	固定资产合计
        profit_prefin_exp	float	扣除财务费用前营业利润
        non_op_profit	float	非营业利润
        op_to_ebt	float	营业利润／利润总额
        nop_to_ebt	float	非营业利润／利润总额
        ocf_to_profit	float	经营活动产生的现金流量净额／营业利润
        cash_to_liqdebt	float	货币资金／流动负债
        cash_to_liqdebt_withinterest	float	货币资金／带息流动负债
        op_to_liqdebt	float	营业利润／流动负债
        op_to_debt	float	营业利润／负债合计
        roic_yearly	float	年化投入资本回报率
        total_fa_trun	float	固定资产合计周转率
        profit_to_op	float	利润总额／营业收入
        q_opincome	float	经营活动单季度净收益
        q_investincome	float	价值变动单季度净收益
        q_dtprofit	float	扣除非经常损益后的单季度净利润
        q_eps	float	每股收益(单季度)
        q_netprofit_margin	float	销售净利率(单季度)
        q_gsprofit_margin	float	销售毛利率(单季度)
        q_exp_to_sales	float	销售期间费用率(单季度)
        q_profit_to_gr	float	净利润／营业总收入(单季度)
        q_saleexp_to_gr	float	销售费用／营业总收入 (单季度)
        q_adminexp_to_gr	float	管理费用／营业总收入 (单季度)
        q_finaexp_to_gr	float	财务费用／营业总收入 (单季度)
        q_impair_to_gr_ttm	float	资产减值损失／营业总收入(单季度)
        q_gc_to_gr	float	营业总成本／营业总收入 (单季度)
        q_op_to_gr	float	营业利润／营业总收入(单季度)
        q_roe	float	净资产收益率(单季度)
        q_dt_roe	float	净资产单季度收益率(扣除非经常损益)
        q_npta	float	总资产净利润(单季度)
        q_opincome_to_ebt	float	经营活动净收益／利润总额(单季度)
        q_investincome_to_ebt	float	价值变动净收益／利润总额(单季度)
        q_dtprofit_to_profit	float	扣除非经常损益后的净利润／净利润(单季度)
        q_salescash_to_or	float	销售商品提供劳务收到的现金／营业收入(单季度)
        q_ocf_to_sales	float	经营活动产生的现金流量净额／营业收入(单季度)
        q_ocf_to_or	float	经营活动产生的现金流量净额／经营活动净收益(单季度)
        basic_eps_yoy	float	基本每股收益同比增长率(%)
        dt_eps_yoy	float	稀释每股收益同比增长率(%)
        cfps_yoy	float	每股经营活动产生的现金流量净额同比增长率(%)
        op_yoy	float	营业利润同比增长率(%)
        ebt_yoy	float	利润总额同比增长率(%)
        netprofit_yoy	float	归属母公司股东的净利润同比增长率(%)
        dt_netprofit_yoy	float	归属母公司股东的净利润-扣除非经常损益同比增长率(%)
        ocf_yoy	float	经营活动产生的现金流量净额同比增长率(%)
        roe_yoy	float	净资产收益率(摊薄)同比增长率(%)
        bps_yoy	float	每股净资产相对年初增长率(%)
        assets_yoy	float	资产总计相对年初增长率(%)
        eqt_yoy	float	归属母公司的股东权益相对年初增长率(%)
        tr_yoy	float	营业总收入同比增长率(%)
        or_yoy	float	营业收入同比增长率(%)
        q_gr_yoy	float	营业总收入同比增长率(%)(单季度)
        q_gr_qoq	float	营业总收入环比增长率(%)(单季度)
        q_sales_yoy	float	营业收入同比增长率(%)(单季度)
        q_sales_qoq	float	营业收入环比增长率(%)(单季度)
        q_op_yoy	float	营业利润同比增长率(%)(单季度)
        q_op_qoq	float	营业利润环比增长率(%)(单季度)
        q_profit_yoy	float	净利润同比增长率(%)(单季度)
        q_profit_qoq	float	净利润环比增长率(%)(单季度)
        q_netprofit_yoy	float	归属母公司股东的净利润同比增长率(%)(单季度)
        q_netprofit_qoq	float	归属母公司股东的净利润环比增长率(%)(单季度)
        equity_yoy	float	净资产同比增长率
        rd_exp	float	研发费用
        '''
        data = pro.fina_indicator(ts_code='600000.SH')
        return data

    def fina_audit(self):
        '''财务审计意见
        描述：获取上市公司定期财务审计意见数据
        输入参数
        ts_code	str	Y	股票代码
        ann_date	str	N	公告日期
        start_date	str	N	公告开始日期
        end_date	str	N	公告结束日期
        period	str	N	报告期(每个季度最后一天的日期,比如20171231表示年报)
        输出参数
        ts_code	str	TS股票代码
        ann_date	str	公告日期
        end_date	str	报告期
        audit_result	str	审计结果
        audit_fees	float	审计总费用（元）
        audit_agency	str	会计事务所
        audit_sign	str	签字会计师
        '''
        data = pro.fina_audit(ts_code='600000.SH', start_date='20100101', end_date='20180808')
        return data

    def fina_mainbz(self):
        '''主营业务构成
        描述：获得上市公司主营业务构成，分地区和产品两种方式
        输入参数
        ts_code	str	Y	股票代码
        period	str	N	报告期(每个季度最后一天的日期,比如20171231表示年报)
        type	str	N	类型：P按产品 D按地区（请输入大写字母P或者D）
        start_date	str	N	报告期开始日期
        end_date	str	N	报告期结束日期
        输出参数
        ts_code	str	TS代码
        end_date	str	报告期
        bz_item	str	主营业务来源
        bz_sales	float	主营业务收入(元)
        bz_profit	float	主营业务利润(元)
        bz_cost	float	主营业务成本(元)
        curr_type	str	货币代码
        update_flag	str	是否更新
        '''
        data = pro.fina_mainbz(ts_code='000627.SZ', period='20171231', type='P')
        return data


'''
debug = TushareFinancialData()
income = debug.income()
balancesheet = debug.balancesheet()
cashflow = debug.cashflow()
forecast = debug.forecast()
express = debug.express()
dividend = debug.dividend()
fina_indicator = debug.fina_indicator()
fina_audit = debug.fina_audit()
fina_mainbz = debug.fina_mainbz()
'''

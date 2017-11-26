# -*- coding:utf-8 -*-  
from sqlalchemy import create_engine
from django.http import HttpResponse
import json
import pandas as pd
import numpy as np
import tushare as ts
import time,sched
import schedule
import time
import datetime

now = datetime.datetime.now()
year = now.strftime('%Y')  
today = now.strftime('%Y-%m-%d')  

def init(request):
    # ts.get_stock_basics()
    schedule.clear()
    return HttpResponse('clear all task')

# 交易数据
def job_1():
    # 股票列表
    stock_basics = ts.get_stock_basics()
    data = pd.DataFrame(stock_basics)
    data.to_sql('stock_basics',engine,index=False,if_exists='replace')
    print("股票列表......done")

# 投资参考数据
def job_2():
    # 分配预案
    profit_data = ts.profit_data(year, top=1000)
    data = pd.DataFrame(profit_data)
    data.to_sql('profit_data',engine,index=False,if_exists='replace')
    print("分配预案......done")

    # 业绩预告
    forecast_data = ts.forecast_data(year,1)
    data = pd.DataFrame(forecast_data)
    data.to_sql('forecast_data',engine,index=False,if_exists='replace')
    print("业绩预告......done")

    # 限售股解禁
    xsg_data = ts.xsg_data()
    data = pd.DataFrame(xsg_data)
    data.to_sql('xsg_data',engine,index=False,if_exists='replace')
    print("限售股解禁......done")

    # 基金持股
    fund_holdings = ts.fund_holdings(year, 1)
    data = pd.DataFrame(fund_holdings)
    data.to_sql('fund_holdings',engine,index=False,if_exists='replace')
    print("基金持股......done")
    
    # 新股数据
    new_stocks = ts.new_stocks()
    data = pd.DataFrame(new_stocks)
    data.to_sql('new_stocks',engine,index=False,if_exists='replace')
    print("新股数据......done")

    # 融资融券（沪市）
    sh_margins = ts.sh_margins()
    data = pd.DataFrame(sh_margins)
    data.to_sql('sh_margins',engine,index=False,if_exists='replace')
    print("融资融券（沪市）......done")

    # 融资融券（深市）
    sz_margins = ts.sz_margins()
    data = pd.DataFrame(sz_margins)
    data.to_sql('sz_margins',engine,index=False,if_exists='replace')
    print("融资融券（深市）......done")

# 股票分类数据
def job_3():
    print("I'm working......基本面数据")
    engine = create_engine('postgresql://postgres@localhost:5432/tushare') 
    # engine = create_engine('postgresql://tushare@localhost:5432/tushare') 
    # engine = create_engine('postgresql://postgres@47.93.193.128:5432/tushare')
    try:
        
        # 行业分类
        industry_classified = ts.get_industry_classified()
        data = pd.DataFrame(industry_classified)
        data.to_sql('industry_classified',engine,index=False,if_exists='replace')
        print("行业分类......done")

        # 概念分类
        concept_classified = ts.get_concept_classified()
        data = pd.DataFrame(concept_classified)
        data.to_sql('concept_classified',engine,index=False,if_exists='replace')
        print("概念分类......done")

        # 地域分类
        area_classified = ts.get_area_classified()
        data = pd.DataFrame(area_classified)
        data.to_sql('area_classified',engine,index=False,if_exists='replace')
        print("地域分类......done")

        # 中小板分类
        sme_classified = ts.get_sme_classified()
        data = pd.DataFrame(sme_classified)
        data.to_sql('sme_classified',engine,index=False,if_exists='replace')
        print("中小板分类......done")

        # 创业板分类
        gem_classified = ts.get_gem_classified()
        data = pd.DataFrame(gem_classified)
        data.to_sql('gem_classified',engine,index=False,if_exists='replace')
        print("创业板分类......done")

        # # 风险警示板分类
        # st_classified = ts.get_st_classified()
        # data = pd.DataFrame(st_classified)
        # data.to_sql('st_classified',engine,index=False,if_exists='replace')
        # print("风险警示板分类......done")

        # 沪深300成份及权重
        hs300s = ts.get_hs300s()
        data = pd.DataFrame(hs300s)
        data.to_sql('hs300s',engine,index=False,if_exists='replace')
        print("沪深300成份及权重......done")

        # 上证50成份股
        sz50s = ts.get_sz50s()
        data = pd.DataFrame(sz50s)
        data.to_sql('sz50s',engine,index=False,if_exists='replace')
        print("上证50成份股......done")

        # 中证500成份股
        zz500s = ts.get_zz500s()
        data = pd.DataFrame(zz500s)
        data.to_sql('zz500s',engine,index=False,if_exists='replace')
        print("中证500成份股......done")

        # 终止上市股票列表
        terminated = ts.get_terminated()
        data = pd.DataFrame(terminated)
        data.to_sql('terminated',engine,index=False,if_exists='replace')
        print("终止上市股票列表......done")

        # 暂停上市股票列表
        suspended = ts.get_suspended()
        data = pd.DataFrame(suspended)
        data.to_sql('suspended',engine,index=False,if_exists='replace')
        print("暂停上市股票列表......done")
    except Exception as e:
        print(e)

# 基本面数据
def job_4():
    # 股票列表
    stock_basics = ts.get_stock_basics()
    data = pd.DataFrame(stock_basics)
    data.to_sql('stock_basics',engine,index=False,if_exists='replace')
    print("股票列表......done")

# 宏观经济数据
def job_5():
    try:
        # 存款利率
        deposit_rate = ts.get_deposit_rate()
        data = pd.DataFrame(deposit_rate)
        data.to_sql('deposit_rate',engine,index=False,if_exists='replace')
        print("存款利率......done")

        # 贷款利率
        loan_rate = ts.get_loan_rate()
        data = pd.DataFrame(loan_rate)
        data.to_sql('loan_rate',engine,index=False,if_exists='replace')
        print("贷款利率......done")

        # 存款准备金率
        rrr = ts.get_rrr()
        data = pd.DataFrame(rrr)
        data.to_sql('rrr',engine,index=False,if_exists='replace')
        print("存款准备金率......done")

        # 货币供应量
        money_supply = ts.get_money_supply()
        data = pd.DataFrame(money_supply)
        data.to_sql('money_supply',engine,index=False,if_exists='replace')
        print("货币供应量......done")

        # 货币供应量(年底余额)
        money_supply_bal = ts.get_money_supply_bal()
        data = pd.DataFrame(money_supply_bal)
        data.to_sql('money_supply_bal',engine,index=False,if_exists='replace')
        print("货币供应量(年底余额)......done")

        # 国内生产总值(年度)
        gdp_year = ts.get_gdp_year()
        data = pd.DataFrame(gdp_year)
        data.to_sql('gdp_year',engine,index=False,if_exists='replace')
        print("国内生产总值(年度)......done")

        # 国内生产总值(季度)
        gdp_quarter = ts.get_gdp_quarter()
        data = pd.DataFrame(gdp_quarter)
        data.to_sql('gdp_quarter',engine,index=False,if_exists='replace')
        print("国内生产总值(季度)......done")

        # 三大需求对GDP贡献
        gdp_for = ts.get_gdp_for()
        data = pd.DataFrame(gdp_for)
        data.to_sql('gdp_for',engine,index=False,if_exists='replace')
        print("三大需求对GDP贡献......done")

        # 三大产业对GDP拉动
        gdp_pull = ts.get_gdp_pull()
        data = pd.DataFrame(gdp_pull)
        data.to_sql('gdp_pull',engine,index=False,if_exists='replace')
        print("三大产业对GDP拉动......done")

        # 三大产业贡献率
        gdp_contrib = ts.get_gdp_contrib()
        data = pd.DataFrame(gdp_contrib)
        data.to_sql('gdp_contrib',engine,index=False,if_exists='replace')
        print("三大产业贡献率......done")

        # 居民消费价格指数
        cpi = ts.get_cpi()
        data = pd.DataFrame(cpi)
        data.to_sql('cpi',engine,index=False,if_exists='replace')
        print("居民消费价格指数......done")

        # 工业品出厂价格指数
        ppi = ts.get_ppi()
        data = pd.DataFrame(ppi)
        data.to_sql('ppi',engine,index=False,if_exists='replace')
        print("工业品出厂价格指数......done")

    except Exception as e:
        print(e)

# 新闻事件数据
def job_6():
    # 即时新闻
    latest_news = ts.get_latest_news()
    data = pd.DataFrame(latest_news)
    data.to_sql('latest_news',engine,index=False,if_exists='replace')
    print("即时新闻......done")

    # 信息地雷
    notices = ts.get_notices()
    data = pd.DataFrame(notices)
    data.to_sql('notices',engine,index=False,if_exists='replace')
    print("信息地雷......done")

    # 新浪股吧
    guba_sina = ts.guba_sina()
    data = pd.DataFrame(guba_sina)
    data.to_sql('guba_sina',engine,index=False,if_exists='replace')
    print("新浪股吧......done")


# 龙虎榜数据
def job_7():
    # 每日龙虎榜列表
    top_list = ts.top_list(today)
    data = pd.DataFrame(top_list)
    data.to_sql('top_list',engine,index=False,if_exists='replace')
    print("每日龙虎榜列表......done")

    # 个股上榜统计
    cap_tops = ts.cap_tops()
    data = pd.DataFrame(cap_tops)
    data.to_sql('cap_tops',engine,index=False,if_exists='replace')
    print("个股上榜统计......done")

    # 营业部上榜统计
    broker_tops = ts.broker_tops()
    data = pd.DataFrame(broker_tops)
    data.to_sql('broker_tops',engine,index=False,if_exists='replace')
    print("营业部上榜统计......done")

    # 机构席位追踪
    inst_tops = ts.inst_tops()
    data = pd.DataFrame(inst_tops)
    data.to_sql('inst_tops',engine,index=False,if_exists='replace')
    print("机构席位追踪......done")

    # 机构成交明细
    inst_detail = ts.inst_detail()
    data = pd.DataFrame(inst_detail)
    data.to_sql('inst_detail',engine,index=False,if_exists='replace')
    print("机构成交明细......done")

# 银行间同业拆放利率
def job_8():
    # Shibor拆放利率
    shibor_data = ts.shibor_data()
    data = pd.DataFrame(shibor_data)
    data.to_sql('shibor_data',engine,index=False,if_exists='replace')
    print("银行间同业拆放利率......done")

    # 银行报价数据
    shibor_quote_data = ts.shibor_quote_data()
    data = pd.DataFrame(shibor_quote_data)
    data.to_sql('shibor_quote_data',engine,index=False,if_exists='replace')
    print("银行报价数据......done")

    # Shibor均值数据
    shibor_ma_data = ts.shibor_ma_data()
    data = pd.DataFrame(shibor_ma_data)
    data.to_sql('shibor_ma_data',engine,index=False,if_exists='replace')
    print("Shibor均值数据......done")

    # 贷款基础利率（LPR）
    lpr_data = ts.lpr_data()
    data = pd.DataFrame(lpr_data)
    data.to_sql('lpr_data',engine,index=False,if_exists='replace')
    print("贷款基础利率......done")

    # LPR均值数据
    lpr_ma_data = ts.lpr_ma_data()
    data = pd.DataFrame(lpr_ma_data)
    data.to_sql('lpr_ma_data',engine,index=False,if_exists='replace')
    print("LPR均值数据......done")

# 电影票房
def job_9():
    # 实时票房
    realtime_boxoffice = ts.realtime_boxoffice()
    data = pd.DataFrame(realtime_boxoffice)
    data.to_sql('realtime_boxoffice',engine,index=False,if_exists='replace')
    print("实时票房......done")

    # 每日票房
    day_boxoffice = ts.day_boxoffice()
    data = pd.DataFrame(day_boxoffice)
    data.to_sql('day_boxoffice',engine,index=False,if_exists='replace')
    print("每日票房......done")

    # 月度票房
    month_boxoffice = ts.month_boxoffice()
    data = pd.DataFrame(month_boxoffice)
    data.to_sql('month_boxoffice',engine,index=False,if_exists='replace')
    print("月度票房......done")

    # 影院日度票房
    day_cinema = ts.day_cinema()
    data = pd.DataFrame(day_cinema)
    data.to_sql('day_cinema',engine,index=False,if_exists='replace')
    print("影院日度票房......done")

  
schedule.every(10).minutes.do(job_1)
schedule.every(1).hour.do(job_2)
schedule.every(1).hour.do(job_3)
schedule.every(1).hour.do(job_4)
schedule.every(1).hour.do(job_5)

schedule.every(1).hour.do(job_6)
schedule.every(1).hour.do(job_7)
schedule.every(1).hour.do(job_8)
schedule.every().day.at("17:00").do(job_9)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

# def worker(msg, starttime):
#     print "time:", time.time(), "msg", msg, 'startTime', starttime
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

def init(request):
    # ts.get_stock_basics()
    schedule.clear()
    return HttpResponse('clear all task')

def job():
    print("I'm working...")
    engine = create_engine('postgresql://postgres@localhost:5432/tushare') 
    # engine = create_engine('postgresql://tushare@localhost:5432/tushare') 
    # engine = create_engine('postgresql://postgres@47.93.193.128:5432/tushare')
    try:
        # 股票列表
        stock_basics = ts.get_stock_basics()
        data = pd.DataFrame(stock_basics)
        data.to_sql('stock_basics',engine,index=False,if_exists='replace')
        print("股票列表......done")

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

        # 风险警示板分类
        st_classified = ts.get_st_classified()
        data = pd.DataFrame(st_classified)
        data.to_sql('st_classified',engine,index=False,if_exists='replace')
        print("风险警示板分类......done")

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

schedule.every(60).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every(1).hour.do(job)
# schedule.every().day.at("17:00").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)


# def worker(msg, starttime):
#     print "time:", time.time(), "msg", msg, 'startTime', starttime
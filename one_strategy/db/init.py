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
    return HttpResponse('ok')

def job():
    print("I'm working...")
    engine = create_engine('postgresql://postgres@localhost:5432/tushare') 
    # engine = create_engine('postgresql://tushare@localhost:5432/tushare') 
    # engine = create_engine('postgresql://postgres@47.93.193.128:5432/tushare')
    try:
        stock_basics = ts.get_stock_basics()
        data = pd.DataFrame(stock_basics)
        data.to_sql('stock_basics',engine,index=False,if_exists='replace')

        industry_classified = ts.get_industry_classified()
        data1 = pd.DataFrame(industry_classified)
        data1.to_sql('industry_classified',engine,index=False,if_exists='replace')
    except Exception as e:
        print(e)

schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)


# def worker(msg, starttime):
#     print "time:", time.time(), "msg", msg, 'startTime', starttime
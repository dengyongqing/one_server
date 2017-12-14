import tushare as ts
from django.http import HttpResponse
import smtplib
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time,sched
import pandas as pd

def hello(request):
    # ts.get_stock_basics()
    stock_basics = ts.get_stock_basics()
    data = pd.DataFrame(stock_basics)
    data = data[(data['npr']>30) & (data['gpr']>30) & (data['rev']>20) & (data['profit']>20)]
    # data.filter("npr>30 and gpr>30 and rev>20 and profit>100")
    # data = data.filter("gpr>30")
    # data = data.filter("rev>20")
    # data = data.filter("profit>50")

    return HttpResponse(json.dumps(data))

def worker(msg, starttime):
    print "time:", time.time(), "msg", msg, 'startTime', starttime
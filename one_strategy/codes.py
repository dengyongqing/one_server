import tushare as ts
from django.http import HttpResponse
import smtplib
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time,sched


def hello(request):
    # ts.get_stock_basics()
    while True:  
      print 'time: ', time.time()  
      time.sleep(1) 
    return HttpResponse(json.dumps(ts.get_stock_basics()))

def worker(msg, starttime):
    print "time:", time.time(), "msg", msg, 'startTime', starttime
from sqlalchemy import create_engine
from django.http import HttpResponse
import json
import pandas as pd
import numpy as np
import tushare as ts
import time,sched

def init(request):
    while True:  
      print 'time: ', time.time()  
      time.sleep(3600) 
      engine = create_engine('postgresql://tushare@localhost:5432/tushare') 
      # ts.get_stock_basics()
      temp = ts.get_stock_basics()
      data = pd.DataFrame(temp)
    
      try:
          data.to_sql('stock_basics',engine,index=False,if_exists='append')
          # return HttpResponse(json.dumps(temp))
      except Exception as e:
          print(e)

def worker(msg, starttime):
    print "time:", time.time(), "msg", msg, 'startTime', starttime
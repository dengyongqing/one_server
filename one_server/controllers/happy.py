# -*- coding:utf-8 -*-  
# run_file_demo
from rqalpha import run_file
from rqalpha.api import *
from rqalpha import run_func
from rqalpha.utils import scheduler
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from one_server.one_strategy.strategies.happy import *
from one_server.db.db import get_db_connect
from django.conf import settings

import sys, os
import schedule
import time
import datetime
import gc
import tushare as ts
import pandas as pd

def happy(request):
    code = request.GET.get('code')
    if os.path.exists('./static/' + code + ".png"):
        return HttpResponseRedirect('http://' + request.get_host() + '/static/' + code + ".png")
    else:
        temp_run(code, 0)
        return HttpResponseRedirect('http://' + request.get_host() + '/static/' + code + ".png")
        # return HttpResponse('http://localhost:7777/static/' + code + ".png")

def temp_run(code, flag):
    now = datetime.datetime.now()
    year = int(now.strftime('%Y'))  
    today = now.strftime('%Y-%m-%d')  
    now = now.strftime("%Y-%m-%d %H:%M:%S")

    strategy_file_path = "./one_server/strategies/happy.py"

    engine = get_db_connect()
    read_sql_query = pd.read_sql_query('select * from my_stocks',con = engine)
    data = pd.DataFrame(read_sql_query)
    # print(data.code)
    # if data['code'] == code:
    #       print(data.iat[0])
    data = data[data['code'] == code]
    obj_dict = data.iloc[-1]
    temp_context = {'esp': obj_dict.esp, 'code': add_tag(code), 'projectName': settings.PROJECT_NAME}

    config = {
      "base": {
        "start_date": "2010-01-01",
        "end_date": today,
        "benchmark": "000300.XSHG",
        "accounts": {
            "stock": code,
        }
      },
      "extra": {
        "log_level": "error",
        "user_system_log_disabled": True,
        "context_vars": temp_context,
      },
      "mod": {
        "sys_analyser": {
          "enabled": True,
          "plot": False,
          # "output_file": './one_data/static/' + code + '.pkl',
          "plot_save_file": './static/' + code + '.png',
          # "plot_save_file": './static/' + row.code + '.png',
        }
      }
    }
    print('开始生成图片......' + code)
    run_func(init=init, before_trading=before_trading, handle_bar=handle_bar, config=config)
    # run_file(strategy_file_path, config)
    print('生成图片成功......' + code)

def add_tag(code):
      if len(code) == 5:
          return code + '.XHKG'
      elif code.startswith('6'):
          return  code + '.XSHG'
      elif code.startswith('3'):
          return code + '.XSHE'
      elif code.startswith('0'):
          return code + '.XSHE'

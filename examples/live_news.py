#! /usr/local/bin/python

# 接口: js_news
# 目标地址: https://www.jin10.com/
# 描述: 金十数据新闻资讯数据
# 限量: 当日最近 4 小时内的新闻资讯数据

import akshare as ak
from datetime import date, datetime

now = datetime.now()
js_news_df = ak.js_news(timestamp=now)
print(js_news_df)

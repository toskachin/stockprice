#! /usr/local/bin/python

import akshare as ak
import argparse
import datetime

today = datetime.datetime.now().strftime("%Y%m%d")
delay = datetime.timedelta(days = 3)
before = today - timedelta(days=3)
print(delay)
print(before)

def getArgs():
    parser = argparse.ArgumentParser(description='查询股票最近几天的价格')
    parser.add_argument('-i', '--stock_id', help='stock id', dest="stock_id",required=True)
    parser.add_argument('-s', '--start_date', help='start date', dest="start_date",default=today)
    parser.add_argument('-e', '--end_date', help='end date', dest="end_date",required=before)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
	args = getArgs()
	# stock_ids = []
	for stock_id in args.stock_id.split(','):
		try:
			stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol=stock_id, period="daily", start_date=args.start_date, end_date=args.end_date, adjust="")
			print(stock_zh_a_hist_df)
		except Exception as inst:
			raise

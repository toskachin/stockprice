#! /usr/local/bin/python

import akshare as ak
import pandas as pd
import datetime
import argparse


def getArgs():
    parser = argparse.ArgumentParser(description='涨停股票信息')
    parser.add_argument('-d', '--date', help='date', dest="date",required=True)
    args = parser.parse_args()
    return args

if __name__ == "__main__":
	args = getArgs()

today = datetime.datetime.now().strftime("%Y%m%d")
#连板股票池
#表头 代码  名称  总市值  最后封板时间  连板数  所属行业

stock_zt_pool_em_df = ak.stock_zt_pool_em(date=args.date)
lb_data = stock_zt_pool_em_df.iloc[:,[1,2,7,11,14,15]]
lb = lb_data.sort_values(by=['连板数'], ascending=False)
lb_filter = lb.loc[lb['连板数'] >= 2]
print(args.date + "涨停股票池")
print(lb)
lb.to_csv('daily_lb_{}.txt'.format(args.date),index=False)


#炸板股池
# 接口: stock_zt_pool_zbgc_em
# 目标地址: http://quote.eastmoney.com/ztb/detail#type=zbgc
# 描述: 东方财富网-行情中心-涨停板行情-炸板股池

stock_zt_pool_zbgc_em_df = ak.stock_zt_pool_zbgc_em(date=args.date)
zb = stock_zt_pool_zbgc_em_df.iloc[:,[1,2,3,7,11,15]]
print( args.date + "炸板股池" )
print(zb)
zb.to_csv('daily_zb_{}.txt'.format(args.date),index=False)

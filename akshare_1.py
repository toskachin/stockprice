#! /usr/local/bin/python

import akshare as ak
import pandas as pd
# stock_zh_a_hist_df = ak.stock_zh_a_hist(symbol="000568", period="daily", start_date="20220510", end_date='20220513', adjust="")
# print(stock_zh_a_hist_df)

# stock_zt_pool_em_df = ak.stock_zt_pool_em(date='20220513')
# print(stock_zt_pool_em_df)

# df = pd.DataFrame(stock_zt_pool_em_df)
# df.to_csv('akshare_1.csv')

stock_zt_pool_zbgc_df = ak.stock_zt_pool_zbgc_em(date='20220513')
print(stock_zt_pool_zbgc_df)
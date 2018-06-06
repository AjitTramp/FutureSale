import os
dir_nam='/home/ajit/Desktop/FutureSales'
os.chdir(dir_nam)
import warnings
import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import dateutil.parser
import datetime

train=pd.read_csv("sales_train_v2.csv")
submission=pd.read_csv("sample_submission.csv")
test=pd.read_csv("test.csv")

train['date']=train['date'].apply(lambda x:datetime.datetime.strptime(x, '%d.%m.%Y'))
monthly_sales=train.groupby(["shop_id","item_id"])["item_cnt_day"].mean()
s=monthly_sales.reset_index()

merged = pd.merge(test, s, how="left", on=["shop_id","item_id"])
merged["Item_cnt_month"]=merged["item_cnt_day"].fillna(0)
merged.to_csv('sub000.csv',columns=['ID','Item_cnt_month'],index=False)

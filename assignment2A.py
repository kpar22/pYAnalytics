# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:34:48 2020

@author: kshitij
"""
import numpy as np
import pandas as pd
mydata=pd.read_csv('denco.csv')

## Who are the most loyal Customers
cust_grp=mydata.groupby('custname')
agg0=cust_grp['custname'].agg(['count'])
print(agg0)

## Which customers contribute the most to their revenue
cust_grp=mydata.groupby('custname')
agg=cust_grp['revenue'].agg(np.sum)
res=agg.sort_values(ascending=False)
print(res)

## What part numbers bring in to significant portion of revenue
part_grp=mydata.groupby('partnum')
agg2=part_grp['revenue'].agg(np.sum)
res2=agg2.sort_values(ascending=False)
print(res2.head())

## What parts have the highest profit margin ?
part_grp=mydata.groupby('partnum')
agg3=part_grp['margin'].agg(np.sum)
res3=agg3.sort_values(ascending=False)
print(res3.head())


writer = pd.ExcelWriter('assignment2A.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
agg0.to_excel(writer, sheet_name='Question1')
res.to_excel(writer, sheet_name='Question2')
res2.to_excel(writer, sheet_name='Question3')
res3.to_excel(writer, sheet_name='Question4')

# Close the Pandas Excel writer and output the Excel file.
writer.save()

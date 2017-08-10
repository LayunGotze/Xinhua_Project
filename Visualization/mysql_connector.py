#!/usr/bin/python
# -*- coding:utf-8 -*-


import mysql_handle

def get_sql_res(start_time, end_time, location):
    sql= "select * from xinhua_data where timestamp>= "+str(start_time)+" and "+"timestamp<= "+str(end_time)+" and location = '"+ location +"'"
    print sql
    return mysql_handle.get_select(sql)



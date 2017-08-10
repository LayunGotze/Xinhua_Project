#!/usr/bin/python
# -*- coding:utf-8 -*-

"""CMySql类，简单的MySQL增删改查。事件、图谱数据库
@version: 0.1
@author: 代码疯子
"""
import os.path
try:
    import MySQLdb
except ImportError:
    raise ImportError("[E]: MySQLdb module not found!")

class CMySql(object):
    def __init__(self):
        self.Option = {"host" : "", "password" : "", "username" : "", "database" : "","port" : "","charset":""}
    
    def setoptions(self, host, pwd, user, db, port, charset):
        self.Option["host"] = host
        self.Option["password"] = pwd
        self.Option["username"] = user
        self.Option["database"] = db
        self.Option["port"]=port
        self.Option["charset"]=charset
    
    def start(self,fun,sqlstate):
        try:
            self.db = MySQLdb.connect(
                        host = self.Option["host"],
                        user = self.Option["username"],
                        passwd = self.Option["password"],
                        db = self.Option["database"],
                        port = self.Option["port"],
                        charset = self.Option["charset"]
            )
            return fun(sqlstate)
        except Exception, e:
            print e
            raise Exception("[E] Cannot connect to %s" % self.Option["host"])
        finally:
            try:
                self.close()
            except Exception, e:
                pass

    def create(self, sqlstate):
        """
        @todo: sqlstate可以自己改成其他参数，下同
        """
        self.cursor = self.db.cursor()
        self.cursor.execute(sqlstate) #创建
        self.db.commit()

    def insert(self, sqlstate):
        """
        @todo: 虽然函数名是insert，不过增删改都行
        """
        self.cursor = self.db.cursor()
        self.cursor.execute(sqlstate) #增、删、改
        self.db.commit()

    def query(self, sqlstate):
        self.cursor = self.db.cursor()
        self.cursor.execute(sqlstate) #查
        qres = self.cursor.fetchall()
        return qres
    
    def one_query(self, sqlstate):
        self.cursor = self.db.cursor()
        self.cursor.execute(sqlstate) #查
        qres = self.cursor.fetchall()[0]
        return qres
        
    def close(self):
        self.db.close()

def get_select(sqlstate):
    cm=CMySql()
    import ConfigParser
    config=ConfigParser.ConfigParser()
    file_dir=os.path.dirname(os.path.abspath(__file__))
    config.read(file_dir+"/db.ini")
    database_name = config.get("db", "db_name")
    host = config.get("db", "db_host")
    port = int(config.get("db", "db_port"))
    user = config.get("db", "db_user")
    pwd = config.get("db", "db_pass")
    # print(host,port,user,pwd)
    cm.setoptions(host=host,pwd=pwd,user=user,db=database_name,port=port,charset="utf8")
    return cm.start(cm.query,sqlstate)


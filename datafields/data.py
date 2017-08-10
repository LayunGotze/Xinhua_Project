#coding = utf-8
import csv
import MySQLdb

data = []

host='192.168.1.110'
user='huangfeiran'
passwd='huangfeiran'
db='xinhua'
port=3306
charset="utf8"

table="xinhua_data"
file_name = "EnvironmentalSensor.csv"
try:
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,port=port,charset=charset)
    cur=conn.cursor()
    sql = "create table "+table+"(timestamp int(11) NOT NULL, temperature varchar(12) NOT NULL,humidity varchar(12) NOT NULL, air_quality varchar(12) NOT NULL, cascophen varchar(12) NOT NULL, gas varchar(12) NOT NULL, particulate_matter varchar(12) NOT NULL, longititude varchar(12) NOT NULL, latitude varchar(12) NOT NULL, location varchar(30) NOT NULL) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
    cur.execute(sql)
    cur.close()
    conn.close()
    print table+" create success..."
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

try:
    conn = MySQLdb.connect(host=host,user=user,passwd=passwd,db=db,port=port,charset=charset)
    reader=csv.reader(file(file_name,'r'))
    data=[]
    for line in reader:
        break
    for line in reader:
        line.append("beijing")
        data.append(line)
    sql = "insert into "+table+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur=conn.cursor()
    cur.executemany(sql,data)
    conn.commit()
    conn.close()
    print table+" insert success..."
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])




'''
for line in reader:#jump first line
    break
for line in reader:
    timestamp = int(line[0])
    temperature = float(line[1])
    humidity = float(line[2])
    air_quality = int(line[3])
    cascophen = int(line[4])
    gas = int(line[5])
    particulate_matter = float(line[6])
    lon = float(line[7])
    lat = float(line[8])
    location = "beijing"
    element = {}
    element['timestamp'] = timestamp
    element['temperature'] = temperature
    element['humidity'] = humidity
    element['air_quality'] = air_quality
    element['cascophen'] = cascophen
    element['gas'] = gas
    element['particulate_matter'] = particulate_matter
    element['lon'] = lon
    element['lat'] = lat
    element['loction'] = location
    data.append(element)
print data
'''
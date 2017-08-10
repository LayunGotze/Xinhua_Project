# -*- coding:utf-8 -*-
import mysql_connector
import json
def data_analysis(data_form):
    start_time = int(data_form['start_time'])
    end_time = int(data_form['end_time'])
    location = data_form['location']
    weight = data_form['weight']
    mod = data_form['mod']
    print start_time,end_time,location,weight,mod###
    results = mysql_connector.get_sql_res(start_time,end_time,location)
    #################################
    news_text = "&nbsp;&nbsp;&nbsp;&nbsp;新华社内罗毕８月２８日电（记者吴宝澍、金正）针对日本首相安倍晋三在第六届日非峰会期间的所谓关于确保太平洋与印度洋航行自由的不当言论，外交部副部长张明２８日予以驳斥。在２７日于肯尼亚首都内罗毕举行的日非峰会开幕式上，安倍说，印度洋、太平洋连接亚洲和非洲，日本有责任推动两大洋成为“航行自由、尊重法治”的地区。 对此，２８日应邀参加日非峰会闭幕式的外交部副部长张明对记者说，２０１５年中非贸易额达１８００亿美元，中非之间的贸易相当一部分是依靠海运，走的就是印度洋、太平洋，除了中非贸易，中国和中东、中国和欧洲的贸易都是走这条航线，多年以来，这个区域的航行自由从来没有问题。张明说，日本政府在日非峰会前的一次高端会议上就已经提出所谓的航行自由问题，表现出要使日非峰会政治化的强烈意愿。而在此次高端会议上，所有发言的非洲国家一致反对、拒绝使会议政治化，最终日方不得不妥协，把相关内容从他们的建议草案中删除，这表明公道自在人心。张明强调，非洲当前的主要任务是发展和改善民生，有些人要把其他区域的问题拿来干扰非洲的发展是错误的。"
    extern_text = "&nbsp;&nbsp;&nbsp;&nbsp;空气是指地球大气层中的气体混合，为此，空气属于混合物，它主要由 氮气、氧气、稀有气体（氦、氖、氩、氪、氙、氡），二氧化碳以及其他物质（如水蒸气、杂质等）组合而成。其中氮气的体积分数约为78%，氧气的体积分数约为21%，稀有气体（氦、氖、氩、氪、氙、氡）的体积分数约为0.934%，二氧化碳的体积分数约为0.034%，其他物质（如水蒸气、杂质等）的体积分数约为0.002%。空气的成分不是固定的，随着高度的改变、气压的改变，空气的组成比例也会改变。但是长期以来人们一直认为空气是一种单一的物质，直到后来法国科学家拉瓦锡通过实验首先得出了空气是由氧气和氮气组成的结论。19世纪末，科学家们又通过大量的实验发现，空气里还有氦、氩、氙等稀有气体。"
    #####################################
    res = []
    for item in results:
        timestamp = int(item[0])
        temperature = float(item[1])
        humidity = float(item[2])
        air_quality = int(item[3])
        cascophen = int(item[4])
        gas = int(item[5])
        particulate_matter = float(item[6])
        lon = float(item[7])
        lat = float(item[8])
        temp = {}
        temp['timestamp'] = timestamp
        temp['temperature'] = temperature
        temp['humidity'] = humidity
        temp['air_quality'] = air_quality
        temp['cascophen'] = cascophen
        temp['gas'] = gas
        temp['particulate_matter'] = particulate_matter
        temp['lng'] = lon
        temp['lat'] = lat
        res.append(temp)
    res = {'data':json.dumps(res),'news_text':json.dumps(news_text),'extern_text':json.dumps(extern_text)}
    return res

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql as pymysql
from itemadapter import ItemAdapter
from pymongo import MongoClient

from . import settings


class OtherspiderPipeline:

    def __init__(self):
        host = settings.MONGODB_HOST
        port = settings.MONGODB_PORT
        dbname = settings.MONGODB_DBNAME

        # 创建MONGODB数据库链接
        self.client = MongoClient(host=host, port=port)
        # 指定数据库
        self.mydb = self.client[dbname]
        # 存放数据的数据库表名

    def open_spider(self, spider):
        """
        该方法用于创建数据库连接池对象并连接数据库
        """
        db = spider.settings.get('MYSQL_DB_NAME', 'mineinfo')
        host = spider.settings.get('MYSQL_HOST', '192.168.2.59')
        port = spider.settings.get('MYSQL_PORT', 3306)
        user = spider.settings.get('MYSQL_USER', 'root')
        passwd = spider.settings.get('MYSQL_PASSWORD', 'admin*123')

        self.db_conn = pymysql.connect(host=host, port=port, db=db, user=user, passwd=passwd, charset='utf8')
        self.db_cur = self.db_conn.cursor()

    def insert_db(self, item):
        """
        sql语句构造方法
        """
        values = (
            item['job'],
            item['company'],
            item['place'],
            item['salary']
        )

        sql = 'INSERT INTO jobs(job,company,place,salary) VALUES(%s,%s,%s,%s)'
        self.db_cur.execute(sql, values)

    def process_item(self, item, spider):
        if spider.name == 'ChinaNatureResourcePartPro':
            # # 存放数据的表名称
            MONGODB_SHEETNAME = "ChinaNatureResource"
            # self.write_mongo(MONGODB_SHEETNAME, item)
            values = (
                item['applicator'],
                item['project_name'],
                item['produce_type'],
                item['examining'],
                item['get_type'],
                item['main_mine'],
                item['create_time'],
            )

            sql = 'INSERT INTO mineinfo(applicator,project_name,produce_type,examining,get_type,main_mine,create_time) ' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s)'
            self.db_cur.execute(sql, values)
            return item


        elif spider.name == 'ChinaNatureResourcePart2Pro':
            # # 存放数据的表名称
            MONGODB_SHEETNAME = "ChinaNatureResource2"
            values = (
                item['applicator'],
                item['project_name'],
                item['produce_type'],
                item['examining'],
                item['get_type'],
                item['main_mine'],
                item['create_time'],
            )
            print(values)
            sql = 'INSERT INTO mineinfo(applicator,project_name,produce_type,examining,get_type,main_mine,create_time) ' \
                  'VALUES(%s,%s,%s,%s,%s,%s,%s)'
            self.db_cur.execute(sql, values)

        elif spider.name == 'TYCPro':
            # # 存放数据的表名称
            MONGODB_SHEETNAME = "TYCZBPro"
            self.write_mongo(MONGODB_SHEETNAME, item)

        elif spider.name == 'TYCNewsPro':
            # # 存放数据的表名称
            MONGODB_SHEETNAME = "TYCNewsPro"
            self.write_mongo(MONGODB_SHEETNAME, item)

        elif spider.name == 'QCCinfoUrl':
            # # 存放数据的表名称
            MONGODB_SHEETNAME = "QCCinfoUrl"
            self.write_mongo(MONGODB_SHEETNAME, item)

        elif spider.name == 'QCCinfoName':
            # # 存放数据的表名称
            MONGODB_SHEETNAME = "QCCinfoName"
            self.write_mongo(MONGODB_SHEETNAME, item)

    # def write_mysql(self,item):



    def close_spider(self, spider):
        """
        该方法用于数据插入以及关闭数据库
        """
        self.db_conn.commit()
        self.db_conn.close()


    def write_mongo(self, MONGODB_SHEETNAME, item):
        sheetname = MONGODB_SHEETNAME
        self.post = self.mydb[sheetname]
        # 调用spider 生成id 与key的方法
        self.mongoDbCount(item)

    def mongoDbCount(self, item):
        self.post.update_one(item, {'$set': item}, upsert=True)
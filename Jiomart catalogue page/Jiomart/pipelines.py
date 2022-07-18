# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector

class JiomartPipeline:
    
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='jiomart')
        

    def create_table(self):
        self.curr=self.conn.cursor()
        self.curr.execute("""DROP TABLE IF EXISTS data""" )
        self.curr.execute("""create table data(productcode varchar(100),displayname varchar(500),Mrp float,availability_status varchar(10),
        urlpath varchar(500),imageurl varchar(500))""")
        self.curr.close()
        
    def process_item(self,item,spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr= self.conn.cursor()
        self.curr.execute("""INSERT INTO data values (%s,%s,%s,%s,%s,%s)""",(
        item['productcode'],
        item['displayname'],
        item['mrp'],
        item['availablility_status'],
        item['urlpath'],
        item['imageurl']
        ))
        self.conn.commit()
        self.curr.close()
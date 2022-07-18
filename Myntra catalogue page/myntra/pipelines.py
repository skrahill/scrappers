# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class MyntraPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn=mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='root',
            database='myntra')
        

    def create_table(self):
        self.curr=self.conn.cursor()
        self.curr.execute("""DROP TABLE IF EXISTS data""" )
        self.curr.execute("""create table data(landingpageurl varchar(100),p_id int,Product varchar(100),Productname varchar(100),ratings float ,Brand varchar(100),Searchimage varchar(500),colour varchar(50),Category varchar(50),
                          Mrp float,Price float)""")
        self.curr.close()
        
    def process_item(self,item,spider):
        self.store_db(item)
        return item

    def store_db(self,item):
        self.curr= self.conn.cursor()
        self.curr.execute("""INSERT INTO data values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",(
        item['landingpageurl'],
        item['p_id'],
        item['Product'],
        item['Productname'],
        item['ratings'],
        item['Brand'],
        item['Searchimage'],
        item['colour'],
        item['Category'],
        item['Mrp'],
        item['Price']
        ))
        self.conn.commit()
        self.curr.close()








        

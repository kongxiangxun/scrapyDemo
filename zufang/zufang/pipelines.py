# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import  sqlite3

class ZufangPipeline(object):
    #这个函数是爬虫开始运行的时候执行，连接sqlite数据库可以放在这里
    def open_spider(self,spider):
        self.con=sqlite3.connect('zufang.sqlite');
        self.cu=self.con.cursor();
    #爬虫从html中分析得到数据，传入item,item被丢到管道文件中，被这个方法消费
    def process_item(self, item, spider):
        inset_sql="insert into zufang (title,money) values('{}','{}')".format(item['title'],item['money'])
        print(inset_sql)
        self.cu.execute(inset_sql);
        self.con.commit()
        print(spider.name,'piplines')
        return item
    #爬虫关闭时，所做的操作。一般是关闭文件和关闭数据库
    def spider_close(self,spider):
        self.con.close()

# 创建sqlite数据库，在Terminal中执行
# ipython
# import sqlite3 （引入类库）
# zufang=sqlite3.connect('zufang.sqlite') （创建数据库文件，这条命令，没有会创建zufang.sqlite数据库文件）
# create_table='create table zufang (title varchar(512),money varchar(128))' （编写脚本）
# zufang.execute(create_table) （执行数据库脚本）
# exit （退出）
# 拓展
# import sqlite3
# conn=sqlite3.connect("db.sqlite") #名称随意取，后缀也可以随意
# cu=conn.cursor()#cursor是光标的意思，在查询中很重要
# #在执行了查询语句之后，execute函数不会反悔任何结果，提取查询出来的结果，需要如下语句
# all_result=cu.fetchall()
# 注意：fetchall函数只能执行一次，执行第二次会无法获取，cu就是cursor，光标的意思
# 查询到结果之后，光标在数据头部；执行一次后，光标就跑到数据的尾部。
# 如果不需要再次拿到提取数据，只要在查询一次就可以了
# 当然，fetch有多个函数，fetchone,fetchall,fetchmany，分别提取一个，提取全部，提取多个【指定】
# 获取数据完成会后，一定要记得关闭 conn.close()

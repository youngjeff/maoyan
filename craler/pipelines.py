# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# coding:utf8
import pymysql.cursors
from craler.items import CralerItem
from craler import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB
MYSQL_charset = settings.MYSQL_utf8
cnx = pymysql.connect(host=MYSQL_HOSTS, user=MYSQL_USER, passwd=MYSQL_PASSWORD, db=MYSQL_DB, port=MYSQL_PORT,charset = MYSQL_charset)
cur = cnx.cursor()

from craler.items import CralerItem

class CralerPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item,CralerItem):
            sql = "SELECT * FROM movie WHERE id = '%s'" % (item['id'])

            try:
                cur.execute(sql)
                result = cur.fetchall()
                if len(result)>0:
                    print "already exist."
                    pass
                else:
                    cur.execute( 'insert into movie(id, name, score, tags, countries, duration,time) values(%s,%s,%s,%s,%s,%s,%s)',
                [item['id'], item['name'], item['score'], item['tags'], item['countries'], item['duration'], item['time']])
                    print "insert one infomation"
                # cur.close()
                cnx.commit()
                # cnx.close()
                
                return item
            except Exception, e:
                print e.message + e.args[0]

    @classmethod
    def check(self,url):
        sql = "SELECT * FROM urls WHERE urls = '%s'" % (url)
        cur.execute(sql)
        result = cur.fetchall()
        if len(result) > 0:
            print "already exist."
            return True
        else:
            cur.execute("insert into urls(urls) values(%s)", url)
            cnx.commit()
            return False
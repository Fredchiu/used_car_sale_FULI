# -*- coding: utf8 -*-
import requests,time,re,os,io
import urllib2
import random,sys
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from bs4 import BeautifulSoup


PATH='./'
index= time.strftime('%Y%m%d',time.localtime())

req = "http://www.flcar.com.tw/cars?plat=pc"
pat = '(?<=\.tw\Scars\S)+[0-9\.]+'
driver = webdriver.Chrome(PATH+'chromedriver')


def find_FCST(req):
    request = urllib2.Request(req) 
    request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36")
    response = urllib2.urlopen(request)
    html = response.read()
    soup = BeautifulSoup(html) 
    #print soup
    ### price data
    pat1='(?<="price">)+[0-9\.,]+'
    price=re.findall(pat1,str(soup)) #GET VALUE
    #print content1
    ### sale label
    pat2='(?<="sale-lebal\s)+[\w]+'
    status=re.findall(pat2,str(soup)) #GET status
    pat3='(?<=class="divTableCell">)+[0-9\.,]+'
    year,volume,mile,door=re.findall(pat3,str(soup)) 
    pat4='(?<=BENZ\S\S\S\S\S\S\S\S)[A-Za-z0-9\s\.-]+'
    item=re.findall(pat4,str(soup))
    return item,year,mile,price,status


driver.get(req)
driver.implicitly_wait(2)
select_city = Select(driver.find_element_by_name("county_id"))
select_city.select_by_value("1")
select_brand = Select(driver.find_element_by_name("brand_id"))
select_brand.select_by_value("4")
driver.implicitly_wait(5)
soup = BeautifulSoup(driver.page_source) 
content1=re.findall(pat,str(soup)) #GET benz number

car_table=pd.DataFrame(columns=['Number','Item','Year','Miles','Price','Status'])
for number in range(0,len(content1),2):
    item,year,mile,price,status = find_FCST('http://www.flcar.com.tw/cars/'+str(content1[number])+'?plat=pc')
    a=(content1[number],item,year,mile,price,status)
    car_table.append(a)
    time.sleep(random.randrange(60,100))

car_table.to_csv(PATH+str(index)+'_CAR_table.csv',sep=',')
print car_tabletable


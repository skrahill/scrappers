import selenium
from selenium import webdriver
from selenium.webdriver import chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
import mysql.connector

pin=int(input('enter pin code : '))
driver  = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://www.naturesbasket.co.in/Online-grocery-shopping/vegetables')
time.sleep(5)


loc=driver.find_element(By.CSS_SELECTOR,'input.servicablepin.headerspantext').click()
time.sleep(5)
loc1=driver. find_element(By.CSS_SELECTOR,("input[id='txt']")).click()
loc2=driver. find_element(By.CSS_SELECTOR,("input[id='txt']")).send_keys(pin)
time.sleep(5)
loc2=driver.find_element(By.CSS_SELECTOR,'input.btnCss').click()
time.sleep(5)
loc3=driver.find_element(By.CSS_SELECTOR,'input.btnCss').click()
time.sleep(5)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



conn = mysql.connector.connect(user='root', password='root', host='localhost', database='nature')


elements =driver.find_elements_by_xpath('//*[@pro-id]')


for i in elements:
    if elements.index(i)%2==0:
        
        
        productid=(i.get_attribute('pro-id'))
        #print('productid: ',productid)
        
        title=i.find_element(By.CSS_SELECTOR,'a.search_Ptitle.linkdisabled').get_attribute('title')
        #print('Title: ',title)
        
        try:
            size=i.find_element(By.CSS_SELECTOR,'div.search_PSelectedSize').text
            #print('Size: ',size)

        except NoSuchElementException:
            
            size='None'
            
        try:
            price=i.find_element(By.CSS_SELECTOR,'div.productlist-price').text
            #print(price)
            
        except NoSuchElementException:
            
            price='none'
        
        try:
            
            producturl=i.find_element(By.CSS_SELECTOR,'a').get_attribute('href')
            #print('product-url: ',producturl)
        except NoSuchElementException:
            
            producturl="none"
            
        try:
            imageurl=i.find_element(By.CSS_SELECTOR,'img').get_attribute('src')
           
            #print(imageurl)
            
        except NoSuchElementException:
            
            imageurl="none"
            
        a=(productid,title,size,price,producturl,imageurl)
        
        print(a)
        print()
    
    
        cursor = conn.cursor()
        sql = """INSERT INTO CATDATANATURE VALUES(%s,%s,%s,%s,%s,%s)"""
        cursor.execute(sql,a)
        conn.commit()
        conn.rollback()
conn.close()
    
            
            
            
        
    
    
    
        
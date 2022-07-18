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





location=input("Enter your location : ").strip()
driver  = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


driver.get('https://www.licious.in/chicken')
time.sleep(10)
loc=driver.find_element(By.CSS_SELECTOR,'div.location-name').click()
time.sleep(5)
loc1=driver.find_element(By.CSS_SELECTOR,'input.location-input').click()
time.sleep(5)
loc1=driver.find_element(By.CSS_SELECTOR,'input.location-input').send_keys(location)
time.sleep(5)
loc2=driver.find_element(By.CSS_SELECTOR,'div.autocomplete-address.suggestion').click()
time.sleep(10)
elements = driver.find_elements(by=By.CLASS_NAME,value="card")

conn = mysql.connector.connect(user='root', password='root', host='localhost', database='licious')

for i in elements:
    
    try:
        pid=i.get_attribute('data-prod')
        #print('product-ID : ',pid)
        
    except NoSuchElementException:
        pid='none'
        
        
    
    Title=i.find_element(By.CSS_SELECTOR,'span.product-name').text
    #print('Title : ',Title)
   
        
    try:
        Net_wt=i.find_element(By.CSS_SELECTOR,'span.net-weight').text
        #print(Net_wt)

    except NoSuchElementException:
        
        Net_wt='none'
        
        
        


    try:
        Gross_wt=i.find_element(By.CSS_SELECTOR,'span.gross-weight').text
        
        #print(Gross_wt)

    except NoSuchElementException:
        Gross_wt='none'

    try:
        price=i.find_element(By.CSS_SELECTOR,'span.rupee.remove-before').text
        #print(price)

    except NoSuchElementException:

        price='none'

    try:
        imageurl=i.find_element(By.CSS_SELECTOR,'img.product-image').get_attribute('data-lazy')
        #print(imageurl)

    except NoSuchElementException:
        imageurl='none'

    try:
        producturl=i.find_element(By.CSS_SELECTOR,'a').get_attribute('href')
        #print(producturl)

    except NoSuchElementException:
        
        producturl='none'
        
        
    a=(Title,pid,Net_wt,Gross_wt,price,imageurl,producturl)
    
    print(a)
    print()
    
    
    cursor = conn.cursor()
    sql = """INSERT INTO CATDATALICIOUS VALUES(%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql,a)
    conn.commit()
    conn.rollback()
conn.close()
    
    
    
    

    


    
  



        
        
        
   
        
        
        
        
        
  
            


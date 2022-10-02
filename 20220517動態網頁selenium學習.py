keyword=input('enter the image you want to search')
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import urllib
#擇一就好
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.google.com") # 更改網址以前往不同網頁
#x_path只要找到之後按右鍵複製xpath就可以，超簡單!!
link = driver.find_element_by_xpath('//*[@id="gb"]/div/div[1]/div/div[2]/a').click()
# 定位搜尋框
element = driver.find_element_by_class_name('gLFyf.gsfi')
# 傳入字串

element.send_keys(keyword)
#送出搜尋
element.send_keys(Keys.RETURN)
#driver.close() # 關閉瀏覽器視窗
imgs=driver.find_elements_by_class_name('rg_i.Q4LuWd')
#創建資料夾
#path=os.path.join('C:/Users/88696/Desktop/'+keyword)
#os.mkdir(path)
count=0
for img in imgs:
    if count ==10:
        break
    #print(img.get_attribute("src"))
    urllib.request.urlretrieve(img.get_attribute("src"),'{}_{}.jpg'.format(keyword,count))
    count+=1
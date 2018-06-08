# coding=utf-8

import os
from time import sleep
import datetime
import time
from selenium import webdriver

chromedriver = "/home/robot/selenium/chromedriver"
driver = webdriver.Chrome(chromedriver)

sleep(5)
# driver.get('http://www.baidu.com/')
driver.get("https://plogin.m.jd.com/user/login.action?appid=119&returnurl=http%3A%2F%2Fcredit.jd.com%2Fchannel%2Fcoupon.html%3Futm_medium%3Dundefined%26couponBusinessId%3D3a03ed87a4b19cab0adbb44e7f0e768e%26actId%3D004%26utm_term%3Dundefined%26agreementSource%3D74%26utm_source%3Dundefined%26utm_campaign%3Dundefined")
usename = "用户名"
password ="密码"

driver.find_element_by_id("username").send_keys(usename)
driver.find_element_by_id("password").send_keys(password)
sleep(2)
driver.find_element_by_id("loginBtn").click()
sleep(5)
js ="var q=document.documentElement.scrollTop=10000"
driver.execute_script(js)
sleep(3)
driver.find_element_by_class_name("banner-0").click()
sleep(5)
driver.execute_script("window.scrollTo(0,600)")
sleep(3)

def time_reduce():
    nowTime = datetime.datetime.now()
    now_time_stamp = time.mktime(nowTime.timetuple())
    end_time = datetime.datetime(2018,6,8,13,29,58) # 2018/06/04/ 17:59:58
    end_time_stamp = time.mktime(end_time.timetuple())
  
    print(end_time)
    print(nowTime)
    if end_time_stamp > now_time_stamp:
        return True
        print('没到开抢时间，请等待1秒')
    else:
        print('已经到开抢时间，开抢！')
        return False


while True:
    a = time_reduce()
    sleep(1)
    if a == False:
	driver.find_elements_by_class_name("large-coupon")[0].click()  # 抢50小白支付卷
	# driver.find_elements_by_class_name("large-coupon")[1].click()  # 抢6元运费
	print("抢没抢到啊，看你运气了，时间控制在57.5-58之间才可，页面的刷新得1点多秒，但是时间是一个对integer，"
          "不能设置成57.5,所以也看运气，看你的网页打开速度是2秒"
          "还是1秒，如果是1秒，就错过了 ")
        break


# 业务逻辑：
   # 通过一个循环，当时间到达你设置的抢票的时候的时候哦，时间终止，跳出循环，
   # 进行下一步操作
#抢50元支付卷
# while True:
#     time_reduce();
#     print('时间已经到了，可以开始抢了')
#     driver.find_elements_by_class_name("large-coupon")[0].click()

# 抢运费
# driver.find_element_by_class_name("large-coupon")[1].click()



from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("https://www.so.com/?src=so.com")
dr.maximize_window()
dr.implicitly_wait(10)#隐式等待
sleep(2)
#获取当前页面的标识码（句柄）
CurrentHandle = dr.current_window_handle

#定位登录按钮
dr.find_element_by_xpath('//*[@id="user-login"]').click()
sleep(1)
#定位找回密码
dr.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div/div[2]/form/div[6]/a[1]').click()
#获取已打开的两个页面的标识码（句柄）
AllHandles = dr.window_handles
for i in AllHandles:#遍历列表中的所有元素
    if i != CurrentHandle:#用每个元素去跟第一个标识码对比，如果不跟第一个相同，则是第二个页面的标识码
        dr.switch_to.window(i)#切换到第二个窗口

sleep(3)

#定位输入框
Username = dr.find_element_by_xpath('//*[@id="doc3"]/div[1]/div[2]/div/form/ul/li[1]/span[2]/input')
Username.clear()
Username.send_keys("我爱你")
sleep(2)

#关闭窗口
#dr.close()#关闭当前操作页面
dr.quit()#整个浏览器进程都杀了
#!/usr/bin/env python
#coding=utf8

from selenium import webdriver
driver=webdriver.Chrome()

driver.get("http://192.168.1.1")
#*****Login IN***** 
driver.find_element_by_xpath("//input[@id='username']").clear()
driver.find_element_by_xpath("//input[@id='username']").send_keys('CMCCAdmin')
driver.find_element_by_xpath("//input[@id='password']").send_keys('aDm8H%MdA')
# driver.find_element_by_id('password').send_keys('admin')
driver.find_element_by_xpath('//*[@id="fLogin"]/div[4]/a[1]').click()
print("****Login OK****")
#********检查WLAN页面配置******
driver.switch_to.frame('mainFrame')
driver.find_element_by_xpath('//*[@id="mmNet"]').click()
driver.find_element_by_xpath('//*[@id="smWLAN"]').click()
if driver.find_element_by_xpath('//*[@id="Frm_RadioStatus"]').is_enabled():
    print('检查无线配置')
else:
    print('无线配置未启用')

#********检查TR069预配置*******

# driver.find_element_by_xpath('//*[@id="wirelessSetup_5"]/div[2]/div/input').get_attribute('value')
# driver.find_element_by_link_text("Adv").click()
# driver.find_element_by_css_selector('a[href="./main.html#info"]').click()
# driver.find_element_by_link_text('Advance').click()
# 右键点击选择copy xpath
# driver.find_element_by_xpath("/html/body/form/section/fieldset[1]/div[1]/div[4]/div[1]/a").click()

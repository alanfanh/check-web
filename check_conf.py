#!/usr/bin/env python
#coding=utf-8
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get("http://192.168.1.1")

class Check_cfg(object):
    def __init__(self,**kargs):
        self.user="CMCCAdmin"
        self.pwd="aDm8H%MdA"
    def login(self):
        driver.find_element_by_xpath("//input[@id='username']").clear()       
        driver.find_element_by_xpath("//input[@id='username']").send_keys('CMCCAdmin')
        driver.find_element_by_xpath("//input[@id='password']").clear()
        driver.find_element_by_xpath("//input[@id='password']").send_keys('aDm8H%MdA')
        driver.find_element_by_xpath('//*[@id="fLogin"]/div[4]/a[1]').click()
        driver.switch_to.frame('mainFrame')
    def check_user(self):
        #检查是否存在user用户
        driver.find_element_by_xpath('//*[@id="mmManager"]').click()
        name=driver.find_element_by_xpath('//*[@id="Frm_Username"]').get_attribute('value')
        print(u'检查用户名:%s\r\n' % name)
        
    def check_wlan(self):
        # if self.login():
        print(u'****检查无线配置****\r\n')
            # driver.switch_to.frame('mainFrame')
        driver.find_element_by_xpath('//*[@id="mmNet"]').click()
        driver.find_element_by_xpath('//*[@id="smWLAN"]').click()
        time.sleep(0.3)
        if driver.find_element_by_xpath('//*[@id="Frm_RadioStatus"]').is_selected():
            print("****无线默认启用****")
            ssid_list=driver.find_element_by_xpath('//*[@id="Frm_SSID_SET"]').text
            print(u'页面可配置SSID为:\n\r%s\r\n' % ssid_list)
            print(u'----检查SSID1配置信息----')
            mode=driver.find_element_by_xpath('//*[@id="Frm_DataRates"]').get_attribute('value')
            print(u'SSID1无线工作模式:%s' % mode)
            ssid=driver.find_element_by_xpath('//*[@id="Frm_ESSID"]').get_attribute('value')
            print(u'SSID1默认名称(CMCC后一部分):%s' % ssid)
            wpa_mode=driver.find_element_by_xpath('//*[@id="Frm_Authentication"]').get_attribute('value')
            print(u'SSID1无线加密模式:%s' % wpa_mode)
            wlpwd=driver.find_element_by_xpath('//*[@id="Frm_KeyPassphrase"]').get_attribute('value')
            print(u'SSID1密钥:%s' % wlpwd)
            en=driver.find_element_by_xpath('//*[@id="Frm_ESSIDHideEnable"]').is_selected()
            print(u'SSID1广播取消是否开启:%s\r\n' % en)
            print(u'----检查SSID5配置信息----')
            driver.find_element_by_xpath('//*[@id="Frm_SSID_SET4"]').click()
            mode=driver.find_element_by_xpath('//*[@id="Frm_DataRates"]').get_attribute('value')
            print(u'SSID5无线工作模式:%s' % mode)
            ssid=driver.find_element_by_xpath('//*[@id="Frm_ESSID"]').get_attribute('value')
            print(u'SSID5默认名称(CMCC后一部分):%s' % ssid)
            wpa_mode=driver.find_element_by_xpath('//*[@id="Frm_Authentication"]').get_attribute('value')
            print(u'SSID5无线加密模式:%s' % wpa_mode)
            wlpwd=driver.find_element_by_xpath('//*[@id="Frm_KeyPassphrase"]').get_attribute('value')
            print(u'SSID5密钥:%s' % wlpwd)
            en=driver.find_element_by_xpath('//*[@id="Frm_ESSIDHideEnable"]').is_selected()
            print(u'SSID5广播取消是否开启:%s\r\n' % en)
        else:
            print("无线配置未启用")
            return False
    def check_tr069(self):
        print(u'****检查TR069页面配置****')
        # driver.switch_to.frame('mainFrame')
        driver.find_element_by_xpath('//*[@id="mmNet"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="smTR069"]').click()
        if driver.find_element_by_xpath('//*[@id="Frm_Tr069Enable"]').is_selected():
            rms_edit=driver.find_element_by_xpath('//*[@id="Frm_Tr069Enable"]').is_enabled()
            url=driver.find_element_by_xpath('//*[@id="Frm_URL"]').get_attribute('value')
            cpe_usr=driver.find_element_by_xpath('//*[@id="Frm_UserName"]').get_attribute('value')
            cpe_pwd=driver.find_element_by_xpath('//*[@id="Frm_UserPassword"]').get_attribute('value')
            req_usr=driver.find_element_by_xpath('//*[@id="Frm_ConnectionRequestUsername"]').get_attribute('value')
            req_pwd=driver.find_element_by_xpath('//*[@id="Frm_ConnectionRequestPassword"]').get_attribute('value')
            cpe_time=driver.find_element_by_xpath('//*[@id="Frm_PeriodicInformInterval"]').get_attribute('value')
            print(u"TR069开关是否可编辑:%s\nurl地址:%s\n平台认证终端帐号:%s\n平台认证终端帐号密码(需手工后台查看):%s\n终端认证平台帐号:%s\n终端认证平台密码(需手工后台查看):%s\n周期上报时间(秒):%s" % (rms_edit,url,cpe_usr,cpe_pwd,req_usr,req_pwd,cpe_time,))
            print('******TR069页面配置读取完毕******')
        else:
            print(u'****Tr069默认未启用****')
    def check_qos(self):
        pass
    def check_wan(self):
        print(u'****检查WAN配置信息****')
        driver.find_element_by_xpath('//*[@id="mmNet"]').click()
        #检查MTU默认值及是否可配置
        mtu=driver.find_element_by_xpath('//*[@id="Frm_MTU"]').get_attribute('value')
        mtu_en=driver.find_element_by_xpath('//*[@id="Frm_MTU"]').is_enabled()
        #检查拨号模式
        mode=driver.find_element_by_xpath('//*[@id="Frm_ConnTrigger"]').text
        m=driver.find_element_by_xpath('//*[@id="Frm_ConnTrigger"]')
        mm=Select(m)
        default_mode=mm.first_selected_option.text
        print(u"默认MTU值:%s\nMTU是否可配置:%s\n拨号模式:%s\n默认拨号模式:%s\n" % (mtu,mtu_en,mode,default_mode))
        #检查tr069-WAN
        wan=driver.find_element_by_xpath('//*[@id="Frm_WANCName0"]')
        ww=Select(wan)
        ww.select_by_value('0')
        wan=driver.find_element_by_xpath('//*[@id="Frm_WANCName0"]')
        ww=Select(wan)
        tr069_name=ww.first_selected_option.text
        protocol=driver.find_element_by_xpath('//*[@id="Frm_protocol"]').get_attribute('value')
        mode=driver.find_element_by_xpath('//*[@id="Frm_mode"]').get_attribute('value')
        pri=driver.find_element_by_xpath('//*[@id="Frm_Priority"]').get_attribute('value')
        vlan=driver.find_element_by_xpath('//*[@id="Frm_VLANID"]').get_attribute('value')
        tr_mtu=driver.find_element_by_xpath('//*[@id="Frm_MTU"]').get_attribute('value')
        print(u'检查tr069-WAN:\r\ntr069连接名字:%s\r\ntr069连接使用的协议:%s\r\n接入方式:%s\r\nQos优先级:%s\r\ntr069连接vlan:%s\r\ntr069连接MTU值:%s\r\n' % (tr069_name,protocol,mode,pri,vlan,tr_mtu))
        #检查Internet-WAN
        driver.find_element_by_xpath('//*[@id="mmNet"]').click()
        #切换ipv6双栈
        protocol=driver.find_element_by_xpath('//*[@id="Frm_protocol"]')
        pro=Select(protocol)
        pro.select_by_value('IPv4/v6')
        #切换至默认WAN
        wan=driver.find_element_by_xpath('//*[@id="Frm_WANCName0"]')
        ww=Select(wan)
        ww.select_by_value('1')
        wan=driver.find_element_by_xpath('//*[@id="Frm_WANCName0"]')
        ww=Select(wan)
        wan_name=ww.first_selected_option.text
        wan_mode=driver.find_element_by_xpath('//*[@id="Frm_mode"]').get_attribute('value')
        wan_pri=driver.find_element_by_xpath('//*[@id="Frm_Priority"]').get_attribute('value')
        wan_vlan=driver.find_element_by_xpath('//*[@id="Frm_VLANID"]').get_attribute('value')
        wan_mtu=driver.find_element_by_xpath('//*[@id="Frm_MTU"]').get_attribute('value')
        print(u'检查Internet-WAN相关配置\r\n默认WAN连接名字:%s\r\n接入方式%s\r\nQos优先级:%s\r\nWAN连接Vlan:%s\r\nWAN连接MTU值:%s\r\n' % (wan_name,wan_mode,wan_pri,wan_vlan,wan_mtu))
        #检查Sip-WAN
        print(u'')
    
    def check_iptv(self):
        print(u'****检查IPTV-WAN和组播vlan相关配置****\r\n')
        driver.find_element_by_xpath('//*[@id="mmNet"]').click()
        wan=driver.find_element_by_xpath('//*[@id="Frm_WANCName0"]')
        wan_int=Select(wan)
        wan_int.select_by_value('2')
        int=driver.find_element_by_xpath('//*[@id="Frm_WANCName0"]')
        interface=Select(int)
        wan_name=interface.first_selected_option.text
        vid=driver.find_element_by_xpath('//*[@id="Frm_VLANID"]').get_attribute('value')
        pri=driver.find_element_by_xpath('//*[@id="Frm_Priority"]').get_attribute('value')
        driver.find_element_by_xpath('//*[@id="ssmMcVlan"]/div').click()
        mvlan=driver.find_element_by_xpath('//*[@id="Special_Table"]/tbody/tr[3]/td[2]').text
        
        print(u'IPTV连接名字:%s\nIPTV连接Vlan:%s\n连接Qos优先级:%s\n公共组播Vlan:%s\n' % (wan_name,vid,pri,mvlan))
        print(u'****检查完成****\r\n')
    def check_igmp(self):
        print(u'检查IGMP相关设置')
        driver.find_element_by_xpath('//*[@id="mmApp"]').click()
        driver.find_element_by_xpath('//*[@id="smIGMP"]').click()
        snoop_en=driver.find_element_by_xpath('//*[@id="Frm_Enable"]').is_selected
        print(u'IGMP Snooping是否启用:%s' % snoop_en) 
    def check_sip(self):
        print(u'****检查宽带电话设置页面配置****')
        # driver.switch_to.frame('mainFrame')
        driver.find_element_by_xpath('//*[@id="mmApp"]').click()
        driver.find_element_by_xpath('//*[@id="smVoIP"]').click()
        driver.find_element_by_xpath('//*[@id="Frm_ServerType"]').get_attribute('value')
        s=driver.find_element_by_xpath('//*[@id="Frm_ServerType"]')
        ss=Select(s)
        sip=ss.first_selected_option.text
        #前往基本通话控制页面，检查位见短定时器
        driver.find_element_by_xpath('//*[@id="ssmBasicCon"]').click()
        time=driver.find_element_by_xpath('//*[@id="Frm_ShortTimer"]').get_attribute('value')
        #前往状态页面检查语音注册状态
        driver.find_element_by_xpath('//*[@id="mmStatus"]').click()
        driver.find_element_by_xpath('//*[@id="smVOIPStatu"]').click()
        sip_status=driver.find_element_by_xpath('//*[@id="TestContent"]/tbody/tr[2]/td[2]').text
        print(u"SIP功能语音协议:%s\n位间短定时器:%s\n语音注册状态:%s" % (sip,time,sip_status))
        print(u"****宽带电话页面配置检查完成****")
    def check_dmz(self):
        print(u'****检查NAT_DMZ页面配置****')
        # driver.switch_to.frame('mainFrame')
        driver.find_element_by_xpath('//*[@id="mmApp"]').click()
        driver.find_element_by_xpath('//*[@id="smFwAlg"]').click()
        driver.find_element_by_xpath('//*[@id="ssmDMZHost"]/div').click()
        dmz=driver.find_element_by_xpath('//*[@id="Frm_Enable"]').is_selected()
        print(u"DMZ功能是否启用(True代表是，False代表否):%s" % dmz)
        print(u"****DMZ页面配置检查完成****")
    def check_alg(self):
        print(u'****检查NAT_Alg页面配置****')
        # driver.switch_to.frame('mainFrame')
        driver.find_element_by_xpath('//*[@id="mmApp"]').click()
        driver.find_element_by_xpath('//*[@id="smFwAlg"]').click()
        sip=driver.find_element_by_xpath('//*[@id="Frm_IsSIPAlg"]').is_selected()
        h323=driver.find_element_by_xpath('//*[@id="Frm_IsSIPAlg"]').is_selected()
        rtsp=driver.find_element_by_xpath('//*[@id="Frm_IsSIPAlg"]').is_selected()
        pptp=driver.find_element_by_xpath('//*[@id="Frm_IsSIPAlg"]').is_selected()
        l2tp=driver.find_element_by_xpath('//*[@id="Frm_IsSIPAlg"]').is_selected()
        ipsec=driver.find_element_by_xpath('//*[@id="Frm_IsSIPAlg"]').is_selected()
        ftp=driver.find_element_by_xpath('//*[@id="Frm_IsSIPAlg"]').is_selected()
        print(u"sip开关是否启用:%s\nh323开关是否启用:%s\nrtsp开关是否启用:%s\npptp开关是否启用:%s\nl2tp开关是否启用:%s\nipsec开关是否启用:%s\nftp开关是否启用:%s" % (sip,h323,rtsp,pptp,l2tp,ipsec,ftp,))
        print(u'****ALG页面配置检查完成****')
    def check_ntp(self):
        print(u'****检查ntp配置****')
        # driver.switch_to.frame('mainFrame')
        driver.find_element_by_xpath('//*[@id="mmNet"]').click()
        driver.find_element_by_xpath('//*[@id="smSNTP"]').click()
        ntp=driver.find_element_by_xpath('//*[@id="Frm_Enable"]').is_selected()
        print(u'检查ntp是否启用(True代表是，False代表否):%s' % ntp)

def main(self):
    pon=check_cfg()
    pon.login()
    pon.check_sip()


if __name__ == "__main__":
    # main()
    pon=Check_cfg()
    pon.login()
    pon.check_user()
    pon.check_wlan()
    # pon.check_iptv()
    # pon.check_sip()
    # pon.check_dmz()
    # pon.check_alg()
    # pon.check_ntp()
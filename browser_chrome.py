# -*- coding: utf-8 -*
import sys
import os
import signal

file_path_old= '/root/job_2021/rlsbj.cq.gov.cn_zwxx_182.pkl'
web_url="http://rlsbj.cq.gov.cn/zwxx_182/sydw/"
email_title= "事业："+web_url
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


from datetime import datetime
from bs4 import BeautifulSoup
import os
import sys
sys.setrecursionlimit(100000)
import pickle
import requests
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import psutil



def chrome_broswer(web_url):
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15")
    browser = webdriver.Chrome(options=chrome_options)
    
    browser.implicitly_wait(20)
    browser.get(web_url)
    
    #time.sleep(20)
    html = browser.page_source
    chromepid = int(browser.service.process.pid)
    process_id = psutil.Process(browser.service.process.pid)
    print(chromepid )
    #print([ child.pid for child in process_id.children(recursive=True)])
    all_childs_id = [ child.pid for child in process_id.children(recursive=True)]
    #print(process_id.getchildren(recursive=True) )
    browser.close()
    browser.quit()
    all_childs_id.append(chromepid)
    try:
        #os.kill(chromepid , signal.SIGTERM)
       # os.kill(chromepid , signal.SIGTERM)
        print(all_childs_id)
        for i in all_childs_id:
            try:
                os.kill(i , signal.SIGTERM)
            #psutil.Process(i).kill()
            except:
                print("os.kill {} err".format(i))
    except:
        print("os.kill error")

    #browser.close()
    #browser.quit()

    return html

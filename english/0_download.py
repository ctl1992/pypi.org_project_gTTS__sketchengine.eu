from time import sleep

import pandas
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
lessEqualFrequency = 11902
delay = 240  # seconds
def login():
    driver.get('https://auth.sketchengine.eu/#login')
    # driver.set_window_size(1616, 876)
    sleep(5)
    driver.find_elements_by_css_selector("#r_0")[1].send_keys("chentianle")
    driver.find_elements_by_css_selector("#r_1")[1].send_keys("ysLLz6nSvm7K")
    driver.find_element_by_css_selector("#btnLogin").click()
    sleep(5)

    pass


def waitForDownload():
    for seconds in range(0, 2000):
        sleep(1)
        for filename in os.listdir("C:\\Users\\Pc\\Downloads\\"):
            if filename.endswith(".xlsx"):
                return
    pass


def downloadXlsx():
    try:
        url = "https://app.sketchengine.eu/#wordlist?corpname=preloaded%2Fententen20_tt31&tab=advanced&wlmaxfreq=" + str(lessEqualFrequency)
        # search form
        driver.get(url)
        # sleep(delay)
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'btnGoAdv')))
        print("loaded succeed:" + url)
        # searching
        driver.find_element_by_css_selector("#btnGoAdv").click()
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'btndownload')))
        # download json failed
        # url = "https://app.sketchengine.eu/bonito/run.cgi/wordlist?corpname=preloaded/ententen20_tt31&results_url=https://app.sketchengine.eu/#wordlist?corpname=preloaded%2Fententen20_tt31&tab=advanced&wlmaxfreq="+str(lessEqualFrequency)+"&showresults=1&wlmaxitems=20000&wlsort=frq&wlattr=lc&wlpat=.*&wlminfreq=5&wlicase=1&wlmaxfreq="+str(lessEqualFrequency)+"&wltype=simple&include_nonwords=0&random=0&relfreq=1&reldocf=1&wlpage=1"
        # driver.get(url)
        # content = driver.page_source
        # print(content)


        # btn download xlsx to c:
        # 以下三行不能点击可能是因为元素不在可见区域
        # driver.find_element_by_css_selector("#btndownload > i").click() #Element <i class="material-icons">...</i> is not clickable at point (814, 20)
        # driver.find_element_by_css_selector("#btndownload").click() # Element <a id="btndownload" class="btn btn-floating  btn-flat ">...</a> is not clickable
        # driver.find_element_by_css_selector("#app > crystal-app > page-router > div > div > div > 0_wordlist-result-options > feature-toolbar > div.bar.right > ul > li:nth-child(2)").click()  # <li class="ft-tooltip" data-tooltip="Download">...</li> is not clickable at point (814, 20). Other element would receive the click: <div id="toast-container">...</div>
        # # Clicking at coordinates
        ac = ActionChains(driver)
        elem = driver.find_element_by_css_selector("#btndownload")
        ac.move_to_element(elem).move_by_offset(2, 2).click().perform()
        sleep(20)
        # WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, '#activeOptionsWrapper > div > div.optsContent > div > div.row.dividerBottom.pb-8 > span > a:nth-child(2)')))
        # driver.find_element_by_css_selector("#activeOptionsWrapper > div > div.optsContent > div > div.row.dividerBottom.pb-8 > span > a:nth-child(2)").click() # element not interactable
        ac = ActionChains(driver) # dom对象已经改变，需要重新实例化对象，否则无法找到新增元素
        elem = driver.find_element_by_css_selector("#activeOptionsWrapper > div > div.optsContent > div > div.row.dividerBottom.pb-8 > span > a:nth-child(2)")
        ac.move_to_element(elem).move_by_offset(2, 2).click().perform()
        waitForDownload()

        # mv C:\Users\Pc\Downloads\wordlist_preloaded_ententen20_tt31_*.xlsx
        # to E:\Users\Pc\PycharmProjects\pypi.org_project_gTTS__sketchengine.eu\english\0_wordlist\wordlist_preloaded_ententen20_lessEqual_2259427253.xlsx

        # url download
        # url = "https://app.sketchengine.eu/bonito/run.cgi/wordlist?corpname=preloaded/ententen20_tt31&results_url=https://app.sketchengine.eu/#wordlist?corpname=preloaded%2Fententen20_tt31&tab=advanced&wlmaxfreq="+str(lessEqualFrequency)+"&showresults=1&wlmaxitems=1000&wlsort=frq&wlattr=lc&wlpat=.*&wlminfreq=5&wlicase=1&wlmaxfreq="+str(lessEqualFrequency)+"&wltype=simple&include_nonwords=0&random=0&relfreq=0&reldocf=0&wlpage=1&page=1&format=xlsx&format=xlsx"
        # driver.get(url)
        # content = driver.page_source
        pass



    except TimeoutException:
        print("Timeout loaded: webPage less equal "+ str(lessEqualFrequency) )


def mvXlsx2English():
    for filename in os.listdir("C:\\Users\\Pc\\Downloads\\"):
        if filename.endswith(".xlsx"):
            wordListXlsx = pandas.read_excel("C:\\Users\\Pc\\Downloads\\"+filename, header=3)

            dropLastNRow = 0
            while dropLastNRow >= -998:
                if wordListXlsx['Frequency'].iloc[dropLastNRow-1] == wordListXlsx['Frequency'].iloc[dropLastNRow-2]:
                    dropLastNRow = dropLastNRow -1
                else:
                    break
            global lessEqualFrequency  # 声明修改全局变量，而不是局部变量
            if dropLastNRow == 0 :
                wordListXlsx.to_excel(
                    "E:\\Users\\Pc\\PycharmProjects\\pypi.org_project_gTTS__sketchengine.eu\\english\\0_wordlist\\wordlist_preloaded_ententen20_lessEqual_" + str(
                        lessEqualFrequency) + ".xlsx", index=False, startrow=3)
            else:
                wordListXlsx[:dropLastNRow].to_excel(
                    "E:\\Users\\Pc\\PycharmProjects\\pypi.org_project_gTTS__sketchengine.eu\\english\\0_wordlist\\wordlist_preloaded_ententen20_lessEqual_" + str(
                        lessEqualFrequency) + ".xlsx", index=False, startrow=3)
            os.remove("C:\\Users\\Pc\\Downloads\\"+filename)
            lessEqualFrequency = wordListXlsx['Frequency'].iloc[-1]
    pass


#
login()
while (lessEqualFrequency>=5):
    downloadXlsx()
    mvXlsx2English()
pass

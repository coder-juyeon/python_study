from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
from flask import Flask


# 필요한 라이브러리 및 모듈

# ChromeDriverManager으로 Chrome 드라이버를 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

import time

# 브라우저가 종료되지 않게 설정
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 오류 메시지를 비활성화
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# Chrome 드라이버를 ChromeDriverManager를 사용하여 설정
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.implicitly_wait(5)  # 웹페이지가 로딩될 때까지 5초 동안 대기합니다.
driver.maximize_window()  # 브라우저 창을 최대화합니다.
driver.get("https://www.jobkorea.co.kr/recruit/joblist?menucode=search")  # 잡코리아 웹사이트를 엽니다.

# 잡코리아의 상세 검색 조건 탭을 클릭합니다.
time.sleep(1)
dev_tab_1 = driver.find_element(By.CSS_SELECTOR, "#devSearchForm > div.detailArea > div > div:nth-child(1) > dl.job.circleType.dev-tab.dev-duty > dt")
dev_tab_1.click()
time.sleep(1)
dev_tab_2 = driver.find_element(By.CSS_SELECTOR, '#devSearchForm > div.detailArea > div > div:nth-child(1) > dl.job.circleType.dev-tab.dev-duty.on > dd.ly_sub > div.ly_sub_cnt.colm3-ty1.clear > dl:nth-child(1) > dd > div.nano-content.dev-main > ul > li:nth-child(6) > label')
dev_tab_2.click()
time.sleep(1)
dev_tab_3 = driver.find_element(By.CSS_SELECTOR,'#duty_step2_10031_ly > li:nth-child(2) > label')
dev_tab_3.click()
time.sleep(1)
dev_tab_4 = driver.find_element(By.CSS_SELECTOR, '#devSearchForm > div.detailArea > div > div:nth-child(1) > dl.exp.circleType.dev-tab.dev-career > dt')
dev_tab_4.click()
time.sleep(1)
dev_tab_5 = driver.find_element(By.CSS_SELECTOR, '#devSearchForm > div.detailArea > div > div:nth-child(1) > dl.exp.circleType.dev-tab.dev-career.on > dd > div.nano-content > ul.expSel > li:nth-child(1) > label')
dev_tab_5.click()
time.sleep(1)

dev_tab_6 = driver.find_element(By.CSS_SELECTOR, "#dev-btn-search")
dev_tab_6.click()
time.sleep(2)

global_parameter = None


index = 0
last_page = False
        
def get_json_FrontEnd_jobs():
    ...
    index = 0
    last_page = False
    jobs = []
    json_data = [] 
    
    while not last_page:
        jobkoreaInfos = driver.find_elements(By.CSS_SELECTOR, "#dev-gi-list div.tplList.tplJobList > table > tbody > tr.devloopArea")
        for item in jobkoreaInfos:
            textinfo = []
            index += 1
            companyName = item.find_element(By.CSS_SELECTOR,"td.tplCo > a.normalLog").text
            postingName = item.find_element(By.CSS_SELECTOR,"td.tplTit > div > strong > a.normalLog").text
            companyInfo = item.find_elements(By.CSS_SELECTOR, 'p.etc > span.cell')
            date = item.find_element(By.CSS_SELECTOR, ".date.dotum").text
            
            for info in companyInfo:
                textinfo.append(info.text)
            result = ', '.join(textinfo)
            job_info = f"{companyName} | {postingName}\n채용조건 : {result.strip(', ')}\n마감일 : {date.replace(' ', '')}\n"
            jobs.append(job_info)
            data = {
                '회사이름' : companyName,
                '공고' :  postingName,
                '채용조건' : result.strip(', '),
                '마감일' : date.replace(' ', '')
            }
            json_data.append(data)
            

        try:
            span_element = driver.find_element(By.CSS_SELECTOR, '#dvGIPaging .tplPagination.newVer ul li span.now')
            next_li_element = span_element.find_element(By.XPATH, "../following-sibling::li[1]")
            if 'active' in next_li_element.get_attribute('class'):
                last_page = True
            else:
                next_li_element.click()
                time.sleep(2)
        except NoSuchElementException:
            print("마지막 페이지에 도달하였습니다.")
            last_page = True
        result = json.dumps(json_data, ensure_ascii=False)
    return result

global_parameter = get_json_FrontEnd_jobs()






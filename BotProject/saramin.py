from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import json

from flask import Flask

# 사람이 한것처럼 하기
import time
import pyautogui
import pyperclip

import discord
from discord.ext import commands


#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

intents = discord.Intents.all()
intents.typing = False  # typing 이벤트 비활성화
intents.presences = False  # presence 이벤트 비활성화
intents.message_content = True #v2

#브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# 웹페이지 해당 주소 이름
driver.implicitly_wait(3) # 웹페이지가 로딩 될때까지 5초를 기다린다.
driver.maximize_window() # 화면 최대화

# 디스코드에서 사용할 수 있게 함수로 선언
def crawling_data(searchText):
    # 첫 페이지 로드
    driver.get(f"https://www.saramin.co.kr/zf_user/jobs/list/job-category?&cat_kewd=84&loc_mcd=101000&keydownAccess=&exp_cd=1&searchword={searchText}&searchType=recently&panel_type=&search_optional_item=y&search_done=y&panel_count=y&preview=y")

    # josn으로 restAPI에 담을 변수 선언
    result_json = []

    # 사람인 검색결과 div
    saramin_search_results = driver.find_elements(By.CSS_SELECTOR, ".list_item")

    # 사람인 채용 정보 가져오기
    for info in saramin_search_results:
        # 사용 언어 리스트 변수
        notification_meta_result = []

        # 채용회사
        company_name = info.find_element(By.CSS_SELECTOR, ".company_nm > a > span").text
        # print(f"compay_name: {company_name}")

        # 채용 제목
        notification_info_job_title = info.find_element(By.CSS_SELECTOR, ".notification_info .job_tit span").text
        # print(f"notification_info_job_title: {notification_info_job_title}")

        # 사용 언어 
        notification_info_job_metas = info.find_elements(By.CSS_SELECTOR, ".notification_info .job_meta span")

        for meta in notification_info_job_metas:
            job_meta_text = meta.text
            """ print(f"job_meta_text: {job_meta_text}") """
            notification_meta_result.append(job_meta_text)

        # print(f"notification_meta_result 첫번째: {notification_meta_result[0]}")

        # 근무 장소
        work_place = info.find_element(By.CSS_SELECTOR, ".company_info .work_place").text
        # print(f"work_place: {work_place}")

        # 마감일
        deadlines = info.find_element(By.CSS_SELECTOR, ".support_info .deadlines").text
        deadline = deadlines.split('\n')[0]
        # print(f"deadline: {deadline}")
    
        # json으로 변환
        data = {
            '채용회사': company_name,
            '채용제목': notification_info_job_title,
            '사용언어': notification_meta_result[0],
            '근무장소': work_place,
            '마감일': deadline
        }
        result_json.append(data)
    json_data = json.dumps(result_json, ensure_ascii=False)
    return json_data



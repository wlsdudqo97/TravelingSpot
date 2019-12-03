#!/usr/bin/env python
# coding: utf-8

# 모듈 접근

from selenium import webdriver
import time
import pandas as pd
from pandas import DataFrame as df


a = [] #리뷰데이터를 담는 리스트
b = [] #평점을 담는 리스트

#첫번째 for문은 전체 페이지 수를 돌리기 위한 for문
#두번째 for문은 한 페이지 내에 있는 리뷰와 평점 데이터를 가져오기 위한 for문
for i in range(0,20,10):
        url_str = "https://www.tripadvisor.co.kr/Attraction_Review-g294197-d324888-Reviews-or"
        url_num = str(i)
        url_keyword = "-Gyeongbokgung_Palace-Seoul.html"

        total_url = url_str + url_num + url_keyword
    
        driver = webdriver.Chrome("C:/ProgramData/Anaconda3/chromedriver.exe")
    
        driver.get(total_url)

        time.sleep(1)

        driver.find_elements_by_css_selector(".ulBlueLinks")[0].click()
        

        for j in range(0,10,1):
            reviews = driver.find_elements_by_css_selector(".review-container")
            rating_code = reviews[j].find_element_by_css_selector(".ui_bubble_rating")
        
            cls_attr = rating_code.get_attribute("class")
            cls_attr = str(cls_attr).split("ui_bubble_rating bubble_")
        
            score = str(cls_attr[1])
        
            time.sleep(1)
        
            Temp_review = reviews[j].find_element_by_css_selector(".partial_entry").text
        
            time.sleep(1)
            review = Temp_review.replace("\n"," ")
            
            a.append(review)
            b.append(score)

#데이터 종합하여 데이터프레임생성, 생성된 데이터프레임을 엑셀파일로 저장
data = df({"리뷰":a, "평점":b})
print(data)

excel_writer = pd.ExcelWriter('C:/Users/Song Eui Seok/Desktop/review_data/review_data.xlsx', engine='xlsxwriter')
data.to_excel(excel_writer, index=True, sheet_name='경복궁')
excel_writer.save()


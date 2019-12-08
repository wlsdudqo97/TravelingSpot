#!/usr/bin/env python
# coding: utf-8

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from pandas import DataFrame as df

page = 15
url = "https://www.tripadvisor.co.kr/Attraction_Review-g294197-d324888-Reviews-or" + str(page) +"-Gyeongbokgung_Palace-Seoul.html#REVIEWS"
html = requests.get(url)
plain_text = html.text
bs = BeautifulSoup(plain_text, 'lxml')

result = list(bs.find_all('q', class_='location-review-review-list-parts-ExpandableReview__reviewText--gOmRC'))
final = []
for i in range(0, len(result)):
    final.append(result[i].text)
print(len(final))
print(final)

def crawlingReviews():

    pass

def extractRiviews():

    pass

if __name__ == '__main__':

    pass


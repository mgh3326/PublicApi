import csv
import json
from random import randint
from time import sleep

import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
oh = [('title', ""), ('content', "")]

with open('data.json', 'r', encoding='') as f:
    array = json.load(f)
    print(array)
    f = csv.writer(open("test.csv", 'w', newline='', encoding='utf-8'))

    # Write CSV Header, If you dont need that, remove this line
    # f.writerow(["pk", "model", "codename", "name", "content_type"])

    f.writerow(
        ["SIGUN_NM", "SIGUN_CD", "ACDNT_DIV_NM", "MULTI_KNOWLG_DIV_NO", "MULTI_KNOWLG_DIV_GROUP_NO", "LEGALDONG_CD_NO",
         "SPOT_NO", "JURISD_POLCSTTN_NM", "LOC_INFO", "OCCUR_CNT", "CASLT_CNT", "DPRS_CNT", "SERINJRY_INDVDL_CNT",
         "SLTINJRY_INDVDL_CNT", "INJURY_APLCNT_CNT", "LOGT", "LAT"])

    for x in array['TfcacdarM'][1]['row']:
        print(x)
        f.writerow([x["SIGUN_NM"],
                    x["SIGUN_CD"],
                    x["ACDNT_DIV_NM"],
                    x["MULTI_KNOWLG_DIV_NO"], x["MULTI_KNOWLG_DIV_GROUP_NO"],
                    x["LEGALDONG_CD_NO"], x["SPOT_NO"],
                    x["JURISD_POLCSTTN_NM"], x["LOC_INFO"], x["OCCUR_CNT"], x["CASLT_CNT"], x["DPRS_CNT"],
                    x["SERINJRY_INDVDL_CNT"], x["SLTINJRY_INDVDL_CNT"], x["INJURY_APLCNT_CNT"], x["LOGT"], x["LAT"],

                    ])

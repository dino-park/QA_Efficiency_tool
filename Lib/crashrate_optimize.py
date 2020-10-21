# -*- coding:utf-8 -*-

import requests
import pandas as pd
import datetime
import urllib.request as req
import simplejson as json
import time

class CrashReport:

    # CrashReport의 전체 앱리스트(appSeq) 기반의 크래시율 도출 DataFrame 클래스

    # 클래스 변수 선언
    now = datetime.datetime.now()  # 현재시간 인스턴스 생성
    # today, 00시로 고정
    # 시,분,초 설정하려면 해당 값에 %H:%M:%S 입력
    yesterDT1 = now.strftime('%Y-%m-%d 00:00:00')  # string convert
    now_yes = now - datetime.timedelta(1)  # today -1일자(어제)의 now_yes 객체 생성
    yesterDT2 = now_yes.strftime('%Y-%m-%d 00:00:00')  # string convert

    def __init__(self):
        self.appUrl = 'http://crashreport.nmn.io/apps?timezone=%2B09%3A00'
        self.cookies = {'IAM': '2370EE6D320EB878BEAC4A0228DD379929B9033E2B5FA4969264C6B8B8A5EC4222407EBE4CAC3BBD06B025EB352345CA9F2610803CF2C96B37BE315A283E1AA43A2F865A3847085B4AB5C3CDD19FD76B7EA1C913B220BE2DF34C985A90B370BBBAD05A6BEB2AF26E40D6A30BC8C2F95AF23D023372F3DF0B0F3FEDC2FB440257DB3B1EE4DF012B0C1BC25BF598470336B68A2D96F378CD7ED6D2BC61EE3FF4DF0B2749C866622172798F43BE5F637ECF16CE0B0B2DD24090A9AE1F2C88B2A034B6FC93629F9DE3164F3850C0AAAD4C0741955D62DBE1EC1CC1C95530852F257E8069F503D7B59E3E88F21A289C3B8DE8D0917D56EA0F62859AF26BBA18E309BF83D38349FDD978EBBD849810AA0016CA4A822667BC64C00FB2EE388A2759EC6076D8466F41C003769DE422F3BF4C6A32090BA00BAA93FC723C3F1F25FE4BD0E44DE3797E46538B6D2E4C7784C7E35AC06530BB186C9373B5A52596F13E78D8320B2380CA8668EABCDC09EAFB24F4D37D1C48698F1FB5A315EB64A0F133955441'}
        print("Program started.")

    def appList_CR(self):
        # crashreport 내 전체 앱 리스트 DataFrame

        res_crashreport = requests.get(self.appUrl, cookies=self.cookies)   # crashreport rquests get
        res_json = res_crashreport.json()   # 해당 api 데이터를 json type으로 변수 저장

        with open('./file/crashreport/crash_report.json', 'w') as writefile:   # json 파일 생성 및 쓰기
            json.dump(res_json, writefile)

        with open('crash_report.json', 'r') as readfile:    # json 파일 읽기
            dataframe1 = pd.DataFrame(json.load(readfile))  # json 파일 DataFrame 생성
            app_info = dataframe1[['deviceOs', 'appSeq', 'name', 'gameCode']].set_index('gameCode')

        return app_info

    def crashRateOfallAppList(self):
        # 전체 앱리스트에(appSeq 활용) 대한 크래시율 데이터 추출 함수 정의

        params = {'startDatetime': CrashReport.yesterDT2, 'endDatetime': CrashReport.yesterDT1, 'timezone': '+09:00'}

        with open('./file/crashreport/crash_report.json', 'r') as readfile:
            dataframe1 = pd.DataFrame(json.load(readfile))
            # Dataframe column 및 index 정의
            app_info = dataframe1[['deviceOs', 'appSeq', 'name', 'gameCode']].set_index('gameCode')
            appSeqidx = app_info['appSeq'].reset_index()    # 'appSeq' index 재정의
            appSeqlist = appSeqidx['appSeq']    # 'appSeq' 추출

            df_crash = []   # 빈 List를 만들어 for문 내부에서 데이터 채우는 방법으로 진행
            for seq in appSeqlist:
                # 원문 URL에 parameter를 추출하여 가공
                url_crash = 'http://crashreport.nmn.io/apps/{}/overviewBeta/crash/summary?'.format(seq)
                r2 = requests.get(url_crash, cookies=self.cookies, params=params)
                # 'appSeqlist'내 크래시율 데이터가 없을 경우, 예외처리
                try:
                    r2json = r2.json()['crashRate']
                except:
                    r2json = None
                # 반복을 통해 df_crash객체에 appSeq/crashrate row 추가(list 내 dict type으로 추가)
                df_crash.append({'appSeq': seq, 'crashrate': r2json})
        # for문 바깥에서 리스트를 DataFrame변환 객체 생성
        df_crash_list = pd.DataFrame(df_crash, columns=['appSeq', 'crashrate'])
        return df_crash_list


if __name__ == '__main__':
    CR = CrashReport()
    start_time = time.time()
    # 출력될 row 데이터의 범위 지정 최대 500개까지 출력
    pd.set_option('display.max_rows', 500)
    crash_list = pd.merge(CR.appList_CR(), CR.crashRateOfallAppList(), how='outer')
    crash_list.to_csv("crashratelist.csv", mode='wt', encoding="utf-8-sig") # csv 쓰기 시, 한글깨짐 없도록 인코딩
    print(CR.yesterDT2, " ~ ", CR.yesterDT1, "Crash Rate\n")
    read_file = pd.read_csv('crashratelist.csv', index_col= 'appSeq')
    crash_list_ = read_file['crashrate'] >= 2
    print("[List of games with a crash rate of 2 percent or higher]")
    print(read_file[crash_list_], "\n")
    print("--Total %s seconds" % int(time.time()-start_time))

    # print(CR.crashRateOfallAppList())






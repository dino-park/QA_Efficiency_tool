import time
import requests, json
import jwt

class appstoreconnect_api:

    def __init__(self):
        self.head = None
        self.auth_jwt()

    def auth_jwt(self):
        # 관리용도로 발급받은 키를 활용한 인증 메서드
        key_id = "G29TJJK9A9"
        issuer_id = "69a6de84-4bd8-47e3-e053-5b8c7c11a4d1"
        expiration_time = int(round(time.time() + (20.0 * 60.0)))
        path_to_key = './file/AuthKey_G29TJJK9A9.p8'
        with open(path_to_key, 'r') as k_file:
            private_key = k_file.read()
        header = {
            "alg": "ES256",
            "kid": key_id,
            "typ": "JWT"
            }
        payload = {
            "iss": issuer_id,
            "exp": expiration_time,
            "aud": "appstoreconnect-v1"
            }
        token = jwt.encode(payload, private_key, algorithm='ES256', headers=header)
        JWT = 'Bearer ' + token.decode()
        self.head = {'Authorization': JWT}

    def atc_api_apps(self):
        URL = 'https://api.appstoreconnect.apple.com/v1/apps'
        req = requests.get(URL, headers=self.head)
        print(req)
        with open('./file/In-app_json/output.json', 'w', encoding='utf-8-sig') as outfile:
            outfile.write(json.dumps(req.json(), ensure_ascii=False, indent=4))

    def atc_api_inApp(self, appid):
        URL = 'https://api.appstoreconnect.apple.com/v1/apps/{}/inAppPurchases?limit=200'.format(appid)
        req = requests.get(URL, headers=self.head)
        print(req)
        with open('./file/In-app_json/inapp.json', 'w', encoding='utf-8-sig') as inappfile:
            inappfile.write(json.dumps(req.json(), ensure_ascii=False, indent=4))
            print('inappfile saved.')

    # def atc_api_inAppNext(self):
    #     with open('../file/In-app_json/inapp.json', 'r', encoding='utf-8-sig') as readfile:
    #         inAppPch_json_l = json.load(readfile)
    #     if 'next' in inAppPch_json_l.get('links'):
    #     # for key, value in inAppPch_json_l.get('links').items():
    #         req = requests.get(inAppPch_json_l.get('links').get('next'), headers=self.head)
    #         next_reqd = json.dumps(req.json(), ensure_ascii=False, indent=4)
    #         next_reql = json.loads(next_reqd)
    #         inval_prd_list = []
    #         total_prd = next_reql['data']
    #         for prd in total_prd:
    #             if not prd['attributes']['state'] in ('APPROVED'):
    #                 inval_prd_list.append(
    #                     {
    #                         'Refer_Name': prd['attributes']['referenceName'],
    #                         'Product_Code': prd['attributes']['productId'],
    #                         'Status': prd['attributes']['state']
    #                     }
    #                 )
    #         print(type(inval_prd_list))
    #         if 'next' in next_reql.get('links'):


    def atc_api_inAppNext(self):
        with open('./file/In-app_json/inapp.json', 'r', encoding='utf-8-sig') as readfile:
            inAppPch_json_l = json.load(readfile)
        for key, value in inAppPch_json_l.get('links').items():
            if 'next' in key:
                req = requests.get(value, headers=self.head)
                with open('./file/In-app_json/inapp_Nextpage.json', 'w', encoding='utf-8-sig') as nextfile:
                    nextfile.write(json.dumps(req.json(), ensure_ascii=False, indent=4))
                    print("nextfile saved.")
                with open('./file/In-app_json/inapp_Nextpage.json', 'r', encoding='utf-8-sig') as read2ndfile:
                    inAppPch_json_lnext = json.load(read2ndfile)
                for key_n, value_n in inAppPch_json_lnext.get('links').items():
                    if 'next' in key_n:
                        req2 = requests.get(value, headers=self.head)
                        with open('./file/In-app_json/inapp_3rdpage.json', 'w', encoding='utf-8-sig') as thirdfile:
                            thirdfile.write(json.dumps(req2.json(), ensure_ascii=False, indent=4))
                            print('third file saved.')
                        with open('./file/In-app_json/inapp_3rdpage.json', 'r', encoding='utf-8-sig') as read3rdfile:
                            inAppPch_json_3rd = json.load(read3rdfile)
                        for key_3n, value_3n in inAppPch_json_3rd.get('links').items():
                            if 'next' in key_3n:
                                req3 = requests.get(value, headers=self.head)
                                with open('./file/In-app_json/inapp_4thpage.json', 'w', encoding='utf-8-sig') as file4th:
                                    file4th.write(json.dumps(req3.json(), ensure_ascii=False, indent=4))
                                    print('4th file saved.')
                                with open('./file/In-app_json/inapp_4thpage.json', 'r', encoding='utf-8-sig') as read4thfile:
                                    inAppPch_json_4th = json.load(read4thfile)


                    else:
                        print('next key is none')
                        break
                break

if __name__ == '__main__':
    appstoreconn = appstoreconnect_api()
    appstoreconn.atc_api_inApp('1449552940')
    appstoreconn.atc_api_inAppNext()
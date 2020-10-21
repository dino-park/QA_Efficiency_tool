import simplejson as json
import requests
import datetime

class AppleSystemCheck:
    def __init__(self):
        #self.apple_dev_srv()
        #print("apple_dev_srv 실행됨")
        #self.apple_usr_srv()
        #print("apple_usr_srv 실행됨")
        now = datetime.datetime.now()
        self.now_datetime = now.strftime("%Y-%m-%d, %H:%M:%S")
        #print(self.now_datetime) #초기화 실행 시간과 해당 메서드 실행시간의 Gap 차이 확인을 위한 print문

    def apple_dev_srv(self):
        apple_dev_service_state = requests.get('https://www.apple.com/support/systemstatus/data/developer/system_status_en_US.js').text.split("(")[1].split(")")[0]
        apple_dev = json.loads(apple_dev_service_state)["services"]
        system_fault = []
        for item in apple_dev:
            if not item['events']:
                continue
            else:
                for event in item['events']:
                    system_fault.append(
                        {
                            "Service": item["serviceName"],
                            "Issue StatusType": event["statusType"],
                            "Event Status": event["eventStatus"],
                            "Start Date": event["startDate"],
                            "End Date": event["endDate"]
                        }
                    )
        return system_fault

    def apple_usr_srv(self):
        apple_usr_service_state = requests.get("https://www.apple.com/support/systemstatus/data/system_status_en_US.js").text
        apple_usr = json.loads(apple_usr_service_state)["services"]
        system_fault = []
        for item in apple_usr:
            if not item['events']:
                continue
            else:
                for event in item['events']:
                    system_fault.append(
                        {
                            "Service": item["serviceName"],
                            "Issue StatusType": event["statusType"],
                            "Event Status": event["eventStatus"],
                            "Start Date": event["startDate"],
                            "End Date": event["endDate"]
                        }
                    )
        return system_fault

if __name__ == '__main__':
    apple_syschk = AppleSystemCheck()
    print("[ Apple Service Status Check"+" - ", apple_syschk.now_datetime, "KST]")
    print(json.dumps(apple_syschk.apple_usr_srv(), indent=4))
    print("\n[ Apple Development Service Status Check"+" - ", apple_syschk.now_datetime, "KST]")
    print(json.dumps(apple_syschk.apple_dev_srv(), indent=4))


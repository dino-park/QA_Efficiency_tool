import sys
import datetime
import time
import webbrowser
import pandas as pd
import simplejson as json
import csv

from PyQt5.QtWidgets import QMainWindow, QWidget, QProgressBar
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QThread, pyqtSignal

from Lib.Work1_viewr_v1 import Ui_MainWindow
from Lib.AppleSystemCheck import AppleSystemCheck
from Lib.crashrate_optimize import CrashReport
from Lib.appstore_jwtAuth import appstoreconnect_api

class Main(QMainWindow, Ui_MainWindow, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.worker = Worker()
        self.inapp_next_Button.setDisabled(True)
        self.init_auth_lock()
        self.init_signal()
        print("할당 완료")

    def init_auth_lock(self):
        # self.applesrvButton.setEnabled(False)
        pass

    def init_auth_active(self):
        pass

    def show_statusmsg(self, msg):
        # 상태표시줄 함수

        self.statusbar.showMessage(msg)

    def init_signal(self):
        # 각 ui 기능들에 대한 signal 함수

        self.applesrvButton.clicked.connect(self.appleusr_sys_check)    # apple 서비스시스템상태 조회 버튼&함수 connect
        self.applesdevButton.clicked.connect(self.appledev_sys_check)   # apple 개발자시스템상태 조회 버튼&함수 connect
        self.welcome_login.clicked.connect(self.shortcuts_nworld)       # 넷마블월드 바로가기 버튼&함수 connect
        self.t_crashrate_Button.clicked.connect(self.btn_crashrate)     # 크래시율 조회 버튼&함수 connect
        print("crashrate 함수 호출")
        self.inAppPch_Button.clicked.connect(self.appstore_inappPch)    # inapp상품 상태 조회 버튼&함수 connect
        self.inapp_next_Button.clicked.connect(self.appstore_inappPch_Next) # inapp상품 상태 다음페이지 조회 버튼&함수 connect
        self.worker.finished.connect(self.total_crashrate)  # Thread연결을 위한 함수간 connect
        self.worker.countChanged.connect(self.crashrateLoadingProgress) # thread를 이용한 progressbar connect

    @pyqtSlot()
    def appstore_inappPch(self):
        # appstoreconnect in-app products api 함수(한페이지 상품 조회 갯수는 limit 200개)

        self.inAppPch_Extract.clear()
        appstoreconn = appstoreconnect_api()
        appstoreconn.atc_api_inApp(self.input_appId.text())
        with open('./file/In-app_json/inapp.json', 'r', encoding='utf-8-sig') as readfile:
            inAppPch_json_l = json.load(readfile, encoding='utf-8-sig')
            inAppPch_json_d = json.dumps(inAppPch_json_l, indent=4, ensure_ascii=False)
        # 모든 상품리스트를 출력(단, 하기 if문에서와 같이 1페이지당 max 200미만 갯수만 리턴됨)
        self.inAppPch_Extract.appendPlainText(inAppPch_json_d)
        inapp_count = inAppPch_json_l.get('meta').get('paging')
        if inapp_count.get('total') > 200:
            self.inapp_next_Button.setEnabled(True)
            self.log_msg("There are additional In-App products available for extract. : More than 200.")
        else:
            self.log_msg("In-App products complete for extract.")

    @pyqtSlot()
    def appstore_inappPch_Next(self):
        # limit 200초과되는 추가 추출 위한 상품api 함수

        self.inAppPch_Extract.clear()
        appstoreconn = appstoreconnect_api()
        appstoreconn.atc_api_inAppNext()
        with open('./file/In-app_json/inapp_Nextpage.json', 'r', encoding='utf-8-sig') as read2ndfile:
            inAppPch_json_lnext = json.load(read2ndfile, encoding='utf-8-sig')
            inAppPch_json_dnext = json.dumps(inAppPch_json_lnext, indent=4, ensure_ascii=False)
        self.inAppPch_Extract.appendPlainText(inAppPch_json_dnext)
        for key, value in inAppPch_json_lnext.get('links').items():
            if 'next' not in key:
                self.inapp_next_Button.setDisabled(True)
                self.log_msg("In-App products complete for extract.")
                break
            else:
                self.log_msg("There are additional In-App products available for extract.")
                with open('./file/In-app_json/inapp_3rdpage.json', 'r', encoding='utf-8-sig') as thirdfile:
                    inAppPch_json_lthird = json.load(thirdfile, encoding='utf-8-sig')
                    inAppPch_json_dthird = json.dumps(inAppPch_json_lthird, indent=4, ensure_ascii=False)
                self.inAppPch_Extract.appendPlainText(inAppPch_json_dthird)
                for key2, value2 in inAppPch_json_lthird.get('links').items():
                    if 'next' not in key2:
                        self.inapp_next_Button.setDisabled(True)
                        self.log_msg("In-App products complete for extract.")
                        break
                    else:
                        pass
    @pyqtSlot(int)
    def crashrateLoadingProgress(self, count):
        self.tot_CR_Progress.setValue(self.tot_CR_Progress.value() + count)
        if count == 0:
            self.tot_CR_Progress.setValue(100)

    @pyqtSlot()
    def btn_crashrate(self):
        '''크래시율 조회 버튼 클릭 시, Thread 클래스 객체 생성 및 Run'''

        self.worker.start()
        print("workerThread 시작")

    @pyqtSlot(str)
    def total_crashrate(self, msg):
        self.tot_CR_Extract.clear()
        print("Editbox clear~!")
        with open('./file/crashreport/crashratelist_2perOver.csv', 'r', encoding='utf-8') as readfile:
            read_file = csv.reader(readfile)
            self.tot_CR_Extract.setPlainText("[List of games with a crash rate of 2 percent or higher]")
            for item in read_file:
                self.tot_CR_Extract.appendPlainText(str(item))
            self.tot_CR_Extract.appendPlainText("--Total %s seconds" % int(time.time() - self.worker.start_time))

        self.log_msg(msg)

    @pyqtSlot()
    def appleusr_sys_check(self):
        apple_syschk = AppleSystemCheck()
        syscheck = json.dumps(apple_syschk.apple_usr_srv(), indent=4)
        self.syscheckprint.clear()
        self.syscheckprint.setPlainText("[ Apple Service Status Check" + " - " + apple_syschk.now_datetime + "KST]")
        self.syscheckprint.appendPlainText(syscheck)
        self.log_msg("Apple service status check complete.")

    @pyqtSlot()
    def appledev_sys_check(self):
        apple_syschk = AppleSystemCheck()
        syscheck = json.dumps(apple_syschk.apple_dev_srv(), indent=4)
        self.syscheckprint.clear()
        self.syscheckprint.setPlainText(
            "[ Apple Development Service Status Check" + " - " + apple_syschk.now_datetime + "KST]")
        self.syscheckprint.appendPlainText(syscheck)
        self.log_msg("Apple development service status check complete.")

    @pyqtSlot()
    def shortcuts_nworld(self):
        webbrowser.open_new_tab('https://p.nmn.io')
        self.show_statusmsg('Netmarble World')
        self.log_msg('netmarble world page access successed.')

    def log_msg(self, act):
        now = datetime.datetime.now()
        now_datetime = now.strftime("%Y-%m-%d, %H:%M:%S")
        append_msg = act + ' - (' + now_datetime + ')'
        self.logPrint.appendPlainText(append_msg)

        with open("./log/log.txt", 'a') as f:
            f.write(append_msg + '\n')

class Worker(QThread):
    finished = pyqtSignal(str)
    countChanged = pyqtSignal(int)
    tot_CR = CrashReport()
    start_time = time.time()

    def __init__(self):
        QThread.__init__(self)

    @pyqtSlot()
    def run(self):

        # 출력될 row 데이터의 범위 지정 최대 500개까지 출력
        pd.set_option('display.max_rows', 500)
        crash_list = pd.merge(self.tot_CR.appList_CR(), self.tot_CR.crashRateOfallAppList(), how='outer')
        print("Data merge 완료")
        with open('./file/crashreport/crashratelist.csv', 'w', encoding='utf-8', newline='') as writefile:
            # csv 쓰기 시, 한글깨짐 없도록 인코딩
            crash_list.to_csv(writefile, mode='wt', encoding="utf-8-sig")
            print("csv write 완료")
            with open('./file/crashreport/crashratelist.csv', 'r', encoding='utf-8') as readfile:
                read_file = pd.read_csv(readfile, index_col='appSeq', encoding='utf-8')
                crash_list_ = read_file['crashrate'] >= 2
                crash_list_MoreThan = read_file[crash_list_]
                print(type(crash_list_MoreThan))
                print("crash_list_처리 완료")
                with open('./file/crashreport/crashratelist_2perOver.csv', 'w', encoding='utf-8', newline='') as write2file:
                    # crash_list_.to_csv(write2file, 'wb', encoding='utf-8-sig')
                    crash_list_MoreThan.to_csv(write2file, mode='wt', encoding='utf-8-sig')
        print("csv write2 완료")

        self.finished.emit("[List of games with a crash rate of 2 percent or higher]")
        print("QThread 전달 완료")
        time.sleep(2)
        while 1:
            count = 1
            self.countChanged.emit(count)
            time.sleep(1)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_app = Main()
    main_app.show()
    app.exec_()
# self.worker.tot_CR.yesterDT2 + " ~ " + self.worker.tot_CR.yesterDT1 + "Crash Rate"+"\n"+
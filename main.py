# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("UF Course Registration ")
        MainWindow.resize(655, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 611, 321))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 370, 92, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        
        
        self.myThread = MyThread()
        self.myThread.msg.connect(self.showMsg)
        self.pushButton.clicked.connect(lambda:self.switch())
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("UF Course Registration", "Developed by: Lucas.Liao"))
        self.textBrowser.setHtml(_translate("UF Course Registration", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9.07563pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">Enter the page of the registration course and set up the search keywords to ensure that the required courses are in the first!<br />Then click the Start button.</span></p></body></html>"))
        self.pushButton.setText(_translate("UF Course Registration", "Start"))


    def  showMsg(self,msg):
        ui.textBrowser.append(msg)
    
    def switch(self):
        if self.pushButton.text() == 'Start':
            self.pushButton.setText('Stop')
            self.myThread.stop = False
            self.myThread.start()
        else:
            self.pushButton.setText('Start')
            ui.textBrowser.append('Stop searching')
            self.myThread.stop = True
           
        


class MyThread(QtCore.QThread):  
    
    
    msg = QtCore.pyqtSignal(str)
    stop = False
    def __init__(self, parent=None ):  
        super().__init__(parent)
        self.driver = webdriver.Edge()
        # 访问网页
        self.driver.get('https://one.uf.edu/myschedule/')
        #设置微信提醒
           # data = {
           #         "appToken":'AT_dBC0kiaXFDbbaxKdPsnnsBVFVJRxaUtO',
           #         "content":'msg:要发送的消息',
           #         "topicIds":['9324',],
           #         "summary":msg[:99], # 该参数可选，默认为 content 的前10个字符
           #         "contentType":1,
           #         "uids":['UID_4SpxxRkSyS5zfEXokp7tYaZQDuHh', ],
           #         }
           # webapi = 'http://wxpusher.zjiecode.com/api/send/message'  
        
        
  
    def run(self):
        
        self.driver.refresh()
        self.sleep(5)
        while True:
            if  self.stop : 
                continue
            try:    
                addbutton = self.driver.find_element(By.XPATH, "//*[text()='+ Add Class']")  
                addbutton.click()
                button = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[text()='Add']")))
                button.click()
                self.sleep(5)
                self.msg.emit('The course you are looking for has been registered.')
                # 发送微信消息
                # result = requests.post(url=webapi,json=data)
                break   
            except:
                self.msg.emit('The course you are looking for is not available now, please wait.') 
                self.driver.refresh()
                self.sleep(5)
                # driver.get('https://one.uf.edu/soc/registration-search/2238?term="2238"&category="CWSP"&prog-level="GRAD"&dept="19140000"&course-title="Computer+and+Network+Security"')
                continue
        # 关闭浏览器
        # self.driver.quit()



    











import sys
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())



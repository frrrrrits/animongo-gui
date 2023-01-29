from multiprocessing import pool
import sys
import requests
import threading
import json
import webbrowser
from multiprocessing.pool import ThreadPool

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from data.ui.ui_home import Ui_MainWindow
from data.ui.ui_functions import *
from api.lendrive import *
from data.extensions.view_ext import *
from data.worker.worker_utils import Worker
from widget.custom_progressbar import LoadingProgressBar
from widget.custom_toast import Toast

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        UIFunctions.set_ui_definitions(self)
        UIFunctions.selectDefaultMenu(self, "btn_menu_1")
        self.stackedWidget.setCurrentWidget(self.page_home)
        self.icon_menu_1.clicked.connect(self.navigation_rail)
        self.icon_menu_2.clicked.connect(self.navigation_rail)
        
        self.progressBar = LoadingProgressBar()
        self.horizontalLayout_10.addWidget(self.progressBar)
        
        self.anime_list.verticalScrollBar().setSingleStep(30)
        self.anime_list.installEventFilter(self)
        self.anime_list.itemDoubleClicked.connect(self.item_click)
        self.btn_search.clicked.connect(self.getSearch)
        
        self.threadpool =  QThreadPool()
        self.create_ongoing_worker()

        self.showToast(msg='Getting Content ..', dur=7)

    def resizeEvent(self, event):
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        
    def navigation_rail(self):
        btn = self.sender()
        btnName = btn.objectName()
        
        if btnName == "icon_menu_1":
            self.stackedWidget.setCurrentWidget(self.page_home)
            UIFunctions.resetStyle(self, "btn_menu_1")
            self.btn_menu_1.setStyleSheet(UIFunctions.selectMenu(self.btn_menu_1.styleSheet()))
            
        if btnName == "icon_menu_2":
            self.stackedWidget.setCurrentWidget(self.page_search)
            UIFunctions.resetStyle(self, "btn_menu_2")
            self.btn_menu_2.setStyleSheet(UIFunctions.selectMenu(self.btn_menu_2.styleSheet()))
    
    def showToast(self, msg: str, dur: float=1):
        toast = Toast(text=msg, duration=dur, parent=self)
        toast.show()
    
    # testing click fun
    def item_click(self, index):
        url = index.statusTip()
        data  = json.loads(index.whatsThis().replace("'", "\""))        
        webbrowser.open_new_tab(url)
        self.showToast("Opening Browser", dur=5)

    # Api Request & Worker
    def getOngoingThread(self, page=1):
        self.progressBar.showProgress()
        if page == 1: self.anime_list.clear()
        data = get_ongoing(page)
        list = map(self.item_view, data)
        for res, _ in list:
            self.anime_list.addItem(res)
        if page:
            if not page: page = 0
            self.anime_list.setWhatsThis(str(page))
        return data
    
    def getSearch(self):
        self.progressBar.showProgress()
        query = self.search_edit.toPlainText()
        self.showToast(query + " Getting Searching Content ..")
        t = threading.Thread(target=self.getSearchThread, args=(query, self.search_list,))
        t.start()

    def getSearchThread(self, query, listview):
        get_search(query)
        self.progressBar.hideProgress()
        self.showToast("Done")
 
    def create_ongoing_worker(self):
        page = 1
        ongoing_worker = Worker(self.getOngoingThread, args=(page,))
        ongoing_worker.signals.result.connect(self.ongoing_worker_complete)
        self.threadpool.start(ongoing_worker)
   
    def ongoing_worker_complete(self, result):
        self.progressBar.hideProgress()
        return "done"

    def item_view(self, data):
        font = QFont()
        font.setPointSize(11)
        rawImg = requests.get(data['img']).content
        imageData = make_rounded(rawImg, eps=data['eps'])
        anime = QListWidgetItem()
        anime.setIcon(QIcon(imageData))
        anime.setText(data['title'])
        anime.setFont(font)
        anime.setTextAlignment(Qt.AlignLeading|Qt.AlignBottom)
        anime.setFlags(Qt.ItemIsEnabled)
        anime.setStatusTip(data['url'])
        anime.setWhatsThis(str(data))
        return anime, rawImg

if __name__ == "__main__":
    main_thread = QApplication(sys.argv)
    make_font_dir = QDir("Roboto")
    QFontDatabase.addApplicationFont("res/fonts.ttf")
    main_window = MainWindow()
    main_window.show()
    sys.exit(main_thread.exec())

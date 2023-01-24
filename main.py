import sys
import requests
import threading
from platform import python_version
from multiprocessing.pool import ThreadPool

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from data.ui.ui_home import Ui_MainWindow
from data.ui.ui_functions import *
from api.lendrive import *
from data.extensions.view_ext import *

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        UIFunctions.set_ui_definitions(self)
        
        threading.Thread(target=self.getOngoingThread).start()
        self.anime_list.verticalScrollBar().setSingleStep(30)
        self.anime_list.installEventFilter(self)

    def resizeEvent(self, event):
        UIFunctions.resize_grips(self)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def getOngoingThread(self, page=1):
        if page == 1:
            self.anime_list.clear()
        data = getOngoing(page)
        result = ThreadPool(16).map(self.itemView, data)
        for res, _ in result:
            self.anime_list.addItem(res)
        if page:
            if not page:
                page = 0
            self.anime_list.setWhatsThis(str(page))

    def itemView(self, data):
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
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

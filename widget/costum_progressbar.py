# CREDIT: https://github.com/yjg30737/pyqt-loading-progressbar

from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtCore import QPropertyAnimation, QAbstractAnimation, QEasingCurve, QSize

class LoadingProgressBar(QProgressBar):
    def __init__(self):
        super().__init__()
        self.__initUi()
        self.setMaximumSize(QSize(16777215, 4))
        self.setStyleSheet(
        '''
        QProgressBar {
            border: none;
            border-radius: 2px;
            background-color: rgb(68, 71, 78)
        }
        QProgressBar::chunk {
            background-color: rgb(176, 190, 255);
            border-radius :2px;
        }
        ''')

    def __initUi(self):
        self.setValue(0)
        self.setTextVisible(False)
        self.__animation = QPropertyAnimation(self, b'loading')
        self.__animation.setStartValue(self.minimum())
        self.__animation.setEndValue(self.maximum())
        self.__animation.valueChanged.connect(self.__loading)
        self.__animation.setDuration(1000)
        self.__animation.setEasingCurve(QEasingCurve.InOutQuad)
        self.__animation.start()

    def __loading(self, v):
        self.setValue(v)
        if self.__animation.currentValue() == self.__animation.endValue():
            self.__animation.setDirection(QAbstractAnimation.Backward)
            self.setInvertedAppearance(True)
            self.__animation.start()
        elif self.__animation.currentValue() == self.__animation.startValue():
            self.__animation.setDirection(QAbstractAnimation.Forward)
            self.setInvertedAppearance(False)
            self.__animation.start()
    
    def hideProgress(self):
        self.hide()
        self.__animation.stop()
        
    def showProgress(self):
        self.show()
        self.__animation.start()

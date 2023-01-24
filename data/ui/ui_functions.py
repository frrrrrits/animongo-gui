from data.ui.theme.style import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from widget.custom_grips import *

_is_maximized = False

class UIFunctions:

    def maximize_restore(self):
       global _is_maximized
       
       def change_ui():
        if not _is_maximized:
            self.resize(self.width()+1, self.height()+1)
            self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
            self.drop_shadow_frame.setStyleSheet(backgroundFrame)
            self.btn_maximize.setToolTip("Maximize")
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()
            self.top_left_grip.show()
            self.top_right_grip.show()
            self.bottom_left_grip.show()
            self.bottom_right_grip.show()
        else:
            self.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            self.drop_shadow_frame.setStyleSheet(backgroundFrameOff)
            self.btn_maximize.setToolTip("Restore")
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
            self.top_left_grip.hide()
            self.top_right_grip.hide()
            self.bottom_left_grip.hide()
            self.bottom_right_grip.hide()
            
       if self.isMaximized():
            _is_maximized = False
            self.showNormal()
            change_ui()
       else:
            _is_maximized = True
            self.showMaximized()
            change_ui()

    def set_ui_definitions(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        def moveWindow(event):
            if self.isMaximized():
                UIFunctions.maximize_restore(self)
                curso_x = self.pos().x()
                curso_y = event.globalPos().y() - QCursor.pos().y()
                self.move(curso_x, curso_y)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.title_bar.mouseMoveEvent = moveWindow

        def maximize_restore(event):
            if event.type() == QEvent.MouseButtonDblClick:
                UIFunctions.maximize_restore(self)
        self.title_bar.mouseDoubleClickEvent = maximize_restore

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(3)
        self.shadow.setYOffset(4)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.drop_shadow_frame.setGraphicsEffect(self.shadow)

        self.btn_maximize.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        self.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.btn_close.clicked.connect(lambda: self.close())

        self.left_grip = PyGrips(self, "left", True)
        self.right_grip = PyGrips(self, "right", True)
        self.top_grip = PyGrips(self, "top", True)
        self.bottom_grip = PyGrips(self, "bottom", True)
        self.top_left_grip = PyGrips(self, "top_left", True)
        self.top_right_grip = PyGrips(self, "top_right", True)
        self.bottom_left_grip = PyGrips(self, "bottom_left", True)
        self.bottom_right_grip = PyGrips(self, "bottom_right", True)

    def resize_grips(self):
        self.left_grip.setGeometry(0, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 10, 10, 10, self.height())
        self.top_grip.setGeometry(0, 0, self.width(), 10)
        self.bottom_grip.setGeometry(0, self.height() - 10, self.width(), 10)
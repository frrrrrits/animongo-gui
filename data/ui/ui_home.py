from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from data.extensions.view_ext import get_res_path
from data.ui.theme.style import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(769, 600)
        MainWindow.setMinimumSize(QSize(769, 680))
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"QFrame#drop_shadow_frame {\n"
"	border-radius: 10px;\n"
"	border: 1px solid rgba(189, 189, 189, 120);\n"
"	background-color:rgb(68, 71, 78)\n"
"};\n"
"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, 9, 9)
        
        # APP BAR
        self.top_bar = QFrame(self.drop_shadow_frame)
        self.top_bar.setObjectName(u"top_bar")
        self.top_bar.setMinimumSize(QSize(0, 43))
        self.top_bar.setMaximumSize(QSize(16777215, 43))
        self.top_bar.setFrameShape(QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.top_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.top_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setLayoutDirection(Qt.LeftToRight)
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, -1, -1)
        self.app_title = QLabel(self.frame_title)
        self.app_title.setObjectName(u"app_title")
        font = QFont("Roboto")
        font.setPointSize(13)
        font.setBold(True)
        self.app_title.setFont(font)
        self.app_title.setStyleSheet(u"color: rgb(248, 251, 255)")
        self.app_title.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.app_title)
        self.horizontalLayout.addWidget(self.frame_title)
        
        # CONTEXT FRAME
        self.frame_btns = QFrame(self.top_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMinimumSize(QSize(124, 0))
        self.frame_btns.setMaximumSize(QSize(90, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	border-radius: 7px;\n"
"	background-color: rgba(217, 217, 217, 34);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border-radius: 7px;\n"
"	background-color: rgba(217, 217, 217, 67);\n"
"}")
        icon = QIcon()
        icon.addFile(get_res_path("icon_minimize.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_6.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        sizePolicy.setHeightForWidth(self.btn_maximize.sizePolicy().hasHeightForWidth())
        self.btn_maximize.setSizePolicy(sizePolicy)
        self.btn_maximize.setMinimumSize(QSize(40, 0))
        self.btn_maximize.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	border-radius: 7px;\n"
"	background-color: rgba(217, 217, 217, 34);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border-radius: 7px;\n"
"	background-color: rgba(217, 217, 217, 67);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(get_res_path("icon_maximize.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize.setIcon(icon1)

        self.horizontalLayout_6.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	border-radius: 7px;\n"
"	background-color: rgba(255, 96, 99, 56);\n"
"}\n"
"QPushButton:pressed {	\n"
"	border-radius: 7px;\n"
"	background-color: rgb(255, 96, 99);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(get_res_path("icon_close.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_6.addWidget(self.btn_close)

        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.top_bar)
        
        self.frame_progress = QFrame(self.drop_shadow_frame)
        self.frame_progress.setObjectName(u"frame_progress")
        self.frame_progress.setFrameShape(QFrame.StyledPanel)
        self.frame_progress.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_progress)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 5)
        self.verticalLayout.addWidget(self.frame_progress)
        self.frame_main = QFrame(self.drop_shadow_frame)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_main)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        
        # NAVIGATION
        self.side_bar = QFrame(self.frame_main)
        self.side_bar.setObjectName(u"side_bar")
        self.side_bar.setMinimumSize(QSize(60, 0))
        self.side_bar.setMaximumSize(QSize(60, 16777215))
        self.side_bar.setFrameShape(QFrame.NoFrame)
        self.side_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.side_bar)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.side_bar_icon = QFrame(self.side_bar)
        self.side_bar_icon.setObjectName(u"side_bar_icon")
        self.side_bar_icon.setMinimumSize(QSize(0, 50))
        self.side_bar_icon.setMaximumSize(QSize(16777215, 50))
        self.side_bar_icon.setLayoutDirection(Qt.LeftToRight)
        self.side_bar_icon.setFrameShape(QFrame.StyledPanel)
        self.side_bar_icon.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.side_bar_icon)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, 0, 2, -1)
        self.app_icon = QLabel(self.side_bar_icon)
        self.app_icon.setObjectName(u"app_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.app_icon.sizePolicy().hasHeightForWidth())
        self.app_icon.setSizePolicy(sizePolicy1)
        self.app_icon.setMinimumSize(QSize(43, 43))
        self.app_icon.setMaximumSize(QSize(43, 43))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.app_icon.setFont(font1)
        self.app_icon.setStyleSheet(u"QLabel {\n"
"	background-color: none;\n"
"	border: none;\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.app_icon.setPixmap(QPixmap(get_res_path("icon.png")))
        self.app_icon.setScaledContents(True)
        self.app_icon.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.app_icon)


        self.verticalLayout_9.addWidget(self.side_bar_icon)

        self.side_bar_menu = QFrame(self.side_bar)
        self.side_bar_menu.setObjectName(u"side_bar_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.side_bar_menu.sizePolicy().hasHeightForWidth())
        self.side_bar_menu.setSizePolicy(sizePolicy2)
        self.side_bar_menu.setMinimumSize(QSize(60, 0))
        self.side_bar_menu.setMaximumSize(QSize(60, 16777215))
        self.side_bar_menu.setLayoutDirection(Qt.LeftToRight)
        self.side_bar_menu.setStyleSheet(u"")
        self.side_bar_menu.setFrameShape(QFrame.NoFrame)
        self.side_bar_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.side_bar_menu)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 29, 0, 0)
        
        #NAVIGATION
        self.frame_left_menu = QFrame(self.side_bar_menu)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy2.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy2)
        self.frame_left_menu.setMinimumSize(QSize(50, 0))
        self.frame_left_menu.setMaximumSize(QSize(50, 133))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: none;")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_menu_1 = QFrame(self.frame_left_menu)
        self.btn_menu_1.setObjectName(u"btn_menu_1")
        self.btn_menu_1.setStyleSheet(Style.rail_menu_button_style_off)
        self.btn_menu_1.setFrameShape(QFrame.NoFrame)
        self.btn_menu_1.setFrameShadow(QFrame.Plain)
        self.verticalLayout_12 = QVBoxLayout(self.btn_menu_1)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.icon_menu_1 = QPushButton(self.btn_menu_1)
        self.icon_menu_1.setObjectName(u"icon_menu_1")
        self.icon_menu_1.setStyleSheet(u"background-color: none;border: 0px solid;")
        icon3 = QIcon()
        icon3.addFile(get_res_path("icon_recent_off.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.icon_menu_1.setIcon(icon3)
        self.icon_menu_1.setIconSize(QSize(27, 49))

        self.verticalLayout_12.addWidget(self.icon_menu_1)


        self.verticalLayout_8.addWidget(self.btn_menu_1, 0, Qt.AlignTop)

        self.btn_menu_2 = QFrame(self.frame_left_menu)
        self.btn_menu_2.setObjectName(u"btn_menu_2")
        self.btn_menu_2.setStyleSheet(Style.rail_menu_button_style_off)
        self.btn_menu_2.setFrameShape(QFrame.NoFrame)
        self.btn_menu_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_121 = QVBoxLayout(self.btn_menu_2)
        self.verticalLayout_121.setSpacing(0)
        self.verticalLayout_121.setObjectName(u"verticalLayout_121")
        self.verticalLayout_121.setContentsMargins(0, 0, 0, 0)
        self.icon_menu_2 = QPushButton(self.btn_menu_2)
        self.icon_menu_2.setObjectName(u"icon_menu_2")
        self.icon_menu_2.setStyleSheet(u"background-color: none;border: 0px solid;")
        icon4 = QIcon()
        icon4.addFile(get_res_path("icon_search_off.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.icon_menu_2.setIcon(icon4)
        self.icon_menu_2.setIconSize(QSize(27, 49))

        self.verticalLayout_121.addWidget(self.icon_menu_2)


        self.verticalLayout_8.addWidget(self.btn_menu_2, 0, Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.frame_left_menu)


        self.verticalLayout_9.addWidget(self.side_bar_menu, 0, Qt.AlignTop)


        self.horizontalLayout_8.addWidget(self.side_bar)
        
        # MAIN CONTENT
        self.content_main = QFrame(self.frame_main)
        self.content_main.setObjectName(u"content_main")
        self.content_main.setStyleSheet(u"QFrame {\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	background-color: rgb(26, 27, 30);\n"
"};\n"
"")
        self.content_main.setFrameShape(QFrame.StyledPanel)
        self.content_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content_main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, -1, 8, -1)
        self.stackedWidget = QStackedWidget(self.content_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        
        # PAGE 1
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.horizontalLayout_2 = QHBoxLayout(self.page_home)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.anime_list = QListWidget(self.page_home)
        self.anime_list.setObjectName(u"anime_list")
        self.anime_list.setStyleSheet(u"QListWidget::item {\n"
"color: rgb(255, 255, 255);\n"
"background-color:transparent;padding: 7px;\n"
"}\n"
"QListView::item:hover {\n"
"border-radius: 10px;\n"
"background:rgb(47, 47, 63);\n"
"}\n"
"QListView::item:selected {\n"
"border-radius: 10px;\n"
"background : rgba(62, 64, 90, 120);\n"
"}\n"
"QListWidget {\n"
"background-color:transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none; background: rgb(29, 25, 30);\n"
"}")
        self.anime_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.anime_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.anime_list.setIconSize(QSize(203, 116))
        self.anime_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.anime_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.anime_list.setResizeMode(QListView.Adjust)
        self.anime_list.setGridSize(QSize(216, 160))
        self.anime_list.setViewMode(QListView.IconMode)

        self.horizontalLayout_2.addWidget(self.anime_list)

        self.stackedWidget.addWidget(self.page_home)
        
        # PAGE 2
        self.page_search = QWidget()
        self.page_search.setObjectName(u"page_search")
        self.verticalLayout_4 = QVBoxLayout(self.page_search)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(self.page_search)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout_3 = QVBoxLayout(self.verticalFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_search = QFrame(self.verticalFrame)
        self.frame_search.setObjectName(u"frame_search")
        self.frame_search.setMinimumSize(QSize(0, 60))
        self.frame_search.setMaximumSize(QSize(16777215, 60))
        self.frame_search.setFrameShape(QFrame.StyledPanel)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_search)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.search_bar = QFrame(self.frame_search)
        self.search_bar.setObjectName(u"search_bar")
        self.search_bar.setMinimumSize(QSize(0, 50))
        self.search_bar.setMaximumSize(QSize(16777215, 50))
        self.search_bar.setFrameShape(QFrame.StyledPanel)
        self.search_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.search_bar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 7, -1, 5)
        self.search_edit = QPlainTextEdit(self.search_bar)
        self.search_edit.setObjectName(u"search_edit")
        self.search_edit.setMinimumSize(QSize(0, 42))
        self.search_edit.setMaximumSize(QSize(16777215, 42))
        font2 = QFont("Roboto")
        font2.setPointSize(11)
        font2.setBold(False)
        self.search_edit.setFont(font2)
        self.search_edit.setStyleSheet(u"QPlainTextEdit {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(68, 71, 78);\n"
"	border-radius: 20px;\n"
"	padding: 7px;\n"
"}")
        self.search_edit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.search_edit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.search_edit.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.horizontalLayout_4.addWidget(self.search_edit)


        self.horizontalLayout_3.addWidget(self.search_bar)

        self.search_bar_icon = QFrame(self.frame_search)
        self.search_bar_icon.setObjectName(u"search_bar_icon")
        self.search_bar_icon.setMinimumSize(QSize(45, 0))
        self.search_bar_icon.setMaximumSize(QSize(45, 45))
        self.search_bar_icon.setStyleSheet(u"")
        self.search_bar_icon.setFrameShape(QFrame.StyledPanel)
        self.search_bar_icon.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.search_bar_icon)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 6, 0, 0)
        self.frame = QFrame(self.search_bar_icon)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(40, 44))
        self.frame.setStyleSheet(u"QFrame {\n"
"	border-radius: 19px;\n"
"	background-color: none;\n"
"	border: 0px solid;\n"
"}\n"
"QFrame:hover {\n"
"	background-color:rgba(167, 200, 255, 78);\n"
"}\n"
"QFrame:pressed {\n"
"	border-radius: 22px;\n"
"	background-color: rgb(167, 200, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setStyleSheet(u"QPushButton {\n"
"	border-radius: 12px;\n"
"	background-color: none;\n"
"	border: 0px solid;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(get_res_path("icon_search_off.svg"), QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon5)
        self.btn_search.setIconSize(QSize(25, 46))

        self.horizontalLayout_9.addWidget(self.btn_search)
        self.horizontalLayout_5.addWidget(self.frame)
        self.horizontalLayout_3.addWidget(self.search_bar_icon, 0, Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_search)

        self.frame_2 = QFrame(self.verticalFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.search_list = QListWidget(self.frame_2)
        self.search_list.setObjectName(u"search_list")
        self.search_list.setStyleSheet(u"QListWidget::item {\n"
"color: rgb(255, 255, 255);\n"
"background-color:transparent;padding: 7px;\n"
"}\n"
"QListView::item:hover {\n"
"border-radius: 10px;\n"
"background:rgb(47, 47, 63);\n"
"}\n"
"QListView::item:selected {\n"
"border-radius: 10px;\n"
"background : rgba(62, 64, 90, 120);\n"
"}\n"
"QListWidget {\n"
"background-color:transparent;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none; background: rgb(29, 25, 30);\n"
"}")
        self.search_list.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.search_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.search_list.setIconSize(QSize(111, 152))
        self.search_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.search_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.search_list.setResizeMode(QListView.Adjust)
        self.search_list.setGridSize(QSize(126, 186))
        self.search_list.setViewMode(QListView.IconMode)

        self.verticalLayout_5.addWidget(self.search_list)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_4.addWidget(self.verticalFrame)

        self.stackedWidget.addWidget(self.page_search)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.content_main)


        self.verticalLayout.addWidget(self.frame_main)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_title.setText(QCoreApplication.translate("MainWindow", u"Animongo", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.app_icon.setText("")
        self.icon_menu_1.setText("")
        self.icon_menu_2.setText("")
        self.search_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cari Anime", None))
        self.btn_search.setText("")
    # retranslateUi
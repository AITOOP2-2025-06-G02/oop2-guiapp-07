# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.x.x
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QIcon, QKeySequence,
    QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QVBoxLayout, QWidget, QFrame)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 650) # ウィンドウ全体の初期サイズ

        # メインのウィジェット（すべての部品が乗る台紙）
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # 縦方向のレイアウト（上から順に並べる）
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")

        # --- 上段：画像表示エリア（横並び） ---
        self.horizontalLayout_images = QHBoxLayout()
        self.horizontalLayout_images.setObjectName(u"horizontalLayout_images")

        # 1. カメラ映像表示用ラベル
        self.lbl_camera_feed = QLabel(self.centralwidget)
        self.lbl_camera_feed.setObjectName(u"lbl_camera_feed")
        self.lbl_camera_feed.setMinimumSize(QSize(640, 480)) # VGAサイズ確保
        self.lbl_camera_feed.setFrameShape(QFrame.Box)       # 枠線をつける
        self.lbl_camera_feed.setAlignment(Qt.AlignCenter)    # 文字を真ん中に
        self.lbl_camera_feed.setStyleSheet("background-color: black; color: white;") # 黒背景

        self.horizontalLayout_images.addWidget(self.lbl_camera_feed)

        # 2. 合成結果表示用ラベル
        self.lbl_result_image = QLabel(self.centralwidget)
        self.lbl_result_image.setObjectName(u"lbl_result_image")
        self.lbl_result_image.setMinimumSize(QSize(640, 480)) # VGAサイズ確保
        self.lbl_result_image.setFrameShape(QFrame.Box)
        self.lbl_result_image.setAlignment(Qt.AlignCenter)
        self.lbl_result_image.setStyleSheet("background-color: #333; color: #aaa;") # グレー背景

        self.horizontalLayout_images.addWidget(self.lbl_result_image)

        # 上段をメインレイアウトに追加
        self.verticalLayout.addLayout(self.horizontalLayout_images)

        # --- 中段：ステータス表示 ---
        self.lbl_status = QLabel(self.centralwidget)
        self.lbl_status.setObjectName(u"lbl_status")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_status.setFont(font)
        self.lbl_status.setAlignment(Qt.AlignCenter)
        
        self.verticalLayout.addWidget(self.lbl_status)

        # --- 下段：操作ボタン（横並び） ---
        self.horizontalLayout_buttons = QHBoxLayout()
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")

        # スペーサー（ボタンを中央に寄せるためのバネのような余白）
        self.horizontalSpacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_buttons.addItem(self.horizontalSpacer_left)

        # 3. 撮影・合成ボタン
        self.btn_capture = QPushButton(self.centralwidget)
        self.btn_capture.setObjectName(u"btn_capture")
        self.btn_capture.setMinimumSize(QSize(150, 50))
        font_btn = QFont()
        font_btn.setPointSize(14)
        self.btn_capture.setFont(font_btn)

        self.horizontalLayout_buttons.addWidget(self.btn_capture)

        # 4. 保存ボタン
        self.btn_save = QPushButton(self.centralwidget)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(150, 50))
        self.btn_save.setFont(font_btn)

        self.horizontalLayout_buttons.addWidget(self.btn_save)

        # スペーサー（右側）
        self.horizontalSpacer_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_buttons.addItem(self.horizontalSpacer_right)

        # 下段をメインレイアウトに追加
        self.verticalLayout.addLayout(self.horizontalLayout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        """画面上の文字を設定する関数"""
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"画像合成カメラアプリ", None))
        self.lbl_camera_feed.setText(QCoreApplication.translate("MainWindow", u"Camera Loading...", None))
        self.lbl_result_image.setText(QCoreApplication.translate("MainWindow", u"合成結果がここに表示されます", None))
        self.lbl_status.setText(QCoreApplication.translate("MainWindow", u"準備完了：撮影ボタンを押してください", None))
        self.btn_capture.setText(QCoreApplication.translate("MainWindow", u"撮影・合成", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"画像を保存", None))
    # retranslateUi
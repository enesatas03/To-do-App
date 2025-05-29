# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(782, 593)
        Widget.setStyleSheet(u"QWidget {\n"
"    background: #ffffff;\n"
"    color: #222;\n"
"    font-family: Segoe UI, Arial, sans-serif;\n"
"    font-size: 11pt;\n"
"    background-image: \n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-attachment: fixed;\n"
"    background-size: cover;\n"
"}\n"
"QGroupBox {\n"
"    border: 1px solid #cccccc;\n"
"    border-radius: 8px;\n"
"    margin-top: 10px;\n"
"    background: #fafafa;\n"
"}\n"
"QPushButton {\n"
"    padding: 6px 16px;\n"
"    border-radius: 6px;\n"
"    background: #f5f5f5;\n"
"    border: 1px solid #cccccc;\n"
"}\n"
"QPushButton:checked, QPushButton:pressed {\n"
"    background: #e0e0e0;\n"
"}\n"
"QTableWidget {\n"
"    background: #fff;\n"
"    alternate-background-color: #f7f7f7;\n"
"    gridline-color: #e0e0e0;\n"
"}\n"
"QHeaderView::section {\n"
"    background: #e0e0e0;\n"
"    font-weight: bold;\n"
"    font-size: 12pt;\n"
"    border: 1px solid #cccccc;\n"
"}\n"
"QLineEdit, QTextEdit, QSpinBox {\n"
"    background: #fff;\n"
"  "
                        "  border: 1px solid #cccccc;\n"
"    border-radius: 4px;\n"
"}")
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(80, 20, 461, 101))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setBaseSize(QSize(6, 6))
        font = QFont()
        font.setFamilies([u"Titillium Web"])
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.lineEdit = QLineEdit(Widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 80, 113, 28))
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(211, 171, 89, 38))
        icon = QIcon()
        icon.addFile(u"../../Downloads/images.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(417, 171, 50, 38))
        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(307, 171, 103, 38))
        self.tableWidget = QTableWidget(Widget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(80, 220, 621, 341))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(510, 40, 111, 41))
        self.label_2.setMinimumSize(QSize(111, 0))
        self.label_2.setMaximumSize(QSize(111, 16777215))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 80, 63, 20))
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 130, 81, 20))
        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 120, 111, 85))
        self.spinBox = QSpinBox(Widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(474, 174, 61, 31))
        self.pushButton_dusuk = QPushButton(Widget)
        self.pushButton_dusuk.setObjectName(u"pushButton_dusuk")
        self.pushButton_dusuk.setGeometry(QRect(420, 80, 83, 29))
        self.pushButton_orta = QPushButton(Widget)
        self.pushButton_orta.setObjectName(u"pushButton_orta")
        self.pushButton_orta.setGeometry(QRect(510, 80, 83, 29))
        self.pushButton_yuksek = QPushButton(Widget)
        self.pushButton_yuksek.setObjectName(u"pushButton_yuksek")
        self.pushButton_yuksek.setGeometry(QRect(600, 80, 91, 29))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:18pt;\">Yap\u0131lacaklar Listesi</span></p><p><br/></p></body></html>", None))
        self.lineEdit.setText("")
        self.pushButton.setText(QCoreApplication.translate("Widget", u"ekle", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"sil", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"tamamla", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u00d6ncelik</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"Ba\u015fl\u0131k", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"A\u00e7\u0131klama", None))
        self.pushButton_dusuk.setText(QCoreApplication.translate("Widget", u"D\u00fc\u015f\u00fck", None))
        self.pushButton_orta.setText(QCoreApplication.translate("Widget", u"Orta", None))
        self.pushButton_yuksek.setText(QCoreApplication.translate("Widget", u"Y\u00fcksek", None))
    # retranslateUi


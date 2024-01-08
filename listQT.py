# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ToDoListForm(object):
    def setupUi(self, ToDoListForm):
        ToDoListForm.setObjectName("ToDoListForm")
        ToDoListForm.resize(1104, 518)
        ToDoListForm.setStyleSheet("/* dark_mode.qss */\n"
"\n"
"/* Ana pencere ve tüm widgetlar için arka plan rengi */\n"
"QWidget {\n"
"    background-color: #001f3f;\n"
"    color: #ffffff;\n"
"    border: 1px solid #003366; /* Widget kenarları için border rengi */\n"
"}\n"
"\n"
"/* Menü çubuğu ve araç çubuğu */\n"
"QMenuBar, QToolBar {\n"
"    background-color: #001a35;\n"
"    border: 1px solid #003366; /* Widget kenarları için border rengi */\n"
"}\n"
"\n"
"/* Menü öğeleri */\n"
"QMenu {\n"
"    background-color: #001f3f;\n"
"    border: 1px solid #003366; /* Widget kenarları için border rengi */\n"
"}\n"
"\n"
"/* Seçili menü öğesi */\n"
"QMenu::item:selected {\n"
"    background-color: #003366;\n"
"}\n"
"\n"
"/* Butonlar */\n"
"QPushButton {\n"
"    background-color: #003366;\n"
"    color: #ffffff;\n"
"    border: 1px solid #001f3f;\n"
"}\n"
"\n"
"/* Seçili buton */\n"
"QPushButton:checked {\n"
"    background-color: #004080;\n"
"}\n"
"\n"
"/* Scroll Bar */\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #003366;\n"
"    background: #001a35;\n"
"    width: 12px;\n"
"    margin: 15px 0 15px 0;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #004080;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
"    background: #001a35;\n"
"    height: 15px;\n"
"}\n"
"\n"
"/* Tab widget */\n"
"QTabWidget::pane {\n"
"    border: 1px solid #003366;\n"
"    background-color: #001a35;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: #003366;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background: #004080;\n"
"}\n"
"\n"
"/* Table Widget - Satır ve Sütunlar */\n"
"QTableWidget {\n"
"    alternate-background-color: #002233;\n"
"    background-color: #001a35;\n"
"    gridline-color: #003366;\n"
"    color: #ffffff;\n"
"    selection-background-color: #004080;\n"
"}\n"
"\n"
"/* Table Widget - İçindeki Yazılar */\n"
"QTableWidget QHeaderView::section, QTableWidget QTableCornerButton::section {\n"
"    background-color: #003366;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* Label Renk */\n"
"QLabel {\n"
"    color: #ffffff;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(ToDoListForm)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget_yenigorevekle = QtWidgets.QTabWidget(ToDoListForm)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget_yenigorevekle.setFont(font)
        self.tabWidget_yenigorevekle.setObjectName("tabWidget_yenigorevekle")
        self.tab_yenigorevekle = QtWidgets.QWidget()
        self.tab_yenigorevekle.setObjectName("tab_yenigorevekle")
        self.pushButton_kaydet = QtWidgets.QPushButton(self.tab_yenigorevekle)
        self.pushButton_kaydet.setGeometry(QtCore.QRect(310, 410, 201, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_kaydet.setFont(font)
        self.pushButton_kaydet.setStyleSheet("QPushButton#pushButton_kaydet {\n"
"    background-color: rgba(2, 65, 118, 255);\n"
"    color: rgba(255, 255, 255, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_kaydet:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(2, 65, 118, 100);\n"
"    background-position: calc(100% - 10px) center;\n"
"}")
        self.pushButton_kaydet.setObjectName("pushButton_kaydet")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.tab_yenigorevekle)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 531, 401))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_yenigorevekle = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_yenigorevekle.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_yenigorevekle.setObjectName("gridLayout_yenigorevekle")
        self.label_23 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("")
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_yenigorevekle.addWidget(self.label_23, 3, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_2)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_yenigorevekle.addWidget(self.dateTimeEdit, 4, 0, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.gridLayoutWidget_2)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout_yenigorevekle.addWidget(self.dateTimeEdit_2, 4, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("")
        self.label_24.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_24.setObjectName("label_24")
        self.gridLayout_yenigorevekle.addWidget(self.label_24, 3, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.gridLayout_yenigorevekle.addWidget(self.label_25, 0, 0, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("")
        self.label_22.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_22.setObjectName("label_22")
        self.gridLayout_yenigorevekle.addWidget(self.label_22, 1, 0, 1, 2)
        self.textEdit_gorevbilgisiekle = QtWidgets.QTextEdit(self.gridLayoutWidget_2)
        self.textEdit_gorevbilgisiekle.setObjectName("textEdit_gorevbilgisiekle")
        self.gridLayout_yenigorevekle.addWidget(self.textEdit_gorevbilgisiekle, 2, 0, 1, 2)
        self.pushButton_sil = QtWidgets.QPushButton(self.tab_yenigorevekle)
        self.pushButton_sil.setGeometry(QtCore.QRect(20, 410, 201, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_sil.setFont(font)
        self.pushButton_sil.setStyleSheet("QPushButton#pushButton_sil {\n"
"    background-color: rgba(2, 65, 118, 255);\n"
"    color: rgba(255, 255, 255, 200);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#pushButton_sil:pressed {\n"
"    padding-left: 5px;\n"
"    padding-top: 5px;\n"
"    background-color: rgba(2, 65, 118, 100);\n"
"    background-position: calc(100% - 10px) center;\n"
"}")
        self.pushButton_sil.setObjectName("pushButton_sil")
        self.tabWidget_yenigorevekle.addTab(self.tab_yenigorevekle, "")
        self.tab_gorevbilgisi = QtWidgets.QWidget()
        self.tab_gorevbilgisi.setObjectName("tab_gorevbilgisi")
        self.tabWidget_yenigorevekle.addTab(self.tab_gorevbilgisi, "")
        self.horizontalLayout.addWidget(self.tabWidget_yenigorevekle)
        self.tableWidget_gorevbilgisi_2 = QtWidgets.QTableWidget(ToDoListForm)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        self.tableWidget_gorevbilgisi_2.setFont(font)
        self.tableWidget_gorevbilgisi_2.setObjectName("tableWidget_gorevbilgisi_2")
        self.tableWidget_gorevbilgisi_2.setColumnCount(4)
        self.tableWidget_gorevbilgisi_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_gorevbilgisi_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_gorevbilgisi_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_gorevbilgisi_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_gorevbilgisi_2.setHorizontalHeaderItem(3, item)
        self.horizontalLayout.addWidget(self.tableWidget_gorevbilgisi_2)

        self.retranslateUi(ToDoListForm)
        self.tabWidget_yenigorevekle.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ToDoListForm)

    def retranslateUi(self, ToDoListForm):
        _translate = QtCore.QCoreApplication.translate
        ToDoListForm.setWindowTitle(_translate("ToDoListForm", "Form"))
        self.pushButton_kaydet.setText(_translate("ToDoListForm", "Kaydet"))
        self.label_23.setText(_translate("ToDoListForm", "Başlangıç:"))
        self.label_24.setText(_translate("ToDoListForm", "Bitiş:"))
        self.label_25.setText(_translate("ToDoListForm", "Yeni Görev Ekle"))
        self.label_22.setText(_translate("ToDoListForm", "Görev Bilgisi"))
        self.pushButton_sil.setText(_translate("ToDoListForm", "Sil"))
        self.tabWidget_yenigorevekle.setTabText(self.tabWidget_yenigorevekle.indexOf(self.tab_yenigorevekle), _translate("ToDoListForm", "Yeni Görev Ekle"))
        self.tabWidget_yenigorevekle.setTabText(self.tabWidget_yenigorevekle.indexOf(self.tab_gorevbilgisi), _translate("ToDoListForm", "Görev Bilgisi"))
        item = self.tableWidget_gorevbilgisi_2.horizontalHeaderItem(0)
        item.setText(_translate("ToDoListForm", "Görevler"))
        item = self.tableWidget_gorevbilgisi_2.horizontalHeaderItem(1)
        item.setText(_translate("ToDoListForm", "Başlangıç"))
        item = self.tableWidget_gorevbilgisi_2.horizontalHeaderItem(2)
        item.setText(_translate("ToDoListForm", "Bitiş"))
        item = self.tableWidget_gorevbilgisi_2.horizontalHeaderItem(3)
        item.setText(_translate("ToDoListForm", "Görev Durumu"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ToDoListForm = QtWidgets.QWidget()
    ui = Ui_ToDoListForm()
    ui.setupUi(ToDoListForm)
    ToDoListForm.show()
    sys.exit(app.exec_())

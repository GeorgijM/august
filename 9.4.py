
from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient)
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys


#
# from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
#     QRect, QSize, QUrl, Qt)
# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
#     QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
#     QRadialGradient)
# from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1111, 807)
        MainWindow.setToolTipDuration(-1)
        self.action1 = QAction(MainWindow)
        self.action1.setObjectName(u"action1")
        self.action2 = QAction(MainWindow)
        self.action2.setObjectName(u"action2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 70, 851, 521))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 2)

        self.toolButton = QToolButton(self.widget)
        self.toolButton.setObjectName(u"toolButton")

        self.gridLayout.addWidget(self.toolButton, 0, 3, 1, 1)

        self.toolButton_2 = QToolButton(self.widget)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.gridLayout.addWidget(self.toolButton_2, 0, 4, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 4, 0, 1, 2)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(300)
        self.spinBox.setValue(175)

        self.gridLayout.addWidget(self.spinBox, 6, 0, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)

        self.spinBox_2 = QSpinBox(self.widget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMaximum(300)
        self.spinBox_2.setValue(75)

        self.gridLayout.addWidget(self.spinBox_2, 8, 0, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)

        self.checkBox_4 = QCheckBox(self.widget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.gridLayout.addWidget(self.checkBox_4, 9, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 10, 0, 1, 2)

        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 11, 0, 1, 2)

        self.checkBox_2 = QCheckBox(self.widget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 12, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.widget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout.addWidget(self.checkBox_3, 13, 0, 1, 2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 14, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 14, 2, 1, 2)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        # self.lineEdit.setFocusPolicy(Qt.NoFocus)
        # self.lineEdit.setContextMenuPolicy(Qt.NoContextMenu)
        self.lineEdit.setMaxLength(32774)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setCursorMoveStyle(Qt.VisualMoveStyle)

        self.gridLayout.addWidget(self.lineEdit, 2, 0, 1, 4)

        self.tableWidget = QTableWidget(self.widget)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setRowCount(3)
        self.tableWidget.setColumnCount(6)

        self.gridLayout.addWidget(self.tableWidget, 0, 5, 15, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1111, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)
        QWidget.setTabOrder(self.pushButton, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.checkBox_3)
        QWidget.setTabOrder(self.checkBox_3, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.toolButton)
        QWidget.setTabOrder(self.toolButton, self.checkBox_4)
        QWidget.setTabOrder(self.checkBox_4, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.dateEdit)
        QWidget.setTabOrder(self.dateEdit, self.pushButton_2)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addSeparator()
        self.menu.addSeparator()
        self.menu.addAction(self.action2)
        self.menu.addAction(self.action1)
        self.menu.addSeparator()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.action2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.toolButton_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Birthday", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Car", None))
        self.checkBox_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Languages", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Python", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"C#", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Java", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Birtday", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Height", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Weight", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Car", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Languages", None));
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u044e", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi





data = [
    {
        "name": "John Smith",
        "birthday": "02.10.1990",
        "height": 175,
        "weight": 76.5,
        "car": True,
        "languages": ["C++", "Python"]
    },
    {
        "name": "Alexey Alexeev",
        "birthday": "05.06.1986",
        "height": 197,
        "weight": 101.2,
        "car": False,
        "languages": ["Pascal", "Delphi"]
    },
    {
        "name": "Maria Ivanova",
        "birthday": "28.08.1998",
        "height": 165,
        "weight": 56.1,
        "car": True,
        "languages": ["C#", "C++", "C"]
    }
]



class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def print_data_to_table(self):
        row = 0
        for person in data:
            col = 0

            for key, value in person.items():
                value = str(value)
                cellinfo = QTableWidgetItem(value)
                self.ui.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1

    for i in data:
        print(i)
        print(data[1]['name'])

    def add_data_to_combobox(self):
        self.ui.comboBox.clear()
        for person in data:
            person_name = person.get('name')
            self.ui.comboBox.addItem(person_name)

    #
    # def name_qline_edit(self):
    #
    #     self.ui.lineEdit.setText("Raul Sombrero")
    #     line_edit_name = self.ui.lineEdit.text()
        # print(line_edit_name)
        # self.ui.lineEdit.textChanged.connect(lambda: self.printw())

    #
    # def printw(self):
    #     line_edit_name = self.ui.lineEdit.text()
    #     print(line_edit_name)


    #
    # def birthday(self):
    #
    #
    #     birthday = self.ui.dateEdit.text()
        # print(birthday)
        # self.ui.lineEdit.textChanged.connect(lambda: self.printw())

    # @property
    def add_new_person_to_data(self):


        name = self.ui.lineEdit.text()
        birthday = self.ui.dateEdit.text()
        height = self.ui.spinBox.text()
        weight = self.ui.spinBox_2.text()
        car = self.ui.checkBox.isChecked()

        languages_check_box =[]
        if self.ui.checkBox_2.isChecked():
            languages_check_box.append('Python')
        if self.ui.checkBox_3.isChecked():
            languages_check_box.extend(['C#'])
        if self.ui.checkBox_4.isChecked():
            languages_check_box += ['Java']
        languages = languages_check_box

        # print(languages)



        new_person = {
            "name": name,
            "birthday": birthday,
            "height": height,
            "weight": weight,
            "car": car,
            "languages": languages
        }
        # print(new_person)
        # print(self.ui.checkBox.isChecked())
        data.append(new_person)
        print(data)



    def save_data(self):
        self.ui.pushButton.clicked.connect(self.add_new_person_to_data)
        self.ui.pushButton.clicked.connect(self.add_data_to_combobox)



app = QtWidgets.QApplication([])
application = mywindow()

application.print_data_to_table()
application.add_data_to_combobox()
# application.name_qline_edit()
# application.birthday()
# application.add_new_person_to_data()
application.save_data()

# print(new_person)

application.show()
sys.exit(app.exec())
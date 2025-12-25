# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_scraper.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 654)
        MainWindow.setStyleSheet(u"")
        self.actionLight_Mode = QAction(MainWindow)
        self.actionLight_Mode.setObjectName(u"actionLight_Mode")
        self.actionLight_Mode_2 = QAction(MainWindow)
        self.actionLight_Mode_2.setObjectName(u"actionLight_Mode_2")
        self.actionDark_Mode = QAction(MainWindow)
        self.actionDark_Mode.setObjectName(u"actionDark_Mode")
        self.light_mode = QAction(MainWindow)
        self.light_mode.setObjectName(u"light_mode")
        self.light_mode.setCheckable(True)
        self.dark_mode = QAction(MainWindow)
        self.dark_mode.setObjectName(u"dark_mode")
        self.dark_mode.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tapwidget = QTabWidget(self.centralwidget)
        self.tapwidget.setObjectName(u"tapwidget")
        self.tapwidget.setTabPosition(QTabWidget.TabPosition.North)
        self.tapwidget.setElideMode(Qt.TextElideMode.ElideNone)
        self.tapwidget.setDocumentMode(False)
        self.tapwidget.setTabsClosable(False)
        self.tapwidget.setMovable(False)
        self.tapwidget.setTabBarAutoHide(False)
        self.input = QWidget()
        self.input.setObjectName(u"input")
        self.verticalLayout_2 = QVBoxLayout(self.input)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.setup_group = QGroupBox(self.input)
        self.setup_group.setObjectName(u"setup_group")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setup_group.sizePolicy().hasHeightForWidth())
        self.setup_group.setSizePolicy(sizePolicy)
        font = QFont()
        font.setBold(False)
        self.setup_group.setFont(font)
        self.setup_group.setFlat(False)
        self.setup_group.setCheckable(False)
        self.verticalLayout = QVBoxLayout(self.setup_group)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.setup_group)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.location_input = QLineEdit(self.setup_group)
        self.location_input.setObjectName(u"location_input")

        self.horizontalLayout_3.addWidget(self.location_input)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.setup_group)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.max_pages = QSpinBox(self.setup_group)
        self.max_pages.setObjectName(u"max_pages")
        self.max_pages.setMinimum(1)
        self.max_pages.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.horizontalLayout_2.addWidget(self.max_pages)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.export_group = QGroupBox(self.setup_group)
        self.export_group.setObjectName(u"export_group")
        self.horizontalLayout = QHBoxLayout(self.export_group)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.csv_checkBox = QCheckBox(self.export_group)
        self.csv_checkBox.setObjectName(u"csv_checkBox")

        self.horizontalLayout.addWidget(self.csv_checkBox)

        self.Excel_checkBox = QCheckBox(self.export_group)
        self.Excel_checkBox.setObjectName(u"Excel_checkBox")

        self.horizontalLayout.addWidget(self.Excel_checkBox)

        self.json_checkBox = QCheckBox(self.export_group)
        self.json_checkBox.setObjectName(u"json_checkBox")

        self.horizontalLayout.addWidget(self.json_checkBox)

        self.all_checkbox = QCheckBox(self.export_group)
        self.all_checkbox.setObjectName(u"all_checkbox")

        self.horizontalLayout.addWidget(self.all_checkbox)


        self.verticalLayout.addWidget(self.export_group)


        self.verticalLayout_2.addWidget(self.setup_group)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.start_button = QPushButton(self.input)
        self.start_button.setObjectName(u"start_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.start_button)

        self.stop_button = QPushButton(self.input)
        self.stop_button.setObjectName(u"stop_button")

        self.horizontalLayout_6.addWidget(self.stop_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.progress_group = QGroupBox(self.input)
        self.progress_group.setObjectName(u"progress_group")
        sizePolicy.setHeightForWidth(self.progress_group.sizePolicy().hasHeightForWidth())
        self.progress_group.setSizePolicy(sizePolicy)
        self.verticalLayout_3 = QVBoxLayout(self.progress_group)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.progressBar = QProgressBar(self.progress_group)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(Qt.Orientation.Horizontal)
        self.progressBar.setInvertedAppearance(False)

        self.verticalLayout_3.addWidget(self.progressBar)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.progress_group)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.progress_page_label = QLabel(self.progress_group)
        self.progress_page_label.setObjectName(u"progress_page_label")

        self.horizontalLayout_4.addWidget(self.progress_page_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.progress_group)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.listing_found = QLabel(self.progress_group)
        self.listing_found.setObjectName(u"listing_found")

        self.horizontalLayout_5.addWidget(self.listing_found)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.progress_group)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tapwidget.addTab(self.input, "")
        self.log = QWidget()
        self.log.setObjectName(u"log")
        self.gridLayout_2 = QGridLayout(self.log)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.log_text = QTextEdit(self.log)
        self.log_text.setObjectName(u"log_text")

        self.gridLayout_2.addWidget(self.log_text, 0, 0, 1, 1)

        self.tapwidget.addTab(self.log, "")
        self.preview = QWidget()
        self.preview.setObjectName(u"preview")
        self.gridLayout_3 = QGridLayout(self.preview)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.preview_table = QTableWidget(self.preview)
        if (self.preview_table.columnCount() < 8):
            self.preview_table.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.preview_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.preview_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.preview_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.preview_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.preview_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.preview_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.preview_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.preview_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.preview_table.setObjectName(u"preview_table")

        self.gridLayout_3.addWidget(self.preview_table, 0, 0, 1, 1)

        self.tapwidget.addTab(self.preview, "")

        self.gridLayout.addWidget(self.tapwidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSettings.menuAction())
        self.menuSettings.addAction(self.dark_mode)

        self.retranslateUi(MainWindow)
        self.all_checkbox.toggled.connect(self.json_checkBox.setChecked)
        self.all_checkbox.toggled.connect(self.Excel_checkBox.setChecked)
        self.all_checkbox.toggled.connect(self.csv_checkBox.setChecked)

        self.tapwidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLight_Mode.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
        self.actionLight_Mode_2.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
        self.actionDark_Mode.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.light_mode.setText(QCoreApplication.translate("MainWindow", u"Light Mode", None))
        self.dark_mode.setText(QCoreApplication.translate("MainWindow", u"Dark Mode", None))
        self.setup_group.setTitle(QCoreApplication.translate("MainWindow", u"SetUp", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Location:", None))
        self.location_input.setPlaceholderText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Max Pages:", None))
        self.export_group.setTitle(QCoreApplication.translate("MainWindow", u"Export Format:-", None))
        self.csv_checkBox.setText(QCoreApplication.translate("MainWindow", u"CSV (default )", None))
        self.Excel_checkBox.setText(QCoreApplication.translate("MainWindow", u"Excel", None))
        self.json_checkBox.setText(QCoreApplication.translate("MainWindow", u"JSON", None))
        self.all_checkbox.setText(QCoreApplication.translate("MainWindow", u"All", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start Scraping", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.progress_group.setTitle(QCoreApplication.translate("MainWindow", u"Progress", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"inprogress page:", None))
        self.progress_page_label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"listing found:", None))
        self.listing_found.setText("")
        self.tapwidget.setTabText(self.tapwidget.indexOf(self.input), QCoreApplication.translate("MainWindow", u"Input", None))
        self.log_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tapwidget.setTabText(self.tapwidget.indexOf(self.log), QCoreApplication.translate("MainWindow", u"Log", None))
        ___qtablewidgetitem = self.preview_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Adress", None));
        ___qtablewidgetitem1 = self.preview_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Building Name", None));
        ___qtablewidgetitem2 = self.preview_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem3 = self.preview_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"AvailabilityCount", None));
        ___qtablewidgetitem4 = self.preview_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Unites", None));
        ___qtablewidgetitem5 = self.preview_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Zipcode", None));
        ___qtablewidgetitem6 = self.preview_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Detail_url", None));
        ___qtablewidgetitem7 = self.preview_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Features", None));
        self.tapwidget.setTabText(self.tapwidget.indexOf(self.preview), QCoreApplication.translate("MainWindow", u"Preview", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
    # retranslateUi


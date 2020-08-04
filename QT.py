from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import requests
import time
from bs4 import  BeautifulSoup as bs
import Game as g
from Exchange import AllExData as ex
from PlayerDatas.Player import Player as player

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.e = player()

        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.white)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        app.setPalette(palette)
        app.setWindowIcon(QIcon("ExchangeIcon.jpg"))

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()

        mainLayout = QGridLayout()
        mainLayout.setObjectName("Exchange Program")
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        self.setLayout(mainLayout)

    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Informs")

        self.label = QLabel("Budget : " + str(self.e.money) + " ₺")
        self.gainLabel = QLabel("Gain : " + str(self.e.gain) + " ₺")
        self.lossLabel = QLabel("Loss : " + str(self.e.loss) + " ₺")

        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        self.tableWidget = QTableWidget(100, 2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Name : "))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Amount : "))

        i = 1
        for name in g.nameList:
            self.tableWidget.setItem(i, 0, QTableWidgetItem(name + " : "))
            i = i + 1

        x  = 1

        for amount in range(0, 100):
            a = 0
            if self.e.isHave(amount) == False:
                a = 0
                self.tableWidget.setItem(x, 1, QTableWidgetItem("0"))
                x  = x + 1
            else:
                f = open("PlayerDatas/PlayerData" + str(amount) + ".txt", "r")
                a = str(f.readline())
                self.tableWidget.setItem(x,1, QTableWidgetItem(a))
                x = x + 1

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.gainLabel)
        layout.addWidget(self.lossLabel)
        layout.addWidget(self.tableWidget)
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)

    def createTopRightGroupBox(self):

        self.topRightGroupBox = QGroupBox("Buy/Sell")

        buyButton = QPushButton("Buy")
        buyButton.setStyleSheet("background-color : gray")
        buyButton.clicked.connect(self.buyButton)
        buyButton.setGeometry(500, 100, 50, 30)

        sellButton = QPushButton("Sell")
        sellButton.setStyleSheet("background-color : gray")
        sellButton.clicked.connect(self.sellButton)

        layout = QVBoxLayout()
        layout.addWidget(buyButton)
        layout.addWidget(sellButton)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftTabWidget(self):
        self.bottomLeftTabWidget = QTabWidget()
        self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Preferred,
                QSizePolicy.Ignored)

        tab1 = QWidget()
        tableWidget = QTableWidget(100, 8)
        tableWidget.setItem(0,0, QTableWidgetItem("Name : "))
        tableWidget.setItem(0,1, QTableWidgetItem("Price : "))
        tableWidget.setItem(0,2, QTableWidgetItem("Highest : "))
        tableWidget.setItem(0,3, QTableWidgetItem("Lowest : "))
        tableWidget.setItem(0,4, QTableWidgetItem("Average : "))
        tableWidget.setItem(0,5, QTableWidgetItem("Percent : "))
        tableWidget.setItem(0,6, QTableWidgetItem("CapacityLot : "))
        tableWidget.setItem(0,7, QTableWidgetItem("CapacityTL : "))

        def load():
            i = 1
            for name in g.nameList:
                tableWidget.setItem(i, 0, QTableWidgetItem(name + " : "))
                i = i + 1

            x = 1
            for price in g.priceList:
                tableWidget.setItem(x, 1, QTableWidgetItem(str(price)))
                x = x + 1

            y = 1
            for highest in g.highestList:
                tableWidget.setItem(y, 2, QTableWidgetItem(str(highest)))
                y = y + 1

            z = 1
            for lowest in g.lowestList:
                tableWidget.setItem(z, 3, QTableWidgetItem(str(lowest)))
                z = z + 1

            k = 1
            for average in g.averageList:
                tableWidget.setItem(k, 4, QTableWidgetItem(str(average)))
                k = k + 1

            l = 1
            for percent in g.percentList:
                tableWidget.setItem(l, 5, QTableWidgetItem(str(percent)))
                l = l + 1

            m = 1
            for capacityLot in g.capacityLotList:
                tableWidget.setItem(m, 6, QTableWidgetItem(str(capacityLot)))
                m = m + 1

            n = 1
            for capacityTL in g.capacityTlList:
                tableWidget.setItem(n, 7, QTableWidgetItem(str(capacityTL)))
                n = n + 1

        load()

        tab1hbox = QHBoxLayout()
        tab1hbox.setContentsMargins(5, 5, 5, 5)
        tab1hbox.addWidget(tableWidget)
        tab1.setLayout(tab1hbox)

        self.bottomLeftTabWidget.addTab(tab1, "&Table")

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox()

        indexLabel = QLabel("Index : ")
        indexLabel.setStyleSheet("color : black")
        amountLabel = QLabel("Amount : ")
        amountLabel.setStyleSheet("color : black")

        self.indexSpinBox = QSpinBox(self.bottomRightGroupBox)
        self.indexSpinBox.setStyleSheet("background-color : gray")
        self.indexSpinBox.setValue(50)

        self.amountSpinBox = QSpinBox(self.bottomRightGroupBox)
        self.amountSpinBox.setStyleSheet("background-color : gray")
        self.amountSpinBox.setValue(50)

        layout = QGridLayout()
        layout.addWidget(indexLabel)
        layout.addWidget(self.indexSpinBox, 1, 0, 1, 2)
        layout.addWidget(amountLabel)
        layout.addWidget(self.amountSpinBox, 3, 0, 1, 2)
        self.bottomRightGroupBox.setLayout(layout)

    def buyButton(self):
        self.e.buy(self.indexSpinBox.value() - 2, self.amountSpinBox.value())
        self.label.setText("Budget : " + str(self.e.money) + " ₺")
        self.gainLabel.setText("Gain : " + str(self.e.money - 1000) + " ₺")
        self.lossLabel.setText("Loss : " + str(1000 - self.e.money) + " ₺")
        f = open("PLayerDatas/PlayerData" + str(self.indexSpinBox.value() - 2) + ".txt")
        lot = str(f.readline())
        self.tableWidget.setItem(self.indexSpinBox.value() - 1, 1, QTableWidgetItem(lot))


    def sellButton(self):
        self.e.sell(self.indexSpinBox.value() - 2, self.amountSpinBox.value())
        self.label.setText("Budget : " + str(self.e.money) + " ₺")
        self.gainLabel.setText("Gain : " + str(self.e.money - 1000) + " ₺")
        self.lossLabel.setText("Loss : " + str(1000 - self.e.money) +  " ₺")
        f = open("PLayerDatas/PlayerData" + str(self.indexSpinBox.value() - 2) + ".txt")
        lot = str(f.readline())
        self.tableWidget.setItem(self.indexSpinBox.value() - 1, 1, QTableWidgetItem(lot))

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())

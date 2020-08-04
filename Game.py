from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)

from Exchange import AllExData as ex
import time
from PlayerDatas.Player import Player as player

gettingMoney = open("PlayerDatas/PlayerData.txt", "r")
money = str(gettingMoney.readline())
money = float(money)
gettingMoney.close()


nameList = []
priceList = []
highestList = []
lowestList = []
averageList = []
percentList = []
capacityLotList = []
capacityTlList = []

for exs in ex.exchanges_list:
    nameList.append(exs.getName())

for exs in ex.exchanges_list:
    priceList.append(exs.getPrice())

for exs in ex.exchanges_list:
    highestList.append(exs.getHighest())

for exs in ex.exchanges_list:
    lowestList.append(exs.getLowest())

for exs in ex.exchanges_list:
    averageList.append(exs.getAverage())

for exs in ex.exchanges_list:
    percentList.append(exs.getPercent())

for exs in ex.exchanges_list:
    capacityLotList.append(exs.getCapacityLot())

for exs in ex.exchanges_list:
    capacityTlList.append(exs.getCapacityTL())

def showAll():
    for i in range(0, 99):
        print("Name : " + nameList[i])
        print("Price : " + priceList[i])
        print("Highest : " + highestList[i])
        print("Lowest : " + lowestList[i])
        print("Average : " + averageList[i])
        print("Percent : " + percentList[i])
        print("CapacityLot : " + capacityLot[i])
        print("CapacityTL : " + capacityTL[i])

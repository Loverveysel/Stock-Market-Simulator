from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QTableWidgetItem)
from PyQt5.QtGui import QKeySequence, QPalette, QColor, QIcon
from PyQt5 import QtGui
import requests
import time
from bs4 import  BeautifulSoup as bs
import Game as g

trExUrl = "http://bigpara.hurriyet.com.tr/borsa/canli-borsa/"

r = requests.get(trExUrl)
soup = bs(r.content, "html.parser")

class Exchange(object):
    def __init__(self, i, Name):
        self.i = i
        self.name = Name

    def getPrice(self):
        price = soup.find_all("li", {"class":"cell048 node-f"})[self.i].text
        price = price.replace(",", ".")
        price = float(price)
        return price

    def getHighest(self):
        highest = soup.find_all("li", {"class":"cell048 node-h"})[self.i].text
        highest = highest.replace(",", ".")
        highest = float(highest)
        return highest

    def getLowest(self):
        lowest = soup.find_all("li", {"class":"cell048 node-i"})[self.i].text
        lowest = lowest.replace(",", ".")
        lowest = float(lowest)
        return lowest

    def getAverage(self):
        average = soup.find_all("li", {"class":"cell048 node-j"})[self.i].text
        average = average.replace(",", ".")
        average = float(average)
        return average

    def getPercent(self):
        percent = soup.find_all("li", {"class":"cell048 node-e"})[self.i].text
        percent = percent.replace(",", ".")
        percent = float(percent)
        return percent

    def getCapacityLot(self):
        capacityLot = soup.find_all("li", {"class":"cell064 node-k"})[self.i].text
        capacityLot = capacityLot.replace(".", "")
        capacityLot = float(capacityLot)
        return capacityLot

    def getCapacityTL(self):
        capacityTL = soup.find_all("li", {"class":"cell064 node-l"})[self.i].text
        capacityTL = capacityTL.replace(".", "")
        capacityTL = float(capacityTL)
        return capacityTL

    def getName(self):
        return self.name

class AllExData(Exchange):
    ExAefes = Exchange(0, "AEFES")
    ExAfyon = Exchange(1, "AFYON")
    ExAkbank = Exchange(2, "AKBANK")
    ExAkenr = Exchange(3, "AKENR")
    ExAksa = Exchange(4, "AKSA")
    ExAksen = Exchange(5, "AKSEN")
    ExAlark = Exchange(6, "ALARK")
    ExAlgyo = Exchange(7, "ALGYO")
    ExAnacm = Exchange(8, "ANACM")
    ExAnele = Exchange(9, "ANELE")
    ExArclk = Exchange(10, "ARCLK")
    ExAsels = Exchange(11, "ASELS")
    ExAygaz = Exchange(12, "AYGAZ")
    ExBagfs = Exchange(13, "BAGFS")
    ExBanvt = Exchange(14, "BANVT")
    ExBera = Exchange(15, "BERA")
    ExBimas = Exchange(16, "BIMAS")
    ExBizim = Exchange(17, "BIZIM")
    ExBjkas = Exchange(19, "BJKAS")
    ExBrisa = Exchange(19, "BRISA")
    ExBrsan = Exchange(20, "BRSAN")
    ExCcola = Exchange(21, "CCOLA")
    ExCemts = Exchange(22, "CEMTS")
    ExCrfsa = Exchange(23, "CRFSA")
    ExDeva = Exchange(24, "DEVA")
    ExDgklb = Exchange(25, "DGKLB")
    ExDoas = Exchange(26, "DOAS")
    ExDohol = Exchange(27, "DOHOL")
    ExEcilc = Exchange(28, "ECILC")
    ExEgeen = Exchange(29, "EGEEN")
    ExEkgyo = Exchange(30, "EKGYO")
    ExEnkai = Exchange(31, "ENKAI")
    ExErbos = Exchange(32, "ERBOS")
    ExEregl = Exchange(33, "EREGL")
    ExFener = Exchange(34, "FENER")
    ExFroto = Exchange(35, "FROTO")
    ExGaran = Exchange(36, "GARAN")
    ExGlyho = Exchange(37, "GLYHO")
    ExGolts = Exchange(38, "GOLTS")
    ExGoody = Exchange(39, "GOODY")
    ExGozde = Exchange(40, "GOZDE")
    ExGsdho = Exchange(41, "GSDHO")
    ExGsaray = Exchange(42, "GSARAY")
    ExGubrf = Exchange(43, "GUBRF")
    ExHalkb = Exchange(44, "HALKB")
    ExHlgyo = Exchange(45, "HLGYO")
    ExHurgz = Exchange(46, "HURGZ")
    ExIcbct = Exchange(47, "ICBCT")
    ExIeyho = Exchange(48, "IEYHO")
    ExIhlas = Exchange(49, "IHLAS")
    ExIhlgm = Exchange(50, "IHLGM")
    ExIpeke = Exchange(51, "IPEKE")
    ExIsctr = Exchange(52, "ISCTR")
    ExIsgyo = Exchange(53, "ISGYO")
    ExKarsn = Exchange(54, "KARSN")
    ExKartn = Exchange(55, "KARTN")
    ExKchol = Exchange(56, "KCHOL")
    ExKlgyo = Exchange(57, "KLGYO")
    ExKords = Exchange(58, "KORDS")
    ExKozaa = Exchange(59, "KOZAA")
    ExKozal = Exchange(60, "KOZAL")
    ExKrdmd = Exchange(61, "KRDMD")
    ExMavi = Exchange(62, "MAVI")
    ExMetro = Exchange(63, "METRO")
    ExMgros = Exchange(64, "MGROS")
    ExNetas = Exchange(65, "NETAS")
    ExNthol = Exchange(66, "NTHOL")
    ExOdas = Exchange(67, "ODAS")
    ExOtkar = Exchange(68, "OTKAR")
    ExPetkm = Exchange(69, "PETKM")
    ExPgsus = Exchange(70, "PGSUS")
    ExPrkme = Exchange(71, "PRKME")
    ExSahol = Exchange(72, "SAHOL")
    ExSasa = Exchange(73, "SASA")
    ExSise = Exchange(74, "SISE")
    ExSkbnk = Exchange(75, "SKBNK")
    ExSngyo = Exchange(76, "SNGYO")
    ExSoda = Exchange(77, "SODA")
    ExTatgd = Exchange(78, "TATGD")
    ExTavhl = Exchange(79, "TAVHL")
    ExTcell = Exchange(80, "TCELL")
    ExThyao = Exchange(81, "THYAO")
    ExTkfen = Exchange(82, "TKFEN")
    ExTknsa = Exchange(83, "TKNSA")
    ExTlman = Exchange(84, "TLMAN")
    ExTmsn = Exchange(85, "TMSN")
    ExToaso = Exchange(86, "TOASO")
    ExTrcas = Exchange(87, "TRCAS")
    ExTrkcm = Exchange(88, "TRKCM")
    ExTskb = Exchange(89, "TSKB")
    ExTtkom = Exchange(90, "TTKOM")
    ExTtrak = Exchange(91, "TTRAK")
    ExTuprs = Exchange(92, "TUPRS")
    ExUlker = Exchange(93, "ULKER")
    ExVakbn = Exchange(94, "VAKBN")
    ExVestl = Exchange(95, "VESTL")
    ExVkgyo = Exchange(96, "VKGYO")
    ExYatas = Exchange(97, "YATAS")
    ExYkbnk = Exchange(98, "YKBNK")
    ExZoren = Exchange(99, "ZOREN")

    exchanges_list = (ExAefes,
        ExAfyon,
        ExAkbank,
        ExAkenr,
        ExAksa,
        ExAksen,
        ExAlark,
        ExAlgyo,
        ExAnacm,
        ExAnele,
        ExArclk,
        ExAsels,
        ExAygaz,
        ExBagfs,
        ExBanvt,
        ExBera,
        ExBimas,
        ExBizim,
        ExBjkas,
        ExBrisa,
        ExBrsan,
        ExCcola,
        ExCemts,
        ExCrfsa,
        ExDeva,
        ExDgklb,
        ExDoas,
        ExDohol,
        ExEgeen,
        ExEcilc,
        ExEkgyo,
        ExEnkai,
        ExErbos,
        ExEregl,
        ExFroto,
        ExFener,
        ExGaran,
        ExGlyho,
        ExGolts,
        ExGoody,
        ExGozde,
        ExGsdho,
        ExGsaray,
        ExGubrf,
        ExHalkb,
        ExHlgyo,
        ExHurgz,
        ExIcbct,
        ExIeyho,
        ExIhlas,
        ExIhlgm,
        ExIpeke,
        ExIsctr,
        ExIsgyo,
        ExKarsn,
        ExKartn,
        ExKchol,
        ExKlgyo,
        ExKords,
        ExKozaa,
        ExKozal,
        ExKrdmd,
        ExMavi,
        ExMetro,
        ExNetas,
        ExNthol,
        ExOdas,
        ExOtkar,
        ExPetkm,
        ExPgsus,
        ExPrkme,
        ExSahol,
        ExSasa,
        ExSise,
        ExSkbnk,
        ExSngyo,
        ExSoda,
        ExTatgd,
        ExTavhl,
        ExTcell,
        ExThyao,
        ExTkfen,
        ExTknsa,
        ExTlman,
        ExTmsn,
        ExToaso,
        ExTrcas,
        ExTrkcm,
        ExTskb,
        ExTtkom,
        ExTtrak,
        ExTuprs,
        ExUlker,
        ExVakbn,
        ExVestl,
        ExVkgyo,
        ExYatas,
        ExYkbnk,
        ExZoren)

class Player(object):
    def __init__(self):
        self.money = str(open("PlayerDatas/PlayerData.txt", "r").readline())
        self.money = float(self.money)
        self.ex = AllExData(1,1)
        self.gain = self.money - 1000
        self.loss = 1000 - self.money

    def getMoney(self):
        return self.money


    def sell(self, comp, lot):
        def isHave(comp):
            try:
                f = open("PlayerDatas/PlayerData" + str(comp) + ".txt" , "r")

            except:
                return False

            compnum = str(f.readline())

            if int(compnum) >= lot:
                return True

            else:
                return False

        if isHave(comp) == True:
            commission = self.ex.exchanges_list[comp].getPrice() * 2 / 1000
            price = self.ex.exchanges_list[comp].getPrice() * lot
            self.money += price
            self.money -= commission
            print("Commission : " + str(commission))
            f = open("PlayerDatas/PlayerData" + str(comp) + ".txt", "r")
            compnum = str(f.readline())
            compnum = int(compnum)
            compnum -= lot
            f.close()
            f = open("PlayerDatas/PlayerData" + str(comp) + ".txt", "w")
            f.write(str(compnum))
            f.close()
            f = open("PlayerDatas/PlayerData.txt", "w")
            f.write(str(self.money))
            print("Price : " + str(price))
            print("Yout New Budget : " + str(self.money))
        else:
            print("You Haven't Lot Enough!")


    def isHave(self, comp):
        try:
            f = open("PlayerDatas/PlayerData" + str(comp) + ".txt" , "r")
        except:
            return False

        compnum = str(f.readline())

        if compnum == "" or compnum == "[]":
            compnum = 0
            return False

        if int(compnum) >= 0:
            return True


    def buy(self, comp, lot):
        commission = self.ex.exchanges_list[comp].getPrice() * 2 / 1000
        price = self.ex.exchanges_list[comp].getPrice() * lot
        self.money -= price
        self.money -= commission

        print("Commission : " + str(commission))

        def isHave(comp):
            try:
                f = open("PlayerDatas/PlayerData" + str(comp) + ".txt" , "r")

            except:
                return False

            compnum = str(f.readline())

            if int(compnum) >= 0:
                return True

        if isHave(comp) == True:
            f = open("PlayerDatas/PlayerData" + str(comp) + ".txt" , "r")
            compnum = str(f.readline())
            lot += int(compnum)

        else:
            f = open("PlayerDatas/PlayerData" + str(comp) + ".txt" , "w")
            compnum = 0

        print("compnum : " + str(compnum) + "\n" + "lot : " + str(lot))

        if compnum == "" or compnum == "[]":
            compnum = 0

        f.close()
        f = open("PlayerDatas/PlayerData" + str(comp) + ".txt" , "w")
        f.write(str(lot))
        f.close()

        f = open("PlayerDatas/PlayerData.txt", "w")
        f.write(str(self.money))
        f.close()
        print("Price : " + str(price))
        print("Your New Budget : " + str(self.money))


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.setWindowTitle('Just a dialog')
        self.lineedit = QLineEdit("Write something and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.connect(self.lineedit, SIGNAL("returnPressed()"),
                     self.update_ui)

    def update_ui(self):
        self.browser.append(self.lineedit.text())



class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.e = Player()

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
        self.setFixedSize(1050, 550)

        disableWidgetsCheckBox = QCheckBox("&Disable widgets")

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftTabWidget()
        self.createBottomRightGroupBox()

        disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
        disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)

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

    w = 1280; h = 720
    app = QApplication(sys.argv)
    frm = QtGui.QFrame ()
    frm.sizeHint = lambda: QtCore.QSize (w, h)
    app.setApplicationName("Exchange Program")
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())

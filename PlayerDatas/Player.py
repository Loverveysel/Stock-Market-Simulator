from Exchange import AllExData as ex

class Player(object):
    def __init__(self):
        self.money = str(open("PlayerDatas/PlayerData.txt", "r").readline())
        self.money = float(self.money)
        self.ex = ex(1,1)
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

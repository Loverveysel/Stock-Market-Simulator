import requests
import time
from bs4 import  BeautifulSoup as bs

trExUrl = "http://bigpara.hurriyet.com.tr/borsa/canli-borsa/"

r = requests.get(trExUrl)
soup = bs(r.content, "html.parser")

class Exchange(object):
    def __init__(self, i, Name):
        self.i = i
        self.name = Name

    def getPrice(self):
        print(self.i)
        price = soup.find_all("li", {"class":"cell048 node-f"})[self.i].text
        price = price.replace(".", "")
        price = price.replace(",", ".")
        price = float(price)
        return price

    def getHighest(self):
        highest = soup.find_all("li", {"class":"cell048 node-h"})[self.i].text
        highest = highest.replace(".", "")
        highest = highest.replace(",", ".")
        highest = float(highest)
        return highest

    def getLowest(self):
        lowest = soup.find_all("li", {"class":"cell048 node-i"})[self.i].text
        lowest = lowest.replace(".", "")
        lowest = lowest.replace(",", ".")
        lowest = float(lowest)
        return lowest

    def getAverage(self):
        average = soup.find_all("li", {"class":"cell048 node-j"})[self.i].text
        average = average.replace(".", "")
        average = average.replace(",", ".")
        average = float(average)
        return average

    def getPercent(self):
        percent = soup.find_all("li", {"class":"cell048 node-e"})[self.i].text
        percent = percent.replace(".", "")
        percent = percent.replace(",", ".")
        percent = float(percent)
        return percent

    def getCapacityLot(self):
        capacityLot = soup.find_all("li", {"class":"cell064 node-k"})[self.i].text
        capacityLot = capacityLot.replace(".", "")
        capacityLot = capacityLot.replace(".", "")
        capacityLot = float(capacityLot)
        return capacityLot

    def getCapacityTL(self):
        capacityTL = soup.find_all("li", {"class":"cell064 node-l"})[self.i].text
        capacityTL = capacityTL.replace(".", "")
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
      )

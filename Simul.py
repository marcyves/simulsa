from datetime import date, datetime

from random import random

class Simul:

    @staticmethod
    def line(length=50):
        print("+" + "-"*(length+4) + "+")

    @staticmethod
    def title(message):
        print("\n")
        Simul.line(len(message))
        print("| ", message, " |")
        Simul.line(len(message))

    @staticmethod
    def menu(items, message):
        print("")
        for i, item in enumerate(items, start=1):
            print("\t{} - {}".format(i, item))
        print("")
        
        answer = 0
        while answer < 1 or answer > i:
            try:
                answer = int(input("{} ==> ".format(message)))
            except ValueError:
                answer = 0

        return answer

    @staticmethod
    def get_choice(message, choix1, choix2):
        answer = ""
        while(answer != choix1 and answer != choix2):
            answer = input("{} ({}/{}) ==> ".format(message, choix1, choix2)).upper()
        return answer

    @staticmethod
    def get_int(message):
        while True:
            try:
                answer = int(input("{} ==> ".format(message)))
                break
            except:
                pass

        return answer

    @staticmethod
    def get_name(message, max=10):
        name = ""
        while name == "" or len(name) > max:
            name = input("{} (maximum {} caractères) ==> ".format(message, max))
        
        return name

    def __init__(self):
        self.title("SIMUL SA")
        print("Créer des programmes, asssurer leur duplication et leur conditionnement, organiser leurs points de vente et leur distribution, et les soutenir avec une campagne publicitaire, voilà les tâches élémentaires d'une société de logiciels.")
        print("Vous êtes son P.D.G : sachez doser chaque action, évaluer chaque investissement, prendre des risques quand il le faut...")
        print("Méfiance, la faillite vous guette !")

        self.GameOptions = ["Fabrication", "Production", "Publicité", "Ventes", "Fin de la journée", "Fin du jeu"]
        self.SoftwareCategories = ["Education", "Gestion", "Professionnel", "Personnel", "Utilitaire", "Artistique", "Jeux"]

        # Ligne 1700
        # TN
        # Points de vente
        self.SalesPoints ={
            "Micropoint":{"Qualité":5,"Actif":0, "Distance":78.0, "Articles":[]},
            "Computer":{"Qualité":2, "Actif":0, "Distance":29.0, "Articles":[]},
            "Chip's":{"Qualité":4, "Actif":0, "Distance":15.0, "Articles":[]},
            "SoftShop":{"Qualité":3, "Actif":0, "Distance":98.0, "Articles":[]},
            "Point-Data":{"Qualité":1, "Actif":0, "Distance":6.0, "Articles":[]},
            "List/Plus":{"Qualité":1, "Actif":0, "Distance":71.0, "Articles":[]},
            "Microwave":{"Qualité":2, "Actif":0, "Distance":49.0, "Articles":[]},
            "Puce-Center":{"Qualité":3, "Actif":0, "Distance":31.0, "Articles":[]},
            "Microhouse":{"Qualité":4, "Actif":0, "Distance":18.0, "Articles":[]},
            "PuceGalery":{"Qualité":5, "Actif":0, "Distance":10.0, "Articles":[]},
            "Ordiland":{"Qualité":4, "Actif":0, "Distance":97.0, "Articles":[]},
            "Orditheque":{"Qualité":3, "Actif":0, "Distance":7.0, "Articles":[]},
            "Soft-Hall":{"Qualité":2, "Actif":0, "Distance":13.0, "Articles":[]},
            "Phone-Home":{"Qualité":5, "Actif":0, "Distance":52.0, "Articles":[]},
            "Hard & Soft":{"Qualité":1, "Actif":0, "Distance":69.0, "Articles":[]}
        }

        # IU
        # Noms des médias
        self.media = ["Affiches", "Journaux", "Soft & Micro", "Radio", "Télévision"]

        # E
        self.meteo = ["Exceptionnel", "Très beau", "beau", "Infect", "Pluvieux", "Couvert"]

        # W
        # Probabilités de vente par catégorie et par qualité
        self.SalesProbability = [
            [50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50],
            [50, 50, 50, 50, 50]
        ]

        self.today = date.today()

        self.trésorerie = 5000              # SD Caisse du joueur
        self.ArticlesProduced = 0           # FA Nombre d'articles créés
        self.ActionsToday = 0               # NA Nombre d'actions par jour
        self.AR = {}                        # TS est contenu dans AR sous l'indice "Stock"
        self.trésoreriePrécédente = self.trésorerie # TTV

    def next_day(self, JA):
        # Ligne 910 Date
        self.today = self.today.replace(day=self.today.day + JA)
    
    def announce(self): # Ligne 1900 Faits du jour              
        self.title("Nous sommes {}".format(datetime.strftime(self.today, '%A %d %B %Y')))

        SoftwareType = int(random() * 7)
        SoftwareQuality = int(random() * 5)
        self.SalesProbability[SoftwareType][SoftwareQuality] = self.SalesProbability[SoftwareType][SoftwareQuality] + int(random() * 10)
        print("\nEn ouvrant votre journal, vous apprenez que les logiciels de catégorie {} et de qualité {} se vendent mieux !".format(self.SoftwareCategories[SoftwareType], SoftwareQuality))
        
        SoftwareType = int(random() * 7)
        SoftwareQuality = int(random() * 5)
        self.SalesProbability[SoftwareType][SoftwareQuality] = self.SalesProbability[SoftwareType][SoftwareQuality] - int(random() * 10)
        print("\nLes logiciels de catégorie {} et de qualité {} se vendent moins !".format(self.SoftwareCategories[SoftwareType], SoftwareQuality))
        
        ME = int(random() * 6)
        print("\nLe temps est {}".format(self.meteo[ME]))

        if ME > 3:
            ME = ME - 7
        for X in range(7):
            for Y in range(5):
                self.SalesProbability[X][Y] = self.SalesProbability[X][Y] + ME * 2

        self.title("Une nouvelle journée commence...")

    def balance(self):  # 2160 RESULTATS
        self.title("Vos comptes au {}".format(datetime.strftime(self.today, '%A %d %B %Y')))
        print("Vous avez dépensé {}€, il vous reste {}€ en trésorerie".format(self.trésoreriePrécédente - self.trésorerie, self.trésorerie))
        self.trésoreriePrécédente = self.trésorerie
        print("Voici le tableau des ventes en euros :")
        AvailableSalesPoints = []
        for item, value in self.SalesPoints.items():
            if value["Actif"] == 1:
                AvailableSalesPoints.append(item)
        if len(AvailableSalesPoints) > 0:
            for SalesPoint in AvailableSalesPoints:
                print("\t== Point de vente : {}".format(SalesPoint))

                if self.SalesPoints[SalesPoint]["Actif"] != 0:
                    for ArticleName in self.SalesPoints[SalesPoint]["Articles"]:
                        print("\n\t  - Article : {}".format(ArticleName))

                        Price = self.AR[ArticleName]["Prix"]
                        Q  = self.AR[ArticleName]["Qualité"]
                        ST = self.AR[ArticleName]["Catégorie"]
                        FR = self.AR[ArticleName]["Support"]

                        TodaySales = self.SalesPoints[SalesPoint]["Qualité"] * 2 +int(random() * 5) + self.SalesPoints[SalesPoint]["Distance"] / 20 + self.AR[ArticleName]["Stock"] * 10
                        PC = Q * 10 + FR * 20 + 10
                        WA = self.SalesProbability[ST][Q]
                        if Price > PC * 2:
                            WA = WA / 2
                        if WA > 100:
                            WA = 100
                        TodaySales = int((TodaySales * WA)/100)
                        if TodaySales > self.AR[ArticleName]["Stock"]:
                            TodaySales = self.AR[ArticleName]["Stock"]
                        
                        TodaySales = int(TodaySales * Price)
                        self.trésoreriePrécédente += TodaySales
                        print(self.AR[ArticleName])

        self.trésoreriePrécédente = self.trésoreriePrécédente * 0.9
        print("Au total vous avez gagné {}€".format(self.trésoreriePrécédente))
        self.trésorerie += self.trésoreriePrécédente
        print("Vous avez {}€ en caisse.".format(self.trésorerie))

    def fabrication(self): # 20
        self.title("Fabrication")
        if self.ArticlesProduced > 49:
            print("Vous avez suffisamment d'articles")
        else:
            SoftwareName  = self.get_name("Nom de ce nouveau logiciel")
            Author = self.get_name("Nom de son auteur")
            Quality = 0
            while Quality < 1 or Quality > 5:
                Quality = self.get_int("Qualité de ce produit (1 à 5)")

            SoftwareCategory = self.menu(self.SoftwareCategories, "Dans quelle catégorie le classer")

            F = self.get_choice("Sera-t'il sur disquette ou cassette", "D", "C")

            FR = 2 if F == "D" else 1
            ProductionCost = (Quality * 10) + (SoftwareCategory * 2) + (FR * 20) + int(random() * 10)

            print("Vous devrez payer {} € pour ajouter {} à votre catalogue".format(ProductionCost, SoftwareName))

            SalesPrice = self.get_int("Combien le vendrez-vous ?")
            self.trésorerie = self.trésorerie - ProductionCost

            self.AddArticle(SoftwareName, Author, Quality, SoftwareCategory, FR, SalesPrice)

    def AddArticle(self, SoftwareName, Author, Quality, SoftwareCategory, FR, SalesPrice):
        self.ArticlesProduced += 1
        self.AR[SoftwareName] = {
                                    "Auteur":Author,
                                    "Qualité":Quality,
                                    "Catégorie":SoftwareCategory,
                                    "Support":FR,
                                    "Prix":SalesPrice,
                                    "Stock":0,
                                    "Ventes":0,
                                    "Publicité":0
                                }
        self.ActionsToday += 1

    def préparation(self): # 390
        if any(self.AR.values()):
            index = self.menu(self.AR.keys(), "Quel logiciel à traiter ?") - 1
            key_list = list(self.AR)
            SoftwareName = key_list[index]
            SoftwareDetails = self.AR[SoftwareName]

            self.line()
            print("Vous avez choisi le logiciel : '{}'".format(SoftwareName))

            for item, detail in SoftwareDetails.items():
                if item == "Catégorie":
                    detail = self.SoftwareCategories[detail - 1]
                print("{:.12}\t: {}".format(item + " . . . . ", detail))
        else:
            self.title("Vous n'avez aucun produit en catalogue")
            SoftwareName = False
    
        return SoftwareName

    def production(self, SoftwareName): # 390
        self.title("Production")

        QuantityToProduce = self.get_int("Combien voulez-vous produire d'articles ?")
        Qualité = self.AR[SoftwareName]["Qualité"]
        Support = self.AR[SoftwareName]["Support"]
        ProductionPrice = int(QuantityToProduce * Qualité) + int(Support * 4) + int(random() * QuantityToProduce)
        print("Cela vous coutera {} €.".format(ProductionPrice))
        if ProductionPrice > self.trésorerie:
            print("Est-ce bien raisonnable ?")
        REP = self.get_choice("Lancez-vous cette production", "O", "N")
        if REP == "O":
            self.AR[SoftwareName]["Stock"] += QuantityToProduce
            self.trésorerie = self.trésorerie - ProductionPrice
            self.ActionsToday += 1

    def publicité(self, SoftwareName): # 390
        if SoftwareName != None:
            self.title("Publicité")
            Qualité = self.AR[SoftwareName]["Qualité"]
            MD = self.menu(self.media, "Quel support choisissez-vous ?")
            PUB = (MD * 1000 ) + (Qualité * 10) + int(random() * 1000)
            self.line()
            print("Cela vous coutera {} €.".format(PUB))
            REP = self.get_choice("Voulez-vous continuer ?", "O", "N")
            if REP == "O":
                self.AR[SoftwareName]["Publicité"] += PUB
                self.trésorerie -= PUB
                self.ActionsToday += 1

    def SalesPointMenu(self, status):
        # Création point de vente
        AvailableSalesPoints = []
        for item, value in self.SalesPoints.items():
            if value["Actif"] == status:
                AvailableSalesPoints.append(item)
        if len(AvailableSalesPoints) > 0:
            PN = self.menu(AvailableSalesPoints, "Quel point de vente choisissez-vous ?")

            SalesPointName = AvailableSalesPoints[PN-1]
        else:
            self.title("Il n'y a pas de point de vente qui corresponde à votre demande")
            SalesPointName = False

        return SalesPointName

    def AddArticleToSalesPoint(self, SalesPointName, SoftwareName):
        CPV = (self.SalesPoints[SalesPointName]["Qualité"] * 1000) + ( self.SalesPoints[SalesPointName]["Distance"] * 2.5) + int(random() *20)
        print("Cela vous coutera {} €.".format(CPV))
        if CPV > self.trésorerie:
            self.title("Vous n'avez pas les moyens de financer cette opération")
        else:
            REP = self.get_choice("Voulez-vous continuer ?", "O", "N")
            if REP == "O":
                self.SalesPoints[SalesPointName]["Actif"] = 1
                self.trésorerie -= CPV
                self.SalesPoints[SalesPointName]["Articles"].append(SoftwareName)

    def ventes(self, SoftwareName): # 960 
        self.title("Ventes")
        REP = self.get_choice("Voulez-vous occuper un nouveau point de ventes ?", "O", "N")
        if REP == "O":
            # Création point de vente
            R = 0
        else:
            R = 1
        SalesPointName = self.SalesPointMenu(R)
        if SalesPointName:
            self.AddArticleToSalesPoint(SalesPointName, SoftwareName)


from datetime import date, datetime
from random import random

class Simul:

    @staticmethod
    def line(length=50):
        print("-"*length)

    @staticmethod
    def title(message):
        print("\n")
        Simul.line()
        print("\t", message)
        Simul.line()

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
            "Micropoint":[5,0, 78.0],
            "Computer":[2,0, 29.0],
            "Chip's":[4, 0, 15.0],
            "SoftShop":[3,0, 98.0],
            "Point-Data":[1,0, 6.0],
            "List/Plus":[1, 0, 71.0],
            "Microwave":[2, 0, 49.0],
            "Puce-Center":[3,0, 31.0],
            "Microhouse":[4, 0, 18.0],
            "PuceGalery":[5, 0, 10.0],
            "Ordiland":[4, 0, 97.0],
            "Orditheque":[3, 0, 7.0],
            "Soft-Hall":[2, 0, 13.0],
            "Phone-Home":[5, 0, 52.0],
            "Hard & Soft":[1, 0, 69.0]
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

        self.trésorerie = 5000              # Caisse du joueur
        self.ArticlesProduced = 0                 # Nombre d'articles créés
        self.ActionsToday = 0                 # Nombre d'actions par jour
        self.AR = {}
        self.trésoreriePrécédente = self.trésorerie

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
            if value[1] == 1:
                AvailableSalesPoints.append(item)
        if len(AvailableSalesPoints) > 0:
            for SalesPoint in AvailableSalesPoints:
                print("{} : ".format(SalesPoint))

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

        QP = self.get_int("Combien voulez-vous produire d'articles ?")
        Qualité = self.AR[SoftwareName]["Qualité"]
        Support = self.AR[SoftwareName]["Support"]
        PP = (QP * Qualité + (Support * 3.5)) + int(random() * QP)
        print("Cela vous coutera {} €.".format(PP))
        if PP > self.trésorerie:
            print("Est-ce bien raisonnable ?")
        REP = self.get_choice("Lancez-vous cette production", "O", "N")
        if REP == "O":
            self.AR[SoftwareName]["Stock"] += QP
            self.trésorerie = self.trésorerie - PP
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
            if value[1] == status:
                AvailableSalesPoints.append(item)
        if len(AvailableSalesPoints) > 0:
            PN = self.menu(AvailableSalesPoints, "Quel point de vente choisissez-vous ?")

            SalesPointName = AvailableSalesPoints[PN-1]
        else:
            self.title("Il n'y a pas de point de vente qui corresponde à votre demande")
            SalesPointName = False

        return SalesPointName

    def ventes(self, SoftwareName): # 960 
        self.title("Ventes")
        REP = self.get_choice("Voulez-vous occuper un nouveau point de ventes ?", "O", "N")
        if REP == "O":
            # Création point de vente
            SalesPointName = self.SalesPointMenu(0)

            if SalesPointName:
                CPV = (self.SalesPoints[SalesPointName][0] * 1000) + ( self.SalesPoints[SalesPointName][2] * 2.5) + int(random() *20)
                print("Cela vous coutera {} €.".format(CPV))
                if CPV > self.trésorerie:
                    self.title("Vous n'avez pas les moyens de financer cette opération")
                else:
                    REP = self.get_choice("Voulez-vous continuer ?", "O", "N")
                    if REP == "O":
                        self.SalesPoints[SalesPointName][1] = 1
                        self.trésorerie -= CPV
        else: # 1200
            # Sélection point de vente
            SalesPointName = self.SalesPointMenu(1)
            if SalesPointName:
                pass
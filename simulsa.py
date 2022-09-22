
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
        # JM
        self.jours_mois =[31,28,31,30,31,30,31,31,30,31,30,31]

        # TN
        # Points de vente
        self.TN = [
            ["Micropoint", 5,0, 78],
            ["Computer", 2,0, 29],
            ["Chip's", 4, 0, 15],
            ["SoftShop", 3,0, 98],
            ["Point-Data", 1,0, 6],
            ["List/Plus", 1, 0, 71],
            ["Microwave", 2, 0, 49],
            ["Puce-Center", 3,0, 31],
            ["Microhouse", 4, 0, 18],
            ["PuceGalery", 5, 0, 10],
            ["Ordiland", 4, 0, 97],
            ["Orditheque", 3, 0, 7],
            ["Soft-Hall", 2, 0, 13],
            ["Phone-Home", 5, 0, 52],
            ["Hard & Soft", 1, 0, 69]
        ]

        # IU
        # Noms des médias
        self.IU = ["Affiches", "Journaux", "Soft & Micro", "Radio", "Télévision"]

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

        self.SD = 5000              # Caisse du joueur
        self.FA = 0                 # Nombre d'articles créés
        self.NA = 0                 # Nombre d'actions par jour
        self.AR = {}
        self.TVV = self.SD


    def next_day(self, JA):
        # Ligne 910 Date
        self.today = self.today.replace(day=self.today.day + JA)
    
    def announce(self):
        # Ligne 1900 Faits du jour
                
        self.title("Nous sommes {}".format(datetime.strftime(self.today, '%A %d %B %Y')))

        SoftwareType = int(random() * 7)
        SoftwareQuality = int(random() * 5)
        self.SalesProbability[SoftwareType][SoftwareQuality] = self.SalesProbability[SoftwareType][SoftwareQuality] + int(random() * 10)
        print("En ouvrant votre journal, vous apprenez que les logiciels de catégorie {} et de qualité {} se vendent mieux !".format(SoftwareType, SoftwareQuality))
        
        SoftwareType = int(random() * 7)
        SoftwareQuality = int(random() * 5)
        self.SalesProbability[SoftwareType][SoftwareQuality] = self.SalesProbability[SoftwareType][SoftwareQuality] - int(random() * 10)
        print("Les logiciels de catégorie {} et de qualité {} se vendent moins !".format(SoftwareType, SoftwareQuality))
        
        ME = int(random() * 6)
        print("Le temps est {}".format(self.meteo[ME]))

        if ME > 3:
            ME = ME - 7
        for X in range(7):
            for Y in range(5):
                self.SalesProbability[X][Y] = self.SalesProbability[X][Y] + ME * 2

        print("Une nouvelle journée commence...")

    def balance(self):
        # 2160
        self.title("Vos comptes au {}".format(datetime.strftime(self.today, '%A %d %B %Y')))
        pass      

    def fabrication(self):
        # 20
        self.title("Fabrication")
        if self.FA > 49:
            print("Vous avez suffisamment d'articles")
        else:
            SoftwareName  = self.get_name("Nom de ce nouveau logiciel")
            AUT = self.get_name("Nom de son auteur")
            Q = 0
            while Q < 1 or Q > 5:
                Q = self.get_int("Qualité de ce produit (1 à 5)")

            ST = self.menu(self.SoftwareCategories, "Dans quelle catégorie le classer")

            F = ""
            while F != "D" and F != "C":
                F = input("Sera-t'il sur disquette ou cassette (D/C) ==> ")
            FR = 2 if F == "D" else 1

            FB = (Q * 10) + (ST * 2) + (FR * 20) + int(random() * 10)

            print("Vous devrez payer {} € pour ajouter {} à votre catalogue".format(FB, SoftwareName))

            PC = self.get_int("Combien le vendrez-vous ?")

            self.SD = self.SD - FB
            self.FA += 1
#            self.AR[self.FA] = [ NM, AUT, Q, ST, FR, PC ]
            self.AR[SoftwareName] = {
                                      "Auteur":AUT,
                                      "Qualité":Q,
                                      "Catégorie":ST,
                                      "Support":FR,
                                      "Prix":PC,
                                      "Stock":0,
                                      "Ventes":0
                                    }
            self.NA += 1

    def préparation(self):
        # 390
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
    
        return SoftwareName

    def production(self, SoftwareName):
        # 390
        self.title("Production")

        QP = self.get_int("Combien voulez-vous produire d'articles ?")
        Qualité = self.AR[SoftwareName]["Qualité"]
        Support = self.AR[SoftwareName]["Support"]
        PP = (QP * Qualité + (Support * 3.5)) + int(random() * QP)
        print("Cela vous coutera {} €.".format(PP))
        if PP > self.SD:
            print("Est-ce bien raisonnable ?")
        REP = ""
        while(REP != "O" and REP != "N"):
            REP = input("Lancez-vous cette production (O/N) ==> ")
        if REP == "O":
            self.AR[SoftwareName]["Stock"] += QP
            self.SD = self.SD - PP
            self.NA += 1

    def publicité(self):
        # 390 ??
        self.title("Publicité")
        pass

    def ventes(self):
        # 960
        self.title("Ventes")
        pass


game = Simul()

# 2600 Boucle principale

game.next_day(1)    #  910
game.announce()     # 1900
NA = 1

choice = 0
while True:
    while choice < 5:
        choice = game.menu(game.GameOptions, "Votre choix")         # 1540
        if choice == 1:
            game.fabrication()
        else:
            SoftwareName = game.préparation()            
            if choice == 2:
                game.production(SoftwareName)
            elif choice == 3: 
                game.publicité(SoftwareName)
            elif choice == 4:
                game.ventes(SoftwareName)

    game.balance()      # 2160

    if choice == 6:
        break
    else:
        choice = 0
        game.next_day(1)


print("Bye...")
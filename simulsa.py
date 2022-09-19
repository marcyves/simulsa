
from datetime import date, time, datetime
from random import Random, random

def title(message):
    print("-"*40)
    print("\t", message)
    print("-"*40)

class Simul:

    def __init__(self):
        title("SIMUL SA")
        print("Créer des programmes, asssurer leur duplication et leur conditionnement, organiser leurs points de vente et leur distribution, et les soutenir avec une campagne publicitaire, voilà les tâches élémentaires d'une société de logiciels.")
        print("Vous êtes son P.D.G : sachez doser chaque action, évaluer chaque investissement, prendre des risques quand il le faut...")
        print("Méfiance, la faillite vous guette !")
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
        self.TVV = self.SD

    def next_day(self, JA):
        # Ligne 910 Date
        self.today = self.today.replace(day=self.today.day + JA)
    
    def announce(self):
        # Ligne 1900 Faits du jour
                
        title("Nous sommes {}".format(datetime.strftime(self.today, '%A %d %B %Y')))

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

    def menu(self):
        # 1540
        print("1 - Fabrication")
        print("2 - Production")
        print("3 - Publicité")
        print("4 - Ventes")
        print("5 - Fin de la journée")
        print("6 - Fin du jeu")

        rep = 0
        while rep < 1 or rep > 6:
            rep = int(input("Votre choix ==> "))
        
        return rep

    def balance(self):
        # 2160
        title("Vos comptes au {}".format(datetime.strftime(self.today, '%A %d %B %Y')))
        pass      

    def fabrication(self):
        # 20
        title("Fabrication")
        if self.FA > 49:
            print("Vous avez suffisamment d'articles")
        else:
            NM = ""
            while NM == "" or len(NM) > 10:
                NM = input("Nom de ce nouveau logiciel (maximum 10 caractères) ==> ")
            AUT = ""
            while AUT != "" and AUT.length()< 10:
                AUT = input("Nom de son auteur (maximum 10 caractères) ==> ")
            Q = 0
            while Q < 1 or Q > 5:
                Q = int(input("Qualité de ce produit (1 à 5) ==> "))
            print("1 - Education")
            print("2 - Gestion")
            print("3 - Professionnel")
            print("4 - Personnel")
            print("5 - Utilitaire")
            print("6 - Artistique")
            print("7 - Jeux")
            ST = 0
            while ST < 1 or ST > 7:
                ST = int(input("Dans quelle catégorie le classer ==> "))
            F = ""
            while F != "D" and F != "C":
                F = input("Sera-t'il sur disquette ou cassette (D/C) ==> ")
            FR = 2 if F == "D" else 1

            FB = (Q * 10) + (ST * 2) + (FR * 20) + int(random() * 10)

            print("Vous devrez payer {} € pour ajouter {} à votre catalogue".format(FB, NM))

            PC = input("Combien le vendrez-vous ? ==> ")

            self.SD = self.SD - FB
            self.FA += 1
            self.AR[self.FA] = [ NM, AUT, Q, ST, FR, PC ]
            self.NA += 1

    def production(self):
        # 390
        title("Production")

        pass

    def publicité(self):
        # 390 ??
        title("Publicité")
        pass

    def ventes(self):
        # 960
        title("Ventes")
        pass


game = Simul()

# 2600 Boucle principale

game.next_day(1)    #  910
game.announce()     # 1900
NA = 1

choice = 0
while choice < 5:
    choice = game.menu()         # 1540
    if choice == 1:
        game.fabrication()
    elif choice == 2:
        game.production()
    elif choice == 3: 
        game.publicité()
    elif choice == 4:
        game.ventes()

game.balance()      # 2160
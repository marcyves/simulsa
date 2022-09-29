import Simul as S

game = S.Simul()

# Test Data

game.AddArticle("Windows", "Bill Gates", 1, 1, 1, 100)
game.AddArticle("Word", "Bill Gates", 2, 2, 1, 150)
game.AddArticle("Excel", "Bill Gates", 3, 3, 2, 200)
game.AddArticle("Powerpoint", "Bill Gates", 4, 4, 2, 300)

# 2600 Boucle principale

gameOn = True
while gameOn:
    game.announce()     # 1900
    choice = 0
    game.NA = 1
    while choice < game.GameOptions.index("Fin de la journée"):
        choice = game.menu(game.GameOptions, "Votre choix") - 1        # 1540
        if choice == game.GameOptions.index("Fabrication"):
            game.fabrication()
        elif choice == game.GameOptions.index("Tableau de Bord"):
            game.balance()
        elif choice < game.GameOptions.index("Fin de la journée"):
            SoftwareName = game.préparation()
            if SoftwareName:            
                if choice == game.GameOptions.index("Production"):
                    game.production(SoftwareName)
                elif choice == game.GameOptions.index("Publicité"): 
                    game.publicité(SoftwareName)
                elif choice == game.GameOptions.index("Ventes"):
                    game.ventes(SoftwareName)

    game.balance()      # 2160
    # Vérification fin de jeu
    if game.trésorerie < 100:
        print("C'est une faillite")
        gameOn = False
    elif game.ArticlesProduced > 49 and game.trésorerie > 1000000:
        print("Vous êtes maitre du marché, c'est gagné")
        gameOn = False
    elif choice == game.GameOptions.index("Fin du jeu"):
        gameOn = False
    else:
        game.next_day(1)


print("Bye...")
import Simul as S

game = S.Simul()

# 2600 Boucle principale

game = True
while game:
    game.announce()     # 1900
    choice = 0
    game.NA = 1
    while choice < 5:
        choice = game.menu(game.GameOptions, "Votre choix")         # 1540
        if choice == 1:
            game.fabrication()
        elif choice < 5:
            SoftwareName = game.préparation()
            if SoftwareName:            
                if choice == 2:
                    game.production(SoftwareName)
                elif choice == 3: 
                    game.publicité(SoftwareName)
                elif choice == 4:
                    game.ventes(SoftwareName)

    game.balance()      # 2160
    # Vérification fin de jeu
    if game.trésorerie < 100:
        print("C'est une faillite")
        game = False
    elif game.ArticlesProduced > 49 and game.trésorerie > 1000000:
        print("Vous êtes maitre du marché, c'est gagné")
        game = False
    elif choice == 6:
        game = False
    else:
        game.next_day(1)


print("Bye...")
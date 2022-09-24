import Simul as S

game = S.Simul()

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

    if choice == 6:
        break
    else:
        choice = 0
        game.next_day(1)


print("Bye...")
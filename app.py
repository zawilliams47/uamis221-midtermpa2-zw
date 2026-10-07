
import time
import random

def main_menu_gui():
    print("=" * 40)
    print("Captian's Cove - Main menu")
    print("=" * 40)
    print(f"Doubloons: {doubloons[0]} | Reputation: {reputations[0]}")
    print("-" * 40)
    print("1. Dice Duel\n2. Hire the Fleet\n3. Leave the Cove")
    choice = int(input("Enter your choice: "))
    return choice

def check_win(choice):
    if doubloons[0] <= 0:
        print("You ran out of doubloons! Try again next time.")
        choice = "User_Lost"
    if reputations[0] >= 30:
        print("Congrats! You win!")
        choice = "User_Won"
    return choice

def rtd():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    return dice1, dice2, dice3

def hit():
    dice_hit = random.randint(1, 6)
    return dice_hit

def user_roll():
    print("----- Dice Duel Rules -----")
    print("3 Dice are rolled. You will need to attain")
    print("a larger sum than your opponent. Hit until")
    print("you are close to 21, since if you go over,")
    print("you will lose!")
    global choice
    choice = check_win(choice)
    wager = int(input("How many doubloons will you wager: "))
    while wager > doubloons[0]:
         print("You don't have enough doubloons for that!")
         wager = int(input("How many doubloons will you wager: "))
    dice1, dice2, dice3 = rtd() #added 3 dice so that double down makes more sense
    total = dice1 + dice2 + dice3
    bust = "False"
    print(f"Doubloons: {doubloons[0]} | Reputation: {reputations[0]}")
    print(f"You roll: {dice1}, {dice2}, and {dice3}. | Total: {total}")
    if doubloons[0] / 2 >= wager:
        dd = 0
        while dd != "y" and dd != "n":
            dd = str(input("Double down? (y/n): "))
            if dd == "y":
                wager = wager * 2
                dice_hit = hit()
                print("Rolling dice...")
                time.sleep(0.5)
                total = dice_hit + total
                print(f"You roll {dice_hit} | Total {total}")
                if total > 21:
                    bust = "True"
                    print(f"--- You bust! Lost {wager} doubloons ---")
                    return total, wager, bust
                else:
                    bust = "False"
                    print(f"You doubled down on {total}")
                    time.sleep(0.5)
                    return total, wager, bust
    decision = str(input("Hit or stand: "))
    while decision.lower() != "hit" and decision.lower() != "stand":
         print("Please input a valid choice")
         decision = str(input("Hit or stand: "))
    if decision.lower() == "hit":
            while decision.lower() == "hit":
                print("Rolling dice...")                
                time.sleep(0.7)
                dice_hit = hit()
                total += dice_hit
                if total > 21:
                     print(f"You roll {dice_hit} | Total: {total}")
                     print(f"--- You bust! Lost {wager} doubloons ---")
                     bust = "True"
                     return total, wager, bust
                print(f"You roll {dice_hit} | Total: {total}")
                decision = str(input("Hit or stand: "))
    elif decision.lower() == "stand":
        print(f"You stood on {total}")
    else:
        print("Please input a valid choice")
        return
    return total, wager, bust

def enemy_roll(bust):
     if bust == "False":
          dice1, dice2, dice3 = rtd()
          total = dice1 + dice2 + dice3
          print(f"Enemy rolls {dice1}, {dice2}, and {dice3} | Total: {total}")
          while total < 17:
               time.sleep(0.7)
               print("Enemy hits...")
               dice_hit = hit()
               total += dice_hit
               time.sleep(0.7)
               print(f"Enemy rolls {dice_hit} | Total: {total}")
          print(f"Enemy stands on {total}")
          return total
     else:
          return

def who_wins(wager, bust, usertotal, enemytotal):
     if bust == "True":
          doubloons[0] = doubloons[0] - wager
     elif enemytotal > 21:
         print(f"Enemy busted! Congrats!")
         print(f"You won {wager} doubloons")
         doubloons[0] += wager
     elif enemytotal == 21 and usertotal == 21:
              print(f"Congrats! You won {wager} doubloons")
              doubloons[0] += wager
     elif enemytotal >= usertotal:
          print(f"You lost! You lose {wager} doubloons")
          doubloons[0] = doubloons[0] - wager
     elif usertotal == 21:
         print(f"Congrats! You won {wager} doubloons")
         doubloons[0] += wager
     else:
          print(f"Congrats! You won {wager} doubloons")
          doubloons[0] += wager
     global choice
     choice = check_win(choice)
     playagain = "n"
     if choice != "User_Won" and choice != "User_Lost":
        playagain = str(input("Would you like to play again? (y/n): "))
     return playagain

def list_shop():
    print("----- Ship Encounter Rules -----")
    print("You can buy up to 3 ships. Each ship")
    print("responds to a certain encounter. Make")
    print("sure that the ship is in your fleet")
    print("or else you will be punished!")
    global choice
    choice = check_win(choice)
    print("-" * 10, " Hire Fleet ", "-" * 10)
    print(f"Doubloons: {doubloons[0]} | Reputation {reputations[0]}")
    print()
    print("Ships for hire:\t\tcost\trep")
    print("1. Sloop\t\t2\t4")
    print("2. Brigantine\t\t3\t6")
    print("3. Frigate\t\t4\t8")
    print("4. Galleon\t\t5\t10")
    print("5. Man-o'-War\t\t6\t12")
    shipnum = int(input("Hire how many ships? (1-3): "))
    if shipnum > 3 or shipnum < 1:
        print("Please enter a valid option.")
        return list_shop()
    return shipnum, choice

def get_ships(shipnum):
    ship2 = "2null" #good bug fix here, ships both equaled null so if you bought one ship it'd break since ship2 == ship3
    ship3 = "3null"
    ship1 = int(input("Ship 1: "))
    if shipnum > 2:
        ship2 = int(input("Ship 2: "))
        ship3 = int(input("Ship 3: "))
    elif shipnum > 1:
        ship2 = int(input("Ship 2: "))
    if ship1 == ship2 or ship2 == ship3 or ship1 == ship3:
        print("You can only hire one ship per excursion!")
        return get_ships(shipnum)
    cost = ship1 + 1
    if ship2 != "2null":
        cost += ship2 + 1
    if ship3 != "3null":
        cost += ship3 + 1
    if cost > doubloons[0]:
        print("You don't have enough doubloons for these ships!")
        return get_ships(shipnum)
    return ship1, ship2, ship3


def ship_index(ship1, ship2, ship3):
    match ship1:
        case 1:
            ship1 = "Sloop"
            doubloons[0] -= 2
        case 2:
            ship1 = "Brigantine"
            doubloons[0] -= 3
        case 3:
            ship1 =  "Frigate"
            doubloons[0] -= 4
        case 4:
            ship1 = "Galleon"
            doubloons[0] -= 5
        case 5:
            ship1 =  "Man-o'-War"
            doubloons[0] -= 6
    match ship2:
        case 1:
            ship2 = "Sloop"
            doubloons[0] -= 2
        case 2:
            ship2 = "Brigantine"
            doubloons[0] -= 3
        case 3:
            ship2 = "Frigate"
            doubloons[0] -= 4
        case 4:
            ship2 = "Galleon"
            doubloons[0] -= 5
        case 5:
            ship2 = "Man-o'-War"
            doubloons[0] -= 6
    match ship3:
        case 1:
            ship3 = "Sloop"
            doubloons[0] -= 2
        case 2:
            ship3 = "Brigantine"
            doubloons[0] -= 3
        case 3:
            ship3 = "Frigate"
            doubloons[0] -= 4
        case 4:
            ship3 = "Galleon"
            doubloons[0] -= 5
        case 5:
            ship3 = "Man-o'-War"
            doubloons[0] -= 6
    print(f"You bought a {ship1}", end="")
    if ship3 != "3null":
            print(f", {ship2}, and {ship3}!")
    elif ship2 != "2null":
            print(f" and {ship2}!")
    print()
    return ship1, ship2, ship3

def encounter(ship1, ship2, ship3):
    encounter_event = random.randint(1, 5)
    # 1: Merchant Convoy
    # 2: Naval Patrol
    # 3: Cursed Fog
    # 4: Rival Armada
    # 5: The Kraken
    if encounter_event == 1:
        time.sleep(0.5)
        print("The lookout cries out...Merchant Convoy!")
        if ship1 == "Sloop" or ship2 == "Sloop" or ship3 == "Sloop":
            print("Your Sloop answers the call.")
            print("+4 reputation")
            reputations[0] += 4
            time.sleep(1)
        else:
            print("Make sure you have a sloop prepared next time...")
    if encounter_event == 2:
        time.sleep(0.5)
        print("The lookout cries out... Naval Patrol!")
        if ship1 == "Brigantine" or ship2 == "Brigantine" or ship3 == "Brigantine":
            print("Your Brigantine answers the call.")
            print("+6 reputation")
            reputations[0] += 6
            time.sleep(1)
        else:
            print("If only there was a Brigantine in your fleet.")
            print("-3 doubloons")
            doubloons[0] -= 3
            time.sleep(1)
    if encounter_event == 3:
        print("The lookout cries out... Cursed Fog!")
        if ship1 == "Frigate" or ship2 == "Frigate" or ship3 == "Frigate":
            print("Your Frigate answers the call.")
            print("+8 reputation")
            reputations[0] += 8
            time.sleep(1)
        else:
            print("Bring a Frigate next time.")
            coin_flip = random.randint(1, 2)
            if coin_flip == 1:
                print("You're let off easy.")
                time.sleep(0.5)
                print("+5 reputation")
                reputations[0] += 5
            if coin_flip == 2:
                print("-5 reputation")
                reputations[0] -= 5
        time.sleep(1)
    if encounter_event == 4:
        print("The lookout cries out... Rival Armada!")
        if ship1 == "Galleon" or ship2 == "Galleon" or ship3 == "Galleon":
            print("Your Galleon answers the call.")
            print("+10 reputation")
            reputations[0] += 10
        else:
            print("Bring a Galleon with your fleet next time.")
            print("-5 reputation")
            reputations[0] -= 5
    if encounter_event == 5:
        print("The lookout cries out... Kraken!")
        if ship1 == "Man-o'-War" or ship2 == "Man-o'-War" or ship3 == "Man-o'-War":
            print()
            print("+12 reputation")
            reputations[0] += 12
        else:
            print("You need a Man-o'-War to defeat the kraken.")
            time.sleep(0.3)
            print("Your fleet is dragged over, you lost all your doubloons")
            doubloons[0] = 0
        time.sleep(1)
    if reputations[0] < 0:
        reputations[0] = 0
    return

def post_encounter():
    print(f"You have {reputations[0]} reputation and {doubloons[0]} doubloons")
    if doubloons[0] <= 0:
        print("You lost! Try again next time")
        return
    elif reputations[0] >= 30:
        print("Congrats, you won the game!")
    else:
        return #<--- add a way to route back to menu

#main
doubloons = [0]
reputations = [0]
doubloons[0] = 12
reputations[0] = 0
choice = 0
while choice != 3 and choice != "User_Lost" and choice != "User_Won": #good thing for bug fix: set "or" which doesn twork with !=
    choice = main_menu_gui()                                           #Had to make it "and" instead.
    if choice == 1:
        usertotal, wager, bust = user_roll()
        enemytotal = enemy_roll(bust)
        playagain = who_wins(wager, bust, usertotal, enemytotal)
        while playagain == "y":
            if choice != "User_Lost" and choice != "User_Won":
                print(f"You have {doubloons[0]} doubloons and {reputations[0]} reputation.")
                usertotal, wager, bust = user_roll()
                enemytotal = enemy_roll(bust)
                playagain = who_wins(wager, bust, usertotal, enemytotal)
    elif choice == 2:
        choice = check_win(choice)
        shipnum, choice = list_shop()
        ship1, ship2, ship3 = get_ships(shipnum)
        ship1, ship2, ship3 = ship_index(ship1, ship2, ship3)
        encounter(ship1, ship2, ship3)
        post_encounter()
    elif choice == 3:
        pass
    else:
        print("Please input a valid menu choice")
        main_menu_gui()

    #good example of a problem; originally didnt have stuff outside the
    #while loop, so i had to add it to not just run thru the programs
    #nvm still broken

    # ADD A WAY TO USE. Check top of userroll. Add af unction to see if the user loses/wins at any point and put it at
    # the top of every functions.
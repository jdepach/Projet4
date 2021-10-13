from os.path import isfile

import model_chess as mc
from os.path import isfile
import csv

menu = "MENU PRINCIPAL \n Pour ajouter des joueurs tapez 1\n Pour lancer un tournois tapez 2\n " \
       "Pour tester preremplir les joueurs tapez 3\n"
answer = input(menu)

if answer == "3" and isfile("players.csv"):

    with open("players.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            players = [row[0], row[1], row[2], row[3], row[4]]
            print(players)
            abstract = mc.player(family_name=players[0], name=players[1], birthday=players[2],
                      gender=players[3], ranking=players[4])
            # mc.player.set_family_name = players[0]
            # mc.player.set_name = players[1]
            # mc.player.set_birthday = players[2]
            # mc.player.set_gender = players[3]
            # mc.player.set_ranking = players[4]

            output = 'family name:%s, name:%s, birthday:%s, gender:%s, ranking:%s' % (
                abstract.family_name, abstract.name, abstract.birthday, abstract.gender, abstract.ranking)
            print(output)

    # temp = dir(player)
    # for item in temp:
    #     print(item, ' : ', temp[item])

else:
    if answer == "1":
        a = input("prenom : ")
        mc.player.input_name = a
        player = mc.player()
        print(player.name)


    elif answer == "2":
        print("let's go")

# menu
# add_players
# print_rapport
# participants_list
# alpha_order
# ranking_order
# players_list
# alpha_order
# ranking_order
# tournament_list
# round/tournament_list
# match/tournament_list
# new_tournament
# modifed_player

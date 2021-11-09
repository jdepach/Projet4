import model_chess as mc
import time

# swiss system for 8 players :
    # round1
        # rank player with global ranking
        # match1 = p1 vs p5 ; match2 = p2 vs p6 ; match3 = p3 vs p7 ; match4 = p4 vs p8
    # round2
        # rank player with instant ranking
        # if p1 vs p2 = false:
            # match1 = p1 vs p2
        # elif p1 vs p3
            #match1
    # round3
    # round4

def set_players():
    """ajout des joueurs à la main, nombre variable"""
    joueur = list()
    i = 1
    test = True

    while test:
        try:
            number_players = int(input("Combien de joueurs sur ce tournois ? : "))
        except ValueError:
            print("veuiller entrer un nombre entier positif")
        else:
            while i <= number_players :
                print(f"\nEntrer P{i} \n")
                joueur_tmp = mc.Player(
                    family_name=input("Nom de famille : "), name=input("Prenom : "),
                    birthday=input("Date de naissance : "), gender=input("Genre : "), ranking=input("Classement : ")
                    )
                joueur.append(joueur_tmp)
                i += 1
    print("\njoueurs inscrit :")
    for index in range(len(joueur)):
        print("\n"+joueur[index].family_name+" "+joueur[index].name+"\n")

    return joueur


def lecture_csv():
    """ajout des joueurs de manière automatique pour tester le programme"""
    with open("players.csv", "r") as fh:
        players = []
        for row in fh:
            row = row.strip().split(", ")
            players.append((row[0], row[1], row[2], row[3], row[4]))
    joueur = []  # liste d'objets

    for i in range(8):
        joueur_tmp = mc.Player(family_name=players[i][0], name=players[i][1], birthday=players[i][2],
                               gender=players[i][3], ranking=players[i][4])
        joueur.append(joueur_tmp)
        #print(f"P{i+1} " + joueur[i].name + " " + joueur[i].family_name)

    return joueur

def new_rank(round):
    """classe les joueurs d'après leur resultats au tournois actuel"""
    new_rank = []
    final_rank = []

    for i in range(4):
        new_rank.append((round[i][0][0], round[i][0][1], int(round[i][0][0].ranking)))
        new_rank.append((round[i][1][0], round[i][1][1], int(round[i][1][0].ranking)))

    #classement calculé en fonction du nombre de point total et du classement
    final_rank = sorted(new_rank, key=lambda rank: (-1*rank[1], rank[2]))

    return final_rank

def set_tournament():
    """lancement d'un nouveau tournois"""
    joueurs = []
    rounds = []
    print("\ntournois d'echecs en quatre rounds. Veuillez renseigner les informations\n")

    #version auto remplie du tournois
    tournament = mc.Tournament(
        name="tournois test", place="Scadrial", date="01/01/1789",
        time_type=1,
        description="ceci est un test", players_involved=joueurs, rounds=rounds)

    #version manuelle
    # tournament = mc.Tournament(
    #     name=input("nom du tournois : "), place=input("lieu : "), date=input("date : "),
    #     time_type=input(
    #         "selectionnez un type de match \n tapez 1 pour quick chess\n tapez 2 pour blitz \n tapez 3 pour bullet \n"),
    #     description=input("remarques generales : "), number_of_round=4, players_involved=joueurs, round=None)

    print(f"Name = {tournament.name}\nPlace = {tournament.place}\nDate = {tournament.date}\n"
          f"Time type = {tournament.time_type}\nDescription = {tournament.description}\n")

    auto_file = input("\njoueurs manuels tapez 1\njoueurs auto tapez 2\n")

    #round 1

    if auto_file == "1":
        set_players()

        #pas fini, voir le mode auto
        for elt in set_players():
            joueurs.append(elt)

        ranking_not_ranked = []

        # for player in joueurs:
        #     ranking_not_ranked.append(joueurs.ranking)

        rank = sorted(ranking_not_ranked)
        print(rank)
        #rank_round1 = {"P1":, "P2":}

    elif auto_file == "2":
        ranking_not_ranked = []
        for elt in lecture_csv():
            joueurs.append(elt)

        for i in range(8):
            print(f"les joueurs sont : P{i+1} " + joueurs[i].name + " " + joueurs[i].family_name)

        for i in range(8):
            rank = (joueurs[i], joueurs[i].ranking)
            ranking_not_ranked.append(rank)

        final_rank = sorted(ranking_not_ranked, key=lambda sc: sc[1])

        round1 = []
        match1 = ([final_rank[0][0]], [final_rank[1][0]])
        match2 = ([final_rank[2][0]], [final_rank[3][0]])
        match3 = ([final_rank[4][0]], [final_rank[5][0]])
        match4 = ([final_rank[6][0]], [final_rank[7][0]])
        round1.append(match1)
        round1.append(match2)
        round1.append(match3)
        round1.append(match4)

        print(f"match 1 : {final_rank[0][0].name} {final_rank[0][0].family_name}/"
              f" {final_rank[1][0].name} {final_rank[1][0].family_name}")
        print(f"match 2 : {final_rank[2][0].name} {final_rank[2][0].family_name}/"
              f" {final_rank[3][0].name} {final_rank[3][0].family_name}")
        print(f"match 3 : {final_rank[4][0].name} {final_rank[4][0].family_name}/"
              f" {final_rank[5][0].name} {final_rank[5][0].family_name}")
        print(f"match 4 : {final_rank[6][0].name} {final_rank[6][0].family_name}/"
              f" {final_rank[7][0].name} {final_rank[7][0].family_name}")

        round1.append(f"Début du round : {time.ctime()}")

        # dictionnaire de rencontre des joueurs entre eux
        versus = {}
        for i in range(len(joueurs)):
            if (i % 2) == 0:
                versus[final_rank[i][0]] = []
                versus[final_rank[i][0]].append(final_rank[i + 1][0])
            else:
                versus[final_rank[i][0]] = []
                versus[final_rank[i][0]].append(final_rank[i - 1][0])

        print("veuillez entrer les scores")

        # #version auto
        print("[AUTO]")
        #joueur1
        round1[0][0].append(0)
        #joueur2
        round1[0][1].append(1)
        # joueur3
        round1[1][0].append(0)
        # joueur4
        round1[1][1].append(1)
        # joueur5
        round1[2][0].append(0)
        # joueur6
        round1[2][1].append(1)
        # joueur7
        round1[3][0].append(0)
        # joueur8
        round1[3][1].append(1)

        # #version manuelle

        round1.append(f"Fin du round : {time.ctime()}")
        print(round1)
            # #joueur1
            # score_tmp = int(input(f"{final_rank[0][0].name} {final_rank[0][0].family_name} : "))
            # match1[0].append(score_tmp)
            # #joueur2
            # score_tmp = int(input(f"{final_rank[1][0].name} {final_rank[1][0].family_name} : "))
            # match1[1].append(score_tmp)
            # # joueur3
            # score_tmp = int(input(f"{final_rank[2][0].name} {final_rank[2][0].family_name} : "))
            # match2[0].append(score_tmp)
            # # joueur4
            # score_tmp = int(input(f"{final_rank[3][0].name} {final_rank[3][0].family_name} : "))
            # match2[1].append(score_tmp)
            # # joueur5
            # score_tmp = int(input(f"{final_rank[4][0].name} {final_rank[4][0].family_name} : "))
            # match3[0].append(score_tmp)
            # # joueur6
            # score_tmp = int(input(f"{final_rank[5][0].name} {final_rank[5][0].family_name} : "))
            # match3[1].append(score_tmp)
            # # joueur7
            # score_tmp = int(input(f"{final_rank[6][0].name} {final_rank[6][0].family_name} : "))
            # match4[0].append(score_tmp)
            # # joueur8
            # score_tmp = int(input(f"{final_rank[7][0].name} {final_rank[7][0].family_name} : "))
            # match4[1].append(score_tmp)
        print(round1)
        rounds.append(round1)

        ######round2#######
        new_rank(round1)

        id = []
        for i in range(len(joueurs)):
            id.append(new_rank(round1)[i][0])

        print(id)

        print("\nclassement à l'issue du premier tour : ")
        for i in range(len(joueurs)):
            print(f"{i + 1}  {new_rank(round1)[i][0].name} {new_rank(round1)[i][0].family_name}")

        round2 = []

        i = 0
        for item in id:
            if i + 1 < 8 and id[i + 1] not in versus[id[i]] and id[i] not in versus[id[i + 1]]:
                match_tmp = ([id[i]], [id[i + 1]])
                versus[id[i]].append(id[i + 1])
                versus[id[i + 1]].append(id[i])
                id.append(id.pop(id.index(id[i + 1])))
                round2.append(match_tmp)
                i += 1

            elif i + 2 < 8 and id[i + 2] not in versus[id[i]] and id[i] not in versus[id[i + 2]]:
                match_tmp = ([id[i]], [id[i + 2]])
                versus[id[i]].append(id[i + 2])
                versus[id[i + 2]].append(id[i])
                id.append(id.pop(id.index(id[i + 2])))
                round2.append(match_tmp)
                i += 1

            elif id[i - 1] not in versus[id[i]] and id[i] not in versus[id[i - 1]]:
                match_tmp = ([id[i]], [id[i - 1]])
                versus[id[i]].append(id[i - 1])
                versus[id[i - 1]].append(id[i])
                id.append(id.pop(id.index(id[i - 1])))
                round2.append(match_tmp)
                i += 1
            if i > 3:
                break

        round2.append(f"Début du round : {time.ctime()}")

        print("veuillez entrer les scores")

        # #version auto
        print("[AUTO]")
        # joueur1
        round2[0][0].append(0)
        # joueur2
        round2[0][1].append(1)
        # joueur3
        round2[1][0].append(0)
        # joueur4
        round2[1][1].append(1)
        # joueur5
        round2[2][0].append(0)
        # joueur6
        round2[2][1].append(1)
        # joueur7
        round2[3][0].append(0)
        # joueur8
        round2[3][1].append(1)

        print(round1)
        print("###################")
        print(round2)

        # #version manuelle
        # #joueur1
        # score_tmp = int(input(f"{final_rank[0][0].name} {final_rank[0][0].family_name} : "))
        # match1[0].append(score_tmp)
        # #joueur2
        # score_tmp = int(input(f"{final_rank[1][0].name} {final_rank[1][0].family_name} : "))
        # match1[1].append(score_tmp)
        # # joueur3
        # score_tmp = int(input(f"{final_rank[2][0].name} {final_rank[2][0].family_name} : "))
        # match2[0].append(score_tmp)
        # # joueur4
        # score_tmp = int(input(f"{final_rank[3][0].name} {final_rank[3][0].family_name} : "))
        # match2[1].append(score_tmp)
        # # joueur5
        # score_tmp = int(input(f"{final_rank[4][0].name} {final_rank[4][0].family_name} : "))
        # match3[0].append(score_tmp)
        # # joueur6
        # score_tmp = int(input(f"{final_rank[5][0].name} {final_rank[5][0].family_name} : "))
        # match3[1].append(score_tmp)
        # # joueur7
        # score_tmp = int(input(f"{final_rank[6][0].name} {final_rank[6][0].family_name} : "))
        # match4[0].append(score_tmp)
        # # joueur8
        # score_tmp = int(input(f"{final_rank[7][0].name} {final_rank[7][0].family_name} : "))
        # match4[1].append(score_tmp)

        round2.append(f"Fin du round : {time.ctime()}")
        rounds.append(round2)


        ####### round3 ########
        new_rank(round2)

        





set_tournament()






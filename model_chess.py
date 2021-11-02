from tinydb import TinyDB

class Tournament:
    """ un nouveau tournois comporte des informations entrées à la main par le directeur :
    nom, lieu, date, description, nombre de tours, liste des joueurs, type de partie. Le nom des rounds est fixe,
     il depend du nombre de tours definit en amont"""

    def __init__(self, name, place, date, rounds, players_involved, time_type, description):
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.players_involved = players_involved
        self.time_type = time_type
        self.description = description

    def set_name(self, input_name):
        name = input_name
    def get_name(self):
        return self.name

    def set_place(self, input_place):
        place = input_place
    def get_place(self):
        return self.place

    def set_date(self, input_date):
        date = input_date
    def get_date(self):
        return self.date

    def set_rounds(self, input_rounds):
        """chaque match du round comporte deux liste contenant une instance
        de joueur et un champs de resultat. soit ([player, result], [player, result])
        le round est rempli a la main quand il est terminé"""

        rounds = input_rounds
    def get_rounds(self):
        return self.rounds

    def set_players_involved(self, list_players_involved):
        """les joueurs impliqués sur le tournois sont entrés à la main et stockés dans une liste"""
        players_involved = list_players_involved
    def get_players_involved(self):
        return self.players_involved

    def set_time_type(self, input_time_type):
        """ types de matchs possibles sur ces tournois :
        quick chess : partie de 30 minutes max
        blitz : parties de 10 minutes max
        bullet : parties de 3 minutes max"""

        if input_time_type == "1":
            self.time_type = "quick chess"
        elif input_time_type == "2":
            self.time_type = "blitz"
        elif input_time_type == "3":
            self.time_type = "bullet"
    def get_time_type(self):
        return self.time_type

    def set_description(self, input_description):
        description = input_description
    def get_description(self):
        return self.description


class Player:
    def __init__(self, family_name, name, birthday, gender, ranking):
        self.name = name
        self.family_name = family_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking
        self.id = id(self)  # code de chaque joueur

    def set_family_name(self, input_family_name):
        family_name = input_family_name
    def get_family_name(self):
        return self.family_name

    def set_name(input_name):
        name = input_name
    def get_name(self):
        return self.name

    def set_birthday(self, input_birthday):
        birthday = input_birthday
    def get_birthday(self):
        return self.birthday

    def set_gender(self, input_gender):
        gender = input_gender
    def get_gender(self):
        return self.gender

    def set_ranking(self, input_ranking):
        ranking = input_ranking
    def get_ranking(self):
        return self.ranking


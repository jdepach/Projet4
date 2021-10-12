

# class tournament
    # tounament_name
    # place
    # date
    # number_of_round (default = 4)
    # round = [
        #[round1, r1_time_beg, r1_time_end]
        #round2,
        #round3,
        #round4 ]
    # players
    # time_type
        # bullet : 3 min
        # blitz : 10 min
        # quick_chess : 30 min
    # description

class player:
    def __init__(self, family_name, name, birthday, gender, ranking):
        self.name = name
        self.family_name = family_name
        self.birthday = birthday
        self.gender = gender
        self.ranking = ranking
        self.id = id(self) # code de chaque joueur

    def set_name(self, input_name):
        name = input_name
    def set_family_name(input_family_name):
        family_name = input_family_name
    def set_birthday(input_birthday):
        birthday = input_birthday
    def set_gender(input_gender):
        gender = input_gender
    def set_ranking(input_ranking):
        ranking = input_ranking


# round = [match1, match2; match3, match4]
# match = ([player1 ; score_p1], [player2 ; score_p2])



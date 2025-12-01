class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def tie(self):
        return self.player1_score == self.player2_score
    
    def point_difference(self):
        return self.player1_score - self.player2_score
    
    def score_when_tied(self):
        if self.player1_score == 0:
            return "Love-All"
        elif self.player1_score == 1:
            return "Fifteen-All"
        elif self.player1_score == 2:
            return "Thirty-All"
        else:
            return "Deuce"
        
    def advantage_or_win(self):
        return self.player1_score >= 4 or self.player2_score >= 4
        
    def score_when_advantage_or_win(self):
        if self.point_difference() == 1:
            return "Advantage player1"
        elif self.point_difference() == -1:
            return "Advantage player2"
        elif self.point_difference() >= 2:
            return "Win for player1"
        else:
            return "Win for player2"
        
    def normal_score(self):
        score = ""
        for i in range(1, 3):
            if i == 1:
                temp_score = self.player1_score
            else:
                score = score + "-"
                temp_score = self.player2_score

            score = score + self.term_point(temp_score)
        return score
    
    def term_point(self, value):
        if value == 0:
            return "Love"
        elif value == 1:
            return "Fifteen"
        elif value == 2:
            return "Thirty"
        elif value == 3:
            return "Forty"
        


    def get_score(self):
        if self.tie():
            return self.score_when_tied()

        elif self.advantage_or_win():
            return self.score_when_advantage_or_win()

        else:
            return self.normal_score()


class Card:

    def __init__( self , suit , point_val , string_val ):
        
        self.suit = suit
        self.point_val = point_val
        self.string_val = string_val

    def card_info(self):
        print(f"{self.string_val} of {self.suit} : {self.point_val} points")

# game 1
game_one = Card("negro", "50", "100")
game_one.card_info()
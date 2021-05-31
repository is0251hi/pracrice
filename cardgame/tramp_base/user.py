
import numpy as np


class User:#複数人のオブジェクト生成する
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def give_card(self,card_num):
        temp_card=self.hand.pop(card_num-1)
        return temp_card

    def get_card(self,temp_card):
        self.hand.append(temp_card)
        np.random.shuffle(self.hand)

    def my_hand(self):
        print(self.name+'の手札')
        print(self.hand)
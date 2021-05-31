import numpy as np
import logging


class Card:
    def  __init__(self):
        self.sign_list=['♢','♧','♤','♡']
        self.number_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.joker = 'Joker'
  

class Deck:
    def __init__(self,joker_use=True):
        card=Card()
        self.joker_use=joker_use
        #self.play_user=0
        self.deck_list=[]
        self.hand_list=[]
        self.deck_list=self.make_deck(card)

    def make_deck(self,card):
        #self.deck_list.append(card.number_list)
        for sign in card.sign_list:
            for number in card.number_list:
                self.deck_list.append([sign,number])#この形はいける？
        
        if self.joker_use==True:
            self.deck_list.append([card.joker,0])
        np.random.shuffle(self.deck_list)
        return self.deck_list


    def distribute_first_hand(self,play_user):
        #play_user(数値)に分割
        hand_num = int((len(self.deck_list))/play_user)#ここでselfいる?→いらんselfはオブジェクト化した際、インスタンスが引数として渡されルガこのとき必要な変数のみで良い
        hand_remain = int((len(self.deck_list))%play_user)
        k=0
        for _ in range(play_user):
            hand=self.deck_list[k:k+hand_num]
            if hand_remain>0:
                hand.append(self.deck_list[k+hand_num])
                hand_remain-=1
                k+=1
            k+=hand_num
            self.hand_list.append(hand)
        logging.info(len(self.hand_list[0])+len(self.hand_list[1])+len(self.hand_list[2]))
        return self.hand_list#これいらん説


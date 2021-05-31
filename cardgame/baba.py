import numpy as np
import logging

from tramp_base import card,user,base_deco

logging.basicConfig(level=logging.INFO)

class baba_User(user.User):#複数人のオブジェクト生成する
    def get_card(self,temp_card):
        pair_flag=True
        for idx,one_card in enumerate(self.hand):
            if one_card[1]==temp_card[1]:
                pair_flag=False
                self.hand[idx].pop#合ってる？
                break
        np.random.shuffle(self.hand)
        if pair_flag:
            self.hand.append(temp_card)
        logging.info(self.hand)

    def check_pair_hand(self):#初手の作業
        trash=[]
        leave_card=[]
        num_list=[one_card[1] for one_card in self.hand]
        for idx,num in enumerate(num_list):
            if num_list.count(num)%2==0:
                trash.append(self.hand[idx])
                self.hand[idx]=[0,0]
            elif num_list.count(num)==3:#koko
                if num in leave_card:
                    trash.append(self.hand[idx])
                    self.hand[idx]=[0,0]
                else:
                    leave_card.append(num)#?
        self.hand=[one_card for one_card in self.hand if one_card!=[0,0]]
        logging.info(self.name)
        logging.debug(trash)
        logging.info(self.hand)
        

class Game:
    def __init__(self,config):
        self.play_user=config.play_user#ここは複数ゲーム作らないので、普通の変数でもいいかも
        self.name_list=config.name_list
        self.user_list=[]
        self.finish_user=[]
    
    def start(self):#この最後にそれぞれの手札のチェックと捨てる作業が必要
        deck=card.Deck(joker_use=True)
        hand_list=deck.distribute_first_hand(self.play_user)
        for idx in range(self.play_user):
            user=baba_User(name=self.name_list[idx],hand=hand_list[idx])
            user.check_pair_hand()
            self.user_list.append(user)

    def next(self,player_idx):#idxがidx+1の人のカードを引く(idx=2の場合、idx=0から引く)
        logging.info(f'{self.name_list[player_idx]}のターン')
        if player_idx==self.play_user:
            hand_num=self.user_list[0].my_hand()
            card_num=Interface.input_take_card(hand_num)
            temp_card=self.user_list[0].give_card(card_num)
        else:
            hand_num=self.user_list[player_idx+1].my_hand()#user_listに値入っているか
            card_num=Interface.input_take_card(hand_num)
            temp_card=self.user_list[player_idx+1].give_card(card_num)
        
        self.user_list[player_idx].get_card(temp_card)
        
    def finish(self):#結果発表,最後の一人格納
        self.finish_user.append(self.name_list[0])
        for idx,u in enumerate(self.finish_user):
            print(f'{idx+1}位：{u}')

    def check(self):#ユーザーの手札
        for idx,u in enumerate(self.user_list):
            if len(u.hand)==0:#player_userとuser_list、name_listの削除
                self.play_user-=1
                self.finish_user.append(self.name_list[idx])
                self.user_list[idx]=0
                self.name_list[idx]=0
        self.user_list=[u for u in self.user_list if u!=0]
        self.name_list=[n for n in self.name_list if n!=0]



class Config:#初期値設定などここで決める説,Interfaceからいじる
    def __init__(self,play_user,name_list):
        self.play_user=play_user
        self.name_list=name_list


class Interface():#入力用←これいる？
    @staticmethod
    def input_config():
        name_list=[]
        print('何名でプレイしますか？')
        play_user=int(input())#player_numは配列のidx
        for idx in range(play_user):
            print(str(idx+1)+'人目の名前を入力してください：')
            name=input()
            name_list.append(name)
            
        config=Config(play_user,name_list)
        return config

    @staticmethod
    def input_take_card(hand_num):
        print('何枚目のカードを取得しますか？：')
        try:
            card_num=int(input())
            if card_num>=hand_num or card_num<=0:
                raise ValueError
        except ValueError:
            print('1~'+str(hand_num)+'の間で入力してください')
        except TypeError:
            print('数値を入力してください')

        return card_num+1

if __name__ == '__main__':#とりあえずターミナル上で動かす
    deco=base_deco.Decorator()
    player_idx=0
    config=Interface.input_config()
    game=Game(config)
    game.start()
    logging.info(f'game.play_user:{game.play_user}')
    while(game.play_user!=1):
        if player_idx==game.play_user:
            player_idx=0
        logging.info('next')
        game.next(player_idx)
        player_idx+=1
        game.check()
    game.finish()
        
    

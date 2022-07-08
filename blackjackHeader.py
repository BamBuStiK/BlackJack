import random
class bk:
    def __init__(self):
        self.playerIn = True#player가 들어옴
        self.dealerIn = True#dealer가 들어옴
        self.deck=[2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        'J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A']
        self.playerHand=[]
        self.dealerHand=[]

#deal the cards
    def dealCard(self, turn):
        card = random.choice(self.deck)
        turn.append(card)#player랑 dealer 번갈아가면서 카드 한장을 deck에서 가져온다
        self.deck.remove(card)#deck에서 그 카드를 제거한다.
#player랑 dealer 손에 있는 카드들을 계산한다
    def total(self, turn):
    #얼굴 있는 카드들은 값을 다르게 쳐야한다, ace=10, ace(bust)=1 등등
        total = 0
        face = ['J','K','Q']#ace는 1 아니면 11일수도 있기 때문에 제외시켰다.(1)
        for card in turn:
            if card in range(1,11):#1~10
                total+=card
            elif card in face:#facecards
                total+=10
            else:#(1)ace는 특별하게 처리
                if total > 11:#bust
                    total+=1
                else:#ace
                    total+=11
        return total
#승자를 결정한다
#give dealer some intelligence
    def revealDealerHand(self):
        if len(self.dealerHand)==2:
            return self.dealerHand[0]
        elif len(self.dealerHand)>2:
            return self.dealerHand[0], self.dealerHand[1]
    
    def check_bust(self, hand):
        total = self.total(hand)
        if total > 21:
            return True
        return False

    def discriminate(self):
        if self.check_bust(self.playerHand):
            print("player bust")
            return 0
        elif self.check_bust(self.dealerHand):
            print("dealer bust")
            return 1
        elif self.check_bust(self.playerHand) and self.check_bust(self.dealerHand):
            print("draw")
            return 2
        else:
            if self.total(self.playerHand) > self.total(self.dealerHand):
                print("player win")
                return 3
            elif self.total(self.playerHand) < self.total(self.dealerHand):
                print("player lose")
                return 4
            elif self.total(self.playerHand) == self.total(self.dealerHand):
                print("draw")
                return 5

    def refill_deck(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6,
                     7, 8, 9, 10,
                     'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
        self.playerHand = []
        self.dealerHand = []
        # if self.dealerHand:
        #     for i in range(len(self.dealerHand)):
        #         tem = self.dealerHand[i]
        #         self.deck.append(tem)
        #         self.dealerHand.remove(tem)
        # if self.playerHand:
        #     for i in range(len(self.playerHand)):
        #         tem = self.playerHand[i]
        #         self.deck.append(tem)
        #         self.playerHand.remove(tem)
        print("refill deck")


import random
class bk:
    def __init__(self):
        playerIn = True#player가 들어옴
        dealerIn = True#dealer가 들어옴
        deck=[2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        'J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A']
        playerHand=[]
        dealerHand=[] 

#deal the cards
    def dealCard(turn):
        card = random.choice(__init__.deck)
        turn.append(card)#player랑 dealer 번갈아가면서 카드 한장을 deck에서 가져온다
        __init__.deck.remove(card)#deck에서 그 카드를 제거한다.
#player랑 dealer 손에 있는 카드들을 계산한다
    def total(turn):
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
    def revealDealerHand():
        if len(__init__.dealerHand)==2:
            return __init__.dealerHand[0]
        elif len(__init__.dealerHand)>2:
            return __init__.dealerHand[0],__init__.dealerHand[1]
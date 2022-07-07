import random
playerIn = True#player가 들어옴
dealerIn = True#dealer가 들어옴
#deck, player hand, dealer hand
deck=[2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        'J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A','J', 'Q', 'K', 'A']
playerHand=[]
dealerHand=[]
#deal the cards
def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)#player랑 dealer 번갈아가면서 카드 한장을 deck에서 가져온다
    deck.remove(card)#deck에서 그 카드를 제거한다.

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
    if len(dealerHand)==2:
        return dealerHand[0]
    elif len(dealerHand)>2:
        return dealerHand[0],dealerHand[1]

#게임 반복 루프시킨다
for _ in range(2):#_는 컴퓨터가 코드 컴파일할때 메모리를 조금 절약시켜준다
    dealCard(dealerHand)
    dealCard(playerHand)
#손에 카드가 제대로 들어갔는지 확인 용도
#print(dealerHand)
#print(playerHand)
while playerIn or dealerIn:#player랑 dealer가 들어와있다면
    print(f"Dealer에게는 {revealDealerHand()}와 x")
    print(f"당신은 {playerHand}를 가지고 있으며 전체 {total(playerHand)}이다.")
    if playerIn:#player input
        stayOrHit=input("1: Stay\n2: Hit\n")#string으로 input
    if total(dealerHand)>16:#dealer가 deck에서 하나 가져갈지 말지 결정
        dealerIn=False#dealer stay
    else:#dealer 손이 16보다 작다면 deck에서 카드 하나 가져간다
        dealCard(dealerHand)#deck에서 하나 가져간다

    if stayOrHit=='1':#player가 1을 입력(stay)
        playerIn==False
    else:#player가 2을 입력(hit)
        dealCard(playerHand)#player가 deck에서 카드하나 가져간다.
    #승자 결정, player, dealer 중 누가 21이거나 넘어가면 루프에서 나간다
    if total(playerHand)>=21:
        break
    elif total(dealerHand)>=21:
        break
#--------------------------------------------------------------------------
#승자를 결정한다.
if total(playerHand)==21:
    print(f"\n당신은 {playerHand}으로 21 달성했고 dealer는 {total(playerHand)}로 총 {total(dealerHand)}을 달성했다.")
    print("BLACKJACK")
elif total(dealerHand)==21:
    print(f"\n당신은 {playerHand}으로 21 달성했고 dealer는 {total(playerHand)}로 총 {total(dealerHand)}을 달성했다.")
    print("Dealer Wins")
elif total(playerHand)>21:
    print(f"\n당신은 {playerHand}으로 21 달성했고 dealer는 {total(playerHand)}로 총 {total(dealerHand)}을 달성했다.")
    print("Player Bust")
elif total(dealerHand)>21:
    print(f"\n당신은 {playerHand}으로 21 달성했고 dealer는 {total(playerHand)}로 총 {total(dealerHand)}을 달성했다.")
    print("Dealer BUst")
#player랑 dealer 둘다 자리에 남는다면(stay), 21에 가장 가까운 사람이 승자가 된다.
elif 21 - total(dealerHand) < 21-total(playerHand):
    print(f"\n당신은 {playerHand}으로 21 달성했고 dealer는 {total(playerHand)}로 총 {total(dealerHand)}을 달성했다.")
    print("Dealer Wins")
elif 21 - total(dealerHand) > 21 - total(playerHand):
    print(f"\n당신은 {playerHand}으로 21 달성했고 dealer는 {total(playerHand)}로 총 {total(dealerHand)}을 달성했다.")
    print("You win")

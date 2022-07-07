import random
import blackjackHeader

#게임 반복 루프시킨다
for _ in range(2):#_는 컴퓨터가 코드 컴파일할때 메모리를 조금 절약시켜준다
    bk.dealCard(bk.dealerHand)
    bk.dealCard(bk.playerHand)
#손에 카드가 제대로 들어갔는지 확인 용도
#print(dealerHand)
#print(playerHand)
while bk.playerIn or dealerIn:#player랑 dealer가 들어와있다면
    print(f"Dealer에게는 {revealDealerHand()}와 x")
    print(f"당신은 {bk.playerHand}를 가지고 있으며 전체 {total(bk.playerHand)}이다.")
    if playerIn:#player input
        stayOrHit=input("1: Stay\n2: Hit\n3: Surrender\n")#string으로 input
    if total(bk.dealerHand)>16:#dealer가 deck에서 하나 가져갈지 말지 결정
        dealerIn=False#dealer stay
    else:#dealer 손이 16보다 작다면 deck에서 카드 하나 가져간다
        dealCard(bk.dealerHand)#deck에서 하나 가져간다

    if stayOrHit=='1':#player가 1을 입력(stay)
        playerIn==False
    elif stayOrHit=='2':#player가 2을 입력(hit)
        dealCard(bk.playerHand)#player가 deck에서 카드하나 가져간다.
    else:#surrender
        break
    #승자 결정, player, dealer 중 누가 21이거나 넘어가면 루프에서 나간다
    if total(bk.playerHand)>=21:
        break
    elif total(bk.dealerHand)>=21:
        break
#--------------------------------------------------------------------------
#승자를 결정한다.
if total(bk.playerHand)==21:
    print(f"\n당신은 {bk.playerHand}으로 21 달성했고 dealer는 {total(bk,playerHand)}로 총 {total(dealerHand)}을 달성했다.")
    print("BLACKJACK")
elif total(dealerHand)==21:
    print(f"\n당신은 {bk.playerHand}으로 21 달성했고 dealer는 {total(bk.playerHand)}로 총 {total(bk.dealerHand)}을 달성했다.")
    print("Dealer Wins")
elif total(playerHand)>21:
    print(f"\n당신은 {bk.playerHand}으로 21 달성했고 dealer는 {total(bk.playerHand)}로 총 {total(bk.dealerHand)}을 달성했다.")
    print("Player Bust")
elif (total(bk.dealerHand)>21) and (stayOrHit=='3'):
    print(f"포기")
elif (total(bk.dealerHand)>21) and (stayOrHit!='3'):
    print(f"\n당신은 {bk.playerHand}으로 21 달성했고 dealer는 {total(bk.playerHand)}로 총 {total(dealerHand)}을 달성했다.")
    print("Dealer Bust")
#player랑 dealer 둘다 자리에 남는다면(stay), 21에 가장 가까운 사람이 승자가 된다.
elif (21 - total(bk.dealerHand) < 21-total(bk.playerHand)) and (stayOrHit=='3'):#surrender
    print(f"당신은 포기했습니다. Dealer 승!")
elif 21 - total(bk.dealerHand) > 21 - total(bk.playerHand):
    print(f"\n당신은 {bk.playerHand}으로 21 달성했고 dealer는 {total(bk.playerHand)}로 총 {total(bk.dealerHand)}을 달성했다.")
    print("You win")
else:
    print(f"\n당신은 {bk.playerHand}으로 21 달성했고 dealer는 {total(bk.playerHand)}로 총 {total(bk.dealerHand)}을 달성했다.")
    print("Dealer Wins")
#renew deck in deck
for i in range(0, len(renewDeck)):
    bk.deck[i]=renewDeck[i]

class Bet_System: #커다란 베팅판. 베팅된 돈을 모아 두고, 승리한 쪽에 돈을 배분한다.
    def __init__(self, money=1000):
        self.game_money = 0 #베팅된 금액.
        self.pocket_money = money #플레이어 보유금액


    def bet_money(self): #베팅하기 기능.
        while True:
            amount = int(input("베팅 금액을 입력하세요: "))
            
            if self.pocket_money == 0:
                print("돈을 탕진했습니다! 금액을 충전하세요.")
                break
                
            elif amount > self.pocket_money:
                print("돈이 모자랍니다! 금액을 다시 입력해주세요.")

            else:
                self.pocket_money -= amount
                self.game_money += amount #플레이어가 베팅한 금액을 베팅시스템 게임머니에 저장.
                print("game_money: ${} pocket_money: ${}".format(amount, self.pocket_money))
                break

    def win_money(self): #승리한 플레이어 지갑에 배당금 추가.
        self.pocket_money += self.game_money + self.game_money #승리시 얻는 금액은 베팅 금액으로 설정했습니다. 베팅했던 금액 + 승리시 얻는 금액.
        print("${} 획득했습니다. pocket_money: ${}".format(self.game_money, self.pocket_money))
        self.game_money = 0 #게임머니 초기화

    def lose_money(self): #베팅액 초기화 및 플레이어가 얼마를 잃었는지 출력해줌.
        print("${} 잃었습니다. pocket_money: ${}".format(self.game_money, self.pocket_money))
        self.game_money = 0

    def draw_money(self):
        self.pocket_money += self.game_money / 2
        print("무승부. 베팅 금액의 절반을 돌려받습니다. pocket_money: ${}".format(self.pocket_money))
        self.game_money = 0




"""딜러와 플레이어만 플레이하기 때문에 플레이어만 베팅을 하는 것으로 설정했습니다. 플레이어 승리 시 얻는 금액은 베팅 금액만큼 얻도록 
설정했고 필요하다면 추후에 카드에 따라 베팅 금액이 달라지는 기능도 넣겠습니다. 추가나 수정이 필요한 기능들이 있다면 말씀해주세요!"""

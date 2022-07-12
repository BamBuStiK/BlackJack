import blackjackHeader
import Betting_System
import time

class Display:
    def Get_line(self): # 선으로 경게를 나타낸다.
        buffer = ""
        for i in range(50):
            buffer += "-"
        print(buffer)

    def setting_d_card(self, stat, d_card):   # 딜러의 카드를 나타낸다.
        buffer1 = ""
        buffer2 = ""
        for i in range(len(d_card)):
            buffer1 += " +-+  "
        print(buffer1)
        if stat == "on":
            for i in range(len(d_card)):
                buffer2 += "| " + str(d_card[i]) + " | "
        elif stat == "off":
            for i in range(len(d_card)):
                if i == 0:
                    buffer2 += "| " + str(d_card[i]) + " | "
                else:
                    buffer2 += "| ? | "
        print(buffer2)
        print(buffer1)

    def setting_p_card(self, p_card):   # 플레이어의 카드를 나타낸다
        buffer1 = ""
        buffer2 = ""
        for i in range(len(p_card)):
            buffer1 += " +-+  "
        print(buffer1)
        for i in range(len(p_card)):
            buffer2 += "| " + str(p_card[i]) + " | "
        print(buffer2)
        print(buffer1)



class Interface(Display):
    def __init__(self):
        self.Bet_sys = Betting_System.Bet_System()
        self.bk = blackjackHeader.bk()
        self.display = Display()
        self.game_stat = 0  # 게임이 진행되고 있는지 확인한다. 0일 때 : 게임 시작 전, 1일 때 : 게임 진행 중

    def re_display(self, stat):   # 현재 진행되고 있는 게임 상황을 나타낸다
        self.display.Get_line()
        print("dealer:")
        self.display.setting_d_card(stat, self.bk.dealerHand)
        self.display.Get_line()
        print("player:")
        self.display.setting_p_card(self.bk.playerHand)
        self.display.Get_line()
        print("game_money: $"+str(self.Bet_sys.game_money))
        self.display.Get_line()
        print("pocket_money: $"+str(int(self.Bet_sys.pocket_money)))
        self.display.Get_line()


    def launch(self):   # 게임이 끝날 때까지 진행한다
        while 1:
            if self.game_stat == 0:
                if self.Bet_sys.pocket_money == 0:
                    print("돈을 탕진했습니다! 금액을 충전하세요.")
                    break
                time.sleep(1)
                self.re_display("off")
                if not self.Bet_sys.bet_money():
                    break

                self.game_stat = 1
                for _ in range(2):  # _는 컴퓨터가 코드 컴파일할때 메모리를 조금 절약시켜준다
                    self.bk.dealCard(self.bk.dealerHand)
                    self.bk.dealCard(self.bk.playerHand)
                # 딜러에게 카드 2장
                # 플레이어에게 카드 2장
            else:
                if self.bk.check_bust(self.bk.playerHand):  # 딜러 혹은 플레이어가 버스트인 경우 : 배팅된 코인을 이긴 사람에게 추가한다
                    self.bk.discriminate()
                    time.sleep(1)
                    self.re_display("on")  # 딜러의 카드를 오픈한 상태로 나타낸다.
                    self.Bet_sys.lose_money()
                    self.bk.refill_deck()
                    self.game_stat = 0
                    continue
                time.sleep(1)
                self.re_display("off")  # 딜러의 카드를 뒤집어 진 상태로 나타낸다.
                print("1. Stay : no more accepting card")
                print("2. Hit : get one card")
                print("3. Surrender : give up the game")
                print("4. Quit : quit the game")
                select = input()
                if select == "1":   # stay
                    time.sleep(1)
                    self.re_display("on")
                    while self.bk.total(self.bk.dealerHand) <= 16:
                        self.bk.dealCard(self.bk.dealerHand)
                        time.sleep(1)
                        self.re_display("on")   # 딜러의 카드를 오픈한 상태로 나타낸다
                        # 딜러에게 카드 1장
                    time.sleep(1)
                    check_result = self.bk.discriminate()
                    if check_result == 0:
                        self.Bet_sys.lose_money()
                    elif check_result == 1:
                        self.Bet_sys.win_money()
                    elif check_result == 2:
                        self.Bet_sys.draw_money()
                    elif check_result == 3:
                        self.Bet_sys.win_money()
                    elif check_result == 4:
                        self.Bet_sys.lose_money()
                    elif check_result == 5:
                        self.Bet_sys.draw_money()
                    self.bk.refill_deck()
                    self.game_stat = 0  # 게임을 다시 시작한다.
                    continue
                elif select == "2":     # hit
                    # 플레이어에게 카드를 1장
                    self.bk.dealCard(self.bk.playerHand)
                    continue
                elif select == "3":     # surrender
                    time.sleep(1)
                    self.re_display("on")   # 딜러의 카드를 오픈한 상태로 나타낸다.
                    self.Bet_sys.lose_money()
                    self.bk.refill_deck()
                    self.game_stat = 0  # 게임을 다시 시작한다.
                    continue
                elif select == "4":
                    break
                else:   # 정해진 명령어 외의 번호가 입력
                    print("you entered an incorrect number")
                    continue

l=Interface()
l.launch()



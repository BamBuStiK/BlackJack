class Display:
    def __init__(self):
        self.d_card = []
        self.p_card = []
        self.b_coin = 0
        self.coin = 100

    def Get_line(self): # 선으로 경게를 나타낸다.
        buffer = ""
        for i in range(50):
            buffer += "-"
        print(buffer)

    def setting_d_card(self, stat):   # 딜러의 카드를 나타낸다.
        buffer1 = ""
        buffer2 = ""
        for i in range(len(self.d_card)):
            buffer1 += " +-+  "
        print(buffer1)
        if stat == "on":
            for i in range(len(self.d_card)):
                buffer2 += "| " + str(self.d_card[i]) + " | "
        elif stat == "off":
            for i in range(len(self.d_card)):
                if i == 0:
                    buffer2 += "| " + str(self.d_card[i]) + " | "
                else:
                    buffer2 += "| ? | "
        print(buffer2)
        print(buffer1)

    def setting_p_card(self):   # 플레이어의 카드를 나타낸다
        buffer1 = ""
        buffer2 = ""
        for i in range(len(self.p_card)):
            buffer1 += " +-+  "
        print(buffer1)
        for i in range(len(self.p_card)):
            buffer2 += "| " + str(self.p_card[i]) + " | "
        print(buffer2)
        print(buffer1)



class Interface:
    def __init__(self):
        self.display = Display()
        self.game_stat = 0  # 게임이 진행되고 있는지 확인한다. 0일 때 : 게임 시작 전, 1일 때 : 게임 진행 중
        self.p_total = 0
        self.d_total = 0

    def re_display(self, stat):   # 현재 진행되고 있는 게임 상황을 나타낸다
        self.display.Get_line()
        print("dealer:")
        self.display.setting_d_card(stat)
        self.display.Get_line()
        print("player:")
        self.display.setting_p_card()
        self.display.Get_line()
        print("Betting Coin: "+str(self.display.b_coin))
        self.display.Get_line()
        print("Coins: "+str(self.display.coin))
        self.display.Get_line()


    def launch(self):   # 게임이 끝날 때까지 진행한다
        while 1:
            if self.game_stat == 0:
                self.p_total = 0
                self.d_total = 0
                self.re_display("off")
                c = input("Betting: ")
                if int(self.display.coin) < int(c) <= 0:
                    print("you don't have enough coin")
                    break
                else:
                    self.display.coin -= int(c)
                    self.display.b_coin += int(c)
                self.game_stat = 1
                # 딜러에게 카드 2장
                # d_total에 카드2장의 값을 더한다
                # 플레이어에게 카드 2장
                # p_total에 카드2장의 값을 더한다
            else:
                # 딜러 혹은 플레이어가 블랙잭인 경우 : 배팅된 코인을 이긴 사람에게 추가한다
                # 딜러 혹은 플레이어가 버스트인 경우 : 배팅된 코인을 이긴 사람에게 추가한다
                self.re_display("off")  # 딜러의 카드를 뒤집어 진 상태로 나타낸다.
                print("1. Stay : no more accepting card")
                print("2. Hit : get one card")
                print("3. Surrender : give up the game")
                print("4. Quit : quit the game")
                select = input()
                if select == "1":   # stay
                    while self.d_total <= 16:
                        self.re_display("on")   # 딜러의 카드를 오픈한 상태로 나타낸다
                        # 딜러에게 카드 1장
                        # d_total에 카드1장의 값을 더한다
                    if self.p_total > self.d_total:     # player가 이겼을 때
                        print("player win")
                        self.display.coin += self.display.b_coin*2
                        self.display.b_coin = 0
                    elif self.p_total == self.d_total:  # player가 비겼을 때
                        print("draw")
                        self.display.coin += self.display.b_coin/2
                        self.display.b_coin = 0
                    elif self.p_total < self.d_total:   # player가 졌을 때
                        print("player lose")
                        self.display.b_coin = 0
                    self.game_stat = 0  # 게임을 다시 시작한다.
                elif select == "2":     # hit
                    # 플레이어에게 카드를 1장
                    print("")
                elif select == "3":     # surrender
                    self.re_display("on")   # 딜러의 카드를 오픈한 상태로 나타낸다
                    self.display.coin += self.display.b_coin/2
                    self.display.b_coin = 0
                    self.game_stat = 0  # 게임을 다시 시작한다.
                elif select == "4":
                    break
                else:   # 정해진 명령어 외의 번호가 입력
                    print("you entered an incorrect number")
                    continue

l=Interface()
l.launch()



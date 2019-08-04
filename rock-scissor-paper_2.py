import random

def get_player_choice():
   player_choice = input("당신의 선택은?: ")
   while player_choice != "가위" and player_choice != "바위" and player_choice != "보":
      player_choice = input("다시 선택해주세요: ")
   return player_choice

def get_computer_choice():
   example = ('가위', '바위', '보')
   comp = random.randint(0, 2)
   computer_choice = example[comp]

   return computer_choice

def check_who_win(player, computer):
   if player == "가위" and computer == "보" or \
   player == "바위" and computer == "가위" or \
   player == "보" and computer == "바위" :
      return 'player'
   elif player == computer:
      return 'draw'
   else:
      return 'computer'
      
def play():
   while True:
      try:
         what_kind = int(input("1번: 3판2선승제, 2번: 5판 3선승제 >"))
         # 플레이어가 1 혹은 2만 입력하도록
         while what_kind != 1 and what_kind != 2:
            what_kind = int(input("다시 입력해주세요: "))
         break
      except ValueError:
         continue

   # what_kind == 1이면, 3판2선승제 : win_game = 2
   # what_kind == 2이면, 5판3선승제 : win_game = 3
   win_game = 2 if what_kind == 1 else 3

   i = 0
   j = 0
   while i != win_game and j != win_game:
      player = get_player_choice()
      computer = get_computer_choice()
      result = check_who_win(player, computer)
      if result == 'player':
         i += 1
         print("플레이어 승!")
      elif result == 'computer':
         j += 1
         print("컴퓨터 승!")
      else:
         print("무승부")

   if i == win_game:
      print("축하합니다 승리하셨습니다.")
      print(f"플레이어: {i}승, 컴퓨터: {j}승")
   else:
      print("아쉽습니다 패배하셨습니다.")
      print(f"플레이어: {i}승, 컴퓨터: {j}승")

play()

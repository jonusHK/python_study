'''
1번: 3판2선승제, 2번: 5판 3선승제 >2
당신의 선택은?: 가위
컴퓨터 승!
당신의 선택은?: 바위
무승부
당신의 선택은?: 보
컴퓨터 승!
당신의 선택은?: 보
무승부
당신의 선택은?: 보
컴퓨터 승!
아쉽습니다 패배하셨습니다.
플레이어: 0승, 컴퓨터: 3승
'''
from random import randint

def who_winner(player, computer):
    '''
    who_winner(player_choice, computer_choice) -> string
    player_choice : '가위 혹은 바위 혹은 보'
    computer_choice : '가위 혹은 바위 혹은 보
    tell who's winner
    return : player, computer, draw
    '''
    if player == '가위' and computer == '보' or \
    player == '바위' and computer == '가위' or \
    player == '보' and computer == '바위' :
        return 'player'
    elif player == computer:
        return 'draw'
    else:
        return 'computer'

def get_player_choice():
    '''
    get_player_choice() -> string
    return : '가위 or 바위 or 보'
    '''
    while True:
        player = input('가위, 바위, 보 중에 하나를 입력하세요 >')
        while player != '가위' and player != '바위' and player != '보':
            print('가위, 바위, 보 중에 하나를 입력하셔야 합니다.')
            player = input('가위, 바위, 보 중에 하나를 입력하세요 >')
        break
    
    return player

def get_computer_choice():
    '''
    get_computer_choice() -> string
    return : '가위 or 바위 or 보'
    '''
    li = ['가위', '바위', '보']
    computer = randint(0, 2)
    return li[computer]
    
# 유저로부터 3판2선승제과 5판3선승제 중, 원하는 게임 입력
while True: 
    while True:
        try:
            select_num = int(input('1번: 3판2선승제, 2번: 5판3선승제 >'))
            if select_num == 1:
                num = 2
                break
            elif select_num == 2:
                num = 3
                break
            else:
                print('숫자 1과 2 중 하나를 입력하세요. >')
        except ValueError:
            print('숫자 1과 2중 하나를 입력하세요. >')
    break

computer_win = 0
player_win = 0
while computer_win != num and player_win != num:
    player = get_player_choice()
    computer = get_computer_choice()
    if who_winner(player, computer) == 'player':
        player_win += 1
    elif who_winner(player, computer) == 'computer':
        computer_win += 1
    else:.
        continue    

if player_win == 2:
    print('축하합니다 승리하셨습니다.')
else:
    print('아쉽습니다 패배하셨습니다.')

print(f'플레이어: {player_win}승, 컴퓨터: {computer_win}승')

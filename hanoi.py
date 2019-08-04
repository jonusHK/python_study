def move_disk(disk_num, start_peg, end_peg):
    print(f"{disk_num}번 원판을 {start_peg}번 기둥에서 {end_peg}번 기둥으로 이동")

def hanoi(num_discs, start_peg, end_peg):
   #base case
   if num_discs == 0:
      return

   other_peg = 6 - start_peg - end_peg

   hanoi(num_discs - 1, start_peg, other_peg)
   move_disk(num_discs, start_peg, end_peg)
   hanoi(num_discs - 1, other_peg, end_peg)
# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)

"""
hanoi(2, 1, 3)
1번 원판을 1번 기둥에서 2번 기둥으로 이동
2번 원판을 1번 기둥에서 3번 기둥으로 이동
1번 원판을 2번 기둥에서 3번 기둥으로 이동

hanoi(3, 1, 3)
1번 원판을 1번 기둥에서 3번 기둥으로 이동
2번 원판을 1번 기둥에서 2번 기둥으로 이동
1번 원판을 3번 기둥에서 2번 기둥으로 이동
3번 원판을 1번 기둥에서 3번 기둥으로 이동
1번 원판을 2번 기둥에서 1번 기둥으로 이동
2번 원판을 2번 기둥에서 3번 기둥으로 이동
1번 원판을 1번 기둥에서 3번 기둥으로 이동

"""
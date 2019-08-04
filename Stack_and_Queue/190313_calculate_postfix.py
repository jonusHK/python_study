from stack import Stack

def calc_to_postfix(ch):
   st = Stack()
   for i in range(len(ch)):
      if ch[i].isdigit():
         st.push(ch[i])
      else:
         b = int(st.pop())
         a = int(st.pop())
         if ch[i] == '*':
               st.push(a * b)
         elif ch[i] == '+':
               st.push(a + b)
         elif ch[i] == '-':
               st.push(a - b)
         else:
               st.push(a // b)

   print(st.peek())

calc_to_postfix('322*+4-3*257-*+')  # 5
calc_to_postfix('57*53/-2+53*+')  # 51
calc_to_postfix('735*2/-35*23*-+')  # 9
calc_to_postfix('6523*-*32*32/+1+-') # -14
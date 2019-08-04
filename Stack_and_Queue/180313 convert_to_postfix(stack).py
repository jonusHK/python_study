from stack import Stack
st = Stack()
listExp = []

def convert_to_postfix(ch):
    global st, listExp
    listExp = []

    for i in range(len(ch)):
        if ch[i].isdigit():
            listExp.append(ch[i])
        else:
            decide_order(ch[i])

    while st.empty() != True:
        listExp.append(st.pop())

    result = "".join(listExp)

    return result
        
def decide_order(sign):
    global st, listExp
    if st.empty() == True or get_weight(sign) == 1:
        st.push(sign)
    elif get_weight(sign) == 0:
        while st.peek() != '(':
            listExp.append(st.pop())
        st.pop()
    else: 
        while get_weight(sign) <= get_weight(st.peek()):
            listExp.append(st.pop())
            if st.empty() == True:
                break
        st.push(sign)
        
def get_weight(sign):
    if sign == '*' or sign == '/':
        weight = 3
        return weight
    elif sign == '+' or sign == '-':
        weight = 2
        return weight
    elif sign == '(':
        weight = 1
        return weight
    else:
        weight = 0
        return weight

print(convert_to_postfix('(3+2*2-4)*3+2*(5-7)'))  # 322*+4-3*257-*+
print(convert_to_postfix('5*7-5/3+2+5*3'))  # 57*53/-2+53*+
print(convert_to_postfix('7-3*5/2+(3*5-2*3)'))  # 735*2/-35*23*-+
print(convert_to_postfix('6*(5-2*3)-(3*2+3/2+1)'))  # 6523*-*32*32/+1+-
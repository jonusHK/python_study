# same life cycle
# strongly coupled
class CPU:
    def __init__(self, c_manf, name):
        self.c_manf = c_manf
        self.name = name

class RAM:
    def __init__(self, r_manf, giga):
        self.r_manf = r_manf
        self.giga = giga

# HAS-A
# 객체의 멤버로써 다른 객체를 포함해서 사용한다.

# composition
# 객체들의 생성 시점이 같다!!
# 객체들의 소멸 시점도 같다!!
# cpu, ram, computer 강하게 커플링 되어 있다.

# 코드 재사용성을 위해서 관계를 구축하는 거라면
# 상속보다는 컴포지션을 사용한다.

class Computer:
    def __init__(self, c_manf, name, r_manf, giga):
        self.cpu = CPU(c_manf, name)
        self.ram = RAM(r_manf, giga)

if __name__ == "__main__":
    comp1 = Computer('intel', 'i7-8700', 'samsung', '16G')
    comp2 = Computer('라이젠', 'AMD', 'LG', '8G')
    print('--- comp1 사양 ---')
    print(comp1.cpu.c_manf)
    print(comp1.cpu.name)
    print(comp1.ram.r_manf)
    print(comp1.ram.giga)
    print('--- comp2 사양 ---')
    print(comp2.cpu.c_manf)
    print(comp2.cpu.name)
    print(comp2.ram.r_manf)
    print(comp2.ram.giga)
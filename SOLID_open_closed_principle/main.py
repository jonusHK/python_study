from character import Player
from attack_kind import FireAttackKind, IceAttackKind
from monsters import FireMonster, IceMonster, StoneMonster, KungfuMonster, ArrowMonster

fm = FireMonster()
im = IceMonster()
sm = StoneMonster()
kfm = KungfuMonster()

monsters=[]
monsters.extend((fm, im, sm, kfm))

# Dependency Injection : DI  --> main.py 에서 
player = Player('john', 120, 20, FireAttackKind(), IceAttackKind())

for mon in monsters:
    player.attack(mon, 'Fire')

for mon in monsters:
    print(mon.get_attack_kind())
    mon.attack(player, mon.get_attack_kind())

new_mon = ArrowMonster()

print(player)
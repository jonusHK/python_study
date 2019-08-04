class Gun:
    def __init__(self, kind):
        self.kind = kind

    def bangbang(self):
        print(f'{self.kind} bangbang!!')

class Police:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def acquire_gun(self, gun):
        self.gun = gun
        gun = None

    def release_gun(self):
        gun = self.gun
        self.gun = None
        return gun

    def shoot(self):
        if not self.gun:
            print('You don\'t have a gun')   # 문자열 '' 안에 '을 쓰고 싶다면, \'
        else:
            self.gun.bangbang()

if __name__ == "__main__":
    pol = Police('john')
    gun = Gun('revolver')
    pol.shoot()

    # police 객체가 gun 객체를 얻은 시점
    pol.acquire_gun(gun)
    pol.shoot()

    gun = pol.release_gun()
    pol.shoot()

    del pol
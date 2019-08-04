class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def browser(self):
        print('browser')

    def work(self):
        print('work')

class Laptop(Computer): 
    def __init__(self, cpu, ram, battery):
        super().__init__(cpu, ram)
        self.battery = battery

    def move(self, to):
        print('move to {}'.format(to))

    
if __name__ == "__main__":
    com = Computer('i5', 12)
    com.browser()
    com.work()

    dell = Laptop('i7', 32, 'powerful')
    dell.browser()
    dell.work()
    dell.move('home')


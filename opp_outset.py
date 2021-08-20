# ПРОСТО ВЕРЮШКА
# демонерирует простейший класс и объект
class Critter(object):
    '''ВИРТУАЛЬНЙ ПИТОМЕЦ'''
    total = 0

    @staticmethod
    # static method
    def status():
        print('\nВсего зверюшек сейчас:', Critter.total)

    def __init__(self, name):
        print('Появилась на свет новая зверюшка')
        self.name = name
        Critter.total += 1

    def __str__(self):
        rep = 'Объкт класса Criter\n'
        rep += 'имя: ' + self.name + '\n'
        return rep

    def talk(self):
        print('Привет. Меня зовут', self.name, '\n')
    # Основная часть


print(Critter.total)
crit = Critter('Паша')

crit.talk()
crit1 = Critter('Фрося')
crit1.talk()

print(crit.name)

print(crit1.name)
crit.name = 'fools'
print(crit.name)
print(Critter.total)
Critter.status()

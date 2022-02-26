print('Úkol 5')


class Warrior:

    def __init__(self, name, maximum_health):
        self.name = name
        self.maximum_health = maximum_health

    def __str__(self):
        return f'{self.name}, životů: {self.maximum_health}, {"žije" if self.is_alive else "již nežije"}'

    def __add__(self, other):
        if self.is_alive and other.is_alive:
            return Warrior(
                f'{other.name}+{self.name} child', (self.maximum_health + other.maximum_health)
            )
        return print(f'Mrtvý nemají děti, zatím.')

    def __sub__(fighter1, fighter2):
        if fighter1.is_alive and fighter2.is_alive:
            if fighter1.maximum_health < fighter2.maximum_health:
                fighter1.maximum_health = 0
                return print(f'{fighter1.name} poražen od {fighter2.name}')
            elif fighter1.maximum_health > fighter2.maximum_health:
                fighter2.maximum_health = 0
                return print(f'{fighter2.name} poražen od {fighter1.name}')
            else:
                fighter1.maximum_health -= 1
                fighter2.maximum_health -= 1
                return print('Plichta!')
        else:
            return print('Mrtvý nebojují, zatím.')

    @property
    def is_alive(self):
        return self.maximum_health > 0


w1 = Warrior('Xena', 1)
print(w1)

w2 = Warrior('Conan', 2)
print(w2)

w3 = w1 + w2
print(w3)

w4 = w1 + w2
print(w4)

c1 = w1 - w2

c2 = w1 - w2

w5 = w1 + w2

c3 = w3 - w4
print(w3)
print(w4)


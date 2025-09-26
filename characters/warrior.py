from characters.character import Character

class Warrior(Character):

    def __init__(self, name = '전사'):
        super().__init__(name = name, health = 100, attack_power = 15)

    def attack(self, target):
        print(f'{self.name}님의 기본 공격!')
        target.take_damage(self.attack_power)

    def special_attack(self, target):
        print(f'{self.name}님의 특수 공격!')
        print('[강력한 일격]')
        damage = self.attack_power * 2
        target.take_damage(damage)
        self.health -= 5
        print(f'{self.name}님 특수 공격 사용 반동으로 5 HP가 감소')
        print(f'남은 HP: {self.health}')
        if self.health < 0:
            self.health = 0
            print('체력을 모두 소진하셨습니다.')


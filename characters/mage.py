from characters.character import Character


class Mage(Character):

    def __init__(self, name = '마법사'):
        super().__init__(name = name, health = 80, attack_power = 18)

    def attack(self, target):
        print(f'{self.name}님의 기본 공격!')
        target.take_damage(self.attack_power)
        
    def special_attack(self, target):
        print(f'{self.name}님의 특수 공격!')
        print('[파이어볼]')
        print()
        if self.mana < 20:
            raise Exception(f'{self.name}님의 마나가 부족합니다! \n 현재 마나: {self.mana}')
        damage = self.attack_power * 1.5
        target.take_damage(damage)
        self.mana -= 20
        print(f'{self.name}님 20 마나를 사용하여 특수 공격 실행')
        print(f'- 20 마나, 남은 마나: {self.mana}')
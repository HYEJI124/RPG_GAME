from abc import ABC, abstractmethod

class Character(ABC):
    @abstractmethod
    def __init__(self, name = '캐릭터', level = 1, health = 100, attack_power = 10, mana = 50):
        self.name = name
        self.level = level
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.mana = mana
        self.max_mana = mana
        print()
        print(f'캐릭터 생성: {name} / LV. {level} /  HP. {health} /  ATK: {attack_power} / 마나: {mana}')
        print()


    @abstractmethod
    def attack(self, target):
        pass
    
    @abstractmethod
    def special_attack(self, target):
        pass

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print('체력을 모두 소진하셨습니다.')
        print(f'{self.name}님이(가) {damage}만큼 피해를 입었습니다!')
        print(f'{self.name}님: -{damage} HP,  남은 체력: {self.health} HP')
        print()

    def is_alive(self):
        return self.health > 0

    def show_status(self):
        print(f'현재 {self.name}님의 상태')
        print(f'LV. {self.level} , HP: {self.health}/{self.max_health} , ATK: {self.attack_power}')
        print()

    def reset_health(self):
        self.health = self.max_health
        print(f'{self.name}님의 체력이 회복되었습니다. \n')
        print(f'현재 HP: {self.health}')

    def reset_mana(self):
        self.mana = self.max_mana
        print(f'{self.name}님의 마나가 회복되었습니다. \n')
        print(f'현재 마나: {self.mana}')

    def get_name(self):
        return self.name













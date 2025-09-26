from characters.warrior import Warrior
from characters.mage import Mage
from characters.rogue import Rogue
from battle.battle_manager import BattleManager

import random

Character_Choice = {
    '1': Warrior, '전사': Warrior,
    '2': Mage, '마법사': Mage,
    '3': Rogue, '도적': Rogue,
}

def choose_character(prompt_message):
    print(prompt_message)

    while True:
        choice = input('1. 전사 / 2. 마법사 / 3. 도적: ').strip()
        cls = Character_Choice.get(choice)
        if cls:
            name = input('캐릭터 이름을 입력하세요 (엔터: 기본 이름 사용): ').strip()
            if name:
                try:
                    return cls(name)
                except TypeError:
                    inst = cls()
                    inst.name = name
                    return inst
            return cls()
        print('잘못된 입력입니다. 1, 2, 3 또는 전사 / 마법사 / 도적 중에서 선택하세요.')

def choose_random_enemy():
    cls = random.choice([Warrior, Mage, Rogue])
    return cls()

def game():
    print('=' * 50)
    print('*' * 17, 'RPG 게임 시작', '*' * 17)
    print('=' * 50)

    player = choose_character('당신의 캐릭터를 선택하세요')
    print()

    while True:
        use_random = input('적을 랜덤으로 생성하시겠습니까? (y/n):').strip().lower()
        print()
        if use_random == 'n':
            enemy = choose_character('상대 캐릭터를 선택하세요')
            print()            
        else:
            enemy = choose_random_enemy()
            print()
            

        bm = BattleManager(player, enemy)
        won = bm.start_battle()

        if won:
            again = input('새로운 적과 싸우시겠습니까? (y/n): ').strip().lower()
            print()
            if again != 'y':
                print('게임을 종료합니다.')
                break

            heal = input('전투 후 체력/마나를 회복하시겠습니까? (y/n): ').strip().lower()
            if heal == 'y':
                player.reset_health()
                player.mana = getattr(player, 'max_mana', 50)

        else:
            print('게임을 종료합니다.')
            break

if __name__ == '__main__':
    try:
        game()
    except Exception as e:
        print(f'\n오류가 발생했습니다: {e}')
        print('게임을 종료합니다.')
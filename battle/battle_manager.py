import time, random

class BattleManager:

    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        print('=' * 50)
        print('*' * 20, '전투 시작!', '*' * 20)
        print('=' * 50)
        self.player.show_status()
        self.enemy.show_status()

        turn = random.choice([self.player, self.enemy])
        print(f'첫 번째 공격자는 {turn.name}님! \n')

        player_turn_count = 0
        enemy_turn_count = 0

        while self.player.is_alive() and self.enemy.is_alive():
            # cmd = input('엔터를 누르면 전투를 계속합니다. (q 입력 시 중단): \n')
            # if cmd.lower() == 'q':
            #     print('\n게임을 중단했습니다. 패배로 처리됩니다..\n')
            #     return False
            
            attacker = turn
            defender = self.enemy if attacker == self.player else self.player

            if attacker == self.player:
                player_turn_count += 1
                print(f'==== {self.player.name}님의 {player_turn_count}번째 공격 ====')
            else:
                enemy_turn_count += 1
                print(f'==== {self.enemy.name}님의 {enemy_turn_count}번째 공격 ====')

            try:
                if random.random() <= 0.7:
                    attacker.attack(defender)
                    print()
                else:
                    attacker.special_attack(defender)
                    print()
            except Exception as e:
                print(f'{e} -> 기본 공격 진행')
                attacker.attack(defender)
                print()

            time.sleep(5)
            print()

            
            if defender.is_alive():
                turn = defender 
            else:
                print('HP: 0')
                print(f'{defender.name}이(가) 쓰러졌습니다! \n')
                break

        if self.player.is_alive():
            print(f'{self.player.name}님의 승리!!')
            return True
        else:
            print(f'{self.enemy.name}님의 승리!!')
            print(f'{self.player.name}님 게임 오버...\n')
            return False


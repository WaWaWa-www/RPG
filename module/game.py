# module/game.py
from module.characters import Hero, Dragon, Skill
import random

class Game:
    def __init__(self):
        self.heroes = [
            Hero("勇者", 100, 50, Skill("剣の舞", 20)),
            Hero("剣士", 80, 10, Skill("連続斬り", 15)),
            Hero("魔法使い", 60, 50, Skill("メテオ", 40)),
            Hero("僧侶", 70, 30, Skill("回復", 25))
        ]
        self.dragon = Dragon("ドラゴン", 200)

    def start_battle(self):
        # バトルの開始処理
        pass

    def hero_turn(self, hero):
        # 勇者のターンの処理
        if hero.use_skill():
            # スキルの効果を適用
            pass
        else:
            # MPが足りない場合の処理
            pass

    def dragon_turn(self):
        # ドラゴンのターンの処理
        pass

    def check_game_over(self):
        # ゲーム終了条件の判定
        pass

    def get_end_message(self):
        # ゲーム終了時のメッセージを取得
        pass

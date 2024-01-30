# main.py
from flask import Flask, render_template
from module.game import Game

app = Flask(__name__)
game_instance = Game()

class Hero:
    def __init__(self, name, hp, mp, skill):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skill = skill

class Skill:
    def __init__(self, name, mp_cost):
        self.name = name
        self.mp_cost = mp_cost

class Game:
    def __init__(self, dragon, heroes):
        self.dragon = dragon
        self.heroes = heroes

class Dragon:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

@app.route('/')
def top():
    return render_template('top.html')

@app.route('/battle')
def battle():
    dragon = Dragon(name="ドラゴン", hp=100)
    hero_skill = Skill(name="ファイアボール", mp_cost=10)
    hero = Hero(name="勇者", hp=80, mp=50, skill=hero_skill)
    game_instance = Game(dragon=dragon, heroes=[hero])
    return render_template('battle.html', game=game_instance, hero=hero)

@app.route('/end')
def end():
    end_message = game_instance.get_end_message()
    return render_template('end.html', end_message=end_message)

if __name__ == '__main__':
    app.run(debug=True)


from random import randint
from enum import Enum
from dataclasses import dataclass
dash = "-" * 50 + "\n"
def dice_roll(num_dice, num_face):
    roll = randint(num_dice, num_face * num_dice)
    return roll
@dataclass
class Item:
    name: str
    quantity: int
class Inventory:
    def __init__(self):
        self.name_item_list = []
        self.quantity_item_list = []
    def add_item(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.item = Item(self.name, self.quantity)
        self.name_item_list.append(self.item.name)
        self.quantity_item_list.append(self.item.quantity)
    def discard_item(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.item = Item(self.name, self.quantity)
        self.index_finder = self.name_item_list.index(self.name)
        self.addends = self.quantity_item_list[self.index_finder]
        self.sum = self.addends - self.quantity
        self.quantity_item_list[self.index_finder] = self.sum
        if self.sum == 0:
            self.name_item_list.remove(self.item.name)
        elif self.sum < 0:
            self.quantity_item_list[self.index_finder] = self.addends
            print("Valeur trop haute")
    def check_inventory(self):
        self.checking = True
        while self.checking:
            for i in range(len(self.name_item_list)):
                print(f"{self.name_item_list[i]}:\n    Quantité: {self.quantity_item_list[i]}")
            self.put_take = int(input("Que voulez-vous faire:\n    1-Mettre un objet\n    2-Prendre un objet\n    3-Quitter\n\n> "))
            match self.put_take:
                case 1:
                    self.add_item(str(input("Que voulez-vous mettre\n> ")), int(input("En quel quantité:\n> ")))
                    for i in range(len(self.name_item_list)):
                        print(f"{self.name_item_list[i]}:\n    Quantité: {self.quantity_item_list[i]}")
                case 2:
                    self.discard_item(str(input("Que voulez-vous enlever\n> ")), int(input("En quel quantité:\n> ")))
                    for i in range(len(self.name_item_list)):
                        print(f"{self.name_item_list[i]}:\n    Quantité: {self.quantity_item_list[i]}")
                case 3:
                    self.checking = False
class Character:
    def __init__(self, name, side, strenght, dexterity, body):
        self.name = name
        self.side = side
        self.str = strenght
        self.dex = dexterity
        self.body = body
        self.hp = dice_roll(1, 100) * body
        print(f"Enemy {self.name} created")
    def do_damage(self):
        self.try_attack = dice_roll(1,100)
        if self.try_attack <= self.dex:
            self.attack_damage = self.str + dice_roll(2,10)
        else:
            self.attack_damage = 0
        print(self.attack_damage)
        return self.attack_damage
    def take_damage(self, damage):
        self.damage = damage
        self.hp -= self.damage


class Player(Character):
    def __init__(self):
        super().__init__("BOB", "player", 200, 60, 50)
class Enemy(Character):
    def __init__(self, id):
        self.id = id
        self.all_name = ["Joe","Xavier","Eric","Diago","Marco"]
        super().__init__(self.all_name[self.id], "enemy", 60, 50, 60)
class Fight:
    def __init__(self, number_of_enemy, difficulty):
        self.num_enemy = number_of_enemy
        self.difficulty = difficulty
        self.fight_list = [p]

    def create_fight(self):
        for i in range(1, self.num_enemy):
            self.enemy = Enemy(i)
            self.fight_list.append(self.enemy)
    def player_turn(self):
        try:
            for i in range(self.num_enemy):
                print(f"{i + 1}-{self.fight_list[i].name}: {self.fight_list[i].hp} pv")
        except:
            pass
        try:
            self.choose_target = int(input("> "))
            self.fight_list[self.choose_target - 1].take_damage(p.do_damage())
            if self.fight_list[self.choose_target - 1].hp <= 0:
                self.fight_list.pop(self.choose_target - 1)
        except:
            pass
    def enemy_turn(self, doer):
        self.doer = doer
        p.take_damage(self.doer.do_damage())
    def battle(self):
        while p.hp > 0:
            for i in range(self.num_enemy):
                try:
                    self.turn = self.fight_list[i].side
                    match self.turn:
                        case "player":
                            self.player_turn()
                        case "enemy":
                            self.enemy_turn(self.fight_list[i])
                except IndexError:
                    pass
        else:
            print("T mow")
    def display_enemies(self):
        for i in range(self.num_enemy):
            print(f"Fighter in fight: {self.fight_list[i].name}")
p = Player()
i = Inventory()
i.add_item("Meth", 100)
i.add_item("Hache", 11)
i.add_item("Lance", 131)
i.add_item("Dague", 112)
i.check_inventory()
f = Fight(4,1)
f.create_fight()
f.display_enemies()
f.battle()

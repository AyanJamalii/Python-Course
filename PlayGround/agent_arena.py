class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(f"{self.name} attacks with basic damage!")

class Warrior(Character):
        def __init__(self, name, health, weapon="Sword"):
            super().__init__(name, health)
            self.weapon = weapon
        def attack(self):
             print(f"{self.name} Swings a sharp {self.weapon} for 50 damage.")

class Mage(Character):
    def __init__(self, name, health, spell="Fireball"):
        super().__init__(name, health)
        self.spell = spell
    def attack(self):
         print(f"{self.name} casts {self.spell} for 80 magic damage!")

class BattleArena:
    def start_battle(self, char1, char2):
        print(f"--- Battle Arena --- ")
        char1.attack()
        char2.attack()


hero1 = Warrior("Bond", 100)
hero2 = Mage("MoneyPenny", 80)

arena = BattleArena()
arena.start_battle(hero1, hero2)
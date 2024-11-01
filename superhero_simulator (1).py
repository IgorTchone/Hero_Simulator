from abc import ABC, abstractmethod

class Fighter(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    @abstractmethod
    def get_health(self):
        pass

class Superman(Fighter):
    def __init__(self):
        self.health = 100

    def attack(self):
        return 20  # Damage from the attack

    def defend(self):
        return 10  # Damage reduction

    def get_health(self):
        return self.health

class WonderWoman(Fighter):
    def __init__(self):
        self.health = 100

    def attack(self):
        return 18

    def defend(self):
        return 12

    def get_health(self):
        return self.health

class Flash(Fighter):
    def __init__(self):
        self.health = 90

    def attack(self):
        return 15

    def defend(self):
        return 8

    def get_health(self):
        return self.health

class Thor(Fighter):
    def __init__(self):
        self.health = 120

    def attack(self):
        return 25

    def defend(self):
        return 15

    def get_health(self):
        return self.health

class Combat:
    def __init__(self, fighter1, fighter2):
        self.fighter1 = fighter1
        self.fighter2 = fighter2

    def start_combat(self):
        while self.fighter1.get_health() > 0 and self.fighter2.get_health() > 0:
            self.round(self.fighter1, self.fighter2)
            if self.fighter2.get_health() <= 0:
                print(f"{self.fighter2.__class__.__name__} has been defeated!")
                break
            self.round(self.fighter2, self.fighter1)
            if self.fighter1.get_health() <= 0:
                print(f"{self.fighter1.__class__.__name__} has been defeated!")

    def round(self, attacker, defender):
        damage = attacker.attack() - defender.defend()
        damage = max(0, damage)  # Damage cannot be negative
        defender.health -= damage
        print(f"{attacker.__class__.__name__} attacks and deals {damage} damage!")
        print(f"{defender.__class__.__name__} now has {defender.get_health()} health.")

if __name__ == "__main__":
    print("Choose two characters for a fight:")
    print("1 - Superman")
    print("2 - Wonder Woman")
    print("3 - Flash")
    print("4 - Thor")

    choice1 = int(input("Choose the first fighter (1, 2, 3, or 4): "))
    choice2 = int(input("Choose the second fighter (1, 2, 3, or 4): "))

    fighters = {
        1: Superman(),
        2: WonderWoman(),
        3: Flash(),
        4: Thor()
    }

    fighter1 = fighters.get(choice1)
    fighter2 = fighters.get(choice2)

    if fighter1 is None or fighter2 is None:
        print("Invalid choice! Please select 1, 2, 3, or 4.")
    else:
        combat = Combat(fighter1, fighter2)
        combat.start_combat()

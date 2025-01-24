class Weappon:
    
    def __init__(self, model, damage):
        self.name = model
        self.damage = damage


class Player:
    health = 100
    money = 800

    def __init__(self, name: str, team: str, weapon: Weappon):
        self.name = name
        self.team = team
        self.weapon = weapon

    def shoot(self, player):
        if self.health > 0 and player.health > 0:
            player.health -= self.weapon.damage
            if player.health <= 0:
                print(f"{self.name} killed {player.name}")


class Counter(Player):
    
    def defuse(self):
        print(f"{self.name} defused the bomb.")

class Terror(Player):
   
    def plant(self):
        print(f"Bomb has been planted by {self.name}.")


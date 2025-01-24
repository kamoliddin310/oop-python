
class Player:
    health = 100
    money = 800

    def __init__(self, name, team):
        self.name = name
        self.team = team

    def shoot(self, player):
        if player.health <= 0:
            return
        player.health -= 15
        if player.health <= 0:
            print(f"{self.name} killed {player.name}")


p2 = Player("mizro", "Counter-Terrorist")
p1 = Player("Devil", "Terrorist")

p1.shoot(p2)
p1.shoot(p2)
p1.shoot(p2)
p1.shoot(p2)
p1.shoot(p2)
p1.shoot(p2)
p1.shoot(p2)



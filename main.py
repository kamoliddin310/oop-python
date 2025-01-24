from cs import Weappon, Terror, Counter

w1 = Weappon("AK74", 25)
w2 = Weappon("AKM", 30)

p1 = Terror("mizro", "Counter-Terrorist", w1)
p2 = Counter("kamoliddin", "Terrorist", w2)

p1.plant()
p2.defuse()

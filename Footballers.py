class Footballer:

    """Best football team ever existed"""

    
    total = 11

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos

footballers = []

for i in [["Tkachuk", 3], ["Ermakov", 5], ["Kovalenko", 25], ["Zapadnya", 13], ["Chenbay", 21], ["Golodyuk", 32], ["Savin", 77], ["Kravchenko", 27], ["Dmytrenko", 22], ["Batyushin", 9]]:
    footballers.append(Footballer(i[0], i[1]))


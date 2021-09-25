class Critter: 
    """Virtual HOHOL""" 
    total = 0 
 
    @staticmethod    
    def status(): 
        print("Total hohol number", Critter.total) 
 
    def __init__(self, name, hunger = 0, boredom = 0): 
        self.__name = name 
        self.hunger = hunger 
        self.boredom = boredom 
        Critter.total += 1 
 
    def __str__(self): 
        ans = 'Object class Critter\n' 
        ans += 'hohol: ' + self.name + '\n' 
        return ans 
     
    def __pass_time(self): 
        self.hunger += 1 
        self.boredom += 1 
 
    @property 
    def name(self): 
        return self.__name 
 
    @name.setter 
    def name(self, new_name): 
        if new_name == "": 
            print("Hohol won't read yor thoughts when you need him. He can't read them at all actually (so far).") 
        else: 
            self.__name = new_name 
            print("Hohol will remember this") 
 
    @property 
    def mood(self): 
        unhappiness = self.hunger + self.boredom 
        if unhappiness < 5: 
            m = "perfect" 
        elif 5 <= unhappiness <= 10: 
            m = "not that bad" 
        elif 11 <= unhappiness <= 15: 
            m = "OK (not really)" 
        else: 
            m = "horrible" 
        return m 
 
    def talk(self): 
        print("My name's", self.name,  
              ", and i'm feeling", self.mood) 
        self.__pass_time() 
 
    def eat(self, food = 4): 
        print("Muchas gracias!") 
        self.hunger -= food 
        if self.hunger < 0: 
            self.hunger = 0 
        self.__pass_time() 
 
    def play(self, fun = 4): 
        print("! !! !!!!!! !!! ! !!!!!!!!!!!!!!!! *crunch* *scream* *loud chomping*") 
        self.boredom -= fun 
        if self.boredom < 0: 
            self.boredom = 0 
        self.__pass_time() 
 
def main(): 
    crit_name = input("How would you call your hohol?: ") 
    crit = Critter(crit_name) 
 
    choice = None   
    while choice != "0": 
        print
        (""" 
        My hohol
        0 - Break hohol's heart and leave him
        1 - How's hohol doing?
        2 - Feed hohol
        3 - Play with hohol 
        """) 
     
        choice = input("Your choise:") 
        print() 
 
        
        if choice == "0": 
            print("Husta la vista!") 
 
        
        elif choice == "1": 
            crit.talk() 
         
         
        elif choice == "2": 
            crit.eat(food=int(input("How much food would you feed to hohol?"))) 
          
        
        elif choice == "3": 
            crit.play(fun=int(input("How much time of your life would you spend pointlessly on hohol?"))) 
 
     
        else: 
            print("Hohol does not understand you, when you say", choice) 
     
main()

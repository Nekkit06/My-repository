class Tv: 
    def num(self,chanel): 
        if chanel<=100: 
            print('Current channel:',chanel) 
        elif chanel>100: 
            print('There are no channels more than 100') 
    def v1(self,vol1): 
        if vol1<=30: 
            print('Loudness successfully changed:',vol1) 
        elif vol1>30: 
            print("Hohol has put on his headphones") 
        elif vol1<=0: 
            print('Your hohol asks you not to make such a mistake') 
         
def main(): 
    crit = Tv() 
    chanel=int(input('Set channel number:')) 
    vol1=int(input('Set loudness:')) 
    choice = None   
    while choice != "0": 
        print 
        (""" 
        Hohol TELEVISION 
     
        0 - Let hohol watch TV and go make some coffee
        1 - Set channel number
        2 - Change loudness  
        """) 
     
        choice = input("Your choise: ") 
        print() 
 
    
        if choice == "0": 
            print("Husta la vista.") 
 
 
        elif choice == "1": 
            crit.num(chanel) 
         
 
        elif choice == "2": 
            crit.v1(vol1) 
          
 
 
        
        else: 
            print("Error 404: Bad request", choice) 
     
main()


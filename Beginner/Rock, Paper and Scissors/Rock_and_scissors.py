import random
# Making a list of all the possible choices
choices=["R","P","S"]   # R-->Rock  P-->Paper   S-->Scissors
computer=random.choice(choices)
player=False
Player_Score=0
Computer_Score=0

while True:
    from playsound import playsound
    playsound("C:\\Users\\dell\\Documents\\PYTHON CODES\\PROJECTS\\Rock, Paper And Scissors\Sound-Effect Race Countdown (HD).mp3")
    
    player=input("What do you want to choose between R,P and S ?").capitalize()
    ## Conditions of rock, paper and scissors
    if player==computer:
        from playsound import playsound
        playsound("C:\\Users\\dell\\Documents\\PYTHON CODES\\PROJECTS\\Rock, Paper And Scissors\\Aww Sound Effect.mp3")
        
        print("Tie!")
    elif player=="R":
        if computer=="P":
            from playsound import playsound
            playsound("C:\\Users\\dell\\Documents\\PYTHON CODES\\PROJECTS\\Rock, Paper And Scissors\Wrong Buzzer - Sound Effect.mp3")
            
            print("You loose: Paper wraps the rock inside it!")
            Computer_Score+=1
        else:
            from playsound import playsound
            playsound("C:\\Users\\dell\\Documents\\PYTHON CODES\\PROJECTS\\Rock, Paper And Scissors\\Winning-sound-effect.mp3")
            
            print("You won: Rock smashed the scissors!")
            Player_Score+=1
    elif player=="P":
        if computer=="S":
            from playsound import playsound
            playsound("C:\\Users\\dell\\Documents\\PYTHON CODES\\PROJECTS\\Rock, Paper And Scissors\Wrong Buzzer - Sound Effect.mp3")
            
            print("You loose: Scissors cut the Paper!")
            Computer_Score+=1
        else:
            from playsound import playsound
            playsound("C:\\Users\\dell\\Documents\\PYTHON CODES\\PROJECTS\\Rock, Paper And Scissors\\Winning-sound-effect.mp3")
            
            print("You won: Paper wraps the rock inside it!")
            Player_Score+=1
    elif player=="S":
        if computer=="R":
            from playsound import playsound
            playsound("C:\\Users\\dell\\Documents\\PYTHON CODES\\PROJECTS\\Rock, Paper And Scissors\Wrong Buzzer - Sound Effect.mp3")
            
            print("You loose: Rock smashed the scissors!")
            Computer_Score+=1
        else:
            from playsound import playsound
            playsound("C:\\Users\\dell\\Documents\\PYTHON CODES\\PROJECTS\\Rock, Paper And Scissors\\Winning-sound-effect.mp3")
            
            print("You won: Scissors cut the paper!")
            Player_Score+=1
    elif player=="End":
        print("The final scores are:")
        import colorama
        from colorama import Fore, Back, Style
        colorama.init(autoreset=True)
        
        print("The score of computer is:" +Fore.RED+ "{}".format(Computer_Score))
        print("The score of the player is :"+Fore.GREEN+ "{}".format(Player_Score))
        if Computer_Score>Player_Score:
            print(Fore.BLUE+Back.WHITE+"COMPUTER WON")
        elif Player_Score>Computer_Score:
            print(Fore.YELLOW+Back.RED+"YOU WON")
        else:
            print(Fore.BLACK+Back.WHITE+"The game is Tie")        
        
        print("Thanks For Playing!")
        from playsound import playsound
        playsound("C:\\Users\\dell\\Documents\\PYTHON CODES\\PROJECTS\\Rock, Paper And Scissors\Thanks For Playing.m4a")
        break



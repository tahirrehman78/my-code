print("Please Enter your Genre -\n"
            "1. action\n"  
            "2. advanture\n" 
            "3. animated\n" 
            "4. drama\n"
            "5. fantasy\n"
            "6. comedy\n")
genre=input("ENTER YOUR GENRE NAME?")
if(genre=="action"or genre=="Action"):
    print("John Wick, Fast and Furious, The Avengers")
elif(genre=="advanture" or genre=="Advanture"):
    print("Indiana Jones, Pirates of the Caribbean, Tomb Raider")
elif(genre=="animated" or genre=="Animated"):
    print("Toy Story, Shrek, Coco, Frozen")
elif(genre=="comedy" or genre=="Comedy"):
    print("Monty Python, The Hangover, What men want")
elif(genre=="drama" or genre=="Drama"):
    print("Marriage Story, The Sound of Metal")
elif(genre=="fantasy" or genre=="Fantasy"):
    print("Harry Potter, Highlander, Lord of the Rings")
else:
    print("This Genre in not in our list")
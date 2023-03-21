
#Created by Gurshaan Singh bansal
#Date 27/02/2023
#Demonstrate asking the user a question, provide multiple choice awnsers, get the user's awnser, check if its correct


#asking the user for their name to start this quiz
name = input("What is your name? \n")
print("\n Hi {} Are you ready to try the most fun car quiz in the world? \n".format(name).strip())
points = 0 

def check(options , user_input):
    if user_input in options:
       return True
    else:
       return False 
#asking user to confirm if the user wants to play he quiz or not    
options = ["yes" , "a" ]
wants_to_play = input ("\n A) Yes \n B) No\n \n").lower().strip()

if check(options, wants_to_play):
    print("\n Okay mate lets start! \n")
elif wants_to_play == "no" or wants_to_play == "b":
    print("\n Too bad you are doing it anyways\n")
    points -= 1
#question one
options = ["d" , "bugatti chiron super sport 300+" , "bugatti" , "chiron super sport 300+" , "chiron super sport 300" , "chiron" , "super sport" , "super" , "sport" , "300+" , "300" , "Bugatti Chiron Super Sport" , "bugatti chiron"]
question = input("What is the fastest car in the world?  \n A) Hennessey Venom F5 \n B) Nissan Skyline r34 GTR \n C) Toyota Supra mk4 (a90) \n D) Bugatti Chiron Super Sport 300+ \n \n").lower().strip()

if check(options, question):
    print("\n You got the right awnser! \n")
    points += 1
else:
    print("\n Wrong awnser! \n")

#question two
options = ["a" ,"mazda" , "mazda miata mx5" ,"miata" , "mx5" ]
question = input ("What car is from Japan?  \n A) Mazda Miata MX5 \n B) Chevrolet Corvette \n C) BMW M4 \n D) Mercades AMG GTR \n \n").lower().strip()

if check(options, question):
    print("\n You got the right awnser! \n")
    points += 1
else:
    print("\n You got the wrong awnser \n")

#question three
options = ["c" , "volvo" , ]
question = input ("Which manufacturer made seatbelts? \n A) Toyota \n B) Ford \n C) Volvo \n D) Hyundai \n \n").lower().strip()

if check(options, question):
    print("\n You got the right awnser! \n")
    points += 1
else:
    print("\n You got the wrong awnser \n")

#question four
options = ["b", "toyota" , ]
question = input ("What car company did Kiichiro Toyoda create? \n A) Opel \n B) Toyota \n C) Nissan \n D) Peugeot \n \n").lower().strip()

if check(options, question):
    print("\n You got the right awnser! \n")
    points += 1
else:
    print("\n You got the wrong awnser \n")

#question five    
options = ["d" ,"volkswagen" , "vw" ,]
question = input ("What car company owns Bugatti? \n A) Lada \n B) Lotus \n C) Mclaren \n D) Volkswagen \n \n").lower().strip()
if check(options, question):
    print("\n You got the right awnser! \n")
    points += 1
else:
    print("\n You got the wrong awnser \n")

#question six
options = ["b" , "tractors"]
question = input ("What did Lamborghini make before cars? \n A) Trucks \n B) Tractors \n C) Motorcycles\n D) Airplanes \n \n").lower().strip()

if check(options, question):
    print("\n You got the right awnser! \n")
    points += 1
else:
    print("\n You got the wrong awnser \n")

#question seven
options = ["a" , "currywurst"]
question = input ("What food item does VW make? \n A) Currywurst \n B) Burgers \n C) Yorkshire pudding \n D) Pies \n \n").lower().strip()

if check(options, question):
    print("\n You got the right awnser! \n")
    points += 1
else:
    print("\nYou got the wrong awnser \n")

#question eight
options = ["c" , "tesla"]
question = input ("What car company does Elon Musk own? \n A) Lucid air \n B) Rivian \n C) Tesla \n D) BYD \n \n").lower().strip()

if check(options, question):
    print("\n You got the right awnser! \n")
    points += 1
else:
    print("\n You got the wrong awnser \n")

#question nine
options = ["a" , "bull"]
question = input ("Which animal features in the logo for Lamborghini? \n A) Bull \n B) Horse \n C) Cow \n D) Frog \n \n").lower().strip()

if check(options, question):
    print("\n hooray it is correct!\n ")
    points += 1
else:
    print("\n You got the wrong awnser \n")

#question ten
options = ["d" , "rolls royce " , "rr" , "rolls" , "royce"]
question = input ("Which iconic car manufacturer also made airplane engines? \n A) Acura \n B) Honda \n C) Suzuki \n D) Rolls Royce \n \n").lower().strip()

if check(options, question):
    print("\n Keep going! \n")
    points += 1
else:
    print("\n You got the wrong awnser \n")
#question eleven
options = ["c" , "toyota corolla" , "corolla " , "toyota"]
question = input ("What is the world's all-time bestselling car?  \n A) Honda Civic \n B) Chevrolet Camero \n C) Toyota Corolla \n D) Dodge Dart \n \n").lower().strip()

if check(options, question): 
    print("\n Good job! \n")
    points += 1
else:
    print("\n You got the wrong awnser \n")

#telling user how many they got right
print("\n Congrats you got {} out of 11 right good job. \n".format(points))

#remove one pint if user did not wanted to play
if wants_to_play == "no" or wants_to_play == "b":
    print ("I took away one point because you said no to playing the quiz. IT TOOK ME AGES.")

#thanking user for playing the quiz
print("\n Bye {} thank you for participating in my little fun quiz, I will see you in my next quiz, bye \n".format(name))
points = 0 

#author credentials
print ("\n Created by Gurshaan Singh Bansal \n published in 2023 \n")
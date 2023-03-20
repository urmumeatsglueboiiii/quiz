
#Created by Gurshaan Singh bansal
#Date 27/02/2023
#Demonstrate asking the user a question, provide multiple choice awnsers, get the user's awnser, check if its correct


#asking the user for their name to start this quiz
name = input("What is your name? \n")
print("Hi {} Are you ready to try the least fun puzzle quiz?\n".format(name))
points = 0 

def check(options , user_input):
    if user_input in options:
       return True
    else:
       return False 

options = ["d" , "bugatti chiron super sport 300+ " , "bugatti" , "chiron super sport 300+" , "chiron super sport 300" , "chiron" , ]
Question = input("What is the fastest car in the world?  \n A) Hennessey Venom F5 \n B) Nissan Skyline r34 GTR \n C) Toyota Supra mk4 (a90) \n D) Bugatti Chiron Super Sport 300+ \n \n").lower()

if check(options, Question):
    print("\n You got the right awnser! \n")
    points += 1
else:
    print("Wrong awnser!")


options = ["a" ,"mazda" , "mazda miata mx5" ,"miata" , "mx5" ]
Question = input ("What car is from Japan?  \n A) Mazda Miata MX5 \n B) Chevrolet Corvette \n C) BMW M4 \n D) Mercades AMG GTR \n ").lower()

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["c" , "volvo" , ]
Question = input ("Which manufacturer made seatbelts? \n A) Toyota \n B) Ford \n C) Volvo \n D) Hyundai \n").lower()

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["b", "toyota" , ]
Question = input ("What car company did Kiichiro Toyoda create? \n A) Opel \n B) Toyota \n C) Nissan \n D) Peugeot \n").lower()

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")

    
options = ["d" ,"volkswagen" , "vw" ,]
Question = input ("What car company owns Bugatti? \n A) Lada \n B) Lotus \n C) Mclaren \n D) Volkswagen \n").lower()

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["b" , "tractors"]
Question = input ("What did Lamborghini make before cars? \n A) Trucks \n B) Tractors \n C) Motorcycles\n D) Airplanes \n").lower()

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["a" , "currywurst"]
Question = input ("What food item does VW make? \n A) Currywurst \n B) Burgers \n C) Yorkshire pudding \n D) Pies \n").lower()

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["c" , "tesla"]
Question = input ("What car company does Elon Musk own? \n A) Lucid air \n B) Rivian \n C) Tesla \n D) BYD \n").lower()

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["a" , "bull"]
Question = input ("Which animal features in the logo for Lamborghini? \n A) Bull \n B) Horse \n C) Cow \n D) Frog \n").lower()

if check(options, Question):
    print("hooray it is correct!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["d" , "rolls royce " , "rr" ,]
Question = input ("Which iconic car manufacturer also made airplane engines? \n A) Acura \n B) Honda \n C) Suzuki \n D) Rolls Royce \n").lower()

if check(options, Question):
    print("Keep going!")
    points += 1
else:
    print("You got the wrong awnser")

options = ["c", "C" , "toyota corolla" , "Toyota Corolla" , "corolla " , "Corolla" , "Toyota", "toyota"]
Question = input ("What is the world's all-time bestselling car?  \n A) Honda Civic \n B) Chevrolet Camero \n C) Toyota Corolla \n D) Dodge Dart \n").lower()

if check(options, Question):
    print("Good job!")
    points += 1
else:
    print("You got the wrong awnser")


print("Congrats you got {} right! Hooray, you did a great job.".format(points))
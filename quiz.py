
#Created by Gurshaan Singh bansal
#Date 27/02/2023
#Demonstrate asking the user a question, provide multiple choice awnsers, get the user's awnser, check if its correct


#asking the user for their name to start this quiz
name = input("What is your name?")
print("Hi {} Are you ready to try the least fun puzzle quiz?".format(name))
points = 0 

def check(options , user_input):
    if user_input in options:
       return True
    else:
       return False

options = ["d" , "D" , "Bugatti Chiron Super Sport 300+ " , "Bugatti" , "bugatti"]
Question = input("What is the fastest car in the world?  \n A) Hennessey Venom F5 \n B) Nissan Skyline r34 GTR \n C) Toyota Supra mk4 (a90) \n D) Bugatti Chiron Super Sport 300+ ")

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("Wrong awnser!")


options = ["a", "A" , "Mazda" , "mazda" , "Mazda Miata MX5" , "mazda miata mx5" ,"miata" , "mx5" ]
Question = input ("What car is from Japan?  \n A) Mazda Miata MX5 \n B) Chevrolet Corvette \n C) BMW M4 \n D) Mercades AMG GTR ") 

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["c", "C" , "volvo" , "Volvo" , ]
Question = input ("Which manufacturer made seatbelts? \n A) Toyota \n B) Ford \n C) Volvo \n D) Hyundai ") 

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["b", "B" , "Toyota" , "toyota" , ]
Question = input ("What car company did Kiichiro Toyoda create? \n A) Opel \n B) Toyota \n C) Nissan \n D) Peugeot ") 

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")

    
options = ["d", "D" , "Volkswagen" , "volkswagen" , "vw" , "VW" , "Vw" , "vW"]
Question = input ("What car company owns Bugatti? \n A) Lada \n B) Lotus \n C) Mclaren \n D) Volkswagen ") 

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["B", "b" , "Tractors" , "tractors"]
Question = input ("What did Lamborghini make before cars? \n A) Trucks \n B) Tractors \n C) Motorcycles\n D) Airplanes ") 

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["A", "a" , "Currywurst" , "currywurst"]
Question = input ("What food item does VW make? \n A) Currywurst \n B) Burgers \n C) Yorkshire pudding \n D) Pies  ") 

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["C", "c" , "tesla" , "Tesla"]
Question = input ("What car company does Elon Musk own? \n A) Lucid air \n B) Rivian \n C) Tesla \n D) BYD ") 

if check(options, Question):
    print("You got the right awnser!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["a", "A" , "bull" , "Bull"]
Question = input ("Which animal features in the logo for Lamborghini? \n A) Bull \n B) Horse \n C) Cow \n D) Frog ") 

if check(options, Question):
    print("hooray it is correct!")
    points += 1
else:
    print("You got the wrong awnser")


options = ["d", "D" , "Rolls Royce " , "Rolls royce " , "rolls royce " , "rr" , "RR"]
Question = input ("Which iconic car manufacturer also made airplane engines? \n A) Acura \n B) Honda \n C) Suzuki \n D) Rolls Royce  ") 

if check(options, Question):
    print("Keep going!")
    points += 1
else:
    print("You got the wrong awnser")

options = ["c", "C" , "toyota corolla" , "Toyota Corolla" , "corolla " , "Corolla" , "Toyota", "toyota"]
Question = input ("What is the world's all-time bestselling car?  \n A) Honda Civic \n B) Chevrolet Camero \n C) Toyota Corolla \n D) Dodge Dart ") 

if check(options, Question):
    print("Good job!")
    points += 1
else:
    print("You got the wrong awnser")


print("Congrats you got {} right! Hooray, you did a great job.".format(points))
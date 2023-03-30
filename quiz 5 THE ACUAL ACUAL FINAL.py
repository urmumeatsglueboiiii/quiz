# Created by Gurshaan Singh Bansal
# Date 27 / 02 / 2023
# Demonstrate asking the user a question, provide multiple choice awnsers, get the user's awnser, check if its correct



# Check function to tell the code if the answer is true of false.
# User input is what the user puts in the text box.
# Correct answer is the variable that activates when the user has entered a input that is part of the correct answer list.
# Incorrect answer is if the user enters one of the options that are listed and then tells them that is is the wrong aswer.

def  check ( user_input, correct_answer, incorrect_answer ):
    if user_input in correct_answer:
       return True 
    elif user_input in incorrect_answer:
       return True
    else: return False 

# Asking the user for their name to start this quiz
# Points are letting the user know how mant questions they got right
# Print is what the user sees in the terminal
# Name is the variable when the code asks the user for their name
name = input ( "\n What is your name? \n" )
print ( "\n Hi {} Are you ready to try the most fun car quiz in the world? \n".format( name ).strip() )
points = 0 

# Asking user to confirm if the user wants to play he quiz or not.
# Wants to play is a variable that only implies for only this question.
# Wants to play is asking the user if they want to play the quiz or not.
# If is telling the code to check if the user ipout is the answer.
# Elif is used when you want to check for a different condition but the initial if statement is false.
# Else is when the code tries if and elif statementsw and if it is not true it will redirect to else statement
# While repets the code until a sepcific condition is met
# Quit variable only applies to this sepcific loop
quit = True
while ( quit ):
    wants_to_play = input ( "\n Did you want to play:\n \n A) Yes \n B) No \nD" ).lower().strip()
    if wants_to_play == "yes" or wants_to_play == "a":
        print ( "\n Okay mate lets start! \n" )
        quit = False
    
    elif wants_to_play == "no" or wants_to_play == "b":
        print ( "\n Too bad you are doing it anyways\n" )
        points -= 1
        quit = False
   
    else:
        print ( "\n C'mon dude there is only two options, a or b. IT'S NOT THAT HARD \n" )
        


# The variable question_.. has the number of the question behind it to direct the check function to check only the correct and incorrect answer lists for that question
# Question 1 What is the fastest car in the world?
question_1 = True
while ( question_1 ):

    correct_answer  = [ "chiron super sport 300+" ,"d" , "4" ,"bugatti" , "bugatti chiron super sport 300+", "chiron", "bugatti chiron"]
    incorrect_answer = ["a", "b", "c", "hennessey venom", "nissan skyline r34 gtr", "toyota supra mk4", "supra", "nissan", "skyline", "hennessy", "venom", "gtr", "r34", "toyota" ]
    question = input ( "What is the fastest car in the world?  \n A) Hennessey Venom F5 \n B) Nissan Skyline r34 GTR \n C) Toyota Supra mk4 (a90) \n D) Bugatti Chiron Super Sport 300+ \n \n" ).lower().strip()
# If statement will trigger if the user input is one of the options in the corerct answer list. If the if statment is true it will trigger a print statement that says,"You got the right awnser!"
# Elif statement will be triggered if the if statement is false (not the correct answer but in the question) which will then trigger a print statement, the print statment will say "You got the wrong awnser!"
# Else statement will trigger if the iff and the elif statement cannot verify the asnwers as true or false (user enters an keyword that is not in the question) and will print "you didnt chose from the options"
# Loop will trigger whn the elif statment is triggered
    if check ( question, correct_answer, incorrect_answer ):
       
        if question in correct_answer :
            print ( "\n You got the right awnser! \n" )
            question_1 = False
            points += 1
        else: 
            print ( "\n You got the wrong answer!\n" )
        question_1 = False
    else:
        print ( "\n you didnt chose from the options \n \n" ) 




# Question two. What car is from Japan?
question_2 = True
while ( question_2 ):

    correct_answer  = [ "a" ,"mazda" , "mazda miata mx5" ,"miata" , "mx5", "1" ]
    incorrect_answer = [ "chevrolet corvette", "bmw m4", "mercades amg gtr", "corvette", "chevrolet", "bmw", "m4", "mercades", "amg", "amg gtr", "mercades amg", "gtr", "2", "3", "4", "d", "b", "c" ]
    question = input ( "What car is from Japan?  \n A) Mazda Miata MX5 \n B) Chevrolet Corvette \n C) BMW M4 \n D) Mercades AMG GTR \n \n" ).lower().strip()

    if check ( question, correct_answer, incorrect_answer ):
       
        if question in correct_answer :
            print ( "\n You got the right awnser! \n" )
            question_2 = False
            points += 1
        else: 
            print ( "\n You got the wrong answer!\n" )
        question_1 = False
    else:
        print ( "\n you didnt chose from the options \n \n" ) 




# Question three. Which manufacturer made seatbelts?
question_3 = True
while ( question_3 ):

    correct_answer  = [ "c", "volvo", "3" ]
    incorrect_answer = [ "toyota", "ford", "hyundai", "a", "b", "d", "1", "2", "4" ]
    question = input ( "Which manufacturer made seatbelts? \n A) Toyota \n B) Ford \n C) Volvo \n D) Hyundai \n \n" ).lower().strip()

    if check ( question, correct_answer, incorrect_answer ):
       
        if question in correct_answer :
            print ("\n You got the right awnser! \n")
            question_3 = False
            points += 1
        else: 
            print ("\n You got the wrong answer!\n")
        question_1 = False
    else:
        print ("\n you didnt chose from the options \n \n") 




# Question four. What car company did Kiichiro Toyoda create?
question_4 = True
while ( question_4 ):

    correct_answer  = [ "b", "toyota", "2" ]
    incorrect_answer = [ "opel", "nissan", "peugeot", "a", "c", "d", "1", "3", "4" ]
    question = input ( "What car company did Kiichiro Toyoda create? \n A) Opel \n B) Toyota \n C) Nissan \n D) Peugeot \n \n" ).lower().strip()

    if check ( question, correct_answer, incorrect_answer ):
       
        if question in correct_answer :
            print ( "\n You got the right awnser! \n" )
            question_4 = False
            points += 1

        else: 
            print ( "\n You got the wrong answer!\n" )
        question_1 = False
    else:
        print ( "\n you didnt chose from the options \n \n" ) 




# Question five. What car company owns Bugatti?
question_5 = True
while ( question_5 ):

    correct_answer  = [ "d", "volkswagen", "4" ]
    incorrect_answer = [ "lada", "lotus", "mclaren", "a", "b", "b", "1", "2", "3" ]
    question = input ( "What car company owns Bugatti? \n A) Lada \n B) Lotus \n C) Mclaren \n D) Volkswagen \n \n" ).lower().strip()

    if check ( question, correct_answer, incorrect_answer ):
       
        if question in correct_answer :
            print ( "\n You got the right awnser! \n" )
            question_5 = False
            points += 1

        else: 
            print ( "\n You got the wrong answer!\n" )
        question_1 = False
    else:
        print ( "\n you didnt chose from the options \n \n" )    




# Question six. What did Lamborghini make before cars?
question_6 = True
while ( question_6 ):

    correct_answer  = [ "b", "tractors", "2" ]
    incorrect_answer = [ "a", "c", "d", "trucks", "motorcycles", "airplanes", "1", "3", "4" ]
    question = input ( "What did Lamborghini make before cars? \n A) Trucks \n B) Tractors \n C) Motorcycles\n D) Airplanes \n \n" ).lower().strip()

    if check ( question, correct_answer, incorrect_answer ):
       
        if question in correct_answer :
            print ( "\n You got the right awnser! \n" )
            question_6 = False
            points += 1

        else: 
            print ( "\n You got the wrong answer!\n" )
        question_1 = False
    else:
        print ( "\n you didnt chose from the options \n \n" ) 




# Question seven. What food item does Volkswagen make?
question_7 = True
while ( question_7 ):

    correct_answer  = [ "a", "currywurst", "1" ]
    incorrect_answer = [ "b", "c", "d", "burgers", "yorkshire pudding", "pies", "2", "3", "4" ]
    question = input ( "What food item does Volkswagen make? \n A) Currywurst \n B) Burgers \n C) Yorkshire pudding \n D) Pies \n \n" ).lower().strip()

    if check ( question, correct_answer, incorrect_answer ):
       
        if question in correct_answer :
            print ( "\n You got the right awnser! \n" )
            question_7 = False
            points += 1

        else: 
            print ( "\n You got the wrong answer!\n" )
        question_7 = False
    else:
        print ( "\n you didnt chose from the options \n \n" )





# Question eight. What car company does Elon Musk own?
question_8 = True
while ( question_8 ):

    correct_answer  = [ "c", "tesla", "3" ]
    incorrect_answer = [ "b", "a", "d", "lucid air", "rivian", "byd", "2", "1", "4" ]
    question = input ( "What car company does Elon Musk own? \n A) Lucid air \n B) Rivian \n C) Tesla \n D) BYD \n \n" ).lower().strip()

    if check ( question, correct_answer, incorrect_answer ):
       
        if question in correct_answer :
            print ( "\n You got the right awnser! \n" )
            question_8 = False
            points += 1

        else: 
            print ( "\n You got the wrong answer!\n" )
        question_8 = False
    else:
        print ( "\n you didnt chose from the options \n \n" )





# Question nine. Which animal features in the logo for Lamborghini?
question_9= True
while ( question_9 ):

    correct_answer  = [ "a", "bull", "1" ]
    incorrect_answer = [ "b", "c", "d", "horse", "cow", "frog", "2", "3", "4" ]
    question = input ( "Which animal features in the logo for Lamborghini? \n A) Bull \n B) Horse \n C) Cow \n D) Frog \n \n" ).lower().strip()

    if check ( question, correct_answer, incorrect_answer ):
       
        if question in correct_answer :
            print ( "\n You got the right awnser! \n" )
            question_9 = False
            points += 1

        else: 
            print ( "\n You got the wrong answer!\n" )
        question_1 = False
    else:
        print ( "\n you didnt chose from the options \n \n" )




# Question ten. Which iconic car manufacturer also made airplane engines?
question_10 = True
while ( question_10 ):

    correct_answer  = [ "d" , "rolls royce " , "rr" , "rolls" , "royce", "4" ]
    incorrect_answer = [ "b", "c", "a", "acura", "honda", "suzuki", "2", "3", "1" ]
    question = input ( "Which iconic car manufacturer also made airplane engines? \n A) Acura \n B) Honda \n C) Suzuki \n D) Rolls Royce \n \n" ).lower().strip()

    if check ( question, correct_answer, incorrect_answer ):
       
        if question in correct_answer :
            print ( "\n You got the right awnser! \n" )
            question_10 = False
            points += 1

        else: 
            print ( "\n You got the wrong answer!\n" )
        question_1 = False
    else:
        print ( "\n you didnt chose from the options \n \n" )




# Question eleven. What is the world's all-time bestselling car?
question_11 = True
while ( question_11 ):

    correct_answer  = [ "c" , "toyota corolla" , "corolla " , "toyota", "3" ]
    incorrect_answer = [ "b", "d", "a", "honda civic", "honda", "civic", "chevrolet camero", "chevrolet", "camero", "dodge dart", "dodge", "dart", "1", "2", "4" ]
    question = input ( "What is the world's all-time bestselling car?  \n A) Honda Civic \n B) Chevrolet Camero \n C) Toyota Corolla \n D) Dodge Dart \n \n" ).lower().strip()

    if check ( question, correct_answer, incorrect_answer ):
       
        if question in correct_answer :
            print ( "\n You got the right awnser! \n" )
            question_11 = False
            points += 1

        else: 
            print ( "\n You got the wrong answer!\n" )
        question_1 = False
    else:
        print ( "\n you didnt chose from the options \n \n" )




# Telling user how many they got right out of eleven questions
print ( "\n Congrats you got {} out of 11 right good job. \n".format( points ) )

# Remove one point if user didn't want to play
# There is only one if statement beacause this print statement will only show up if they pressed no or b when they were asked if they wanted to play this quiz or not
if wants_to_play == "no" or wants_to_play == "b":
    print ( "I took away one point because you said no to playing the quiz. IT TOOK ME AGES." )

# Thanking user for playing the quiz
# Name variable so that the code says bye to the person who is playing the quiz
print ( "\n Bye {} thank you for participating in my little fun quiz, I will see you in my next quiz, bye \n".format(name) )

# Author credentials
print ( "\n Created by Gurshaan Singh Bansal \n published in 2023 \n" )
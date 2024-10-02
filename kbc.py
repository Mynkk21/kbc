# KON BNEGA CROREPATI GAME

questions=[
          
 [
     "Question 1 What is the world's largest living structure, according to the Guinness World Records?",
     "A) The Great Barrier Reef" , "B) The Amazon Rainforest" , "C) The Grand Canyon" , "D) The Great Wall of China" ,1
 ],
 [
     "Question 2 Which of the following planets in our solar system is known as the \"Red Planet\"?",
     "A) Earth" , "B) Mars" , "C) Jupiter" , "D) Saturn" ,2
 ],
 [
     "Question 3 Who is the author of the famous novel \"To Kill a Mockingbird\"?",
     "A) F. Scott Fitzgerald" , "B) Harper Lee" , "C) Jane Austen" , "D) J.K. Rowling",2
 ],
 [
     "Question 4 Which of the following Indian freedom fighters was known as the \"Lion of the Punjab\"?",
     "A) Mahatma Gandhi" , "B) Bhagat Singh" , "C) Lala Lajpat Rai" , "D) Subhas Chandra Bose",3
 ],
 [
     "Question 5 What is the chemical symbol for gold?",
     "A) Ag" , "B) Au" , "C) Hg" , "D) Pb",2
 ],
 [
     "Question 6 Which of the following musical instruments is often associated with the Indian classical music legend Ravi Shankar?",
     "A) Sitar" , "B) Tabla"  , "C) Tanpura",  "D) Flute",1
 ],
 [
     "Question 7 Who is the founder of the popular social media platform Facebook?",
     "A) Mark Zuckerberg" ,"B) Steve Jobs" ,"C) Bill Gates", "D) Elon Musk",1
 ],
 [
     "Question 8 What is the capital city of Australia?",
     "A) Sydney", "B) Melbourne", "C) Canberra", "D) Perth",1
 ],
 [
     "Question 9 Which of the following ancient Indian empires was founded by Chandragupta Maurya?",
     "A) Mauryan Empire" , "B) Gupta Empire" , "C) Vijayanagara Empire" , "D) Mughal Empire",1
 ],
 [
     "Question 10 What is the process by which water moves through a plant, from the roots to the leaves, and is then released into the air as water vapor?",
     "A) Respiration" , "B) Photosynthesis" , "C) Transpiration" , "D) Evaporation",3
 ],
 [
     "Question 11 Who is the lead singer of the popular rock band Queen?",
     "A) Freddie Mercury" , "B) Brian May" , "C) Roger Taylor" , "D) John Deacon",1
 ],
 [
     "Question 12 Which of the following Indian cities is known as the \"Pink City\"?",
     "A) Jaipur", "B) Jodhpur","C) Udaipur", "D) Bikaner",1
 ],
 [
     "Question 13 What is the largest mammal on Earth?",
     "A) Elephant" , "B) Blue whale" , "C) Hippopotamus" , "D) Rhinoceros",2
 ],
 [
     "Question 14 Who is the author of the famous Indian epic poem \"Ramayana\"?",
     "A) Valmiki" , "B) Vyasa", "C) Kalidasa" , "D) Tulsidas",1
 ],
 [
     "Question 15 Which of the following Indian states is known as the \"Land of Five Rivers\"?",
     "A) Punjab" , "B) Haryana" , "C) Uttar Pradesh" , "D) Rajasthan",1
 ],
 [
     "Question 16 What is the process by which the Earth's plates move and change, causing earthquakes and volcanic eruptions?",
     "A) Weathering" , "B) Erosion" , "C) Plate tectonics" , "D) Glaciation",3
 ],
 [
     "Question 17 Who is the founder of the popular Indian company Tata Group?",
     "A) Jamsetji Tata" , "B) Ratan Tata" , "C) JRD Tata" , "D) Cyrus Mistry",1
 ],
          
]
# money winning amount 
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,7500000,10000000,75000000]
money=0
# for y in range(0,16):
#        y=questions
#        print(f"{questions[0]}")
for i in range(0,len(questions)):
        x=questions[i]
        # print(f"\nQuestions.{questions[0]}")
        print(f"\n\nQuestion for Rs.{levels[i]}")
        print(f"a.{x[1]}     b. {x[2]}")
        print(f"c.{x[3]}     d. {x[4]}")
        reply=int(input("Enter the answer between 1-4 or 0 to quit the game:\n"))
        if (reply==0):
                money= levels[i-1]
                break
        if (reply==questions[-1]):
                print(f"Correct answer , You have won Rs. {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
               money=320000
        elif(i==14):
               money==7500000
        else:
               print("You choose wrong answer , Better luck next time ")
               break
        print(f"You Take Money home {money}")       
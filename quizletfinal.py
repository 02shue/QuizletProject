"""
Quizlet Questionnaire Project - Minsuk "Sean" Hue and Sangsoo "Andy" Lim
Completed December 23, 2022

"""

#This code takes a Quizlet URL and creates a questionnaire test for the users.
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
#Importing necessary modules for web scraping and randomization of the flashcards.

def main():
    """
    This is the main python code for the Quizlet Questionnaire for the user to input the answer after receiving the "word" or "question".
    The user will input the "definition" or "answer" to the question, where the python code will keep track of the correct and incorrect answers.
    The user is able to input 3 different types of answer.
        - (1) "end" will exit the questionnaire and give back the score for the answered questions.
        - (2) "hint" will skip the question, give you the correct answer, and mark it as incorrect on the final score but still have the opportunity to answer again later.
        - (3) the given answer will be assessed to see if the answer is correct or incorrect, adding to the final score if correct and repeated later on if incorrect.

    """
   
    load()

    print("Type 'end' to exit.\nIf wrong, question will be repeated.\nType 'hint', if you do not know & wish to skip.\n")

    f = open("data.txt", "r")
    lib = dict()
    total = 0

    #This code takes the txt file that was created in the load() and creates a dictionary with the question/word as the key and the answer/defintion as the value
    while True:
        question = f.readline()
        if not question:
            break
        else:
            total += 1
        lib[question] = f.readline()
    
    #This code is the questionnaire part of the code, where the word will be given and the code will wait for the user input
    score = 0
    while (len(lib) >= 0):
        key = random.choice(list(lib))
        print("Question: " + key)
        user_def = input("definition: ")
        if user_def == str(lib[key]).strip("\n"):
            lib.pop(key)
            score += 1
            print("Correct!")
            continue
        elif user_def == "hint":
            print(lib[key])
            continue
        elif user_def == "end":
            break
        else:
            print("Wrong. Correct answer: " + lib[key])

        
    print("\nfinal score: " + str(score) + "/" + str(total))



def load():
    """
    This is the code for the web scraping of the Quizlet URL.
    The user will input their url for the Quizlet that they want to study for. Then, the code will create a txt file containing all the words and definition for the Quizlet.
    This txt file will be later used in the "main()" for the questionnaire.
    The code will first open the URL and execute a script to scroll to the bottom of the Quizlet to allow all of the elements on the page to load.
    Then, the code will find all the elements with a class name of "TermText.notranslate.lang-en", which is the class for the words and defintion on Quizlet. 
    The code will then compile each WebElement and make them into the "word" and "definition" strings, as shown on Quizlet, which are all stored on the txt fie.
    At the end, the code will then close the browser and the txt file will be ready to be used in "main()".

    """
    f = open("data.txt", "w")
    user_url = input("Quizlet Link: ")
    #Example URL: "https://quizlet.com/260245848/short-flash-cards/"
    user_browser = webdriver.Chrome()
    user_browser.get(user_url)

    #This code scrolls the window down to the bottom of the page to allow all WebElements to load
    user_browser.execute_script("window.scrollBy(0, document.body.scrollHeight || document.documentElement.scrollHeight)")
   
   #This code finds all the WebElements with this class name, which are unique to the word and defintion of the flashcards.
    user_all = user_browser.find_elements(By.CLASS_NAME, "TermText.notranslate.lang-en")

    #Writes/converts all the WebElements onto the txt file.
    for i in range(len(user_all)):
        if i % 2 == 0:
            f.write(user_all[i].text.strip("\n") + "\n")
        else:
            f.write(user_all[i].text.strip("\n") + "\n")

    f.close()
    user_browser.close()


if '__main__':
    main()
import answers as ans
import about as abt
from termcolor import colored
import os

aux = "_"

opt0 = colored('(0)READ ABOUT.', 'yellow')
opt1 = colored('(1)READ THE QUESTIONS.', 'yellow')
opt2 = colored('(2)VIEW ANSWERS.', 'yellow')

print(f"{aux*50} \n\n WELCOME TO NATIONAL ENERGY AND CLIMATE PLANS (EU). \n\n {aux*50} \n\n WHAT DO YOU WANT TO ACCOMPLISH TODAY? \n TYPE ON YOUR KEYBOARD AN OPTION IN THE MENU BELOW, WHICH IS IN PARENTHESES AT THE BEGINNING OF THE OPTION. \n\n{opt0} \n\n{opt1} \n\n{opt2}\n\n")

answer = int(input('ENTER YOUR ANSWER: '))
while answer < 0 | answer > 2:
    print(f"Oooooops, you must enter a valid option between 0 and 3. \n\n{opt0} \n\n{opt1} \n\n{opt2}\n\n")
    answer = int(input('ENTER YOUR ANSWER: '))
else:
    while True:
        if answer == 0:
            abt.about()
        elif answer == 1:
            print(abt.b)
        elif answer == 2:
            while True:
                print('Select one question, typing on your keyboard. \n\n(0)for question 0. \n(1)for question 1. \n(2)for question 2. \n(3)for questio 3. \n(4)for question4. \n(5)for question 5. \n(6)for question6. \n(7)for question 7.')
                question = int(input('ENTER YOUR ANSWER: '))
                while question < 0 | question > 7:
                    print('Oooooops, you must enter a valid option between 0 and 7.')
                    question = int(input('ENTER YOUR ANSWER: '))
                else:
                    if question == 0: 
                        q0 = ans.listEngagement()
                        print(q0)
                    if question == 1: 
                        q1 = ans.engagementsforcountry()
                        print(q1)
                    if question == 2: 
                        q2 = ans.percentageEngagementforcountry()
                        print(q2)
                    if question == 3: 
                        q3 = ans.contryforproposalEE()
                        print(q3)
                    if question == 4: 
                        q4 = ans.contryforproposalD()
                        print(q4)
                    if question == 5: 
                        q5 = ans.contryforproposalES()
                        print(q5)
                    if question == 6: 
                        q6 = ans.contryforproposalI()
                        print(q6)
                    if question == 7: 
                        q7 = ans.contryforproposalRI()
                        print(q7)
                    if input('Do you wish to continue? Y for yes and N for NO:-') == "N": break
        
        if input('Do you wish to continue? Y for yes and N for NO:-') == "Y":
            os.system('cls')
            print(f"\n\n{opt0} \n\n{opt1} \n\n{opt2}\n\n")
            answer = int(input('ENTER YOUR ANSWER: '))
            if answer == 0:
                abt.about()
            elif answer == 1:
                print(abt.b)
            elif answer == 2:
                while True:
                    print('Select one question, typing on your keyboard. \n\n(0)for question 0. \n(1)for question 1. \n(2)for question 2. \n(3)for questio 3. \n(4)for question4. \n(5)for question 5. \n(6)for question6. \n(7)for question 7.')
                    question = int(input('ENTER YOUR ANSWER: '))
                    while question < 0 | question > 7:
                        print('Oooooops, you must enter a valid option between 0 and 7.')
                        question = int(input('ENTER YOUR ANSWER: '))
                    else:
                        if question == 0: 
                            q0 = ans.listEngagement()
                            print(q0)
                        if question == 1: 
                            q1 = ans.engagementsforcountry()
                            print(q1)
                        if question == 2: 
                            q2 = ans.percentageEngagementforcountry()
                            print(q2)
                        if question == 3: 
                            q3 = ans.contryforproposalEE()
                            print(q3)
                        if question == 4: 
                            q4 = ans.contryforproposalD()
                            print(q4)
                        if question == 5: 
                            q5 = ans.contryforproposalES()
                            print(q5)
                        if question == 6: 
                            q6 = ans.contryforproposalI()
                            print(q6)
                        if question == 7: 
                            q7 = ans.contryforproposalRI()
                            print(q7)
                        if input('Do you wish to continue? Y for yes and N for NO:-') == "N": break
        else: break
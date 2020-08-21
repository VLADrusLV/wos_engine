# First setup my bot for learning English
# Close file
import sys
import pandas as pd
import random

def v2_form_test(data, index):

    v2_your_answer = input(f"Do you know past simple form {data.loc[index]['V1']}? >>> ")
    v2_correct = data.loc[i]['V2']

    if v2_your_answer == v2_correct:

        print(f"You are right!. Really the past simple form {data.loc[index]['V1']} is {v2_your_answer}")
        return True

    else:

        print(f"You are wrong. The past simple form {data.loc[index]['V1']} is {data.loc[index]['V2']}")
        return False

print("Hi!\nI'm  your English helper.\nI know all irregular verbs I can help you.")
name = input("What are you name? >>> ")
first_answer = input(f"Ok {name}. Are you ready? y/n >>> ").strip().lower()

start = None

if first_answer == 'y':
    start = True
elif first_answer == 'n':
    print("See you later. Goodbye")
    exit()

if start:
    right_answer = 0
    wrong_answer = 0
    name_data_file = sys.argv[1]
    data = pd.read_csv(name_data_file)
    df_len = len(data)
    print("Good! You are ready. Let's start")

    while start:
        i = random.randint(0, df_len)
        result = v2_form_test(data, i)
        if result:
            right_answer += 1
        else:
            wrong_answer += 1
        print(f'Your balance {right_answer}/{wrong_answer}')
        while not result:
            print('Try again')
            result = v2_form_test(data, i)

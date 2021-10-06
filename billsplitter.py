import random

friends_dictionary = {}
print('Enter the number of friends joining (including you):')
number_of_friends = int(input())
print()
if number_of_friends <= 0:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for _ in range(number_of_friends):
        friend = input()
        friends_dictionary.update({friend: 0})
    print()
    print('Enter the total bill value:')
    bill = float(input())
    print()
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    lucky_one = ""
    number_to_split = number_of_friends
    if answer == 'Yes':
        print()
        random.seed()
        lucky_one = random.choice(list(friends_dictionary.keys()))
        print(f'{lucky_one} is the lucky one!')
        number_to_split -= 1
    else:
        print()
        print('No one is going to be lucky')
    split = round(bill / number_to_split, 2)
    friends_dictionary = dict.fromkeys(friends_dictionary.keys(), split)
    if len(lucky_one) > 0:
        friends_dictionary.update({lucky_one: 0})
    print()
    print(friends_dictionary)


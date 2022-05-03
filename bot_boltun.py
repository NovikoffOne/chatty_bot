bot_name = 'Lil Loader'
birth_year = '03.05.2022'

def hallo():
    print(f'Sap boy, my name is {bot_name}!')
    print(f'I was created in {birth_year}.')

def wat_you_name():
    your_name = input('Plese, remind me your name. \n> ')
    print(f'What a great name you have, {your_name}!')

def guess_the_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')
    rem3 = float(input('> '))
    rem5 = float(input('> '))
    rem7 = float(input('> '))
    your_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print(f'Your age is {int(your_age)}; that\'s a good time to start programming!')

def count_number():
    number = int(input())
    i = 0
    while i < number:
        print(i)
        i += 1

def test():
    print("Let's test your programming knowledge.")
    print('Why do we use methods?')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')
    ans = True
    while ans:
        answer = int(input())
        if answer == 2:
            print('Completed, have a nice day!')
            ans = False
        else:
            print('Please try again')



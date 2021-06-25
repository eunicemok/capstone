# My game is a virtual escape room, featuring the mysterious murder of DR FRANCIS.  At various crimescenes,
# the player must collect clues and interact with the coded environment to determine the real murderer.

import random
import time


def intro():
    print('It is a dark and stormy night and you are enjoying a cup of tea by the fire.')
    # using the time function to add suspense
    time.sleep(3)
    print('Your phone begins to ring.')
    time.sleep(2)
    print('It\'s the police station.')
    time.sleep(2)
    print('\"We need your help.\"')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.', end='')
    time.sleep(1)
    print('.')
    time.sleep(1)
    print('\"There\'s been a murder.\"')
    print('Press enter to continue.')

    input()


def casefile():
    print(
        'On February 29th 20XX, DR. JAMES FRANCIS was found dead in his locked office at 11:39 pm by a colleague.  Test results show that he had been dead for only 9 minutes.')
    print('''MR.FRANCIS was known for his great benevolence with his patients.
But he was also extremely mysterious, anti-social, and even described as somewhat of a recluse,
and like any man, he had his enemies...''')

    print('''You are handed a file with the possible suspects.
(Press enter to open)''')
    input()
    print('''SUSPECTS:
OPHELIA LANCASTER: The mother of one of DR FRANCIS' first patients, LUNA, who passed away in 20XX from terminal cancer.
DR TIMOTHY CALLAWAY: Colleague of DR FRANCIS and the only other doctor with keys to his office.
EMMA KARLS: DR FRANCIS' ex-wife who remained financially dependent on him for 5 years following their divorce.''')


def ask(answer):
    if str(answer).lower().startswith('y'):
        return True
    else:
        return False


# Here the game begins with three puzzles at three different scenes

def houseSetUp():
    print('Your first stop is the doctor\'s house.')
    print('''The moment you walk, you notice a strong floral scent.
You walk into the bedroom, and you are shocked to see that the walls are lined with various articles and newspapers.''')
    input()
    print('''One of them catches your eye, it\'s a letter...
James,
Just wanted to let you know I\'m off to visit
my mother in the Hamptons.
I\'m taking Scott with me so don\'t worry,
Take care of yourself James.
Tell Abby I said hello.
- em''')

    input()
    print('''Further along, you notice ripped up newspapers, and notes.
One of them is pinned on the wall next to his bed.''')
    print('''On it is scribbled:
there is nO hoPe for tHE unLovable.''')

    input()
    print('You can see some writing below it, but it doesn\'t seem visible in the light.')
    input()

    print('On his desk is a red ring with an inscription in it, a golden lock, and a small locked chest.')
    input()


# Selecting and reducing options works
def choiceOne(lst):
    print('''What do you do next?:''')
    print('\n'.join(lst))

    keepgoing = True
    while keepgoing:
        print('Please choose one of the options (type 1,2,3)')

        ans = input()
        if ans == '1' or ans == '2' or ans == '3':
            return ans
        else:
            continue


def keyBox():
    print()
    print('''You open the box with the key. In it is another ring, identical to the other.''')


def darkArticle():
    print()
    print('''You turn off the lights and look at the article. FRANCIS\' note continues
there is nO hoPe for tHE unLovable...
I Am''')


def redRing():
    print()
    print('''Carefully, you tilt the red ring to get a look at what\'s written inside. It writes:
To my one and only love.''')


def ophelia():
    print('Next you decide to go to OPHELIA LANCASTER\'s home to find more clues.')
    print('Although the house is fairly old, the rooms are clean and well kept.')
    input()
    print('''You see notes posted on the calender.''')
    input()
    for x in range(3):
        print('-' * 7, end='')
        print(' ' * 5, end='')

    print()
    print('Dentist' + ' ' * 3 + 'Anniversary' + ' ' * 4 + 'Movie')
    print('appointment' + ' ' * 2 + 'Dinner' + ' ' * 6 + 'Night')

    for x in range(3):
        print('-' * 7, end='')
        print(' ' * 5, end='')
    input()
    print('''You continue into the master bedroom and you find
several pieces of paper on a night desk.''')
    input()
    print('''
                         |Receipt 2/20/XX  |
  __________________     | Steak... $XX    |
 |1 Adm. The Affair|     | XX... $XX       |
 |2/29/20XX 11:30pm|     | Lamb...$X2      |
 |_________________|     | XX... $XX       |            
                         | XX... $XX       |
    _______________      | XX... $29       |
    |MOVIE COUPON!!|     | Wine... $XX     |
    |FOR WATCHING  |     |                 |
    |  Unlovable   |     |                 |
    |  The Affair  |
    |   Revenge    |
    |______________|
 ''')
    input()


def doctor():
    print('Next is DR CALLAWAY\'s home.')
    print('The home is suprisingly empty, with little furniture.')
    input()
    print('''There are blankets strewn across the coach
surrounded by empty takeout boxes.''')
    input()
    print('''You walk into the bedroom and see dust has been
collecting on the bed and a half used bottle of flowery perfume is left on the table.
Most notably you see a box poking under the bed.''')
    input()
    print('It\'s a chest.')
    input()
    print('''You try prying it open but its locked securely by a mechanic lock
with a 4 number key code.
It seems you will have to look around for some clues.
''')
    input()
    print('''On the bookshelf you see three poems.  You suspect the code may be in one of them:
1. A Dream Within a Dream by J. Alfred Prufrock
2. Unlovable by Timothy Y. Callaway
3. Annabel Lee by Edgar A. Poe
''')

    print('Which do you choese?')
    keepgoing = True
    while keepgoing:
        print('Please choose one of the poems to read. (type 1,2,3)')
        choice = input()
        if choice == '1' or choice == '2' or choice == '3':
            if choice == '1':
                print('''I have seen them riding seaward on the waves
    Combing the white hair of the waves blown back
    When the wind blows the water white and black.
    We have lingered in the chambers of the sea
    By sea-girls wreathed with seaweed red and brown
    Till human voices wake us, and we drown.''')


            elif choice == '3':
                print('''For the moon never beams,
    without bringing me dreams
    Of the beautiful Annabel Lee;
    And the stars never rise, but I feel the bright eyes
    Of the beautiful Annabel Lee;
    And so, all the night-tide, I lie down by the side
    Of my darling—my darling—my life and my bride,
    In her sepulchre there by the sea—
    In her tomb by the sounding sea.''')
            else:
                print('''Six crows sang by my bed
    When I dreamt alone of my lover
    She was standing on the edge of a shore
    White blouse drifting in the wind,
    Then one man came, white coat to match her dress
    Took her far away from me
    I cried for her to no avail
    I beat the sand feeling my fourth finger bruise
    Until I threw our vows into the waves
    Three crows squawk
    The anthem of the unlovable''')

        print('''Would you like to return to the chest now?''')
        ask = input()
        if (ask.lower().startswith('y')):
            keepgoing = False

    code = ['6', '1', '4', '3']
    # answer not right yet
    allright = False

    # reiterate until Guess == code
    while allright == False:
        # Get the guess
        print('What do you believe is the code? (Place spaces between each number)')
        guess = input()
        realguess = list(guess.split(' '))
        if len(realguess) != 4:
            print('The code must be 4 numbers!')
        else:
            for number in range(len(code)):
                if realguess[number] != code[number]:
                    allright = False
                    print('Your guess, %s %s %s %s was incorrect' % (
                    realguess[0], realguess[1], realguess[2], realguess[3]))
                    break
                else:
                    allright = True

    if allright:
        guess.split(' ')
        print('Your guess, %s %s %s %s was correct' % (realguess[0], realguess[1], realguess[2], realguess[3]))
        input()
        print('You open the box and inside you find piles of documents.')
        input()
        print('You grab the top folder and open it.')
        input()
        print('Its a divorce paper signed by TIMOTHY and ABBY CALLAWAY')

    input()


def answer():
    print('''Finally you return to the department where the captain
of the police is waiting for you anxiously.''')
    input()
    print('''So who was the killer?
1) O. LANCASTER 2) T. CALLAWAY 3) E. KARLS?''')

    final = input()
    if final == '2':
        print('CONGRATULATIONS. YOU HAVE SOLVED DR FRANCIS\' MURDER')

    elif final == '1':
        print('''OPHELIA LANCASTER was not the murderer.
Better luck next time!''')
    else:
        print('''EMMA KARLS was not the murderer.
Better luck next time!''')


intro()
casefile()

print('Will you take this case? (type yes or no)')
response = input()

notcorrect = True
if ask(response):
    houseSetUp()
    choices = ['1. Try opening the box with the key',
               '2. Look at the article',
               '3. Read whats inscribed in the ring']
    while len(choices) != 0:
        value = choiceOne(choices)
        if value == '1':
            choices.remove('1. Try opening the box with the key')
            keyBox()

        elif value == '2':
            choices.remove('2. Look at the article')
            darkArticle()

        else:
            choices.remove('3. Read whats inscribed in the ring')
            redRing()

    ophelia()
    doctor()
    answer()








else:
    print('Goodbye, then')

# If you were curious as to what the hidden hints were, here's a list :)
# The keys things to remember during the case is which suspect has the strongest motive.

# First, at Dr. Francis' home, the letter left by 'em' which we can assume is Emma Karls,
# his ex-wife. She tells Francis that she's leaving to the Hamptons so we can immediately eliminate her as a suspect.

# !Its also important to remember that she mentions a woman named Abby.

# When given the three options we find that Dr.Francis has a pair of rings and a letter with the hidden word Ophelia.

# Given this information, you may suspect Ophelia, but when we go to her house, we find a movie ticket for the same time
# as the murder.  Ophelia was not present for the murder.

# Finally, at Dr.Callaway's place, there is a bottle of floral perfume, referring to the floral scent in Dr.Francis' place.
# The divorce papers confirm Dr.Callaway's possible motive.

# Dr.Francis and Dr.Callaway's wife, Abby were having an affair leading to their subsequent divorce.
# Dr.Callaway, in failing mental health, then murdered Dr.Francis in revenge.

# Thank you so much for playing!





















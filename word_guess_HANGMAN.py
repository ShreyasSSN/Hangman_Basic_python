import random
def replacer(char, word, Guessed_answer):
    word = list(word)
    Guessed_answer = list(Guessed_answer)
    indices = [i for i, x in enumerate(word) if x == char]
    for x in indices:
        Guessed_answer[x] = char
    New_answer = ''.join(Guessed_answer)
    return New_answer

print('Guess the color I\'m thinking..!!!')
words = ['violet', 'Indigo', 'Green', 'Blue',
         'Orange', 'Red', 'Yellow', 'Cyan',
         'Magenta', 'Pink', 'White', 'Black']
flag = 0
word = random.choice(words)
Guessed_answer = ''.join(['_' for x in word])
print(Guessed_answer)
n = len(word)
print('You have',n+2,'guesses')
Guesses = n+2
for i in range(n+2):
    char = input('Guess a charater: ')
    char = char.lower()
    if char in Guessed_answer.lower():
        print('Already Guessed. Try another')
    elif char in word.lower():
        print('Yay... Correct..!!!')
        Guessed_answer= replacer(char.lower(), word.lower(), Guessed_answer)
        print(Guessed_answer)
        if '_' not in Guessed_answer:
            flag = 1
            break
    else:
        Guesses -= 1
        print('Try Again\n\nRemaining Guesses:  ',Guesses)

if flag != 1 and Guesses == 0:
    print('Sorry, You lost')
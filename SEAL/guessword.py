import random
words = """Condition,Administrator,List,Mister,Python,Game,Guess,Like,
,Player,Seal,Project,Computer,Science,Instrumentation,Electronics,
,Apply,Plug,Vocabulary,Nickel,Strontium,Germanium,Helium,Neon,
,Yttrium,Tungsten,Petrification,Astronaut"""


def lister():
    word_list = words.split(",")
    for word in word_list:
        if word == "\n" or word == " ":
            word_list.remove(word)
    return word_list


def names():
    p1 = input("Enter your name player 1: ")
    p2 = input("Enter your name player 2: ")
    return p1, p2


def chance(p1, p2, i):
    player = p1
    if i % 2 == 0:
        player = p2
    return player


def wordder():
    word = random.choice(lister())
    jumbled = "".join(random.sample(word, len(word)))
    print(f"Un-jumble: {jumbled}")
    lister().remove(word)
    if len(lister()) == 1:
        lister()
    return word, jumbled


def guesser(chance, p1, p2):
    if chance == p1:
        guess = input(f"Enter your answer, {p1} : ")
    else:
        guess = input(f"Enter your answer, {p2} : ")
    return guess


def checker(word, guess_word):
    if word.lower() == guess_word.lower():
        return True
    else:
        return False


def main(des):
    p1, p2 = names()
    i, j, result = 1, 1, 0
    word, jumbled = wordder()
    while des == 1:
        player = chance(p1, p2, i)
        if result == 1 or (j % 2 == 0 and result == 0 and player == p1):
            word, jumbled = wordder()
            j, result = 1, 0
        guess_word = guesser(chance=player, p1=p1, p2=p2)
        result = checker(word, guess_word)
        if result == 1:
            des, i = int(input(f"You Have won, {player}. Would you like to play again? (1-Yes/0-NO) : ")), 1
            print()
        else:
            if j % 2 == 0:
                des = int(input("Both Lost, Will you keep going? (1-Yes/0-NO) : "))
                print()
                if des == 0:
                    print(f"The real word was - {word}")
                    des = int(input("Would you like to try again? (1-Yes/0-NO) : "))
                    print()
                    if des == 1:
                        j, result = 1, 0
            i += 1
        j += 1


main(des=1)

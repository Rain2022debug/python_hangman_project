import random
#No.1 Game
#youtube="PinkSky"
#print("Subscribe to "+youtube)
#print("Subscribe to {}".format(youtube))
#print(f"Subscribe to {youtube}")

#adj=input("Adj: ")
#madline=f"CS is so {adj}"
#print(madline)

#NO.2 Game
#def people_guess(x):
#    correct_number= random.randint(1,x)
#    while True:
#        guess_number=int(input("Guess: "))
#        if guess_number== correct_number:
#            print("Guess Right! Congratulations!")
#            break
#        elif guess_number< correct_number:  print("Too low")
#        else :  print("Too high")
#    print("Game finish!")

#max_limit=input("Max: ")
#people_guess( int( max_limit ) )

#NO.3 Game Scissors

from words import rwords
import urllib.request
from bs4 import BeautifulSoup
#NO.4 Hangman
def hangman(words):
    print("GAME START!\n")
    #choose a word
    correct_word=random.choice(words)
    #search the meaning
    word_url = "https://www.oxfordlearnersdictionaries.com/us/definition/english/"+ \
        correct_word + "?q=" + correct_word
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"}
    req=urllib.request.Request(word_url,headers=header)
    res=urllib.request.urlopen(req)
    long_txt=res.read().decode('UTF-8')
    soup = BeautifulSoup(long_txt, 'html.parser')
    meaning=soup.find("span","def")
    #show the meaning as a hint
    if meaning:
        print(meaning.text)
    # store all correct alpha
    alpha_set=set(correct_word)
    used_alpha=[]
    while len(alpha_set)>0:
        show_list=[w if w in used_alpha else '-' for w in correct_word ]
        print( ''.join( show_list ) )
        print("Start Guess!")
        guess_alpha=input("Guess an alpha: ")
        used_alpha.append( guess_alpha )
        alpha_set.discard( guess_alpha )
        print("You have used: ",''.join( used_alpha ))
        print('\n')
    print("Game Over! The word is "+ correct_word )

hangman(rwords)

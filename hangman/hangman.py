import random

ls=['ambivert', 'calcspar', 'deaness', 'entrete', 'gades', 'monkeydom', 'outclimbed', 'outdared', 'pistoleers', 'redbugs',
 'snake-line', 'subrules', 'subtrends', 'torenia', 'unhides']
def play():
    word = random.choice(ls)
    word=word.upper()
    word_completion= "_"*len(word)
    word_as_list = list(word_completion)
    tries=0
    max_try=6
    given=[]
    print("lets play hangman")
    print(word_completion)
    print(try_arr[0])
    while (tries<max_try):
        l=input("guess a letter").upper()
        temp=0
        if(len(l)==1 and l.isalpha()):
            if l in given:
                print("you already entered the alphabet ", l)
            else:
                for i in range (0,len(word)):
                    if(l==word[i]):
                        word_as_list[i]=l
                        word_completion = ''.join(word_as_list)
                        given.append(l)
                        temp=1
                        print(word_completion)

                if '_' not in word_completion:
                        print("yeppi you sucessfully guessed the word")
                        print(word)
                if temp!=1:
                        given.append(l)
                        tries+=1
                        print (try_arr[tries])
    if "_" in word_completion:
        print("sorry you lost it :(")
        print("The word was ", word)


try_arr=[

    '''       |------
       |      |
       |      |
       |      
       |      
       |     
       |
       |
       |
       __
    ''',
    '''|------
       |      |
       |      |
       |      O
       |      
       |     
       |
       |
       |
       __
    ''',
    '''|------
       |      |
       |      |
       |     \O
       |      
       |     
       |
       |
       |
      __
    ''',
        '''|------
           |      |
           |      |
           |     \O/
           |      
           |     
           |
           |
           |
           __
        ''',
        '''|------
           |      |
           |      |
           |     \O/
           |      |
           |     
           |
           |
           |
           __
        ''',
        '''       |------
           |      |
           |      |
           |     \O/
           |      |
           |     / 
           |
           |
           |
           __
        ''',
        '''|------
           |      |
           |      |
           |     \O/
           |      |
           |     / \ 
           |
           |
           |
           __
        ''',
]
play()





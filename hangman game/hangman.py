import random
import words
import stages

chosen_word= random.choice(words.word_lists)
length_of_chosen_word=int(len(chosen_word))
display=("_ "*length_of_chosen_word).split()

end_game=False
lives=6
while not end_game:
    guess= input("Guess a letter: ").lower()
    

    if guess in display:
       print(f"you have already try {guess}. please try another letter.")  
    for position in range(length_of_chosen_word):
            letter= chosen_word[position]
            if letter== guess:
                display[position]=letter

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. you lose a life.")
        lives-=1
        if lives==0:
            end_game=True
            print("you loose!")
             
    print(' '.join(display))

    if "_" not in display:
        end_game=True
        print("you win!")

    print(stages.stages[lives])






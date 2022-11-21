import random
from hangman_art import logo
from hangman_art import stages

from hangman_words import word_list
lives = 6
chosen_word = random.choice(word_list)
display = []
print(logo)
for letter in chosen_word:
  display.append("_")
print(display)
end = False

while not end:
  guess = input("Guess a Letter ")
  if guess in display:
    print(f"You have already guessed {guess}")
  for pos in range(len(chosen_word)):
    letter = chosen_word[pos]
    if letter == guess:
      display[pos]=letter
    
  if guess not in chosen_word:
    print(f"You guessed {guess}, it's not in the word")
    lives-=1
    if lives==0: 
      end = True
      print("You Lose")          
  print(display)
  
  if "_" not in display:
    end = True
    print("You Win") 
  print(stages[lives])
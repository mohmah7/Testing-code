import random
from combinatorics import all_colours

def inconsistent(p, guesses):
   """ the function checks, if a permutation p, i.e. a list of 
colours like p = ['pink', 'yellow', 'green', 'red'] is consistent
with the previous colours. Each previous colour permuation guess[0]
compared (check()) with p has to return the same amount of blacks 
(rightly positioned colours) and whites (right colour at wrong 
position) as the corresponding evaluation (guess[1] in the 
list guesses) """
   for guess in guesses:
      res = check(guess[0], p)
      (rightly_positioned, permutated) = guess[1]
      if res != [rightly_positioned, permutated]:
         return True # inconsistent
   return False # i.e. consistent

def answer_ok(a):
   """ checking of an evaluation given by the human player makes 
sense. 3 blacks and 1 white make no sense for example. """
   (rightly_positioned, permutated) = a
   if (rightly_positioned + permutated > number_of_positions) \
       or (rightly_positioned + permutated < len(colours) - number_of_positions):
      return False
   if rightly_positioned == 3 and permutated == 1:
      return False
   return True

def get_evaluation():
   """ asks the human player for an evaluation """
   show_current_guess(new_guess[0])
   rightly_positioned = int(input("Blacks: "))
   permutated = int(input("Whites: "))
   return (rightly_positioned, permutated)

def new_evaluation(current_colour_choices):
   """ This funtion gets an evaluation of the current guess, checks 
the consistency of this evaluation, adds the guess together with
the evaluation to the list of guesses, shows the previous guesses 
and creates a new guess """
   rightly_positioned, permutated = get_evaluation()
   if rightly_positioned == number_of_positions:
      return(current_colour_choices, (rightly_positioned, permutated))
	
   if not answer_ok((rightly_positioned, permutated)):
      print("Input Error: Sorry, the input makes no sense")
      return(current_colour_choices, (-1, permutated))
   guesses.append((current_colour_choices, (rightly_positioned, permutated)))
   view_guesses()
	
   current_colour_choices = create_new_guess() 
   if not current_colour_choices:
      return(current_colour_choices, (-1, permutated))
   return(current_colour_choices, (rightly_positioned, permutated))


def check(p1, p2):
   """ check() calculates the number of bulls (blacks) and cows (whites)
of two permutations """
   blacks = 0
   whites = 0
   for i in range(len(p1)):
      if p1[i] == p2[i]:
          blacks += 1
      else:
         if p1[i] in p2:
             whites += 1
   return [blacks, whites] 

def create_new_guess():
   """ a new guess is created, which is consistent to the 
previous guesses """
   next_choice = next(permutation_iterator) 
   while inconsistent(next_choice, guesses):
      try:
         next_choice = next(permutation_iterator)
      except StopIteration:
         print("Error: Your answers were inconsistent!")
         return ()
   return next_choice

def show_current_guess(new_guess):
   """ The current guess is printed to stdout """
   print("New Guess: ",end=" ")

   for c in new_guess:
      print(c, end=" ")
   print()

def view_guesses():
   """ The list of all guesses with the corresponding evaluations 
is printed """
   print("Previous Guesses:")
   for guess in guesses:
      guessed_colours = guess[0]
      for c in guessed_colours:
         print(c, end=" ")
      for i in guess[1]:
         print(" %i " % i, end=" ")
      print()

if __name__ == "__main__":
   colours = ["red","green","blue","yellow","orange","pink"]
   guesses = []				
   number_of_positions = 4

   permutation_iterator = all_colours(colours, number_of_positions)
   current_colour_choices = next(permutation_iterator)

   new_guess = (current_colour_choices, (0,0) )
   while (new_guess[1][0] == -1) or (new_guess[1][0] != number_of_positions):
      new_guess = new_evaluation(new_guess[0])

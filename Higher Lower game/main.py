import art
import game_data
import random
print(art.logo)


def game():
  a_dict = random.choice(game_data.data)
  
  game_continue = True
  score = 0
  while game_continue:
    b_dict = random.choice(game_data.data)
    print("Choose who has more followers on instagram.")
    print(f"Compare A = {a_dict['name']} , {a_dict['description']} , {a_dict['country']}")
    print(art.vs)
    print(f"Against B = {b_dict['name']} , {b_dict['description']} , {b_dict['country']}")
  
    a_followers = a_dict['follower_count']
    b_followers = b_dict['follower_count']
  
    choice = input("choose A or B : ").lower()
    
    if (choice == "a" and a_followers > b_followers) or (choice == "b" and a_followers < b_followers) :
      a_dict = b_dict
      score += 1 
      print("Correct answer. \n")
    
    else : 
      game_continue = False
      print(f"Wrong answer. \nYour score is {score}. Better luck next time! ")

game()


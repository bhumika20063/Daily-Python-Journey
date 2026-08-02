from art import logo
from art import vs
import random
from game_data import data

# print(logo)
# item1 = random.choice(data)
# item2 = random.choice(data)
def print_statement(a,b):
    print(f"Compare A: {a['name']}," f"{a['description']}," f" from {a['country']}")
    print(vs)
    print(f"Compare B: {b['name']}," f"{b['description']}," f" from {b['country']}")

# print_statement()

def game():
    is_continue = True
    score = 0
    print(logo)
    while is_continue:
        item1 = random.choice(data)
        item2 = random.choice(data)
        print_statement(item1,item2)
        compare = input("Who has more followers? Type 'A' or 'B': ").lower()
        if item1['follower_count'] > item2['follower_count'] and compare == "a":
            score += 1
            print(100 * "\n")
            print(logo)
            print(f"You're right. Current score: {score}")
        elif item1['follower_count'] < item2['follower_count']and compare == "b":
            score += 1
            print(100 * "\n")
            print(logo)
            print(f"You're right. Current score: {score}")
        elif item1['follower_count'] > item2['follower_count'] and compare == "b":
            print(100 * "\n")
            print(logo)
            print(f"Sorry that's wrong. Final Score: {score}")
            print("Thanks for playing!")
            break
        elif item1['follower_count'] < item2['follower_count'] and compare == "a":
            print(100 * "\n")
            print(logo)
            print(f"Sorry that's wrong. Final Score: {score}")
            print("Thanks for playing!")
            break

game()
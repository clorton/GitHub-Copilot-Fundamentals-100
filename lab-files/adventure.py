"""
This is a simple text-based adventure game.
The player starts in a dark forest and has three options:
1. Go deeper into the forest and discover a treasure chest, increasing the score by 10.
2. Rest by the campfire and regain 20 health.
3. Quit the game, displaying the final score.

The player's health starts at 100 and decreases by 10 with each choice.
The game ends when the player's health reaches 0 or when they choose to quit.
"""

health = 100
score = 0

print("Welcome to the Adventure Game!")
print("You are in a dark forest.")

while health > 0:
    print("\nOptions:")
    print("1. Go deeper into the forest.")
    print("2. Rest by the campfire.")
    print("3. Quit the game.")

    choice = input("Enter your choice: ")

    if choice.isdigit():
        choice = int(choice)
        if choice == 1:
            print("You go farther into the forest and discover a treasure chest!")
            score += 10
        elif choice == 2:
            print("You rest by the campfire and regain 20 health.")
            health += 20
        elif choice == 3:
            print(f"Thanks for playing! Your score: {score}")
            break
        else:
            print("Invalid choice. Try again.")
        health -= 10
        if health <= 0:
            print(f"Game over. Your score: {score}")
    else:
        print("Invalid input. Please enter a valid number.")

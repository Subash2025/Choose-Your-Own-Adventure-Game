def intro():
    name = input("Enter your name: ")
    print(f"Welcome to the mysterious adventurous treasure search game {name}!")
    print("Do you:")
    print("1. Take the path to left.")
    print("2. Take the path to right.")

    choice = int(input("Enter the number: "))

    if choice == 1:
        left_path()
    elif choice == 2:
        right_path()
    else:
        print("Invalid option. Try again.")


def left_path():
    print("You reached a middle of forest lake.")
    print("Do you:")
    print("1. Want to swim across?")
    print("2. Keep walking?")

    choice = int(input("Enter the number: "))

    if choice == 1:
        swim_across()
    elif choice == 2:
        keep_walking()
    else:
        print("Invalid option. Try again.")


def right_path():
    print("You got beat by snake you died. Game over.")


def swim_across():
    print("Congratulation you found the treasure across the river.")
    print("You won!")
   

def keep_walking():
    print("You got attack by goblins you died. Game over.")


if __name__ == "__main__":
    intro()


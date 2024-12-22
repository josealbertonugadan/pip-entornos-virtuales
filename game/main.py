import random


def choose_options():
    """
    Prompts the user to choose between 'piedra', 'papel', or 'tijera' and randomly selects
    an option for the computer.

    Returns:
        tuple: A tuple containing the user's choice and the computer's choice.
        If the user's choice is invalid, returns (None, None).
    """
    options = ("piedra", "papel", "tijera")
    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()

    if user_option not in options:
        print("esa opcion no es valida")
        return None, None

    computer_option = random.choice(options)

    print("User option =>", user_option)
    print("Computer option =>", computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    """
    Determines the winner between the user's choice and the computer's choice based on the
    rules of the game.

    Args:
        user_option (str): The user's choice.
        computer_option (str): The computer's choice.
        user_wins (int): The current number of wins for the user.
        computer_wins (int): The current number of wins for the computer.

    Returns:
        tuple: Updated win counts for the user and the computer.
    """
    if user_option == computer_option:
        print("Empate!")
    elif user_option == "piedra":
        if computer_option == "tijera":
            print("piedra gana a tijera")
            print("user gano!")
            user_wins += 1
        else:
            print("Papel gana a piedra")
            print("computer gano!")
            computer_wins += 1
    elif user_option == "papel":
        if computer_option == "piedra":
            print("papel gana a piedra")
            print("user gano")
            user_wins += 1
        else:
            print("tijera gana a papel")
            print("computer gano!")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print("user gano!")
            user_wins += 1
        else:
            print("piedra gana a tijera")
            print("computer gano!")
            computer_wins += 1
    return user_wins, computer_wins


def run_game():
    """
    Runs the main game loop for 'piedra, papel o tijera'.

    The game continues until either the user or the computer wins 2 rounds.

    Returns:
        None
    """
    computer_wins = 0
    user_wins = 0
    rounds = 1
    while True:
        print("*" * 10)
        print("ROUND", rounds)
        print("*" * 10)

        print("computer_wins", computer_wins)
        print("user_wins", user_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        if user_option is None:
            continue
        user_wins, computer_wins = check_rules(
            user_option, computer_option, user_wins, computer_wins
        )

        if computer_wins == 2:
            print("El ganador es la computadora")
            break

        if user_wins == 2:
            print("El ganador es el usuario")
            break


run_game()

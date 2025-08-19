"""
Author: S.Kavishanthan
Version: 2.3
Date: 2024-07-27

Description:
This script implements a Rock-Paper-Scissors-Lizard-Spock game using an Arduino board with buttons, LEDs, and a buzzer.
"""

import pyfirmata
import time
import random

# Define the choices available in the game
choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# Initialize the Arduino board
board = pyfirmata.Arduino('COM9')

# Define pins

# Analog pins for Buttons
button_pins = ['a:0:i', 'a:1:i', 'a:2:i', 'a:3:i', 'a:4:i', 'a:5:i']

# Digital Pins for LEDs and Buzzer
led_pins = [2, 3, 4, 5, 6, 9, 10, 11, 12, 13] 
buzzer_pin = 8

# Setup buttons, LEDs, and buzzer
buttons = [board.get_pin(pin) for pin in button_pins]
leds = [board.get_pin(f'd:{pin}:o') for pin in led_pins]
buzzer = board.get_pin(f'd:{buzzer_pin}:o')

time.sleep(2)
iterator = pyfirmata.util.Iterator(board)
iterator.start()

# Button pins are set to input mode
for button in buttons:
    button.mode = pyfirmata.INPUT

def display_choices():
    """
    Print the available choices for the game.
    """
    for i, choice in enumerate(choices, start=1):
        print(f"{i}: {choice}")

def display_player_choice(choice, player):
    """
    Display the choice made by a player.
    
    Parameters:
    choice (int): The index of the chosen option.
    player (str): The name of the player making the choice.
    """
    print(f"{player} choice: {choices[choice]}")

def get_computer_choice():
    """
    Randomly select a choice for the computer.
    
    Returns:
    int: The index of the computer's choice.
    """
    return random.randint(0, 4)

def determine_round_result(player1_choice, player2_choice):
    """
    Determine the result of a round based on the choices made by Player 1 and the computer.
    
    Parameters:
    player1_choice (int): The index of Player 1's choice.
    player2_choice (int): The index of the computer's choice.
    
    Returns:
    int: 1 if Player 1 wins, -1 if the computer wins, 0 for a draw.
    """
    if player1_choice == player2_choice:
        return 0  # Draw
    elif (player1_choice - player2_choice) % 5 in [1, 3]:
        return 1  # Player 1 wins
    else:
        return -1  # Computer wins

def update_points(winner, player1_points, player2_points):
    """
    Update the points for both players based on the round winner.
    
    Parameters:
    winner (int): 1 if Player 1 wins, -1 if the computer wins, 0 for a draw.
    player1_points (int): Current points of Player 1.
    player2_points (int): Current points of the computer.
    
    Returns:
    tuple: Updated points of Player 1 and the computer.
    """
    if winner == 1:
        player1_points += 1
    elif winner == -1:
        player2_points += 1
    print(f"Player 1 Points = {player1_points} \nPlayer 2 Points = {player2_points}")
    return player1_points, player2_points

def indicate_winner(winner, leds):
    """
    Indicate the winner of a round using LEDs.
    
    Parameters:
    winner (int): 1 if Player 1 wins, -1 if the computer wins, 0 for a draw.
    leds (list): List of LED pins.
    """
    if winner == 1:
        leds[8].write(1)  # Player 1 wins
    elif winner == -1:
        leds[9].write(1)  # Computer wins
    else:
        leds[8].write(1)  # Draw
        leds[9].write(1)
    time.sleep(1)
    leds[8].write(0)
    leds[9].write(0)

def display_result_LED(player, result, leds):
    """
    Display the result on LEDs in binary format.
    
    Parameters:
    player (str): The player whose result to display ('player1' or 'player2').
    result (int): The result to display.
    leds (list): List of LED pins.
    """
    leds[8].write(1 if player == "player1" else 0)
    leds[9].write(1 if player == "player2" else 0)
    bit = format(result, '03b')
    for pin, i in zip(range(5, 8), range(3)):
        leds[pin].write(int(bit[i]))
    time.sleep(2)
    leds[8].write(0)
    leds[9].write(0)
    for pin in range(5, 8):
        leds[pin].write(0)

def blink_led(times, leds):
    """
    Blink LEDs a specified number of times.
    
    Parameters:
    times (int): Number of times to blink the LEDs.
    leds (list): List of LED pins.
    """
    for i in range(times):
        for pin in range(5, 8):
            leds[pin].write(1)
        time.sleep(0.3)
        for pin in range(5, 8):
            leds[pin].write(0)
        time.sleep(0.3)

def buzz(times, buzzer):
    """
    Buzz a specified number of times.
    
    Parameters:
    times (int): Number of times to buzz.
    buzzer (pyfirmata.Pin): Buzzer pin.
    """
    for _ in range(times):
        buzzer.write(1)
        time.sleep(0.2)
        buzzer.write(0)
        time.sleep(0.2)

def turn_off_all_leds(leds):
    """
    Turn off all LEDs.
    
    Parameters:
    leds (list): List of LED pins.
    """
    for pin in leds:
        pin.write(0)

def get_player1_choice(buttons):
    """
    Get the choice made by Player 1 by checking button presses.
    
    Parameters:
    buttons (list): List of button pins.
    
    Returns:
    int: Index of Player 1's choice, or -1 if no choice was made in time.
    """
    start_time = time.time()
    while time.time() - start_time < 3: # Wait for a choice
        for i, button in enumerate(buttons[:5]):
            if button.read() is not None and button.read() > 0.5:  # Check if the button is pressed
                return i
            time.sleep(0.2)

    buzz(2, buzzer)
    return -1  # Return -1 if no choice is made

def main():
    """
    Main game loop to play the Rock-Paper-Scissors-Lizard-Spock game.
    """
    print("Game Begins!!!")
    player1_points = 0
    player2_points = 0

    for round_number in range(7):  # Play 7 rounds
        if buttons[5].read() is not None and buttons[5].read() > 0.5:  # Exit the game if button 5 is pressed
            print("Game ended by player.")
            buzz(3, buzzer)
            break
        print(f"\n \nRound {round_number + 1}")
        buzz(1, buzzer)
        display_choices()
        
        # Player 1 makes a choice
        player1_choice = get_player1_choice(buttons)
        if player1_choice == -1:
            print("Player 1 did not make a choice in time.")
            player2_points += 1  # Player 2 gets a point
            print(f"Player 1 Points = {player1_points}\nPlayer 2 Points = {player2_points}")
            display_result_LED("player1", player1_points, leds)
            display_result_LED("player2", player2_points, leds)
            continue

        display_player_choice(player1_choice, "Player 1")

        # Player 2 (computer) makes a choice
        player2_choice = get_computer_choice()
        display_player_choice(player2_choice, "Player 2")
        leds[player2_choice].write(1)
        time.sleep(3)
        leds[player2_choice].write(0)

        # Determine the winner
        winner = determine_round_result(player1_choice, player2_choice)
        player1_points, player2_points = update_points(winner, player1_points, player2_points)

        if player1_points >= 4 or player2_points >= 4:
            indicate_winner(winner, leds)
            break
        
        # Show winner on LEDs
        indicate_winner(winner, leds)
        display_result_LED("player1", player1_points, leds)
        display_result_LED("player2", player2_points, leds)

    # Display the final results    
    final_winner = 1 if player1_points > player2_points else -1 if player2_points > player1_points else 0
    indicate_winner(final_winner, leds)
    print(f"Final Winner: {'Player 1' if final_winner == 1 else 'Player 2' if final_winner == -1 else 'Draw'}")
    blink_led(5, leds)

if __name__ == "__main__":
    try:
        main()
    finally:
        turn_off_all_leds(leds)
        # Signal end of the game
        buzz(1, buzzer)  
        board.exit()

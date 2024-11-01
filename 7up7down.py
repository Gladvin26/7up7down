import time
from random import randint

# Start with the initial amount of money and provide game rules
print("Hey, wassup!")
time.sleep(2)
print("🎲 Welcome to 7th Up 7th Down! 🎲")
time.sleep(2)
print("Get ready to place your bets on whether the sum of two dice will be higher, lower, or exactly 7!")
time.sleep(2)

# Displaying the Game Rules
print("\n📜 GAME RULES 📜")
time.sleep(3)
print("1. You start with a certain amount of money that you decide.")
time.sleep(3)
print("2. For each round, you can place a bet on one of the following options:")
time.sleep(3)
print("   - 7 Up (a): Bet that the dice sum will be more than 7. If correct, you win the amount you bet.")
time.sleep(3)
print("   - 7 Down (b): Bet that the dice sum will be less than 7. If correct, you win the amount you bet.")
time.sleep(3)
print("   - Lucky 7 (c): Bet that the dice sum will be exactly 7. If correct, you win *double* your bet! However, if you're wrong, you lose double your bet.")
time.sleep(3)
print("3. If you run out of money, you can withdraw more funds to keep playing.")
time.sleep(3)
print("4. At any time, you can choose to withdraw your balance and end the game.")
time.sleep(3)
print("\nLet’s get started and may the odds be in your favor! 🎲💸\n")

# Start the game
play = input("Would you like to join this exciting game of 7th Up 7th Down? (Y/N): ").lower()

if play == 'y':
    money = int(input("💰 How much money would you like to start with? "))

    # Check if the user ran out of money
    if money < 1:
        print("Oops, looks like you're out of money! Time to visit the ATM 💳.")
        money = int(input("How much money would you like to withdraw from your ATM? 💸 "))

    # Ask if the user wants to play
    while play == 'y':
        number = randint(2, 12)  # Dice sum should be between 2 and 12
        bet = int(input(f"🎲 Place your bet! You have {money} rupees. How much would you like to wager? "))

        if bet > money:
            print(f"Not enough funds! You need {bet - money} more rupees to place this bet. Try a smaller amount next time!")
            break

        if bet == 0:
            print("Minimum bet is 1 rupee. Please place a bet of at least 1 rupee next time.")
            bet = int(input(f"🎲 How much would you like to bet? You have {money} rupees: "))

        # Check if the user ran out of money
        if money < 1:
            print("You're out of money again! Time to visit the ATM 💳.")
            money = int(input("How much money would you like to withdraw from your ATM? 💸 "))

        guess = input("What's your guess? Bet 'a' for more than 7, 'b' for less than 7, or 'c' for exactly 7: ").lower()

        # Simulate the dice rolling
        time.sleep(1)
        print(".....")
        time.sleep(1)
        print("🎲 The dice are rolling... 🎲")
        time.sleep(1)
        print(".....")
        time.sleep(1)

        # Handle guesses
        if guess == 'a':
            if number > 7:
                print(f"🎉 Congratulations! You guessed correctly, the dice sum was {number}. 🎉")
                money += bet
            else:
                print(f"Oops! Your guess was wrong. The dice sum was {number}. Better luck next time!")
                money -= bet

        elif guess == 'b':
            if number < 7:
                print(f"🎉 Awesome! You guessed correctly, the dice sum was {number}. 🎉")
                money += bet
            else:
                print(f"Oops! Your guess was wrong. The dice sum was {number}. Better luck next time!")
                money -= bet

        elif guess == 'c':
            if number == 7:
                print(f"🎉 Lucky 7! You hit it right! The dice sum was {number}. You win double your bet! 🎉")
                money += bet * 2
            else:
                print(f"Oh no! You missed the Lucky 7. The dice sum was {number}. You lose double your bet.")
                money -= bet * 2
        else:
            print("Invalid choice! Please select 'a', 'b', or 'c'.")

        # Display current balance
        print(f"💵 Current Balance: {money} rupees 💵")

        # Check if the user ran out of money
        if money < 1:
            print("You're out of money! Time to visit the ATM 💳.")
            money = int(input("How much money would you like to withdraw from your ATM? 💸 "))

        # Ask if the player wants to continue playing or withdraw the balance
        play = input("Would you like to continue playing, withdraw your balance, or end the game? Enter 'Y' to play again, 'W' to withdraw your balance, or 'N' to end the game: ").lower()

        if play == 'w':
            print(f"💰 You have chosen to withdraw your current balance of {money} rupees. 💰")
            print("Thank you for playing 7th Up 7th Down! We hope to see you again soon. Have a great day! 😊")
            break
        elif play == 'n':
            print("Thank you for playing! Exiting the game now. Goodbye! 😊")
            break

else:
    print("Alright, maybe next time! Goodbye!")

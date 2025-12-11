import random
import os
import sys

class HangmanGame:
    def __init__(self):
        self.word_categories = {
            "Animals": {
                "words": ["elephant", "giraffe", "kangaroo", "penguin", "octopus", "dolphin", "tiger", "zebra"],
                "hints": [
                    "Has a trunk and large ears",
                    "Long neck and patterned coat",
                    "Hops and carries babies in pouch",
                    "Bird that swims but cannot fly",
                    "Sea creature with eight arms",
                    "Intelligent marine mammal",
                    "Large cat with stripes",
                    "African horse with black and white stripes"
                ]
            },
            "Countries": {
                "words": ["brazil", "canada", "japan", "egypt", "australia", "germany", "italy", "mexico"],
                "hints": [
                    "Famous for Carnival and Amazon",
                    "Known for maple syrup and hockey",
                    "Land of the rising sun",
                    "Ancient pyramids and Nile River",
                    "Home to kangaroos and koalas",
                    "Famous for cars and castles",
                    "Known for pizza and pasta",
                    "Colorful culture and tacos"
                ]
            },
            "Programming": {
                "words": ["python", "javascript", "function", "variable", "algorithm", "database", "framework", "syntax"],
                "hints": [
                    "Snake-named programming language",
                    "Language for web interactivity",
                    "Reusable block of code",
                    "Named storage for data",
                    "Step-by-step problem solution",
                    "Organized data collection",
                    "Reusable software platform",
                    "Rules for writing code"
                ]
            }
        }
        
        # ASCII art for hangman stages
        self.hangman_art = [
            """
               -----
               |   |
                   |
                   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
                   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
               |   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|   |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\  |
                   |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\  |
              /    |
                   |
            =========
            """,
            """
               -----
               |   |
               O   |
              /|\  |
              / \  |
                   |
            =========
            """
        ]
        
        self.score = 0
        self.games_won = 0
        self.games_played = 0
        self.current_category = ""
        self.current_word = ""
        self.current_hint = ""
        
    def clear_screen(self):
        
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_header(self):
        print("=" * 50)
        print("          UNIQUE HANGMAN GAME")
        print("=" * 50)
        print(f"🎮 Score: {self.score} | 🏆 Wins: {self.games_won}/{self.games_played}")
        print("-" * 50)
    
    def select_category(self):
        print("\n📚 CATEGORIES:")
        categories = list(self.word_categories.keys())
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category}")
        
        print("\nChoose an option:")
        print("1. Select category")
        print("2. Random category")
        
        while True:
            choice = input("Enter choice (1 or 2): ").strip()
            if choice == "1":
                while True:
                    try:
                        cat_num = int(input(f"Enter category number (1-{len(categories)}): "))
                        if 1 <= cat_num <= len(categories):
                            self.current_category = categories[cat_num-1]
                            break
                        else:
                            print("Invalid number. Try again.")
                    except ValueError:
                        print("Please enter a valid number.")
                break
            elif choice == "2":
                self.current_category = random.choice(categories)
                print(f"🎲 Selected random category: {self.current_category}")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
    
    def setup_game(self):
        """Set up a new game."""
        category_data = self.word_categories[self.current_category]
        
        # Select random word and hint
        index = random.randint(0, len(category_data["words"])-1)
        self.current_word = category_data["words"][index].upper()
        self.current_hint = category_data["hints"][index]
        
        return self.current_word
    
    def display_game_state(self, guessed_letters, wrong_guesses, max_wrong=6):
        """Display current game state."""
        self.clear_screen()
        self.display_header()
        
        print(f"\n📂 Category: {self.current_category}")
        print(f"💡 Hint: {self.current_hint}")
        
        # Display hangman art
        print("\n" + self.hangman_art[wrong_guesses])
        
        # Display word with blanks
        display_word = ""
        for letter in self.current_word:
            if letter in guessed_letters or letter == " ":
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"\n🔤 Word: {display_word}")
        
        # Display guessed letters
        print(f"\n✅ Correct letters: {', '.join([l for l in guessed_letters if l in self.current_word])}")
        print(f"❌ Wrong guesses: {', '.join([l for l in guessed_letters if l not in self.current_word])}")
        print(f"📊 Wrong guesses left: {max_wrong - wrong_guesses}")
        
        # Display score info
        print(f"\n💰 Current game score: {self.score}")
    
    def play_round(self):
        """Play one round of hangman."""
        word = self.setup_game()
        guessed_letters = set()
        wrong_guesses = 0
        max_wrong = 6
        
        while wrong_guesses < max_wrong:
            self.display_game_state(guessed_letters, wrong_guesses, max_wrong)
            
            # Check if word is complete
            if all(letter in guessed_letters or letter == " " for letter in word):
                print(f"\n🎉 CONGRATULATIONS! You guessed the word: {word}")
                self.score += 50  # Win bonus
                self.games_won += 1
                return True
            
            # Get player's guess
            while True:
                guess = input("\n🔤 Guess a letter (or type 'hint' for another hint): ").strip().upper()
                
                if guess == "HINT":
                    print(f"\n💡 Additional hint: The word has {len(word)} letters")
                    continue
                
                if len(guess) != 1:
                    print("❌ Please enter exactly one letter.")
                    continue
                
                if not guess.isalpha():
                    print("❌ Please enter a letter (A-Z).")
                    continue
                
                if guess in guessed_letters:
                    print("❌ You already guessed that letter.")
                    continue
                
                break
            
            guessed_letters.add(guess)
            
            # Check if guess is correct
            if guess in word:
                print(f"✅ Good guess! '{guess}' is in the word.")
                self.score += 10  # Points for correct guess
            else:
                print(f"❌ Sorry, '{guess}' is not in the word.")
                wrong_guesses += 1
                self.score -= 5  # Penalty for wrong guess
        
        # Game over - player lost
        self.display_game_state(guessed_letters, wrong_guesses, max_wrong)
        print(f"\n💀 GAME OVER! The word was: {word}")
        return False
    
    def play_game(self):
        """Main game loop."""
        print("=" * 50)
        print("          WELCOME TO UNIQUE HANGMAN!")
        print("=" * 50)
        print("\n🎯 Features:")
        print("  • 3 Themed categories with hints")
        print("  • Score tracking with bonuses/penalties")
        print("  • Visual hangman progression")
        print("  • Play multiple rounds")
        
        input("\nPress Enter to start...")
        
        while True:
            self.clear_screen()
            self.display_header()
            
            # Select category
            self.select_category()
            
            # Play round
            self.games_played += 1
            self.play_round()
            
            # Ask to play again
            print("\n" + "=" * 50)
            print(f"📊 Session Stats:")
            print(f"   Score: {self.score}")
            print(f"   Wins: {self.games_won}/{self.games_played}")
            print("=" * 50)
            
            play_again = input("\n🔄 Play again? (yes/no): ").strip().lower()
            if play_again not in ['yes', 'y', 'ye']:
                break
        
        # Final results
        self.clear_screen()
        print("=" * 50)
        print("           FINAL RESULTS")
        print("=" * 50)
        print(f"\n🎮 Games Played: {self.games_played}")
        print(f"🏆 Games Won: {self.games_won}")
        print(f"📈 Win Rate: {(self.games_won/self.games_played*100 if self.games_played > 0 else 0):.1f}%")
        print(f"💰 Final Score: {self.score}")
        print("\n" + "=" * 50)
        print("   Thanks for playing Unique Hangman!")
        print("   CodeAlpha Python Internship Project")
        print("=" * 50)

def main():
    """Main function to run the game."""
    try:
        game = HangmanGame()
        game.play_game()
    except KeyboardInterrupt:
        print("\n\n👋 Game interrupted. Thanks for playing!")
        sys.exit(0)
    except Exception as e:
        print(f"\n⚠️  An error occurred: {e}")
        print("Please try running the game again.")

if __name__ == "__main__":
    main()
import requests


class Hangman:
    hangman_states = {
        1: "/ \\",
        2: """
            |
            |
           / \\
        """,
        3: """
                |
                |
                |
                |
               / \\
        """,

        4: """      
                    _ _ _
                   |     
                   |
                   |
                   |
                  / \\
        """,
        5: """
                    _ _ _
                   |      |
                   |
                   |
                   |
                  / \\
        """,
        6: """
                    _ _ _
                   |     |    
                   |     O
                   |    
                   |
                  / \\
        """,
        7: """      
                    _ _ _
                   |     |    
                   |     O
                   |    /|\\
                   |
                  / \\
        """,
        8: """
                    _ _ _
                   |     |    
                   |     O
                   |    /|\\
                   |    / \\
                  / \\
            """,

    }

    word = []

    def start_game(self):
        print("Welcome to hangman!")
        print("Press enter to start a new game!")

        while input() != "":
            print("Press enter to start a new game!")

        self.init_word_to_guess()
        mistakes = 0

        while not self.game_is_over(mistakes):
            guess = self.take_guess()

            chars = [c[0].lower() for c in self.word]
            if guess in chars:
                print("Absolutely right!")
                for index, char_guessed_tuple in enumerate(self.word):
                    if guess == char_guessed_tuple[0].lower():
                        self.word[index] = (char_guessed_tuple[0], True)
            else:
                print("WRRROOOONG!")
                mistakes += 1

            self.draw_hangman(mistakes)
            print("")

        if mistakes == 8:
            print("You are hanging. Bad luck for you this time.")
        else:
            print("Congrats, you guessed the word and survived this time.")

        print("Your word was: " + "".join([c[0] for c in self.word]))
        print("GAME OVER!!!")

    def init_word_to_guess(self):
        word = self.fetch_word()
        print(word)
        for c in word:
            self.word.append((c, False))

    def game_is_over(self, mistakes):
        return mistakes == 8 or False not in [x[1] for x in self.word]

    def draw_hangman(self, mistakes):
        if mistakes == 0:
            print("Lucky you! No mistakes yet.")
            return

        print(self.hangman_states[mistakes])

    def fetch_word(self):
        random_word_json = requests.get("https://random-words-api.vercel.app/word")
        return random_word_json.json()[0]["word"]

    def take_guess(self):
        self.print_word_to_guess()
        user_input = ""
        while user_input == "":
            print("Take a guess if you dare!")
            user_input = input()

        return user_input.lower()

    def print_word_to_guess(self):
        print("Your word to guess: ")
        word_to_guess = ""
        for char, isGuessed in self.word:
            word_to_guess += char if isGuessed else "_"
            word_to_guess += " "

        print(word_to_guess)

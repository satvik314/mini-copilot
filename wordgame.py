import random
from utils import PromptTemplate, run_prompt

class WordGame:
    def __init__(self, words):
        self.words = words
        self.used_words = []

    def build_word(self, myword):
        last_letter = myword[-1]
        build_word_template = """
        Give me a word that starts with '{last_letter}'. 
        Just give the 'word' in the JSON response and nothing else.
        """
        build_word_template = PromptTemplate(input_variables=['last_letter'], template = build_word_template)
        build_word_prompt = build_word_template.format(last_letter=last_letter)
        output = run_prompt(prompt = build_word_prompt, json_mode= True)
        print(output)
        return output['word']

    def play(self):
        ai_word = random.choice(self.words)
        self.used_words.append(ai_word)
        print(f"AI starts with the word: {ai_word}")

        while True:
            player_word = self.build_word(ai_word)
            if player_word in self.used_words or player_word[0] != ai_word[-1]:
                print("Invalid word. You lose.")
                break
            self.used_words.append(player_word)

            ai_word = self.build_word(player_word)
            if ai_word is None:
                print("AI can't find a word. You win.")
                break
            print(f"AI's word: {ai_word}")


# Initialize the game with a word list
game = WordGame(['apple', 'elephant', 'tiger', 'rat', 'tail'])

# Start the game
game.play()

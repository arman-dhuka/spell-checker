from spellchecker import SpellChecker


class spellchecker :
    def __init__(self):
        self.spell = SpellChecker()

    def check_spelling(self, text):
        words = text.split()
        correct_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f"Misspelled word: {word} -> Corrected to: {corrected_word}")
                correct_words.append(corrected_word)

        return ' '.join(correct_words)
    
    def run (self):

        while True:
            text = input("Enter text to check spelling: ")
            
            if text.lower() == 'exit':
                break

            corrected_text = self.check_spelling(text)
            print("Corrected text:", corrected_text)
    

obj = spellchecker()
obj.run()



# this program is enhance by ai

from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def check_spelling(self, text):
        words = text.split()
        corrected_sentence = []

        for word in words:
            lower_word = word.lower()
            if lower_word in self.spell:  # Correct word
                corrected_sentence.append(word)
            else:
                corrected_word = self.spell.correction(lower_word)
                print(f"Misspelled: {word} -> Suggestion: {corrected_word}")
                print(f"Other suggestions: {self.spell.candidates(lower_word)}")
                # Preserve capitalization
                if word[0].isupper():
                    corrected_sentence.append(corrected_word.capitalize())
                else:
                    corrected_sentence.append(corrected_word)

        return ' '.join(corrected_sentence)

    def run(self):
        print("🔍 Spell Checker is running! Type 'exit' to quit.")
        while True:
            text = input("\nEnter text to check spelling: ")
            if text.lower() == 'exit':
                print("✅ Exiting Spell Checker. Goodbye!")
                break

            corrected_text = self.check_spelling(text)
            print(f"✔ Corrected text: {corrected_text}")

if __name__ == "__main__":
    obj = SpellCheckerApp()
    obj.run()

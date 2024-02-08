# Class that stores and manipulates the text
class FreeTextInterface():
    
    text: str = ''      # Text to be manipulated

    # Set the text obtained
    def setFreeText(self, text):
        pass

    # Append text received to the current one
    def appendFreeText(self, text):
        pass

    # Get the text obtained
    def getFreeText(self):
        pass

    # Get word in the current position
    def getCurrentWord(self):
        pass

    # Go to the next word of the text
    def goToNextWord(self):
        pass

    # Reset the current word pointer
    def goToFirstWord(self):
        pass

# Class that implements the FreeTextInterface
class FreeText(FreeTextInterface):
    start_of_word: int = 0
    end_of_word: int = 0

    # Set the text obtained
    def setFreeText(self, text):
        self.text = text

    # Append text received to the current one
    def appendFreeText(self, text):
        self.text = self.text + text

    # Get the text obtained
    def getFreeText(self):
        return self.text

    # Get word in the current word pointers
    def getCurrentWord(self):
        return self.text[self.start_of_word:self.end_of_word]

    # Updates the word pointers to the next word
    def goToNextWord(self):
        self.start_of_word = self.end_of_word
        self.end_of_word = self.__getNextWhitespace()

    # Reset the current word pointers
    def goToFirstWord(self):
        self.start_of_word = 0
        self.end_of_word = self.__getNextWhitespace()

    # Get a pointer to the next whitespace of the word
    def __getNextWhitespace(self):
        try:
            new_whitespace = self.text[self.start_of_word:].index(" ") + 1 + self.start_of_word
        except:
            new_whitespace = len(self.text)
        return new_whitespace

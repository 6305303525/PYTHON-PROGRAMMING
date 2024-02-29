from typing import List

class MagicDictionary:
    def __init__(self):
        self.words = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            for i in range(len(word)):
                # Create a pattern with '*' in place of the i-th character
                pattern = word[:i] + '*' + word[i+1:]
                # Add the word to the list of words with the pattern
                if pattern not in self.words:
                    self.words[pattern] = [word]
                else:
                    self.words[pattern].append(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            # Create a pattern with '*' in place of the i-th character
            pattern = searchWord[:i] + '*' + searchWord[i+1:]
            # Check if there is a word with the pattern in the dictionary
            if pattern in self.words:
                # If there is more than one word with the pattern, we can change one character
                # If there is exactly one word with the pattern, it must be different from the searchWord
                if len(self.words[pattern]) > 1 or self.words[pattern][0] != searchWord:
                    return True
        return False

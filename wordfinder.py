"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Get a random word from a file

    >>> wf = WordFinder('words2.txt')
    7 words read

    >>> wf.random() in ['A', 'a', 'aa', 'aal', 'aalii', 'aam', 'Aani']
    True

    >>> wf.random() in ['A', 'a', 'aa', 'aal', 'aalii', 'aam', 'Aani']
    True

    >>> wf.random() in ['A', 'a', 'aa', 'aal', 'aalii', 'aam', 'Aani']
    True

    """

    def __init__(self, path):
        """Read the file and return how many words were read"""
        file = open(path)
        self.words = self.generate_words(file)
        print(f'{len(self.words)} words read')
    def generate_words(self, file):
        """Generating the words in the file"""
        return [word.strip() for word in file]
    def random(self):
        """Get a random word from the file"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Get the word with not including the '#' and blankspace"""
    def generate_actual_words(self, file):
        return [word.strip() for word in file if word.strip() and not word.startwith('#')]

# wf = WordFinder('./words.txt')
# A
# a
# aa
# aal
# aalii
# aam
# Aani
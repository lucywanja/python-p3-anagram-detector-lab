class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        # Convert the initialized word to a sorted list of characters
        sorted_word = sorted(self.word)
        
        # List to store the matching anagrams
        matches = []
        
        # Iterate over each word in the possible anagrams list
        for candidate in possible_anagrams:
            # If the sorted characters of the candidate match the sorted initialized word
            if sorted(candidate) == sorted_word:
                matches.append(candidate)
        
        # Return the list of matches
        return matches

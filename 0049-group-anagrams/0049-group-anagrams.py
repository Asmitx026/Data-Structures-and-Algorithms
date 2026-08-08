class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Sorting and HashMaps
        Simple but high time complexity (O(n*mlogm))
        """

        """
        words = {}

        for word in strs:
            string = ''.join(sorted(word))
            if string not in words:
                words[string] = []
            words[string].append(word)
        
        return list(words.values())
        """

        """
        using HashMaps and Without Sorting
        Better time complexity since words are now grouped by the frequency of occuerences of characters (O(n*m*26))
        """

        words = {}

        for word in strs:
            count = [0]*26

            for char in word:
                count[ord(char) - ord('a')] +=1 # its specified that words are in lowercase, so this won't work with uppercase characters
            
            if tuple(count) not in words:
                words[tuple(count)] = []
            words[tuple(count)].append(word) # converting to tuple since keys must be immutable to be hashable

        return list(words.values())
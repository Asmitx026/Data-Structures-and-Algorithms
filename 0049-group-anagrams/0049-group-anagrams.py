class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Sorting and HashMaps
        Simple but high time complexity (O(n*mlogm))
        """
        words = {}

        for word in strs:
            string = ''.join(sorted(word))
            if string not in words:
                words[string] = []
            words[string].append(word)
        
        return [v for v in words.values()]
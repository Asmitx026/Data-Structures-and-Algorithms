class Solution:
    '''
    Encoded in this pattern '<len1>#<reversed-word1>...'
    Decoding took O(n) too

    Example: encoded_str = '4#olleH4#dlroW'
             decoded_str = ['Hello','World']
    '''

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""

        for word in strs:
            encoded_str += str(len(word)) + "#" + word[::-1]

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            i = j + 1
            decoded_str.append(s[i:i+length][::-1])
            i += length

        return decoded_str

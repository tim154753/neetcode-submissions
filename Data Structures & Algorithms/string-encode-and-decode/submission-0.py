class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded = encoded + f'{len(s)}#' + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            c = s[i]
            num = ''
            place = 0
            while c != '#':
                num += c
                place += 1
                c = s[i+place]
            i = i + place + 1
            num = int(num)
            decoded.append(s[i:i+num])
            i = i+num
        return decoded
                
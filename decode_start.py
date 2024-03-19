alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
f = open("secret.txt")
text =  f.read()

lines = text.split("\n")ç
for line in lines:
    def caesar_decrypt(ciphertext, shift):
        decrypted_text = ""
        for char in ciphertext:
            if char.isalpha():
                shifted_unicode = ord(char) - shift
                if char.islower():
                    if shifted_unicode < ord('a'):
                        shifted_unicode += 26
                elif char.isupper():
                    if shifted_unicode < ord('A'):
                        shifted_unicode += 26
                decrypted_text += chr(shifted_unicode)
            else:
                decrypted_text += char
        return decrypted_text


    encoded_text = "kskpnmmerynrthtullixbwjvfxsqdhngmphjjwgoaodzzalckqiqcybpgevfphpqdrlmzxvbcdpygrfsjnnhmjgxlkfbmcsckftwvqslbqtyktdgwzhnrjzybeiiruqwogjepegscounuaufnhoivqwczkxisezaeitaydfrmbdvaxoatlypsllkcwkqg

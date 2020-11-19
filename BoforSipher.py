def InitKey(text, initialKey):
    return (initialKey * (len(text)) + initialKey)[:len(text)]


def BoforSipherEncrypt(text, key):
    return ''.join([chr(((ord(text[i]) - ord(key[i])) % 26) + ord("A")) for i in range(len(text))])

def BoforSipherDecrypt(text, key):
    return ''.join([chr(((ord(key[i]) + ord(text[i])) % 26) + ord("A")) for i in range(len(text))])

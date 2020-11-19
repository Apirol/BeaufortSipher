from InputHandler import openFileAndReadData
from InputHandler import PrepareText
from OuputHandler import writeDataToFile
from BoforSipher import BoforSipherEncrypt
from BoforSipher import BoforSipherDecrypt
from BoforSipher import InitKey


if __name__ == '__main__':
    textToEncrypt = PrepareText(openFileAndReadData("Data/Text.txt"))
    initialKey = openFileAndReadData("Data/keyForText.txt")
    key = InitKey(textToEncrypt, initialKey)
    encryptedText = BoforSipherEncrypt(textToEncrypt, key)
    decryptedText = BoforSipherDecrypt(encryptedText, key)
    writeDataToFile(encryptedText, "Data/EncryptedText.txt")
    writeDataToFile(decryptedText, "Data/DecryptedText.txt")

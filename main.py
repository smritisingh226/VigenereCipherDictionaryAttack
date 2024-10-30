"""
*    Title: HACKING THE VIGENÈRE CIPHER
*    Author: Al Sweigart
*    Date: 2018
*    Code version: 2nd edition
*    Availability: Cracking codes with python: An introduction to building and breaking ciphers
"""

#A dictionary attack is a brute-force technique
#The hacker attempts to decrypt the ciphertext using the words from a dictionary file as the keys
#Also known as exhaustive search
import detectEnglish, vigenereCipher



def main():
    ciphertext = input("Please enter cipher text to be decoded: ")
    print("Decoding... Please wait...\n")
    hackedMessage = hackVigenere(ciphertext)

    if hackedMessage != None:
        print(hackedMessage)


    else:
        print('Failed to hack encryption.')

#function reads in the contents of the dictionary file,
#Considers each word in that file as a key to decrypt the ciphertext,
#If decrypted text looks readable , it gives an option to either quit or continue
def hackVigenere(ciphertext):
    #Opens the dictionary.txt file to match possible keys
    fo = open('dictionary.txt')
    decryptText = open("decrypted.txt", "w")
    #return a list of strings from the dictionar file, where each string is on a new line
    words = fo.readlines()
    fo.close()

    for word in words:                  #Loops through the string of keys
        word = word.strip()             #remove the newline at the end
        decryptedText = vigenereCipher.decryptMessage(word,ciphertext)

        if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
            # Check with user to see if the decrypted key has been found.
            print('Possible encryption break:')
            print('Key ' + word + ': ' + decryptedText)
            print()
            #Asks user if the decryption makes a meaning.
            #Gives user the option to break out from decryption or keep decrypting.
            print('Enter D for done, or just press Enter to continue breaking:')
            response = input('> ')

            if response.upper().startswith('D'):
                #If the user input is D then the decrypted message is written to a file decrypted.txt
                decryptText.write(decryptedText)
                return "The decrypted text has been written to the file decrypted.txt"




main()


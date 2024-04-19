import pickle

# Define the mapping of alphabet letters to unique non-keyboard codes
encryption_codes = {
    'A': 'α', 'a': 'β', 'B': 'γ', 'b': 'δ', 'C': 'ε', 'c': 'ζ', 'D': 'η',
    'd': 'θ', 'E': 'ι', 'e': 'κ', 'F': 'λ', 'f': 'μ', 'G': 'ν', 'g': 'ξ',
    'H': 'ο', 'h': 'π', 'I': 'ρ', 'i': 'ς', 'J': 'σ', 'j': 'τ', 'K': 'υ',
    'k': 'φ', 'L': 'χ', 'l': 'ψ', 'M': 'ω', 'm': 'ᾶ', 'N': 'ῆ', 'n': 'ὴ',
    'O': 'ὶ', 'o': 'ῖ', 'P': 'ῦ', 'p': 'ᾷ', 'Q': 'ῇ', 'q': 'ή', 'R': 'ί',
    'r': 'ῗ', 'S': 'ῧ', 's': 'ᾳ', 'T': 'ῃ', 't': 'ῳ', 'U': 'ἀ', 'u': 'ἁ',
    'V': 'ἂ', 'v': 'ἃ', 'W': 'ἄ', 'w': 'ἅ', 'X': 'ἆ', 'x': 'ἇ', 'Y': 'Ἀ',
    'y': 'Ἁ', 'Z': 'Ἂ', 'z': 'Ἃ'
}

# Decrypt the encrypted data from the pickle file
def decrypt_pickle(filepath_of_pickle):
    with open(filepath_of_pickle, 'rb') as pickle_file:
        encrypted_data = pickle.load(pickle_file)
        decrypted_data = []
        for encrypted_line in encrypted_data:
            decrypted_line = ''
            for character in encrypted_line:
                decrypted_char = ''
                for key, value in encryption_codes.items():
                    if value == character:
                        decrypted_char = key
                        break
                if decrypted_char:
                    decrypted_line += decrypted_char
                else:
                    decrypted_line += character

            decrypted_data.append(decrypted_line)
    return decrypted_data


# main function
if __name__ == '__main__':
    filepath_of_pickle = '/Users/sandeepk/Library/Mobile Documents/com~apple~CloudDocs/IUPUI/CSCI-A 205 Programming/Chapter 9/encrypt:decrypt/encrypted_data.pickle'
    
    decrypted_data = decrypt_pickle(filepath_of_pickle)
    
    print('Decrypted Data:')
    for line in decrypted_data:
        print(line)

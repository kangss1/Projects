import pickle

# Encryption Program

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

# Encrypt alphabetical characters from file into random code and serialize it using pickle
def encrypt_and_pickle(input_file):
    encrypted_data = []
    with open(input_file, 'r') as infile:
        for line in infile:
            encrypted_line = ''
            for character in line:
                if character.isalpha() and character in encryption_codes:
                    encrypted_line += encryption_codes[character]  # Encrypt the character
                    print(f'{character} encoded to {encryption_codes[character]}')                    
                else:
                    encrypted_line += character  # Keep the character as is if it's not in the codes
                    print(f'{character} encoded to {character}')
            encrypted_data.append(encrypted_line)
    return encrypted_data

# main function
if __name__ == '__main__':
    filepath_of_input = '/Users/sandeepk/Library/Mobile Documents/com~apple~CloudDocs/IUPUI/CSCI-A 205 Programming/Chapter 9/encrypt:decrypt/input_file.txt'
    filepath_of_pickle = '/Users/sandeepk/Library/Mobile Documents/com~apple~CloudDocs/IUPUI/CSCI-A 205 Programming/Chapter 9/encrypt:decrypt/encrypted_data.pickle'
    
    encrypted_data = encrypt_and_pickle(filepath_of_input)
    
    with open(filepath_of_pickle, 'wb') as pickle_file:
        pickle.dump(encrypted_data, pickle_file)
    
    print(f'File has been encrypted and serialized using pickle to: \nFile Path: {filepath_of_pickle}')

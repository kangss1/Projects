README

This repository contains two Python scripts for encoding and decoding text files using a custom encryption scheme, followed by serialization/deserialization using Python's pickle module.

1. pickle_encoder.py

- Function: This script encrypts textual data by mapping each alphabetic character to a unique non-keyboard character based on a predefined dictionary. The encrypted data is then serialized into a pickle file.
- Usage:
  - Modify the 'filepath_of_input' variable to the path of your input text file.
  - The output pickle file path is set in 'filepath_of_pickle'.
  - Run the script to encode and serialize the input file.

2. pickle_decoder.py

- Function: This script deserializes the data from a pickle file created by 'pickle_encoder.py' and decrypts it back to its original form using the reverse of the predefined dictionary used for encryption.
- Usage:
  - Ensure that 'filepath_of_pickle' matches the output path used in 'pickle_encoder.py'.
  - Run the script to deserialize and decrypt the data.

Encryption Dictionary:
The scripts use a custom dictionary for encryption and decryption, mapping each English letter (A-Z, a-z) to unique symbols. Ensure that this dictionary remains consistent between the two scripts.

Requirements:
- Python 3.x
- Access to a system that supports Python and the ability to read/write to the specified file paths.

Notes:
- These scripts are designed for educational and demonstrative purposes. The encryption method used should not be considered secure for sensitive data.
- Adjust file paths based on your system configuration to ensure proper reading and writing of files.

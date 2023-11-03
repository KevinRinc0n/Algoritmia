# Your task is to implement a function that would take the morse code as input and return a decoded human-readable string.

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8',
    '----.': '9', '···−−−···': 'SOS'
}

def decode_morse(morse_code):
    morse_words = morse_code.strip().split('   ')
    decoded_words = []
    
    for morse_word in morse_words:
        morse_characters = morse_word.split(' ')
        decoded_word = ''.join(MORSE_CODE[char] for char in morse_characters if char in MORSE_CODE)
        decoded_words.append(decoded_word)
    
    decoded_message = ' '.join(decoded_words)
    return decoded_message

morse_code = '.... . -.--   .--- ..- -.. .'
decoded_message = decode_morse(morse_code)
print(decoded_message)  

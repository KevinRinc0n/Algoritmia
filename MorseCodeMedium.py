# Function , that should find out the transmission rate of the message, correctly decode the message to dots , dashes and spaces (one between characters, three between words) and return those as a string. Note that some extra 's may naturally occur at the beginning and the end of a message, make sure to ignore them. Also if you have trouble discerning if the particular sequence of 's is a dot or a dash, assume it's a dot.decodeBits(bits).-01

# 2. Function , that would take the output of the previous function and return a human-readable string.decodeMorse(morseCode)

# All the test strings would be valid to the point that they could be reliably decoded as described above, so you may skip checking for errors and exceptions, just do your best in figuring out what the message is!


MORSE_CODE = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
    "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
    "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
    ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
    "--..": "Z", "-----": "0", ".----": "1", "..---": "2", "...--": "3",
    "....-": "4", ".....": "5", "-....": "6", "--...": "7", "---..": "8",
    "----.": "9"
}

def decodeBits(bits):
    bits = bits.strip('0')
    unit_time = min(len(s) for s in bits.split('1'))
    morse_code = bits.replace('0000000'*unit_time, '   ').replace('000'*unit_time, ' ').replace('0'*unit_time, '').replace('1'*unit_time, '.')
    return morse_code

def decodeMorse(morseCode):
    words = morseCode.strip().split('   ') 
    decoded_message = ""
    for word in words:
        chars = word.split(' ')  
        decoded_chars = [MORSE_CODE[char] for char in chars if char in MORSE_CODE]
        decoded_message += ''.join(decoded_chars) + ' ' 
    return decoded_message.strip()  

bits = "1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011"
morse_code = decodeBits(bits)
decoded_message = decodeMorse(morse_code)
print(decoded_message)  

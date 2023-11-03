# 1. Function , that should find an estimate for the transmission rate of the message, take care about slight speed variations that may occur in the message, correctly decode the message to dots , dashes and spaces (one between characters, three between words) and return those as a string. Note that some extra 's may naturally occur at the beginning and the end of a message, make sure to ignore them. If message is empty or only contains 's, return empty string. Also if you have trouble discerning if the particular sequence of 's is a dot or a dash, assume it's a dot. If stuck, check this for ideas.decodeBitsAdvanced(bits).-001

# 2. Function , that would take the output of the previous function and return a human-readable string. If the input is empty string or only contains spaces, return empty string.decodeMorse(morseCode)


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

def decodeBitsAdvanced(bits):
    bits = bits.strip('0') 
    if not bits:
        return ''
    
    min_duration = float('inf')
    max_duration = float('-inf')
    i = 0
    while i < len(bits):
        if bits[i] == '1':
            count = 0
            while i < len(bits) and bits[i] == '1':
                count += 1
                i += 1
            min_duration = min(min_duration, count)
            max_duration = max(max_duration, count)
        else:
            count = 0
            while i < len(bits) and bits[i] == '0':
                count += 1
                i += 1
            min_duration = min(min_duration, count)
            max_duration = max(max_duration, count)
    
    avg_duration = (min_duration + max_duration) // 2
    
    chunks = [bits[i:i+avg_duration] for i in range(0, len(bits), avg_duration)]
    
    morse_code = ''
    for chunk in chunks:
        if chunk == '1':
            morse_code += '.'
        elif chunk == '111':
            morse_code += '-'
        elif chunk == '0':
            morse_code += ' '
        elif chunk == '000':
            morse_code += '   '
    
    return morse_code

def decodeMorse(morseCode):
    words = morseCode.strip().split('   ')
    decoded_message = ''
    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in MORSE_CODE:
                decoded_message += MORSE_CODE[letter]
        decoded_message += ' '
    return decoded_message.strip()

bits = "0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000"
morse_code = decodeBitsAdvanced(bits)
decoded_message = decodeMorse(morse_code)
print(decoded_message) 

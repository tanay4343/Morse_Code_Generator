from flask import Flask, render_template, request
import winsound
import time
import pyttsx3

# Morse code dictionary

morse_code_dict = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H',
    '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0', '/': ' ', '': ''
}

# Morse code dictionary
text_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

def text_to_morse(text):
    text_code = []
    for char in text.upper():
        if char in text_code_dict:
            text_code.append(text_code_dict[char])
        else:
            text_code.append(char)
    return ' '.join(text_code)

def morse_to_text(morse_code):
    words = morse_code.split(' / ')
    decoded_message = []
    for word in words:
        letters = word.split()
        decoded_word = ''
        for letter in letters:
            if letter in morse_code_dict:
                decoded_word += morse_code_dict[letter]
        decoded_message.append(decoded_word)
    return ' '.join(decoded_message)

def play_morse_code(morse_code):
    for char in morse_code:
        if char == '.':
            winsound.Beep(1000, 200)  # Beep for dot
        elif char == '-':
            winsound.Beep(1000, 600)  # Beep for dash
        elif char == '/':
            time.sleep(0.4)  # Pause for word gap
        elif char == ' ':
            time.sleep(0.2)  # Pause for letter gap

def play_text_sound(text_code):
    engine = pyttsx3.init()
    engine.say(text_code)
    engine.runAndWait()

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])  # Change to accept POST requests
def done():
    type_value = request.form.get("type")
    code_value = request.form.get("code")
    if type_value == "T":
        Inp = "Your Morse Code:"
        morse_code = text_to_morse(code_value)
        time.sleep(10)
        sound = play_morse_code(morse_code)
        return render_template("submit.html", Input=Inp, Output=morse_code, play=sound)
    elif type_value == "M":
        Inp = "Your Text is:"
        text_code = morse_to_text(code_value)
        time.sleep(10)
        sound = play_text_sound(text_code)
        return render_template("submit.html", Input=Inp, Output=text_code, play=sound)
    else:
        Noway = "Select Only From T and M NothingElse."
        return render_template("submit.html", Output=Noway)

if __name__ =="__main__":
    app.run(debug=True)

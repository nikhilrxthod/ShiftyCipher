# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

def shifty_cipher(text, shift):
    def shift_char(char, shift_amount):
        base = ord('a') if char.islower() else ord('A')
        return chr((ord(char) - base + shift_amount) % 26 + base)

    shift_amount = shift % 26
    return ''.join(shift_char(char, shift_amount) if char.isalpha() else char for char in text)

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ""
    if request.method == 'POST':
        text = request.form.get('text', '')
        shift = int(request.form.get('shift', 0))
        encrypted_text = shifty_cipher(text, shift)
    return render_template('index.html', encrypted_text=encrypted_text)

if __name__ == '__main__':
    app.run(debug=True)

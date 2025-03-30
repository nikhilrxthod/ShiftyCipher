# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

def shifty_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

@app.route('/', methods=['GET', 'POST'])
def index():
    encrypted_text = ""
    if request.method == 'POST':
        text = request.form['text']
        shift = int(request.form['shift'])
        encrypted_text = shifty_cipher(text, shift)
    return render_template('index.html', encrypted_text=encrypted_text)

if __name__ == '__main__':
    app.run(debug=True)
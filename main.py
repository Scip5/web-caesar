from flask import Flask, request
from caesar import rotate_string 

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!doctype html>
    <html>
        <head>
            <style>
                
                form {{
                    
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    border-radius: 10px;
                }}

                textarea {{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}

                .error {{
                    color: red;
                }}

            </style>
        </head>
        <body>
            <form method="POST">
                
                <label>Rotate by: 
                    <input type="text" name="rot" value='{rotate}' />
                </label>

                <p class="error">{input_error}</p>

                <textarea name="text">{text}</textarea>

                <br>

                <input type="submit" />            
            </form>
        </body>          
    </html>
"""

@app.route("/")
def index():
    return form.format(rotate='', input_error='' , text='')

def is_integer(num):

    try:
        int(num)
        return True
    except ValueError:
        return False

def number_alpha(num):
    
    num = int(num)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_char = alphabet[num]
    return alpha_char
    
@app.route("/", methods=['POST'])
def encrypt():
    rot = request.form['rot']
    text = request.form['text']
    input_error = ""
    numbers = "0123456789"
    newString = ""
    finalString = ""
    

    if not is_integer(rot):
        input_error = "Input must be an integer"
        rot = ""
    else:
        rot = int(rot)
        newString = rotate_string(text, rot)

    for char in newString:
        if char in numbers:
            letter = number_alpha(char)            
            finalString = finalString + letter

        else:
            finalString = finalString + char

    if not input_error:
        return form.format(text=finalString) 
    else:
        return form.format(rotate=rotate, input_error=input_error, text=text)

app.run()


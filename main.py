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
            </style>
        </head>
        <body>
            <form method="POST">
                <label>Rotate by: 
                    <input type="text" name="rot" value="0" />
                </label>
                <p>
                </p>
                <textarea name="text">{0}</textarea>
                <br>
                <input type="submit" />            
            </form>
        </body>
          
</html>
"""
@app.route("/", methods=['POST'])
def encrypt():
    num = request.form['rot']
    realNum = int(num)
    string = request.form['text']
    newString = rotate_string(string, realNum)
    return form.format(newString) 

@app.route("/")
def index():
    return form.format("")

app.run()


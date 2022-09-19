from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def index():
    return render_template('index.html')

@app.get("/SQLstatements")
def sql():
    return render_template('statements.html')

@app.get("/About")
def about():
    me = {
        "first_name": "Eduardo",
        "last_name": "Reynoso",
        "hobbies": "Gym, Programming",
        "bio": "My name is Eduardo Reynoso and I am a student."
    }
    return render_template('about.html', about_dict=me)
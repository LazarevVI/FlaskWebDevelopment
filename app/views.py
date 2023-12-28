from app import app

@app.route('/')
@app.route('/home')
def home():
    return "Home Page"
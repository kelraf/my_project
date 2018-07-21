from flask import Flask, url_for, render_template

app =Flask(__name__)

@app.route('/')
def landing_page():
    return render_template('landing_page.html')

@app.route('/registration') 
def registration_1():
    return render_template('registration_form_1.html')

@app.route('/registration_2')
def registration_2():
    return render_template('registration_form_2.html')    

@app.route('/login')
def login():
    return render_template('login.html') 

@app.route('/home')  
def home():
    return render_template('home.html')  

@app.route('/backetlist')   
def backetlist():
    return render_template('backetlist.html') 

@app.route('/my_account')
def my_account():
    return render_template('my_account.html')    


if __name__ == '__main__':
    app.run(debug = True)
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy data store
feedback_list = []
admin_credentials = {"admin": "password123"}  # Replace with secure method in production

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    feedback = request.form['feedback']
    feedback_list.append(feedback)
    return "Thanks for your feedback!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if admin_credentials.get(username) == password:
            session['admin'] = True
            return redirect(url_for('admin'))
        else:
            return "Login Failed"
    return render_template('login.html')

@app.route('/admin')
def admin():
    if not session.get('admin'):
        return "Access Denied"
    return render_template('admin.html', feedback=feedback_list)

@app.route('/logout')
def logout():
    session.pop('admin', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

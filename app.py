from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Flask Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'latunechient@gmail.com'
app.config['MAIL_PASSWORD'] = 'Adunni#88'
app.config['MAIL_DEFAULT_SENDER'] = 'latunechient@gmail.com'

mail = Mail(app)

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Send an email with the contact form details
        msg = Message(f'New message from {name}', recipients=['latunechient@gmail.com'])
        msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        
        try:
            mail.send(msg)
            return redirect(url_for('contact_success'))
        except Exception as e:
            return f"Error: {str(e)}"
    
    return render_template('contact.html')

# Contact Success Route (After form submission)
@app.route('/contact-success')
def contact_success():
    return render_template('contact_success.html')

# Projects Route
@app.route('/projects')
def projects():
    return render_template('projects.html')

# Gallery Route
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

if __name__ == '__main__':
    app.run(debug=True)


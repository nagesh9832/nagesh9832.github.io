from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

app = Flask(__name__)

# Replace with your receiving email address
receiving_email_address = 'nageshv.9832@gmail.com'

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Create an email message
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = receiving_email_address
        msg['Subject'] = subject

        body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        msg.attach(MIMEText(body, 'plain'))

        # Setup SMTP server (replace with your SMTP server details)
        smtp_server = 'your-smtp-server.com'
        smtp_port = 587
        smtp_username = 'your-username'
        smtp_password = 'your-password'

        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(email, receiving_email_address, msg.as_string())
            return 'Email sent successfully!'
        except Exception as e:
            return f'Error: {str(e)}'

    return render_template('contact_form.html')

if __name__ == '__main__':
    app.run(debug=True)

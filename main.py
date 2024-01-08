from flask import Flask, render_template, request, flash, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators
from wtforms.validators import DataRequired, Email, Regexp, Length
import smtplib
from twilio.rest import Client
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('F_KEY')
Bootstrap5(app)


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()], render_kw={"placeholder": "Enter your name"})
    email = StringField('Email', validators=[DataRequired(), Email(message="Invalid email address")],
                        render_kw={"placeholder": "Email: to be contacted at"})
    phone = StringField('Phone Number',
                        validators=[validators.Optional(), Regexp(r'^\d{10}$', message="Invalid phone number")],
                        render_kw={"placeholder": "Cell(optional): if you prefer a callback"})
    message = TextAreaField('Message', validators=[DataRequired(), Length(max=1000)],
                            render_kw={"placeholder": "Your message ...\nMax characters: 1000"})
    email_button = SubmitField('Send Email', render_kw={"class": "btn-custom"})
    text_button = SubmitField('Send Text', render_kw={"class": "btn-custom"})
    clear_button = SubmitField('Clear Form', render_kw={"class": "btn-secondary"})


def send_email(message):
    my_email = os.environ.get("E_ID")
    password = os.environ.get("E_KEY")
    email_to = os.environ.get("E_ID_TO")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email_to,
                            msg=message)
        connection.close()


def send_text(message):
    client = Client(os.environ.get('A_ID'), os.environ.get('A_T'))
    client.messages.create(
        body=message,
        from_=os.environ.get('S_ID'),
        to=os.environ.get('T_ID')
    )


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/experience')
def experience():
    return render_template('experience.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/eng')
def eng():
    return render_template('eng.html')


@app.route('/grad')
def grad():
    return render_template('grad.html')


@app.route('/award')
def award():
    return render_template('award.html')


@app.route('/test/<int:num>')
def test(num):
    filename = f'assets/test/{num}.pdf'
    file_path = url_for('static', filename=filename)
    return render_template('testimonial.html', path=file_path)


@app.route('/slides')
def slides():
    total = 23
    image_paths = []
    for x in range(1, total + 1):
        filename = f'assets/slides/Slide{x}.jpeg'
        image_path = url_for('static', filename=filename)
        image_paths.append(image_path)
    image_paths_with_index = [(index, path) for index, path in enumerate(image_paths)]
    return render_template('slides.html', image_paths=image_paths_with_index)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST' and 'clear_button' in request.form:
        return redirect(url_for('contact'))
    if request.method == 'POST' and form.validate_on_submit():
        name = request.form['name']
        if request.form['phone']:
            phone = request.form['phone']
        else:
            phone = 'Not given'
        email = request.form['email']
        message = request.form['message']
        if 'email_button' in request.form:
            send_email(
                message=f"Subject: New message from {name}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: "
                        f"\n{message}")
            flash('Email has been sent successfully')
            return render_template('contact.html', form=form)
        if 'text_button' in request.form:
            send_text(
                message=f"Subject: New message from {name}\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: "
                        f"\n{message}")
            flash('Text message has been sent successfully')
            return render_template('contact.html', form=form)
    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=False)

from flask import Flask, render_template, url_for, redirect, request
import csv

# Development Server 
# Flask Run to Start
# "set FLASK_ENV=development for debug near-live veiw"
app = Flask(__name__)

@app.route('/')
def index_original():
    return render_template('index.html')

# Routes Home Page
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/Submission', methods = ['GET', 'POST'])
def submit():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_data_csv(data)
            return "Form Submitted"
        
        except:
            return "Did not save data to db"
    else:
        return "Form Not Submitted"

@app.route('/<string:page_name>')
def page(page_name='/'):
    try:
        return render_template(page_name)
    except:
        return redirect('/')

def write_data_csv(data):
    email = data['email']
    subject = data['subject']
    message = data['message']
''' 
   with open('db.csv', 'a', newline='') as csvfile:
        db_writer = csv.writer(csvfile, delimeter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        db_writer.writerow([email,subject,message])
'''
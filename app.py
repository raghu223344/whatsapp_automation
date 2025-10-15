from flask import Flask, render_template, request
import pywhatkit

app = Flask(__name__)

GRADES = ["1A", "1B", "2A", "2B", "3", "4", "5", "6", "7"]

def get_contacts_for_grade(grade):
    file_path = f'contacts/{grade}.txt'
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    contacts = []
    selected_grade = None
    message = ""
    sent = False
    if request.method == 'POST':
        selected_grade = request.form.get('grade')
        message = request.form.get('message')
        contacts = get_contacts_for_grade(selected_grade)
        # Send message to these contacts
        for number in contacts:
            pywhatkit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
        sent = True
    return render_template('index.html', grades=GRADES, contacts=contacts, selected_grade=selected_grade, message=message, sent=sent)

if __name__ == "__main__":
    app.run(debug=True)

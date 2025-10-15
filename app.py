from flask import Flask, render_template, request, redirect, url_for
import pywhatkit

app = Flask(__name__)

GRADES = ["1A", "1B", "2A", "2B", "3", "4", "5", "6", "7"]

def get_contacts_for_grade(grade):
    if not grade:
        return []
    file_path = f'contacts/{grade}.txt'
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    grades = GRADES
    contacts = []
    selected_grade = None
    message = ""
    sent = False

    if request.method == 'POST':
        selected_grade = request.form.get('grade')
        message = request.form.get('message')
        contacts = get_contacts_for_grade(selected_grade)
        for number in contacts:
            pywhatkit.sendwhatmsg_instantly(number, message, wait_time=10, tab_close=True)
        # Redirect after POST to avoid resending
        return redirect(url_for('index', sent="1", grade=selected_grade))
    else:
        selected_grade = request.args.get('grade')
        sent = request.args.get('sent') == "1"
        contacts = get_contacts_for_grade(selected_grade) if selected_grade else []
    return render_template('index.html', grades=grades, contacts=contacts, selected_grade=selected_grade, message="", sent=sent)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary in-memory storage (restarts will lose data)
failures = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_failure():
    if request.method == 'POST':
        title = request.form['title']
        date = request.form['date']
        description = request.form['description']
        lesson = request.form['lesson']
        failures.append({
            'title': title,
            'date': date,
            'description': description,
            'lesson': lesson
        })
        return redirect(url_for('list_failures'))
    return render_template('add_failure.html')

@app.route('/failures')
def list_failures():
    return render_template('list_failures.html', failures=failures)

# *** NEW: Interactive A4 Resume Builder ***
@app.route('/create')
def create_cv():
    return render_template('create_cv.html')

if __name__ == "__main__":
    app.run(debug=True)

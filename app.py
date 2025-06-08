from flask import Flask, render_template, request, redirect
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

cred = credentials.Certificate('firebase-key.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        if task:
            db.collection('todos').add({'task': task})
        return redirect('/')
    
    todos_ref = db.collection('todos').stream()
    tasks = [doc.to_dict() for doc in todos_ref]
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import json
from json.decoder import JSONDecodeError
import random
from datetime import datetime

app = Flask(__name__)

class UserController:
    def __init__(self,surname, name,timestamp):
        self.id = random.randint(1000,9999)
        self.surname = surname
        self.name = name
        self.timestamp=timestamp    
    def get_id(self):
        return self.id
    def get_surname(self):
        return self.surname
    def get_name(self):
        return self.name
    def get_timestamp(self):
        return self.timestamp

def load_records(records):
    with open("records.json", 'r+') as file:
        try:
            file_data = json.load(file)
        except json.decoder.JSONDecodeError:
            file_data = {"details": []}
        file_data["details"].append(records)
        file.seek(0)
        json.dump(file_data, file, indent=4)

@app.route('/', methods = ['GET'])
def index():
    return render_template('menu.html')

@app.route('/index21.html', methods=['GET'])
def button1():
    return render_template('index21.html')

@app.route('/createrecord', methods = ['POST'])
def createRecord():
    surname = request.form['Surname']
    name = request.form['name']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    u1 = UserController(surname, name,timestamp)
    records = {"id": u1.get_id(),"surname": u1.get_surname(), "name": u1.get_name(),"timestamp":u1.get_timestamp()}
    data = load_records(records)
    print(data)
    return f"ID: <b>{u1.get_id()}</b><br>Name: <b>{u1.get_name()}</b><br>Surname: <b>{u1.get_surname()}</b><br>Timestamp: <b>{u1.get_timestamp()}</b>"

@app.route('/records.html', methods = ['GET'])
def display_records():
    with open("records.json", "r") as f:
        data = json.load(f)
    return render_template('records.html', records=data['details'], colnames=['id', 'surname', 'name','timestamp'])

@app.route("/recordid.html", methods = ['GET'])
def button2():
    return render_template('recordid.html')

@app.route("/recordid.html", methods = ['POST'])
def getRecord():
    id = request.form['id']
    with open("records.json", "r") as f:
        data = json.load(f)
        for item in data['details']:
            if int(id) == int(item['id']):		
            	return f"Name: <b>{str(item['name'])}</b><br>Surname: <b>{str(item['surname'])}</b><br><br><br>Timestamp: <b>{str(item['timestamp'])}</b>"

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0',port = 8000)

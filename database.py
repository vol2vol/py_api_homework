from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Создаем базу данных, если ее нет
conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS blocks (name TEXT, description TEXT)''')
conn.close()

@app.route('/add_block', methods=['POST'])
def add_block():
    data = request.get_json()
    name = data.get('name')
    description = data.get('description')

    conn = sqlite3.connect("mydata.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO blocks (name, description) VALUES (?, ?)", (name, description))
    conn.commit()
    conn.close()
    
    return "Block added successfully"

if __name__ == '__main__':
    app.run()
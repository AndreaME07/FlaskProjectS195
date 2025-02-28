from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    connection = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        port="3306",
        database="db"
    )

    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
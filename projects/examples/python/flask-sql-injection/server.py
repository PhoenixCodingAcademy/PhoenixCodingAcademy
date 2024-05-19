'''
Here is a flask web site that is vulnerable to SQL injection.
The code is simple and straightforward. The user can enter their first and last name into a form,
and the data is inserted into a SQLite database.
The problem is that the code does not properly escape the user input,
so an attacker can inject SQL commands into the form fields.
This is a common security vulnerability that can be exploited to steal data, delete data, or even take control of the server.

OPEN A TERMINAL WINDOW:
set FLASK_DEBUG=true
python server.py --debug run

OPEN IN BROWSER:
http://127.0.0.1:5000

USE SQLITE BROWSER TO VIEW THE DATABASE:
https://sqlitebrowser.org/

'''

import argparse
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Connect to the SQLite database
def ensureDatabase():
  # Add code to ensure the database exists
  connection = sqlite3.connect('database.db')
  cursor = connection.cursor()

  # Create the "person" table if it doesn't exist
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS person (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      firstname TEXT,
      lastname TEXT,
      favorite_color TEXT -- private data
    )
  ''')
  connection.commit()
  connection.close()


@app.route('/people', methods=['GET'])
def get_people():
  # Create as lastname string that would cause an SQL injection that would return the favorite_color of all records
  # lastname = "'; SELECT favorite_color FROM person WHERE 1=1; --"

  # Get the data from the "person" table
  with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT id, firstname, lastname FROM person')
    people = cursor.fetchall()
  return render_template('index.html', data= {'people': people})


@app.route('/people', methods=['POST'])
def post_people():
  # Get the form data
  firstname = request.form['firstname']
  lastname = request.form['lastname']
  favorite_color = request.form['favorite_color']

  # Insert the data into the "person" table
  with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    # Check if a record with the same name already exists
    cursor.execute('SELECT id FROM person WHERE firstname = ? AND lastname = ?', (firstname, lastname))
    person = cursor.fetchone()
    if person:
      # If a record with the same name already exists, update it
      cursor.execute('UPDATE person SET favorite_color = ? WHERE id = ?', (favorite_color, person[0]))  # SQL injection vulnerability
    cursor.execute('INSERT INTO person (firstname, lastname, favorite_color) VALUES (?, ?, ?)', (firstname, lastname))
    conn.commit()

  render_template('add_person.html')


@app.route('/people', methods=['GET'])
def list_people():
  with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT id, firstname, lastname FROM person')
    people = cursor.fetchall()
  render_template('list_people.html', data= {'people': people})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  print(f"catch_all: {path}")
  return render_template('index.html')


if __name__ == '__main__':
  ensureDatabase()
  parser = argparse.ArgumentParser()
  parser.add_argument('-p', '--port', type=int, default=5000)
  parser.add_argument('--debug', action='store_true', default=False, help='Enable debug mode. Watch for changes.')
  args = parser.parse_args()
  app.run(debug=args.debug, port=args.port)

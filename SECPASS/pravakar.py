# pifrom flask import Flask, render_template, jsonify, request
from urllib.request import Request
from urllib.robotparser import RequestRate
from wsgiref.util import request_uri
from flask import Flask, jsonify , render_template
from flask_mysqldb import MySQL
import encrypt

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"  # Change this to your MySQL host
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Newpr@va2003"
app.config["MYSQL_DB"] = "passworddatabase"  # Change this to your MySQL database name

mysql = MySQL(app)

app.config['TEMPLATES_AUTO_RELOAD'] = True
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save_password():
    website = request_uri.json["website"]
    username = RequestRate.json["username"]
    encrypted_password = encrypt.encrypt(Request.json["password"])

    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO passwords (website, username, password) VALUES (%s, %s, %s)",
        (website, username, encrypted_password),
    )
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Password saved successfully"})

@app.route("/passwords", methods=["GET"])
def get_passwords():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM passwords")
    passwords = [
        {"website": row[1], "username": row[2], "password": encrypt.decrypt(row[3])}
        for row in cur.fetchall()
    ]
    cur.close()

    return jsonify(passwords)

if __name__ == "__main__":
    app.run(debug=True)

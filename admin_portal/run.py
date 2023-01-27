from flask import Flask, render_template, flash, redirect, url_for, session, logging, request, send_file
import sqlite3
import pyexcel
import pandas as pd

userConn = sqlite3.connect('../user.sqlite', check_same_thread=False)
userCur = userConn.cursor()

attenConn = sqlite3.connect('../attendance.sqlite', check_same_thread=False)
attenCur = attenConn.cursor()


app = Flask(__name__)

# check if authentication is done
authentication_done = False

# cur.execute("""Insert OR REPLACE INTO user (name, password) Values( "admin", "admin")""")
# conn.commit()
# cur2.execute("""CREATE TABLE "21-JAN-22" ("reg_no"	INTEGER NOT NULL,"name"	TEXT NOT NULL,"department"	TEXT NOT NULL,"email"	TEXT NOT NULL,"date"	TEXT NOT NULL,"status"	TEXT NOT NULL,"time"	TEXT NOT NULL,PRIMARY KEY("reg_no"));""")
# conn2.commit()

# attenCur.execute("""Insert OR REPLACE INTO attendance_21_JAN_22 (reg_no, name, department, email, date, status, time) Values( 219301073, "gaurav", "CSE", "gaurav.219301072@muj.manipal.edu", "21-Jun-22", "P", "06:09:00")""")
# attenConn.commit()




@app.route("/", methods=["GET", "POST"])
def login():
    global authentication_done
    authentication_done = False
    if request.method == "POST":
        username = request.form["username"].lower()
        password = request.form["password"]

        userCur.execute('''Select * From user Where name = ? And password = ?''', (username, password))
        row = userCur.fetchone()

        if row is not None:

            authentication_done = True
            return redirect("/view_attendance")
        else:
            return redirect('/')

    return render_template("login.html")


@app.route("/view_attendance", methods=["GET", "POST"])
def view_attendance():
    global authentication_done
    # get request
    if authentication_done:
        attenCur.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        attendance_record = attenCur.fetchall()

        return render_template("user.html", attendance_record=attendance_record)

    return redirect('/')


@app.route("/xlsx", methods=["GET", "POST"])
def xlsx():
    if request.method == "POST":
        date = request.form["date"]
        attenCur.execute("Select * From " + date)
        data = attenCur.fetchall()
        pyexcel.createExcel(date, data)

        df = pd.read_excel("Excel/" + date + ".xlsx")
        # json = df.to_json

        return df.to_html()

    return redirect('/')


@app.route('/download', methods=["GET", "POST"])
def download_file():
    path = "Excel/" + request.form["filename"] + ".xlsx"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9998, use_reloader=True, debug=True)

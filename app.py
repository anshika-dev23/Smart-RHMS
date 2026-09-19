from flask import Flask, render_template, request, redirect, url_for
from database import create_database
import sqlite3

app = Flask(__name__)

create_database()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/patients")
def patients():

    connection = sqlite3.connect("database.db")

    patients = connection.execute("""
        SELECT id, name, age, gender, village
        FROM patients
    """).fetchall()

    connection.close()

    return render_template("patients.html", patients=patients)

@app.route("/patient/<int:patient_id>")
def patient_detail(patient_id):

    connection = sqlite3.connect("database.db")

    patient = connection.execute("""
        SELECT id, name, age, gender, village, phone,
               emergency_contact, blood_group
        FROM patients
        WHERE id = ?
    """, (patient_id,)).fetchone()

    vitals = connection.execute("""
        SELECT blood_pressure, spo2, temperature, pulse, recorded_at, status
        FROM vitals
        WHERE patient_id = ?
        ORDER BY recorded_at DESC
        LIMIT 1
    """, (patient_id,)).fetchone()

    connection.close()

    return render_template(
        "patient_detail.html",
        patient=patient,
        vitals=vitals
    )
@app.route("/vitals/<int:patient_id>", methods=["GET", "POST"])
def add_vitals(patient_id):

    if request.method == "POST":

        blood_pressure = request.form["blood_pressure"]
        spo2 = request.form["spo2"]
        temperature = request.form["temperature"]
        pulse = request.form["pulse"]

        # Default status
        status = "Normal"

        # Check blood pressure
        try:
            systolic, diastolic = blood_pressure.split("/")
            systolic = int(systolic)
            diastolic = int(diastolic)

            if systolic >= 140 or diastolic >= 90:
                status = "Attention Needed"

        except ValueError:
            status = "Check BP"

        # Save vitals
        connection = sqlite3.connect("database.db")

        connection.execute("""
            INSERT INTO vitals
            (patient_id, blood_pressure, spo2, temperature, pulse, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            patient_id,
            blood_pressure,
            spo2,
            temperature,
            pulse,
            status
        ))

        connection.commit()
        connection.close()

        return redirect(url_for(
            "patient_detail",
            patient_id=patient_id
        ))

    return render_template(
        "vitals.html",
        patient_id=patient_id
    )
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        gender = request.form["gender"]
        village = request.form["village"]
        phone = request.form["phone"]
        emergency_contact = request.form["emergency_contact"]
        blood_group = request.form["blood_group"]

        connection = sqlite3.connect("database.db")

        connection.execute("""
            INSERT INTO patients
            (name, age, gender, village, phone, emergency_contact, blood_group)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            name,
            age,
            gender,
            village,
            phone,
            emergency_contact,
            blood_group
        ))

        connection.commit()
        connection.close()

        return redirect(url_for("home"))

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)
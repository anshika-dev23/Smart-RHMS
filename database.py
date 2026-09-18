import sqlite3
import csv
def create_database():
    connection=sqlite3.connect("database.db")
    connection.execute("""
    CREATE TABLE IF NOT EXISTS patients(id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT,
    village TEXT,
    phone TEXT,
    emergency_contact TEXT,
    blood_group TEXT)""")
    connection.commit()
    connection.close()

def insert_patient(data):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(
        """INSERT INTO patients
        (name, age, gender, village, phone, emergency_contact, blood_group)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (
            data.get('name'),
            data.get('age'),
            data.get('gender'),
            data.get('village'),
            data.get('phone'),
            data.get('emergency_contact'),
            data.get('blood_group'),
        ),
    )
    conn.commit()
    conn.close()

def get_all_patients():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, age, gender, village, phone, emergency_contact, blood_group FROM patients ORDER BY id DESC"
    )
    rows = cur.fetchall()
    conn.close()
    return rows

def get_patient_by_id(pid):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(
        "SELECT id, name, age, gender, village, phone, emergency_contact, blood_group FROM patients WHERE id = ?",
        (pid,),
    )
    row = cur.fetchone()
    conn.close()
    return row

def update_patient(pid, data):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute(
        """UPDATE patients SET name=?, age=?, gender=?, village=?, phone=?, emergency_contact=?, blood_group=? WHERE id=?""",
        (
            data.get('name'),
            data.get('age'),
            data.get('gender'),
            data.get('village'),
            data.get('phone'),
            data.get('emergency_contact'),
            data.get('blood_group'),
            pid,
        ),
    )
    conn.commit()
    conn.close()

def delete_patient(pid):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM patients WHERE id = ?", (pid,))
    conn.commit()
    conn.close()


def export_patients_csv(file_path='patients.csv'):
    rows = get_all_patients()
    with open(file_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['id','name','age','gender','village','phone','emergency_contact','blood_group'])
        writer.writerows(rows)
    return file_path
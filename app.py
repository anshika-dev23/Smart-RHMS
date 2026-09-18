from flask import Flask,render_template,request,redirect,url_for,Response
from database import create_database, insert_patient, get_all_patients, get_patient_by_id, update_patient, delete_patient

app=Flask(__name__)
create_database()

@app.route("/")
def home():
    patients = get_all_patients()
    msg = request.args.get('msg')
    return render_template("index.html", patients=patients, message=msg)

@app.route('/add_patient', methods=['POST'])
def add_patient():
    data = {k: request.form.get(k) for k in ('name','age','gender','village','phone','emergency_contact','blood_group')}
    insert_patient(data)
    return redirect(url_for('home', msg='Patient added'))

@app.route('/edit/<int:pid>', methods=['GET'])
def edit_patient(pid):
    patient = get_patient_by_id(pid)
    if not patient:
        return redirect(url_for('home', msg='Patient not found'))
    return render_template('edit.html', patient=patient)

@app.route('/update_patient/<int:pid>', methods=['POST'])
def update_patient_route(pid):
    data = {k: request.form.get(k) for k in ('name','age','gender','village','phone','emergency_contact','blood_group')}
    update_patient(pid, data)
    return redirect(url_for('home', msg='Patient updated'))


@app.route('/delete_patient/<int:pid>', methods=['POST'])
def delete_patient_route(pid):
    delete_patient(pid)
    return redirect(url_for('home', msg='Patient deleted'))


@app.route('/export_csv')
def export_csv():
    import io, csv
    rows = get_all_patients()
    si = io.StringIO()
    w = csv.writer(si)
    w.writerow(['id','name','age','gender','village','phone','emergency_contact','blood_group'])
    w.writerows(rows)
    output = si.getvalue()
    return Response(output, mimetype='text/csv', headers={'Content-Disposition':'attachment;filename=patients.csv'})

if __name__=="__main__":
    app.run(debug=True,port=5002)
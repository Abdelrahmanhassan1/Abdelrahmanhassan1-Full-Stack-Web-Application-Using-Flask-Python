import mysql.connector

from flask import Flask, render_template, request, url_for

mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    passwd = "mysql",
    database = "icuRooms"
)

mycursor = mydb.cursor()

app = Flask(__name__)

# Home

@app.route("/")
def home():
    return render_template("home.html")


# Sign In Forms

@app.route("/signin")
def signIn():
    return render_template("signIn.html")


@app.route("/signin/doctor")
def signInDoc():
    return render_template("SignInForms/signInDoc.html")


@app.route("/signin/nursery")
def signInNursery():
    return render_template("SignInForms/signInNursery.html")


@app.route("/signin/patient")
def signInPatient():
    return render_template("SignInForms/signInPatient.html")


# Contact Us Form

@app.route("/contactUs", methods=['GET', 'POST'])
def contactUs():
    if request.method == 'POST':
        email = request.form['email']
        statement = request.form['statement']
        sql = 'INSERT INTO contactUsProblems(email, statement) VALUES(%s, %s)'
        val = (email, statement)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("contactUs.html")
    else:
        return render_template("contactUs.html")


# Admin

@app.route("/admin", methods = ['GET', 'POST'])
def admin():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']
        if name == 'admin' and password == 'admin':
            return render_template("adminPage/adminPage.html")
        else:
            return render_template("admin.html")          
    else:
        return render_template("admin.html")


@app.route("/admin/privilages")
def adminPrivilages():
    return render_template("adminPage/adminPage.html")

# Admin Forms
 
@app.route("/admin/privilages/bedform", methods = ['GET', 'POST'])
def bedForm():
    if request.method == 'POST':
        bednum = request.form['bedNum']
        roomnum = request.form['roomNum']
        status = request.form['status']
        sql = 'INSERT INTO Beds(bedNum, roomNum, status) VALUES(%s, %s, %s)'
        val = (bednum, roomnum, status)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("adminForm/bedForm/index.html")
    
    else:
        return render_template("adminForm/bedForm/index.html")


@app.route("/admin/privilages/medicalform", methods = ['GET', 'POST'])
def medicalForm():
    if request.method == 'POST':
        devicename = request.form['devicename']
        serialnumber = request.form['serialnumber']
        prodDate = request.form['prodDate']
        manufacturer = request.form['manufacturer']
        
        sql = 'INSERT INTO MedicalEquipment(serialNum, name, manufacturer, prodDate) VALUES(%s, %s, %s, %s)'
        val = (serialnumber, devicename, manufacturer, prodDate)
        mycursor.execute(sql, val)
        mydb.commit()

        return render_template("adminForm/medicalForm/index.html")
    else:
        return render_template("adminForm/medicalForm/index.html")



@app.route("/admin/privilages/doctorform",  methods = ['GET', 'POST'])
def doctorForm():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        mlnumber = request.form['mlnumber']
        id = request.form['id']
        email = request.form['email']
        password = request.form['password']
        sql = 'INSERT INTO Doctor(MLNum, id, name, age, email, password) VALUES(%s, %s, %s, %s, %s, %s)'
        val = (mlnumber, id, name, age, email, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("adminForm/doctorForm/index.html")
    else:
        return render_template("adminForm/doctorForm/index.html")

 

@app.route("/admin/privilages/nurseryform", methods = ['GET', 'POST'])
def nurseryForm():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        mlnumber = request.form['mlnumber']
        id = request.form['id']
        email = request.form['email']
        password = request.form['password']
        sql = 'INSERT INTO NurseryStuff(MLNum, id, name, age, email, password) VALUES(%s, %s, %s, %s, %s, %s)'
        val = (mlnumber, id, name, age, email, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("adminForm/nurseryForm/index.html")
    else:
        return render_template("adminForm/nurseryForm/index.html")


@app.route("/admin/privilages/patientform", methods = ['GET', 'POST'])
def patientForm():
    
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        id = request.form['id']
        entrydate = request.form['entrydate']
        address = request.form['address']
        password = request.form['password']
        sql = 'INSERT INTO Patient(id, name, age, entryDate, address, password) VALUES(%s, %s, %s, %s, %s, %s)'
        val = (id, name, age, entrydate, address, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("adminForm/patientForm/index.html")
    
    else:
        return render_template("adminForm/patientForm/index.html")


@app.route("/admin/privilages/roomform", methods = ['GET', 'POST'])
def roomForm():
    if request.method == 'POST':
        roomnum = request.form['roomnum']
        numofbeds = request.form['numofbeds']
        sql = 'INSERT INTO Rooms(roomNum, numOfBeds) VALUES(%s, %s)'
        val = (roomnum, numofbeds)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template("adminForm/roomsForm/index.html")
    else:
        return render_template("adminForm/roomsForm/index.html")

# Admin View Forms

@app.route("/admin/privilages/bedview")
def bedView():
    return render_template("adminView/bedView/index.html")

@app.route("/admin/privilages/medicalview")
def medicalView():
    return render_template("adminView/medicalView/index.html")

@app.route("/admin/privilages/doctorview")
def doctorView():
    return render_template("adminView/doctorView/index.html")

@app.route("/admin/privilages/nurseryview")
def nurseryView():
    return render_template("adminView/nurseryView/index.html")

@app.route("/admin/privilages/patientview")
def patientView():
    return render_template("adminView/patientView/index.html")

@app.route("/admin/privilages/roomview")
def roomView():
    return render_template("adminView/roomsView/index.html")




if __name__ == "__main__":
    app.run(debug=True)

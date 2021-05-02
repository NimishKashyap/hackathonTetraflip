from flask import *
import pyrebase

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyDrT6qDDzh_Z9qIXRfbkzeihswnGZkA6ic",
    "authDomain": "hackathonnk.firebaseapp.com",
    "databaseURL": "https://hackathonnk-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "hackathonnk",
    "storageBucket": "hackathonnk.appspot.com",
    "messagingSenderId": "911312261680",
    "appId": "1:911312261680:web:f78e00cb10ee54c83b13f5",
    "measurementId": "G-77W18ZLQXK"
}
firebase = pyrebase.initialize_app(config)
database = firebase.database()

loggedIn = True

def checkPass(password, confirm_password):
    return password == confirm_password

@app.route("/",methods=["GET","POST"])
def home():
    return render_template("index.html")

@app.route("/signIn", methods = ["GET","POST"])
def signin():
    if request.method == "POST":
        var = request.form["iuname"]
        password = request.form["pass"]
        print(var, password)
    return render_template("login.html")


@app.route("/signUp", methods = ["GET","POST"])
def signUp():
    if request.method == "POST":
        name = request.form["name"]
        fname = request.form["fname"]
        anum = request.form["anumber"]
        mnumber = request.form["mnumber"]
        
        password = request.form["password"]
        c_password = request.form["cpassword"]
        data = {"name" : name, "fname": fname, "anum" : anum, "mnumber": mnumber, "password": password, "c_password" : c_password}
        if checkPass(password,c_password):
            database.child("users").push(data)
            get = database.child("users").get()
            print(get)
            
            return render_template("index.html", name = get)
        
    return render_template("signup.html")

@app.route("/main", methods= ["GET","POST"])
def main():
    if loggedIn:
        return render_template("main.html", name = [1,2,3])
    else:
        return redirect("/signIn")
if __name__=="__main__":
    app.run(debug=True)

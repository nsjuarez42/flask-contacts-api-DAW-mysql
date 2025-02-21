from flask import Flask,request,jsonify
from config import Development,Build
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config.from_object(Development)

mysql= MySQL(app)

def tup_to_dict(tup):
    return {"id":tup[0],"alias":tup[1],"name":tup[2],"phone":tup[3],"email":tup[4]}

@app.route("/contacts",methods=["GET","POST"])
def contacts():
    db = mysql.get_db()
    cursor = db.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM contact")
        contacts = cursor.fetchall()
        cursor.close()
        return jsonify(contacts)
    
    elif request.method == "POST":
        try:
            name,email,phone,alias = request.json["name"],request.json['email'],request.json["phone"],request.json["alias"]
            print(name,email,phone,alias)
        except KeyError:
            return jsonify({"error":"Data format not valid"}),400
        try:
            cursor.execute("INSERT INTO contact(id,name,phone,alias,email) VALUES(NULL,%s,%s,%s,%s)",(name,phone,alias,email))
            
        except Exception as e:
            print(e)
            return jsonify({"error":"Server error"}),500
        db.commit()
        cursor.execute("SELECT * FROM contact WHERE id=%s",(cursor.lastrowid))
        contact = cursor.fetchall()[0]
        contact_dict = tup_to_dict(contact)
        cursor.close()
        return jsonify(contact_dict)
 


@app.route("/contact/<id>",methods=["GET","PUT","DELETE"])
def contact(id):

    db = mysql.get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM contact WHERE id=%s",(id))

    contacts = cursor.fetchall()
    print(contacts)
    if len(contacts) == 0:
        return jsonify({"error":"User not found"})
    contact = tup_to_dict(contacts[0])
    
    if request.method == "GET":
        return jsonify(contact)

    elif request.method == "PUT":
        try:
            name,email,phone,alias = request.json["name"],request.json["email"],request.json["phone"],request.json["alias"]
        except KeyError:
            return jsonify({"error":"Data format not valid"}),400
    
        cursor.execute("UPDATE contact SET name=%s,phone=%s,email=%s,alias=%s WHERE id=%s",(name,phone,email,alias,id))

        cursor.execute("SELECT * FROM contact WHERE id=%s",(id))

        return jsonify(tup_to_dict(cursor.fetchall()[0]))

    elif request.method == "DELETE":
        
        try:
            cursor.execute("DELETE FROM contact WHERE id=%s",(id))
            db.commit()
        except Exception as e:
            print(e)
            return jsonify({"error":"server error"}),500

        return jsonify({"msg":"Deleted successfully","contact":contact})


if __name__ == "__main__":
    app.run(debug=True)
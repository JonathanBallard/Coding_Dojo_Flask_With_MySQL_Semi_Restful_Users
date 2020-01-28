from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)



@app.route('/')
def index():
    mysql = connectToMySQL("create_and_read_pets")
    pets = mysql.query_db("SELECT * FROM pets;")
    print(pets)
    return render_template("index.html", all_pets = pets)
            
@app.route("/create_pet", methods=["POST"])
def add_friend_to_db():
    print(request.form)
    mysql = connectToMySQL("create_and_read_pets")
    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES (%(name)s, %(type)s, NOW(), NOW());"
    data = {
        "name": request.form['name'],
        "type": request.form['type']
    }
    new_pet_id = mysql.query_db(query, data)



    # SQL INJECTION

    # mysql = connectToMySQL("create_and_read_pets")
    # name = request.form['name']
    # typeA = request.form['type']
    # query = f"INSERT INTO pets (name, type, created_at, updated_at) VALUES ({name}, {typeA}, NOW(), NOW());"
    # new_pet_id = mysql.query_db(query)






    
    return redirect("/")
    # QUERY: INSERT INTO first_flask (first_name, last_name, occupation, created_at, updated_at) 
    #                         VALUES (fname from form, lname from form, occupation from form, NOW(), NOW());

if __name__ == "__main__":
    app.run(debug=True)
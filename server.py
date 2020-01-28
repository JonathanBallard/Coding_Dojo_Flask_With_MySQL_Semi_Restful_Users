from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)



@app.route('/users')
def index():
    mysql = connectToMySQL("semi_restful_users")
    users = mysql.query_db("SELECT * FROM users;")
    print(users)
    return render_template("index.html", all_users = users)
    
    
@app.route('/users/new')
def new_user():
    return render_template("new_user.html")

@app.route('/users/<id>')
def user_id(id):
    return render_template("user.html", user_id = id)





@app.route("/users/create", methods=["POST"])
def add_user_to_db():
    print(request.form)
    mysql = connectToMySQL("semi_restful_users")
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s);"
    data = {
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }
    new_user_id = mysql.query_db(query, data)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True)
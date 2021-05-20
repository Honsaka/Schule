from bottle import run , request , route
@route("/login")
def login():
    username = request.query.username
    password = request.query.password

    return "login :" + username + "password: " + password
if __name__ =="__main__":
    run(debug=True , reloader=True)
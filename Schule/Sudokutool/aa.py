from bottle import run, route, request

@route("/a")
def querytest():
    param1 = request.query.param1
    param2 = request.query.param2

    return "a" + param1 + "b" + param2

if __name__=="__main__":
    run(debug=True , reloader=True)
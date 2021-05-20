from bottle import run , route ,template
@route("/class/<klasse>")
def first(klasse):
    return template("first", klasse=klasse)
if __name__=="__main__":
    run()
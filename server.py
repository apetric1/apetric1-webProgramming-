from bottle import route, run, template

@route("/")
def get_index():
    return ("hello!")

@route("/hello")
@route("/hello/<name>")
def get_hello(name="world"):
    return template("hello.tpl", name=name)

run(host="localhost", port=3000)
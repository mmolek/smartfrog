import flask
from shelljob import proc

app = flask.Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There! Test lala!</h1>"


@app.route( '/version' )
def stream():
    g = proc.Group()
    p = g.run( [ "cat", ".git/refs/heads/master" ] )

    def read_process():
        while g.is_pending():
            lines = g.readlines()
            for proc, line in lines:
                yield line

    return flask.Response( read_process(), mimetype= 'text/plain' )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

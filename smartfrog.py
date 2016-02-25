import flask
from shelljob import proc

application = flask.Flask(__name__)

@application.route("/")
def hello():
    return "<h1>Hello There SmartFrog! :) :)</h1>"


@application.route( '/version' )
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
    application.run(debug=True, host='0.0.0.0')


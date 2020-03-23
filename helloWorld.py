from bottle import route, run, template

@route('/hello/world')
def index():
    return template('<b>Hello World</b>!')


@route('/hello/world2')
def index2():
    return template('<b>Hello World2</b>!')

run(host='localhost', port=8080, debug=True)
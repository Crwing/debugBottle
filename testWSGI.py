#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 13:47
# @Author  : icon
# @File    : class_decorator.py
from wsgiref.simple_server import make_server


class WSGIapp:
    def __init__(self):
        self.routes = {}

    def route(self, url=None):
        def decorator(func):
            self.routes[url] = func
            return func

        return decorator

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']
        if path in self.routes:
            status = '200 OK'
            response_headers = [('Content-Type', 'text/plain')]
            start_response(status, response_headers)
            return self.routes[path]()
        else:
            status = '404 Not Found'
            response_headers = [('Content-Type', 'text/plain')]
            start_response(status, response_headers)
            return '404 Not Found!'


app = WSGIapp()


@app.route('/')
def index():
    return ['index']


@app.route('/hello')
def hello():
    return ['hello world']


httpd = make_server('localhost', 8888, app)
httpd.serve_forever()
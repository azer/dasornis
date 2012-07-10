from dispatcher import Dispatcher

def serve(hostname,port,urlmap):
    # DASORNIS Wrapper for Simple Server of wsgi
    from wsgiref.simple_server import make_server
    srv = make_server( hostname, port, Dispatcher( urlmap )  )
    srv.serve_forever()



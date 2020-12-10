import cgi,json

def read_stat():
    with open('rain_state') as t:
        return t.read()

def application(env, start_response):
    if env['REQUEST_METHOD'] == 'GET':
        response = read_state()
    else:
        response = '{"error":"not allowed"}'
    start_response('200',[('Content-Type','text/html'),('Access-Control-Allow-Origin','*')])
    return[response]

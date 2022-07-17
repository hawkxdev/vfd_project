# VIEWS #

def request_get(request, param, else_val=None, to_bool=False):
    res = request.GET[param] if param in request.GET else else_val
    if to_bool:
        res = res == '1'
    return res

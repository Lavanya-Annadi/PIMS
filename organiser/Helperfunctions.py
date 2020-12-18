import json


def byte_dict_conv(byte_string):
    str_val=byte_string.decode('UTF-8')
    dict_val=json.loads(str_val)
    return dict_val

def list_conv(querysetval):

    listvalues=list(querysetval)

    for singlelist in listvalues:
        del singlelist["username"]
        del singlelist["id"]

    return listvalues









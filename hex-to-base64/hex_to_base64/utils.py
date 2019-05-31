def translate(hex_string):
    '''a utility that will translate a hexadecimal string to base64.

    Args
    hex_string - A Hex String

    Returns
    A base64 String
    '''
    return hex_string.decode('hex').encode('base64')

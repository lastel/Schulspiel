import codecs

def Verschlüsseln(String):
    return codecs.encode(String, 'rot13')

def Entschlüsseln(String):
    return codecs.decode(String, 'rot13')

def data_recovery(data):
    headers={rb'\x89PNG\r\n\x1a\n':"PNG",rb'\xff\xd8\xff':"JPEG",rb'\x42\x4d':"BMP",rb'\x49\x49\x2a\x00':"TIFF",rb'\x47\x49\x46\x38':"GIF",rb'\x50\x4b\x03\x04':"ZIP",rb'\x7fELF':"ELF",rb'\x25\x50\x44\x46':"PDF",rb'\x49\x44\x33':"MP3",rb'\xff\xfb':"MPEG",rb'\x00\x00\x01\x00':"PDDF",rb'\x00\x01\x00\x00':"ICO"}
    named_header=[]
    for i in headers:
        if i in data:
            named_header.append(headers[i])
        else:
            pass
    return named_header
data=input("please enter the data:")
print(data_recovery(data.encode()))
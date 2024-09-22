def data_recovery(data):
    header1=rb'\x89PNG\r\n\x1a\n' # PNG header
    header2=rb'\xff\xd8\xff' # JPEG header
    header3=rb'\x42\x4d' # BMP header
    header4=rb'\x49\x49\x2a\x00' #TIFF header
    header5=rb'\x47\x49\x46\x38' # GIF header
    header6=rb'\x50\x4b\x03\x04' # ZIP header
    header7=rb'\x7fELF' # ELF header
    header8=rb'\x25\x50\x44\x46' # PDF header
    header9=rb'\x49\x44\x33' # MP3 header
    header10=rb'\xff\xfb' # MPEG header
    header11=rb'\x00\x00\x01\x00' # PDDF header
    header12=rb'\x00\x01\x00\x00' # ICO header
    x=[]
    if header1 in data:
        x.append("PNG")
    if header2 in data:
        x.append("JPEG")
    if header3 in data:
        x.append("BMP")
    if header4 in data:
        x.append("TIFF")
    if header5 in data:
        x.append("GIF")
    if header6 in data:
        x.append("ZIP")
    if header7 in data:
        x.append("ELF")
    if header8 in data:
        x.append("PDF")
    if header9 in data:
        x.append("MP3")
    if header10 in data:
        x.append("MPEG")
    if header11 in data:
        x.append("PDDF")
    if header12 in data:
        x.append("ICO")
    return x
input_str=input("please enter the data:")
data=bytes(input_str,encoding='UTF8')
print(data_recovery(data))
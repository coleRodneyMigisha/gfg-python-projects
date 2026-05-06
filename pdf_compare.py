import hashlib


def get_hash(file_name):
    hshobj = hashlib.sha256()
    file = open(file_name, 'rb')
    while True:
        chunk = file.read(1024)
        hshobj.update(chunk)
        if not chunk:
            break
    return hshobj.hexdigest()


def compare(one, two):
    if one == two:
        print("SAMESIEEESSSS!")
    else:
        print("Different pdfs here! Not identitcal.")


pdf1_hash = get_hash("pdf1.pdf")
pdf2_hash = get_hash("pdf2.pdf")
pdf3_hash = get_hash("pdf3.pdf")
pdf4_hash = get_hash("pdf4.pdf")

compare(pdf2_hash, pdf2_hash)
compare(pdf1_hash, pdf2_hash)
compare(pdf3_hash, pdf1_hash)
compare(pdf1_hash, pdf4_hash)
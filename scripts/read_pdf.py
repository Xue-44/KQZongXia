import PyPDF2
f = open('广汽传祺新媒体营销通知.pdf', 'rb')
r = PyPDF2.PdfReader(f)
for i, page in enumerate(r.pages[:5]):
    print(f'=== PAGE {i+1} ===')
    print(page.extract_text())
f.close()
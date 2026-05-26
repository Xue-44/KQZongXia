from pdfminer.high_level import extract_text
text = extract_text('广汽传祺新媒体营销通知.pdf')
print(text[:10000])
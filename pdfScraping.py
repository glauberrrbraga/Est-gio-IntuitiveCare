from os import name
import camelot

tables = camelot.read_pdf('TISS.pdf', pages='79, 80, 81, 82, 83, 84, 85')
tables.export('Teste_Intuitive_Care_Glauber', f='csv', compress=True)
tables.export

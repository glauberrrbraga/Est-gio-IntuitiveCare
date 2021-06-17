import camelot

tables = camelot.read_pdf('TISS.pdf', pages='79, 80, 81, 82, 83, 84, 85')
tables.export('TISS.csv', f='csv')
tables.export

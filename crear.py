import xlsxwriter


# crear un nuevo archivo y una hoja de trabajo.
workbook = xlsxwriter.Workbook('demo.xlsx')
worksheet = workbook.add_worksheet()

# hacemos mas grande la columa A 
worksheet.set_column('A:A', 20)

# agregamos a la variable bold atributos de formato
bold = workbook.add_format({'bold': True})

# agregamos texto simple
worksheet.write('A1', 'Hello')

# agreganmos texto con formato
worksheet.write('A2', 'World', bold)

# escribir datos usando numeros para fila y columnas
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

# insertar una imagen
#worksheet.insert_image('B5', 'logo.png')

workbook.close()
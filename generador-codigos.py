import sys
import xlrd

values = "values ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')"
query_string = "INSERT INTO {table} (d_codigo,d_asenta,d_tipo_asenta,D_mnpio,d_estado,d_ciudad,d_CP,c_estado,c_oficina,c_CP,c_tipo_asenta,c_mnpio,id_asenta_cpcons,d_zona,c_cve_ciudad)"

def one_file(book, insert):
    sheet_names = book.sheet_names()

    sheet_names.remove('Nota')

    file = open('sql/codigos_postales_todos_los_estados.sql', 'w')

    for name in sheet_names:
        sheet = book.sheet_by_name(name)
        file.write('\n\n-- Codigos postales para {}\n\n'.format(name))
        for index in range(sheet.nrows):
            row = sheet.row(index)
            inserted_values = values.format( *( str(cell.value) for cell in row ) )
            query = "{} {};\n".format(insert, inserted_values)
            file.write(query)

    file.close()

def multifile(book, insert):
    sheet_names = book.sheet_names()

    sheet_names.remove('Nota')

    for name in sheet_names:
        file = open('sql/{}.sql'.format(name), 'w')
        sheet = book.sheet_by_name(name)
        file.write('\n\n-- Codigos postales para {}\n\n'.format(name))
        for index in range(sheet.nrows):
            row = sheet.row(index)
            inserted_values = values.format( *( str(cell.value) for cell in row ) )
            query = "{} {};\n".format(insert, inserted_values)
            file.write(query)

        file.close()

def main(archivos_separados=False, **kwargs):

    print("Cargando archivo, esto puede tardar un poco...\n\n\n")

    if 'table' not in kwargs:
        raise Exception('El parámetro table es requerido')


    insert = query_string.format(table=kwargs['table'])

    book = xlrd.open_workbook('source/CPdescarga.xls')

    if archivos_separados:
        multifile(book, insert)
    else:
        one_file(book, insert)


if __name__=='__main__':
    args = sys.argv[1:]
    dict_args = dict(arg.split('=') for arg in sys.argv[1:] if '=' in arg)

    if '--archivos-separados' in args:
        main(**dict_args, archivos_separados=True)
    else:
        main(**dict_args)

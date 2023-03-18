from db import get_connection

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call consultar_alumno()')
        resulset=cursor.fetchall()
        for row in resulset:
            print(row)
except Exception as ex:
    print(ex)


"""try:
    connection = get_connection
    with connection.cursor() as cursor:
        cursor.execuete("call agregar_alumno()")
    connection.commit()
    connection.close()
except Exception as ex:
    print("ERROR") """

# try:
#     connection=get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('call agregar_alumno(%s, %s, %s)',('Arturo','Alba', 'alba@gmail.com'))
#         resulset=cursor.fetchall()
#         for row in resulset:
#             print(row)
# except Exception as ex:
#     print('ERROR')



# try:
#     connection=get_connection()
#     with connection.cursor() as cursor:
#         cursor.execute('call consulta_alumnos(%s)',(2,))
#         resulset=cursor.fetchall()
#         for row in resulset:
#             print(row)
# except Exception as ex:
#     print('ERROR')


try:
    connection=get_connection()
    with connection.cursor() as cursor:
        cursor.execute('call agregar_alumno(%s, %s, %s)',('Arturo','Alba', 'alba@gmail.com'))
    connection.commit()
    connection.close()
except Exception as ex:
  print(ex)
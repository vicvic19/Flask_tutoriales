import psycopg2

conexion = psycopg2.connect(user = 'postgres', password = 'admin', host= '127.0.0.1', port = '5432', database = 'test_db')

tipo = input("Ingresa lo que harás ['Mostrar todos', 'Mostrar uno', 'Mostrar uno por uno']: ")
if tipo == 'Mostrar todos':
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM persona'
                cursor.execute(sentencia)
                registros = cursor.fetchall()
                print(registros)

    except Exception as e:
        print(f'Ocurrio un error: {e}')

    finally:
        conexion.close()

if tipo == 'Mostrar uno':
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM persona where id_persona = %s'
                id_persona = input('Proporciona el id a buscar: ')
                cursor.execute(sentencia, (id_persona,))
                registros = cursor.fetchone()
                print(registros)

    except Exception as e:
        print(f'Ocurrio un error: {e}')

    finally:
        conexion.close()

if tipo == 'Mostrar uno por uno':
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'SELECT * FROM persona where id_persona IN %s'
                entrada = input('Proporciona los id\'s a buscar separados por coma: ')
                llaves_primarias = (tuple(entrada.split(',')), )
                cursor.execute(sentencia, llaves_primarias)
                registros = cursor.fetchall()
                for registro in registros:
                    print(registro)

    except Exception as e:
        print(f'Ocurrio un error: {e}')

    finally:
        conexion.close()
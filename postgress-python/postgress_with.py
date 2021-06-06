import psycopg2

conexion = psycopg2.connect(user = 'postgres', password = 'admin', host= '127.0.0.1', port = '5432', database = 'test_db')

tipo = input("Ingresa lo que harás ['Mostrar todos', 'Mostrar uno', 'Mostrar uno por uno','Insertar uno', 'Insertar varios', 'Actualizar uno', 'Actualizar varios']: ")
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

if tipo == 'Insertar varios':
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
                valores = (
                    ('Ramon', 'Ramirez', 'rramirez@mail.com'),
                    ('Pedro', 'Ramirez', 'pramirez@mail.com'),
                    ('Sebastian', 'Ramirez', 'sramirez@mail.com')
                )

                cursor.executemany(sentencia, valores)
                registros_insertados = cursor.rowcount
                print(f'Registros insertados: {registros_insertados}')

    except Exception as e:
        print(f'Ocurrio un error: {e}')

    finally:
        conexion.close()

if tipo == 'Insertar uno':
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s, %s, %s)'
                valores = ('Carlos', 'Ramirez', 'cramirez@mail.com')

                cursor.execute(sentencia, valores)
                registros_insertados = cursor.rowcount
                print(f'Registros insertados: {registros_insertados}')

    except Exception as e:
        print(f'Ocurrio un error: {e}')

    finally:
        conexion.close()

if tipo == 'Actualizar uno':
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'UPDATE persona SET nombre= %s, apellido=%s, email=%s WHERE id_persona=%s'
                valores = ('Juan Carlos', 'Castro', 'jcastro@mail.com', 7)

                cursor.execute(sentencia, valores)
                registros_actualizados = cursor.rowcount
                print(f'Registros actualizados: {registros_actualizados}')

    except Exception as e:
        print(f'Ocurrio un error: {e}')

    finally:
        conexion.close()

if tipo == 'Actualizar varios':
    try:
        with conexion:
            with conexion.cursor() as cursor:
                sentencia = 'UPDATE persona SET nombre= %s, apellido=%s, email=%s WHERE id_persona=%s'
                valores = (
                    ('Juan Carlos', 'Castro', 'jcastro@mail.com', 7),
                    ('Alberto', 'Morande', 'amorande@mail.com', 2),
                    ('Veronica', 'Morales', 'vmorales@mail.com', 5),
                )

                cursor.executemany(sentencia, valores)
                registros_actualizados = cursor.rowcount
                print(f'Registros actualizados: {registros_actualizados}')

    except Exception as e:
        print(f'Ocurrio un error: {e}')

    finally:
        conexion.close()
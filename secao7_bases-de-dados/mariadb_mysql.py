# CRUD - CREATE, READ, UPDATE, DELETE

import pymysql.cursors
from contextlib import contextmanager

@contextmanager
def conecta():
    conexao = pymysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = 'anatolian25',
        db = 'clientes',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        yield conexao
    finally:
        print('Conexão fechada')
        conexao.close()
        
        
# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
#         cursor.execute(sql, ('Gabriel', 'Branco', 25, 76))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'INSERT INTO clientes (nome, sobrenome, idade, peso) VALUES (%s, %s, %s, %s)'
        
#         dados = [
#             ('Linda', 'Dotto', '24', '64'),
#             ('Érico', 'Weber', '25', '69'),
#             ('Luiza', 'Branco', '22', '66')
#         ]
        
#         cursor.executemany(sql, dados)
        
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id = %s'
#         cursor.execute(sql, (7,))
#         conexao.commit()


# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9,))
#         conexao.commit()

# with conecta() as conexao:
#     with conexao.cursor() as cursor:
#         sql = 'DELETE FROM clientes WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         conexao.commit()

with conecta() as conexao:
    with conexao.cursor() as cursor:
        sql = 'UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql, ('Pedro', 6))
        conexao.commit()
  
        
with conecta() as conexao:
    with conexao.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes ORDER BY id ASC LIMIT 100')
        resultado = cursor.fetchall()
        
        for linha in resultado:
            print(linha)
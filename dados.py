import sqlite3

def conectar_banco():
    return sqlite3.connect('banco.db')

def criar_tabela_usuarios():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            tipo TEXT NOT NULL
        )
    ''')
    conn.commit()

    cursor.execute('SELECT * FROM usuarios WHERE tipo = "admin"')
    admin = cursor.fetchone()
    if not admin:
        cursor.execute('''
            INSERT INTO usuarios (nome, cpf, senha, tipo)
            VALUES (?, ?, ?, ?)
        ''', ('Admin', 'fluir_admin', 'admin123', 'admin'))
        conn.commit()

    conn.close()


banco = conectar_banco()
banco.row_factory = sqlite3.Row
usuario = banco.execute(
    'SELECT * FROM usuarios WHERE cpf = ? AND senha = ?',
    #(cpf_digitado, senha_digitada)
).fetchone()
banco.close()


banco = conectar_banco()
try:
    banco.execute(
        'INSERT INTO usuarios (nome, cpf, senha, tipo) VALUES (?, ?, ?, ?)',
        #(nome_completo, cpf_novo, senha_nova, 'usuario')
    )
    banco.commit()
except sqlite3.IntegrityError:
    #flash('Esse CPF já está cadastrado.')
#finally:
    banco.close()

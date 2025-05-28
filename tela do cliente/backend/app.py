from flask import Flask, request, jsonify, session

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'  # Necessário para sessions
DATABASE = 'database.db'

# ... (código anterior de init_db, login, register permanecem)

# Rota para logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove a sessão
    return jsonify({"success": True, "message": "Logout bem-sucedido!"})

# Rota para verificar autenticação
@app.route('/check_auth')
def check_auth():
    user_id = session.get('user_id')
    return jsonify({"logged_in": user_id is not None})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
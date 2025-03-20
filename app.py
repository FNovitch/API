import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Bem-vindo à API de Livros! Explore e compartilhe histórias.</h1>'


def init_db():

    with sqlite3.connect("database.db") as conn:

        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  
                    titulo TEXT NOT NULL,
                    categoria TEXT NOT NULL,  
                    autor TEXT NOT NULL,  
                    image_url TEXT NOT NULL  
                )
            """
        )


init_db()

@app.route('/doar', methods=['POST'])
def doar():
    dados = request.get_json()

    titulo = dados['titulo']
    categoria = dados['categoria']
    autor = dados['autor']
    image_url = dados['image_url']

    if not titulo or not categoria or not autor or not image_url:
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400  

    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
        INSERT INTO LIVROS (titulo, categoria, autor, image_url) 
        VALUES ("{titulo}", "{categoria}", "{autor}", "{image_url}")
        """)

    conn.commit()

    
    return jsonify({"mensagem": "Livro cadastrado com sucesso!"}), 201


@app.route('/livros', methods=['GET'])
def get_livros():
    with sqlite3.connect("database.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, titulo, categoria, autor, image_url FROM LIVROS")
        livros = cursor.fetchall()

    livros_json = [
        {
            "id": livro[0],
            "titulo": livro[1],
            "categoria": livro[2],
            "autor": livro[3],
            "image_url": livro[4],
        }
        for livro in livros
    ]
    return jsonify(livros_json)



if __name__ == '__main__':
    app.run(debug=True)

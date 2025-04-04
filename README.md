# Api Livros Doados VnW

Essa é uma API simples feita com Flask e SQLite para fins de estudo na escola Vai Na Web, ela permite cadastrar e listar os livros doados.

## Como rodar o projeto?

1. Faça o clone do repositório:

```bash
git clone <LINK_DO_REPOSITÓRIO>
cd nome_do_projeto
```

2. Criar um ambiente virtual (Obrigatório):

**Windows**

```bash
python -m venv venv
source venv/Scripts/activate
```

**Linux/Mac**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Inicie o servidor:

```bash
python app.py
```

> A API estará disponível em http://127.0.0.1:5000/

## Endpoints

### POST /doar

Endpoint para cadastro das informações do livro doado.

**Envio (JSON)**

```json
{
  "titulo": "Testando a API",
  "categoria": "Drama/Tecnologia",
  "autor": "Frank Novitch",
  "image_url": "https://exemplo.com"
}
```

## Deploy
```bash
https://api-ilql.onrender.com/livros
```

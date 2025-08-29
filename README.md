🛒 E-commerce API com Django REST Framework
Este projeto é uma API para um sistema de e-commerce construída com Django e Django REST Framework. Ele possui autenticação personalizada, controle de permissões por tipo de usuário e gerenciamento de produtos, pedidos e itens de pedido.

🚀 Tecnologias utilizadas
Python 3.11+, Django 4+, Django REST Framework, SQLite (padrão, mas pode ser trocado por PostgreSQL). A autenticação é customizada com AbstractBaseUser.

🧠 Lógica de acesso por tipo de usuário
Admin tem acesso total à API e ao painel administrativo do Django. Vendedor pode criar, editar, listar e deletar produtos e pedidos. Cliente pode visualizar apenas seus próprios pedidos e não pode criar produtos.

Ao se cadastrar pela API, o usuário é automaticamente do tipo cliente. Para se tornar vendedor, é necessário alterar o campo tipo no painel admin.

👥 Usuários de teste
Você pode usar os seguintes logins para testar os diferentes níveis de acesso:

Admin: test@test.com / Senha: senha123 — acesso total e painel admin

Vendedor: test2@test.com / Senha:  senha123  — pode gerenciar produtos e pedidos

Cliente: test5@test.com / Senha:  senha123 — pode visualizar seus próprios pedidos

📦 Endpoints principais
Autenticação:

POST /api/login/ — login

POST /api/cadastro/ — cadastro (tipo padrão: cliente)
__________________________________________________________
Produtos:

GET /api/produtos/lista/ — listar produtos

POST /api/produto/ — criar produto (vendedor ou admin)

GET, PUT, DELETE /api/produtos/<id>/ — detalhar, editar ou deletar produto

_____________________________________________________
Pedidos (gerenciados via ViewSet com DefaultRouter):

GET /api/pedidos/ — listar pedidos (cliente vê apenas os seus)

POST /api/pedidos/ — criar pedido (cliente)

GET /api/pedidos/<id>/ — visualizar pedido específico

PUT /api/pedidos/<id>/ — atualizar pedido (vendedor ou admin)

DELETE /api/pedidos/<id>/ — remover pedido (vendedor ou admin)

Os pedidos são compostos por itens (PedidoItem), acessíveis via /api/pedidos-item/.

⚙️ Como rodar localmente
Clone o repositório: git clone https://github.com/Claudeir29/market_place.git

Acesse a pasta do projeto: cd seu-repo

Crie e ative o ambiente virtual: python -m venv venv source venv/bin/activate (Linux/macOS) ou venv\Scripts\activate (Windows)

Instale as dependências: pip install -r requirements.txt

Execute as migrações: python manage.py migrate

Inicie o servidor: python manage.py runserver
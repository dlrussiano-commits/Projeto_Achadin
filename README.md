# 🛍️ Achadin
 
Marketplace online desenvolvido com **Django**, onde logistas criam e personalizam suas lojas e clientes encontram produtos por categoria ou pela busca.
 
---
 
## 📌 Sobre o projeto
 
O Achadin reúne lojas de diferentes segmentos em um só lugar. Cada logista pode cadastrar sua loja e seus produtos, e os clientes navegam pelas categorias, pesquisam produtos e fazem suas compras.
 
## 🛠️ Tecnologias
 
| Tecnologia | Uso |
|---|---|
| Python 3.14 | Linguagem principal |
| Django 6.0 | Framework web |
| django-allauth | Login com conta Google |
| SQLite | Banco de dados |
| Bootstrap 5.3 | Estilização e layout responsivo |
| HTML, CSS | Templates e design |
 
## 🗂️ Estrutura dos apps
 
```
Achadin/
├── core/            # Home, categorias, busca e menu principal
├── loja/            # Criação, edição, exclusão e personalização de lojas
├── produto/         # Cadastro e compra de produtos
├── conta_cliente/   # Conta do cliente
├── conta_logista/   # Conta do logista
└── manage.py
```
 
---
 
## ✅ 1ª VA: Funcionalidades iniciais
 
### Página inicial
- Home com menu superior (home bar) e links de navegação.
- Menu de categorias com ícones: Restaurantes e Lanchonetes, Mercados, Roupas, Calçados e Acessórios, Ferramentas e Construção, Moda e Beleza, Pet-shop, Saúde e Músicas e Games.
- Banners promocionais e área de cupons em destaque.
### Categorias
- Listagem das lojas de cada categoria, com logo e nome.
### Lojas
- Criar loja (nome, logo, banner e categoria).
- Ver detalhes da loja.
- Editar loja.
- Excluir loja, com tela de confirmação.
### Produtos
- Cadastro de produtos (nome, preço, quantidade, foto, descrição e loja).
- Página de compra do produto.
- Página de acompanhamento da entrega.
### Contas e acesso
- Estrutura separada para contas de **clientes** e **logistas**.
- Login com conta **Google**.
---
 
## 🚀 2ª VA: Novas funcionalidades
 
### 🔎 Barra de pesquisa de produtos
- Campo de busca no menu superior, disponível em todas as páginas que usam o menu.
- Pesquisa por **nome** e **descrição** do produto, sem diferenciar maiúsculas de minúsculas.
- Página de resultados com cards (foto, nome, preço e loja) e contador de resultados.
- Mensagem amigável quando nenhum produto é encontrado.
- Rota própria: `/buscar/?q=termo`.
### 🧩 Menu reutilizável
- Menu superior separado em um componente único (`_navbar.html`), incluído em todas as páginas.
- Qualquer mudança no menu é feita em um só lugar e vale para o site inteiro.
### 🎨 Personalização da loja
- O logista escolhe a **cor principal** da loja (vermelho, azul, amarelo, verde, rosa, laranja ou azul escuro).
- Escolha do **estilo dos botões**: sólido, contorno ou arredondado.
- **Texto do banner** personalizado.
- A página da loja aplica a cor, o estilo e o banner automaticamente.
### 🗄️ Banco de dados
- Novos campos no modelo `Loja`: `estilo_botao` e `texto_banner`.
- Migrações aplicadas para os novos campos.
---
 
## ▶️ Como rodar o projeto
 
1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd Projeto_Achadin/Achadin
```
 
2. Instale as dependências:
```bash
pip install django django-allauth pillow
```
 
3. Aplique as migrações:
```bash
python manage.py migrate
```
 
4. Inicie o servidor:
```bash
python manage.py runserver 8080
```
 
5. Acesse em `http://127.0.0.1:8080/`.
> Se a porta 8000 estiver bloqueada no Windows, use outra porta, como a 8080 acima.
 
## 🔮 Próximos passos
 
- Preview em tempo real da personalização da loja.
- Escolha de cor de destaque livre (hexadecimal).
- Upload de banner e fundo de página personalizados.
- Carrinho de compras e histórico de pedidos.
- Links nos resultados da busca levando à página do produto.
## 👤 Autor
 
**Davi Russiano**
 
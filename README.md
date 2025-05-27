# Funcionalidade: Página de Pedidos

Esta branch implementa a **página de pedidos** do Projeto Fluir, responsável por receber as solicitações dos usuários e armazená-las no banco de dados para controle e gerenciamento.

## Descrição da Funcionalidade

- A página contém um formulário onde o usuário pode preencher os dados necessários para realizar um pedido de entrega de água.
- Os dados do formulário são enviados via **POST** para o servidor.
- O backend recebe esses dados, cria um novo pedido e salva no banco de dados.
- Cada pedido recebe um **status inicial** (exemplo: "Pendente") para controle posterior.
- Esta funcionalidade permite o registro organizado das solicitações, facilitando o acompanhamento e a gestão pela prefeitura.

## Tecnologias e Ferramentas Utilizadas

- **Frontend:** HTML, CSS (para a página e formulário)  
- **Backend:** Python, Flask (recebimento de dados via POST, criação e salvamento no banco)  
- **Banco de dados:** SQLite 



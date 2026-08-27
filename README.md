# 📚 Organizador de Estudos

Um organizador de estudos em Python, feito para rodar no terminal. Permite cadastrar disciplinas, adicionar tarefas para cada uma delas, marcar como concluídas e acompanhar o progresso — tudo salvo automaticamente em um arquivo, para não perder nada entre uma sessão e outra.

Este foi meu primeiro projeto pessoal em Python, construído do zero como parte do meu aprendizado no primeiro semestre de Ciência da Computação.

## ✨ Funcionalidades

- **Disciplinas**
  - Adicionar novas disciplinas
  - Visualizar todas as disciplinas cadastradas, com progresso de tarefas concluídas
  - Remover disciplinas (com confirmação antes de excluir)

- **Tarefas**
  - Adicionar tarefas dentro de cada disciplina
  - Marcar/desmarcar tarefas como concluídas
  - Editar o nome de uma tarefa
  - Remover tarefas (com confirmação antes de excluir)

- **Persistência de dados**
  - Todas as informações são salvas automaticamente em um arquivo `disciplinas.json`
  - Os dados são carregados automaticamente ao abrir o programa novamente

- **Interface no terminal**
  - Cores para diferenciar mensagens de sucesso (verde) e erro (vermelho)
  - Validação de entradas do usuário em todas as telas

## 🛠️ Tecnologias usadas

- **Python 3**
- Biblioteca `json` (persistência de dados)
- Biblioteca `time` (pausas visuais)
- Códigos ANSI (cores no terminal)

## 🚀 Como rodar

1. Clone este repositório ou baixe o arquivo `main.py`
2. Certifique-se de ter o Python 3 instalado ([python.org](https://www.python.org/downloads/))
3. No terminal, navegue até a pasta do projeto e rode:

```bash
python main.py
```

4. Siga as instruções que aparecem no menu para começar a organizar suas disciplinas!

## 🧠 O que aprendi construindo esse projeto

Esse foi meu primeiro contato prático com Python, e o projeto foi crescendo aos poucos, junto com meu entendimento. Alguns dos principais aprendizados:

- **Estruturas de dados**: dicionários aninhados com listas de dicionários, para representar disciplinas e suas tarefas (incluindo o status de conclusão)
- **Controle de fluxo**: loops `while` aninhados, `break` para navegação entre "telas", e a diferença entre validar antes (`.isdigit()`) e tratar erros depois (`try`/`except`)
- **Funções**: organização do código em funções reutilizáveis, entendendo parâmetros, retorno de valores (`return`) e a diferença entre escopo local e global
- **Persistência de dados**: leitura e escrita de arquivos JSON, com tratamento de exceções (`FileNotFoundError`) para lidar com a primeira execução do programa
- **Boas práticas**: identificação e eliminação de código duplicado (criando uma função de validação reutilizável), nomeação clara de variáveis, e depuração sistemática de bugs

---
Desenvolvido por Ana Leticia — meu primeiro projeto em Python! 🐍
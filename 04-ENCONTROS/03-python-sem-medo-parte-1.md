# Encontro 3 — Python sem medo, parte 1

**Duração:** 2h · **Fase do projeto:** primeiros passos no código
**Entregável:** script alterado e rodando no Colab
**Notebook:** `05-NOTEBOOKS-COLAB/01-primeiros-dados.ipynb`

---

## 1. Objetivo

Ao final, o grupo é capaz de abrir o Google Colab, rodar uma célula, alterar variáveis e listas
em um código pronto e explicar o que cada linha faz — sem decorar sintaxe.

---

## 2. Conceitos do dia

| Conceito | Definição simples |
|---|---|
| **Colab** | Ambiente que roda Python no navegador, sem instalar |
| **Célula** | Bloco de código ou texto que pode ser executado |
| **Variável** | Nome que guarda um valor |
| **Lista** | Sequência de valores |
| **Função** | Bloco de código que faz uma tarefa |
| **Erro** | Mensagem que o Python dá quando algo não faz sentido |

---

## 3. Materiais

- Conta Google (do aluno ou da escola) para acessar o Colab.
- Notebook 01 disponível em `05-NOTEBOOKS-COLAB/`.
- Projetor para demonstração.
- Cartões impressos com trechos de código (plano B offline).

---

## 4. Roteiro minuto a minuto (120 min)

### Fase 1 — Engajar (10 min)

1. Quiz de recuperação (5 perguntas) sobre o encontro 2.
2. Pergunta: "o que uma planilha faz bem? o que ela não faz bem?"
3. Objetivo do dia: "dar o primeiro passo para automatizar a análise".

### Fase 2 — Explorar (20 min)

1. Abrir o Colab e mostrar a interface: menu, célula, botão de rodar, saída.
2. Rodar a primeira célula do notebook e ler a saída em voz alta.
3. Alterar um número e rodar de novo: "o que mudou? por quê?"
4. Mostrar um erro de propósito e perguntar: "o que o computador está tentando dizer?"

### Fase 3 — Explicar (15 min)

1. Variável como "caixa com etiqueta": `temperatura = 32`.
2. Lista como "fila de valores": `chuvas = [0, 12, 5, 30]`.
3. Operações básicas: soma, média, máximo e mínimo.
4. Funções: `len()`, `sum()`, `max()`, `min()`.
5. Leitura de erro: última linha da mensagem é a dica principal.

### Fase 4 — Aplicar (60 min)

1. **Rodar o notebook inteiro** (10 min) e observar a saída.
2. **Alterar parâmetros** (20 min): trocar os valores da lista de chuvas e ver a média mudar.
3. **Criar uma variável do tema do grupo** (15 min): por exemplo, `focos_2023 = 120`.
4. **Escrever um comentário** (10 min): explicar com as próprias palavras o que a célula faz.
5. **Desafio extra** (5 min): calcular a média de uma lista com um valor a mais.

### Fase 5 — Avaliar (15 min)

1. Dois grupos mostram a tela e explicam uma linha.
2. A turma aponta um erro que apareceu e como foi resolvido.
3. Tarefa da semana: rodar o notebook em casa ou na escola e trazer uma alteração feita.

---

## 5. Uso de IA neste encontro

**Objetivo:** usar a IA como tutora de código, pedindo explicação — não a resposta pronta.

**Prompt sugerido:**

> "Estou aprendendo Python no Colab. Explique em linguagem simples o que esta linha faz:
> `media = sum(chuvas) / len(chuvas)`. Depois, me dê um exemplo diferente com dados de
> temperatura. Não me dê a resposta do meu exercício, só explique o conceito."

**Verificação obrigatória:**

- Rodar o exemplo da IA no Colab.
- Explicar a linha com as próprias palavras no comentário do notebook.
- Registrar o prompt e o que foi aprendido.

**Alerta:** a IA pode sugerir código com biblioteca que não está instalada ou com erro de
versão. O teste no Colab é obrigatório.

---

## 6. Base científica da aula

| Decisão | Evidência | Por quê |
|---|---|---|
| Alterar código pronto antes de escrever do zero | Papert (1980); Resnick (2017) | Começar do que funciona reduz a barreira |
| Erro como objeto de estudo | Freeman et al. (2014) | Prática ativa de depuração |
| Explicar com as próprias palavras | Karpicke (2012) | Recuperação e elaboração |
| Dica de 30 s, não resposta | Vygotsky (1978) | Zona de desenvolvimento proximal |

---

## 7. Avaliação do encontro

| Critério | Nível 1 | Nível 2 | Nível 3 | Nível 4 |
|---|---|---|---|---|
| Execução | Não abriu | Abriu com ajuda | Rodou sozinho | Rodou e alterou |
| Explicação | Repete | Explica com ajuda | Explica com exemplo | Ensina o colega |
| Erro | Trava | Pede ajuda | Lê a mensagem | Corrige e explica |

---

## 8. Acessibilidade e diferenciação

- Cartões impressos com o código para quem não tem acesso ao Colab.
- Dupla com papéis: quem digita e quem lê a mensagem de erro.
- Quem já programa recebe o desafio de criar uma função própria.

---

## 9. Erros comuns e como conduzir

| Erro | O que fazer |
|---|---|
| `NameError` | Mostrar que a variável não foi criada ou tem nome diferente |
| `IndentationError` | Explicar o papel da indentação |
| Colab sem internet | Usar o plano B impresso e o Python local se houver |
| Aluno apaga tudo | Ensinar a baixar/duplicar o notebook antes de editar |

---

## 10. Para o professor

- Teste o Colab com a conta da escola antes da aula.
- Deixe o notebook 01 duplicado por aluno/grupo para não sobrescrever o original.
- Não corrija o código pelo aluno: aponte a linha e faça a pergunta.

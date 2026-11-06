# Encontro 9 — IA aplicada ao meio ambiente

**Duração:** 2h · **Fase do projeto:** modelo, avaliação e ética
**Entregável:** modelo simples treinado + ficha de modelo + registro de uso de IA
**Notebooks:** `03-ia-classificacao-ambiental.ipynb` e `04-visao-computacional-satelite.ipynb`

---

## 1. Objetivo

Ao final, o grupo é capaz de explicar a diferença entre **IA generativa** e **machine learning**,
treinar um modelo simples de classificação, ler sua matriz de confusão e preencher uma ficha de
modelo com finalidade, dados, erro e limitação.

---

## 2. Conceitos do dia

| Conceito | Definição simples |
|---|---|
| **IA generativa** | Modelo que produz texto, imagem ou código a partir de um pedido |
| **Machine learning** | Modelo que aprende padrões a partir de exemplos |
| **Aprendizado supervisionado** | Aprende com exemplos que já têm a resposta |
| **Variável de entrada** | Informação usada para prever (feature) |
| **Rótulo** | Resposta que o modelo tenta prever |
| **Treino e teste** | Parte dos dados para aprender; parte para avaliar |
| **Acurácia** | Proporção de acertos |
| **Matriz de confusão** | Tabela que mostra acertos e erros por classe |
| **Viés** | Erro sistemático que prejudica um grupo ou contexto |
| **Ficha de modelo** | Documento que explica o que o modelo faz e onde falha |

---

## 3. Materiais

- Notebooks 03 e 04 no Colab.
- Projetor.
- Ficha de modelo impressa.
- Cartões com exemplos de classificações (fogo/não fogo, água boa/ruim).
- Teachable Machine aberto no navegador (opcional).

---

## 4. Roteiro minuto a minuto (120 min)

### Fase 1 — Engajar (10 min)

1. Quiz de recuperação (5 perguntas) sobre análise, viés e limitação.
2. Mostrar duas situações: um chatbot que escreve um relatório e um modelo que prevê risco de
   fogo. Perguntar: "os dois são IA? qual a diferença?"
3. Objetivo: "entender como a IA aprende, como ela erra e como documentar isso".

### Fase 2 — Explorar (20 min)

1. Demonstração curta do Teachable Machine: treinar um classificador com 2 classes de imagens
   (ex.: "com árvore" e "sem árvore") em 5 minutos.
2. Testar com uma imagem nova e mostrar os erros.
3. Perguntar: "por que ele errou? o que faltou nos exemplos?"
4. Conectar com os dados do curso: "se eu der poucos exemplos de queimada, o modelo aprende
   errado".

### Fase 3 — Explicar (20 min)

1. IA generativa vs. ML: uma produz conteúdo; a outra faz previsão/classificação.
2. Fluxo do ML: dados → treino → teste → métrica → decisão.
3. Acurácia sozinha engana: um modelo que diz "não fogo" sempre pode acertar 95% se 95% dos
   casos forem "não fogo".
4. Matriz de confusão: falso positivo e falso negativo têm custos diferentes na gestão
   ambiental.
5. Ética: quem é afetado pelo erro? o modelo exclui alguma área ou grupo?
6. Ficha de modelo: finalidade, dados, métrica, erro, limitação, uso recomendado.

### Fase 4 — Aplicar (55 min)

1. **Abrir o notebook 03** (10 min) e rodar o exemplo de classificação.
2. **Treinar e testar** (15 min): separar treino e teste, treinar a árvore de decisão, ver a
   acurácia.
3. **Ler a matriz de confusão** (10 min): quantos falsos positivos e falsos negativos?
4. **Testar uma variação** (10 min): mudar uma variável ou o tamanho do teste e comparar.
5. **Preencher a ficha de modelo** (10 min) com o que o grupo observou.

### Fase 5 — Avaliar (15 min)

1. Dois grupos apresentam o modelo e a ficha em 2 minutos.
2. A turma pergunta: "onde esse modelo erraria na prática? quem seria prejudicado?"
3. Tarefa da semana: revisar a ficha e preparar 3 slides para a mostra.

---

## 5. Uso de IA neste encontro

Este é o encontro em que a IA é **objeto de estudo**, não só ferramenta.

### 5.1 IA generativa como assistente (com verificação)

**Prompt sugerido:**

> "Explique a diferença entre IA generativa e machine learning para um estudante do ensino médio,
> usando um exemplo de meio ambiente. Depois, liste 3 perguntas que eu deveria fazer para
> avaliar se um modelo de previsão de queimadas é confiável. Não invente números."

**Verificação:**

- Comparar a explicação com o notebook e com o professor.
- Responder às 3 perguntas com os dados do grupo.
- Registrar o prompt e a conferência.

### 5.2 Machine learning supervisionado

O notebook 03 usa um conjunto de dados didático com variáveis como temperatura, umidade, vento
e histórico de chuva para prever **risco de foco de calor**. O aluno:

1. separa treino e teste;
2. treina uma árvore de decisão (`DecisionTreeClassifier`);
3. calcula acurácia;
4. vê a matriz de confusão;
5. interpreta o que o modelo aprendeu.

### 5.3 Visão computacional

O notebook 04 mostra como usar um modelo pré-treinado (MobileNetV2) para classificar imagens
ambientais, ou como treinar um classificador no Teachable Machine. O foco não é a arquitetura,
mas:

- o que o modelo vê;
- por que ele confunde classes parecidas;
- o que acontece quando a imagem é de outra região ou estação;
- como documentar o erro.

### 5.4 Regras de uso

- Nenhum dado pessoal em prompt ou imagem.
- Toda resposta de IA é conferida com fonte ou com o notebook.
- O grupo responde pelo que entrega; a IA não é autora.
- A ficha de modelo é obrigatória.

---

## 6. Base científica da aula

| Decisão | Evidência | Por quê |
|---|---|---|
| Começar pelo erro do modelo | O'Neil (2016) | Entender limite antes de confiar |
| Acurácia + matriz de confusão | Mitchell et al. (2019) | Métrica única esconde viés |
| Ficha de modelo | Mitchell et al. (2019) | Documentação e transparência |
| Datasheet e fonte dos dados | Gebru et al. (2021) | Rastreabilidade e responsabilidade |
| ML em sensoriamento remoto | Zhu et al. (2017); Reichstein et al. (2019) | Aplicação real e limites |
| Supervisão humana | UNESCO (2021) | Ética e governança |

---

## 7. Avaliação do encontro

| Critério | Nível 1 | Nível 2 | Nível 3 | Nível 4 |
|---|---|---|---|---|
| Modelo | Não rodou | Rodou com ajuda | Rodou e avaliou | Rodou, variou e comparou |
| Métrica | Não lê | Lê acurácia | Lê acurácia e matriz | Explica falso positivo e negativo |
| Ficha | Ausente | Parcial | Completa | Completa e crítica |
| Ética | Ignora | Cita | Discute viés | Relaciona com grupo afetado |
| Uso de IA | Sem registro | Registro parcial | Registro completo | Registro e reflexão |

---

## 8. Acessibilidade e diferenciação

- Quem não tem computador usa o Teachable Machine no celular ou a versão impressa da matriz de
  confusão.
- Grupo avançado testa outra métrica (precisão, recall) e explica a diferença.
- Grupo com dificuldade usa o modelo pronto e foca na interpretação.

---

## 9. Erros comuns e como conduzir

| Erro | O que fazer |
|---|---|
| Achar que acurácia alta = modelo bom | Mostrar o caso do "não fogo" sempre |
| Usar treino e teste iguais | Explicar vazamento de dados |
| Achar que a IA "vê" como humano | Mostrar exemplos de erro |
| Não documentar o prompt | Exigir o registro antes de entregar |
| Concluir causa | Retomar a diferença correlação/causalidade |

---

## 10. Anexos

### Anexo A — Ficha de modelo (simplificada)

```
Nome do modelo: ______________________________________
O que ele faz (1 frase): _____________________________
Quem usa e para quê: _________________________________
Dados de treino (fonte, período, tamanho): ____________
Variáveis de entrada: ________________________________
Rótulo previsto: _____________________________________
Métrica usada: ______________  Resultado: _____________
Falsos positivos: ______  Falsos negativos: ___________
Onde ele erra mais: __________________________________
Quem é afetado pelo erro: ____________________________
Limitação principal: _________________________________
Uso recomendado: _____________________________________
Uso NÃO recomendado: _________________________________
```

### Anexo B — Registro de uso de IA

```
Data: ________  Ferramenta: __________________________
Prompt usado: ________________________________________
Para que usei: _______________________________________
O que a IA respondeu (resumo): ________________________
O que eu verifiquei: _________________________________
O que eu corrigi: ____________________________________
O que eu descartei e por quê: ________________________
```

---

## 11. Para o professor

- Teste os notebooks antes: o modelo precisa rodar em menos de 1 minuto.
- Se a internet cair, use o Teachable Machine offline? Não funciona; use a atividade impressa de
  matriz de confusão e o debate ético.
- Reserve 15 min finais para a discussão ética: é o coração do encontro.

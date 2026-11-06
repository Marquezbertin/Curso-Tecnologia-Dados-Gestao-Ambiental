# Plano de Ensino — 10 encontros de 2h (20h)

**Público:** ensino médio (14–18 anos) · **Turma:** até 30 alunos, em duplas ou trios
**Formato:** 2h por encontro, 1 encontro por semana · **Projeto:** um por grupo, desde o encontro 1

---

## 1. Grade completa

| # | Encontro | Foco | Entregável | Notebook | IA |
|---|---|---|---|---|---|
| 1 | Por que dados e meio ambiente? | Problema, pergunta e fonte | Tema + pergunta de investigação | — | Assistente organiza mapa mental |
| 2 | Primeiros dados na planilha | Dado, variável, série temporal | Gráfico comentado | `01-primeiros-dados` | IA explica o gráfico; aluno confere |
| 3 | Python sem medo — 1 | Colab, variável, lista, lógica | Script alterado e rodando | `01-primeiros-dados` | IA como tutora de código |
| 4 | Python sem medo — 2 | CSV, pandas, filtro, média, gráfico | Notebook com análise do tema | `01-primeiros-dados` | IA revisa o código |
| 5 | Mapas e território | Coordenada, ponto, área, camada | Mapa do município com camada | `02-mapas-e-territorio` | IA interpreta o mapa |
| 6 | Queimadas e desmatamento | Série, comparação, fonte | Comparação entre anos/regiões | `03-ia-classificacao-ambiental` | IA classifica focos de calor |
| 7 | Coleta de dados na escola | Amostragem, instrumento, ética | Plano de coleta + registros | — | IA revisa o desenho amostral |
| 8 | Analisando os dados coletados | Limpeza, estatística, viés | Análise com limitações | `01-primeiros-dados` | IA audita vieses |
| 9 | IA aplicada ao meio ambiente | ML, visão computacional, ética | Modelo + ficha de modelo | `03` e `04` | Núcleo do curso |
| 10 | Do dado à solução e mostra | Storytelling e proposta | Pôster + apresentação | — | IA ensaia a comunicação |

---

## 2. Estrutura de cada encontro (120 min)

| Fase | Tempo | O que acontece |
|---|---|---|
| **1. Engajar** | 10 min | Quiz de recuperação (5 perguntas) + problema do dia |
| **2. Explorar** | 20 min | Dados reais, pergunta e hipótese em grupo |
| **3. Explicar** | 15 min | Conceito necessário, com exemplo do território |
| **4. Aplicar** | 60 min | Notebook + projeto do grupo (pausa de 5 min no meio) |
| **5. Avaliar** | 15 min | Mostra rápida, feedback e tarefa da semana |

---

## 3. Materiais por encontro

| # | Materiais | Preparação do professor |
|---|---|---|
| 1 | Papel, canetas, projetor, formulário de tema | Imprimir fichas de problema e fonte |
| 2 | Planilha modelo, notebook 01, dados de exemplo | Testar o Colab e baixar o CSV do INMET |
| 3 | Notebook 01 (parte A), conta Google | Testar login dos alunos com antecedência |
| 4 | Notebook 01 (parte B), CSV do grupo | Escolher um CSV de exemplo do tema |
| 5 | Notebook 02, MapBiomas, Google Earth | Testar o Folium e o acesso ao MapBiomas |
| 6 | Notebook 03, dados do INPE | Baixar focos de calor do município/estado |
| 7 | Fichas de coleta, trena, termômetro, planilha | Definir pontos de coleta na escola |
| 8 | Planilha da escola, notebook 01 | Conferir os dados coletados na semana |
| 9 | Notebooks 03 e 04, Teachable Machine | Testar o modelo pré-treinado e a internet |
| 10 | Cartolina, impressão do pôster, projetor | Montar cronograma da mostra |

---

## 4. Progressão e dependências

```
1. Pergunta
   └─ 2. Planilha
        └─ 3. Python básico
             └─ 4. pandas e gráficos
                  ├─ 5. Mapas
                  ├─ 6. Queimadas e desmatamento
                  └─ 7. Coleta na escola
                       └─ 8. Análise
                            └─ 9. IA
                                 └─ 10. Mostra
```

Cada encontro retoma o anterior. Se um grupo faltar, a tarefa de retomada está no plano do
encontro seguinte e no [`08-GUIA-DO-PROFESSOR/02-plano-b-offline.md`](08-GUIA-DO-PROFESSOR/02-plano-b-offline.md).

---

## 5. Entregáveis e pesos

| Entregável | Encontro | Peso no processo |
|---|---|---|
| Tema + pergunta de investigação | 1 | 10% |
| Gráfico comentado | 2 | 10% |
| Script alterado e rodando | 3 | 10% |
| Notebook com análise | 4 | 15% |
| Mapa com camada | 5 | 10% |
| Comparação de queimadas/desmatamento | 6 | 10% |
| Plano de coleta + registros | 7 | 10% |
| Análise com limitações | 8 | 10% |
| Modelo + ficha de modelo | 9 | 15% |
| Pôster + apresentação | 10 | — (projeto final) |

O projeto final vale 40% e a apresentação 20%, conforme o
[`01-PROJETO-PEDAGOGICO.md`](01-PROJETO-PEDAGOGICO.md).

---

## 6. Regras de uso de IA na turma

1. A IA é **assistente**, não autora. O aluno responde pelo que entrega.
2. Todo uso de IA é registrado: prompt, finalidade e o que foi verificado.
3. Nenhum número vai para o pôster sem conferência na planilha ou no notebook.
4. A IA não substitui a leitura da fonte original.
5. Dados pessoais nunca entram em prompt.
6. O professor revisa a ficha de uso antes da mostra.

Detalhes em [`08-GUIA-DO-PROFESSOR/03-etica-e-seguranca-ia.md`](08-GUIA-DO-PROFESSOR/03-etica-e-seguranca-ia.md).

---

## 7. Critérios de aprovação

| Critério | Regra |
|---|---|
| Presença | ≥ 8 de 10 encontros |
| Entregáveis | ≥ 7 de 9 entregas parciais |
| Projeto | Apresentado na mostra com pôster e análise |
| Ficha de IA | Entregue e revisada |
| Reposição | Tarefa equivalente em até 15 dias |

Quem não atinge o critério **não é reprovado**: recebe plano de recuperação de 2 semanas e conclui
no ciclo seguinte, sem custo.

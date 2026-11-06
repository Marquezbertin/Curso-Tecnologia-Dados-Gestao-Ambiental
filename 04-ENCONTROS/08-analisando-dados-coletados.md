# Encontro 8 — Analisando os dados coletados

**Duração:** 2h · **Fase do projeto:** análise e limitações
**Entregável:** análise dos dados da escola com seção de limitações
**Notebook:** `05-NOTEBOOKS-COLAB/01-primeiros-dados.ipynb` (adaptado à planilha do grupo)
**Dados de exemplo:** `06-DADOS/exemplos/exemplo-escola-sintetico.csv`

---

## 1. Objetivo

Ao final, o grupo é capaz de limpar e organizar os dados que coletou, calcular medidas simples,
comparar com dados abertos e escrever uma conclusão **com suas limitações explícitas**.

---

## 2. Conceitos do dia

| Conceito | Definição simples |
|---|---|
| **Limpeza** | Corrigir erros, vazios e formatos |
| **Média e mediana** | Medidas de tendência central |
| **Dispersão** | O quanto os valores variam |
| **Comparação** | Contraste entre períodos, pontos ou fontes |
| **Viés** | Erro sistemático que empurra o resultado para um lado |
| **Limitação** | O que o dado não permite concluir |

---

## 3. Materiais

- Planilha da coleta preenchida.
- Notebook 01 adaptado ou planilha com gráficos.
- Dados abertos do encontro 2 para comparação.
- Projetor.
- Ficha de análise e limitações.

---

## 4. Roteiro minuto a minuto (120 min)

### Fase 1 — Engajar (10 min)

1. Quiz de recuperação (5 perguntas) sobre amostragem, protocolo e ética.
2. Mostrar duas planilhas: uma bagunçada e uma limpa. Perguntar: "qual permite concluir algo?"
3. Objetivo: "transformar registro em análise".

### Fase 2 — Explorar (20 min)

1. Cada grupo abre sua planilha e conta quantas linhas tem.
2. Levantar problemas: valores vazios, vírgula no lugar de ponto, unidade trocada, data errada.
3. Comparar com o CSV de exemplo da escola (dados sintéticos) para ver o formato esperado.
4. Perguntar: "o que esses dados podem responder? o que não podem?"

### Fase 3 — Explicar (15 min)

1. Limpeza: remover vazio, corrigir tipo, padronizar unidade.
2. Média vs. mediana: quando um valor extremo distorce a média.
3. Gráfico adequado: linha para tempo, barras para comparação, dispersão para relação.
4. Viés de amostragem: medir só o pátio da manhã não representa a escola inteira.
5. Estrutura da conclusão: resultado + evidência + limite + próximo passo.

### Fase 4 — Aplicar (60 min)

1. **Limpar a planilha** (15 min) e registrar o que foi corrigido.
2. **Calcular** (15 min): média, mediana, máximo, mínimo por ponto.
3. **Construir dois gráficos** (15 min): um da escola e um de comparação com dado aberto.
4. **Escrever a análise** (15 min): 1 parágrafo com resultado, 1 com limitação e 1 com proposta
   de próximo passo.

### Fase 5 — Avaliar (15 min)

1. Dois grupos apresentam a análise em 2 minutos.
2. A turma aponta: o gráfico é adequado? a conclusão excede o dado? a limitação está clara?
3. Tarefa da semana: revisar a análise com base no feedback e trazer a versão final.

---

## 5. Uso de IA neste encontro

**Objetivo:** usar a IA como auditora de viés e de exagero na conclusão.

**Prompt sugerido:**

> "Escrevi esta conclusão a partir dos meus dados: '[cole a conclusão]'. Meus dados foram
> coletados em [pontos], durante [período], com [instrumento]. Liste 3 formas de eu estar
> exagerando ou generalizando e 3 limitações que eu deveria declarar. Não reescreva por mim."

**Verificação obrigatória:**

- Comparar cada crítica com a planilha.
- Ajustar a conclusão para o que o dado permite.
- Registrar o que mudou depois da auditoria.

**Alerta:** a IA não conhece a escola; ela só pode apontar riscos lógicos. A decisão é do grupo.

---

## 6. Base científica da aula

| Decisão | Evidência | Por quê |
|---|---|---|
| Limpar antes de analisar | Wickham & Grolemund (2017) | Dado organizado é pré-requisito de análise |
| Média e mediana juntas | Freeman et al. (2014) | Evitar conclusão distorcida por outlier |
| Seção de limitações | D'Ignazio & Klein (2020); O'Neil (2016) | Letramento crítico de dados |
| IA como auditora | UNESCO (2021) | Supervisão humana |

---

## 7. Avaliação do encontro

| Critério | Nível 1 | Nível 2 | Nível 3 | Nível 4 |
|---|---|---|---|---|
| Limpeza | Não fez | Fez parcial | Fez e registrou | Fez, registrou e justificou |
| Cálculo | Errado | Correto em parte | Correto | Correto e comparado |
| Gráfico | Inadequado | Adequado | Adequado com fonte | Destaca padrão e limite |
| Conclusão | Exagera | Descreve | Interpreta com limite | Interpreta, limita e propõe próximo passo |

---

## 8. Acessibilidade e diferenciação

- Planilha com fórmulas prontas para quem tem dificuldade com código.
- Versão impressa com os dados e espaço para desenhar o gráfico.
- Grupo avançado calcula dispersão (desvio padrão) e explica em linguagem simples.

---

## 9. Erros comuns e como conduzir

| Erro | O que fazer |
|---|---|
| Concluir causa a partir de correlação | Pedir hipótese alternativa |
| Ignorar valores vazios | Mostrar o efeito na média |
| Gráfico de pizza com muitos pontos | Trocar por barras |
| Generalizar para a cidade | Lembrar o recorte da amostra |
| IA reescreve tudo | Proibir cópia; exigir autoria do grupo |

---

## 10. Anexo — Ficha de análise e limitações

```
Grupo: ______________________  Encontro: 8
Dados coletados em: ______________  Período: __________
Linhas: ______  Valores vazios: ______  Corrigidos: ____
Resultado principal (1 frase): ________________________
Evidência (gráfico/número): ___________________________
Limitação 1: _________________________________________
Limitação 2: _________________________________________
Viés possível: _______________________________________
Próximo passo: _______________________________________
O que a IA apontou e eu aceitei: ______________________
O que a IA apontou e eu recusei (e por quê): __________
```

---

## 11. Para o professor

- Se a coleta não foi feita, use o CSV sintético e deixe claro que é didático.
- Reserve tempo para a escrita: é a parte mais difícil e a mais importante.
- Guarde as análises: elas alimentam o pôster do encontro 10.

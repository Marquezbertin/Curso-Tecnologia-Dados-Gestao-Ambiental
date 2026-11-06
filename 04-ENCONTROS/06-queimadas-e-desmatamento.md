# Encontro 6 — Queimadas e desmatamento

**Duração:** 2h · **Fase do projeto:** série histórica e comparação
**Entregável:** comparação entre anos ou regiões + ficha de fonte
**Notebook:** `05-NOTEBOOKS-COLAB/03-ia-classificacao-ambiental.ipynb` (introdução)
**Dados de exemplo:** `06-DADOS/exemplos/exemplo-focos-calor-sintetico.csv`

---

## 1. Objetivo

Ao final, o grupo é capaz de baixar ou abrir dados de focos de calor e desmatamento, comparar
anos e regiões, e explicar **o que os dados mostram e o que não mostram**.

---

## 2. Conceitos do dia

| Conceito | Definição simples |
|---|---|
| **Foco de calor** | Ponto detectado por satélite como possível queimada |
| **PRODES** | Monitoramento do desmatamento por corte raso na Amazônia |
| **DETER** | Alertas de desmatamento e degradação |
| **Série histórica** | Dados comparáveis ao longo de vários anos |
| **Comparação** | Contraste entre períodos, regiões ou categorias |
| **Viés de detecção** | O satélite vê melhor algumas áreas que outras |

---

## 3. Materiais

- Notebook 03 (parte 1) no Colab.
- Acesso ao TerraBrasilis (INPE).
- CSV de exemplo de focos de calor.
- Projetor.
- Ficha de fonte impressa.

---

## 4. Roteiro minuto a minuto (120 min)

### Fase 1 — Engajar (10 min)

1. Quiz de recuperação (5 perguntas) sobre mapas, coordenadas e legenda.
2. Mostrar uma notícia com número de focos de calor e perguntar: "de onde veio esse número? ele
   compara o quê com o quê?"
3. Objetivo: "aprender a comparar séries sem enganar nem se enganar".

### Fase 2 — Explorar (20 min)

1. Abrir o TerraBrasilis e localizar a série de focos de calor do estado/município.
2. Mostrar a diferença entre dado bruto, dado filtrado e dado agregado.
3. Comparar dois anos e perguntar: "a diferença é grande? pode ser variação natural?"
4. Mostrar que o satélite tem horário de passagem e resolução — isso afeta o que é detectado.

### Fase 3 — Explicar (15 min)

1. Foco de calor não é sinônimo de desmatamento.
2. Desmatamento pode ocorrer sem fogo e fogo pode ocorrer sem desmatamento.
3. Comparação justa: mesmo período, mesma região, mesma fonte, mesma metodologia.
4. Como ler a ficha de fonte e a seção de limitações.
5. Introdução à ideia de classificação: "como um algoritmo decide se um ponto é fogo?"

### Fase 4 — Aplicar (60 min)

1. **Carregar os dados** (10 min) e conferir as colunas.
2. **Agrupar por ano e mês** (15 min) e calcular totais.
3. **Comparar dois períodos** (15 min) com gráfico de barras ou linha.
4. **Preencher a ficha de fonte** (10 min) com link, ano, metodologia e limitação.
5. **Escrever a conclusão** (10 min): "o que mudou, em que período e com que limite".

### Fase 5 — Avaliar (15 min)

1. Dois grupos mostram a comparação.
2. A turma aponta: a comparação é justa? a fonte está citada? a limitação está clara?
3. Tarefa da semana: comparar o município com o estado ou com um município vizinho.

---

## 5. Uso de IA neste encontro

**Objetivo:** usar a IA para ajudar a classificar e comparar, mas com validação nos dados.

**Prompt sugerido:**

> "Tenho uma tabela de focos de calor com as colunas [liste]. Quero comparar [ano A] com [ano B]
> no município de [nome]. Sugira um gráfico adequado, 3 cuidados de comparação e 2 limitações.
> Não invente os números; eu vou calcular."

**Verificação obrigatória:**

- Conferir os totais com o código do notebook.
- Confirmar a fonte e a metodologia no site do INPE.
- Registrar a diferença entre "foco de calor" e "desmatamento".

**Alerta:** a IA pode misturar PRODES com DETER e com focos de calor. São coisas diferentes.

---

## 6. Base científica da aula

| Decisão | Evidência | Por quê |
|---|---|---|
| Comparar mesmo período e fonte | Wiggins & McTighe (2005) | Critério explícito evita comparação injusta |
| Distinguir foco de desmatamento | INPE | Rigor conceitual |
| Ficha de fonte | Wineburg & McGrew (2019) | Leitura lateral e checagem |
| Introdução à classificação | Zhu et al. (2017) | Prepara o encontro 9 |

---

## 7. Avaliação do encontro

| Critério | Nível 1 | Nível 2 | Nível 3 | Nível 4 |
|---|---|---|---|---|
| Dados | Não carregou | Carregou | Carregou e limpou | Carregou, limpou e documentou |
| Comparação | Sem critério | Compara | Compara com critério | Compara e aponta viés |
| Fonte | Ausente | Nome | Nome e link | Nome, link, ano e metodologia |
| Conclusão | Opinião | Descreve | Interpreta | Interpreta com limite |

---

## 8. Acessibilidade e diferenciação

- Tabela impressa com os totais para quem não tem computador.
- Quem termina antes compara um terceiro ano ou outra região.
- Texto de apoio com glossário de PRODES, DETER e foco de calor.

---

## 9. Erros comuns e como conduzir

| Erro | O que fazer |
|---|---|
| Somar focos de anos diferentes | Explicar que cada ano é uma série |
| Dizer que foco = desmatamento | Retomar a diferença conceitual |
| Ignorar mudança de metodologia | Ler a nota técnica da fonte |
| IA mistura datasets | Pedir que o aluno abra a fonte e confira |

---

## 10. Anexo — Ficha de fonte

```
Fonte: ____________________  Link: __________________
Variável: _________________  Unidade: _______________
Período: __________________  Abrangência: ___________
Metodologia (resumo): ________________________________
Limitação declarada: _________________________________
Limitação que eu percebi: ____________________________
O que os dados NÃO mostram: ___________________________
```

---

## 11. Para o professor

- Baixe os dados com antecedência e guarde uma cópia local.
- Explique que "foco de calor" é uma detecção, não uma certidão de queimada.
- Use a comparação para introduzir a ideia de modelo e erro, que será aprofundada no encontro 9.

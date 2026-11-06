# Encontro 2 — Primeiros dados na planilha

**Duração:** 2h · **Fase do projeto:** primeira análise
**Entregável:** gráfico comentado (planilha) + ficha de leitura do gráfico
**Notebook:** `05-NOTEBOOKS-COLAB/01-primeiros-dados.ipynb` (opcional neste encontro)
**Dados de exemplo:** `06-DADOS/exemplos/exemplo-inmet-sintetico.csv`

---

## 1. Objetivo

Ao final, o grupo é capaz de baixar ou abrir uma série de dados meteorológicos, organizar em
planilha, construir um gráfico e **explicar por escrito** o que o gráfico mostra — e o que não
mostra.

---

## 2. Conceitos do dia

| Conceito | Definição simples |
|---|---|
| **Planilha** | Tabela organizada em linhas e colunas |
| **Variável** | Coluna que representa uma medida (temperatura, chuva) |
| **Série temporal** | Sequência de valores ao longo do tempo |
| **Média** | Soma dividida pela quantidade |
| **Valor atípico (outlier)** | Valor muito distante do padrão |
| **Tendência** | Direção geral da série (subir, descer, ficar estável) |
| **Sazonalidade** | Padrão que se repete em certos períodos do ano |

---

## 3. Materiais

- Computador ou celular com Google Sheets/Excel.
- Notebook 01 aberto no Colab (opcional).
- CSV de exemplo (`exemplo-inmet-sintetico.csv`) para quem não conseguir baixar o dado real.
- Projetor para demonstrar o download no INMET.
- Ficha de leitura do gráfico impressa.

---

## 4. Roteiro minuto a minuto (120 min)

### Fase 1 — Engajar (10 min)

1. Quiz de recuperação (5 perguntas):
   - O que é um dado?
   - Qual a diferença entre dado e evidência?
   - O que é uma variável?
   - O que é uma fonte?
   - Por que o recorte de tempo importa?
2. Retomar as perguntas dos grupos e apresentar o objetivo do dia: "transformar a pergunta em
   uma primeira tabela e um primeiro gráfico".

### Fase 2 — Explorar (20 min)

1. Abrir o portal do INMET e localizar a estação automática mais próxima do município.
2. Mostrar o arquivo baixado: colunas, data, hora, temperatura, chuva.
3. Perguntar: "quantas linhas tem? o que cada coluna representa? o que está faltando?"
4. Comparar com o CSV de exemplo sintético: **"este arquivo é didático, não é medição real"**.

### Fase 3 — Explicar (15 min)

1. Estrutura de uma planilha: cabeçalho, linhas, colunas, tipos de dado.
2. Data no formato ISO (`AAAA-MM-DD`) para ordenar corretamente.
3. Gráfico de linha para série temporal; gráfico de barras para comparação entre categorias.
4. Como ler um gráfico: título, eixos, unidade, período, fonte.
5. O que um gráfico **não** mostra: causa, ausência de dado, mudança de metodologia.

### Fase 4 — Aplicar (60 min)

1. **Organizar a planilha** (15 min):
   - Criar colunas: data, temperatura máxima, temperatura mínima, chuva.
   - Ordenar por data.
   - Remover linhas vazias ou com erro (`-9999` ou vazio).
2. **Calcular** (10 min): média, máximo, mínimo e soma da chuva no período.
3. **Construir o gráfico** (15 min): linha da temperatura máxima ao longo dos meses.
4. **Escrever a leitura** (15 min): 5 linhas com (a) o que o gráfico mostra, (b) um valor
   atípico, (c) uma limitação, (d) uma pergunta nova.
5. **Circular e ajustar** (5 min): o professor confere se o gráfico tem título, eixos e fonte.

### Fase 5 — Avaliar (15 min)

1. Dois ou três grupos mostram o gráfico em 1 minuto.
2. A turma identifica: tem título? tem unidade? tem fonte? tem limitação?
3. Tarefa da semana: repetir o gráfico com outra variável (chuva ou temperatura mínima) e trazer
   a leitura.

---

## 5. Uso de IA neste encontro

**Objetivo:** usar a IA para explicar o gráfico, mas o aluno precisa conferir cada afirmação.

**Prompt sugerido:**

> "Este é um gráfico de [variável] entre [mês/ano] e [mês/ano] da estação [nome]. A série mostra
> [descreva em uma frase]. Me ajude a listar 3 hipóteses para o padrão observado e 2 limitações
> dos dados. Não invente números."

**Verificação obrigatória:**

- Cada hipótese precisa ser confrontada com o gráfico e com o conhecimento local.
- Nenhum número citado pela IA entra no texto sem conferência na planilha.
- Registrar: "o que a IA sugeriu / o que eu confirmei / o que eu descartei".

**Alerta:** a IA não vê o gráfico se você não enviar os dados. Se enviar, não inclua nome de
aluno ou dado pessoal.

---

## 6. Base científica da aula

| Decisão | Evidência | Por quê |
|---|---|---|
| Quiz de recuperação | Karpicke & Roediger (2008) | Recuperar fixa mais que reler |
| Planilha antes de Python | Kolb (1984) | Do concreto ao abstrato; reduz carga cognitiva |
| Escrever a leitura do gráfico | Freeman et al. (2014) | Prática ativa de interpretação |
| Seção "o que não mostra" | D'Ignazio & Klein (2020) | Letramento crítico de dados |

---

## 7. Avaliação do encontro

| Critério | Nível 1 | Nível 2 | Nível 3 | Nível 4 |
|---|---|---|---|---|
| Planilha | Desorganizada | Organizada | Organizada e limpa | Organizada, limpa e documentada |
| Gráfico | Sem título/eixos | Com título | Com título, eixos e unidade | Com fonte e destaque |
| Leitura | Descreve | Descreve e interpreta | Interpreta e aponta limite | Relaciona com hipótese local |

---

## 8. Acessibilidade e diferenciação

- Quem não tem computador usa a versão impressa da tabela e desenha o gráfico no papel.
- Quem termina antes ajuda o colega (nível 4 da rubrica exige "ajudou um colega").
- Arquivo de exemplo disponível em CSV e em imagem para leitura.

---

## 9. Erros comuns e como conduzir

| Erro | O que fazer |
|---|---|
| Data como texto | Ensinar o formato ISO e reordenar |
| `-9999` tratado como temperatura | Explicar código de erro e remover |
| Gráfico sem unidade | Pedir que o aluno escreva a unidade no eixo |
| Concluir causalidade | Perguntar "que outra explicação existe?" |
| IA inventa número | Pedir conferência na planilha e registro |

---

## 10. Anexo — Ficha de leitura do gráfico

```
Grupo: ______________________  Encontro: 2
Variável: ____________________  Período: ______________
Fonte: _______________________________________________
1. O que o gráfico mostra (2 linhas): _________________
2. Um valor atípico e o que pode explicá-lo: __________
3. O que o gráfico NÃO mostra: _______________________
4. Uma pergunta nova: ________________________________
5. O que a IA sugeriu e eu confirmei: _________________
6. O que a IA sugeriu e eu descartei: _________________
```

---

## 11. Para o professor

- Tenha o CSV de exemplo em mãos: internet instável não pode travar a aula.
- Se o INMET estiver fora do ar, use o arquivo local e explique a diferença entre dado real e
  dado didático.
- Guarde os gráficos: eles serão comparados no encontro 8.

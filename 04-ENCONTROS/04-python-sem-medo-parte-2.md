# Encontro 4 — Python sem medo, parte 2

**Duração:** 2h · **Fase do projeto:** análise do tema do grupo
**Entregável:** notebook com leitura de um CSV, filtro, média e gráfico
**Notebook:** `05-NOTEBOOKS-COLAB/01-primeiros-dados.ipynb`

---

## 1. Objetivo

Ao final, o grupo é capaz de ler um arquivo CSV com pandas, filtrar linhas, calcular média e
máximo, gerar um gráfico com Matplotlib e **comentar** o resultado.

---

## 2. Conceitos do dia

| Conceito | Definição simples |
|---|---|
| **CSV** | Arquivo de texto com valores separados por vírgula |
| **DataFrame** | Tabela do pandas, com linhas e colunas |
| **Filtro** | Seleção de parte dos dados por uma condição |
| **Agrupamento** | Juntar linhas por uma categoria (mês, ano, bairro) |
| **Matplotlib** | Biblioteca que gera gráficos |
| **Limpeza** | Corrigir tipos, remover vazios e tratar erros |

---

## 3. Materiais

- Notebook 01 aberto no Colab.
- CSV do tema do grupo ou o arquivo de exemplo.
- Projetor.
- Ficha de análise impressa (plano B).

---

## 4. Roteiro minuto a minuto (120 min)

### Fase 1 — Engajar (10 min)

1. Quiz de recuperação (5 perguntas) sobre variável, lista e erro.
2. Retomar o gráfico do encontro 2: "como faríamos isso com 10 mil linhas?"
3. Objetivo: "automatizar a análise que fizemos na planilha".

### Fase 2 — Explorar (20 min)

1. Abrir o CSV no editor de texto e mostrar que é só texto separado por vírgula.
2. Mostrar `pd.read_csv()` e o DataFrame resultante.
3. Perguntar: "quantas linhas? quantas colunas? que tipo de dado tem em cada coluna?"
4. Mostrar o que acontece quando a data é lida como texto.

### Fase 3 — Explicar (15 min)

1. `pd.read_csv()` e `df.head()`.
2. `df['coluna']` para selecionar.
3. Filtro: `df[df['chuva'] > 0]`.
4. Média: `df['temperatura'].mean()`.
5. Gráfico: `plt.plot()` com título, rótulos e fonte.
6. Limpeza: `pd.to_datetime()`, `dropna()`, tratamento de `-9999`.

### Fase 4 — Aplicar (60 min)

1. **Ler o CSV** (10 min) e conferir a tabela.
2. **Limpar** (15 min): data, valores vazios, código de erro.
3. **Filtrar e calcular** (15 min): recorte do período e do tema do grupo.
4. **Gerar o gráfico** (10 min) com título, eixos e unidade.
5. **Escrever a leitura** (10 min): 5 linhas com resultado e limitação.

### Fase 5 — Avaliar (15 min)

1. Dois grupos mostram o notebook e o gráfico.
2. A turma confere: o código roda do início ao fim? o gráfico tem fonte? a leitura tem limite?
3. Tarefa da semana: aplicar o mesmo código a outra variável do tema.

---

## 5. Uso de IA neste encontro

**Objetivo:** usar a IA para revisar o código e apontar erros, não para escrever o notebook
inteiro.

**Prompt sugerido:**

> "Este é meu código pandas: [cole o trecho]. Ele deveria [objetivo]. Está dando este erro:
> [mensagem]. Explique a causa e me dê duas opções de correção, sem reescrever tudo. Depois,
> diga como eu testo se a correção funcionou."

**Verificação obrigatória:**

- Rodar a correção no Colab.
- Comparar o resultado com o cálculo feito à mão em uma amostra pequena.
- Registrar o prompt, o erro e a solução no notebook.

**Alerta:** não cole dados com nome de aluno. Use apenas dados ambientais.

---

## 6. Base científica da aula

| Decisão | Evidência | Por quê |
|---|---|---|
| Do concreto (planilha) ao código | Kolb (1984) | A experiência anterior ancora o novo conceito |
| Comparar com cálculo à mão | Freeman et al. (2014) | Verificação ativa do resultado |
| Comentar o gráfico | Karpicke (2012) | Elaboração e recuperação |
| IA com verificação | UNESCO (2021) | Transparência e supervisão humana |

---

## 7. Avaliação do encontro

| Critério | Nível 1 | Nível 2 | Nível 3 | Nível 4 |
|---|---|---|---|---|
| Código | Não roda | Roda em parte | Roda completo | Roda e está comentado |
| Limpeza | Não trata | Trata um problema | Trata os principais | Documenta o que tratou |
| Gráfico | Sem título | Com título | Com título, eixos e fonte | Destaca um padrão |
| Leitura | Descreve | Interpreta | Interpreta e aponta limite | Relaciona com hipótese |

---

## 8. Acessibilidade e diferenciação

- Notebook com células prontas e apenas alguns campos para preencher.
- Versão impressa com o código e a saída para quem não tem computador.
- Quem termina antes cria um segundo gráfico comparando dois períodos.

---

## 9. Erros comuns e como conduzir

| Erro | O que fazer |
|---|---|
| Separador `;` em vez de `,` | Usar `sep=';'` e explicar |
| Acentuação no nome da coluna | Copiar o nome exato e evitar digitar |
| Data como texto | `pd.to_datetime()` e conferir |
| `KeyError` | Mostrar `df.columns` e comparar |
| Gráfico vazio | Verificar se o filtro removeu tudo |

---

## 10. Anexo — Ficha de análise

```
Grupo: ______________________  Encontro: 4
Arquivo usado: _______________  Período: _____________
Linhas antes da limpeza: ______  depois: ______________
Variável analisada: ___________________________________
Resultado principal (1 frase): ________________________
Valor máximo/mínimo e data: ___________________________
O que os dados NÃO mostram: ___________________________
O que a IA ajudou e o que eu conferi: _________________
```

---

## 11. Para o professor

- Tenha um CSV pequeno para testar o código rapidamente.
- Se o Colab falhar, use o Python local ou a planilha como plano B.
- Guarde o notebook de cada grupo: ele é a base do encontro 8.

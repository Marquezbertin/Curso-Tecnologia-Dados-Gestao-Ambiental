# Notebooks do curso

Todos os notebooks rodam no **Google Colab** sem instalação. O Colab já traz pandas,
Matplotlib e scikit-learn; o Folium é instalado na primeira célula do notebook de mapas.

| Notebook | Encontros | O que faz |
|---|---|---|
| [`01-primeiros-dados.ipynb`](01-primeiros-dados.ipynb) | 2, 3, 4 e 8 | Lê CSV, limpa, calcula e gera gráfico |
| [`02-mapas-e-territorio.ipynb`](02-mapas-e-territorio.ipynb) | 5 | Cria mapa interativo com Folium |
| [`03-ia-classificacao-ambiental.ipynb`](03-ia-classificacao-ambiental.ipynb) | 6 e 9 | Treina árvore de decisão e avalia o erro |
| [`04-visao-computacional-satelite.ipynb`](04-visao-computacional-satelite.ipynb) | 9 (opcional) | Classifica imagens com modelo pré-treinado |

## Versões resolvidas

Os notebooks com **todas as respostas e comentários** estão em
[`11-RESOLUCAO-DOS-EXERCICIOS/`](../11-RESOLUCAO-DOS-EXERCICIOS/). Use como gabarito, apoio para
quem faltou ou referência para o professor. Eles também rodam com **Runtime → Run all** e baixam
os dados automaticamente.

| Resolução | Notebook original |
|---|---|
| [`01-resolucao-primeiros-dados.ipynb`](../11-RESOLUCAO-DOS-EXERCICIOS/01-resolucao-primeiros-dados.ipynb) | 01 |
| [`02-resolucao-mapas-e-territorio.ipynb`](../11-RESOLUCAO-DOS-EXERCICIOS/02-resolucao-mapas-e-territorio.ipynb) | 02 |
| [`03-resolucao-ia-classificacao-ambiental.ipynb`](../11-RESOLUCAO-DOS-EXERCICIOS/03-resolucao-ia-classificacao-ambiental.ipynb) | 03 |
| [`04-resolucao-visao-computacional-satelite.ipynb`](../11-RESOLUCAO-DOS-EXERCICIOS/04-resolucao-visao-computacional-satelite.ipynb) | 04 |

## Como abrir no Colab

1. Acesse https://colab.research.google.com/
2. Clique em **Arquivo → Fazer upload de notebook** e escolha o `.ipynb`.
3. Faça upload do CSV correspondente em `06-DADOS/exemplos/` (ícone de pasta à esquerda).
4. Rode as células em ordem (`Shift + Enter`).

> **Dica:** faça uma cópia em **Arquivo → Salvar uma cópia no Drive** para não perder as
> alterações.

## Como abrir localmente

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
jupyter notebook
```

## Dados

Os arquivos em `06-DADOS/exemplos/` são **sintéticos e didáticos**. Para dados reais, use as
fontes do [`06-DADOS/README.md`](../06-DADOS/README.md).

## Regras de uso de IA nos notebooks

- Toda resposta de IA é conferida com o código ou com a fonte.
- Registre o prompt e o que foi verificado.
- Não cole dados pessoais em prompts.
- O notebook entregue é de autoria do grupo; a IA é assistente.

## Problemas comuns

| Problema | Solução |
|---|---|
| `FileNotFoundError` | Faça upload do CSV para a sessão do Colab |
| `ModuleNotFoundError: folium` | Rode a célula `!pip -q install folium` |
| `ModuleNotFoundError: sklearn` | No Colab, reinicie o ambiente; localmente, `pip install scikit-learn` |
| Acento quebrado | Confirme que o CSV está em UTF-8 |
| TensorFlow lento | Use a Opção A (Teachable Machine) do notebook 04 |

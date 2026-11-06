# 📚 12-APOSTILA-DIDATICA — Apostila Oficial do Curso

Este diretório contém o material didático completo, unificado e detalhado do curso **"Tecnologia, Dados e Inteligência Artificial na Gestão Ambiental"**, formatado especialmente para **estudantes e profissionais leigos em tecnologia e programação**, bem como para **educadores e gestores ambientais**.

---

## 📄 Arquivo Principal em PDF

- **[`Apostila-Tecnologia-Dados-Gestao-Ambiental.pdf`](Apostila-Tecnologia-Dados-Gestao-Ambiental.pdf)**: Documento completo diagramado profissionalmente (28 páginas, padrão A4, alta resolução), contendo:
  - Capa institucional e ficha catalográfica aberta (CC BY-NC-SA 4.0 e MIT).
  - Sumário detalhado dos 10 módulos.
  - **Módulos 1 a 10** cobrindo 100% da grade curricular do curso.
  - **7 Gráficos Didáticos Científicos** gerados sob medida (séries temporais, camadas SIG, correlações de queimadas, análise de outliers, matriz de confusão didática, árvore de decisão conceitual e ciclo da gestão ambiental).
  - **Tabelas comparativas e conceituais** (portais abertos, tipos de variáveis, sistemas PRODES vs. DETER, instrumentos de ciência cidadã, métricas de IA).
  - **Desconstrução de código linha a linha** de todos os blocos executáveis dos notebooks (Pandas, Matplotlib, Folium, Scikit-Learn e TensorFlow), traduzindo comandos de máquina para a linguagem humana cotidiana.
  - **Boxes pedagógicos**: *💡 Desmistificando*, *🌿 Conexão Ambiental*, *⚠️ Atenção ao Erro Comum* e *🎯 Passo a Passo Prático*.
  - **Apêndice A:** Glossário Didático Integrado com mais de 30 verbetes essenciais.
  - **Apêndice B:** Guia Rápido de Consulta de Sintaxe Python, Pandas e Folium.
  - **Apêndice C:** Caderno de Resolução Comentada dos Exercícios dos Notebooks.

---

## 🛠️ Estrutura dos Arquivos de Construção

Se você for professor ou desenvolvedor e desejar customizar os textos, adicionar novos módulos ou atualizar os gráficos, todos os scripts fonte estão disponíveis:

| Arquivo | Função |
|---|---|
| `compilar_apostila.py` | Script mestre que executa a montagem e gera o arquivo PDF final. |
| `gerar_graficos.py` | Script que gera as 7 figuras e diagramas em alta resolução (pasta `graficos/`). |
| `estilos_apostila.py` | Configuração da paleta de cores, estilos tipográficos ReportLab e numeração dinâmica de páginas. |
| `conteudo_parte1.py` | Capa, Sumário e textos completos dos Módulos 1, 2 e 3. |
| `conteudo_parte2.py` | Textos completos, tabelas e códigos dos Módulos 4, 5 e 6. |
| `conteudo_parte3.py` | Textos completos, tabelas e códigos dos Módulos 7, 8, 9 e 10. |
| `conteudo_apendices.py` | Glossário, Guia de Sintaxe e Resolução Comentada dos Exercícios. |
| `graficos/` | Pasta contendo os arquivos PNG gerados em 200–300 DPI embutidos no PDF. |

---

## 🔄 Como Recompilar a Apostila

Caso você faça alterações nos textos ou nos dados, basta executar no terminal:

```bash
# 1. Regenerar os gráficos (se houver alteração visual)
python 12-APOSTILA-DIDATICA/gerar_graficos.py

# 2. Recompilar o PDF completo
python 12-APOSTILA-DIDATICA/compilar_apostila.py
```

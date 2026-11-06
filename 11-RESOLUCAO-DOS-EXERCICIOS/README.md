# Resolução dos exercícios

Notebooks **resolvidos**, comentados e prontos para rodar do início ao fim. Eles são o gabarito
dos notebooks de [`05-NOTEBOOKS-COLAB/`](../05-NOTEBOOKS-COLAB/) e podem ser usados pelo professor
como referência, pela turma como apoio ou por quem está estudando sozinho.

> **Como usar:** abra no Colab, faça uma cópia no seu Drive e clique em **Runtime → Run all**.
> Não é preciso enviar CSV nem imagem: os arquivos são baixados automaticamente do repositório.

## Notebooks

| Notebook | Encontros | O que resolve | Abrir no Colab |
|---|---|---|---|
| [`01-resolucao-primeiros-dados.ipynb`](01-resolucao-primeiros-dados.ipynb) | 2, 3, 4 e 8 | Leitura, limpeza, estatísticas, gráficos, IQR e ficha de fonte | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marquezbertin/Curso-Tecnologia-Dados-Gestao-Ambiental/blob/main/11-RESOLUCAO-DOS-EXERCICIOS/01-resolucao-primeiros-dados.ipynb) |
| [`02-resolucao-mapas-e-territorio.ipynb`](02-resolucao-mapas-e-territorio.ipynb) | 5 | Mapa com Folium, pontos, áreas, focos, legenda e distâncias | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marquezbertin/Curso-Tecnologia-Dados-Gestao-Ambiental/blob/main/11-RESOLUCAO-DOS-EXERCICIOS/02-resolucao-mapas-e-territorio.ipynb) |
| [`03-resolucao-ia-classificacao-ambiental.ipynb`](03-resolucao-ia-classificacao-ambiental.ipynb) | 6 e 9 | Árvore de decisão, baseline, matriz de confusão, métricas, pesos e validação cruzada | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marquezbertin/Curso-Tecnologia-Dados-Gestao-Ambiental/blob/main/11-RESOLUCAO-DOS-EXERCICIOS/03-resolucao-ia-classificacao-ambiental.ipynb) |
| [`04-resolucao-visao-computacional-satelite.ipynb`](04-resolucao-visao-computacional-satelite.ipynb) | 9 (opcional) | MobileNetV2, classificação de duas imagens, limite do modelo e ficha de modelo | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Marquezbertin/Curso-Tecnologia-Dados-Gestao-Ambiental/blob/main/11-RESOLUCAO-DOS-EXERCICIOS/04-resolucao-visao-computacional-satelite.ipynb) |

## O que já está respondido

- **01:** período de 60 dias, temperatura máxima de 35,4 °C em 14/01/2024, chuva total de 253,2 mm,
  janeiro com 187,3 mm e fevereiro com 65,9 mm, correlação fraca (0,183) e nenhum outlier por IQR.
- **02:** Cerrado com 2.926 focos, Mata Atlântica com 1.617, pico em setembro (726) e maior
  registro em setembro de 2022 (99 focos no Cerrado).
- **03:** baseline de 0,822; árvore com `max_depth=3` com acurácia 0,889, precisão 0,800, recall
  0,500 e F1 0,615; matriz `[[72, 2], [8, 8]]`; recall médio na validação cruzada de 0,400.
- **04:** o MobileNetV2 não reconhece paisagem; as cinco classes mais prováveis são objetos do
  ImageNet (por exemplo, *balloon*, *envelope*, *iPod* e *toilet tissue*). Isso demonstra, na
  prática, por que um modelo genérico não serve como laudo ambiental.

## Imagens de exemplo

As imagens [`exemplo-area-verde.jpg`](exemplo-area-verde.jpg) e
[`exemplo-area-queimada.jpg`](exemplo-area-queimada.jpg) são **ilustrações sintéticas** geradas
para a aula. Não são fotos de satélite nem representam um município real.

## Requisitos

- **01–03:** pandas, Matplotlib e scikit-learn. O Colab já traz tudo; localmente,
  `pip install pandas matplotlib scikit-learn`.
- **02:** Folium. A primeira célula instala automaticamente se necessário.
- **04:** PyTorch e torchvision. O Colab já traz; localmente,
  `pip install torch torchvision`. O modelo baixa os pesos do ImageNet na primeira execução.

## Aviso de uso

Os dados são **sintéticos e didáticos**. Não use os resultados como laudo, alerta, fiscalização ou
decisão ambiental real. O notebook 04 mostra justamente o limite de um modelo treinado em outro
domínio. Em qualquer aplicação real, registre a fonte, o período, a versão dos dados e mantenha
**revisão humana** antes de agir.

## Links úteis

- Repositório: <https://github.com/Marquezbertin/Curso-Tecnologia-Dados-Gestao-Ambiental>
- Notebooks originais (com lacunas para completar): [`05-NOTEBOOKS-COLAB/`](../05-NOTEBOOKS-COLAB/)
- Dados de exemplo: [`06-DADOS/exemplos/`](../06-DADOS/exemplos/)
- Guia do professor: [`08-GUIA-DO-PROFESSOR/`](../08-GUIA-DO-PROFESSOR/)

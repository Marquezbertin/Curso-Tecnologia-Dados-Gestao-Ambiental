"""
Conteúdo Didático Parte 2:
- Módulo 4: Python sem Medo (Parte 2: Análise e Gráficos com Pandas e Matplotlib)
- Módulo 5: Geotecnologias e Cartografia Digital: Mapeando o Território com Folium
- Módulo 6: Monitoramento por Satélite: Focos de Calor, Queimadas e Desmatamento
"""

from reportlab.platypus import Paragraph, Spacer, PageBreak, KeepTogether, Image, HRFlowable
from reportlab.lib import colors
import os
from estilos_apostila import criar_box, criar_tabela_codigo, criar_tabela_geral

def obter_modulo_4(styles):
    story = []
    story.append(Paragraph("Módulo 4 — Python sem Medo (Parte 2: Pandas e Matplotlib)", styles['ModTitle']))
    story.append(Paragraph("<i>Análise automatizada de planilhas ambientais e visualização gráfica profissional</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    story.append(Paragraph(
        "No módulo anterior, vimos que o Python nativo lida bem com variáveis e listas simples. Porém, quando trabalhamos com dados do mundo real "
        "— contendo centenas de milhares de linhas meteorológicas ou territoriais —, usamos as <b>Bibliotecas Especializadas</b>. "
        "Uma biblioteca é uma coleção de ferramentas criadas por cientistas do mundo inteiro para resolver problemas complexos com pouquíssimas linhas.",
        styles['Normal']
    ))
    
    story.append(Paragraph("4.1 A Dupla Dinâmica da Ciência de Dados: Pandas e Matplotlib", styles['SecTitle']))
    story.append(Paragraph(
        "Neste curso, trabalhamos com duas bibliotecas consagradas internacionalmente:",
        styles['Normal']
    ))
    story.append(Paragraph(
        "<b>1. Pandas:</b> É o 'Excel superpotente' do Python. Ele permite carregar arquivos CSV, filtrar informações por data ou gravidade, calcular médias por ano ou mês e eliminar registros corrompidos instantaneamente.<br/>"
        "<b>2. Matplotlib:</b> É a ferramenta responsável por desenhar gráficos científicos de alta qualidade (linhas, barras, histogramas e dispersões) com total controle visual de cores, legendas e eixos.",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("4.2 O que é um DataFrame?", styles['SecTitle']))
    story.append(Paragraph(
        "Quando o Pandas carrega um arquivo CSV, ele organiza as informações em uma estrutura chamada <b>DataFrame</b> (frequentemente abreviada no código como <code>df</code>). "
        "Um DataFrame é exatamente uma <b>tabela bidimensional na memória do computador</b>, com linhas numeradas (índice) e colunas nomeadas exatamente como as variáveis do arquivo original.",
        styles['Normal']
    ))
    
    story.append(Paragraph("4.3 Desconstrução do Código: Carregamento, Limpeza e Análise", styles['SecTitle']))
    story.append(Paragraph(
        "Vejamos o passo a passo executado no <b>Notebook 01</b> para carregar e inspecionar a base meteorológica do INMET:",
        styles['Normal']
    ))
    
    codigo_pandas = [
        ("import pandas as pd", "Importa a biblioteca de tabelas Pandas e cria o apelido abreviado 'pd' para facilitar a digitação ao longo do código."),
        ("import matplotlib.pyplot as plt", "Importa o módulo gráfico Pyplot do Matplotlib e cria o apelido 'plt', padrão adotado por cientistas no mundo todo."),
        ("caminho = 'exemplo-inmet-sintetico.csv'", "Armazena em uma variável de texto o nome e local do arquivo CSV meteorológico a ser aberto."),
        ("df = pd.read_csv(caminho)", "A função read_csv() lê o arquivo do disco rígido e o transforma em uma tabela viva na memória do computador (DataFrame)."),
        ("df.info()", "Exibe a 'radiografia' da tabela: quantas linhas existem, os nomes das colunas e se há valores nulos (dados faltantes)."),
        ("df.describe()", "Gera instantaneamente um resumo estatístico completo de todas as colunas numéricas: contagem, média, desvio padrão, mínimo e máximo."),
        ("df['data'] = pd.to_datetime(df['data'])", "Converte a coluna de texto para o formato oficial de data reconhecido pelo computador, habilitando filtros cronológicos."),
        ("df = df.dropna()", "Remove automaticamente todas as linhas que contêm medições nulas ou sensores que falharam (saneamento da base).")
    ]
    story.append(criar_tabela_codigo(codigo_pandas, styles))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("4.4 Desconstrução do Código: Construindo os Gráficos Ambientais", styles['SecTitle']))
    story.append(Paragraph(
        "Após o saneamento da tabela, o código desenha o gráfico de temperatura e o gráfico de precipitação. "
        "Acompanhe o que cada instrução visual comanda no computador:",
        styles['Normal']
    ))
    
    codigo_graficos = [
        ("plt.figure(figsize=(10, 4))", "Cria uma tela de desenho em branco com largura proporcional de 10 unidades e altura de 4 unidades."),
        ("plt.plot(df['data'], df['temp_max_c'], label='Temperatura Máxima', color='red')", "Desenha uma linha conectando as datas no eixo horizontal (X) com as temperaturas no eixo vertical (Y), com traço vermelho."),
        ("plt.title('Série Histórica de Temperaturas')", "Adiciona o título didático no topo do gráfico para contextualizar quem está lendo."),
        ("plt.xlabel('Data da Medição')", "Escreve a identificação do que representa o eixo horizontal."),
        ("plt.ylabel('Temperatura em °C')", "Escreve a unidade de medida oficial no eixo vertical."),
        ("plt.grid(True, linestyle='--')", "Insere linhas de grade pontilhadas suaves para facilitar a leitura visual dos valores exatos."),
        ("plt.legend()", "Exibe a legenda identificando o significado da linha traçada no gráfico."),
        ("plt.show()", "Finaliza a renderização e exibe o gráfico na tela para visualização imediata do usuário.")
    ]
    story.append(criar_tabela_codigo(codigo_graficos, styles))
    story.append(Spacer(1, 10))
    
    story.append(criar_box(
        "COMO FILTRAR SITUAÇÕES DE EMERGÊNCIA",
        ["Com o Pandas, você pode fazer perguntas inteligentes à base de dados com comandos de uma linha só:",
         "<b>Dias de Calor Extremo:</b> <code>dias_criticos = df[df['temp_max_c'] >= 35]</code> (Seleciona apenas dias com 35°C ou mais).",
         "<b>Seca Severa:</b> <code>dias_sem_chuva = df[df['chuva_mm'] == 0]</code> (Filtra todos os dias em que não caiu uma única gota d'água).",
         "<b>Temporais Perigosos:</b> <code>temporais = df[df['chuva_mm'] > 40]</code> (Identifica datas com risco iminente de alagamentos urbanos)."],
        tipo="didatico",
        styles=styles
    ))
    
    story.append(PageBreak())
    return story

def obter_modulo_5(styles, img_dir):
    story = []
    story.append(Paragraph("Módulo 5 — Geotecnologias e Cartografia Digital: Mapeando o Território", styles['ModTitle']))
    story.append(Paragraph("<i>Sistemas de Informação Geográfica (SIG), coordenadas e mapas interativos com Folium</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    story.append(Paragraph(
        "Todos os problemas ambientais — desmatamento, queimadas, poluição hídrica ou ilhas de calor urbano — ocorrem em um <b>lugar físico específico</b>. "
        "Saber apenas que <i>'houve 50 focos de incêndio no município'</i> não resolve a emergência; a Defesa Civil precisa saber <b>onde</b> eles estão. "
        "Aqui entram as <b>Geotecnologias</b> e os <b>Sistemas de Informação Geográfica (SIG)</b>.",
        styles['Normal']
    ))
    
    story.append(Paragraph("5.1 Coordenadas Geográficas: Latitude e Longitude para Leigos", styles['SecTitle']))
    story.append(Paragraph(
        "A Terra é dividida por uma grade imaginária que permite identificar qualquer centímetro do planeta usando dois números decimais:",
        styles['Normal']
    ))
    story.append(Paragraph(
        "<b>• Latitude (Eixo Norte-Sul):</b> Mede a distância em graus a partir da Linha do Equador (0°). Valores ao Norte são positivos e ao Sul são negativos. Como o Brasil está quase todo no Hemisfério Sul, as nossas latitudes são sempre <b>negativas</b> (ex: São Paulo está em aproximadamente -23.55°).<br/>"
        "<b>• Longitude (Eixo Leste-Oeste):</b> Mede a distância em graus a partir do Meridiano de Greenwich (0°). Como o Brasil inteiro está situado no Hemisfério Ocidental (a Oeste de Greenwich), nossas longitudes também são <b>negativas</b> (ex: São Paulo está em aproximadamente -46.63°).",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("5.2 A Lógica do SIG: O Mundo em Camadas", styles['SecTitle']))
    story.append(Paragraph(
        "Um software de geoprocessamento moderno não desenha tudo misturado. Ele organiza o território em <b>Camadas Sobrepostas (Layers)</b>. "
        "Veja na Figura 2 como diferentes dimensões da realidade se combinam para apoiar a tomada de decisão:",
        styles['Normal']
    ))
    
    # Inserção da Figura 2
    caminho_fig2 = os.path.join(img_dir, "grafico2_camadas_sig.png")
    if os.path.exists(caminho_fig2):
        story.append(Image(caminho_fig2, width=470, height=220))
        story.append(Paragraph("Figura 2: Estrutura em camadas sobrepostas de um Sistema de Informação Geográfica (SIG) para gestão ambiental municipal.", styles['FigCaption']))
        story.append(Spacer(1, 8))
        
    story.append(Paragraph("5.3 Criando Mapas Interativos com a Biblioteca Folium", styles['SecTitle']))
    story.append(Paragraph(
        "O <b>Folium</b> é uma biblioteca Python fantástica que conecta dados tabulares com a biblioteca JavaScript Leaflet. "
        "Ela gera mapas totalmente dinâmicos, que você pode aproximar com o zoom, arrastar com o mouse e clicar sobre os pontos para abrir janelas de detalhes (popups).",
        styles['Normal']
    ))
    
    story.append(Paragraph(
        "Abaixo está a desconstrução pedagógica do código principal utilizado no <b>Notebook 02</b>:",
        styles['Normal']
    ))
    
    codigo_folium = [
        ("!pip -q install folium", "Instala a biblioteca no servidor em nuvem do Colab sem poluir a tela com mensagens técnicas desnecessárias."),
        ("import folium", "Carrega o motor cartográfico do Folium na memória do programa para uso."),
        ("lat, lon = -22.55, -47.90", "Define as coordenadas geográficas exatas do ponto central onde o mapa deve abrir."),
        ("mapa = folium.Map(location=[lat, lon], zoom_start=13)", "Desenha o mapa base centralizado nas coordenadas informadas, definindo um nível de ampliação (zoom) adequado."),
        ("camada_focos = folium.FeatureGroup(name='Focos de Calor')", "Cria uma camada temática exclusiva para organizar os pontos de incêndio separadamente."),
        ("folium.Marker([lat, lon], popup='Ponto Crítico', icon=folium.Icon(color='red')).add_to(camada_focos)", "Adiciona um marcador com alfinete vermelho e balão informativo na posição indicada."),
        ("folium.CircleMarker([lat, lon], radius=15, color='orange', fill=True).add_to(camada_focos)", "Desenha uma área circular de raio 15 metros para simbolizar o raio de impacto do foco."),
        ("camada_focos.add_to(mapa)", "Insere a camada temática completa dentro do mapa principal."),
        ("folium.LayerControl().add_to(mapa)", "Cria um botão no canto superior do mapa que permite ao usuário ligar e desligar cada camada temática individualmente.")
    ]
    story.append(criar_tabela_codigo(codigo_folium, styles))
    
    story.append(PageBreak())
    return story

def obter_modulo_6(styles, img_dir):
    story = []
    story.append(Paragraph("Módulo 6 — Monitoramento Ambiental por Satélite: Queimadas e Desmatamento", styles['ModTitle']))
    story.append(Paragraph("<i>Como sensores orbitais detectam o fogo e a perda de florestas no Brasil</i>", styles['Normal']))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#145a32'), spaceBefore=2, spaceAfter=10))
    
    story.append(Paragraph(
        "O Brasil possui mais de 8,5 milhões de km² de território continental. Seria humanamente e financeiramente impossível colocar fiscais a pé "
        "para vigiar cada pedaço da Amazônia, Cerrado, Mata Atlântica ou Pantanal. O monitoramento ecológico em escala continental só é viável "
        "graças ao <b>Sensoriamento Remoto por Satélites</b>.",
        styles['Normal']
    ))
    
    story.append(Paragraph("6.1 O que é Exatamente um 'Foco de Calor' do INPE?", styles['SecTitle']))
    story.append(Paragraph(
        "Muitos cidadãos e jornalistas cometem o equívoco de dizer que <i>'o satélite tirou uma foto da fogueira'</i>. Não é assim que funciona. "
        "Os satélites meteorológicos utilizados pelo Programa Queimadas do INPE (como a série NOAA, Terra e Aqua) operam na faixa do <b>infravermelho termal</b>. "
        "Eles medem a <b>temperatura de brilho</b> de uma área de aproximadamente 1 km × 1 km na superfície terrestre.",
        styles['Normal']
    ))
    story.append(Paragraph(
        "Quando uma frente de fogo com mais de 30 metros de extensão emite calor intenso, a temperatura média daquele pixel sobe drasticamente. "
        "O algoritmo matemático do INPE compara aquele valor com os pixels vizinhos que estão frios e registra um <b>Foco de Calor</b> georreferenciado.",
        styles['Normal']
    ))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("6.2 A Diferença Crucial: PRODES versus DETER", styles['SecTitle']))
    story.append(Paragraph(
        "Dentro do próprio INPE existem dois sistemas fundamentais que medem o desmatamento, mas com finalidades e metodologias distintas. "
        "Confundir esses dois sistemas é o erro mais comum em reuniões de meio ambiente:",
        styles['Normal']
    ))
    
    comp_sistemas = [
        ["Critério", "Sistema PRODES (Oficial Anual)", "Sistema DETER (Alertas Rápidos Diários)"],
        ["Finalidade Central", "Medir a taxa oficial e consolidada de desmatamento por corte raso no ano.", "Orientar a fiscalização do IBAMA e órgãos estaduais em tempo quase real."],
        ["Frequência / Prazo", "Publicação anual consolidada (medida de agosto de um ano a julho do ano seguinte).", "Divulgação diária ou semanal para flagrar o crime ambiental enquanto ele acontece."],
        ["Área Mínima Mapeada", "Polígonos a partir de 6,25 hectares (satélites de alta resolução óptica).", "Polígonos a partir de 3 hectares (satélites com maior frequência de revisita)."],
        ["Uso Recomendado", "Balanços históricos, metas internacionais do clima e formulação de políticas.", "Operações de campo de fiscalização e aplicação de multas emergenciais."]
    ]
    story.append(criar_tabela_geral(comp_sistemas[0], comp_sistemas[1:], [110, 195, 200], styles))
    story.append(Spacer(1, 10))
    
    # Inserção da Figura 3
    caminho_fig3 = os.path.join(img_dir, "grafico3_queimadas_desmatamento.png")
    if os.path.exists(caminho_fig3):
        story.append(Image(caminho_fig3, width=470, height=220))
        story.append(Paragraph("Figura 3: Correlação histórica entre focos de calor registrados e desmatamento anual consolidado em km².", styles['FigCaption']))
        story.append(Spacer(1, 8))
        
    story.append(Paragraph("6.3 Limitações e Vieses do Monitoramento Orbital", styles['SecTitle']))
    story.append(Paragraph(
        "Nenhum sensor é perfeito. Para analisar relatórios de queimadas e desmatamento sem ingenuidade, o gestor leigo precisa conhecer os 4 vieses clássicos:",
        styles['Normal']
    ))
    
    vieses_satelite = [
        "<b>1. Cobertura de Nuvens:</b> Sensores ópticos e termais não enxergam através de nuvens densas. Em dias chuvosos ou muito nublados, um incêndio pode estar ocorrendo sem ser detectado pelo satélite.",
        "<b>2. Fogo Rasteiro sob a Copa:</b> Incêndios que queimam apenas a vegetação rasteira sob florestas densas e fechadas muitas vezes têm seu calor bloqueado pelas árvores altas.",
        "<b>3. Horário de Passagem:</b> Satélites de órbita polar passam sobre o município apenas uma ou duas vezes ao dia em horários fixos (geralmente início da tarde). Queimadas criminosas feitas à noite podem escapar do satélite de referência.",
        "<b>4. Resolução Temporal vs. Espacial:</b> Satélites que cobrem o planeta inteiro todo dia têm pixels mais largos (menor detalhe). Satélites com detalhe métrico demoram muitos dias para passar novamente no mesmo local."
    ]
    story.append(criar_box("OS LIMITES DA TECNOLOGIA NO ESPAÇO", vieses_satelite, tipo="alerta", styles=styles))
    
    story.append(PageBreak())
    return story

print("Módulo de conteúdo didático parte 2 compilado com sucesso.")

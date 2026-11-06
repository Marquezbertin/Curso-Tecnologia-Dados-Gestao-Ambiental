import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os

output_dir = r"C:\Users\Usuário\Desktop\Curso-Tecnologia-Dados-Gestao-Ambiental\12-APOSTILA-DIDATICA\graficos"
os.makedirs(output_dir, exist_ok=True)

# Estilo geral limpo e profissional
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#cccccc'
plt.rcParams['axes.linewidth'] = 0.8

# 1. Gráfico Série Temporal Climática (Módulo 2 e 4)
fig, ax1 = plt.subplots(figsize=(8.5, 4.2), dpi=200)

dias = np.arange(1, 31)
np.random.seed(42)
temp_max = 27 + 5 * np.sin(dias / 5.0) + np.random.normal(0, 1.2, 30)
temp_max[14] = 38.5  # Outlier de calor extremo
chuva_mm = np.random.exponential(scale=4, size=30)
chuva_mm[chuva_mm < 1.5] = 0
chuva_mm[14] = 0
chuva_mm[22] = 45.0  # Temporal

ax2 = ax1.twinx()
ax2.bar(dias, chuva_mm, color='#2b7bba', alpha=0.6, width=0.6, label='Chuva (mm)')
ax2.set_ylabel('Precipitação Acumulada (mm)', color='#1a5380', fontsize=10, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='#1a5380')
ax2.set_ylim(0, 60)

ax1.plot(dias, temp_max, color='#d9381e', marker='o', markersize=4, linewidth=2, label='Temp. Máxima (°C)')
ax1.set_ylabel('Temperatura (°C)', color='#a6240f', fontsize=10, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='#a6240f')
ax1.set_ylim(18, 42)
ax1.set_xlabel('Dias do Mês de Monitoramento', fontsize=10, fontweight='bold')
ax1.set_title('Figura 1: Monitoramento Meteorológico Integrado — Temperatura e Chuva Diária', fontsize=11, fontweight='bold', pad=12, color='#1f2d3d')

# Anotação didática de outlier
ax1.annotate('Valor Atípico (Outlier):\nOnda de Calor Extrema (38.5°C)', xy=(15, 38.5), xytext=(17, 39.5),
             arrowprops=dict(facecolor='#d9381e', shrink=0.08, width=1.5, headwidth=6),
             fontsize=8.5, fontweight='bold', color='#801403',
             bbox=dict(boxstyle="round,pad=0.3", fc="#fdf2f0", ec="#d9381e", lw=1))

# Anotação de temporal
ax2.annotate('Evento Extremo de Chuva:\nTemporal Localizado (45 mm)', xy=(23, 45), xytext=(15, 48),
             arrowprops=dict(facecolor='#1a5380', shrink=0.08, width=1.5, headwidth=6),
             fontsize=8.5, fontweight='bold', color='#0b3252',
             bbox=dict(boxstyle="round,pad=0.3", fc="#eef6fb", ec="#2b7bba", lw=1))

ax1.grid(True, linestyle='--', alpha=0.4)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, "grafico1_serie_climatica.png"))
plt.close(fig)

# 2. Diagrama de Camadas de Dados Espaciais (SIG / Geotecnologias) (Módulo 5)
fig, ax = plt.subplots(figsize=(8.5, 4.0), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Caixas representando camadas empilhadas
layers = [
    ("Camada 4: Gestão e Decisão", "Áreas prioritárias para fiscalização e plantio comunitário", "#e7f6ec", "#27ae60", 4.5),
    ("Camada 3: Monitoramento Dinâmico (Pontos)", "Focos de calor INPE / BDQueimadas e denúncias de descarte", "#fef5e7", "#e67e22", 3.2),
    ("Camada 2: Vetorial e Hidrografia (Linhas e Polígonos)", "Bacias hidrográficas, nascentes, ruas e limites de bairros", "#ebf5fb", "#2980b9", 1.9),
    ("Camada 1: Imagem Base / Sensoriamento Remoto", "Satélite Sentinel/Landsat e Cobertura do Solo MapBiomas", "#f4f6f7", "#7f8c8d", 0.6)
]

for title, desc, bg_color, border_color, y_pos in layers:
    rect = plt.Rectangle((1.0, y_pos), 8.0, 0.9, facecolor=bg_color, edgecolor=border_color, linewidth=2)
    ax.add_patch(rect)
    ax.text(1.3, y_pos + 0.52, title, fontsize=10, fontweight='bold', color=border_color)
    ax.text(1.3, y_pos + 0.22, desc, fontsize=8.5, color='#333333')

# Linhas de conexão vertical
ax.annotate('', xy=(0.6, 5.2), xytext=(0.6, 0.8),
            arrowprops=dict(arrowstyle="->", color='#2c3e50', lw=2.5))
ax.text(0.3, 3.0, 'INTEGRAÇÃO ESPACIAL DE DADOS', rotation=90, va='center', ha='center', fontsize=9, fontweight='bold', color='#2c3e50')

ax.set_title('Figura 2: Estrutura em Camadas de um Sistema de Informações Geográficas (SIG)', fontsize=11, fontweight='bold', pad=10, color='#1f2d3d')
fig.tight_layout()
fig.savefig(os.path.join(output_dir, "grafico2_camadas_sig.png"))
plt.close(fig)

# 3. Gráfico Comparativo Queimadas e Desmatamento (Módulo 6)
fig, ax1 = plt.subplots(figsize=(8.5, 4.2), dpi=200)

anos = np.arange(2018, 2025)
focos_calor = [1240, 1890, 2450, 1920, 2180, 1650, 1420]
desmatamento_km2 = [145.2, 210.5, 290.8, 230.1, 260.4, 185.0, 160.2]

ax2 = ax1.twinx()
p1 = ax1.bar(anos - 0.18, focos_calor, width=0.35, color='#e67e22', alpha=0.85, label='Focos de Calor (INPE/BDQueimadas)')
p2 = ax2.bar(anos + 0.18, desmatamento_km2, width=0.35, color='#c0392b', alpha=0.85, label='Área Desmatada em km² (PRODES)')

ax1.set_xlabel('Ano de Monitoramento', fontsize=10, fontweight='bold')
ax1.set_ylabel('Número de Focos de Calor Detectados', color='#b95f13', fontsize=10, fontweight='bold')
ax1.tick_params(axis='y', labelcolor='#b95f13')
ax1.set_ylim(0, 3000)

ax2.set_ylabel('Área Suprimida Acumulada (km²)', color='#8e2519', fontsize=10, fontweight='bold')
ax2.tick_params(axis='y', labelcolor='#8e2519')
ax2.set_ylim(0, 350)

ax1.set_title('Figura 3: Correlação entre Alertas de Queimadas e Desmatamento Consolidado Anual', fontsize=11, fontweight='bold', pad=12, color='#1f2d3d')
ax1.grid(True, linestyle=':', alpha=0.5)

# Linha de legenda integrada
lines = [p1, p2]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', frameon=True, framealpha=0.9, fontsize=8.5)

fig.tight_layout()
fig.savefig(os.path.join(output_dir, "grafico3_queimadas_desmatamento.png"))
plt.close(fig)

# 4. Gráfico Estatística: Média vs. Mediana com Outliers (Módulo 8)
fig, ax = plt.subplots(figsize=(8.5, 4.0), dpi=200)

amostras = [12, 14, 15, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 110]  # 110 é um descarte clandestino pontual
media = np.mean(amostras)
mediana = np.median(amostras)

y_jitter = np.zeros(len(amostras)) + 0.5
ax.scatter(amostras[:-1], y_jitter[:-1], color='#2980b9', s=70, alpha=0.7, edgecolors='black', label='Medições Comuns (kg de resíduos)')
ax.scatter(amostras[-1], y_jitter[-1], color='#e74c3c', s=120, edgecolors='black', zorder=5, label='Descarte Excepcional / Outlier (110 kg)')

ax.axvline(media, color='#d35400', linestyle='--', linewidth=2, label=f'Média Aritmética ({media:.1f} kg) — Puxada pelo extremo!')
ax.axvline(mediana, color='#27ae60', linestyle='-', linewidth=2.5, label=f'Mediana Robusta ({mediana:.1f} kg) — Representa a realidade típica!')

ax.set_ylim(0.2, 0.8)
ax.set_yticks([])
ax.set_xlim(0, 125)
ax.set_xlabel('Resíduos Coletados por Ponto Amostral (kg)', fontsize=10, fontweight='bold')
ax.set_title('Figura 4: O Efeito Distorcedor de Valores Extremos — Por que a Mediana Protege a Análise', fontsize=11, fontweight='bold', pad=12, color='#1f2d3d')

ax.annotate(f'MÉDIA = {media:.1f} kg\n(Distorcida)', xy=(media, 0.58), xytext=(media+8, 0.68),
            arrowprops=dict(facecolor='#d35400', shrink=0.05, width=1.2, headwidth=5),
            fontsize=9, fontweight='bold', color='#a04000',
            bbox=dict(boxstyle="round,pad=0.3", fc="#fbeee6", ec="#d35400", lw=1))

ax.annotate(f'MEDIANA = {mediana:.1f} kg\n(Valor Central Típico)', xy=(mediana, 0.42), xytext=(mediana-5, 0.28),
            arrowprops=dict(facecolor='#27ae60', shrink=0.05, width=1.2, headwidth=5),
            fontsize=9, fontweight='bold', color='#196f3d',
            bbox=dict(boxstyle="round,pad=0.3", fc="#eafaf1", ec="#27ae60", lw=1))

ax.legend(loc='upper right', frameon=True, fontsize=8.5)
ax.grid(True, axis='x', linestyle=':', alpha=0.6)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, "grafico4_estatistica_outliers.png"))
plt.close(fig)

# 5. Matriz de Confusão Didática para Gestão Ambiental (Módulo 9)
fig, ax = plt.subplots(figsize=(8.5, 4.4), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis('off')

# Quatro quadrantes
# VP (Fogo Real + Previsto Fogo)
rect_vp = plt.Rectangle((5.2, 5.2), 4.3, 3.8, facecolor='#d4efdf', edgecolor='#27ae60', lw=2)
ax.add_patch(rect_vp)
ax.text(7.35, 8.2, 'VERDADEIRO POSITIVO (VP)', ha='center', fontsize=10, fontweight='bold', color='#1e8449')
ax.text(7.35, 7.3, 'Previsão: FOGO  |  Real: FOGO', ha='center', fontsize=9, fontweight='bold', color='#2c3e50')
ax.text(7.35, 6.1, 'A equipe ambiental é enviada\ne contém o foco a tempo!\nSucesso total da prevenção.', ha='center', fontsize=8, color='#333333')

# FN (Fogo Real + Previsto NÃO Fogo) - O erro mais grave!
rect_fn = plt.Rectangle((1.0, 5.2), 4.0, 3.8, facecolor='#fadbd8', edgecolor='#c0392b', lw=2)
ax.add_patch(rect_fn)
ax.text(3.0, 8.2, 'FALSO NEGATIVO (FN)', ha='center', fontsize=10, fontweight='bold', color='#922b21')
ax.text(3.0, 7.3, 'Previsão: NÃO  |  Real: FOGO', ha='center', fontsize=9, fontweight='bold', color='#78281f')
ax.text(3.0, 6.1, 'ERRO CRÍTICO!\nO incêndio ocorre sem alerta\ne destrói a mata protegida.', ha='center', fontsize=8, color='#5c1d16')

# FP (Não Fogo Real + Previsto Fogo) - Alarme falso
rect_fp = plt.Rectangle((5.2, 1.0), 4.3, 3.8, facecolor='#fcf3cf', edgecolor='#f39c12', lw=2)
ax.add_patch(rect_fp)
ax.text(7.35, 4.0, 'FALSO POSITIVO (FP)', ha='center', fontsize=10, fontweight='bold', color='#b7950b')
ax.text(7.35, 3.1, 'Previsão: FOGO  |  Real: NÃO', ha='center', fontsize=9, fontweight='bold', color='#7d6608')
ax.text(7.35, 1.9, 'ALARME FALSO!\nA equipe gasta combustível\nmas encontra o local seguro.', ha='center', fontsize=8, color='#4d4007')

# VN (Não Fogo Real + Previsto NÃO Fogo)
rect_vn = plt.Rectangle((1.0, 1.0), 4.0, 3.8, facecolor='#e8f8f5', edgecolor='#16a085', lw=2)
ax.add_patch(rect_vn)
ax.text(3.0, 4.0, 'VERDADEIRO NEGATIVO (VN)', ha='center', fontsize=10, fontweight='bold', color='#117864')
ax.text(3.0, 3.1, 'Previsão: NÃO  |  Real: NÃO', ha='center', fontsize=9, fontweight='bold', color='#2c3e50')
ax.text(3.0, 1.9, 'Dia tranquilo e sem incidentes.\nModelo operando normalmente.', ha='center', fontsize=8, color='#333333')

# Rótulos externos
ax.text(0.4, 7.1, 'REAL:\nINCÊNDIO', va='center', ha='center', fontsize=9, fontweight='bold', color='#c0392b')
ax.text(0.4, 2.9, 'REAL:\nSEM FOGO', va='center', ha='center', fontsize=9, fontweight='bold', color='#27ae60')
ax.text(3.0, 9.4, 'PREVISÃO: SEM FOGO', ha='center', fontsize=9, fontweight='bold', color='#555555')
ax.text(7.35, 9.4, 'PREVISÃO: ALERTA DE FOGO', ha='center', fontsize=9, fontweight='bold', color='#c0392b')

ax.set_title('Figura 5: Matriz de Confusão Explicada para Gestores Ambientais — O Custo do Erro em IA', fontsize=11, fontweight='bold', pad=12, color='#1f2d3d')
fig.tight_layout()
fig.savefig(os.path.join(output_dir, "grafico5_matriz_confusao.png"))
plt.close(fig)

# 6. Diagrama de Árvore de Decisão Didática (Módulo 9)
fig, ax = plt.subplots(figsize=(8.5, 4.2), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

# Raiz
rect_root = plt.Rectangle((3.5, 4.6), 3.0, 1.1, facecolor='#ebf5fb', edgecolor='#2980b9', lw=2)
ax.add_patch(rect_root)
ax.text(5.0, 5.25, 'Umidade Relativa < 30%?', ha='center', fontsize=9.5, fontweight='bold', color='#1b4f72')
ax.text(5.0, 4.85, '(Variável Mais Crítica)', ha='center', fontsize=8, color='#555555')

# Nó Esquerdo (Alta umidade -> Risco Baixo)
rect_l1 = plt.Rectangle((0.6, 2.3), 3.2, 1.1, facecolor='#eafaf1', edgecolor='#27ae60', lw=2)
ax.add_patch(rect_l1)
ax.text(2.2, 2.95, 'FOLHA: RISCO BAIXO', ha='center', fontsize=9.5, fontweight='bold', color='#196f3d')
ax.text(2.2, 2.55, 'Ar úmido inibe a propagação', ha='center', fontsize=8, color='#333333')

# Nó Direito (Baixa umidade -> Testa Temperatura)
rect_r1 = plt.Rectangle((5.8, 2.3), 3.6, 1.1, facecolor='#fef9e7', edgecolor='#f39c12', lw=2)
ax.add_patch(rect_r1)
ax.text(7.6, 2.95, 'Temperatura Máxima > 32°C?', ha='center', fontsize=9.5, fontweight='bold', color='#9a7d0a')
ax.text(7.6, 2.55, 'Combustão espontânea / calor', ha='center', fontsize=8, color='#555555')

# Folhas finais sob o nó direito
rect_ll2 = plt.Rectangle((4.8, 0.4), 2.3, 1.0, facecolor='#fdf2e9', edgecolor='#e67e22', lw=2)
ax.add_patch(rect_ll2)
ax.text(5.95, 0.95, 'RISCO MÉDIO', ha='center', fontsize=9, fontweight='bold', color='#a04000')
ax.text(5.95, 0.60, 'Vigilância passiva', ha='center', fontsize=7.5, color='#333333')

rect_rr2 = plt.Rectangle((7.5, 0.4), 2.3, 1.0, facecolor='#fadbd8', edgecolor='#c0392b', lw=2)
ax.add_patch(rect_rr2)
ax.text(8.65, 0.95, 'RISCO CRÍTICO', ha='center', fontsize=9, fontweight='bold', color='#922b21')
ax.text(8.65, 0.60, 'Alerta aos brigadistas!', ha='center', fontsize=7.5, color='#333333')

# Conexões
# Raiz para L1 (NÃO)
ax.annotate('NÃO (>= 30%)', xy=(2.2, 3.4), xytext=(3.7, 4.6),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='#27ae60'),
            fontsize=8, fontweight='bold', color='#196f3d')

# Raiz para R1 (SIM)
ax.annotate('SIM (< 30%)', xy=(7.6, 3.4), xytext=(6.3, 4.6),
            arrowprops=dict(arrowstyle="->", lw=1.5, color='#c0392b'),
            fontsize=8, fontweight='bold', color='#922b21')

# R1 para Folha Média (NÃO)
ax.annotate('NÃO', xy=(5.95, 1.4), xytext=(6.8, 2.3),
            arrowprops=dict(arrowstyle="->", lw=1.3, color='#e67e22'),
            fontsize=8, fontweight='bold', color='#a04000')

# R1 para Folha Crítica (SIM)
ax.annotate('SIM', xy=(8.65, 1.4), xytext=(8.4, 2.3),
            arrowprops=dict(arrowstyle="->", lw=1.3, color='#c0392b'),
            fontsize=8, fontweight='bold', color='#922b21')

ax.set_title('Figura 6: Modelo de Árvore de Decisão Interpretável — Regras Transparentes de Classificação', fontsize=11, fontweight='bold', pad=12, color='#1f2d3d')
fig.tight_layout()
fig.savefig(os.path.join(output_dir, "grafico6_arvore_decisao.png"))
plt.close(fig)

# 7. Ciclo Virtuoso da Gestão Ambiental Orientada por Dados (Módulo 10)
fig, ax = plt.subplots(figsize=(8.5, 4.0), dpi=200)
ax.set_xlim(0, 10)
ax.set_ylim(0, 6)
ax.axis('off')

steps = [
    ("1. Problema Territorial", "Identificação de dor real no município", 1.5, 4.5, '#e8f8f5', '#16a085'),
    ("2. Fontes & Ciência Cidadã", "Dados abertos + Coleta em campo", 5.0, 4.5, '#ebf5fb', '#2980b9'),
    ("3. Tratamento & Python", "Limpeza, Pandas e Visualização", 8.5, 4.5, '#f4ecf7', '#8e44ad'),
    ("6. Ação & Política Pública", "Impacto positivo na sociedade", 1.5, 1.5, '#eafaf1', '#27ae60'),
    ("5. Storytelling & Defesa", "Pôster, Pitch e Tomada de Decisão", 5.0, 1.5, '#fef9e7', '#f39c12'),
    ("4. Modelagem & IA", "Classificação e Avaliação Ética", 8.5, 1.5, '#fdf2e9', '#d35400')
]

for title, desc, cx, cy, bg_c, border_c in steps:
    rect = plt.Rectangle((cx-1.4, cy-0.6), 2.8, 1.2, facecolor=bg_c, edgecolor=border_c, lw=2)
    ax.add_patch(rect)
    ax.text(cx, cy+0.15, title, ha='center', fontsize=8.5, fontweight='bold', color=border_c)
    ax.text(cx, cy-0.25, desc, ha='center', fontsize=7.2, color='#333333')

# Setas do fluxo
arrow_style = dict(arrowstyle="->", lw=2, color='#34495e')
ax.annotate('', xy=(3.5, 4.5), xytext=(2.9, 4.5), arrowprops=arrow_style)
ax.annotate('', xy=(7.0, 4.5), xytext=(6.4, 4.5), arrowprops=arrow_style)
ax.annotate('', xy=(8.5, 2.2), xytext=(8.5, 3.8), arrowprops=arrow_style)
ax.annotate('', xy=(6.5, 1.5), xytext=(7.1, 1.5), arrowprops=arrow_style)
ax.annotate('', xy=(3.0, 1.5), xytext=(3.6, 1.5), arrowprops=arrow_style)
ax.annotate('', xy=(1.5, 3.8), xytext=(1.5, 2.2), arrowprops=dict(arrowstyle="->", lw=2, color='#27ae60', linestyle='--'))

ax.set_title('Figura 7: O Ciclo Completo da Gestão Ambiental Orientada por Dados e Evidências', fontsize=11, fontweight='bold', pad=12, color='#1f2d3d')
fig.tight_layout()
fig.savefig(os.path.join(output_dir, "grafico7_ciclo_gestao_dados.png"))
plt.close(fig)

print("Todos os 7 gráficos gerados com sucesso em:", output_dir)

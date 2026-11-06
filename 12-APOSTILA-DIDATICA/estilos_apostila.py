"""
Script de Geração da Apostila Didática Completa do Curso:
'Tecnologia, Dados e Inteligência Artificial na Gestão Ambiental'

Gera um PDF didático profissional, extenso, passo a passo, voltado para leigos,
com desconstrução linha a linha de códigos, tabelas comparativas e gráficos didáticos embutidos.
"""

import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

# ==============================================================================
# 1. CANVAS DE DUAS PASSAGENS PARA NUMERAÇÃO DE PÁGINAS "PÁGINA X DE Y"
# ==============================================================================
class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            if self._pageNumber > 1:
                self.saveState()
                # Cabeçalho Superior
                self.setFont('Helvetica-Bold', 8)
                self.setFillColor(colors.HexColor('#1b4d3e'))
                self.drawString(45, 804, "TECNOLOGIA, DADOS E IA NA GESTÃO AMBIENTAL")
                self.setFont('Helvetica-Oblique', 8)
                self.setFillColor(colors.HexColor('#555555'))
                self.drawRightString(550, 804, "Apostila Didática Teórica e Prática para Leigos")
                
                # Linha divisória cabeçalho
                self.setStrokeColor(colors.HexColor('#bdc3c7'))
                self.setLineWidth(0.6)
                self.line(45, 798, 550, 798)

                # Linha divisória rodapé
                self.line(45, 45, 550, 45)
                
                # Rodapé Inferior
                self.setFont('Helvetica', 8)
                self.setFillColor(colors.HexColor('#7f8c8d'))
                self.drawString(45, 33, "Material Didático Aberto — Licença CC BY-NC-SA 4.0 & MIT")
                self.drawRightString(550, 33, f"Página {self._pageNumber} de {num_pages}")
                self.restoreState()
            super().showPage()
        super().save()

# ==============================================================================
# 2. DEFINIÇÃO DA PALETA DE CORES E ESTILOS TIPOGRÁFICOS
# ==============================================================================
def criar_estilos():
    base_styles = getSampleStyleSheet()
    
    styles = {
        'Normal': ParagraphStyle(
            'CustomNormal',
            parent=base_styles['Normal'],
            fontName='Helvetica',
            fontSize=9.5,
            leading=14.2,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=8,
            alignment=4 # Justificado
        ),
        'CoverTitle': ParagraphStyle(
            'CoverTitle',
            fontName='Helvetica-Bold',
            fontSize=26,
            leading=32,
            textColor=colors.HexColor('#145a32'),
            alignment=1, # Centralizado
            spaceAfter=12
        ),
        'CoverSubtitle': ParagraphStyle(
            'CoverSubtitle',
            fontName='Helvetica',
            fontSize=13,
            leading=18,
            textColor=colors.HexColor('#1f618d'),
            alignment=1,
            spaceAfter=25
        ),
        'CoverMeta': ParagraphStyle(
            'CoverMeta',
            fontName='Helvetica',
            fontSize=9,
            leading=14,
            textColor=colors.HexColor('#566573'),
            alignment=1
        ),
        'ModTitle': ParagraphStyle(
            'ModTitle',
            fontName='Helvetica-Bold',
            fontSize=17,
            leading=21,
            textColor=colors.HexColor('#145a32'),
            spaceBefore=14,
            spaceAfter=8,
            keepWithNext=True
        ),
        'SecTitle': ParagraphStyle(
            'SecTitle',
            fontName='Helvetica-Bold',
            fontSize=12.5,
            leading=16,
            textColor=colors.HexColor('#1b4f72'),
            spaceBefore=12,
            spaceAfter=6,
            keepWithNext=True
        ),
        'SubSecTitle': ParagraphStyle(
            'SubSecTitle',
            fontName='Helvetica-Bold',
            fontSize=10.5,
            leading=14,
            textColor=colors.HexColor('#2e4053'),
            spaceBefore=8,
            spaceAfter=4,
            keepWithNext=True
        ),
        'BoxText': ParagraphStyle(
            'BoxText',
            fontName='Helvetica',
            fontSize=8.8,
            leading=13.2,
            textColor=colors.HexColor('#212f3d'),
            spaceAfter=4
        ),
        'BoxTitle': ParagraphStyle(
            'BoxTitle',
            fontName='Helvetica-Bold',
            fontSize=9.8,
            leading=13.5,
            textColor=colors.HexColor('#145a32'),
            spaceAfter=4
        ),
        'CodeStyle': ParagraphStyle(
            'CodeStyle',
            fontName='Courier',
            fontSize=7.8,
            leading=10.5,
            textColor=colors.HexColor('#17202a')
        ),
        'CodeExplain': ParagraphStyle(
            'CodeExplain',
            fontName='Helvetica',
            fontSize=8.2,
            leading=11.8,
            textColor=colors.HexColor('#2c3e50')
        ),
        'TableHeader': ParagraphStyle(
            'TableHeader',
            fontName='Helvetica-Bold',
            fontSize=8.5,
            leading=11.5,
            textColor=colors.white,
            alignment=1
        ),
        'TableCell': ParagraphStyle(
            'TableCell',
            fontName='Helvetica',
            fontSize=8.0,
            leading=11.0,
            textColor=colors.HexColor('#2c3e50')
        ),
        'TableCellBold': ParagraphStyle(
            'TableCellBold',
            fontName='Helvetica-Bold',
            fontSize=8.0,
            leading=11.0,
            textColor=colors.HexColor('#1b4f72')
        ),
        'FigCaption': ParagraphStyle(
            'FigCaption',
            fontName='Helvetica-Oblique',
            fontSize=8.2,
            leading=11.5,
            textColor=colors.HexColor('#555555'),
            alignment=1,
            spaceBefore=4,
            spaceAfter=10
        ),
        'TOCItem': ParagraphStyle(
            'TOCItem',
            fontName='Helvetica',
            fontSize=9.2,
            leading=14,
            textColor=colors.HexColor('#1b4f72')
        )
    }
    return styles

# ==============================================================================
# 3. HELPERS DE CONSTRUÇÃO DE ELEMENTOS VISUAIS
# ==============================================================================
def criar_box(titulo, texto_paragrafos, tipo="didatico", styles=None):
    """Cria uma caixa destacada com cores temáticas."""
    temas = {
        "didatico": {"bg": "#eafaf1", "border": "#27ae60", "icon": "💡 DESMISTIFICANDO: "},
        "ambiental": {"bg": "#ebf5fb", "border": "#2980b9", "icon": "🌿 CONEXÃO AMBIENTAL: "},
        "alerta": {"bg": "#fef9e7", "border": "#f39c12", "icon": "⚠️ ATENÇÃO AO ERRO COMUM: "},
        "pratica": {"bg": "#f4ecf7", "border": "#8e44ad", "icon": "🎯 PASSO A PASSO PRÁTICO: "}
    }
    t = temas.get(tipo, temas["didatico"])
    
    conteudo = []
    conteudo.append(Paragraph(f"<b>{t['icon']}{titulo}</b>", ParagraphStyle(
        'BoxHeaderStyle',
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=colors.HexColor(t["border"]),
        spaceAfter=5
    )))
    
    for p in texto_paragrafos:
        if isinstance(p, str):
            conteudo.append(Paragraph(p, styles['BoxText']))
        else:
            conteudo.append(p)
            
    tabela_box = Table([[conteudo]], colWidths=[505])
    tabela_box.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor(t["bg"])),
        ('LINELEFT', (0,0), (-1,-1), 3.5, colors.HexColor(t["border"])),
        ('TOPPADDING', (0,0), (-1,-1), 7),
        ('BOTTOMPADDING', (0,0), (-1,-1), 7),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#d5dbdb')),
    ]))
    return tabela_box

def criar_tabela_codigo(linhas_codigo, styles):
    """
    linhas_codigo: lista de tuplas (codigo_str, explicacao_leigo_str)
    """
    dados = [
        [Paragraph("<b>Linha de Código (Python)</b>", styles['TableHeader']),
         Paragraph("<b>O que ela faz no computador? (Explicação para Leigos)</b>", styles['TableHeader'])]
    ]
    for cod, exp in linhas_codigo:
        p_cod = Paragraph(f"<code>{cod}</code>", styles['CodeStyle'])
        p_exp = Paragraph(exp, styles['CodeExplain'])
        dados.append([p_cod, p_exp])
        
    tabela = Table(dados, colWidths=[205, 300])
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (1,0), colors.HexColor('#1b4f72')),
        ('ALIGN', (0,0), (1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#d6dbdf')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#fcfcfc'), colors.HexColor('#f4f6f7')])
    ]))
    return tabela

def criar_tabela_geral(cabecalhos, linhas, larguras, styles):
    """Cria tabelas de dados ou comparativas com cabeçalho verde floresta."""
    dados = [[Paragraph(f"<b>{c}</b>", styles['TableHeader']) for c in cabecalhos]]
    for linha in linhas:
        linha_p = []
        for celula in linha:
            if isinstance(celula, str):
                linha_p.append(Paragraph(celula, styles['TableCell']))
            else:
                linha_p.append(celula)
        dados.append(linha_p)
        
    tabela = Table(dados, colWidths=larguras)
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#145a32')),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#d5dbdb')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f9fbf9')])
    ]))
    return tabela

print("Módulo de estilos e componentes estruturado com sucesso.")

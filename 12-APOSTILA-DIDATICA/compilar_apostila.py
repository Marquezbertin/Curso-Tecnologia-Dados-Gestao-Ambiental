"""
Script Principal de Compilação da Apostila Didática Completa:
'Tecnologia, Dados e Inteligência Artificial na Gestão Ambiental'

Compila todos os módulos, gráficos, tabelas e apêndices em um PDF editorial de alta qualidade.
"""

import os
import sys
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate
from estilos_apostila import criar_estilos, NumberedCanvas
from conteudo_parte1 import obter_capa_e_abertura, obter_modulo_1, obter_modulo_2, obter_modulo_3
from conteudo_parte2 import obter_modulo_4, obter_modulo_5, obter_modulo_6
from conteudo_parte3 import obter_modulo_7, obter_modulo_8, obter_modulo_9, obter_modulo_10
from conteudo_apendices import obter_apendices

def compilar():
    base_dir = r"C:\Users\Usuário\Desktop\Curso-Tecnologia-Dados-Gestao-Ambiental\12-APOSTILA-DIDATICA"
    img_dir = os.path.join(base_dir, "graficos")
    pdf_saida = os.path.join(base_dir, "Apostila-Tecnologia-Dados-Gestao-Ambiental.pdf")
    
    print("Iniciando compilação da Apostila Didática...")
    styles = criar_estilos()
    
    # Montando a história (fluxo de elementos)
    story = []
    
    # 1. Capa e Sumário
    print("-> Carregando Capa, Apresentação e Sumário...")
    story.extend(obter_capa_e_abertura(styles, img_dir))
    
    # 2. Módulos Iniciais (1 a 3)
    print("-> Carregando Módulos 1, 2 e 3...")
    story.extend(obter_modulo_1(styles))
    story.extend(obter_modulo_2(styles, img_dir))
    story.extend(obter_modulo_3(styles))
    
    # 3. Módulos Técnicos (4 a 6)
    print("-> Carregando Módulos 4, 5 e 6...")
    story.extend(obter_modulo_4(styles))
    story.extend(obter_modulo_5(styles, img_dir))
    story.extend(obter_modulo_6(styles, img_dir))
    
    # 4. Módulos Avançados e Práticos (7 a 10)
    print("-> Carregando Módulos 7, 8, 9 e 10...")
    story.extend(obter_modulo_7(styles))
    story.extend(obter_modulo_8(styles, img_dir))
    story.extend(obter_modulo_9(styles, img_dir))
    story.extend(obter_modulo_10(styles, img_dir))
    
    # 5. Apêndices (A, B e C)
    print("-> Carregando Apêndices A, B e C...")
    story.extend(obter_apendices(styles))
    
    # Configuração do Documento A4 com margens equilibradas
    doc = SimpleDocTemplate(
        pdf_saida,
        pagesize=A4,
        leftMargin=45,
        rightMargin=45,
        topMargin=50,
        bottomMargin=50
    )
    
    print("-> Renderizando documento PDF com ReportLab (NumberedCanvas)...")
    doc.build(story, canvasmaker=NumberedCanvas)
    
    tamanho_kb = os.path.getsize(pdf_saida) / 1024
    print(f"Sucesso! Apostila Didática gerada com sucesso:")
    print(f"Arquivo: {pdf_saida}")
    print(f"Tamanho: {tamanho_kb:.1f} KB")

if __name__ == "__main__":
    compilar()

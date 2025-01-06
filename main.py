
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import numpy as np

st.title('Gerador de gráfico padronizado para o programa ALHPA SIM')
st.divider()
custom_style = {
    'font.size': 12,  # Tamanho adequado para leitura de gráficos
    'axes.labelsize': 14,  # Tamanho dos rótulos dos eixos
    'axes.titlesize': 16,  # Tamanho do título do gráfico
    'axes.linewidth': 1.5,  # Espessura das bordas dos gráficos
    'xtick.labelsize': 12,  # Tamanho do texto dos ticks no eixo x
    'ytick.labelsize': 12,  # Tamanho do texto dos ticks no eixo y
    'lines.linewidth': 2,  # Espessura das linhas dos gráficos
    'lines.markersize': 6,  # Tamanho dos marcadores
    'legend.fontsize': 12,  # Tamanho da legenda
    'legend.frameon': False,  # Remove a moldura ao redor da legenda
    'legend.loc': 'best',  # Melhor posição automática para a legenda
    'figure.figsize': (8, 6),  # Tamanho padrão da figura (polegadas)
    'savefig.dpi': 600,  # Alta resolução para exportação (publicação)
    'savefig.bbox': 'tight',  # Salva a imagem sem cortar parte do gráfico
    }

uploaded_file = st.file_uploader("Escolha os arquivos CSV", type='csv',accept_multiple_files=True)

if uploaded_file is not None:
    dfs_list = []
    for uploaded_file in uploaded_file:
        df = pd.read_csv(uploaded_file,sep=';',decimal=',',skiprows=3,)
        colunas = df.columns.tolist()
        df.rename(columns={f'{colunas[0]}': 'x', f'{colunas[1]}': 'y'}, inplace=True)
        dfs_list.append(df)

    x_eixo = st.text_input(r'Título do eixo X')
    y_eixo = st.text_input(r'Título do eixo Y')
    title = st.text_input(r'Título do gráfico')

    plt.rcParams.update(custom_style)
    fig, ax = plt.subplots()


    for i in range(len(dfs_list)):
        a = -np.abs(dfs_list[i]['x'])
        ax.plot(dfs_list[i]['y'],a,label = f'A')


    ax.set_xlabel(x_eixo)
    ax.set_ylabel(y_eixo)
    ax.set_title(f'{title}')
    plt.grid(alpha=0.5)
    ax.margins(x=0.1, y=0.1)
    plt.legend()
    st.pyplot(fig)

    buffer = BytesIO()  # Cria um buffer de memória para armazenar o arquivo PDF temporariamente
    fig.savefig(buffer, format='pdf')  # Salva o gráfico no buffer em formato PDF
    buffer.seek(0)  # Retorna para o início do buffer para leitura

    st.divider()

    st.download_button(
        label="Baixar gráfico em PDF",
        data=buffer,
        file_name="grafico.pdf",
        mime="application/pdf"
        )
else:
    st.write("Nenhum arquivo foi selecionado")

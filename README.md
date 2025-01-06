**Gerar Gráfico a partir de Arquivos CSV**

Este repositório contém um código Python para criar gráficos a partir de arquivos CSV. Ele permite customizações de título, rótulos dos eixos, e exportação em formato PDF com estilo adequado para apresentações ou publicações.

**Funcionalidades**

Lê múltiplos arquivos CSV.
Plota dados com estilo personalizado.
Gera gráficos com título e rótulos configuráveis.
Exporta o gráfico em alta resolução no formato PDF.

**Requisitos**

Este código requer as seguintes bibliotecas:

- pandas;
- matplotlib;
- numpy.

**Uso**

O código principal está na função gerar_grafico, que aceita os seguintes parâmetros:

- caminhos_csv: Lista de caminhos para os arquivos CSV (separador ;, decimal ,);
- titulo: Título do gráfico;
- xlabel: Rótulo do eixo X (opcional, detectado automaticamente se não fornecido);
- ylabel: Rótulo do eixo Y (opcional, detectado automaticamente se não fornecido);
- salvar_pdf: Booleano indicando se o gráfico deve ser salvo como PDF.

**Exemplo**

arquivos = ["holdup.csv", "holdup_2.csv"]
gerar_grafico(arquivos, titulo="Holdup X Length", xlabel=None, ylabel=None, salvar_pdf=True)

**Entrada (Formato dos Arquivos CSV)**

Os arquivos CSV foram confiurados para exportar dados obitdos do padrão de saída do programa ALPHA SIM.

**Saída**

O gráfico é exibido na tela.

Se salvar_pdf=True, o gráfico será salvo como um arquivo grafico.pdf no diretório atual.

**Estilo do Gráfico**

O estilo dos gráficos foi otimizado para apresentações e publicações:

- Fonte e tamanhos adequados;
- Alta resolução para exportação;
- Bordas e linhas configuradas para clareza.

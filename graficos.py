def grafico_distancia(x, y, name):
    from matplotlib import pyplot as plt
    plt.rcParams['figure.figsize'] = [12, 8]
    plt.plot(x, y, color='blue',
             label='Média da distância caminhada ao longo das iterações', linewidth=3)
    # plt.title(f'Evolução ao longo das iterações\nPercentual de melhora: {improvement}%', size='x-large')
    plt.xlabel('Iterações', size='x-large')
    plt.ylabel('Média da distância caminhada (metros)', size='x-large')
    plt.legend(loc='best', fontsize='large')
    plt.xticks(size='large')
    plt.yticks(size='large')
    plt.savefig(name)
    plt.close()


def grafico_pontos(x, y, name):
    from matplotlib import pyplot as plt
    plt.rcParams['figure.figsize'] = [12, 8]
    plt.plot(x, y, color='blue',
             label='Número de Pontos de ônibus ao longo das iterações', linewidth=3)
    # plt.title(f'Evolução ao longo das iterações\nPercentual de melhora: {improvement}%', size='x-large')
    plt.xlabel('Iterações', size='x-large')
    plt.ylabel('Número de pontos de ônibus', size='x-large')
    plt.legend(loc='best', fontsize='large')
    plt.xticks(size='large')
    plt.yticks(size='large')
    plt.savefig(name)
    plt.close()
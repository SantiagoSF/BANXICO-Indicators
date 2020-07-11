from matplotlib import pyplot as plt

def plot_series(series):
    """ Funcion para graficar las series """
    # plt.close('all')

    print("plotting...............")
    rates = []
    dates = []
    for values in series:
        dates.append(values[1])
        rates.append(float(values[2]))

    plt.title('Series de tiempo - Banxico | ' + series[0][0])
    plt.plot(dates, rates, 'go--', label=series[0][0], linewidth=2, markersize=12)
    plt.xlabel('Tiempo - Meses')
    plt.ylabel('Cifras')
    plt.legend()
    plt.grid(True)
    plt.subplots_adjust(bottom=0.25,top=0.94)
    plt.show()
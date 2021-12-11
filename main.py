import matplotlib.pyplot as plt
import numpy as np
# from matplotlib import cm
# from matplotlib.ticker import LinearLocator
from Factors import Factors
from Factors_u_t import Factors_u_t


def case_fact(facts):
    ex = Factors(facts)
    ex.calc()
    ex.print()
    return ex


def create_sub_plot(y_label, x_label, ax, x, y):
    ax.plot(x, y)
    ax.set_title(str(y_label) + "= " + str(x_label))


if __name__ == '__main__':
    print('Program start...')
    fs1 = case_fact([0, 22, -1, 0.1, 0.1, 0, 80, 0.5, 0, 500, 1, 1, 1, 1, 0.5, 25])
    zahod102 = [1, 5, 12, 15, 17, 22]
    zahod105 = [35, 15, 7, 2, 0.5, 0]
    values1 = []
    values2 = []
    for i in zahod102:
        for j in zahod105:
            values1.append(i)
            values2.append(j)
    # fs1.change_value(105, 3)
    fs1.change_value(107, 81)
    # fs1.change_value(102, 18)
    fct1 = Factors_u_t(102, values1, fs1)
    fct2 = Factors_u_t(105, values2, fs1)
    # fct1.generate_u_t(fs1, 1)
    # fct2.generate_u_t(fs1, 35)
    for i in range(0, 36):
        fct1.generate_u_t(fs1, fct1.get_values()[i])
        fct2.generate_u_t(fs1, fct2.get_values()[i])
    # fct3 = Factors_u_t(107, range(75, 120), fs1)
    fct = [fct1, fct2]

    print('102value\t-\t105value\t-\t\tUT\t\t-\t\tCategory\t\t-\t\tY\t\t-\t\tP')
    for i in range(0, 36):
        print(f'{fct1.get_values()[i]}\t\t\t-' + "{:10.1f}".format(fct2.get_values()[i]) + '\t\t-'
              "{:10.3f}".format(fct2.get_u_ts()[i]) + '\t\t-\t\t\t' +
              f'{fct2.get_category()[i]}' + '\t\t\t- '
              "{:10.3f}".format(fct2.get_ys()[i]) + '\t-'
              "{:10.3f}".format(fct2.get_ps()[i]))
    fs1.print()
    plt.style.use('fivethirtyeight')

    fig, ax = plt.subplots(2)

    for i in range(len(fct)):
        # print(f 'code: {fct[i].get_code()}, values: {fct[i].get_values()}, '
        #       f'UTs: {fct[i].get_UTs()}')
        create_sub_plot('UT', fct[i].get_code(), ax[i], fct[i].get_values(), fct[i].get_u_ts())

    fig1, ax1 = plt.subplots(2)

    for i in range(len(fct)):
        # print(f 'code: {fct[i].get_code()}, values: {fct[i].get_values()}, '
        #       f'UTs: {fct[i].get_UTs()}')
        create_sub_plot('P', fct[i].get_code(), ax1[i], fct[i].get_values(), fct[i].get_ps())

    fig11, ax11 = plt.subplots(2)

    for i in range(len(fct)):
        # print(f 'code: {fct[i].get_code()}, values: {fct[i].get_values()}, '
        #       f'UTs: {fct[i].get_UTs()}')
        create_sub_plot('Category', fct[i].get_code(), ax11[i], fct[i].get_values(), fct[i].get_category())

    fig2 = plt.figure()

    x = fct[0].get_values()
    y = fct[1].get_values()
    z1 = fct[0].get_u_ts()
    z2 = fct[1].get_u_ts()
    ax2 = fig2.add_subplot(111, projection='3d')
    ax2.plot_trisurf(x, y, z2, color='white', edgecolors='grey', alpha=0.5)
    ax2.scatter(x, y, z2, c='red')

    plt.show()

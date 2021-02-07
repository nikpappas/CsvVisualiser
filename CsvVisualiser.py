import os
from math import sqrt, sin

import numpy as np
from matplotlib import pyplot as plt


def main():
    createData()
    variables = readData()
    analysis = analyse(variables)
    plotAnalysis(analysis)


def createData():
    for i in range(30):
        with open(f'data/{i}.csv', 'w') as f:
            f.write('"power"\n')
            for j in range(1000):
                x = j / 50
                val = 100 * sin(j + i) + (-x + 2 * x ** 2 + (i - 3) * x ** 3 - ((-i - 3) * x) ** 5 + i * x ** 6 + (
                    sqrt(i * 100 + 100)) + 1000) / 100000000000 + (sqrt(i * 100 + 100)) + 1000
                f.write(f'{val}\n')


def readData():
    variables = {}
    walkRes = os.walk("data")
    files = list(walkRes)[0][2]
    for fn in files:
        if fn.endswith(".csv"):
            with open(f'data/{fn}', 'r') as f:
                lines = f.readlines()
                variables[f'{lines[0].strip()}_{fn}'] = [float(l.strip()) for l in lines[1:]]
    return variables


def analyse(variables):
    analysis = {}
    for k, v in variables.items():
        analysis[k] = {}
        analysis[k]['mean'] = sum(v) / len(v)
        analysis[k]['max'] = max(v)
        analysis[k]['min'] = min(v)
        analysis[k]['p_99'] = np.percentile(v, 99)

    return analysis


def plotAnalysis(analysis):
    x = list(range(len(analysis)))
    mean = []
    p99 = []
    max = []
    min = []
    for k, v in analysis.items():
        mean.append(v['mean'])
        p99.append(v['p_99'])
        max.append(v['max'])
        min.append(v['min'])

    plt.plot(x, mean, label='mean')
    plt.plot(x, p99, label='p_99')

    plt.title("power")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Power (W)")
    plt.legend()
    plt.fill_between(x, max, min, color=(0.5, 0.6, 0.7, 0.3))

    plt.show()


if __name__ == '__main__':
    main()

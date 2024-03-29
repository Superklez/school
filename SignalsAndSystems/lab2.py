import numpy as np
import matplotlib.pyplot as plt

def getPlot(f:float=10, fs:float=100, minmax:list=[-20, 21],
        compare:bool=False):

    def func(t:float, f:float=10):
        return np.sin(2*np.pi*f*t)

    def samp(nT:float, f:float=10):
        return np.sin(2*np.pi*f*nT)

    if compare:
        t = np.linspace(minmax[0], minmax[1], 1000) / fs
        x = func(t, f)
    nT = np.arange(minmax[0], minmax[1]) / fs
    xc = samp(nT, f)

    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    ax.scatter(nT, xc, label='sampled sine wave', zorder=4)
    ax.plot(nT, xc, zorder=4)
    if compare:
        ax.plot(t, x, label='true sine wave', zorder=3)
        plt.legend(loc='lower left')
    ax.set_xlabel('$t=nT$')
    ax.set_ylabel('$x[n]=x_c(nT)$')
    ax.set_xlim([nT[0], nT[-1]])
    ax.axhline(y=0, color='k', zorder=2)
    ax.axvline(x=0, color='k', zorder=2)
    ax.grid(zorder=1)
    plt.tight_layout()
    plt.show()

sampling_rates = {'1':100, '2':150}
frequencies = {
    '1':{'a':10, 'b':90, 'c':20, 'd':80, 'e':36, 'f':64, 'g':49, 'h':51},
    '2':{'a':10, 'b':90, 'c':140, 'd':20, 'e':80, 'f':130, 'g':36, 'h':64,
        'i':114}
}

if __name__ == '__main__':
    print('Choose a number:')
    for i in sampling_rates:
        print(f'{i}. {sampling_rates[i]} Hz')

    number = input('Number: ').strip()
    while number not in sampling_rates.keys():
        print('-'*30)
        error = list(map(int, sampling_rates.keys()))
        print(f'ERROR: Number selected not in {error}')
        number = input('Number: ').strip()

    print('-'*30)
    print('Choose a letter:')
    for i in frequencies[number]:
        print(f'{i}. {frequencies[number][i]:3} Hz')
    letter = input('Letter: ').strip()
    while letter not in frequencies[number].keys():
        print('-'*30)
        error = list(frequencies[number].keys())
        print(f'ERROR: Letter selected not in {error}')
        letter = input('Letter: ').strip()

    print('-'*30)
    ans = input('Compare sine waves? (y/[n]): ')
    if ans in ['y']:
        compare = True
    elif ans in ['', 'n']:
        compare = False

    print('-'*30)
    print(f'Selected number: {number}')
    print(f'Selected letter: {letter}')

    getPlot(frequencies[number][letter], sampling_rates[number],
        compare=compare)

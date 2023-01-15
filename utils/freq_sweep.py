import numpy as np
from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt

# returns a linear frequency sweep
def freq_sweep_linear(sweep_time, min_freq, max_freq, sampling_rate):
    fs = sampling_rate
    T  = sweep_time
    x  = np.arange(0, int(T*fs)) / fs
    
    return chirp(x, f0=min_freq, f1=max_freq, t1=sweep_time, method='linear')

# returns a quadratic frequency sweep
def freq_sweep_quad(sweep_time, min_freq, max_freq, sampling_rate):
    fs = sampling_rate
    T  = sweep_time
    x  = np.arange(0, int(T*fs)) / fs
    
    return chirp(x, f0=min_freq, f1=max_freq, t1=sweep_time, method='quadratic')

# returns a logarithmic frequency sweep
def freq_sweep_log(sweep_time, min_freq, max_freq, sampling_rate):
    fs = sampling_rate
    T  = sweep_time
    x  = np.arange(0, int(T*fs)) / fs
    
    return chirp(x, f0=min_freq, f1=max_freq, t1=sweep_time, method='logarithmic')

# returns a hyperbolic frequency sweep
def freq_sweep_hyperbolic(sweep_time, min_freq, max_freq, sampling_rate):
    fs = sampling_rate
    T  = sweep_time
    x  = np.arange(0, int(T*fs)) / fs
    
    return chirp(x, f0=min_freq, f1=max_freq, t1=sweep_time, method='hyperbolic')

# plots all 4 types of implemented sweeps (for visualization purposes only)
def plot_all_sweeps(sweep_time, sampling_rate, min_freq, max_freq):
    # different types of frequency sweeps
    y_linear     = freq_sweep_linear    (sweep_time, min_freq, max_freq, sampling_rate)
    y_quad       = freq_sweep_quad      (sweep_time, min_freq, max_freq, sampling_rate)
    y_log        = freq_sweep_log       (sweep_time, min_freq, max_freq, sampling_rate)
    y_hyperbolic = freq_sweep_hyperbolic(sweep_time, min_freq, max_freq, sampling_rate)
    
    plot_spectrogram(y_linear, y_quad, y_log, y_hyperbolic, sampling_rate, min_freq, max_freq, sweep_time)
    plt.show()

# adapted from: https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.chirp.html
def plot_spectrogram(w1, w2, w3, w4, fs, min_freq, max_freq, sweep_time):
    ff1, tt1, Sxx1 = spectrogram(w1, fs=fs)
    ff2, tt2, Sxx2 = spectrogram(w2, fs=fs)
    ff3, tt3, Sxx3 = spectrogram(w3, fs=fs)
    ff4, tt4, Sxx4 = spectrogram(w4, fs=fs)
    
    fig, ax = plt.subplots(2, 2)
    
    ax[0, 0].pcolormesh(tt1, ff1, Sxx1, cmap='gray_r', shading='gouraud')
    ax[0, 1].pcolormesh(tt2, ff2, Sxx2, cmap='gray_r', shading='gouraud')
    ax[1, 0].pcolormesh(tt3, ff3, Sxx3, cmap='gray_r', shading='gouraud')
    ax[1, 1].pcolormesh(tt4, ff4, Sxx4, cmap='gray_r', shading='gouraud')
    
    for i in [0, 1]:
        for j in [0, 1]:
            ax[i, j].set_xlabel('t (sec)')
            ax[i, j].set_ylabel('Frequency (Hz)')
            ax[i, j].set_xlim(0, 3)
            ax[i, j].set_ylim(0, 20000)
            ax[i, j].grid(True)
    
    ax[0, 0].set_title("Linear Sweep")
    ax[0, 1].set_title("Quadratic Sweep")
    ax[1, 0].set_title("Logarithmic Sweep")
    ax[1, 1].set_title("Hyperbolic Sweep")
    
    fig.suptitle(f'Sweep Spectrograms, f(0s)={min_freq}Hz, f({sweep_time}s)={max_freq}Hz')

import utils.freq_sweep as freq_sweep

# FREQ SWEEP PARAMETERS
sweep_time    = 3      # frequency sweep lasts 3 seconds
min_freq      = 20     # 20Hz
max_freq      = 20000  # 20kHz
sampling_rate = 100000 # 10kHz

def main():
    freq_sweep.plot_all_sweeps(sweep_time, sampling_rate, min_freq, max_freq)

main()
import numpy as np
import matplotlib.pyplot as plt


def get_signal_variance(plaintexts, traces, t, plt_index):
    all_mean = []
    for key in range(256):
        indices = np.where(plaintexts[:, plt_index] == key)     # find the indices
        same_plaintext_traces = traces[indices, t]              # find the trace with the same plaintext
        if same_plaintext_traces.size > 0:
            trace_mean = np.mean(same_plaintext_traces)         # mean of all traces with same plaintext
        else:
            trace_mean = 0
        all_mean.append(trace_mean)

    all_mean = np.array(all_mean)
    non_zero_mean = all_mean[np.where(all_mean != 0)]   # exclude zeros
    signal_variance = np.var(non_zero_mean)             # variance all non-zero means
    return signal_variance


def get_noise_mean(plaintexts, traces, t, plt_index):   # almost similar to calculate the signal
    all_variance = []
    for key in range(256):
        indices = np.where(plaintexts[:, plt_index] == key)     # find the indices
        same_plaintext_traces = traces[indices, t]              # find the trace with the same plaintext
        if same_plaintext_traces.size > 0:
            trace_variance = np.var(same_plaintext_traces)      # variance first, different from signal
        else:
            trace_variance = 0
        all_variance.append(trace_variance)

    noise_mean = np.mean(all_variance)      # the last step is mean
    return noise_mean


if __name__ == '__main__':
    plaintexts = np.memmap("plaintext_10000x16_uint8.bin", dtype=np.uint8, mode="r", shape=(10000, 16))
    traces = np.memmap("traces_10000x50_int8.bin", dtype=np.int8, mode="r", shape=(10000, 50))

    for plt_index in range(16):     # 16 key byte
        signal = []
        noise = []
        snr = []
        print("Byte: ", plt_index)
        for t in range(50):     # get signal of 50 datapoint
            signal_variance = get_signal_variance(plaintexts, traces, t, plt_index)
            signal.append(signal_variance)
        print("Signal: ", signal)

        for t in range(50):     # get noise of 50 datapoint
            noise_mean = get_noise_mean(plaintexts, traces, t, plt_index)
            noise.append(noise_mean)
        print("Noise: ", noise)

        snr = np.divide(signal, noise)      # SNR = signal/noise
        print("SNR: ", snr)

        # Plot the result
        print("Plot")
        fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, figsize=(6, 10))
        x = np.arange(50)

        ax1.plot(x, signal, label='Signal Variance')
        ax1.legend()

        ax2.plot(x, noise, label='Noise Mean')
        ax2.legend()

        ax3.plot(x, snr, label='SNR')
        ax3.legend()

        plt.show()
        print("------------------------------------------------")


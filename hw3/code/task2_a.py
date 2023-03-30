import numpy as np
import matplotlib.pyplot as plt

plaintexts = np.load('textin_attack.npy')       # (20000, 16), uint8
traces = np.load('traces_attack_int16.npy')     # (20000, 24000), int16

def get_signal_variance(t, plt_index):
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


def get_noise_mean(t, plt_index):   # almost similar to calculate the signal
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
    for plt_index in range(16):     # 16 key byte
        signal = []
        noise = []
        snr = []
        print("Byte: ", plt_index)
        for t in range(24000):      # get signal of 24000 datapoints
            signal_variance = get_signal_variance(t, plt_index)
            signal.append(signal_variance)

        for t in range(24000):      # get noise of 24000 datapoint
            noise_mean = get_noise_mean(t, plt_index)
            noise.append(noise_mean)

        snr = np.divide(signal, noise)  # SNR = signal/noise

        # # detect the KeyAdd and KeySub
        # for t, snr_val in enumerate(snr):
        #     if snr_val > 1:
        #         print("Time:", t, " SNR:", snr_val)

        # Plot the result
        print("Plot")
        plt.figure()
        plt.plot(snr)
        plt.title("SNR Plot for Byte {}".format(plt_index))
        plt.xlabel("Time")
        plt.ylabel("SNR")
        plt.show()


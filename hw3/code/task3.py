import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # all input files we need
    # tvla_0: data set 1, random
    # keylist_0 = np.load('tvla_0keylist.npy')        # (10000, 16)
    textin_0 = np.load('tvla_0textin.npy')          # (10000, 16)
    # textout_0 = np.load('tvla_0textout.npy')      # (10000, 16)
    traces_0 = np.load('tvla_0traces_int16.npy')    # (10001, 24000) last row is useless
    traces_0 = np.delete(traces_0, -1, axis=0)      # (10000, 24000)

    # tvla_1: data set 2, fixed
    # keylist_1 = np.load('tvla_1keylist.npy')  # (10000, 16) same as tvla_0keylist
    textin_1 = np.load('tvla_1textin.npy')  # (10000, 16)
    # textout_1 = np.load('tvla_1textout.npy')  # (10000, 16)
    traces_1 = np.load('tvla_1traces_int16.npy')  # (10001, 24000) last row is useless
    traces_1 = np.delete(traces_1, -1, axis=0)  # (10000, 24000)

    # deal with group 0 first: tvla0
    fixed_data = np.array([218, 57, 163, 238, 94, 107, 75, 13, 50, 85, 191, 239, 149, 96, 24, 144])

    # # Divide the dataset into two subsets
    # fixed_data_mask = np.all(textin_0 == fixed_data, axis=1)    # mask the fixed data first
    # dataset_1_mask = np.invert(fixed_data_mask)                 # invert the mask, and get the mask of random data
    # dataset_2_mask = np.all(textin_1 == fixed_data, axis=1)
    #
    # dataset_1 = textin_0[dataset_1_mask]    # (4924, 16)
    # dataset_2 = textin_1[dataset_2_mask]    # (4924, 16)
    #
    # indices_1 = np.where(dataset_1_mask)
    # indices_2 = np.where(dataset_2_mask)

    # Na = len(dataset_1)     # size of data set 1: 4924
    # Nb = len(dataset_2)     # size of data set 2: 4924
    Na = len(traces_0)
    Nb = len(traces_1)

    # Traces
    trace_T = []
    for t in range(24000):
        # find the corresponding traces at the specific time
        dataset_1_traces = traces_0[:, t]
        dataset_2_traces = traces_1[:, t]

        # compute the average of all traces in each subset
        Xa = np.mean(dataset_1_traces)
        Xb = np.mean(dataset_2_traces)

        # compute the sample standard deviation of all traces in each subset
        Var_a = np.var(dataset_1_traces, ddof=1)
        Var_b = np.var(dataset_2_traces, ddof=1)

        # Welch's t-test
        std_err = np.sqrt((Var_a / Na) + (Var_b / Nb))
        t_value = (Xa - Xb) / std_err

        trace_T.append(t_value)

    trace_T = np.array(trace_T)  # convert the list to a NumPy array for convenience

    time_indices = np.where(trace_T > 4.5)[0]   # find the time values where t-value > 4.5
    print("Time values where t-value > 4.5:")
    print(time_indices)

    print("Plot:")
    plt.plot(trace_T)
    plt.axhline(y=4.5, color='r', linestyle='-')
    plt.show()

    # # Traces
    # trace_T = []
    # for t in range(24000):
    #     # find the corresponding traces at the specific time
    #     dataset_1_traces = traces_0[indices_1, t]
    #     dataset_2_traces = traces_1[indices_2, t]
    #
    #     # compute the average of all traces in each subset
    #     Xa = np.mean(dataset_1_traces)
    #     Xb = np.mean(dataset_2_traces)
    #
    #     # compute the sample standard deviation of all traces in each subset
    #     Var_a = np.var(dataset_1_traces, ddof=1)
    #     Var_b = np.var(dataset_2_traces, ddof=1)
    #
    #     # Welch's t-test
    #     std_err = np.sqrt((Var_a / Na) + (Var_b / Nb))
    #     t_value = (Xa - Xb) / std_err
    #
    #     trace_T.append(t_value)
    #
    # print("Plot:")
    # plt.plot(trace_T)
    # # plt.axhline(y=4.5, color='r', linestyle='-')
    # plt.show()

    # # Traces
    # group_0_trace_T = []
    # for t in range(24000):  # 24000
    #     # find the traces at the specific time and divide into two subsets
    #     group_0_traces_1 = traces_0[group_0_indices_1, t]
    #     group_0_traces_2 = traces_0[group_0_indices_2, t]
    #
    #     # compute the average of all traces in each subset
    #     group_0_Xa = np.mean(group_0_traces_1)
    #     group_0_Xb = np.mean(group_0_traces_2)
    #
    #     # compute the sample standard deviation of all traces in each subset
    #     group_0_var_a = np.var(group_0_traces_1, ddof=1)
    #     group_0_var_b = np.var(group_0_traces_2, ddof=1)
    #
    #     # Welch's t-test
    #     group_0_std_err = np.sqrt((group_0_var_a/group_0_Na) + (group_0_var_b/group_0_Nb))
    #     group_0_t_value = (group_0_Xa - group_0_Xb) / group_0_std_err
    #
    #     group_0_trace_T.append(group_0_t_value)
    #
    # # deal with group 1: tvla1
    #
    #
    # # deal with group 1: tvla1
    # group_1_fixed_data = np.array([218, 57, 163, 238, 94, 107, 75, 13, 50, 85, 191, 239, 149, 96, 24, 144])
    #
    # # Divide the dataset into two subsets
    # group_1_dataset_2_mask = np.all(textin_1 == group_1_fixed_data, axis=1)     # fixed: data set 2
    # group_1_dataset_1_mask = np.invert(group_1_dataset_2_mask)                  # random: data set 1
    #
    # group_1_dataset_1 = textin_1[group_1_dataset_1_mask]
    # group_1_dataset_2 = textin_1[group_1_dataset_2_mask]
    #
    # group_1_indices_1 = np.where(group_1_dataset_1_mask)  # indices of data set 1 (5076, )
    # group_1_indices_2 = np.where(group_1_dataset_2_mask)  # indices of data set 2 (4924, )
    #
    # # Welch's t-test
    # group_1_Na = len(group_1_dataset_1)  # size of subset A: 5076 #random data set 1
    # group_1_Nb = len(group_1_dataset_2)  # size of subset B: 4924 #fixed data set 2
    #
    # # Traces
    # group_1_trace_T = []
    # for t in range(24000):  # 24000
    #     # find the traces at the specific time and divide into two subsets
    #     group_1_traces_1 = traces_1[group_1_indices_1, t]
    #     group_1_traces_2 = traces_1[group_1_indices_2, t]
    #
    #     # compute the average of all traces in each subset
    #     group_1_Xa = np.mean(group_1_traces_1)
    #     group_1_Xb = np.mean(group_1_traces_2)
    #
    #     # compute the sample standard deviation of all traces in each subset
    #     group_1_var_a = np.var(group_1_traces_1, ddof=1)
    #     group_1_var_b = np.var(group_1_traces_2, ddof=1)
    #
    #     # Welch's t-test
    #     group_1_std_err = np.sqrt((group_1_var_a / group_1_Na) + (group_1_var_b / group_1_Nb))
    #     group_1_t_value = (group_1_Xa - group_1_Xb) / group_1_std_err
    #
    #     group_1_trace_T.append(group_1_t_value)
    #
    # print("Plot:")
    # plt.plot(group_1_trace_T)
    # plt.axhline(y=4.5, color='r', linestyle='-')
    # plt.show()


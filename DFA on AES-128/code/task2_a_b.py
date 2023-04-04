import numpy as np
row_type = np.dtype((np.uint8, (4, 4)))
all_ctext = np.fromfile("full_dfa_data/ctext.bin", dtype=row_type).transpose(0, 2, 1)
all_ptext = np.fromfile("full_dfa_data/ptext.bin", dtype=row_type).transpose(0, 2, 1)
all_ftext = np.fromfile("full_dfa_data/ftext.bin", dtype=row_type).transpose(0, 2, 1)


if __name__ == '__main__':
    # question2(a)
    print("-----Qustion2(a)-----")
    same_rows = np.equal(all_ctext, all_ftext)
    same_rows_mask = np.all(same_rows, axis=(1, 2))     # (1000, )

    true_indices = np.where(same_rows_mask)[0]
    false_indices = np.where(~same_rows_mask)[0]

    # Print the indices of True and False values
    print("# of same values: ", len(true_indices))          # number of same elements between all_ctext and all_ftext
    print("# of different values: ", len(false_indices))    # number of different elements ...
    print("\n")

    # question2(b)
    print("-----Qustion2(b)-----")
    # we need "8 pairs" to perform the full DFA attack
    diff_indices = false_indices[0:402]

    # print out the first 20 glitch pairs and find out 8 desired matrix.
    col_1 = []
    col_2 = []
    col_3 = []
    col_4 = []
    for i in range(402):
        n = diff_indices[i]
        # print("diff #", n)
        arr = all_ctext[n] ^ all_ftext[n]
        # print(arr)
        # collect the data pair for column 1
        if arr[0][0] != 0:
            col_1.append(n)
        if arr[0][1] != 0:
            col_2.append(n)
        if arr[0][2] != 0:
            col_3.append(n)
        if arr[0][3] != 0:
            col_4.append(n)
    print("Column1: ", col_1)
    print("Column2: ", col_2)
    print("Column3: ", col_3)
    print("Column4: ", col_4)

    print("\n")

    # list 8 different pairs
    print("First column with two pair diff:")
    print(all_ctext[18] ^ all_ftext[18])
    print(all_ctext[22] ^ all_ftext[22])

    print("Second column with two pair diff:")
    print(all_ctext[4] ^ all_ftext[4])
    print(all_ctext[5] ^ all_ftext[5])

    print("Third column with two pair diff:")
    print(all_ctext[24] ^ all_ftext[24])
    print(all_ctext[28] ^ all_ftext[28])

    print("Fourth column with two pair diff:")
    print(all_ctext[0] ^ all_ftext[0])
    print(all_ctext[8] ^ all_ftext[8])

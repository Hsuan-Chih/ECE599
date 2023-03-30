import numpy as np
import hashlib
import time as t
import multiprocessing as mp


start_time = t.time()

row_type = np.dtype((np.uint8, (4, 4)))
all_ctext = np.fromfile("full_dfa_data/ctext.bin", dtype=row_type).transpose(0, 2, 1)
all_ptext = np.fromfile("full_dfa_data/ptext.bin", dtype=row_type).transpose(0, 2, 1)
all_ftext = np.fromfile("full_dfa_data/ftext.bin", dtype=row_type).transpose(0, 2, 1)

# create the list of indices that help rearrange the array
indices = [0, 4, 8, 12, 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15]

#####################################
#            FIRST COLUMN           #
#####################################
flat_ctxt1 = all_ctext[18].flatten()
flat_ftxt1 = all_ftext[18].flatten()
simple_ctxt1 = [flat_ctxt1[i] for i in indices]
simple_ftxt1 = [flat_ftxt1[i] for i in indices]

flat_ctxt2 = all_ctext[22].flatten()
flat_ftxt2 = all_ftext[22].flatten()
simple_ctxt2 = [flat_ctxt2[i] for i in indices]
simple_ftxt2 = [flat_ftxt2[i] for i in indices]

# Load ctext/ftext pairs in the correct AES column order
simple_ctxt1 = np.reshape(simple_ctxt1, (4, 4), order='F').astype(np.uint8)
simple_ftxt1 = np.reshape(simple_ftxt1, (4, 4), order='F').astype(np.uint8)

simple_ctxt2 = np.reshape(simple_ctxt2, (4, 4), order='F').astype(np.uint8)
simple_ftxt2 = np.reshape(simple_ftxt2, (4, 4), order='F').astype(np.uint8)

# all variables we need in "preliminary filtering"
c0 = simple_ctxt1[np.unravel_index(0, shape=(4, 4), order='F')]
cp0 = simple_ftxt1[np.unravel_index(0, shape=(4, 4), order='F')]
c13 = simple_ctxt1[np.unravel_index(13, shape=(4, 4), order='F')]
cp13 = simple_ftxt1[np.unravel_index(13, shape=(4, 4), order='F')]
c10 = simple_ctxt1[np.unravel_index(10, shape=(4, 4), order='F')]
cp10 = simple_ftxt1[np.unravel_index(10, shape=(4, 4), order='F')]
c7 = simple_ctxt1[np.unravel_index(7, shape=(4, 4), order='F')]
cp7 = simple_ftxt1[np.unravel_index(7, shape=(4, 4), order='F')]

# all variables we need in "finding final candidate"
cs0 = simple_ctxt2[np.unravel_index(0, shape=(4, 4), order='F')]
cps0 = simple_ftxt2[np.unravel_index(0, shape=(4, 4), order='F')]
cs13 = simple_ctxt2[np.unravel_index(13, shape=(4, 4), order='F')]
cps13 = simple_ftxt2[np.unravel_index(13, shape=(4, 4), order='F')]
cs10 = simple_ctxt2[np.unravel_index(10, shape=(4, 4), order='F')]
cps10 = simple_ftxt2[np.unravel_index(10, shape=(4, 4), order='F')]
cs7 = simple_ctxt2[np.unravel_index(7, shape=(4, 4), order='F')]
cps7 = simple_ftxt2[np.unravel_index(7, shape=(4, 4), order='F')]


#####################################
#           SECOND COLUMN           #
#####################################
flat_ctxt1_col2 = all_ctext[9].flatten()
flat_ftxt1_col2 = all_ftext[9].flatten()
simple_ctxt1_col2 = [flat_ctxt1_col2[i] for i in indices]
simple_ftxt1_col2 = [flat_ftxt1_col2[i] for i in indices]

flat_ctxt2_col2 = all_ctext[23].flatten()
flat_ftxt2_col2 = all_ftext[23].flatten()
simple_ctxt2_col2 = [flat_ctxt2_col2[i] for i in indices]
simple_ftxt2_col2 = [flat_ftxt2_col2[i] for i in indices]

# Load ctext/ftext pairs in the correct AES column order
simple_ctxt1_col2 = np.reshape(simple_ctxt1_col2, (4, 4), order='F').astype(np.uint8)
simple_ftxt1_col2 = np.reshape(simple_ftxt1_col2, (4, 4), order='F').astype(np.uint8)

simple_ctxt2_col2 = np.reshape(simple_ctxt2_col2, (4, 4), order='F').astype(np.uint8)
simple_ftxt2_col2 = np.reshape(simple_ftxt2_col2, (4, 4), order='F').astype(np.uint8)

# all variables we need in "preliminary filtering"
c4 = simple_ctxt1_col2[np.unravel_index(4, shape=(4, 4), order='F')]
cp4 = simple_ftxt1_col2[np.unravel_index(4, shape=(4, 4), order='F')]
c1 = simple_ctxt1_col2[np.unravel_index(1, shape=(4, 4), order='F')]
cp1 = simple_ftxt1_col2[np.unravel_index(1, shape=(4, 4), order='F')]
c14 = simple_ctxt1_col2[np.unravel_index(14, shape=(4, 4), order='F')]
cp14 = simple_ftxt1_col2[np.unravel_index(14, shape=(4, 4), order='F')]
c11 = simple_ctxt1_col2[np.unravel_index(11, shape=(4, 4), order='F')]
cp11 = simple_ftxt1_col2[np.unravel_index(11, shape=(4, 4), order='F')]

# all variables we need in "finding final candidate"
cs4 = simple_ctxt2_col2[np.unravel_index(4, shape=(4, 4), order='F')]
cps4 = simple_ftxt2_col2[np.unravel_index(4, shape=(4, 4), order='F')]
cs1 = simple_ctxt2_col2[np.unravel_index(1, shape=(4, 4), order='F')]
cps1 = simple_ftxt2_col2[np.unravel_index(1, shape=(4, 4), order='F')]
cs14 = simple_ctxt2_col2[np.unravel_index(14, shape=(4, 4), order='F')]
cps14 = simple_ftxt2_col2[np.unravel_index(14, shape=(4, 4), order='F')]
cs11 = simple_ctxt2_col2[np.unravel_index(11, shape=(4, 4), order='F')]
cps11 = simple_ftxt2_col2[np.unravel_index(11, shape=(4, 4), order='F')]


#####################################
#           THIRD COLUMN            #
#####################################
flat_ctxt1_col3 = all_ctext[24].flatten()
flat_ftxt1_col3 = all_ftext[24].flatten()
simple_ctxt1_col3 = [flat_ctxt1_col3[i] for i in indices]
simple_ftxt1_col3 = [flat_ftxt1_col3[i] for i in indices]

flat_ctxt2_col3 = all_ctext[28].flatten()
flat_ftxt2_col3 = all_ftext[28].flatten()
simple_ctxt2_col3 = [flat_ctxt2_col3[i] for i in indices]
simple_ftxt2_col3 = [flat_ftxt2_col3[i] for i in indices]

# Load ctext/ftext pairs in the correct AES column order
simple_ctxt1_col3 = np.reshape(simple_ctxt1_col3, (4, 4), order='F').astype(np.uint8)
simple_ftxt1_col3 = np.reshape(simple_ftxt1_col3, (4, 4), order='F').astype(np.uint8)

simple_ctxt2_col3 = np.reshape(simple_ctxt2_col3, (4, 4), order='F').astype(np.uint8)
simple_ftxt2_col3 = np.reshape(simple_ftxt2_col3, (4, 4), order='F').astype(np.uint8)

# all variables we need in "preliminary filtering"
c8 = simple_ctxt1_col3[np.unravel_index(8, shape=(4, 4), order='F')]
cp8 = simple_ftxt1_col3[np.unravel_index(8, shape=(4, 4), order='F')]
c5 = simple_ctxt1_col3[np.unravel_index(5, shape=(4, 4), order='F')]
cp5 = simple_ftxt1_col3[np.unravel_index(5, shape=(4, 4), order='F')]
c2 = simple_ctxt1_col3[np.unravel_index(2, shape=(4, 4), order='F')]
cp2 = simple_ftxt1_col3[np.unravel_index(2, shape=(4, 4), order='F')]
c15 = simple_ctxt1_col3[np.unravel_index(15, shape=(4, 4), order='F')]
cp15 = simple_ftxt1_col3[np.unravel_index(15, shape=(4, 4), order='F')]

# all variables we need in "finding final candidate"
cs8 = simple_ctxt2_col3[np.unravel_index(8, shape=(4, 4), order='F')]
cps8 = simple_ftxt2_col3[np.unravel_index(8, shape=(4, 4), order='F')]
cs5 = simple_ctxt2_col3[np.unravel_index(5, shape=(4, 4), order='F')]
cps5 = simple_ftxt2_col3[np.unravel_index(5, shape=(4, 4), order='F')]
cs2 = simple_ctxt2_col3[np.unravel_index(2, shape=(4, 4), order='F')]
cps2 = simple_ftxt2_col3[np.unravel_index(2, shape=(4, 4), order='F')]
cs15 = simple_ctxt2_col3[np.unravel_index(15, shape=(4, 4), order='F')]
cps15 = simple_ftxt2_col3[np.unravel_index(15, shape=(4, 4), order='F')]


#####################################
#          FOURTH COLUMN            #
#####################################
flat_ctxt1_col4 = all_ctext[0].flatten()
flat_ftxt1_col4 = all_ftext[0].flatten()
simple_ctxt1_col4 = [flat_ctxt1_col4[i] for i in indices]
simple_ftxt1_col4 = [flat_ftxt1_col4[i] for i in indices]

flat_ctxt2_col4 = all_ctext[8].flatten()
flat_ftxt2_col4 = all_ftext[8].flatten()
simple_ctxt2_col4 = [flat_ctxt2_col4[i] for i in indices]
simple_ftxt2_col4 = [flat_ftxt2_col4[i] for i in indices]

# Load ctext/ftext pairs in the correct AES column order
simple_ctxt1_col4 = np.reshape(simple_ctxt1_col4, (4, 4), order='F').astype(np.uint8)
simple_ftxt1_col4 = np.reshape(simple_ftxt1_col4, (4, 4), order='F').astype(np.uint8)

simple_ctxt2_col4 = np.reshape(simple_ctxt2_col4, (4, 4), order='F').astype(np.uint8)
simple_ftxt2_col4 = np.reshape(simple_ftxt2_col4, (4, 4), order='F').astype(np.uint8)

# all variables we need in "preliminary filtering"
c12 = simple_ctxt1_col4[np.unravel_index(12, shape=(4, 4), order='F')]
cp12 = simple_ftxt1_col4[np.unravel_index(12, shape=(4, 4), order='F')]
c9 = simple_ctxt1_col4[np.unravel_index(9, shape=(4, 4), order='F')]
cp9 = simple_ftxt1_col4[np.unravel_index(9, shape=(4, 4), order='F')]
c6 = simple_ctxt1_col4[np.unravel_index(6, shape=(4, 4), order='F')]
cp6 = simple_ftxt1_col4[np.unravel_index(6, shape=(4, 4), order='F')]
c3 = simple_ctxt1_col4[np.unravel_index(3, shape=(4, 4), order='F')]
cp3 = simple_ftxt1_col4[np.unravel_index(3, shape=(4, 4), order='F')]

# all variables we need in "finding final candidate"
cs12 = simple_ctxt2_col4[np.unravel_index(12, shape=(4, 4), order='F')]
cps12 = simple_ftxt2_col4[np.unravel_index(12, shape=(4, 4), order='F')]
cs9 = simple_ctxt2_col4[np.unravel_index(9, shape=(4, 4), order='F')]
cps9 = simple_ftxt2_col4[np.unravel_index(9, shape=(4, 4), order='F')]
cs6 = simple_ctxt2_col4[np.unravel_index(6, shape=(4, 4), order='F')]
cps6 = simple_ftxt2_col4[np.unravel_index(6, shape=(4, 4), order='F')]
cs3 = simple_ctxt2_col4[np.unravel_index(3, shape=(4, 4), order='F')]
cps3 = simple_ftxt2_col4[np.unravel_index(3, shape=(4, 4), order='F')]


SBOX = np.array([
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
        0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
        0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
        0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
        0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
        0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
        0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
        0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
        0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
        0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
        0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
        0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
        0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
], dtype=np.uint8)

# Inverse of AES SBOX: give you the hex to indicate the corresponding row and column
ISBOX = SBOX.argsort()

# AES MixCols matrix
MIXCOLS = np.array([[2, 3, 1, 1],
                    [1, 2, 3, 1],
                    [1, 1, 2, 3],
                    [3, 1, 1, 2]])


# Galois multiplication by 2 (for MixCols)
def galois_mult_2(a):
    temp = (a << 1) & 0xff

    if (a & 0x80):
        temp ^= 0x1b

    return temp


# Galois multiplication by 3 (for MixCols)
def galois_mult_3(a):
    return galois_mult_2(a) ^ a

D = []
for row in range (4):
    mixcol = MIXCOLS[:, row]
    for x in range(1, 255+1):
        D_element = []
        for j in range(4):
            out = None
            if mixcol[j] == 1:
                out = x
            if mixcol[j] == 2:
                out = galois_mult_2(x)
            if mixcol[j] == 3:
                out = galois_mult_3(x)
            D_element.append(out)
        D.append(D_element)

# print("Length of lookup table:", len(D))    # Length of lookup table: 1020
# print(D[0][0])  # D[x=0, 0]   x: 0 ~ 254
d0 = np.array(D)[:, 0]  # (1020, )
d1 = np.array(D)[:, 1]  # (1020, )
d2 = np.array(D)[:, 2]  # (1020, )
d3 = np.array(D)[:, 3]  # (1020, )

# used for comparing the candidates to each group
D_f01 = np.dstack((d0, d1)).reshape(1020, 2)
D_f02 = np.dstack((d0, d1, d2)).reshape(1020, 3)
D_f03 = np.dstack((d0, d1, d2, d3)).reshape(1020, 4)


def check_keybytes(k_0: int, k_13: int, k_10: int, k_7: int):
    keybytes = bytes([k_0, k_13, k_10, k_7])
    hasher = hashlib.sha3_256()
    hasher.update(keybytes)
    key_hash = hasher.hexdigest()
    if key_hash == '4409976e63e88e6d0ef93405e6b6d678c2a498d22dcaa72b28c8c9cd6233ec7f':
        print("Congratulations! Correct 4 keybytes found")
        return True

    print("Not quite right")
    return False


def full_DFA(K0, Kp0, Ks0, Kps0, K1, Kp1, Ks1, Kps1, K2, Kp2, Ks2, Kps2, K3, Kp3, Ks3, Kps3):
    # first for-loop
    print("Executing Kc2 ...")
    Kc2 = []
    for k0 in range(256):
        for k13 in range(256):
            result_0 = np.bitwise_xor(ISBOX[np.bitwise_xor(k0, K0)], ISBOX[np.bitwise_xor(k0, Kp0)])
            result_13 = np.bitwise_xor(ISBOX[np.bitwise_xor(k13, K1)], ISBOX[np.bitwise_xor(k13, Kp1)])

            D_comp01 = np.array([result_0, result_13])
            if any(np.array_equal(D_comp01, x) for x in D_f01):
                Kc2.append((k0, k13))

    # print(len(Kc2))

    # second for-loop
    print("Executing Kc3 ...")
    Kc3 = []
    for k10 in range(256):
        for k0, k13 in Kc2:
            result_0 = np.bitwise_xor(ISBOX[np.bitwise_xor(k0, K0)], ISBOX[np.bitwise_xor(k0, Kp0)])
            result_13 = np.bitwise_xor(ISBOX[np.bitwise_xor(k13, K1)], ISBOX[np.bitwise_xor(k13, Kp1)])
            result_10 = np.bitwise_xor(ISBOX[np.bitwise_xor(k10, K2)], ISBOX[np.bitwise_xor(k10, Kp2)])

            D_comp02 = np.array([result_0, result_13, result_10])
            if any(np.array_equal(D_comp02, x) for x in D_f02):
                Kc3.append((k0, k13, k10))

    # print(len(Kc3))

    # third for-loop
    print("Executing Kc4 ...")
    Kc4 = []
    for k7 in range(256):
        for k0, k13, k10 in Kc3:
            result_0 = np.bitwise_xor(ISBOX[np.bitwise_xor(k0, K0)], ISBOX[np.bitwise_xor(k0, Kp0)])
            result_13 = np.bitwise_xor(ISBOX[np.bitwise_xor(k13, K1)], ISBOX[np.bitwise_xor(k13, Kp1)])
            result_10 = np.bitwise_xor(ISBOX[np.bitwise_xor(k10, K2)], ISBOX[np.bitwise_xor(k10, Kp2)])
            result_7 = np.bitwise_xor(ISBOX[np.bitwise_xor(k7, K3)], ISBOX[np.bitwise_xor(k7, Kp3)])

            D_comp03 = np.array([result_0, result_13, result_10, result_7])
            if any(np.array_equal(D_comp03, x) for x in D_f03):
                Kc4.append((k0, k13, k10, k7))

    # print(len(Kc4))

    # fourth for-loop: second pair
    print("Executing final_result ...")
    final_result = []
    for k0, k13, k10, k7 in Kc4:
        result_0 = np.bitwise_xor(ISBOX[np.bitwise_xor(k0, Ks0)], ISBOX[np.bitwise_xor(k0, Kps0)])
        result_13 = np.bitwise_xor(ISBOX[np.bitwise_xor(k13, Ks1)], ISBOX[np.bitwise_xor(k13, Kps1)])
        result_10 = np.bitwise_xor(ISBOX[np.bitwise_xor(k10, Ks2)], ISBOX[np.bitwise_xor(k10, Kps2)])
        result_7 = np.bitwise_xor(ISBOX[np.bitwise_xor(k7, Ks3)], ISBOX[np.bitwise_xor(k7, Kps3)])

        D_comp_final = np.array([result_0, result_13, result_10, result_7])
        if any(np.array_equal(D_comp_final, x) for x in D_f03):
            final_result.append((k0, k13, k10, k7))

    # print(final_result)
    # print("Length of final result: ", len(final_result))
    return final_result


def shift(mat):
    shifted = np.zeros_like(mat)
    for i in range(4):
        shifted[i] = mat[i, np.arange(i, 4+i) % 4]
    return shifted


if __name__ == '__main__':

    # Key = []
    # # first column: [(168, 138, 164, 45)]
    # Key.append(full_DFA(c0, cp0, cs0, cps0, c13, cp13, cs13, cps13, c10, cp10, cs10, cps10, c7, cp7, cs7, cps7))
    #
    # # second column: [(53, 73, 46, 0)]
    # Key.append(full_DFA(c4, cp4, cs4, cps4, c1, cp1, cs1, cps1, c14, cp14, cs14, cps14, c11, cp11, cs11, cps11))
    #
    # # third column: [(93, 213, 55, 198)
    # Key.append(full_DFA(c8, cp8, cs8, cps8, c5, cp5, cs5, cps5, c2, cp2, cs2, cps2, c15, cp15, cs15, cps15))
    # print(Key)
    #
    # # fourth column: [(170, 35, 50, 172)]
    # Key.append(full_DFA(c12, cp12, cs12, cps12, c9, cp9, cs9, cps9, c6, cp6, cs6, cps6, c3, cp3, cs3, cps3))
    # print(Key)

    # using multiprocessing
    args_list = [(c0, cp0, cs0, cps0, c13, cp13, cs13, cps13, c10, cp10, cs10, cps10, c7, cp7, cs7, cps7),
                 (c4, cp4, cs4, cps4, c1, cp1, cs1, cps1, c14, cp14, cs14, cps14, c11, cp11, cs11, cps11),
                 (c8, cp8, cs8, cps8, c5, cp5, cs5, cps5, c2, cp2, cs2, cps2, c15, cp15, cs15, cps15),
                 (c12, cp12, cs12, cps12, c9, cp9, cs9, cps9, c6, cp6, cs6, cps6, c3, cp3, cs3, cps3)]

    pool = mp.Pool(processes=4)
    results = pool.starmap(full_DFA, args_list)

    pool.close()
    pool.join()

    key_value = np.array(results).flatten()
    # print("Key: ", key_value)

    # shiftrow to get the right order
    round_10_key = np.reshape(key_value, (4, 4)).transpose(1, 0)    # reshape the 1D arr
    print("Before Shiftrow: ")
    print(round_10_key)

    ans = shift(round_10_key)
    print("After Shiftrow: ")
    print(ans)

    ans = ans.flatten(order='F')
    print("Round 10 Key: ", ans)

    # final result: [(168, 138, 164, 45)]
    check_keybytes(ans[0], ans[13], ans[10], ans[7])

end_time = t.time()
print("Time: ", end_time - start_time)




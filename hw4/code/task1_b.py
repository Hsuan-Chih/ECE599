import numpy as np

# //e:
# 01 00 01
# e = np.array([0, 1, 0, 0, 0, 1])

# all given hex numbers
hex_n = 'C2D2BE8E722AE5BBD23DFAD362A08B4D32A45115542E23E49B3546583338CD8B8BA42EF289B2E447E9BF6EAF7F24D02565D224ABDDD6D2F44A6F2816A4323196942DF20DED8F10024524E1B2F02F4AD0C1CBF7C778270BCD708EBFA049384EDEEF24C084DA3CA2EE146CA579CC42AEE7F6D4B0F59E5843A519329BEB5F976607'
hex_m = '1E8ADB08E98A58012C55A8C419747BD8D8DB40FAC240DA92BF4874F79E9AD73B20A934070CAA60C767254168ABEB37955618458F6BF94B2D7BA8921DE7E84FA67AF7E0D6FE9EDD554ABF4418F7AEE8D829E6EC1245CFCBAF589667963B531B89AF63879C9A653176A03BA689BC5DD45DA663910A19FA496A6AEFB3F9ADFFF696'
hex_sp = '2572EE15579D2E18724E98A137BC82CC46654E04E0AF227C36D7B0C29EF49D1B7757A367712EBC6C8DAD7E526678860CCD44AFFBE0C3791F4E0BA3E1863303E807CC4BD8A89542B22158D67D99DC93050ACA584D2D06950B6DC6157E47CFED4DC6D877E47A0C7F1A09FEA4115EBF67EFDAF4A8409689054366E58786E74D2ABD'
hex_e = '010001'

# return Z = m^d mod N
# def calculate_mod(m, N):
#     Z = 1
#     n = len(e)   # e = 010001, which is 6
#
#     for i in range(0, n):
#         Z = (Z ** 2) % N
#         if e[i] == 1:
#             Z = (Z * m) % N
#
#     return Z


if __name__ == '__main__':
    # convert hex numbers to decimal
    n = int(hex_n, 16)
    m = int(hex_m, 16)
    sp = int(hex_sp, 16)
    e = int(hex_e, 16)

    # Lenstra
    # calculate s'^e mod N
    # subtrahend = calculate_mod(sp, n)
    subtrahend = pow(sp, e, n)

    # calculate diff = m - subtrahend = m - (s'^e mod n)
    diff = np.subtract(m, subtrahend)

    # q = gcd(n, diff) = gcd(n, m - (s'^e mod n))
    q = np.gcd(n, diff)
    print("q:", q)
    print("[hex]:", hex(q))

    # p = n/q
    p = n // q
    print("p:", p)
    print("[hex]:", hex(p))
    print("------------verify it--------------")
    if q*p == n:
        print("congrats!")
    else:
        print("oops")






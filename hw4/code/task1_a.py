import numpy as np

# all hexadecimal numbers
hex_n = '9B1F16A7696AC90FA7AE615A1F71BD1AC0C31B37A9F14376BEC7FB701412F0E3B79CAB88F906B350B521578766C78CACD2E80632D0935F50CDDC415DC1B046EB3B3556624EB412D056F873E5A056C2B85B364D032BBAA9276757B058879B02CB2098D63C61551D4753B1AE1890D8FF79BA10F82307492A775A5715AD605B5601'
hex_s = '1448FA660D3DEE693A9AE10E3DBE176DD0AE9637F2896003367FAB3F71C1BE2C8A143DD9E4167C9A07801E666AC268F376EE6B9A27752322E1BBD16F8DDA2B90058A07B1AB564537C800953BD23771D8CFD08B96D34BA6013B10383B19D0F263E0EEBC7D09FDFEA003D73DDA885D25A3C2870CF8E5FFE7201AE75874F383097B'
hex_sp = '9ABD38BDD461B4F8F6A1824B1B43D41C18319071CA6028865576C32A258532BB08A449F29372F4BDB016B5A1F57AAA96BE66B17ECF0CD2BF89C7CAC77E5B1A43460688C3EDBF6DA6EBCEEA9B5797A4FC28EC93EF18DA6EE54A523861ABEDC82C4A148EC5C88DE1C51B6C813C8C13173E8526D0035E2A375CF7222A18C2860B1A'


if __name__ == '__main__':
    # convert hex numbers to decimal
    n = int(hex_n, 16)
    s = int(hex_s, 16)
    sp = int(hex_sp, 16)

    # Bellcore:
    # Compute the p by using GCD and numpy
    q = np.gcd((sp-s), n)
    print("q:", q)
    print("[hex]:", hex(q))

    # p = n/q
    p = n // q
    print("p:", p)
    print("[hex]:", hex(p))
    print("----------------verify it---------------------")
    if p*q == n:
        print("congrats")
    else:
        print("oops!")

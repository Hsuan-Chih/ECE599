import numpy as np
import aeskeyschedule
from Crypto.Cipher import AES

if __name__ == '__main__':
    # I get this result from the last (d) question, and just copy/paste
    round_10_key = [168, 73, 55, 172, 53, 213, 50, 45, 93, 35, 164, 0, 170, 138, 46, 198]
    # Key = np.reshape(Key, (4, 4), order='F')
    # print(Key[0:4])

    key_bytes = bytes(round_10_key)
    print("Round 10 key bytes: ", key_bytes)

    round_1_key = aeskeyschedule.reverse_key_schedule(key_bytes, 10)
    print("Round 1 key bytes: ", round_1_key)

    secret = bytes.fromhex("2a92fc6ad8006b658f49062c2843ad99")

    # Create an AES cipher object using the recovered key
    cipher = AES.new(round_1_key, AES.MODE_ECB)
    ans = cipher.decrypt(secret)
    print("ANS: ", ans)









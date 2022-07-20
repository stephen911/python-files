from hashlib import sha256
from time import time
max_nonce = 1000
def SHA56(text):
    return sha256(text.encode("ascii")).hexdigest()

sha256()

def mineBitcoin(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * prefix_zeros
    for nonce in range(max_nonce):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA56(text)
        if new_hash.startswith(prefix_str):
            print("Congratulations!!! you have successfully mined Bitcoin with nonce value: {}".format(nonce))
            return new_hash
    raise BaseException("Couldn't find correct hash after trying {} times".format(max_nonce))


if __name__ == "__main__":
    transactions = "stephen->dollar-> 50, kobby->danny-> 100, mark->francis->70"
    difficulty = 5
    start = time()
    print("Bitcoin mining started")
    new_hash = mineBitcoin(5, transactions, "00000xasjddianidhoshreoiahbkehag92hh982r3ty28y9241y9834b89y28", difficulty)
    total_time = str((time() - start))
    print("Mining took: {} seconds".format(total_time))
    print(new_hash)



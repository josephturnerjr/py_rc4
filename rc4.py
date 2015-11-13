class RC4Generator(object):
    def __init__(self, key):
        keylength = len(key)
        self.S = range(256)
        j = 0
        for i in range(256):
            j = (j + self.S[i] + key[i % keylength]) % 256 
            self.swap(i, j)

    def swap(self, i, j):
        self.S[i], self.S[j] = self.S[j], self.S[i]

    def keystream(self):
        i = j = 0
        while True:
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            self.swap(i, j)
            K = self.S[(self.S[i] + self.S[j]) % 256]
            yield K

    def encode(self, msg):
        return map(lambda (x, y): x ^ y, zip(msg, self.keystream()))

    def decode(self, msg):
        return self.encode(msg)

s_to_a = lambda s: [ord(x) for x in s]
a_to_s = lambda a: "".join([chr(x) for x in a])

msg = s_to_a(raw_input("What is your message? "))
key = s_to_a(raw_input("What is your key? "))
generator = RC4Generator(key)
encoded = generator.encode(msg)
decoder = RC4Generator(key)
decoded = decoder.decode(encoded)
for m in [msg, key, encoded, decoded]:
    print a_to_s(m)

src = input()
enc = input()
to_enc = input()
to_dec = input()
D = {}
E = {}
i = 0
while i < len(src):
    E[src[i]] = enc[i]
    D[enc[i]] = src[i]
    i += 1

do_enc = ''
do_dec = ''

for j in to_enc:
    do_enc += E[j]
print(do_enc)

for k in to_dec:
    do_dec += D[k]
print(do_dec)

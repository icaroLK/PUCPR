# media final: RA1 * 0,52 + 

# S1 * 0.25 + S2 * 0.6 + (S3 * 0.15 / 0.203496) + 

# {S1 * 0.25 + S2 * 0.6 + (S3 * 0.15 / 0.203496) + ((F1 / 1) * 0.017) + ((F2 / 1) * 0.017) + ((F3 / 0.06) * 0.017) + ((F4 / 0.03) * 0.017) + ((F5 / 1) * 0.013) + ((F6 / 1) * 0.013)}


S1 = 10
S2 = 7.5
S3 = 2.03

F1 = 0.99
F2 = 1
F3 = 0.64
F4 = 0.3
F5 = 1
F6 = 1





RA1 = S1 * 0.25 + S2 * 0.6 + (S3 * 0.15 / 0.203496) + ((F1 / 1) * 0.017) + ((F2 / 1) * 0.017) + ((F3 / 0.06) * 0.017) + ((F4 / 0.03) * 0.017) + ((F5 / 1) * 0.013) + ((F6 / 1) * 0.013)

print(RA1)

# RA1 = 8.9

RA2 = 2.03 / 0.203496

print(RA2)

# RA2 = 9.9
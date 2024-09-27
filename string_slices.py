# Slices

alpha = "SillyWalks"

print(alpha[1:3])  # expected output: 'il'
print(alpha[3:])  # expected output: 'lyWalks'
print(alpha[:3])  # expected output: 'Sil'
print(alpha[3:-2])  # expected output: 'lyWal'
print(alpha[
      -3:4])  # expected output: '' # we're incrementing here, so the first number had to be lower to produce any slice!
print(alpha[::2])  # expected output: 'Slyak'
print(alpha[1::2])  # expected output: 'ilWls'

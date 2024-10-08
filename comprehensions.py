even = [{f'{x}': True} if x % 2 == 0 else {f'{x}': False} for x in range(100)]
uneven = [x if x % 2 == 1 else 0 for x in range(100)]

print("Even", even)
print("Uneven", uneven)

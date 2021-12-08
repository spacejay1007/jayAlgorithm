
A = input()
B = input()
C = input()

res = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5,
       'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}

print(((res[A]*10)+(res[B]*1)) * (10**res[C]))

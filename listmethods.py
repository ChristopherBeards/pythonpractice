a = [1, 2, 3]
b = [4, 5, 6]

print(a + b)

s = 'a b c d e f'
z = s.split() # Adds every element to a list separated at a space
print(z)

if 'a' in z:
  print('A is in Z')
else:
  print('A is NOT in Z')

if 'g' not in z:
  print('G IS NOT in z')
else:
  print('G IS in z')

for i in z:
  print(i)

q = [4, 5, 3, 2, 7]
q.sort()
print(q)
q.reverse()
print(q)

u = [3, 5, 7, 1, 2]
u.reverse()
print(u)

print('How many 3s?', u.count(3))
print('Index of 7', u.index(7))
print('Length of List', len(u))
print('Min Element', min(u))
print('Max element', max(u))
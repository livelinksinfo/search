s = set()
s.add(2)
s.add(3)
s.add(1)
s.add(5)

t=set()
t.add(4)
t.add(2)
t.add(6)
t.add(3)

s.union(t)
print(f"there are {len(s)} elements in s")
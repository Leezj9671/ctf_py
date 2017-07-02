start = 'a'
s = 'xrlvf23xfqwsxsqf'
ds = ''
n = 13

for _ in s:
    ds += chr((ord(_) - ord(start) + n) % 26 + ord(start))

for _ in ds:
    s += chr((ord(_) - ord('a') - 13) % 26 + ord('a'))

print(ds)
print(s)
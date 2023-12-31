from pathlib import Path

p1 = Path('/config/workspace/files_creation/abc.txt')

print(type(p1))

with open(p1,'r') as file:
    print(file.read())

p2 = Path('/config/workspace/files_creation/ghi.txt')

if not p2.exists():
    with open(p2,'w') as file:
        file.write("Content 3")

print(p1.name)
print(p1.stem)
print(p1.suffix)

p3 = Path('/config/workspace/files_creation')
print(p3.iterdir())
for p in p3.iterdir():
    print(p)
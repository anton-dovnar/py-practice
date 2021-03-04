chunk_size = 16
content = ''

with open('poem.txt') as poem:
    for chunk in iter(lambda: poem.read(chunk_size), ''):
        content += chunk

print(content)

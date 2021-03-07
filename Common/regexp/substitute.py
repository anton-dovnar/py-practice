import re


# Basic substitute
print(re.sub(r'[a-z]', ' ', '1a2b3c'))

# Substitute with group reference
print(re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', '2016-01-01'))

# Lookup around
print(re.sub(r'(?=\d{3})', '%', '12345'))
print(re.sub(r'(?!\d{3})', '%', '12345'))
print(re.sub(r'(?<=\d{3})', '$', '12345'))
print(re.sub(r'(?<!\d{3})', '$', '12345'))


# Camel case to underscores
def convert(content: str) -> str:
    res = re.sub(r'(.)([A-Z][a-z]+)', r'\1_\2', content)
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', res).lower()


if __name__ == '__main__':
    assert convert('CamelCase') == 'camel_case'
    print(convert('CamelCase'))

    assert convert('CamelCamelCase') == 'camel_camel_case'
    print(convert('CamelCamelCase'))

    assert convert('SimpleHTTPServer') == 'simple_http_server'
    print(convert('SimpleHTTPServer'))

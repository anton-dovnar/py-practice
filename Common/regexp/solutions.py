import re
import random


def is_valid(pattern: str, content: str) -> bool:
    match = pattern.match(content)
    return True if match else False


if __name__ == '__main__':
    # Hex match
    hex_pattern = re.compile(r'^#?([a-f0-9]{6}|[a-f0-9]{3})$')
    assert is_valid(hex_pattern, '#ffffff') is True

    email_pattern = re.compile(r'^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$')
    assert is_valid(email_pattern, 'hello.world@example.com') is True

    # 1st group - http / https, 2nd group - domain, 3rd group - domain, 4th group - api or file
    url_pattern = re.compile(r'''^(https?:\/\/)?
                            ([\da-z\.-]+)\.
                            ([a-z\.]{2,6})
                            ([\/\w \.-]*)\/?$''', re.X)
    assert is_valid(url_pattern, 'www.google.com') is True
    assert is_valid(url_pattern, 'http://www.example/file.html') is True

    # (?:...) - don’t capture group
    # 25[0-5] - match 251-255 pattern
    # [1]?[0-9][0-9] - Match 0-199 pattern
    ip_pattern = re.compile(r'''^(?:(?:25[0-5]
                            |2[0-4][0-9]
                            |[1]?[0-9][0-9]?)\.){3}
                            (?:25[0-5]
                            |2[0-4][0-9]
                            |[1]?[0-9][0-9]?)$''', re.X)
    assert is_valid(ip_pattern, '192.168.1.1') is True
    assert is_valid(ip_pattern, '256.0.0.0') is False

    mac = [random.randint(0x00, 0x7f) for _ in range(6)]
    mac = ':'.join(map(lambda m: f"{m:02x}", mac))
    print(mac)
    mac_pattern = re.compile(r'''[0-9a-f]{2}([:])
                            [0-9a-f]{2}
                            (\1[0-9a-f]{2}){4}$''', re.X)
    assert is_valid(mac_pattern, mac) is True

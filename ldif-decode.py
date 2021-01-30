#!/usr/bin/env python3

import base64
import re
import sys


def decode_b64(b64_string: str) -> str:
    """Decode base64 string into utf8 string."""
    if len(b64_string) == 0:
        return ""

    try:
        utf_string = base64.b64decode(b64_string.encode('ascii')).decode('utf8')
    except UnicodeDecodeError as e:
        # Probably some none utf8 character in decoding result
        print(e, file=sys.stderr)
    except base64.binascii.Error as e:
        # Probably some none ascii character in base64 string
        print(e, file=sys.stderr)
    else:
        return utf_string
    
    return b64_string


def main(file_handle: object) -> None:
    b64_string: str = ""
    label: str = ""

    for line in file_handle.readlines():
        # First line of a base64 value
        if re.match(r'^\w+::\s', line):
            utf_string = decode_b64(b64_string)
            if len(utf_string) > 0:
                print(label, utf_string)
            label, b64_string = line.strip().split()
            continue
        
        # Continuation line of a base64 value
        if re.match(r'^ ', line):
            if len(b64_string) > 0:
                b64_string += line.strip()
                continue

        # Decode once we have a complete base64 value
        if len(b64_string) > 0:
            utf_string = decode_b64(b64_string)
            print(label, utf_string)
            b64_string = ""

        # Print all other lines
        print(line, end="")


if __name__ == '__main__':
    try:
        # Try to read from first program parameter
        file_handle = open(sys.argv[1])
    except:
        # ... and if it fails, read from stdin
        file_handle = sys.stdin

    main(file_handle)

    file_handle.close()


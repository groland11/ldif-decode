#!/usr/bin/env python3

import base64
import re
import sys


def decode_b64(b64_string: str) -> str:
    if len(b64_string) == 0:
        return ""

    try:
        asc_string = base64.b64decode(b64_string.encode('ascii')).decode('utf8')
    except UnicodeDecodeError as e:
        # Probably some none utf8 character in decoding result
        print(e, file=sys.stderr)
    except base64.binascii.Error as e:
        # Probably some none ascii character in base64 string
        print(e, file=sys.stderr)
    else:
        return asc_string
    
    return b64_string


def main():
    b64_string: str = ""
    label: str = ""

    try:
        # Try to read from first program parameter
        f = open(sys.argv[1])
    except:
        # ... and if it fails, read from stdin
        f = sys.stdin

    for line in f.readlines():
        # First line of a base64 value
        if re.match(r'^\w+::\s', line):
            asc_string = decode_b64(b64_string)
            if len(asc_string) > 0:
                print(label, asc_string)
            label, b64_string = line.strip().split()
            continue
        
        # Continuation line of a base64 value
        if re.match(r'^ ', line):
            if len(b64_string) > 0:
                b64_string += line.strip()
                continue

        # Decode once we have a complete base64 value
        if len(b64_string) > 0:
            asc_string = decode_b64(b64_string)
            print(label, asc_string)
            b64_string = ""

        # Print all other lines
        print(line, end="")

    f.close()


if __name__ == '__main__':
    main()


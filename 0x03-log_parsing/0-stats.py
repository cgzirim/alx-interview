#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""
import sys
import ipaddress
from typing import List
from typing import Union


if __name__ == "__main__":

    def validate_line(line: str) -> Union[List[int], bool]:
        """Checks that a line aligns with a format.
        
        format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"\
                <status code> <file size>

        Returns [status_code, file_size] if the line alines with the format.
        Otherwise, returns False.
        """
        try:
            # Split line into variables
            ip = line[: line.index("-")].strip()
            date = line[line.index("[") + 1 : line.index("]")]

            sub_str_start = line.index('"')
            tmp_str = line[sub_str_start + 1 :]
            sub_str_end = tmp_str.index('"') + len(line[: sub_str_start + 2])

            ints = line[sub_str_end:].strip()
            status_code = ints.split(" ")[0]
            file_size = ints.split(" ")[1]

            # Validate line
            if type(ipaddress.ip_address(str(ip))) != ipaddress.IPv4Address:
                return False
            if "GET /projects/260 HTTP/1.1" not in line[sub_str_start:sub_str_end]:
                return False
            if type(eval(status_code)) != int:
                return False
            if type(eval(file_size)) != int:
                print(file_size)
                return False

            return [int(status_code), int(file_size)]
        except (ValueError, IndexError):
            return False

    file_size, count = 0, 0
    status_code = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in sys.stdin:
            count += 1
            result = validate_line(line)
            if result == False:
                continue

            status_code[result[0]] += 1
            file_size += result[1]

            if (count % 10) == 0:
                print(f"File size: {file_size}")
                for k, v in status_code.items():
                    if v != 0:
                        print(f"{k}: {v}")
    except KeyboardInterrupt:
        print(f"File size: {file_size}")
        for k, v in status_code.items():
            if v != 0:
                print(f"{k}: {v}")


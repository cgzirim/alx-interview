#!/usr/bin/python3
"""Reads stdin line by line and computes metrics."""
import sys


if __name__ == "__main__":

    file_size, count = 0, 0
    status_code = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    try:
        for line in sys.stdin:
            count += 1
            data = line.split(" ")
            try:
                file_size += int(data[-1])
                if data[-2] in status_code.keys():
                    status_code[data[-2]] += 1
            except (IndexError, ValueError):
                continue

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

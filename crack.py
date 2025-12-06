#!/usr/bin/env python3
import argparse, math, string, json, sys

POOLS = [
    string.ascii_lowercase,          # 26
    string.ascii_uppercase,          # 26
    string.digits,                   # 10
    string.punctuation               # 32
]
SPEED = 10_000_000_000               # 10 GH/s

def entropy_bits(pw: str) -> float:
    if not pw:
        return 0.0
    pools_used = sum(1 for p in POOLS if any(c in p for c in pw))
    charset = pools_used * 26 + pools_used * 26 + pools_used * 10 + pools_used * 32
    # simpler: charset = sum(len(p) for p in POOLS[:pools_used])
    return len(pw) * math.log2(sum(len(p) for p in POOLS[:pools_used]))

def crack_time(e: float) -> str:
    secs = (2 ** (e - 1)) / SPEED
    for unit in ['s','min','hr','day','yr','cent']:
        if secs < 60: break
        secs /= 60 if unit != 'yr' else (365.25*24*60*60)
        unit = 'centuries' if unit == 'cent' else unit
    return f"{secs:.1f} {unit}"

def main():
    parser = argparse.ArgumentParser(description="Password-Cracking Time Estimator")
    parser.add_argument('-p', '--password', required=True, help='password to test')
    args = parser.parse_args()

    e = entropy_bits(args.password)
    print(f"{e:.2f} bits  ->  {crack_time(e)} (at 10 GH/s)")

if __name__ == '__main__':
    main()
"""Small exact examples accompanying the general written telescoping proofs.

No third-party libraries, historical input files, or large prime search.
Finite checks illustrate the proof; they are not a proof for every index.
"""
from bisect import bisect_left, bisect_right
from math import isqrt
import json


def primes_through(limit):
    flags = bytearray(b"\x01") * (limit + 1)
    flags[:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if flags[p]:
            start = p * p
            flags[start::p] = b"\x00" * ((limit - start) // p + 1)
    return [n for n, prime in enumerate(flags) if prime]


def run():
    if not __debug__:
        raise RuntimeError("Run without -O: verification assertions must be enabled.")
    primes = primes_through(100_000)
    assert primes[:6] == [2, 3, 5, 7, 11, 13]

    def survivor(k, n):
        assert k >= 0 and n >= 1
        for _ in range(k):
            assert n <= len(primes), "Finite demonstration exceeded its stated sieve."
            n = primes[n - 1]
        return n

    def gap(k, n):
        return survivor(k, n + 1) - survivor(k, n)

    block_checks = 0
    wrong_formula_rejected = False
    for k in range(1, 4):
        for n in range(1, 9):
            block = range(primes[n - 1], primes[n])
            assert gap(k + 1, n) == sum(gap(k, j) for j in block)
            incomplete = sum(gap(k, j) - 1 for j in block)
            assert gap(k + 1, n) - 1 == gap(1, n) - 1 + incomplete
            wrong_formula_rejected |= gap(k + 1, n) - 1 != incomplete
            block_checks += 1
    assert wrong_formula_rejected

    levels = {0: list(range(1, 100_001)), 1: primes}
    for k in range(2, 5):
        levels[k] = [primes[n - 1] for n in levels[k - 1] if n <= len(primes)]

    count_checks = 0
    for k in range(2, 6):
        for n in range(1, 9):
            left, right = survivor(k, n), survivor(k, n + 1)
            for j in range(k):
                actual = bisect_left(levels[j], right) - bisect_right(levels[j], left)
                assert actual == gap(k - j, n) - 1
                count_checks += 1
    left, right = survivor(5, 1), survivor(5, 2)
    example = [bisect_left(levels[j], right) - bisect_right(levels[j], left)
               for j in range(5)]
    assert (left, right, example) == (31, 127, [95, 19, 5, 1, 0])

    # A nonprime base sequence obeys the same reindexing/telescoping mechanism.
    affine = lambda n: 2 * n + 1
    for n in range(1, 9):
        assert affine(primes[n]) - affine(primes[n - 1]) == sum(
            affine(j + 1) - affine(j) for j in range(primes[n - 1], primes[n]))

    return {"sieve_limit": 100_000, "block_identity_examples": block_checks,
            "interior_count_examples": count_checks, "interval": [left, right],
            "interior_counts": example, "missing_correction_rejected": True,
            "affine_control_examples": 8,
            "scope": "Exact finite demonstrations; general proof is written separately."}


if __name__ == "__main__":
    print(json.dumps(run(), indent=2))

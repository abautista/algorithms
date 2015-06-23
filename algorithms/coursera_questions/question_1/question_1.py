#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def count_inversions_brute_force(input):
    inversions = 0
    for i in range(0, len(input)):
        for j in range(i+1, len(input)):
            if input[i] > input[j]:
                inversions += 1

    return inversions


def merge_and_count_split_inversions(input, p, q, r):
    i = p
    j = q + 1
    tmp = []
    split_inversions = 0

    for k in range(p, r+1):
        if j > r or (input[i] <= input[j] and i <= q):
            tmp.append(input[i])
            i += 1
        else:
            tmp.append(input[j])
            split_inversions = split_inversions + 1 + q - i
            j += 1

    for k in range(0, len(tmp)):
        input[p+k] = tmp[k]

    return split_inversions


def count_inversions_aux(input, p, r):
    if r == p:
        return 0

    q = (p + r) / 2

    left_inversions = count_inversions_aux(input, p, q)
    right_inversions = count_inversions_aux(input, q+1, r)
    split_inversions = merge_and_count_split_inversions(input, p, q, r)
    return left_inversions + right_inversions + split_inversions


def count_inversions(input):
    inversions = count_inversions_aux(input, 0, len(input)-1)
    return inversions


if __name__ == '__main__':
    input = []
    with open(sys.argv[1], "r") as f:
        for line in f:
            input.append(int(line))
    print count_inversions(input)
#    print count_inversions_brute_force(input)

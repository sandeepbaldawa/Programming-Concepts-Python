#!/usr/bin/python
# -*- coding: utf-8 -*-


def read_input():
    return (input().rstrip(), input().rstrip())


    # return ("abc", "abdeabc")

def print_occurrences(output):
    print ' '.join(map(str, output))


prime = 1


def get_occurrences(pattern, text):
    m = len(pattern)
    n = len(text)


def read_input():
    return (input().rstrip(), input().rstrip())


    # return ("abc", "abdeabc")

def print_occurrences(output):
    print ' '.join(map(str, output))


prime = 1


def get_occurrences(pattern, text):
    m = len(pattern)
    n = len(text)
    res = []
    pattern_hash = create_hash(pattern, m)
    text_hash = create_hash(text[:m], m)

    # print(pattern_hash, text_hash)

    for i in range(n - m + 1):

        # print(pattern_hash, text_hash)

        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                res.append(i)
        if i < n - m:
            text_hash = recalculate_hash(text, i, i + m, text_hash, m)
    return res


def create_hash(input, end):
    hash = 0
    for i in range(end):
        hash = hash + ord(input[i]) * pow(prime, i)
    return hash


def recalculate_hash(
    input,
    old_index,
    new_index,
    old_hash,
    pattern_len,
    ):
    new_hash = old_hash - ord(input[old_index])
    new_hash = new_hash // prime
    new_hash += ord(input[new_index]) * pow(prime, pattern_len - 1)
    return new_hash


def hash_value(s, base):
    """Calculate the hash value of a string using base.
    Example: 'abc' = 97 x base^2 + 98 x base^1 + 99 x base^0
    @param s string to compute hash value for
    @param base base to use to compute hash value
    @return hash value
    """

    v = 0
    p = len(s) - 1
    for i in range(p + 1):
        v += ord(s[i]) * base ** p
        p -= 1

    return v


__name__ = '__main__'
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

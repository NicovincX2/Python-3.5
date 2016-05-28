# -*- coding: utf-8 -*-

import os


def ack3(M, N):
    return (N + 1) if M == 0 else (
           (N + 2) if M == 1 else (
               (2 * N + 3) if M == 2 else (
                   (8 * (2**N - 1) + 5) if M == 3 else (
                       ack3(M - 1, 1) if N == 0 else ack3(M - 1, ack3(M, N - 1))))))

os.system("pause")

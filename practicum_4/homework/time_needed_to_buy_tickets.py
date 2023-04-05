from typing import Any

import yaml
import numpy as np


def time_taken(tickets: list[int], k: int) -> int:
    seconds_elapsed = 0
    n = len(tickets)
    bought_tickets = [0] * n
    i = 0
    while sum(bought_tickets) < n:
        if bought_tickets[i] < tickets[i]:
            bought_tickets[i] += 1
            seconds_elapsed += i - k if i >= k else i + n - k
            k = i
        i = (i + 1) % n
    return seconds_elapsed + max(tickets)


if __name__ == "__main__":
    # Let's solve Time Needed to Buy Tickets problem from leetcode.com:
    # https://leetcode.com/problems/time-needed-to-buy-tickets/
    with open("time_needed_to_buy_tickets_cases.yaml", "r") as f:
        cases = yaml.safe_load(f)
    for c in cases:
        res = time_taken(tickets=c["input"]["tickets"], k=c["input"]["k"])
        print(f"Input: {c['input']}. Output: {res}. Expected output: {c['output']}")

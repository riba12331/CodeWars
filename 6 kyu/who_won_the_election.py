from collections import Counter, defaultdict


def getWinner(ballots):
    """ get_winner == PEP8 (forced mixedCase by CodeWars) """
    counts = Counter(ballots)
    flip = defaultdict(list)
    for a, b in counts.items():
        flip[b].append(a)
    max_key = max(flip)
    max_val = flip[max_key]
    return max_val[0] if len(max_val) == 1 and \
        max_key > len(ballots) / 2 else None

assert getWinner('A') == 'A'
assert getWinner(('A', 'A', 'A', 'B', 'B', 'B', 'A')) == 'A'
assert getWinner(('A', 'A', 'A', 'B', 'B', 'B')) is None
assert getWinner(('A', 'A', 'A', 'B', 'C', 'B')) is None
assert getWinner(('A', 'A', 'B', 'B', 'C')) is None

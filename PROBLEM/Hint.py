"""Hint
"""

units_rel, units_dig = input().split()
tens_rel, tens_dig = input().split()
hund_rel, hund_dig = input().split()

units_rel = units_rel.strip()
tens_rel = tens_rel.strip()
hund_rel = hund_rel.strip()

units_dig = int(units_dig)
tens_dig = int(tens_dig)
hund_dig = int(hund_dig)

def get_numbers(rel, dig):
    """Return list of valid digits 0-9 for given relation and digit."""
    result = []
    for d in range(10):
        if rel == "==" and d == dig:
            result.append(d)
        elif rel == ">" and d > dig:
            result.append(d)
        elif rel == "<" and d < dig:
            result.append(d)
        elif rel == ">=" and d >= dig:
            result.append(d)
        elif rel == "<=" and d <= dig:
            result.append(d)
        elif rel == "!=" and d != dig:
            result.append(d)
    return result


units = get_numbers(units_rel, units_dig)
tens = get_numbers(tens_rel, tens_dig)
hundreds = get_numbers(hund_rel, hund_dig)

results = []
for h in hundreds:
    for t in tens:
        for u in units:
            results.append(h * 100 + t * 10 + u)

results.sort()

for num in results:
    print(f"{num:03d}")

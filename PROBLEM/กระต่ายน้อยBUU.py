"""กระต่ายน้อยรัก BUU"""
def solve(s: str) -> str:
    """กระต่ายน้อยรัก BUU"""
    n = len(s)
    upper = s.upper()

    max_u = 0
    found = False
    for i, ch in enumerate(upper):
        if ch == 'B':
            cnt = 0
            j = i + 1
            while j < n and upper[j] == 'U':
                cnt += 1
                j += 1
            if cnt >= 2:
                found = True
                max_u = max(max_u, cnt)

    if found:
        return f"Yes {max_u}"

    idx = upper.find('B')
    if idx != -1:
        result = list(s)
        for k in range(idx + 1, n):
            result[k] = 'U'
        return ''.join(result)

    pattern = ('BUU' * ((n // 3) + 2))[:n]
    return pattern


def main():
    """อ่านข้อความจาก input แล้วพิมพ์ผลลัพธ์ตามเงื่อนไขของ solve()"""
    raw_input_text = input().strip()
    print(solve(raw_input_text))

main()

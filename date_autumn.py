def date_autumn(dates):
    minn = 2147483647
    j = ""
    seg = 2020 * 365 + 10 * 30 + 29
    for i in dates:
        h = i.split("-")
        seg1 = int(h[-1]) * 356 + int(h[-2]) + int(h[-3]) * 30
        if abs(seg - seg1) < minn and 9 <= int(h[-3]) <= 11:
            minn = abs(seg - seg1)
            j = h
    return "-".join(seg)

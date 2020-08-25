def cut(s):
    last = {c: i for i, c in enumerate(s)}
    partitions = []
    start = end = 0
    for i, c in enumerate(s):
        end = max(end, last[c])
        print(s[start:end])
        if i == end:
            partitions.append(i - start + 1)
            start = i + 1
    return partitions

print(cut('ababcbacadefegdehijhklij')) # Expected [9, 7, 8]

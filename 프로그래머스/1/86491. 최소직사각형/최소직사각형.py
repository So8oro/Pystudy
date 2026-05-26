def solution(sizes):
    long, short = [], []
    for size in sizes:
        if size[0] > size[1]:
            long.append(size[0])
            short.append(size[1])
        else:
            long.append(size[1])
            short.append(size[0])
    return max(long)*max(short)
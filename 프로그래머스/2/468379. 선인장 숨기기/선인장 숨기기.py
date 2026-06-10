class Rectangle:
    def __init__(self, r1, c1, r2, c2):
        self.r1 = r1  
        self.c1 = c1  
        self.r2 = r2  
        self.c2 = c2  

    def __repr__(self):
        return f"({self.r1}, {self.c1}, {self.r2}, {self.c2})"

    def __lt__(self, other):
        if self.r1 == other.r1:
            return self.c1 < other.c1
        return self.r1 < other.r1

def subtract_rectangle(empty, stamp):
    ir1 = max(empty.r1, stamp.r1)
    ic1 = max(empty.c1, stamp.c1)
    ir2 = min(empty.r2, stamp.r2)
    ic2 = min(empty.c2, stamp.c2)

    if ir1 > ir2 or ic1 > ic2:
        return [empty]

    result = []
    if ic2 < empty.c2:
        result.append(Rectangle(empty.r1, ic2 + 1, empty.r2, empty.c2))
    if ic1 > empty.c1:
        result.append(Rectangle(empty.r1, empty.c1, empty.r2, ic1 - 1))
    if ir1 > empty.r1:
        result.append(Rectangle(empty.r1, ic1, ir1 - 1, ic2))
    if ir2 < empty.r2:
        result.append(Rectangle(ir2 + 1, ic1, empty.r2, ic2))

    return result

# 새롭게 추가된 클린업 함수
def merge_rectangles(rects):
    if not rects:
        return []

    merged = True
    # 더 이상 합쳐지는 조각이 없을 때까지 반복
    while merged:
        merged = False

        # 1. 가로 병합 (r축 기준 높이와 위치가 완벽히 같은 조각들을 딕셔너리로 묶기)
        row_groups = {}
        for r in rects:
            key = (r.r1, r.r2)
            if key not in row_groups:
                row_groups[key] = []
            row_groups[key].append(r)

        next_rects = []
        for key, group in row_groups.items():
            # 같은 그룹 내에서 왼쪽(c1)에서 오른쪽 순으로 정렬
            group.sort(key=lambda x: x.c1)  
            merged_group = [group[0]]
            
            for i in range(1, len(group)):
                prev = merged_group[-1]
                curr = group[i]
                # 직전 조각의 오른쪽 끝과 현재 조각의 왼쪽 끝이 정확히 맞닿아 있다면
                if prev.c2 + 1 == curr.c1:  
                    # 하나로 합친 새로운 직사각형으로 덮어씌움
                    merged_group[-1] = Rectangle(prev.r1, prev.c1, prev.r2, curr.c2)
                    merged = True
                else:
                    merged_group.append(curr)
            next_rects.extend(merged_group)

        rects = next_rects

        # 2. 세로 병합 (c축 기준 너비와 위치가 완벽히 같은 조각들을 딕셔너리로 묶기)
        col_groups = {}
        for r in rects:
            key = (r.c1, r.c2)
            if key not in col_groups:
                col_groups[key] = []
            col_groups[key].append(r)

        next_rects = []
        for key, group in col_groups.items():
            # 같은 그룹 내에서 위(r1)에서 아래 순으로 정렬
            group.sort(key=lambda x: x.r1)  
            merged_group = [group[0]]
            
            for i in range(1, len(group)):
                prev = merged_group[-1]
                curr = group[i]
                # 직전 조각의 아래쪽 끝과 현재 조각의 위쪽 끝이 정확히 맞닿아 있다면
                if prev.r2 + 1 == curr.r1:  
                    # 하나로 합친 새로운 직사각형으로 덮어씌움
                    merged_group[-1] = Rectangle(prev.r1, prev.c1, curr.r2, prev.c2)
                    merged = True
                else:
                    merged_group.append(curr)
            next_rects.extend(merged_group)

        rects = next_rects

    return rects

def solution(m, n, h, w, drops):
    empty = [Rectangle(0, 0, m - h, n - w)]   

    for r, c in drops:
        next_empty = []
        stamp = Rectangle(r - h + 1, c - w + 1, r, c)

        for area in empty:
            next_empty.extend(subtract_rectangle(area, stamp))

        # 잘게 쪼개진 영역들을 다시 합쳐주는 클린업 과정 실행
        next_empty = merge_rectangles(next_empty)

        if not next_empty:
            empty.sort()
            return [empty[0].r1, empty[0].c1]

        empty = next_empty
    
    empty.sort()
    return [empty[0].r1, empty[0].c1]
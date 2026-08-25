def solution(arr):
    groups = ''.join(arr).split('-')

    first = sum(map(int, groups[0].split('+')))

    if len(groups) == 1:
        return first

    right_min = 0
    right_max = 0

    for group in groups[:0:-1]:
        nums = list(map(int, group.split('+')))

        group_min = -sum(nums)
        group_max = sum(nums[1:]) - nums[0]

        next_min = min(
            group_min + right_min,
            group_min - right_max
        )

        next_max = max(
            group_max + right_max,
            group_min - right_min
        )

        right_min, right_max = next_min, next_max

    return first + right_max
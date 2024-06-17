# LC 46
def permute(nums):
    def helper(path):
        if len(path) == len(nums):
            out.append(path[:])
            return

        for i, num in enumerate(nums):
            if not used[i]:
                path.append(num)
                used[i] = True
                helper(path)
                path.pop()
                used[i] = False

    out = []
    used = [False] * len(nums)
    helper([])
    return out


permute([4, 5, 6])


#------------------------------------------------------------------------

# LC 47
def permuteUnique(nums):
    def helper(path):
        if len(path) == len(nums):
            out.append(path[:])
            return

        for num, freq in counts.items():
            if freq > 0:
                path.append(num)
                counts[num] -= 1
                helper(path)
                path.pop()
                counts[num] += 1

    out = []
    counts = Counter(nums)
    helper([])
    return out



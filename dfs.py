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


#---------------------------------

def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1
    elif n < 0:
        self.myPow(1/x, abs(n))
    return x * self.myPow(x, n-1)

print(myPow(2.0, 10))
print(myPow(2.1, 3))
print(myPow(2.0, -2))


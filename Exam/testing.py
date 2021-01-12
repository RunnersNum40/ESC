def product(l, r):
    pools = [tuple(l)] * r
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)

def permutations(l):
    if len(l) == 1:
        yield l

    for n in range(len(l)):
        for new in permutations(l[:n]+l[n+1:]):
            yield [l[n]]+new

def interleave(nums, operators):
    exp = ""
    for n, o in zip(nums, operators):
        exp += n+o

    return exp+nums[-1]

def get_target(nums, target):
    operators = list("*/+-")
    if len(nums) == 0:
        return str(nums[0])

    for combo in permutations(nums):
        combo = list(map(str, combo))
        for n in range(0, len(nums)):
            for i in range(n+1, len(nums)):
                sub = list(combo)
                sub[n] = "("+sub[n]
                sub[i] = sub[i]+")"

                for j in range(0, len(nums)):
                    for k in range(j+1, len(nums)):
                        sub_sub = list(sub)
                        sub_sub[j] = "("+sub_sub[j]
                        sub_sub[k] = sub_sub[k]+")"
                        for o in product(operators, len(nums)-1):
                            expression = interleave(sub_sub, o)
                            try:
                                result = eval(expression)
                                if result == target:
                                    return expression
                            except:
                                pass

# 3*4*6+8 [3, 4, 6, 8] 80
print("Found", get_target([4, 6, 1, 7], 7))

# from random import randint, choice

# for x in range(100):
#     nums = [randint(1, 9) for i in range(randint(1, 10))]
#     o = [choice(list("+-*/")) for i in range(len(nums)-1)]

#     expression = [None for i in range(len(nums)*2-1)]
#     expression[::2] = "".join(map(str, nums))
#     expression[1::2] = o
#     expression = "".join(expression)

#     target = eval(expression)

#     print(expression, target)
#     result = get_target_noparens(nums, target)
#     print(result)
#     if result == None or eval(result) != target:
#         print("AAAAAAAAAAAAAAAA", expression, nums, target)
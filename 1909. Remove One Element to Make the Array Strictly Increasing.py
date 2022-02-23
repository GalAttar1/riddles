def canBeIncreasing(nums) -> bool:
    boolean = True
    i = 0
    while i < (len(nums) - 1):
        if len(nums) == 1: return True
        if nums[i] >= nums[i + 1]:
            if not boolean:
                return False
            else:
                boolean = False
                if len(nums) > i + 2:
                    if nums[i + 2] > nums[i] and nums[i + 2] > nums[i]:
                        nums.pop(i + 1)
                    else:
                        nums.pop(i)
                else:
                    nums.pop(i + 1)
                if i > 0: i -= 1
        else:
            i += 1
    return True


# test
lst = [42,50,54,74,84,86,88,93,104,127,143,160,164,169,170,181,209,223,225,231,247,257,262,274,282,306,307,320,346,357,378,381,387,392,394,404,423,437,444,456,476,491,507,524,527,528,537,558,566,574,169,584,585,609,621,626,632,644,653,661,662,670,676,698,704,710,718,719,730,735,737,746,748,755,776,782,785,795,802,812,822,828,863,866,870,872,877,899,905,909,919,929,940,944,961,963,980,981]
print(canBeIncreasing(lst))

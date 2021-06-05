def binary_search(self, nums, target):
    # Corner case,
    # It equals that nums is None or len(nums) == 0
    if not nums:
        return -1

    start, end = 0, len(nums) - 1

    # "start + 1 < end", not "start < end" => Avoid deadlock
    # First position of target => No deadlock
    # Last position of target => Deadlock
    # E.g.：nums = [1，1] target = 1
    while start + 1 < end:
        # In Python there is no overflow => // 2
        # But in Java or C++ => mid = start + (end - start) / 2
        # to avoid overflow when "start = 2^31 - 1, end = 2^31 - 1"
        mid = (start + end) // 2

        # Try to separate logic that > , =, <  
        # And then combine = to other branch
        if nums[mid] < target:
            start = mid
        elif nums[mid] == target:
            end = mid
        else:
            end = mid

    # When condition to break loop is "start + 1 < end"
    # start/end is like 1/2 or 3/4
    # So need to check that start or end, which is answer
    # For first position of target -> start, otherwise -> end
    if nums[start] == target:
        return start
    if nums[end] == target:
        return end
    return -1
    
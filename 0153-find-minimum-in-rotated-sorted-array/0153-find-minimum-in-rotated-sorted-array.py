class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        start = 0
        end = size - 1

        while start <= end:

            mid = start + (end - start) // 2
            prev = (mid - 1 + size) % size
            next = (mid + 1) % size

            if nums[mid] <= nums[next] and nums[mid] <= nums[prev]:
                return nums[mid]

            elif nums[mid] <= nums[end]:
                end = mid - 1

            elif nums[mid] >= nums[start]:
                start = mid + 1

        return

        
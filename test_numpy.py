
class Solution(object):
	def twosum(self, nums, target):
		#flags = [0 for i in range(len(nums))]
		l = len(nums)
		dict_name = {nums[i]: i for i in range(l)}
		for a in range(l):
			one_num = nums[a]
			other_one = target - one_num
			if other_one in dict_name and a != dict_name[other_one]:
				return [a, dict_name[other_one]]


nums = [7, 15, 11, 2]
target = 9
test = Solution()
result = test.twosum(nums, target)
print(nums[result[0]], nums[result[1]])
#print({nums[i]: i for i in range(len(nums))})
#dict_name = {nums[i]: i for i in range(len(nums))}
#print(nums[2])
#print(dict_name[7])
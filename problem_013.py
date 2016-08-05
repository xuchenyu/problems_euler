def solution(nums):
	result = [0]*13
	for i in range(11):
		i_sum = sum([int(nums[j][i]) for j in range(100)])
		result[i] += i_sum/100
		result[i+1] += i_sum%100/10
		result[i+2] += i_sum%100%10
	
	for i in range(11, 1, -1):
		if result[i] > 9:
			result[i] -= 10
			result[i-1] += 1

	return reduce(lambda x, y: str(x)+str(y), result[:10])

f = open('data_013.txt', 'r')
nums = [row for row in f.readlines()]
f.close()
print solution(nums)
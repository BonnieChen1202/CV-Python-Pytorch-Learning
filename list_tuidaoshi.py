# 目标：从【1，2，3，4 ，5 ，6 ，7 ，8 】中筛选偶数并求平方
nums = [1,2,3,4,5,6,7,8]

result = [x**2 for x in nums if x % 2 == 0]

print("筛选并求平方后的结果：", result)
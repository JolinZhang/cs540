nums = [1,2,3,4,5,6]
evenNums = [x for x in nums if x % 2 == 0]
print 'the even numbers are:' + str(evenNums)
evenNumsPlusOne = [x+1 for x in evenNums]
print evenNumsPlusOne

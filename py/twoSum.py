# Given an array of integers, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, 
# where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution.
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2


class Solution:
    ### @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, nums, target):
        numsDict = dict()
        for index,item in enumerate(nums):
            numsDict[item] = index
        for indexCheck,itemCheck in enumerate(nums):
            remainder = target - itemCheck
            if remainder in numsDict:
                if numsDict[remainder] != indexCheck:
                    secondIndex = numsDict[remainder]
                    if indexCheck <= secondIndex:
                        return [indexCheck + 1, secondIndex + 1]
                    else:
                        return [secondIndex + 1, indexCheck + 1]

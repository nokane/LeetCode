/**

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.

 * @param {number[]} nums
 * @return {number[][]}
 */

var threeSum = function(nums) {
  var result = [];
  var compare = {};

  var createArray = function(first, second, third) {
    return [first, second, third];
  };

  var checkFound = function(a, b, needed) {
    var found;
    if (a <= b) {
      if (b <= needed) {
        found = createArray(a, b, needed);
      } else {
        if (needed <= a) {
          found = createArray(needed, a, b);
        } else {
          found = createArray(a, needed, b);
        }
      }
    } else {
      if (b <= needed) {
        if (needed <= a) {
          found = createArray(b, needed, a);
        } else {
          found = createArray(b, a, needed);                  
        }
      } else {
        found = createArray(needed, b, a);
      }
    }
    if (!compare.hasOwnProperty(found.slice())) {
      result.push(found.slice());
      compare[found.slice()] = 1;
      delete found;
    }
  };

  var search = function(nums) {
    for (var i = 0; i < nums.length; i++) {
      var a = nums[i];
      for (var j = 0; j < nums.length; j++) {
        if (j !== i) {
          var b = nums[j];
          var needed = -1 * (b + a);
          var neededIndex = nums.indexOf(needed)
          if (neededIndex > -1 && neededIndex !== i && neededIndex !== j) {
            //zero sum found
            checkFound(a, b, needed);
          }
        }
      }
    }
  }
  search(nums);
  return result;
};

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
  var objResult = {};

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
    if (!objResult.hasOwnProperty(found.slice())) {
      result.push(found.slice());
      objResult[found.slice()] = 1;
      delete found;
    }
  };

  for (var i = 0; i < nums.length; i++) {
    compare[nums[i]] = i;
  }

  var search = function(arr) {
    for (var j = 0; j < arr.length; j++) {
      var a = arr[j];
      for (var k = 0; k < arr.length; k++) {
        if (k !== j) {
          var b = arr[k];
          var needed = -1 * (b + a);
          if (compare.hasOwnProperty(needed)) {
            var neededIndex = compare[needed];
            if (neededIndex > -1 && neededIndex !== j && neededIndex !== k) {
            //zero sum found
            checkFound(a, b, needed);
            }
          }
        }
      }
    }
  }
  search(nums);
  return result;
};

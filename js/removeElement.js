/**

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
  var checkIndex = function(ind) {
    if (nums[ind] === val) {
      nums.splice(ind,1);
      checkIndex(ind);
    }
  }
  for (var i = 0; i < nums.length; i++) {
    checkIndex(i);
  }
  return nums.length;
};

/**
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
For example:
Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {

  var recurseNum = function(checkNum) {
    var numString = checkNum.toString();
    if (numString.length === 1) {
      return checkNum;
    }
    var total = 0;
    for (var i = 0; i < numString.length; i++) {
      total += parseInt(numString.charAt(i));
    }
    return recurseNum(total);
  }

  return recurseNum(num);
};

/**
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

 * @param {number} x
 * @return {number}
 */

var reverse = function(x) {
  var reversed = '';
  if (x < 0) {
    x *= -1;
    reversed += '-';
  }
  var stringified = x.toString();

  for (var i = stringified.length - 1; i >= 0; i--) {
    reversed += stringified.charAt(i);
  }

  return parseInt(reversed);

};
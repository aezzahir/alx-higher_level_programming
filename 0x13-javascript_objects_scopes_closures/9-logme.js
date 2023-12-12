#!/usr/bin/node
exports.logMe = function (item) {
  if (typeof exports.logMe.counter === 'undefined') {
    exports.logMe.counter = 0;
  } else {
    exports.logMe.counter++;
  }

  console.log(exports.logMe.counter + ': ' + item);
};

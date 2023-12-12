#!/usr/bin/node
exports.esrever = function (list) {
  const array = [];
  for (const element of list) {
    array.unshift(element);
  }
  return (array);
};

#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOfocc = 0;
  for (const element of list) {
    if (element === searchElement) {
      nOfocc++;
    }
  }
  return (nOfocc);
};

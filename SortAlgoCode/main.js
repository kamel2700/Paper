//nodejs v8.10.0

let arr = Array.from({length: 10000}, () => Math.floor(Math.random() * 1000));
arr.sort(function(a, b) {
  return a - b;
});

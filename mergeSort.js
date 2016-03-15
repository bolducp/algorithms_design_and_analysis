function mergeSort(aList) {
  if (aList.length <= 1) {
    return aList;
  }

  var mid = parseInt(aList.length / 2);
  var left = aList.slice(0, mid);
  var right = aList.slice(mid);

  return merge(mergeSort(left), mergeSort(right));
}


function merge(a, b) {
  var merged = [];

  while (a.length && b.length) {
    if (a[0] < b[0]) {
      merged.push(a.shift());
    } else {
      merged.push(b.shift());
    }
  }

  while (a.length) {
    merged.push(a.shift());
  }

  while (b.length) {
    merged.push(b.shift());
  }

  return merged;
}



function mergeV2(a, b) {
  var merged = [];
  var aIndex = 0;
  var bIndex = 0;

  while (aIndex < a.length && bIndex < b.length) {
    if (a[aIndex] < b[bIndex]) {
      merged.push(a[aIndex]);
      aIndex++;
    } else {
      merged.push(b[bIndex]);
      bIndex++;
    }
  }

  while (aIndex < a.length) {
    merged.push(a[aIndex]);
    aIndex++;
  }

  while (bIndex < b.length) {
    merged.push(b[bIndex]);
    bIndex++;
  }

  return merged;
}


console.log(merge([3, 4, 5], [0, 2, 7, 8]));
console.log(mergeSort([3, 4, 5, 0, 2, 7, 8]));

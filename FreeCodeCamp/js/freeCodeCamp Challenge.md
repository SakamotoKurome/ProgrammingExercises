#### freeCodeCamp Challenge Guide: Restrict Possible Usernames

你的正则表达式应该匹配字符串 JACK
你的正则表达式应该匹配字符串 Jo
你的正则表达式应该匹配字符串 Oceans11
你的正则表达式应该匹配字符串 RegexGuru
你的正则表达式应该匹配字符串 Z97
你的正则表达式应该匹配字符串 AB1

##### My Solution

```js
/^[a-zA-Z][a-zA-Z]+$|^[a-zA-Z][a-zA-Z]+\d*$|^[a-zA-Z]\d\d+$/
```

##### Solution1

```js
/^[a-z][a-z]+\d*$|^[a-z]\d\d+$/i
```

##### Solution2

```js
/^[a-z]([0-9]{2,}|[a-z]+\d*)$/i
```

#### 找出数字范围内的最小公倍数

找到给定参数的最小公倍数，可以被这两个参数整除，也可以被指定范围内的所以整数整除。

注意，较小数不一定总是出现在数组的第一个元素。

例如，如果给定 1 和 3，找到 1 和 3 的最小公倍数，也可以被 1 到 3 之间的所有数字整除。 这里的答案将是 6。

##### My Solution

```js
function smallestCommons(arr) {
  function GCD(num1, num2) {//最大公约数-辗转相除法
    if (num1 % num2 === 0) {
      return num2;
    } else {
      return GCD(num2, num1 % num2);
    }
  }
  
  function FCM(num1, num2) {//最小公倍数-公式法
    return num1 * num2 / GCD(num1, num2);
  }

  let newArr = [];
  if (arr[0] > arr[arr.length-1]) {
    arr.reverse();
  }
  console.log(arr);
  for (let i = arr[0]; i <= arr[arr.length-1]; i++) {
    newArr.push(i);
  }

  let result = newArr.reduce((fcm, elem) => {
    return FCM(fcm, elem);
  });

  return result;
}

smallestCommons([5, 1]);
```

#### 数组扁平化

嵌套数组扁平化成一维数组。 必须考虑到各种深度的嵌套层级。

##### My Solution

```
function steamrollArray(arr, newArr = []) {
  arr.forEach(elem => {
    if (elem instanceof Array) {
      steamrollArray(elem, newArr);
    } else {
      newArr.push(elem);
    }
  })
  return newArr;
}

steamrollArray([1, [2], [3, [[4]]]]);
```

#### 翻译二进制字符串

请实现一个函数，把传入的二进制字符串转换成英文句子。

二进制字符串会以空格分隔。

##### My Solution

```js
function binaryAgent(str) {
  // let chars = str.split(' ');
  // chars = chars.map(elem => parseInt(elem, 2));
  // chars = chars.map(elem => String.fromCharCode(elem));
  // str = chars.join('');
  str = str.split(' ').map(elem => {
    return String.fromCharCode(parseInt(elem, 2));
  }).join('');
  return str;
}

binaryAgent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111");
```

#### 回文检查器

##### My Solution

```js
function palindrome(str) {
  let str1 = str.replace(/[^a-z0-9]/ig, '').toLowerCase();
  let str2 = str1.split('').reverse().join('');
  let result = str1.indexOf(str2);
  if (result === 0) {
    return true;
  } else {
    return false;
  }
}

palindrome("almostomla");
palindrome("2A3*3a2");
```

#### 罗马数字转换器

##### My Solution

```js
function convertToRoman(num) {
  if (num >= 4000) {
    console.log('max is 3999');
    return;
  }

  let roman = {
    Thousands: ['M', '', ''],
    Hundreds: ['C', 'D', 'M'],
    Tens: ['X', 'L', 'C'],
    Ones: ['I', 'V', 'X'],
  }

  let numArr = [
    Math.floor(num / 1000),
    Math.floor(num % 1000 / 100),
    Math.floor(num % 100 / 10),
    num % 10,
  ];

  function convert(number, s1, s2, s3) {
    switch(number) {
      case 0: return '';
      case 1: return s1;
      case 2: return s1+s1;
      case 3: return s1+s1+s1;
      case 4: return s1+s2;
      case 5: return s2;
      case 6: return s2+s1;
      case 7: return s2+s1+s1;
      case 8: return s2+s1+s1+s1;
      case 9: return s1+s3;
    }
  }

  let i = 0;
  let result = '';
  for (let k in roman) {
    result += convert(numArr[i], ...roman[k]);
    i++;
  }

  return result;
}

convertToRoman(3014);
```

#### 凯撒密码

##### My Solution

```js
function rot13(str) {
  let alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
  let rot13 = {};
  for (let i = 0; i < alpha.length; i++) {
    let rot = alpha[(i+13) % 26];
    rot13[alpha[i]] = rot;
  }

  return str.split('').map(elem => {
    if(/[A-Z]/.test(elem)) {
      return rot13[elem];
    } else {
      return elem;
    }
  }).join('');
}

let result = rot13("SERR PBQR PNZC");
```

#### 电话号码检查器

##### My Solution

```js
function telephoneCheck(str) {

  let result = str.match(/^(\d?)[ -]?(\(?)\d{3}(\)?)[ -]?\d{3}[ -]?\d{4}$/);

  if (!result) {
    return false;
  }

  if (result[1] && result[1] != 1) {
      return false;
  }

  if ((!result[2] && result[3])
    || (result[2] && !result[3])) {
      return false;
  }
  return true;
}

let result = telephoneCheck("-1 (757) 622-7382");
console.log('result:', result);
```

#### 计算找零

##### My Wrong Solution

```js
function checkCashRegister(price, cash, cid) {

  let change = cash - price;

  let cidObj = cid.reduce((obj, elem) => {
    obj[elem[0]] = elem[1];
    return obj;
  }, {});

  let cidSum = 0;
  for (let key in cidObj) {
    cidSum += cidObj[key];
  }

  let output = {};
  if (cidSum === change) {
    output.status = 'CLOSED';
    output.change = cid;
    return output;
  }

  if (cidSum < change) {
    return {status: "INSUFFICIENT_FUNDS", change: []};
  }

  let changeObj = {};

  function Face(name, value, nextface) {
    this.name = name;
    this.value = value;
    this.nextface = nextface;
  }

  let face = [
    {
      name: 'ONE HUNDRED',
      value: 100,
    },
    {
      name: 'TWENTY',
      value: 20,
    },
    {
      name: 'TEN',
      value: 10,
    },
    {
      name: 'FIVE',
      value: 5,
    },
    {
      name: 'ONE',
      value: 1,
    },
    {
      name: 'QUARTER',
      value: 0.25,
    },
    {
      name: 'DIME',
      value: 0.1,
    },
    {
      name: 'NICKEL',
      value: 0.05,
    },
    {
      name: 'PENNY',
      value: 0.01,
    },
  ];

  let hundred = face.reverse().reduce((nextface, elem) => {
    let newFace = new Face(elem.name, elem.value, nextface);
    return newFace;
  }, null);


  function get(face) {
    if (change > cidObj[face.name]) {
      changeObj[face.name] = cidObj[face.name];
      cidObj[face.name] = 0;
      change = change - changeObj[face.name];
      change = Math.round(change * 100) / 100;
      if (face.nextface !== null) {
        get(face.nextface);
      }
    } else {
      let mid = change % face.value;
      changeObj[face.name] = change - mid;
      cidObj[face.name] = cidObj[face.name] - changeObj[face.name];
      change = mid;
      change = Math.round(change * 100) / 100;
      if (change !== 0 && face.nextface !== null) {
        get(face.nextface);
      }
    }
  }

  get(hundred);

  if (changeObj.length < 1 || change > 0) {
    return {status: "INSUFFICIENT_FUNDS", change: []};
  }

  let changeArr = [];
  for (let key in cidObj) {
    if (changeObj[key] && changeObj !== 0) {
      changeArr.push(new Array(key, changeObj[key]));
    } 
  }
  changeArr = changeArr.reverse();

  output.status = 'OPEN';
  output.change = changeArr;
  return output;
}

let result = checkCashRegister(3.26, 100, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]])
console.log(result);
```


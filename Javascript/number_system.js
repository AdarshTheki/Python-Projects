/**

Practice Questions in JavaScript

Number Systems

Convert Decimal to Binary Without .toString()
Write a function that takes a decimal number and returns its binary form using division & modulus.

Check if a Number is a Power of Two
Use bitwise operations (&) to check.

Count Set Bits in a Number
Write a function that counts how many 1s are in the binary representation of a number.

Implement XOR Swap
Swap two numbers without using a temporary variable.

📦 Data Structures

Arrays
Implement a function that reverses an array without using reverse().
Write a function to find the maximum subarray sum (Kadane’s Algorithm).
Implement a function that removes duplicates from an array without using Set.

Linked List
Implement a function to reverse a linked list.
Detect if a linked list has a cycle (Floyd’s Cycle Detection Algorithm).
Merge two sorted linked lists into one.

Stack
Implement a function to check for balanced parentheses using a stack.
Implement Min Stack (stack that supports getMin() in O(1) time).
Evaluate a postfix expression using stack.

Queue
Implement a queue using two stacks.
Implement a circular queue.
Simulate a printer queue where tasks are dequeued in order.

HashMap
Count character frequencies in a string using Map.
Find the first non-repeating character in a string.
Implement a two-sum problem using a HashMap.
Group words that are anagrams using a HashMap.

* **/

// 1. Binary, Octal, Hexadecimal
function binaryFunction() {
  const decimal = 25;

  console.log(decimal.toString(2)); // "11001" → Binary
  console.log(decimal.toString(8)); // "31"    → Octal
  console.log(decimal.toString(16)); // "19"    → Hexadecimal

  console.log(parseInt('11001', 2)); // 25
  console.log(parseInt('31', 8)); // 25
  console.log(parseInt('19', 16)); // 25

  // num.toString(base) → converts number into binary (2), octal (8), hex (16).
  // parseInt(str, base) → converts from binary/octal/hex string into decimal.
}

// 2. Binary Operations & Bits
function operationsAndBits() {
  let a = 5; // 0101 (binary)
  let b = 3; // 0011 (binary)

  console.log(a & b); // 1  → AND  (0101 & 0011 = 0001)
  console.log(a | b); // 7  → OR   (0101 | 0011 = 0111)
  console.log(a ^ b); // 6  → XOR  (0101 ^ 0011 = 0110)
  console.log(~a); // -6 → NOT  (~0101 = 1010 in 2's complement)
  console.log(a << 1); // 10 → Left Shift (0101 → 1010)
  console.log(a >> 1); // 2  → Right Shift (0101 → 0010)

  // & AND → both must be 1.
  // | OR → at least one 1.
  // ^ XOR → only one is 1.
  // ~ NOT → flips bits.
  // << left shift → multiply by 2.
  // >> right shift → divide by 2.
}

// 3. Logical Gates (AND, OR, NOT, XOR)
function logicalGates() {
  const AND = (a, b) => a & b;
  const OR = (a, b) => a | b;
  const NOT = (a) => a ^ 1; // or use ! for boolean
  const XOR = (a, b) => a ^ b;

  console.log(AND(1, 0)); // 0
  console.log(OR(1, 0)); // 1
  console.log(NOT(1)); // 0
  console.log(XOR(1, 0)); // 1
  /**
   * Explanation:
   * We can mimic digital logic gates using bitwise operators.
   * Useful in low-level programming, encryption, compression.*/
}

// 4. Arrays
function arrays() {
  // Insert: push, unshift;
  // Delete: pop, shift;
  // Access: arr[index];
  // Search: indexOf, includes;
}

// 5. Linked Lists
function linkedLists() {
  class Node {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
  }
  class LinkedList {
    constructor() {
      this.head = null;
    }
    append(value) {
      const newNode = new Node(value);
      if (!this.head) {
        this.head = newNode;
        return;
      }
      let curr = this.head;
      while (curr.next) {
        curr = curr.next;
      }
      curr.next = newNode;
    }
    print() {
      let curr = this.head;
      let arr = [];
      while (curr) {
        arr.push(curr.value);
        curr = curr.next;
      }
      console.log(arr);
    }
  }

  const liked = new LinkedList();
  liked.append(10);
  liked.append(20);
  liked.append(30);
  liked.print();
}

// 6. Stack - LIFO mechanism
function stack() {
  class Stack {
    constructor() {
      this.items = [10, 20];
    }
    push(item) {
      this.items.push(item);
    }
    pop() {
      this.items.pop();
    }
    peek() {
      return this.items[this.items.length - 1];
    }
    isEmpty() {
      return (this.items.length = 0);
    }
  }

  const stack1 = new Stack();
  stack1.push(30);
}

// 7. Queues - FIFO mechanism
function queue() {
  class Queue {
    constructor() {
      this.items = [10, 20, 30];
    }
    enqueue(item) {
      this.items.push(item);
    }
    dequeue() {
      this.items.shift();
    }
    peek() {
      return this.items[0];
    }
    isEmpty() {
      return (this.items.length = 0);
    }
  }
  let q1 = new Queue();
  q1.isEmpty();
}

// 8. HashMaps
function hashMaps() {
  const map = new Map();
  map.set('name', 'Adarsh');
  map.set('age', 28);

  for (let [k, v] of map) {
    console.log(k, v);
  }

  // Map in JS works like a HashMap.
  // Insert: set
  // Access: get
  // Delete: delete
  // Check: has
  // Efficient for key-value pair storage & lookup.
}

// DSA: Question

function decimalToBinary(n) {
  let result = '';
  while (n > 0) {
    result = (n % 2) + result;
    n = Math.floor(n / 2);
  }
  return result || '0';
}

function isPowerOfTwo(n) {
  return n > 0 && (n & (n - 1)) === 0;
}

function xorSwap() {
  let a = 5,
    b = 9;
  console.log('Before Swap:', a, b);
  a = a ^ b;
  b = a ^ b;
  a = a ^ b;
  console.log('After Swap:', a, b);
}

function countSetBits(n = 13) {
  let count = 0;
  while (n > 0) {
    count += n & 1; // check last bit
    n >>= 1; // right shift
  }
  console.log(count); // 3 (1101 has 3 ones)
}

function reverseArray() {
  let arr = [1, 2, 4, 6, 5, 3, 7];
  let left = 0,
    right = arr.length - 1;
  while (left < right) {
    [arr[left], arr[right]] = [arr[right], arr[left]];
    left++;
    right--;
  }
  console.log(arr);
}

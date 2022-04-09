# Fancy Fizzbuzz
## How
You should write code to solve this problem without googling for an answer or
asking your friends for an answer. It is OK to look up syntax online or in a book. For
example, if you don’t recall the syntax needed for a “for” loop in Python, you can
look that up. However, please don’t try to find someone else’s solution for
“Fizzbuzz” (there are plenty of them out there).

## What
You are asked to solve the classic problem “Fizzbuzz”, but with a few changes
(don’t worry if you have never heard of “Fizzbuzz”). Here are the specs.
Ask the user for a beginning integer value.
Ask the user for an integer value that will “stop the loop”. That is, when you hit this value or go beyond it, the loop should end.
Ask the user for an integer value that will “step” from the beginning value to the ending value.
Iterate from the beginning value to the ending value in the designated step amount. For example, if you begin at 1, end at 10, and step by 1 your numbers will be (in order): 1,2,3,4,5,6,7,8,9. If you begin at 5, end at 20, and step by 5 your numbers will be (in order): 5,10,15.
For each number that you are going through, print “Fizz” if the number is divisible by 3. Print “Buzz” if the number is divisible by 5. Print the number itself if it is neither divisible by 3, nor by 5.
Try to make your program output look similar to the examples below.
You must define at least one function in the program and must call the function at least once to do some valuable work (not just call it and have it do nothing).
## Tips
Focus on breaking this into small, working pieces.
Your goal should be to have a program that compiles when you submit it - even if not all features are in place, compiling with a smaller feature set is better than a broken program with lots of half-finished ideas
Think about saving off working versions of your code in case you need to revert

# Desired Output
## Example Program Run Number 1
```
Enter the starting number: 23
Enter the limit: 47
Enter the increment: 1
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
```
## Example Program Run Number 2
```
Enter the starting number: 25
Enter the limit: 14
Enter the increment: -1
Buzz
Fizz
23
22
Fizz
Buzz
19
Fizz
17
16
FizzBuzz
```
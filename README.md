# HCL TRAINING
## First Task:
Collect the test cases from Amazon e-commerce site.

## Excel sheet:
[View the manual excel sheet](https://1drv.ms/x/c/3f24897300df0f03/IQBRUV_phyqETrC2RdSyAJuEARk8QOXuOD2tjazzZuPrbaU?e=eA0LCQ).

## Second Task
Find the test cases and valid and invalid input from given exercises.

## Excel sheet:
[View the test cases from given exercises XL sheet](https://1drv.ms/x/c/3f24897300df0f03/IQB25jVCIfegRqRBawPXy3_eASXzp7QLlZx2asbUlbraHzo?e=pIUsvK).

# Python Programming Exercises
## Programs

### 1. Binary Numbers Divisible by 5

#### Aim
Write a Python program that accepts a sequence of comma-separated 4-digit binary numbers and checks which numbers are divisible by 5.

#### Algorithm
1. Read comma-separated binary numbers from the user.
2. Split the input using `split(",")`.
3. Convert each binary number into decimal using `int(i, 2)`.
4. Check whether the decimal value is divisible by 5.
5. Store the divisible numbers in a list.
6. Print the numbers as a comma-separated sequence.

#### Program

```python
s=input().split(",")
result=[]
for i in s:
    if (int(i,2)%5==0):
        result.append(i)
print(",".join(result))
```
### OUTPUT

<img width="890" height="56" alt="image" src="https://github.com/user-attachments/assets/f5d10255-c47a-4fbf-8b5f-6748cbdb31c0" />

### 2. Count Letters and Digits

#### Question
Write a Python program that accepts a sentence and calculates the number of letters and digits.

#### Aim
Write a Python program that accepts a sentence and calculates the number of letters and digits.

#### Algorithm
1. Read a sentence from the user.
2. Initialize `letters` and `digits` to 0.
3. Traverse each character using a `for` loop.
4. Check whether the character is a letter using `isalpha()`.
5. Check whether the character is a digit using `isdigit()`.
6. Increment the respective counter.
7. Display the number of letters and digits.

#### Program

```python
n=input("Enter the sentence:")
letters=0
digits=0
for i in n:
    if i.isalpha():
        letters+=1
    elif i.isdigit():
        digits+=1
print("LETTERS: ",letters)
print("DIGITS: ",digits)
```
### OUTPUT

<img width="877" height="92" alt="image" src="https://github.com/user-attachments/assets/b6b70cae-f0e5-47b7-9abb-81d2bf454dc9" />

### 3. Factorial of a Number

#### Question
Write a program which can compute the factorial of a given number. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8

#### Aim
Write a Python program to compute the factorial of a given number.

#### Algorithm
1. Read a number from the user.
2. Initialize `fact` to 1.
3. Use a `for` loop from 1 to the given number.
4. Multiply each number with `fact`.
5. Store the calculated factorial.
6. Display the factorial.

#### Program

```python
n=int(input("Enter the value:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
```
## OUTPUT

<img width="817" height="112" alt="image" src="https://github.com/user-attachments/assets/3f5bb022-e6f8-4dcb-ab07-70035fdc5172" />

'''
1. Student Attendance Analysis
'''
n = int(input())
a = list(map(int, input().split()))

seen = set()
left = 0
maximum = 0

for right in range(n):
    while a[right] in seen:
        seen.remove(a[left])
        left += 1

    seen.add(a[right])
    maximum = max(maximum, right - left + 1)

print("Maximum value of length",maximum)

'''
2. Online Shopping Price Analysis
'''
n = int(input())
a = list(map(int, input().split()))

current = a[0]
maximum = a[0]

for i in range(1, n):
    current = max(a[i], current + a[i])
    maximum = max(maximum, current)

print(maximum)

'''
3. Rainwater Collection System
'''
n = int(input())
a = list(map(int, input().split()))

left = 0
right = n - 1

left_max = 0
right_max = 0

water = 0

while left <= right:
    if a[left] <= a[right]:
        if a[left] >= left_max:
            left_max = a[left]
        else:
            water += left_max - a[left]

        left += 1

    else:
        if a[right] >= right_max:
            right_max = a[right]
        else:
            water += right_max - a[right]

        right -= 1

print(water)

'''
4. Employee Performance Analysis
'''
n = int(input())
a = list(map(int, input().split()))

current = a[0]
maximum = a[0]

for i in range(1, n):
    current = max(a[i], current + a[i])
    maximum = max(maximum, current)

print(maximum)

'''
5. Product Sales Analysis
'''
n = int(input())
a = list(map(int, input().split()))

maximum = a[0]
minimum = a[0]
answer = a[0]

for i in range(1, n):
    x = a[i]

    if x < 0:
        maximum, minimum = minimum, maximum

    maximum = max(x, maximum * x)
    minimum = min(x, minimum * x)

    answer = max(answer, maximum)

print(answer)
'''
6. Customer Purchase History
'''
n = int(input())
a = list(map(int, input().split()))

seen = set()
left = 0
maximum = 0

for right in range(n):
    while a[right] in seen:
        seen.remove(a[left])
        left += 1

    seen.add(a[right])
    maximum = max(maximum, right - left + 1)

print("Maximum value of length",maximum)
'''
7. Bank Transaction Analysis
'''
n = int(input())
a = list(map(int, input().split()))

target = int(input())

prefix = {0: 1}

total = 0
count = 0

for x in a:
    total += x

    if total - target in prefix:
        count += prefix[total - target]

    prefix[total] = prefix.get(total, 0) + 1

print(count)
'''
8. Employee Skill Grouping
'''
n = int(input())
words = input().split()

groups = {}

for word in words:
    key = ''.join(sorted(word))

    if key not in groups:
        groups[key] = []

    groups[key].append(word)

for group in groups.values():
    print(*group)
'''
9. Network Packet Analysis    
'''
n = int(input())
a = list(map(int, input().split()))

numbers = set(a)

maximum = 0

for num in numbers:

    if num - 1 not in numbers:
        current = num
        length = 1

        while current + 1 in numbers:
            current += 1
            length += 1

        maximum = max(maximum, length)

print(maximum)
'''
10. Hospital Appointment Scheduling
'''
n = int(input())

intervals = []

for i in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

intervals.sort()

merged = []

for start, end in intervals:

    if not merged or start > merged[-1][1]:
        merged.append([start, end])

    else:
        merged[-1][1] = max(merged[-1][1], end)

for start, end in merged:
    print(start, end)

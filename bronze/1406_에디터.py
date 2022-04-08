import sys
input = sys.stdin.readline

input_str = input().rstrip()
M = int(input())
i = len(input_str) - 1

for _ in range(M):
    command = input().split()

    if command[0] == 'L' and i != -1:
        i -= 1
    elif command[0] == 'D' and i != len(input_str) - 1:
        i += 1
    elif command[0] == 'B' and i != -1:
        input_str = input_str[:i] + input_str[i + 1:]
        i -= 1
    elif command[0] == 'P':
        input_str = input_str[:i+1] + command[1] + input_str[i+1:]
        i += 1

print(input_str)

# import sys
#
# temp = sys.stdout                 # store original stdout object for later
# sys.stdout = open('log.txt', 'w') # redirect all prints to this log file
# print('testing123')               # nothing appears at interactive prompt
# print('another line')             # again nothing appears. it's written to log file instead
# sys.stdout.close()                # ordinary file object
# sys.stdout = temp                 # restore print commands to interactive prompt
# print('back to normal')           # this shows up in the interactive prompt



# import sys
#
# print('Python')
#
# sys.stdout = open('file.txt', 'w')
#
# print('is')
# print('Power')

# Задача 1

# import sys
# data = list(map(str.strip, sys.stdin))
# for i in data:
#     print(i[::-1])

# Задачи 2
# import sys
# from datetime import datetime, timedelta
# data = list(map(str.strip, sys.stdin))
# sp = [datetime.strptime(i, "%Y-%m-%d") for i in data]
# dev = max(sp) - min(sp)
# print(dev.days)

# Задача 3

import sys

soks = list(map(str.strip, sys.stdin))
last = soks[-1]

if int(last) % 2 == 0 and len(soks) % 2 == 1:
    print("Арни")
if int(last) % 2 == 0 and len(soks) % 2 == 0:
    print("Дима")



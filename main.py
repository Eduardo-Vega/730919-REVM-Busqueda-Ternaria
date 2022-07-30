arr = None
key = None
r = None
l = None
mid1 = None
mid2 = None
i = None

def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
key = 6
r = len(arr) - 1
l = 0
mid1 = l + (r - l) / 3
mid2 = r - (r - l) / 3
if key == arr[int(mid1 - 1)]:
  print(mid1)
elif key == arr[int(mid2 - 1)]:
  print(mid2)
else:
  if key < arr[int(mid1 - 1)]:
    for i in (1 <= float(mid1)) and upRange(1, float(mid1), 1) or downRange(1, float(mid1), 1):
      if key == arr[int(i - 1)]:
        print(i)
  elif key > arr[int(mid2 - 1)]:
    i_end = float(len(arr))
    for i in (float(mid2) <= i_end) and upRange(float(mid2), i_end, 1) or downRange(float(mid2), i_end, 1):
      if key == arr[int(i - 1)]:
        print(i)
  else:
    for i in (float(mid1) <= float(mid2)) and upRange(float(mid1), float(mid2), 1) or downRange(float(mid1), float(mid2), 1):
      if key == arr[int(i - 1)]:
        print(i)
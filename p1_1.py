# -*- coding: utf-8 -*-
"""P1_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_GlkQo2LuC8448mXl-fZcA9MNHJZxN3L
"""

start = input().split()
end = input().split()
start_x = int(start[0])
start_y = int(start[1])
end_x = int(end[0])
end_y = int(end[1])
if checkerboard[end_x][end_y] == 0:
  if start_x != end_x or start_y != end_y:
    if abs(start_x - end_x) <= 1 and abs(start_y - end_y) <= 1:
      print("Yes")
    else:
      print("No")
  else:
    print("No")
else:
  print("No")
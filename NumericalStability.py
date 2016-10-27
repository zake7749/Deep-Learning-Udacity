"""
Whip out a Python interpreter or use this online Sandbox.

Set a variable to 1 billion (109). Then add 10-6 to it a million (106) times. Now subtract 1 billion from it. What is the result?
"""

res = 1e9

for i in range(1000000):
	res += 1e-6

res -= 1e9
print(res)
# Last updated: 1/19/2026, 10:44:38 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        sstack = []
4        hmap = {")":"(", "]":"[", "}":"{"}
5        for i in s:
6            if i == "(" or i == "[" or i == "{":
7                sstack.append(i)
8            elif i == ")" or i == "]" or i == "}":
9                if len(sstack) != 0:
10                    if sstack[-1] == hmap[i]:
11                        print(sstack[-1], hmap[i])
12                        sstack.pop()
13                    else:
14                        sstack.append(i)
15                else:
16                    print(sstack)
17                    sstack.append(i)
18        print(sstack)
19        if len(sstack) == 0:
20            return True
21        else:
22            return False
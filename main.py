import copy

memory = []

class Node:
    def __init__(self, w, h, d1, d2, d, l1, direction, total):
        self.w = w #weight
        self.h = h #hueristic
        self.d1 = d1 #current
        self.d2 = d2 #final
        self.d = d #depth
        self.l1 = l1 #current in array form
        self.direction = direction #list of moves in array
        self.total = total #total f(n) in array
    def calculate(self):
        l = []
        """
        print(self.d1)
        for x in range(4):
                print(self.l1[x])
        print("")
        """
        if self.d1[0][0] < 3:
            other = self.l1[self.d1[0][0]+1][self.d1[0][1]]
            temp = eff_heuristic(self.w, self.h, copy.deepcopy(self.d1), copy.deepcopy(self.d2), self.d, copy.deepcopy(self.l1)
                          , copy.deepcopy(self.direction), copy.deepcopy(self.total), other, "U")
            if temp.l1 not in memory:
                l.append(temp)
                memory.append(temp.l1)
            pass #+1 x Up
        if self.d1[0][1] < 3:
            other = self.l1[self.d1[0][0]][self.d1[0][1]+1]
            temp = eff_heuristic(self.w, self.h, copy.deepcopy(self.d1), copy.deepcopy(self.d2), self.d, copy.deepcopy(self.l1)
                          , copy.deepcopy(self.direction), copy.deepcopy(self.total), other, "L")
            if temp.l1 not in memory:
                l.append(temp)
                memory.append(temp.l1)
            pass #+1 y right
        if self.d1[0][0] > 0:
            other = self.l1[self.d1[0][0] - 1][self.d1[0][1]]
            temp = eff_heuristic(self.w, self.h, copy.deepcopy(self.d1), copy.deepcopy(self.d2), self.d, copy.deepcopy(self.l1)
                          , copy.deepcopy(self.direction), copy.deepcopy(self.total), other, "D")
            if temp.l1 not in memory:
                l.append(temp)
                memory.append(temp.l1)
            pass  #-1 x down
        if self.d1[0][1] > 0:
            other = self.l1[self.d1[0][0]][self.d1[0][1] - 1]
            temp = eff_heuristic(self.w, self.h, copy.deepcopy(self.d1), copy.deepcopy(self.d2), self.d, copy.deepcopy(self.l1)
                          , copy.deepcopy(self.direction), copy.deepcopy(self.total), other, "R")
            if temp.l1 not in memory:
                l.append(temp)
                memory.append(temp.l1)
        return l
    def get_value(self):
        return self.h
    def __lt__(self, other):
        return self.total[-1] > other.total[-1]


def eff_heuristic(w, h, d1, d2, d, l1, direction, total, other, which_direct): #num total
    other = int(other)
    zero = d1[0] #location of 0
    before = d1[other] #location of other num
    final = d2[other] #location of final num
    h+= max(abs(final[0] - zero[0]) , abs(final[1] - zero[1])) - max(abs(final[0] - before[0]) , abs(final[1] - before[1]))
    l1[zero[0]][zero[1]], l1[before[0]][before[1]] = l1[before[0]][before[1]], l1[zero[0]][zero[1]]
    d1[0], d1[other] = d1[other], d1[0]
    d += 1
    total.append(h * w + d)
    direction.append(which_direct)


    return Node(w, h, d1,d2,d,l1,direction,total)


num_node = 0
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open(input("Filename: "), "r")
    w = float(f.readline().split()[0])
    f.readline()
    x = 0
    l1 = []
    l2 = []
    d1 = {}
    d2 = {}
    repeated = {} #use l1
    while x<4:
        line = f.readline().split()
        l1.append(line)
        print(" ".join(line))
        for y in range(4):
            d1[int(line[y])] = (x, y)
        x+=1
    f.readline()
    x = 0
    h = 0
    while x<4:
        line = f.readline().split()
        for y in range(4):
            d2[int(line[y])] = (x, y)
            if int(line[y]) != 0:
                h+=max(abs(x - d1[int(line[y])][0]), abs(y - d1[int(line[y])][1]))
        l2.append(line)
        x+=1
    listy = [Node(w, h, d1, d2, 0, l1, [], [w*h])]
    memory.append(l1)
    print()
    num_node+=1
    while listy != None and h > 0:
        popped = listy.pop()
        holder = popped.calculate()
        for x in holder:
            listy.append(x)
            num_node+=1
        listy.sort()
        h = popped.h
    for x in popped.l1:
        print(" ".join(x))
    print()
    print(popped.w)
    print(popped.d)
    print(num_node)
    print(" ".join(popped.direction))
    for x in range(len(popped.total)):
        popped.total[x] = str(popped.total[x])
    print(" ".join(popped.total))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

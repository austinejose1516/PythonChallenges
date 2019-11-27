'''

Sam's house has an apple tree and an omnge tree that yield an abundance of frurt. In the diagram below, the red region denotes his house,
where rt is the start pow, and t is the endpoint The apple tree is to the left of his house, and the orange tree Is to its right.
Mu can assume the trees are located on a single poi. where Me apple tree is at p.n., and the orange tree Is at point

When a frurt falls from tree, it lands d unrs of diswnce from tree of origin along the dwias.
A negative value of d means the frurt fell d units to the tree's I., and a positive value of d means it falls d units to the tree's oght.
Gwen the value of d for m apples and On oranges, determine how many apples and oranges will fall on .m's house be.,
In the inclusive range [rt, t]p For exarnple, Sam's house Is between s w 7 and t w 10. The apple tree is located at w 4 and the orange at b w 12.
There are m w 3 apples and n w 3 oranges. Apples are thrown apples w [2,3, —4]. distance from a, and oranges w [3, —2, —4] units distance.
Addng ea. apple distance to the posmon of the tree, they land at [4 + 2,4 + 3, 4 + —4] w [6,7, 01. Oranges land at [12 + 3,12 + —2,12 + —4] w [15,10,4]
One apple and two oranges land in the Inclusive range 7 — 10 so we print
1
2

'''

st = [2, 3]
ab = [1, 5]
mn = [1, 1]
apples = [2]
oranges = [-2]

def appleorange(st, ab, apples, oranges):

    s = st[0]
    t = st[1]
    a = ab[0]
    b = ab[1]
    NoApple = 0
    NoOrange = 0
    newApplePosition = []
    newOrangePosition = []

    if a < s and b > t:

        for i in apples:
            newApplePosition.append(a+i)
        for j in oranges:
            newOrangePosition.append(b+j)
        for k in range(s, t+1):
            if k in newApplePosition:
                NoApple += 1
            if k in newOrangePosition:
                NoOrange += 1
    print(NoApple)
    print(NoOrange)

appleorange(st, ab, apples, oranges)


# Genius Code

def appleorange(st, ab, apples, oranges):

    s = st[0]
    t = st[1]
    a = ab[0]
    b = ab[1]

    print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))
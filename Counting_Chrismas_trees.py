def CountingTrees(Trees):
    n = len(Trees)
    decreasing = 0
    increasing = 0
    decreasingn = 0
    increasingn = 0
    for i in range(n-1):
        if i > i+1:
            decreasing +=1
            if decreasing > decreasingn:
                    decreasingn = decreasing
                    decreasing = 0

        if i < i+1:
            increasing +=1
            if increasing > increasingn:
                    increasingn = increasing
                    increasing = 0

    print(increasingn)
    print(decreasingn)

CountingTrees([1, 3, 4, 2,])

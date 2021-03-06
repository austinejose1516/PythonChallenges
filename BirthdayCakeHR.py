'''

You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.

For example, if your niece is turning  years old, and the cake will have  candles of height , , , , she will be able to blow out  candles successfully, since the tallest candles are of height  and there are  such candles.

Function Description

Complete the function birthdayCakeCandles in the editor below. It must return an integer representing the number of candles she can blow out.

birthdayCakeCandles has the following parameter(s):
ar: an array of integers representing candle heights

'''

# Solution

arr = [1, 2, 3, 4, 5, 4, 8, 8, 8]

def birthdaycake(arr):

    big = max(arr)
    val = 0

    for i in range(len(arr)):
        if arr[i] == big:
            val += 1
    print(val)

birthdaycake(arr)
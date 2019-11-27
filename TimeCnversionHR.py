'''

Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock. Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):
s: a string representing time in  hour format
Input Format

A single string  containing a time in -hour clock format (i.e.:  or ), where  and .
Constraints

All input times are valid

Output Format
Convert and print the given time in -hour format, where .

Sample Input 0
07:05:45PM

Sample Output 0
19:05:45

'''

# Solution

s = '02:45:54PM'

def timeconverter(s):
    result = 0

    if 'PM' in s:
        s = s.split(':', 3)
        s[2] = s[2].replace('PM', '')
        if '12' in s:
            s[0] = s[0].replace('12', '12')
        else:
            s[0] = int(s[0]) + 12
        result = '{}:{}:{}'.format(s[0], s[1], s[2])

    elif 'AM' in s:
        s = s.split(':', 3)
        s[2] = s[2].replace('AM', '')
        s[0] = s[0].replace('12', '00')
        result = '{}:{}:{}'.format(s[0], s[1], s[2])

    print(result)

timeconverter(s)
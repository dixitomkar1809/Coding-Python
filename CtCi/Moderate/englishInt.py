# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
English Int: Given any integer, print an English phrase that describes the integer (e.g., "One
Thousand, Two Hundred Thirty Four").
'''

smalls = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
bigs = ['', 'thousands', 'million', 'billion']
hundred = 'hundred',
negative = 'negative'

def solution(num):
    if num == 0:
        return smalls[0]
    elif num < 0:
        return negative + convertChunk(-1 * num)
    parts = []
    chunkCount = 0
    while num > 0:
        if (num % 1000 != 0):
            chunk = convertChunk(num % 1000) + " " + bigs[chunkCount]
            parts.insert(0, chunk)
            num = num // 1000
            chunkCount += 1
    return listToString(parts)
    

def convertChunk(number):
    parts = []
    if number >= 100:
        parts.append(smalls[number//100])
        parts.append('hundred')
        number %= 100
    if number >= 10 and number <= 19:
        parts.append(smalls[number])
    elif number >= 20:
        parts.append(tens[number//10])
        number %= 10
    if number >= 1 and number <= 9:
        parts.append(smalls[number])
    return listToString(parts)

def listToString(parts):
    output = ""
    for i in range(len(parts)):
        output += parts[i]
        output += " "
    return output

if __name__ == "__main__":
    print(solution(19323984))


        
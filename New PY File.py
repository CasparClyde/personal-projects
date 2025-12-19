import re
print("start---------------------------")
def rotation(S,d,V,count):
    S_0 = S
    if d == "R":
        R = +V
        diff_0 = 100 - S_0
    if d == "L":
        R = -V
        diff_0 = S_0
        if S_0 == 0:
            diff_0 = 100


    if abs(R) > diff_0:
        count += 1
        tot_rot = (abs(R)-diff_0) // 100
        count += tot_rot

        if R> 0:
            S = (R-diff_0) % 100
        if R< 0:
            S = 100 - (abs(R)-diff_0) % 100
        elif abs(diff_0+R) % 100 == 0:
            S = 0
    elif abs(R) == diff_0:
        count += 1
        S = 0
    elif abs(R) < abs(diff_0):
        S = S + R
    return S,count

count = 0
S = 50

with open("input.txt") as f:
    for line in f:
        line = line.strip()
        match = re.match(r"([A-Za-z]+)(\d+)", line)
        
        letters, number = match.groups()
        print(letters, number)
        S,count = rotation(S,str(letters),int(number),count)
'''list = ['R1000', 'L1000']

for item in list:
    match = re.match(r"([A-Za-z]+)(\d+)", str(item))
    letters, number = match.groups()
    print(letters, number)
    S,count = rotation(S,str(letters),int(number),count)'''
print("counts:",count)
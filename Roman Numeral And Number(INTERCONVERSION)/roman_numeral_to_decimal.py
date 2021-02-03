Roman=input()


# Making a dictionary which contains all the necessary roamn numerals
tallies={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

def Roman_Numeral_To_Decimal(romanNumeral):
    result=0
    for i in range(len(romanNumeral)-1):
        left=romanNumeral[i]
        right=romanNumeral[i+1]
        if left<right:
            result-=tallies[left]
        else:
            result+=tallies[left]

    result+=tallies[romanNumeral[-1]]
    
    return result

print(Roman_Numeral_To_Decimal(Roman))            


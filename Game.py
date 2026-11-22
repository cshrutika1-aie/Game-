def minion_game(s):
    vowels = "AEIOU"
    s1=list(s)
    n = len(s)
    total_s = n*(n+1)//2
    
    sum_kevin = sum(n-idx for idx,val in enumerate(s1) if val in vowels)
    
    sum_stuart = total_s - sum_kevin
    
    if sum_kevin > sum_stuart:
            print('Kevin won by the score ',sum_kevin)
    elif sum_kevin < sum_stuart:    
            print('Stuart won by the score ',sum_stuart)
    else:
            print("Draw between Kevin and Stuart")


## Main program

S = input("Input your alphabetic word to start playing the game : ").upper()
if S.isalpha():
    minion_game(S)
else:
    print('You entered non alphabetic character')

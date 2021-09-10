
# Consider an alternative version of Pig Latin—We don’t check to see if the first letter is a vowel,
# but, rather, we check to see if the word contains two different vowels. If it does, we don’t move the 
# first letter to the end. Because the word “wine” contains two different vowels (“i” and “e”), we’ll add “way”
# to the end of it, giv- ing us “wineway.” By contrast, the word “wind” contains only one vowel, so we would move the
# first letter to the end and add “ay,” rendering it “indway.” 
# How would you check for two different vowels in the word? (Hint: sets can come in handy here.)
def pig_latin(str):
    cnt=0
    for i in str:
        if i in 'aeiou':
            cnt+=1
    if cnt==2:
        return (f'{str}way')
    if cnt==1:
        return (f'{str[1:]}{str[0]}ay')


str = 'wind'
print(pig_latin(str))

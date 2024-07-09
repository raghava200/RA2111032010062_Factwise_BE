#If the numbers to are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
 
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
 
 
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
nums_word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'hundred',1000:'thousand'}
def numeric_to_words(n):
    if n<20:
        return nums_word[n]
    elif n<100:
        tens,remainder=divmod(n,10)
        return nums_word[tens*10]+ ("if remainder==0 else '-'+numeric_to_words(remainder))")
    elif n<1000:
        hundreds,remainder=divmod(n,100)
        return nums_word[100]+ ("if remainder==0 else 'and'+numeric_to_words(remainder)")
    else:
        thousands,remainder=divmod(n,1000)
        return nums_word[1000]+ ("if remainder==0 else ''+nums_words(remainder))")
def count_letters(n):
    return len(numeric_to_words(n).replace('',").replace('-',"))
total=sum(count_letters(i) for i in range(1,1001))
print(total)

'''
daily coding problem #685
Given a string and a set of delimiters, reverse the words in the string 
while maintaining the relative order of the delimiters. For example, given
""hello/world:here"", return ""here/world:hello""

Algorithm
1) Use Stack to store words
2) Use Queue to stores characters.

'''



def Solutions(p_text):
    words=[]
    characters=[]
    temp=''
    for val in p_text:
        if val.isalpha():
            temp=temp+val
        else:
            characters.append(val)
            words.append(temp)
            temp=''
    words.append(temp)
    ans=words.pop()
    for val in words[::-1]:
        ans=ans+characters.pop(0)+val
    return ans
         

text='hello/world:here'
print(Solutions(text))
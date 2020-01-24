str1 = "dhaka"
str2 = "barisal"
str3 = "khulna"


index=0
str4= str1[:index]+str1[index].upper()+ str1[index+1:]

str5 = f"{str4}-{str2}-{str3}"

print(str5)
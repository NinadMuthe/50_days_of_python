company = "Coding For All"

print(company)

#print length of the variable
print(len(company))

#print all letters of variable in upper case
print(company.upper())

#print all letters in lowercase
print(company.lower())

#convert first letter of sentence into upper case and reaining into lower case
print(company.capitalize())

#convert first letter of eache word into upper case and remainig into lower case
print(company.title())

#swap the case. if it is in originaly in upper case it convert into lower case and if it is in lower case then it cnvert into upper case
print(company.swapcase())

#slice the sentence from 0th index to 6th index, not including 6th index
print(company[0:6])

#write the index of first letter of word, if value is not found then written -1
print(company.find("Coding"))

#write the index of first letter of word, if value is nor found the give value error
print(company.index("Coding"))

#replace the word
print(company.replace("Coding","Python"))

#split the each word of sentence and make a list or array of words
print(company.split())

#split the string at comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

#print the character at index 0
print(company[0])

#print the last index of character
print(len(company)-1)

#print the character at 10th index, which is blank space
print(company[10])

#print acronym of the sentence
text = "Python For Everyone"
acronym=text[0]+text[7]+text[11]
print(acronym)

#print first appearance of index of caracter C
print(company.index("C"))

#print last appearance of index of caracter l
print(company.rfind("l"))

#print index of first appearance of word because
sentence = "You cannot end a sentence with because because because is a conjuction"
print(sentence.find("because"))

#find the last appearance of the because
print(sentence.rfind("because"))

#slice the sentence into because because because
start= sentence.find("because")
end= sentence.find("is") -1
print(sentence[start:end])

#to find the string company startwith word Coding
print(company.startswith("Coding"))

#to find the string company endswith word Coding
print(company.endswith("Coding"))

print("30DaysofPython".isidentifier())
print("thirty_days_of_python".isidentifier())
programming_languages = {"Python", "Java", "C++", "JavaScript"}
print(programming_languages)    
# Output: {'Java', 'C++', 'Python', 'JavaScript'}
# Creating a set of programming languages
print(type(programming_languages))
# Output: <class 'set'>
# Verifying the type of the set     

print(len(programming_languages))    
# Output: 4
# Getting the number of elements in the set 

programming_languages.add("Go")
print(programming_languages)    
# Output: {'Java', 'C++', 'Python', 'JavaScript', 'Go'}
# Adding a new language to the set  

programming_languages.remove("Java")
print(programming_languages)    
# Output: {'C++', 'Python', 'JavaScript', 'Go'}
# Removing a language from the set  

print("Python" in programming_languages)    
# Output: True
# Checking if 'Python' is in the set    

programming_languages.discard("Ruby")
print(programming_languages)    
# Output: {'C++', 'Python', 'JavaScript', 'Go'}
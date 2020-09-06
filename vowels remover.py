string = input("Enter any string: ")

if string == '':
    print("plz try again")
else:
    newstr = string;
    print("\nRemoving vowels from the given string");
    print()
    vowels = ('a', 'e', 'i', 'o', 'u');
    for x in string.lower():
        if x in vowels:
            newstr = newstr.replace(x,"");
    print("New string after removing the vowels: " + newstr  );

    

# caeser cipher
alphabet_list = [chr(i) for i in range(97, 123)]

def do():
    list = []
    # asking the user to choose decode or encode
    ask = input('type "encode" to encode and "decode" to decode:')

    # if user chooses encode this if statement will be executed
    if ask == "encode":
        word = input("write a word :")
        shift = int(input("type shift :"))

        for alphabet in word:
            list.append(alphabet)  

        for i in range(len(list)):
            for k in range(len(alphabet_list)):
               if list[i] == alphabet_list[k]:
                   list[i] = alphabet_list[(k + shift)%26]
                   break
           
    # if user chooses decode this if statement will be executed
    elif ask == "decode":
        word = input("write a word :")
        shift = int(input("type shift :"))

        for alphabet in word:
            list.append(alphabet)  

        for i in range(len(list)):
            for k in range(len(alphabet_list)):
               if list[i] == alphabet_list[k]:
                   list[i] = alphabet_list[(k - shift)%26]
                   break
    # telling the user not to provide any other word except "decode" or "encode"
    # and starting the function again
    else:
        print("provide a valid input")
        do()
    
    
    # converts a list of strings into a single string.
    word = "".join(list)             
    print(word) 

    # asking the user to run again or not
    ask = input("want to try again 'yes' or 'no':")
    if ask == "yes":
        do()
    else:
        print("bye bye") 

do()

   

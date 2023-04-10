import re
print('''
**********************************************
***** Welcome to the Mad Lips Game! *****
**********************************************
In this game, we will ask you for various words,
such as nouns, verbs, adjectives, and more.
Then, we will use your words to fill in the blanks
in a fun and silly story.
Get ready to laugh and have some fun!
''')
def read_template(path):
    try:
       example=open(path)
       return example.read()
    except FileNotFoundError as err:
        print('file is not found pls change the path !')
        print(err)


def parse_template(text):
    actual_stripped=''
    actual_parts=[]
    x=text.split(' ')
   
    reg=r"^{\w+}"  
    for i in x:
        
        if re.match(reg,i)==None :
            
            actual_stripped+=f"{i} " 
            
        else : 
            if i==x[-1]:
                actual_stripped+='{}.' 
                actual_parts+=[i[1:-2]] 
            else:
                actual_parts+=[i[1:-1]]  
                actual_stripped+='{} ' 
    
    actual_parts=tuple(actual_parts)
    return (actual_stripped,actual_parts)
    
 
def merge(text,tep): 
    return text.format(*tep)

def create_file(result ,file_to_write_on_it): #over write the file
    with open(file_to_write_on_it, "w") as f:
        f.write(result)
        
def start_game(file_toRead_game,file_toWrite_game):
    text = read_template(file_toRead_game)
    stripped_text, parts_tuple = parse_template(text)
    user_input = []
    
    for i in range(len(parts_tuple)):
        x = input('enter a {} > '.format(parts_tuple[i]))
        user_input.append(x)
    result = stripped_text.format(*user_input)
    print(f"Here is the result \n{result}")
    create_file(result,file_toWrite_game)

if __name__=="__main__":
    start_game("../assets/madlib.txt","../assets/result.txt")
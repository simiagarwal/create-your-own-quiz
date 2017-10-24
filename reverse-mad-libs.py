test_string1 = """A _1_ is created with the def keyword.You specify the inputs a _1_takes by adding _2_ separated """\
               """by commas between the parenthesis._1_s by default returns _3_ if you don't specify the value to return."""\
               """_2_ can be standard data types such as string,numbers,dictionary,tuple,and"""\
                """_4_ or can be more complicated such as objects and lambda functions."""

test_string2 ="""_1_ is a for-profit educational organization founded by Sebastian _3_, David Stavens, and """\
                 """  Mike Sokolsky offering massive open online _2_(MOOCs). According to _3_, the origin of the name """\
                 """_1_ comes from the company's desire to be "audacious for you, the student". While  it originally focused"""\
                 """on offering university-style _2_, it now focuses more on vocational _2_ for professionals. _1_ is the """\
                 """outgrowth of free computer science classes offered in 2011 through _4_ University."""

test_string3 ="""_1_ is the scientific and practical approach to _2_ and its applications. It is the systematic _4_of the feasibility, """\
               """structure,expression, and mechanization of the methodical procedures (or _3_) thatunderlie the acquisition, representation,"""\
               """processing, storage, communication of,and access to information. An alternate, more succinct definition of _1_ is the _4_of """\
               """automating algorithmic processes that scale. A computer scientist specializes in the theory of _2_ and the design of computational """\
               """systems.Despite its short history as a formal academic discipline, _1_ has made a number of fundamental contributions to science """\
               """and society.  3_ for performing computations have existed since antiquity, even before the development of sophisticated computing equipment."""\
                 """ The ancient Sanskrit treatise Shulba Sutras, or "Rules of the Chord", is a book of _3_ """




def fill_the_blanks(astring,blank,user_input):#returns the string with blanks filled with user_input
    return astring.replace(blank,user_input)


"""This function asks the user input for the specific blank and  if the answer is correct then returns
   the whole string with blanks filled for that number otherwise keep asking for the answer until its correct"""

def play_madlib(astring,correct_answer,blank,index):
    transformed_string = []
 
 
    user_input = raw_input("Type in the answer for blank %s:" %blank.strip("_"))
      # comparing for the right answer
    while(check_answer(user_input,correct_answer,index)!=1):
        print "try again"
        user_input = raw_input("Type in the answer for blank %s:" %blank.strip("_"))
    transformed_string.append(fill_the_blanks(astring,blank,user_input) )              
                            
    return "".join(transformed_string)
    

def check_answer(user_input, correct_answer,index):#checks for the correct answer with the user_input

   #correct_answer =["function","arguments","none","list"]

   if (user_input== correct_answer[index]):
      return 1
   else:
      return 0
  

def all_blanks_madlib(astring,correct_answer): # check for the each blank in the list

    num_blanks = ["_1_","_2_","_3_","_4_"]
    index =0
    while (index < len(num_blanks)):
        for blank in num_blanks:
#going through the loop to fill each blank 
            if blank in astring:
              astring = play_madlib(astring,correct_answer,blank,index)
              print astring
              index +=1
        
                
def reverse_mad_libs():
    """depending on the difficulty level the specific string is retuned """
    correct_answer1 =["function","arguments","none","list"]
    correct_answer2= ["Udacity","courses","Thrun","Stanford"]
    correct_answer3 = ["computer science","computation","algorithms","study"]


    user_input= raw_input("Choose your level of preferences- easy, medium or hard : ")
    if user_input == 'easy':#for easy level test_string1 is returned
        print test_string1
        return all_blanks_madlib(test_string1,correct_answer1)
    if user_input == 'medium':#for medium level test_string2 is returned
        print test_string2
        return  all_blanks_madlib(test_string2,correct_answer2)
    else:
        print test_string3#for hard level test_string3 is returned
        return  all_blanks_madlib(test_string3,correct_answer3)



print reverse_mad_libs()



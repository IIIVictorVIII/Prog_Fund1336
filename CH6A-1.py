#Victor Villarreal
#completed; 2/25/26

#program has two functions, main opens file in writing mode
#and writes contents. main2 opens file in reading mode, 
#reads first 3 lines and displays what was read as well as age and age/2


def main ():
   
#open file w variable: writing mode
   my_name_file = open ('My_Name','w' )


#write contents into newly made file
   my_name_file.write('Victor Villarreal\n')
   my_name_file.write('John Doe\n')
   my_name_file.write ('20')


   my_name_file.close ()

def main2 ():

#open file in reading mode
   my_name_file = open ('my_name','r')
  

#read 3 lines in file and half age
   name1= my_name_file.readline()   
   name2 = my_name_file.readline()
   age = int(my_name_file.readline())
  

#display what was read from the new file
   print(name1.rstrip('\n'))
   print(name2.rstrip('\n'))
   print(age)
   print(int(age/2))
   
   
   
   my_name_file.close

#call functions 
main()
main2()

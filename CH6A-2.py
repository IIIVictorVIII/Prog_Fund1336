#Victor Villarreal 
#incomplete
#

def main():
    
    infile= open('number_list', 'w')
    
    for counts in range (50,101):
        infile.write (str(counts) +'\n')

    infile.close

def read():

    read_file = open ('number_list', 'r')  
    
    line = read_file.readline()

    for line in read_file:
        line = int(line)
        print (line)

        read_file.close  

main ()
read ()
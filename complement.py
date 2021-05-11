#complemet program
#Kanako Kato
#Last updated 5/11/21

def complement_program(dna):
    '''This program will take any dna sequence and return complemt sequence'''
    complement_base={'A':'T', 'C':'G', 'T':'A', 'G':'C'}
    seq=''#set an empty string
    for base in dna:
        seq += complement_base[base]#new complemet sequence is added to the seq
    return seq[::-1]# complemet 3' to 5' 

#main program
DNA='CCGGAAGAATGGATATTACTTAG'
print(complement_program(DNA) )

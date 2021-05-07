#Sequence (FAFSA file) is outputed with a number of each base count. 

my_file=open("file.txt",'r')
header=my_file.readline()
seq=''
for line in my_file:
    mod_line= line.rstrip('\n').upper()
    seq=seq+mod_line
a_count=seq.count('A')
t_count=seq.count('T')
c_count=seq.count('C')
g_count=seq.count('G')

print('A count is', a_count)
print('T count is', t_count)
print('C count is', c_count)
print('G count is', g_count)

#This function will return GC content of a sequence and writes it to a file.
def gc_content(dna, file_object):
    g=dna.count("G")
    c=dna.count("C")
    gc=(g+c)/len(dna)*100
    print(gc)
    file_object.write(str(gc))
# Main part 
my_file.open=("gc_file.txt",'w')
gc_content(seq, my_file)
my_file.close


#In this part, tri nucleotide is coutned with a dictionary output. 
tri_list=[]
for num in range(0,len(seq)-2,3):
    tri=seq[num:num+3]
    tri_list.append(tri)
print(tri_list)
tri_dict={}
for combination in tri_list:
    if combination in tri_dict:

my_file.close()

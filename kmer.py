

def find_kmers(sequence, kmersize):# for example seq='ATCGG' kmersize=3
    kmers = []
    kmernum= len(sequence) - kmersize + 1 # kmernum= 5-3+1=3

    for i in range(kmernum):#range(3)
        kmer = sequence[i:i + kmersize] #seq[0:3], seq[1:4]...etc
        kmers.append(kmer)

    return kmers



Seq='ATGATGATGGT'
print(find_kmers(Seq,3))

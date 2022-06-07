def read_fasta(filename):
    # Read in Lines
    f = open(filename, "r")
    Lines = f.readlines()
    seqs = [""]
    i = -1
    for line in Lines:
        if len(line) < 10:
            continue
        if ">" in line:
            i += 1
            seqs.append("")
            continue
        else:
            line = line.strip('\n')
            line = line.strip(' ')
            seqs[i] += line
    
    # Make Same Length
    min_len = 999999999
    min_index = 0
    for j in range(0, len(seqs)):            
        if (len(seqs[j]) < min_len and len(seqs[j]) != 0): 
            min_len = len(seqs[j])
            min_index = j
    for j in range(0, len(seqs)):
        s = seqs[j]
        if (len(seqs[j]) < 10): 
            del seqs[j]
            break
        seqs[j] = s[0:len(seqs[min_index])] # make len of shortest
        # print(j, " ", len(seqs[j]),"\n", seqs[j], "\n")
        
    return len(seqs[min_index]), seqs

def main():
    filename = "files/fancyname.txt"
    length_of_shorter_seq, seqs = read_fasta(filename)

    shared = 0
    different = 0    

    for j in range(1, len(seqs)):
        for i in range(length_of_shorter_seq):
            if seqs[0][i] == seqs[j][i]:
                shared += 1
            else:
                different +=1

        sequence_identity = shared/length_of_shorter_seq
        print(f"There were {shared} shared nucleotides and {different} different nucleotides among the sequences")
        print(f"Sequence identity: {round(sequence_identity,2)}")    
        sequence_identity = shared = different = 0


main()
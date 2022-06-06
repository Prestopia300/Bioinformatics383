# sequences = {"seq1":"ATGCTGGGTACGATCGTACGTACGTACG","seq2":"ATCGCGGGGCTATATCTGGATTTTTAAACGGATCG","seq3":"ATCGACGATCGTACGATCGTACGGGGGGGGTACTAT"}

# output_path = 'test_fasta_file.txt'
# output_file = open(output_path,'w')

# for seq_id, seq in sequences.items():
#     identifier_line = ">" + seq_id + "\n"
#     output_file.write(identifier_line)
#     sequence_line = seq + "\n"
#     output_file.write(sequence_line)
    
# #Close the file when we're done
# output_file.close()

import os

def combine():
    # for file in dir
    # read its info
    # write its info to x.fasta
    # PUT A LOG IN THE POT (hehehehahahahohoho)

    output_path = 'files/don_cheedle.fasta'
    output_file = open(output_path,'w')

    directory = 'files'

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            # print(f)
            f = open(f)
            output_file.write(f.read())

combine()
# f = open(input_file)

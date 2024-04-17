from Bio import Entrez
from Bio import SeqIO

def get_sequence():
    Entrez.email = "gnbuckle@idrisoncology.com"
    handle = Entrez.efetch(db="nucleotide", id="J02459", rettype="fasta")
    sequence = handle.read()
    handle.close()
    newline_index = sequence.find("\n")
    sequence = sequence[newline_index + 1:]
    return sequence

def find_similar_sequences(dna_sequence, target_length, min_differences, max_differences):
    sequence_length = len(dna_sequence)
    for i in range(len(dna_sequence) - target_length + 1):

        seq1 = dna_sequence[i:i + target_length]
        for j in range(i + 1, len(dna_sequence) - target_length + 1):
            seq2 = dna_sequence[j:j + target_length]
            # Calculate Hamming distance using zip and sum with generator expression
            distance = sum(a != b for a, b in zip(seq1, seq2))
            if min_differences <= distance <= max_differences:
                print(f"Found similar sequences: ({seq1}, {seq2})")  # Print immediately
    return None

target_length = int(input("Enter the specific length of similar sequences to find: "))
min_differences = int(input("Enter the minimum number of allowed differences: "))
max_differences = int(input("Enter the maximum number of allowed differences: "))

sequence = get_sequence()


# Find similar sequences
similar_sequences = find_similar_sequences(sequence, target_length, min_differences, max_differences)

# Print results
if similar_sequences:
    print("Found similar sequence pairs:")
    for pair in similar_sequences:
        print(f"Sequence 1: {pair[0]}, Sequence 2: {pair[1]}")
else:
    print("No sequence pairs found with the specified criteria.")
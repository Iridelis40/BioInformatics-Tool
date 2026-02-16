def count_nuc(seq):
    #Count nucleotides in a DNA strand
    nucleotides = {
        "A":0,
        "C":0,
        "G":0,
        "T":0
    }
    for nuc in seq:
        nucleotides[f"{nuc}"]+=1
    return f"{nucleotides}"

def reverse_complement(seq):
    #Retrieve de reverse complement of a DNA strand
    rev = []
    for nuc in seq:
        rev.insert(0, nuc)
    complements = {"A":"T","T":"A","C":"G","G":"C"}
    complementary = []
    for i in rev:
        complementary.append(complements[i])
    return "".join(complementary)

def GC_content(seq):
    #Calculate GC content in a DNA sequence
    GC = 0
    for nuc in seq:
        if nuc in ["G","C"]: GC+=1
    return round((GC/len(seq)*100),3)

def read_fasta():
    #Read a FASTA format and return a dictionary where each element represents an ID (key) with it's string (value)
    with open("fasta.txt", encoding="utf-8") as fasta:
        content = fasta.read().replace("\n","")
        content_list = content.split(">")
        content_list.pop(0)
        content_dict = {}
        for x in content_list:
            content_dict[f"{x[:13]}"] = f"{x[13:]}"
        return content_dict

def GC_content_FASTA(fasta_dict):
    #Return the sequence with the highest GC content from a fasta formatted dictionary
    for x in fasta_dict: 
        fasta_dict[x] = GC_content(fasta_dict[x])
    GC_list = list(fasta_dict.values())
    GC_list.sort(reverse=True)
    for key, value in fasta_dict.items():
        if value == GC_list[0]:
            return f"{key}\n{value}"
    
def Humming_distance(seq1, seq2):
    #Return Humming distance (count point mutations between two strands of equal length)
    distance = 0
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]: distance += 1
    return distance
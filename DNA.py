def count_nuc(seq):
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
    rev = []
    for nuc in seq:
        rev.insert(0, nuc)
    complements = {"A":"T","T":"A","C":"G","G":"C"}
    complementary = []
    for i in rev:
        complementary.append(complements[i])
    return "".join(complementary)

def GC_content(seq):
    GC = 0
    for nuc in seq:
        if nuc in ["G","C"]: GC+=1
    return GC/len(seq)*100

def read_fasta():
    with open("fasta.txt", encoding="utf-8") as fasta:
        content = fasta.read()
        return content
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
def read_seq(inputfile):
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n","")
    seq = seq.replace("\r","")
    return seq
    
def translate(seq):
    table = {'ATA':'I', 'CCG':'T', 'CCC':'R', ...}
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i+3]
            protein += table[codon]
            
    return protein
    
prt = read_seq("protein.txt")
dna = read_seq("dna.txt")

translate(dna[20:235]) == prt
translate(dna[20:238])[:-1] == prt
# both should return True

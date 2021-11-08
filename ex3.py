
dna = input("Enter a DNA strand :  ")    

def rna(dna):
    dna = dna.upper()
    rna = {"A": "U", "T": "A", "C": "G", "G": "C"}
    for o, r in rna.items():
        dna = dna.replace(o, r)
    print("RNA transcoding : "+ dna)

rna(dna)
def to_rna(dna_strand):
    if dna_strand == 'C':
        return dna_strand.replace('C','G')
    if dna_strand == 'G':
        return dna_strand.replace('G','C')
    if dna_strand == 'T':
        return dna_strand.replace('T','A')
    if dna_strand == 'A':
        return dna_strand.replace('A','U')
    else:
        rna_strand =""
        dic = {'C':'G','G':'C','T':'A','A':'U'}
        for character in dna_strand:
            for i,j in dic.items():
                if character == i:
                    rna_strand+=j
        return rna_strand
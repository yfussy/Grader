nucleotides = ['A', 'T', 'G', 'C']
dna = input().strip().upper()
valid = True

for n in dna:
    if n not in nucleotides:
        valid = False

if valid:
    match input():
        case 'R':
            rna = ''
            for n in dna:
                rna += nucleotides[abs((nucleotides.index(n)%2) - 1) + (nucleotides.index(n)//2)*2]
            print(rna[::-1])
        case 'F':
            nucleotidesCount = [[x, 0] for x in nucleotides]
            for n in dna:
                for nucleotide in nucleotidesCount:
                    if n == nucleotide[0]:
                        nucleotide[1] += 1
                        break
            nucleotidesCount = [f'{x[0]}={x[1]}' for x in nucleotidesCount]
            print(', '.join(nucleotidesCount))
        case 'D':
            pair = input()
            d = 0
            for i in range(len(dna) - 1):
                dnaPair = dna[i:i+2]
                if dnaPair == pair:
                    d += 1
            print(d)
else:
    print("Invalid DNA")
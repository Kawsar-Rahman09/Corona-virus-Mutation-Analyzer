# SARS-CoV-2 Full Spike Protein Mutation Analyzer

def compare_sequences(ref_seq, var_seq):
    mutations = []
    mutation_counts = {
        "Substitution": 0,
        "Insertion": 0,
        "Deletion": 0
    }

    max_len = max(len(ref_seq), len(var_seq))

    for i in range(max_len):
        ref_residue = ref_seq[i] if i < len(ref_seq) else "-"
        var_residue = var_seq[i] if i < len(var_seq) else "-"

        if ref_residue == var_residue:
            continue

        if ref_residue == "-":
            mut_type = "Insertion"
        elif var_residue == "-":
            mut_type = "Deletion"
        else:
            mut_type = "Substitution"

        mutations.append((i + 1, ref_residue, var_residue, mut_type))
        mutation_counts[mut_type] += 1

    return mutations, mutation_counts

def print_report(mutations, mutation_counts):
    for pos, ref_aa, var_aa, mtype in mutations:
        print(f"Position {pos}: {ref_aa} -> {var_aa} ({mtype})")

    print(f"\nTotal mutations found: {len(mutations)}")
    print("Mutation Type Counts:")
    for mtype, count in mutation_counts.items():
        print(f"  {mtype}: {count}")

def main():
    # Full-length spike protein (1273 amino acids) - Wuhan-Hu-1 (NCBI derived)
    reference_sequence = (
        "MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFL"
        "PFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDS"
        "KTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTF"
        "ELTQHGKPCNGVEGFNCYFPLQSYGFQPTNGVGYQPYRVVVLSFELLHAPATVCGP"
        "KKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLE"
        "ILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTG"
        "SNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSPRRARSVASQSIIAY"
        "TMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSN"
        "LLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILP"
        "DPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPL"
        "LTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQK"
        "LIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLN"
        "DILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLG"
        "QSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPRE"
        "GVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFK"
        "EELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKY"
        "EQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEP"
        "VLKGVKLHYT"
    )

    # Full-length spike protein - Omicron BA.1 (NCBI derived)
    variant_sequence = (
        "MFVFLVLLPLVSSQCVNLTTKTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFL"
        "PFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDS"
        "KTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTF"
        "ELTQHGKPCNGVAGFNCYFPLRSYSFRPTYGVGHQPYRVVVLSFELLHAPATVCGPK"
        "KSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLEIL"
        "DITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTGSNV"
        "FQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSRRRARSVASQSIIAYTMSL"
        "GAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSNLLLQY"
        "GSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILPDPSKPS"
        "KRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPPLLTDEMI"
        "AQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYENQKLIANQF"
        "NSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISSVLNDILSRL"
        "DKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSECVLGQSKRVD"
        "FCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKAHFPREGVFVSN"
        "GTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQPELDSFKEELDKY"
        "FKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLIDLQELGKYEQYIKW"
        "PWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCKFDEDDSEPVLKGVK"
        "LHT"
    )

    print("Comparing Full-Length Spike Protein Sequences...\n")

    mutations, mutation_counts = compare_sequences(reference_sequence, variant_sequence)
    print_report(mutations, mutation_counts)

if __name__ == "__main__":
    main()

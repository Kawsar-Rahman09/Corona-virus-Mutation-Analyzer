# SARS-CoV-2 Spike Protein Mutation Analyzer
def compare_sequences(ref_seq, var_seq):
    mutations = []
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

    return mutations

def print_report(mutations):
    for pos, ref_aa, var_aa, mtype in mutations:
        print(f"Position {pos}: {ref_aa} -> {var_aa} ({mtype})")
    print(f"\nTotal mutations found: {len(mutations)}")

def main():
    # First 60 amino acids of spike protein from Wuhan reference strain
    reference_sequence = (
        "MFVFLVLLPLVSSQCVNLTTRTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFL"
    )

    # First 60 amino acids of Omicron BA.1 variant (real substitutions highlighted)
    variant_sequence = (
        "MFVFLVLLPLVSSQCVNLTTKTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFL"
    )

    print("Reference (Wuhan) Spike Fragment:")
    print(reference_sequence)
    print("\nVariant (Omicron BA.1) Spike Fragment:")
    print(variant_sequence)
    print("\nComparing...\n")

    mutations = compare_sequences(reference_sequence, variant_sequence)
    print_report(mutations)

if __name__ == "__main__":
    main()

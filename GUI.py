import tkinter as tk
from tkinter import messagebox, scrolledtext
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

# GUI logic
def run_comparison():
    mutations, mutation_counts = compare_sequences(reference_sequence, variant_sequence)

    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, "Mutation Details:\n\n")

    for pos, ref_aa, var_aa, mtype in mutations:
        result_box.insert(tk.END, f"Position {pos}: {ref_aa} → {var_aa} ({mtype})\n")
    result_box.insert(tk.END, f"\nTotal mutations: {len(mutations)}\n")
    result_box.insert(tk.END, "Mutation Type Counts:\n")
    for mtype, count in mutation_counts.items():
        result_box.insert(tk.END, f"  {mtype}: {count}\n")

root = tk.Tk()
root.title("SARS-CoV-2 Spike Protein Mutation Analyzer")
root.geometry("700x600")

title = tk.Label(root, text="SARS-CoV-2 Spike Protein Mutation Analyzer", font=("Arial", 16, "bold"))
title.pack(pady=10)

compare_btn = tk.Button(root, text="Compare Sequences", command=run_comparison, font=("Arial", 12))
compare_btn.pack(pady=10)

result_box = scrolledtext.ScrolledText(root, width=80, height=25, font=("Courier", 10))
result_box.pack(pady=10)

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
    "DPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPP"
    "LLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYEN"
    "QKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISS"
    "VLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSE"
    "CVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKA"
    "HFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQP"
    "ELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLID"
    "LQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCK"
    "FDEDDSEPVLKGVKLHYT"
)

variant_sequence = (
    "MFVFLVLLPLVSSQCVNLTTKTQLPPAYTNSFTRGVYYPDKVFRSSVLHSTQDLFL"
    "PFFSNVTWFHAIHVSGTNGTKRFDNPVLPFNDGVYFASTEKSNIIRGWIFGTTLDS"
    "KTQSLLIVNNATNVVIKVCEFQFCNDPFLGVYYHKNNKSWMESEFRVYSSANNCTF"
    "ELTQHGKPCNGVAGFNCYFPLRSYSFRPTYGVGHQPYRVVVLSFELLHAPATVCGP"
    "KKSTNLVKNKCVNFNFNGLTGTGVLTESNKKFLPFQQFGRDIADTTDAVRDPQTLE"
    "ILDITPCSFGGVSVITPGTNTSNQVAVLYQDVNCTEVPVAIHADQLTPTWRVYSTG"
    "SNVFQTRAGCLIGAEHVNNSYECDIPIGAGICASYQTQTNSRRRARSVASQSIIAY"
    "TMSLGAENSVAYSNNSIAIPTNFTISVTTEILPVSMTKTSVDCTMYICGDSTECSN"
    "LLLQYGSFCTQLNRALTGIAVEQDKNTQEVFAQVKQIYKTPPIKDFGGFNFSQILP"
    "DPSKPSKRSFIEDLLFNKVTLADAGFIKQYGDCLGDIAARDLICAQKFNGLTVLPP"
    "LLTDEMIAQYTSALLAGTITSGWTFGAGAALQIPFAMQMAYRFNGIGVTQNVLYEN"
    "QKLIANQFNSAIGKIQDSLSSTASALGKLQDVVNQNAQALNTLVKQLSSNFGAISS"
    "VLNDILSRLDKVEAEVQIDRLITGRLQSLQTYVTQQLIRAAEIRASANLAATKMSE"
    "CVLGQSKRVDFCGKGYHLMSFPQSAPHGVVFLHVTYVPAQEKNFTTAPAICHDGKA"
    "HFPREGVFVSNGTHWFVTQRNFYEPQIITTDNTFVSGNCDVVIGIVNNTVYDPLQP"
    "ELDSFKEELDKYFKNHTSPDVDLGDISGINASVVNIQKEIDRLNEVAKNLNESLID"
    "LQELGKYEQYIKWPWYIWLGFIAGLIAIVMVTIMLCCMTSCCSCLKGCCSCGSCCK"
    "FDEDDSEPVLKGVKLHT"
)

root.mainloop()

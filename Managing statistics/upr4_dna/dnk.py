from Bio import SeqIO
from Bio.Seq import Seq
import matplotlib.pyplot as plt
import math

def calculate_percentages(dna):
    length = len(dna)
    counts = {
        "A": dna.count("A"),
        "T": dna.count("T"),
        "G": dna.count("G"),
        "C": dna.count("C")
    }
    percentages = {base: (count / length) * 100 if length > 0 else 0
                   for base, count in counts.items()}
    return percentages

def plot_sequences_all(seq_percentages, seq_ids):
    n = len(seq_percentages)
    cols = min(3, n)                      # max 3 columns
    rows = math.ceil(n / cols)

    fig, axes = plt.subplots(rows, cols,
                             figsize=(5 * cols, 4 * rows),
                             constrained_layout=True)

    # Always work with a flat list of axes
    axes_flat = [axes] if n == 1 else list(axes.flat)

    colors = ['green', 'red', 'blue', 'orange']

    for i, (perc, seq_id) in enumerate(zip(seq_percentages, seq_ids)):
        ax = axes_flat[i]
        ax.bar(perc.keys(), perc.values(), color=colors)
        ax.set_ylim(0, 100)
        ax.set_ylabel('Percentage (%)')
        ax.set_title(f'{seq_id}', fontsize=9)
        ax.tick_params(axis='x', labelsize=9)

    # Hide any unused subplot slots
    for j in range(n, len(axes_flat)):
        axes_flat[j].set_visible(False)

    fig.suptitle('Nucleotide Composition', fontsize=13, fontweight='bold')
    plt.show()

def search_sequence_in_fasta(file_path, target_seq):
    target = Seq(target_seq)
    complement = target.complement()

    print(f"Търсена последователност: {target}")
    print(f"Комплементарна: {complement}")

    seq_percentages = []
    seq_ids = []

    for record in SeqIO.parse(file_path, "fasta"):
        dna = record.seq
        print(f"\nСеквенция: {record.id}")
        pos1 = dna.find(target)
        pos2 = dna.find(complement)

        if pos1 != -1:
            print(f"Намерена (оригинал) на позиция: {pos1}")
        if pos2 != -1:
            print(f"Намерена (комплементарна) на позиция: {pos2}")
        if pos1 == -1 and pos2 == -1:
            print("Няма съвпадение")

        perc = calculate_percentages(str(dna))
        print("\nПроцентно съдържание:")
        for base, p in perc.items():
            print(f"{base}: {p:.2f}%")

        seq_percentages.append(perc)
        seq_ids.append(record.id)

    plot_sequences_all(seq_percentages, seq_ids)

file_path = r"C:\Uni\СМОИ\upr4_dna\malaria_dna.fna"
target_sequence = "AGCTTTTGCA"

search_sequence_in_fasta(file_path, target_sequence)
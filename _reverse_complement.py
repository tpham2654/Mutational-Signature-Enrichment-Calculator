def _reverse_complement(dna_seq_in):
	dna_complement = ""
	complement_pair = {"A":"T",
	"G":"C",
	"T":"A",
	"C":"G"}
	for nt in dna_seq_in:
		dna_complement = dna_complement + complement_pair[nt]
	return str(dna_complement[::-1]) #reversed
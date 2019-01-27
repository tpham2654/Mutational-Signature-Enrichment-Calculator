import pandas as pd

def _reverse_complement(dna_seq_in):
	dna_complement = ""
	complement_pair = {"A":"T",
	"G":"C",
	"T":"A",
	"C":"G"}
	for nt in dna_seq_in:
		dna_complement = dna_complement + complement_pair[nt]
	return str(dna_complement[::-1]) #reversed

def _make_mutation_dict_key(change,sthreebefore):
	#changes COSMIC formatted mutation description to dictionary key format this program uses.
	arr_nucleotidechange = change.split(">")
	nucleotide_before = arr_nucleotidechange[0]
	nucleotide_after = arr_nucleotidechange[1]
	arr_three_nt_before = [s for s in sthreebefore]
	arr_three_nt_after = [s for s in arr_three_nt_before]
	if arr_three_nt_before[1] == nucleotide_before:
		arr_three_nt_after[1] = nucleotide_after
		return str("".join(arr_three_nt_before)) + " ==> " + str("".join(arr_three_nt_after))
	return False

def _make_reverse_complement_mutation_dict_key(dictkeyin):
	arr_dictkey = dictkeyin.split(" ==> ")
	three_nt_before = _reverse_complement(arr_dictkey[0].strip())
	three_nt_after = _reverse_complement(arr_dictkey[1].strip())
	return three_nt_before + " ==> " + three_nt_after
	

def _load_cosmic_mutation_signature_by_number(signum,doreversecomplement=True):
	mutation_sigs_df = pd.read_table('signatures_probabilities.txt') #file comes from COSMIC.
	mutsig_dictout = {}
	for i,r in mutation_sigs_df.iterrows():
		mutsig_dictkey = _make_mutation_dict_key(r["Substitution Type"],r["Trinucleotide"])
		revcomplement_dictkey = _make_reverse_complement_mutation_dict_key(mutsig_dictkey)
		if mutsig_dictkey != False:
			mutsig_dictout[mutsig_dictkey] = r["Signature " + str(signum)]
			#reverse complement of described mutation is treated the same as original.
			if doreversecomplement==True:
				mutsig_dictout[revcomplement_dictkey] = r["Signature " + str(signum)] 
	return mutsig_dictout
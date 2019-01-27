import pandas as pd
from _make_mutation_dict_key import _make_mutation_dict_key
from _make_reverse_complement_mutation_dict_key import _make_reverse_complement_mutation_dict_key
from _reverse_complement import _reverse_complement

def _load_cosmic_mutation_signature_by_number(cosmic_mutation_signature_number,use_reverse_complements=True):
	mutation_sigs_df = pd.read_table('./data/signatures_probabilities.txt') #file comes from COSMIC.
	mutsig_dictout = {}
	for i,r in mutation_sigs_df.iterrows():
		mutsig_dictkey = _make_mutation_dict_key(r["Substitution Type"],r["Trinucleotide"])
		revcomplement_dictkey = _make_reverse_complement_mutation_dict_key(mutsig_dictkey)
		if mutsig_dictkey != False:
			mutsig_dictout[mutsig_dictkey] = r["Signature " + str(cosmic_mutation_signature_number)]
			#reverse complement of described mutation is treated the same as original.
			if use_reverse_complements==True:
				mutsig_dictout[revcomplement_dictkey] = r["Signature " + str(cosmic_mutation_signature_number)] 
	return mutsig_dictout
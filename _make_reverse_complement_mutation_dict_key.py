from _reverse_complement import _reverse_complement
def _make_reverse_complement_mutation_dict_key(dictkeyin):
	arr_dictkey = dictkeyin.split(" ==> ")
	three_nt_before = _reverse_complement(arr_dictkey[0].strip())
	three_nt_after = _reverse_complement(arr_dictkey[1].strip())
	return three_nt_before + " ==> " + three_nt_after
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
from compute_mutational_signature_enrichment import compute_mutational_signature_enrichment
import pandas as pd
from os import listdir
from os.path import isfile, join

reference_file_path = "" #your reference GrCh37.75 fasta path here.  Don't forget to index the file!
maf_path = "./TCGA_test"
mutation_file_paths = [join(maf_path,f) for f in listdir(maf_path) if isfile(join(maf_path, f))]
lst_MSE_dfs = []

for sig_num in [0,2,13]:
	MSE_output = compute_mutational_signature_enrichment(mutation_file_paths,reference_file_path,cosmic_mutation_signature_number=sig_num)
	signature_name = "Signature {}".format(sig_num)
	if sig_num==0:
		signature_name = "AMSE"
	lst_MSE_dfs.append(MSE_output.T["Mutational Signature Enrichment"].to_frame().rename(columns={"Mutational Signature Enrichment":signature_name}))
pd.concat(lst_MSE_dfs, axis=1).to_csv("test_MSE.csv")
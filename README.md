# Mutational Signature Enrichment (MSE) Calculator

This is the code for the Mutation Signature Enrichment calculating tool used in these publications:
- [Boichard, Pham, et. al APOBEC-related mutagenesis and neo-peptide hydrophobicity: implications for response to immunotherapy](https://www.tandfonline.com/doi/full/10.1080/2162402X.2018.1550341)
- Pham, Boichard, et. al Role of Ultra-Violet Mutational Signature versus Tumor Mutation Burden in Predicting Response to Immunotherapy (manuscript)


It is UCSD CCAL's implementation of the PMAC-D metric from [Roberts, et. al An APOBEC Cytidine Deaminase Mutagenesis Pattern is Widespread in Human Cancers](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3789062/), called AMSE (APOBEC Mutational Signature Enrichment) in the APOBEC paper above, used to measure the degree of APOBEC mutagenesis from a list of mutations called in a sample.  PMAC-D counted the following nucleotide changes and their reverse complements, weighted equally:

- TCA ==> TGA
- TCA ==> TTA
- TCT ==> TGT
- TCT ==> TTT

In addition to the PMAC-D signature definition included by default, it has also been generalized to calculate the MSE statistic based on probabilities for each of the 96 trinucleotide switches as defined by [Alexandrov, et. al](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3776390/) and available on the [COSMIC Mutational Signatures page](https://cancer.sanger.ac.uk/cosmic/signatures).  These mutation signature probabilities are defined in the tab-delimited file "signatures_probabilities.txt" in the "data" directory.

# Usage
The code accepts called mutations in MAF files, with the same column order as found on TCGA, or VCF files as inputs.  
```
from compute_mutational_signature_enrichment import compute_mutational_signature_enrichment

mutation_file_paths = ["./data/TCGA-",]

compute_mutational_signature_enrichment(
    mutation_file_paths, #list of called mutation file paths in MAF or VCF format, 1 file per sample
    reference_file_path, #reference genome FASTA, must be the same as the one used to call the mutations in the mutation_file_paths
	cosmic_mutation_signature_number=0 #Default 0 uses the defined PMAC-D weights, any number from 1-30, inclusive corresponding to the Alexandrov signatures can be used. 
	)

```

The output is a pandas dataframe where the columns are sample file names and the rows are information related to the calculation for a particular sample.  The signature MSE score is in the row "Mutational Signature Enrichment".  

This code should work on any computer that can run Python 3.  
### Dependencies:
- pandas
- pyfaidx (don't forget to index reference FASTA file)
- pprint

## Example output of 5 TCGA tumors using APOBEC Signatures PMAC-D/AMSE, Signature 2, and Signature 13:

| Sample | AMSE | Signature 2 | Signature 13 |
|--------|------|-------------|--------------|
|TCGA-44-7661.maf|2.5153333995826297|1.696616476895444|2.122606877977259|
|TCGA-CQ-7068.maf|2.5070760447035956|1.7943464758950072|2.628330781579929|
|TCGA-DD-A73G.maf|0.9325034978530419|0.7367417842643569|1.1181360888995775|
|TCGA-FF-A7CX.maf|0.6527777777777777|0.7307526870927789|0.5969015874220198|

The ENSEMBL GRCh37 full genome DNA reference (ftp://ftp.ensembl.org/pub/grch37/current/fasta/homo_sapiens/dna/Homo_sapiens.GRCh37.dna.primary_assembly.fa.gz), which was used to call the TCGA mutations, was used.
Please see the [TCGA_test folder](/TCGA_test/) for the exact TCGA MAF files used to generate this table.  The script [TCGA_test.py](/TCGA_test.py) can be used to generate the above table.

## Comparison with PMAC-D on Pan-Cancer TCGA Data:
![PMAC-D vs AMSE graph](/images/PMAC-D_AMSE.png)

# Info
This repository is intended to be a partial fork of the files from the UCSD [CCAL Computational Cancer Analysis Library](https://github.com/KwatME/ccal) required to calculate MSE values, generalized to work on any mutational signature. 

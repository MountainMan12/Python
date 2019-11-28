# 1. INSTRUCTIONS
Kindly read these instructions before running the code in Python.
There is an input file provided with the python code that contains the gene sequences for Saccharomyces Cerevisiae.

The user will be prompted to enter the name of the file during execution.
Enter filename as: sequence.txt

The user will be prompted to enter a number which signifies per how many codons does the user wish to calculate codon bias.
The value used in the url http://www.kazusa.or.jp/codon/cgi-bin/showcodon.cgi?species=4932 is: 1000
Most online tools will calculate these values per 1000 codons.

After the table is generated the user can view the codon bias followed by codon preference values.
To confirm the results, the user can refer to online tools

Link to online SMS tool: [http://www.bioinformatics.org/sms2/codon_usage.html](SMS Tool)

## 1.1 ABOUT THE DATA

The data was downloaded from the Refseq database in NCBI.
url: https://www.ncbi.nlm.nih.gov/nuccore

The latest sequence data consists of 16 chromosomes and chromosome sequences were subsequently updated independently numerous times before the recent major genome update. All strains are derived from S288C.

The data used in the program is the complete nucleotide record of CDS of Saccharomyces cerevisiae.

For more information on the genome refer the url [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3962479/](*S. Cerevisiae*)

Note: There will be a slight variation in the first decimal place of the values as the data used was updated after the generation of table in the link mentioned.

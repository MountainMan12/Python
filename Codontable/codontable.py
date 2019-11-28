#Program to generate a codon usage table using Saccharomyces Cerevisiae genome
#AUTHOR: Pawan Verma

#Using FASTA file to read sequence
seq = raw_input('Enter the filename: ')
fh = open(seq, 'r')
line = fh.readline()
meta = ''
sequence = ''
while line:
	line = line.rstrip('\n') #removing newline character
	if '>' in line:
		meta = line
	else:
		sequence += line
	line = fh.readline()


l = len(sequence)
print 'The length of the sequence: %d'%l

#Generating a list of the codons present
codon = list(map(''.join, zip(*[iter(sequence)]*3)))
tc = len(codon)
print "The total number of codons: %d"%tc

per = float(raw_input('Per how many codons would you like to calculate codon bias: '))

print 'NOTE: Columns 2,5,8 and 11 shows Codon usage and Columns 3,6,9 and 12 show codon preference'

#Codon Bias calculation and Codon Preference calculation
#Phe
#CODON BIAS
print '\n'
print '-----------------------CODON BIAS TABLE FOR Saccharomyces cerevisiae---------------------------'
print '\n'
UUU_Phe = (float(codon.count('UUU')) / tc)*per
UUC_Phe = (float(codon.count('UUC')) / tc)*per
#CODON PREFERENCE
UUU_Phe_cp = float(UUU_Phe/(UUU_Phe + UUC_Phe))
UUC_Phe_cp = float(UUC_Phe/(UUU_Phe + UUC_Phe))
#Leu
#CODON BIAS
UUA_Leu = (float(codon.count('UUA')) / tc)*per
UUG_Leu = (float(codon.count('UUG')) / tc)*per
CUU_Leu = (float(codon.count('CUU')) / tc)*per
CUC_Leu = (float(codon.count('CUC')) / tc)*per
CUA_Leu = (float(codon.count('CUA')) / tc)*per
CUG_Leu = (float(codon.count('CUG')) / tc)*per
#CODON PREFERENCE
UUA_Leu_cp = float(UUA_Leu/(UUA_Leu + UUG_Leu + CUU_Leu + CUC_Leu + CUA_Leu + CUG_Leu))
UUG_Leu_cp = float(UUG_Leu/(UUA_Leu + UUG_Leu + CUU_Leu + CUC_Leu + CUA_Leu + CUG_Leu))
CUU_Leu_cp = float(CUU_Leu/(UUA_Leu + UUG_Leu + CUU_Leu + CUC_Leu + CUA_Leu + CUG_Leu))
CUC_Leu_cp = float(CUC_Leu/(UUA_Leu + UUG_Leu + CUU_Leu + CUC_Leu + CUA_Leu + CUG_Leu))
CUA_Leu_cp = float(CUA_Leu/(UUA_Leu + UUG_Leu + CUU_Leu + CUC_Leu + CUA_Leu + CUG_Leu))
CUG_Leu_cp = float(CUG_Leu/(UUA_Leu + UUG_Leu + CUU_Leu + CUC_Leu + CUA_Leu + CUG_Leu))

#Ile
#CODON BIAS
AUU_Ile = (float(codon.count('AUU')) / tc)*per
AUC_Ile = (float(codon.count('AUC')) / tc)*per
AUA_Ile = (float(codon.count('AUA')) / tc)*per
#CODON PREFERENCE
AUU_Ile_cp = float(AUU_Ile/(AUU_Ile + AUC_Ile + AUA_Ile))
AUC_Ile_cp = float(AUC_Ile/(AUU_Ile + AUC_Ile + AUA_Ile))
AUA_Ile_cp = float(AUA_Ile/(AUU_Ile + AUC_Ile + AUA_Ile))

#Met
#CODON BIAS
AUG_MET = (float(codon.count('AUG')) / tc)*per
#CODON PREFERENCE
AUG_MET_cp = 1

#Val
#CODON BIAS
GUU_Val = (float(codon.count('GUU')) / tc)*per
GUC_Val = (float(codon.count('GUC')) / tc)*per
GUA_Val = (float(codon.count('GUA')) / tc)*per
GUG_Val = (float(codon.count('GUG')) / tc)*per
#CODON PREFERENCE
GUU_Val_cp = float(GUU_Val/(GUU_Val + GUC_Val + GUA_Val + GUG_Val))
GUC_Val_cp = float(GUC_Val/(GUU_Val + GUC_Val + GUA_Val + GUG_Val))
GUA_Val_cp = float(GUA_Val/(GUU_Val + GUC_Val + GUA_Val + GUG_Val))
GUG_Val_cp = float(GUG_Val/(GUU_Val + GUC_Val + GUA_Val + GUG_Val))

#Ser
#CODON BIAS
UCU_Ser = (float(codon.count('UCU')) / tc)*per
UCC_Ser = (float(codon.count('UCC')) / tc)*per
UCA_Ser = (float(codon.count('UCA')) / tc)*per
UCG_Ser = (float(codon.count('UCG')) / tc)*per
#CODON PREFERENCE
UCU_Ser_cp = float(UCU_Ser/(UCU_Ser + UCC_Ser + UCA_Ser + UCG_Ser))
UCC_Ser_cp = float(UCC_Ser/(UCU_Ser + UCC_Ser + UCA_Ser + UCG_Ser))
UCA_Ser_cp = float(UCA_Ser/(UCU_Ser + UCC_Ser + UCA_Ser + UCG_Ser))
UCG_Ser_cp = float(UCG_Ser/(UCU_Ser + UCC_Ser + UCA_Ser + UCG_Ser))

#Pro
#CODON BIAS
CCU_Pro = (float(codon.count('CCU')) / tc)*per
CCC_Pro = (float(codon.count('CCC')) / tc)*per
CCA_Pro = (float(codon.count('CCA')) / tc)*per
CCG_Pro = (float(codon.count('CCG')) / tc)*per
#CODON PREFERENCE
CCU_Pro_cp = float(CCU_Pro/(CCU_Pro + CCC_Pro + CCA_Pro + CCG_Pro))
CCC_Pro_cp = float(CCC_Pro/(CCU_Pro + CCC_Pro + CCA_Pro + CCG_Pro))
CCA_Pro_cp = float(CCA_Pro/(CCU_Pro + CCC_Pro + CCA_Pro + CCG_Pro))
CCG_Pro_cp = float(CCG_Pro/(CCU_Pro + CCC_Pro + CCA_Pro + CCG_Pro))

#Thr
#CODON BIAS
ACU_Thr = (float(codon.count('ACU')) / tc)*per
ACC_Thr = (float(codon.count('ACC')) / tc)*per
ACA_Thr = (float(codon.count('ACA')) / tc)*per
ACG_Thr = (float(codon.count('ACG')) / tc)*per
#CODON PREFERENCE
ACU_Thr_cp = float(ACU_Thr/(ACU_Thr + ACC_Thr + ACA_Thr + ACG_Thr))
ACC_Thr_cp = float(ACC_Thr/(ACU_Thr + ACC_Thr + ACA_Thr + ACG_Thr))
ACA_Thr_cp = float(ACA_Thr/(ACU_Thr + ACC_Thr + ACA_Thr + ACG_Thr))
ACG_Thr_cp = float(ACG_Thr/(ACU_Thr + ACC_Thr + ACA_Thr + ACG_Thr))

#Ala
#CODON BIAS
GCU_Ala = (float(codon.count('GCU')) / tc)*per
GCC_Ala = (float(codon.count('GCC')) / tc)*per
GCA_Ala = (float(codon.count('GCA')) / tc)*per
GCG_Ala = (float(codon.count('GCG')) / tc)*per
#CODON PREFERENCE
GCU_Ala_cp = float(GCU_Ala/(GCU_Ala + GCC_Ala + GCA_Ala + GCG_Ala))
GCC_Ala_cp = float(GCC_Ala/(GCU_Ala + GCC_Ala + GCA_Ala + GCG_Ala))
GCA_Ala_cp = float(GCA_Ala/(GCU_Ala + GCC_Ala + GCA_Ala + GCG_Ala))
GCG_Ala_cp = float(GCG_Ala/(GCU_Ala + GCC_Ala + GCA_Ala + GCG_Ala))

#Tyr
#CODON BIAS
UAU_Tyr = (float(codon.count('UAU')) / tc)*per
UAC_Tyr = (float(codon.count('UAC')) / tc)*per
#CODON PREFERENCE
UAU_Tyr_cp = float(UAU_Tyr/(UAU_Tyr + UAC_Tyr))
UAC_Tyr_cp = float(UAC_Tyr/(UAU_Tyr + UAC_Tyr))


#TERMINATION CODON
#CODON BIAS
UAA_TER = (float(codon.count('UAA')) / tc)*per
UAG_TER = (float(codon.count('UAG')) / tc)*per
UGA_TER = (float(codon.count('UGA')) / tc)*per
#CODON PREFERENCE
UAA_TER_cp = float(UAA_TER/(UAA_TER + UAG_TER + UGA_TER))
UAG_TER_cp = float(UAG_TER/(UAA_TER + UAG_TER + UGA_TER))

#His
#CODON BIAS
CAU_His = (float(codon.count('CAU')) / tc)*per
CAC_His = (float(codon.count('CAC')) / tc)*per
#CODON PREFERENCE
CAU_His_cp = float(CAU_His/(CAU_His + CAC_His))
CAC_His_cp = float(CAC_His/(CAU_His + CAC_His))

#Gln
#CODON BIAS
CAA_Gln = (float(codon.count('CAA')) / tc)*per
CAG_Gln = (float(codon.count('CAG')) / tc)*per
#CODON PREFERENCE
CAA_Gln_cp = float(CAA_Gln/(CAA_Gln + CAG_Gln))
CAG_Gln_cp = float(CAG_Gln/(CAA_Gln + CAG_Gln))

#Asn
#CODON BIAS
AAU_Asn = (float(codon.count('AAU')) / tc)*per
AAC_Asn = (float(codon.count('AAC')) / tc)*per
#CODON PREFERENCE
AAU_Asn_cp = float(AAU_Asn/(AAU_Asn + AAC_Asn))
AAC_Asn_cp = float(AAC_Asn/(AAU_Asn + AAC_Asn))

#Lys
#CODON BIAS
AAA_Lys = (float(codon.count('AAA')) / tc)*per
AAG_Lys = (float(codon.count('AAG')) / tc)*per
#CODON PREFERENCE
AAA_Lys_cp = float(AAA_Lys/(AAA_Lys + AAG_Lys))
AAG_Lys_cp = float(AAG_Lys/(AAA_Lys + AAG_Lys))

#Asp
#CODON BIAS
GAU_Asp = (float(codon.count('GAU')) / tc)*per
GAC_Asp = (float(codon.count('GAC')) / tc)*per
#CODON PREFERENCES
GAU_Asp_cp = float(GAU_Asp/(GAU_Asp + GAC_Asp))
GAC_Asp_cp = float(GAC_Asp/(GAU_Asp + GAC_Asp))

#Glu
#CODON BIAS
GAA_Glu = (float(codon.count('GAA')) / tc)*per
GAG_Glu = (float(codon.count('GAG')) / tc)*per
#CODON PREFERENCES
GAA_Glu_cp = float(GAA_Glu/(GAA_Glu + GAG_Glu))
GAG_Glu_cp = float(GAG_Glu/(GAA_Glu + GAG_Glu))

#Cys
#CODON BIAS
UGU_Cys = (float(codon.count('UGU')) / tc)*per
UGC_Cys = (float(codon.count('UGC')) / tc)*per
#CODON PREFERENCE
UGU_Cys_cp = float(UGU_Cys/(UGU_Cys + UGC_Cys))
UGC_Cys_cp = float(UGU_Cys/(UGC_Cys + UGC_Cys))

#TERMINATION CODON
#UGA_TER = float(codon.count('UGA')) / tc
#CODON PREFERENCE
UGA_TER_cp = float(UGA_TER/(UAA_TER + UAG_TER + UGA_TER))

#Trp
#CODON BIAS
UGG_Trp = (float(codon.count('UGG')) / tc)*per
#CODON PREFERENCE
UGG_Trp_cp = 1

#Arg
#CODON BIAS
CGU_Arg = (float(codon.count('CGU')) / tc)*per
CGA_Arg = (float(codon.count('CGA')) / tc)*per
CGC_Arg = (float(codon.count('CGC')) / tc)*per
CGG_Arg = (float(codon.count('CGG')) / tc)*per
AGA_Arg = (float(codon.count('AGA')) / tc)*per
AGG_Arg = (float(codon.count('AGG')) / tc)*per
#CODON PREFERENCE
CGU_Arg_cp = float(CGU_Arg/(CGU_Arg + CGA_Arg + CGC_Arg + CGG_Arg + AGA_Arg + AGG_Arg))
CGA_Arg_cp = float(CGA_Arg/(CGU_Arg + CGA_Arg + CGC_Arg + CGG_Arg + AGA_Arg + AGG_Arg))
CGC_Arg_cp = float(CGC_Arg/(CGU_Arg + CGA_Arg + CGC_Arg + CGG_Arg + AGA_Arg + AGG_Arg))
CGG_Arg_cp = float(CGG_Arg/(CGU_Arg + CGA_Arg + CGC_Arg + CGG_Arg + AGA_Arg + AGG_Arg))

#Ser
#CODON BIAS
AGU_Ser = (float(codon.count('AGU')) / tc)*per
AGC_Ser = (float(codon.count('AGC')) / tc)*per
#CODON PREFERENCE
AGU_Ser_cp = float(AGU_Ser/(AGU_Ser + AGC_Ser))
AGC_Ser_cp = float(AGC_Ser/(AGU_Ser + AGC_Ser))

#Arg
#CODON BIAS
#AGA_Arg = float(codon.count('AGA')) / tc
#AGG_Arg = float(codon.count('AGG')) / tc
#CODON PREFERENCE
AGA_Arg_cp = float(AGA_Arg/(CGU_Arg + CGA_Arg + CGC_Arg + CGG_Arg + AGA_Arg + AGG_Arg))
AGG_Arg_cp = float(AGG_Arg/(CGU_Arg + CGA_Arg + CGC_Arg + CGG_Arg + AGA_Arg + AGG_Arg))

#Gly
#CODON BIAS
GGU_Gly = (float(codon.count('GGU')) / tc)*per
GGC_Gly = (float(codon.count('GGC')) / tc)*per
GGA_Gly = (float(codon.count('GGA')) / tc)*per
GGG_Gly = (float(codon.count('GGG')) / tc)*per
#CODON PREFERENCE
GGU_Gly_cp = float(GGU_Gly/(GGU_Gly + GGC_Gly + GGA_Gly + GGG_Gly))
GGC_Gly_cp = float(GGC_Gly/(GGU_Gly + GGC_Gly + GGA_Gly + GGG_Gly))
GGA_Gly_cp = float(GGA_Gly/(GGU_Gly + GGC_Gly + GGA_Gly + GGG_Gly))
GGG_Gly_cp = float(GGG_Gly/(GGU_Gly + GGC_Gly + GGA_Gly + GGG_Gly))


print "UUU-Phe %f %f    UCU-Ser %f %f    UAU-Tyr %f %f   UGU-Cys %f %f" %(UUU_Phe,UUU_Phe_cp,UCU_Ser,UCU_Ser_cp,UAU_Tyr,UAU_Tyr_cp,UGU_Cys,UGU_Cys_cp)
print "UUC-Phe %f %f    UCC-Ser %f %f    UAC-Tyr %f %f    UGC-Cys %f %f" %(UUC_Phe,UUC_Phe_cp,UCC_Ser,UCC_Ser_cp,UAC_Tyr,UAC_Tyr_cp,UGC_Cys,UGC_Cys_cp) 
print "UUA-Leu %f %f    UCA-Ser %f %f    UAA-TER %f %f    UGA-TER %f %f" %(UUA_Leu,UUA_Leu_cp,UCA_Ser,UCA_Ser_cp,UAA_TER,UAA_TER_cp,UGA_TER,UGA_TER_cp) 
print "UUG-Leu %f %f    UCG-Ser %f %f    UAG-TER %f %f    UGG-Trp %f %f" %(UUG_Leu,UUG_Leu_cp,UCG_Ser,UCG_Ser_cp,UAG_TER,UAG_TER_cp,UGG_Trp,UGG_Trp_cp) 
print '\n'
print "CUU-Leu %f %f    CCU-Pro %f %f    CAU-His %f %f    CGU-Arg %f %f" %(CUU_Leu,CUU_Leu_cp,CCU_Pro,CCU_Pro_cp,CAU_His,CAU_His_cp,CGU_Arg,CGU_Arg_cp) 
print "CUC-Leu %f %f    CCC-Pro %f %f    CAC-His %f %f    CGC-Arg %f %f" %(CUC_Leu,CUC_Leu_cp,CCC_Pro,CCC_Pro_cp,CAC_His,CAC_His_cp,CGC_Arg,CGC_Arg_cp) 
print "CUA-Leu %f %f    CCA-Pro %f %f    CAA-Gln %f %f    CGA-Arg %f %f" %(CUA_Leu,CUA_Leu_cp,CCA_Pro,CCA_Pro_cp,CAA_Gln,CAA_Gln_cp,CGA_Arg,CGA_Arg_cp) 
print "CUG-Leu %f %f    CCG-Pro %f %f    CAG-Gln %f %f    CGG-Arg %f %f" %(CUG_Leu,CUG_Leu_cp,CCG_Pro,CCG_Pro_cp,CAG_Gln,CAG_Gln_cp,CGG_Arg,CGG_Arg_cp) 
print '\n'
print "AUU-Ile %f %f    ACU-Thr %f %f    AAU-Asn %f %f    AGU-Ser %f %f" %(AUU_Ile,AUU_Ile_cp,ACU_Thr,ACU_Thr_cp,AAU_Asn,AAU_Asn_cp,AGU_Ser,AGU_Ser_cp) 
print "AUC-Ile %f %f    ACC-Thr %f %f    AAC-Asn %f %f    AGC-Ser %f %f" %(AUC_Ile,AUC_Ile_cp,ACC_Thr,ACC_Thr_cp,AAC_Asn,AAC_Asn_cp,AGC_Ser,AGC_Ser_cp) 
print "AUA-Ile %f %f    ACA-Thr %f %f    AAA-Lys %f %f    AGA-Arg %f %f" %(AUA_Ile,AUA_Ile_cp,ACA_Thr,ACA_Thr_cp,AAA_Lys,AAA_Lys_cp,AGA_Arg,AGA_Arg_cp) 
print "AUG-MET %f %f    ACG-Thr %f %f    AAG-Lys %f %f    AGG-Arg %f %f" %(AUG_MET,AUG_MET_cp,ACG_Thr,ACG_Thr_cp,AAG_Lys,AAG_Lys_cp,AGG_Arg,AGG_Arg_cp) 
print '\n'
print "GUU-Val %f %f    GCU-Ala %f %f    GAU-Asp %f %f    GGU-Gly %f %f" %(GUU_Val,GUU_Val_cp,GCU_Ala,GCU_Ala_cp,GAU_Asp,GAU_Asp_cp,GGU_Gly,GGU_Gly_cp) 
print "GUC-Val %f %f    GCC-Ala %f %f    GAC-Asp %f %f    GGC-Gly %f %f" %(GUC_Val,GUC_Val_cp,GCC_Ala,GCC_Ala_cp,GAC_Asp,GAC_Asp_cp,GGC_Gly,GGC_Gly_cp) 
print "GUA-Val %f %f    GCA-Ala %f %f    GAA-Glu %f %f    GGA-Gly %f %f" %(GUA_Val,GUA_Val_cp,GCA_Ala,GCA_Ala_cp,GAA_Glu,GAA_Glu_cp,GGA_Gly,GGA_Gly_cp) 
print "GUG-Val %f %f    GCG-Ala %f %f    GAG-Glu %f %f    GGG-Gly %f %f" %(GUG_Val,GUG_Val_cp,GCG_Ala,GCG_Ala_cp,GAG_Glu,GAG_Glu_cp,GGG_Gly,GGG_Gly_cp) 







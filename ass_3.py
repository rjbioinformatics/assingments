#solution of ass 3


bcell_iedb={"ANPYFSQRMTPYVPKQKKVTKKLRTTTSKPSNKKPDSVRAIDSNATN",
             "S","PSIPI","NEKVTKGAP","KVTKAAGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
             "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
             }
bcell_bepipred={"ANPYFSQRMTPYVPKQKKVTKKKKPDSVRAIDSNATN",
             "S","PSIPI","NEKVTKGAP","KVTKGAP","LSISDYFIPLEKSTLVPKK","GAPNLET",
             "WMDPQKLAALRELVPEIPKIWADL","LSISDYFIPLEKSTLVPKK","LRTTTSKPSN"
             }
#solution1
inter_section=bcell_iedb&bcell_bepipred
print(inter_section,len(inter_section))  

#solution2
only_in_bcelliedb=bcell_iedb-bcell_bepipred
print(only_in_bcelliedb,len(only_in_bcelliedb))

#solution3

any_but_notcommon=bcell_iedb^bcell_bepipred
print(any_but_notcommon,len(any_but_notcommon))

#solution4

unique_epitopes=bcell_iedb^bcell_bepipred
print(unique_epitopes)








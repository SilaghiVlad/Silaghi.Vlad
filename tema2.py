sir="Ferdinand Porsche a înființat  în 1931, cu sediul la Königstrasse în centrul Stuttgartului. Compania oferea inițial servicii de consultanță și proiectare, și nu construia automobile sub numele propriu. Unul din primele contracte a fost cu guvernul german pentru a proiecta o mașină populară, în germană[4]."
mijloc=len(sir)//2
partea1=sir[:mijloc]
partea2=sir[mijloc:]
partea1.strip()
partea2=partea2[::-1]
partea2=partea2.replace(',',' ')
partea2=partea2.replace('.',' ')
print(partea1.upper()+partea2.capitalize())
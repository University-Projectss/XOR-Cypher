# Proiect-ASC
Welcome to the Proiect-ASC wiki!

PARTEA I

Instructiuni de utilizare:

1. Descarcam cele doua scriptui in folderul in care avem si fisierul text pe care dorim sa il criptam. In acest exemplu ne vom referi la fisierul text ca fiind numit input.txt

2. Deschidem un terminal/command line in folderul respectiv

3. Pentru a cripta fisierul text si a salva versiunea criptata intr-un alt fisier o sa rulam comanda: `python encrypt.py parolasecreta input.txt output`. Acum a fost generat fisierul 'output' care contine textul criptat. Fisierul NU este de tip text, ci este de forma binara. "Binary file" pe google pentru mai multe detalii legate de fisierele binare.

4. Pentru a decripta textul, in acelasi terminal, rulam comanda: `python decrypt.py output parolasecreta input-recuperat.txt`. Acum a fost generat fisierul 'input-recuperat.txt' in care avem textul decriptat.



Acest proiect a fost realizat de Robert Udrea, Andrei Lefter si Matei Biciusca, pe scurt echipa *HeliXor*

Pentru a rula scripturile este nevoie de Python 3.2 sau o versiune mai noua

parolasecreta folosita este STRICT SECRETA si este stiuta doar de membrii echipei.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

PARTEA II

HeliXor vs A.R.C.
Cheia echipei adverse(A.R.C.): speramcaebine

Cum am facut? - Am xorat fisierul de input cu cel output

Putem afla parola si folosind doar fisierul output? Ramane de vazut ;)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

PARTEA II v2.0

In urma a doua seri de codat in echipa pe Discord, am reusit sa aflam parola folosindu-ne exclusiv de fisierul output. Programul intreg si eficient este decryptarefaraoutput.py, iar in decryptareavansata_v1.py avem o varianta a programului care a fost decisiva in realizarea proiectului. 


Cum am procedat? 

  Pentru inceput, am citit fisierul de output menit sa fie decryptat ca sa aflam parola. Pe urma am aflat lungimea parolei folosindu-ne de ideea ca pentru codificare parola a fost multiplicata, astfel am cautat caracterele care s-ar repeta din x in x caractere(unde 10 <= x <= 15).
  Dupa ce am aflat lungimea parolei, treaba e simpla: Ne-am folosit de xor pentru a vedea ce caractere din fisierul output pot fi xorate cu caractere alfanumerice astfel incat sa obtinem caracterele posibile dintr-un text in limba romana(litere mici/mari, semne de punctuatie, numere). Astfel am selectat doar caracterele bune si am obtinut (din nou) parola adversarilor: speramcaebine.


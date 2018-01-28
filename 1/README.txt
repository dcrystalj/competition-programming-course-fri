DN: Tomaz Tomazic (dcrystalj)

1. A Phone numbers:  (A.pn.py)
V nalogi vedno delim na pare crk. Torej na vsake 2 crki dodam '-', V primeru lihega stevila znakov pa pustim zadnje 3.

2. B. Supercentral Point B (B.sp.py)
V zanki grem cez vse tocke in preverim ce ima vse 4 sosede. Ce ima, povecam stevec

3. C. Palindromic Times (C.pt.py)
Shranim vsako stevilko v svojo spremenljivko. Povecujem stevke s pravili kot veljajo za uro. V vsaki iteraciji preverim ce je palindrom.

4. D. Memory Manager (D.mm.py)
Za vsako operacijo imam svojo funkcijo. Vse operacije preberem in nato iteriram po njih. Pomnilnik je predstavljen z poljem nicel. Vsaka alokacija spremeni zasedn pomnilnik na doloceno zaporedno stevilko. Za defragment izbrisem nicle in jih dam na konec. Za erase sem zal sele po nekaj urah gledanja kode doejel, da je potrebno preveriti za nenegativnost :(

5. E. Find Pair (E.fp.py)
Stevila sortiram in za vsako stevilo si v slovar shranim stevilo njene ponovitve. Prvo stevilo izracunam po formuli k/n medtekmo za drugo stevilo Iteriram po sortiranem polju in K zmanjsujem dokler je mozno po formuli: [stevilo ponovitev za i-to stevilo v polju  *  dolzina polja]. Na koncu K delim z stevilom ponovitev.

6. Y. Winner  (Y.winner.py)
Tocke sestevam za vsakega igralca. Istocasno si zapomnim vsa stanja (igralec, tocke) v polje states. Poiscem igralca ki ima na koncu najvec tock in nato iteriram po stanjih in izpisem prvega igralca ki je dosegel max st tock.

7. Nisem razumel naloge
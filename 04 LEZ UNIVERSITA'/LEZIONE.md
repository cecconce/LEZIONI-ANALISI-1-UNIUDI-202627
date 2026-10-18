# 04 LEZ UNIVERSITA' – Famiglie di insiemi, De Morgan, prodotto cartesiano, insiemi numerici

- **Docente:** prof. Lorenzo Freddi – Analisi Matematica 1, Università di Udine, a.a. 2026/27
- **Data della lezione:** da confermare (videolezione successiva alla lezione 03 del 29/09/2026)
- **Studiata in chat:** dal 05/10/2026 al 18/10/2026

## Argomenti trattati

La lezione riparte dopo la slide 32 (insieme delle parti) e arriva alla **slide 41**.

1. Unione e intersezione di due insiemi (slide 33–34)
2. Famiglie di insiemi: unione e intersezione di una famiglia (slide 35)
3. Proprietà associative e distributive (slide 36)
4. Complementare e differenza di insiemi (slide 37)
5. Leggi di De Morgan, per due insiemi e per una famiglia (slide 38)
6. Coppie ordinate e prodotto cartesiano (slide 39)
7. Insiemi numerici $\mathbb{N}, \mathbb{Z}, \mathbb{Q}, \mathbb{R}$ (slide 41)

## Materiali su Drive (solo link)

- [2026_pres_01_logica_e_insiemi.pdf](https://drive.google.com/file/d/1K72wRUI-xyKGGE2JaSwpFnFshwy3CFT6/view) – slide del prof. Freddi (questa lezione: slide 33–41)

---

## 1. Unione e intersezione di due insiemi

**L'idea.** In una classe: $A$ = chi ha consegnato matematica, $B$ = chi ha consegnato fisica.

- **Unione** $A \cup B$: chi ha consegnato **almeno uno** dei due compiti.
- **Intersezione** $A \cap B$: chi ha consegnato **tutti e due**.

**Con i numeri.** $A = \{1,2,3,4\}$, $B = \{3,4,5\}$

| elemento | in A? | in B? | in $A \cup B$? | in $A \cap B$? |
|:-:|:-:|:-:|:-:|:-:|
| 1 | sì | no | sì | no |
| 2 | sì | no | sì | no |
| 3 | sì | sì | sì | sì |
| 4 | sì | sì | sì | sì |
| 5 | no | sì | sì | no |

$$A \cup B = \{1,2,3,4,5\}, \qquad A \cap B = \{3,4\}$$

**I simboli del prof.**

$$A \cup B = \{\, x : x \in A \lor x \in B \,\} \qquad A \cap B = \{\, x : x \in A \land x \in B \,\}$$

$\lor$ = "oppure" (basta una), $\land$ = "e" (servono tutte e due).

**A cosa serve.** Il dominio di una funzione è l'**intersezione** delle condizioni (radice ≥ 0 *e* denominatore ≠ 0). La soluzione di una disequazione spezzata in casi è un'**unione** di intervalli.

---

## 2. Famiglie di insiemi (slide 35)

**L'idea.** Una scuola ha tre classi; ogni classe è un insieme di studenti. L'elenco delle classi è un **insieme di insiemi**: una **famiglia di insiemi**. I "nomi" delle classi (1, 2, 3) formano l'**insieme degli indici** $I$.

$$\mathscr{F} = \{\, A_i \in \wp(U) : i \in I \,\}$$

- se $I = \{1,2,\dots,n\}$ allora $\mathscr{F} = \{A_1, A_2, \dots, A_n\}$
- se $I = \{1,2,\dots,n,\dots\}$ allora $\mathscr{F} = \{A_1, A_2, \dots, A_n, \dots\}$

**Con i numeri.** $I = \{1,2,3\}$, $A_1 = \{0,1\}$, $A_2 = \{1,2\}$, $A_3 = \{1,3\}$

| elemento | in $A_1$? | in $A_2$? | in $A_3$? | almeno uno? | tutti? |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | sì | no | no | sì | no |
| 1 | sì | sì | sì | sì | **sì** |
| 2 | no | sì | no | sì | no |
| 3 | no | no | sì | sì | no |

$$\bigcup_{i\in I} A_i = \{0,1,2,3\}, \qquad \bigcap_{i\in I} A_i = \{1\}$$

**I simboli del prof.**

$$\bigcup_{i\in I} A_i := \{\, x \in U : \exists\, i \in I : x \in A_i \,\} \qquad \text{(almeno uno)}$$

$$\bigcap_{i\in I} A_i := \{\, x \in U : x \in A_i \ \ \forall\, i \in I \,\} \qquad \text{(tutti)}$$

**Regola da ricordare:** unione ↔ $\exists$, intersezione ↔ $\forall$.

**A cosa serve.** All'orale si chiedono le due definizioni con $\exists$ e $\forall$. Con $I = \mathbb{N}$ si hanno famiglie infinite (servirà con successioni e limiti).

---

## 3. Proprietà associative e distributive (slide 36)

La slide le dà come esercizio da dimostrare:

1. $A \cap (B \cap C) = (A \cap B) \cap C$
2. $A \cup (B \cup C) = (A \cup B) \cup C$
3. $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
4. $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$

**L'idea.** Come con i numeri: $(2+3)+4 = 2+(3+4)$ e $2 \cdot (3+4) = 2\cdot 3 + 2\cdot 4$. Con gli insiemi $\cap$ fa la parte del "per" e $\cup$ del "più". Novità: con gli insiemi la distributiva vale **nei due sensi** (la 3 e la 4).

**Con i numeri (distributiva 4).** $A = \{1,2\}$, $B = \{2,3\}$, $C = \{3,4\}$

- Sinistra: $B \cup C = \{2,3,4\}$, poi $A \cap \{2,3,4\} = \{2\}$
- Destra: $A \cap B = \{2\}$, $A \cap C = \emptyset$, poi $\{2\} \cup \emptyset = \{2\}$
- $\{2\} = \{2\}$ ✓

**Dimostrazione (metodo da usare all'orale):** si traduce in logica e si usa la distributiva di "e/o".

$$
\begin{aligned}
x \in A \cap (B \cup C)
&\iff x \in A \land (x \in B \lor x \in C) \\
&\iff (x \in A \land x \in B) \lor (x \in A \land x \in C) \\
&\iff x \in (A \cap B) \lor x \in (A \cap C) \\
&\iff x \in (A \cap B) \cup (A \cap C)
\end{aligned}
$$

Le altre tre si dimostrano con lo stesso schema.

---

## 4. Complementare e differenza (slide 37)

**L'idea: la scatola.** Una scatola con le palline $1,2,3,4,5$ è $U$ (il "tutto"). Le rosse $1,2,3$ sono $A$.

- **Complementare** $A^C$: "quali palline della scatola **non** sono rosse?" → $\{4,5\}$. Si capovolge la colonna sì/no.
- **Differenza** $A \setminus B$ ("A meno B"): le palline con la stella sono $B = \{3,4\}$. "Quali palline rosse **non** hanno la stella?" → parto dalle rosse e tolgo la 3 → $\{1,2\}$.

| pallina | rossa (in A)? | stella (in B)? | in $A^C$? | in $A \setminus B$? |
|:-:|:-:|:-:|:-:|:-:|
| 1 | sì | no | no | **sì** |
| 2 | sì | no | no | **sì** |
| 3 | sì | sì | no | no |
| 4 | no | sì | **sì** | no |
| 5 | no | no | **sì** | no |

Attenzione: la differenza non è simmetrica, $B \setminus A = \{4\} \neq A \setminus B$.

**I simboli del prof.**

$$A^C := \mathcal{C}(A) := \{\, x \in U : x \notin A \,\}$$

$$A \setminus B := \{\, x \in U : (x \in A) \land (x \notin B) \,\}$$

**Collegamento:** il complementare è "tutta la scatola meno A":

$$A^C = U \setminus A$$

**A cosa serve.** I domini si scrivono come differenze: $\mathbb{R} \setminus \{0\}$ per $f(x) = \frac{1}{x}$. Il complementare serve per De Morgan.

---

## 5. Leggi di De Morgan (slide 38)

**L'idea.**
- *"Non voglio né tè né caffè"* = non voglio il tè **e** non voglio il caffè. Il "non" entra e **"o" diventa "e"**.
- *"Non è vero che ho sia fame sia sete"* = non ho fame **oppure** non ho sete. Il "non" entra e **"e" diventa "o"**.

**Con la scatola.** $U = \{1,2,3,4,5\}$, $A = \{1,2,3\}$, $B = \{3,4\}$, quindi $A^C = \{4,5\}$, $B^C = \{1,2,5\}$.

- 1ª legge: $(A \cup B)^C = \{1,2,3,4\}^C = \{5\}$ e $A^C \cap B^C = \{5\}$ ✓
- 2ª legge: $(A \cap B)^C = \{3\}^C = \{1,2,4,5\}$ e $A^C \cup B^C = \{1,2,4,5\}$ ✓

**I simboli del prof (per due insiemi).**

$$(A \cup B)^C = A^C \cap B^C \qquad (A \cap B)^C = A^C \cup B^C$$

| Legge | prima | dopo |
|---|---|---|
| 1ª | $(A \cup B)^C$ | $A^C \cap B^C$ |
| 2ª | $(A \cap B)^C$ | $A^C \cup B^C$ |

Regola: il complementare entra nella parentesi e **∪ e ∩ si scambiano**.

**Per una famiglia** $\mathscr{F} = \{A_i \in \wp(U) : i \in I\}$ (sulla slide, non svolta in chat):

$$\Big(\bigcup_{i\in I} A_i\Big)^C = \bigcap_{i\in I} A_i^C \qquad \Big(\bigcap_{i\in I} A_i\Big)^C = \bigcup_{i\in I} A_i^C$$

**A cosa serve.** All'orale la slide la dà come esercizio da dimostrare (stesso metodo della distributiva). Negli esercizi serve per negare frasi: "$x < 1$ oppure $x > 3$" diventa "$x \geq 1$ e $x \leq 3$".

---

## 6. Coppie ordinate e prodotto cartesiano (slide 39)

**L'idea.** Al cinema "fila 3, posto 5" non è "fila 5, posto 3": nella **coppia ordinata** conta l'ordine. $(3,5) \neq (5,3)$, mentre con gli insiemi $\{3,5\} = \{5,3\}$.

Il **prodotto cartesiano** $A \times B$ è l'elenco di **tutte** le coppie: primo elemento da $A$, secondo da $B$ (come i pranzi possibili di un menù: 2 primi × 3 secondi = 6 pranzi).

**Con i numeri.** $A = \{1,2\}$, $B = \{3,4,5\}$

| | **3** | **4** | **5** |
|---|---|---|---|
| **1** | (1,3) | (1,4) | (1,5) |
| **2** | (2,3) | (2,4) | (2,5) |

$2 \cdot 3 = 6$ coppie: i numeri di elementi si moltiplicano, da qui il nome "prodotto". Ogni coppia è un punto del piano (primo numero in orizzontale, secondo in verticale).

**I simboli del prof.**

$$(x,y) = (x',y') \iff x = x' \land y = y'$$

$$A \times B := \{\, (x,y) : x \in A \land y \in B \,\}$$

**A cosa serve.** $\mathbb{R} \times \mathbb{R}$ è il piano cartesiano. Il grafico di una funzione è un insieme di coppie $(x, f(x))$; le funzioni di più variabili $f(x,y)$ sono definite su $\mathbb{R} \times \mathbb{R}$.

---

## 7. Insiemi numerici (slide 41)

**L'idea: matrioske.** Ogni scatola nasce perché nella precedente manca qualcosa.

| Insieme | Nella vita | Cosa aggiunge |
|---|---|---|
| $\mathbb{N}$ naturali | contare oggetti | — |
| $\mathbb{Z}$ interi | temperature sotto zero, conto in rosso | i negativi |
| $\mathbb{Q}$ razionali | mezza pizza, un quarto d'ora | le frazioni |
| $\mathbb{R}$ reali | diagonale di un quadrato di lato 1 | i numeri che non sono frazioni ($\sqrt{2}, \pi$) |

| numero | $\mathbb{N}$ | $\mathbb{Z}$ | $\mathbb{Q}$ | $\mathbb{R}$ |
|:-:|:-:|:-:|:-:|:-:|
| $3$ | sì | sì | sì | sì |
| $-2$ | no | sì | sì | sì |
| $\frac{1}{2}$ | no | no | sì | sì |
| $\sqrt{2}$ | no | no | no | sì |

Chi sta in una scatola sta anche in tutte quelle più grandi: $\mathbb{N} \subseteq \mathbb{Z} \subseteq \mathbb{Q} \subseteq \mathbb{R}$.

**I simboli del prof.**

$$\mathbb{N} := \{0,1,2,3,4,\dots\} \qquad \mathbb{Z} := \{0,1,-1,2,-2,3,-3,\dots\}$$

$$\mathbb{Q} := \left\{ \frac{p}{q} : p \in \mathbb{Z},\ q \in \mathbb{Z} \setminus \{0\} \right\} \qquad \mathbb{R} := \text{insieme dei numeri reali}$$

Per il prof **lo 0 è in $\mathbb{N}$**. In $\mathbb{Q}$ torna la differenza: $q \in \mathbb{Z} \setminus \{0\}$, perché non si divide per 0.

**A cosa serve.** Le funzioni d'esame vivono in $\mathbb{R}$; i domini si scrivono con questi simboli.

---

## Esercizi svolti (05/10/2026 – 18/10/2026)

### Esercizio 1 – Unione e intersezione

**Testo:** $A = \{0,2,4,6\}$, $B = \{x \in \mathbb{N} : x < 4\}$. Scrivi $A \cup B$ e $A \cap B$.

**Mia risposta:** $A \cup B = \{0,2,4,6\}$, $A \cap B = \{0,2\}$.

**Esito:** intersezione ✅. Unione ❌: $B = \{0,1,2,3\}$, e l'unione prende tutto quello che sta in almeno uno, quindi entrano anche 1 e 3.
$$A \cup B = \{0,1,2,3,4,6\}$$

### Esercizio 2 – Famiglia di insiemi

**Testo:** $I = \{1,2,3\}$, $A_1 = \{0,2,4\}$, $A_2 = \{2,3,4\}$, $A_3 = \{2,4,5\}$. Scrivi $\bigcup_{i\in I} A_i$ e $\bigcap_{i\in I} A_i$.

**Mia risposta (tabella sul tablet):** unione $\{0,2,3,4,5\}$, intersezione $\{4\}$.

**Esito:** unione ✅. Intersezione ❌: nella colonna $A_3$ avevo scritto 2 → no e 3 → sì, invertiti. Il 2 sta in tutti e tre.
$$\bigcap_{i\in I} A_i = \{2,4\}$$

### Esercizio 3 – Distributiva

**Testo:** $A = \{0,1,2\}$, $B = \{1,3\}$, $C = \{2,3\}$. Calcola $A \cap (B \cup C)$ e $(A \cap B) \cup (A \cap C)$.

**Esito:** non svolto da me, risolto in chat:
$B \cup C = \{1,2,3\}$, $A \cap (B \cup C) = \{1,2\}$; $A \cap B = \{1\}$, $A \cap C = \{2\}$, unione $\{1,2\}$. Uguali ✓

### Esercizio 4 – Complementare e differenza

| Domanda | Mia risposta | Esito |
|---|---|---|
| $U = \{1,\dots,6\}$, $A = \{2,4,6\}$: quanto vale $A^C$? | $\{1,3,5\}$ | ✅ |
| $A = \{2,4,6\}$, $B = \{4,5,6\}$: quanto vale $A \setminus B$? | $\{2\}$ | ✅ |

(La prima spiegazione insieme di complementare e differenza non l'avevo capita: rifatta con la scatola di palline, un pezzo alla volta.)

### Esercizio 5 – 1ª legge di De Morgan

**Testo:** $U = \{1,\dots,6\}$, $A = \{1,2\}$, $B = \{2,3\}$. Calcola $(A \cup B)^C$ e $A^C \cap B^C$. Vengono uguali?

**Mia risposta:** no, sono diversi.

**Esito:** ❌ sono uguali (è una legge, vale sempre). Errore nell'intersezione finale: vanno tenuti **solo gli elementi in comune**.
$$(A \cup B)^C = \{1,2,3\}^C = \{4,5,6\}, \qquad A^C \cap B^C = \{3,4,5,6\} \cap \{1,4,5,6\} = \{4,5,6\}$$

### Esercizio 6 – 2ª legge di De Morgan

**Testo:** stessi insiemi. Calcola $(A \cap B)^C$ e $A^C \cup B^C$.

**Mia risposta:** $\{4,5,6\}$.

**Esito:** ❌ era il risultato della 1ª legge. Qui $A \cap B = \{2\}$, quindi il complementare toglie solo il 2.
$$(A \cap B)^C = \{1,3,4,5,6\}, \qquad A^C \cup B^C = \{3,4,5,6\} \cup \{1,4,5,6\} = \{1,3,4,5,6\}$$

### Esercizio 7 – Prodotto cartesiano

**Testo:** $A = \{0,1\}$, $B = \{1,2,3\}$. Scrivi le coppie di $A \times B$. Quante sono?

**Mia risposta:** 6 coppie: $(0,1), (0,2), (0,3), (1,1), (1,2), (1,3)$.

**Esito:** ✅ ($2 \cdot 3 = 6$).

### Esercizio 8 – Insiemi numerici

**Testo:** per ogni numero, la scatola più piccola in cui sta.

| Numero | Mia risposta | Esito |
|:-:|---|---|
| $-5$ | interi | ✅ $\mathbb{Z}$ (negativo, quindi non in $\mathbb{N}$) |
| $0$ | naturali, ma non in $\mathbb{Q}$ | ✅ $\mathbb{N}$; ❌ "non in $\mathbb{Q}$": $0 = \frac{0}{1}$, lo 0 non può stare sotto la frazione ma sopra sì |
| $\frac{7}{3}$ | $\mathbb{Q}$ | ✅ ($7 : 3 = 2{,}333\dots$, non intero) |
| $\pi$ | reali | ✅ non si scrive come frazione |

---

## Dubbi aperti

- **Data della lezione** da confermare.
- **Slide 40**: nessuno screenshot, contenuto da verificare sul video (probabilmente il seguito del prodotto cartesiano).
- **Da ripassare**: nelle intersezioni tengo elementi che non sono in comune o ne perdo alcuni (Esercizi 2 e 5). Controllare riga per riga in tabella.
- **Da fare**: dimostrare con la catena di $\iff$ le altre proprietà della slide 36 e le leggi di De Morgan (slide 38), anche per una famiglia.

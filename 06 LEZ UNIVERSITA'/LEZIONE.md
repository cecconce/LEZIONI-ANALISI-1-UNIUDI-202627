# 06 LEZ UNIVERSITA' – Funzioni: definizioni di base

- **Docente:** prof. Lorenzo Freddi – Analisi Matematica 1, Università di Udine, a.a. 2026/27
- **Data della lezione:** 02/10/2026, videolezione alla lavagna (ore 8:35, 1 h 8 min, e ore 9:53, 26 min)
- **Studiata in chat:** 21/10/2026, 24/10/2026, 02/11/2026, 08/11/2026

Nei due video il prof lavora alla lavagna e non ci sono slide catturate: il contenuto è ricostruito dalla pres_02, slide 2–10 (il 6/10 il prof riparte da «Funzioni composte», slide 11).

## Argomenti trattati

La lezione apre la presentazione pres_02 e arriva fino a «Funzioni composte» esclusa (**slide 2–10**).

1. Grafico di funzione come sottoinsieme di $A \times B$; dominio, codominio, variabile, valore; notazione (slide 2–3)
2. Esempi: funzione costante, identità, restrizione (slide 4)
3. Immagine e controimmagine (slide 5–6)
4. Funzioni iniettive, suriettive, biiettive; l'esempio di $x^2$ con domini e codomini diversi (slide 7–8)
5. Lemma: se $f$ è iniettiva, $f(x) = f(y) \iff x = y$ (slide 9)
6. Funzioni reali di variabile reale e dominio naturale (slide 10)

## Materiali su Drive (solo link)

- [2026_pres_02_funzioni.pdf](https://drive.google.com/file/d/10cclpI1x6npMY6ImQ7oINCC6LCPRbUuO/view) – slide del prof. Freddi (questa lezione: slide 2–10)

---

## 1. Grafico di funzione (slide 2–3)

**L'idea.** Una funzione è un "registro": a ogni elemento della partenza associa **uno e un solo** elemento dell'arrivo (come il registro dei mesi di nascita: ogni studente ha un solo mese, due studenti possono avere lo stesso mese).

**Con i numeri.** $A = \{-1, 0, 1, 2\}$, $B = \{-1, 0, 1, 2, 3\}$, $F(x) = x^2 - 1$

| $x$ | $F(x)$ | coppia |
|:-:|:-:|:-:|
| $-1$ | $1 - 1 = 0$ | $(-1, 0)$ |
| $0$ | $0 - 1 = -1$ | $(0, -1)$ |
| $1$ | $1 - 1 = 0$ | $(1, 0)$ |
| $2$ | $4 - 1 = 3$ | $(2, 3)$ |

**Disegno.** Nella griglia $A \times B$ (20 punti) la funzione sceglie **un punto per colonna**: niente colonne vuote, niente colonne con due punti (test della retta verticale).

**I simboli del prof.** $F \subseteq A \times B$ è un grafico di funzione di dominio $A$ e codominio $B$ se

$$\forall\, x \in A \ \ \exists!\, y \in B : (x,y) \in F$$

- $\forall x \in A$: nessuna colonna vuota; $\exists!$: un solo punto per colonna.
- Al posto di $(x,y) \in F$ si scrive $y = F(x)$: $x$ è la **variabile**, $F(x)$ il **valore** o **immagine** di $F$ in $x$.

$$F : A \to B, \qquad x \mapsto F(x)$$

$F(x)$ è la **legge**: può essere una formula ($x^2 - 1$) o a casi ($0$ se $x > 7$, $1$ altrimenti). Una funzione può anche essere solo un elenco di coppie, senza formula.

**A cosa serve.** Una funzione sono **tre cose insieme**: dominio, codominio, legge (si vede al punto 4). Lo studio di funzione d'esame disegna proprio l'insieme delle coppie in $\mathbb{R} \times \mathbb{R}$. Per la funzione inversa (slide 12–17) si scambiano le coppie $(x,y) \to (y,x)$.

---

## 2. Costante, identità, restrizione (slide 4)

**L'idea.**
- **Costante**: un distributore guasto, qualunque tasto premi dà sempre caffè.
- **Identità**: uno specchio, quello che entra esce uguale.
- **Restrizione**: stesso registro, guardato solo per una parte della partenza.

**Con i numeri** ($A = \{-1,0,1,2\}$):

| $x$ | costante $f(x) = 2$ | identità $\mathrm{id}_A(x) = x$ | $F(x)=x^2-1$ ristretta a $C=\{1,2\}$ |
|:-:|:-:|:-:|:-:|
| $-1$ | $2$ | $-1$ | — |
| $0$ | $2$ | $0$ | — |
| $1$ | $2$ | $1$ | $0$ |
| $2$ | $2$ | $2$ | $3$ |

**I simboli del prof.**

$$\text{costante: } f(x_1) = f(x_2) \quad \forall\, x_1, x_2 \in A$$

$$\mathrm{id}_A : A \to A, \qquad \mathrm{id}_A(x) = x$$

$$f|_C : C \to B, \qquad x \mapsto f|_C(x) := f(x) \qquad (C \subseteq A)$$

**A cosa serve.** Costante: derivata nulla su un intervallo ⇒ funzione costante (la "$+c$" degli integrali). Identità: serve a definire l'inversa ($g \circ f = \mathrm{id}_A$, $f \circ g = \mathrm{id}_B$). Restrizione: serve a rendere invertibile una funzione (così nascono $\sqrt{x}$, $\arcsin$, $\arccos$).

---

## 3. Immagine e controimmagine (slide 5–6)

**L'idea.** **Immagine**: do un gruppo di $x$ e chiedo quali risultati danno (si va **avanti**). **Controimmagine**: do un gruppo di risultati e chiedo quali $x$ ci finiscono (si va **indietro**).

**Con i numeri** ($F(x) = x^2 - 1$ su $A = \{-1,0,1,2\}$):

- $C = \{-1, 1, 2\}$: risultati $0, 0, 3$ → $F(C) = \{0, 3\}$ (i doppioni si scrivono una volta).
- $D = \{0, 1\}$: si passano **tutti** gli $x$ di $A$ e si tengono quelli con $F(x) \in D$ → $F^{-1}(D) = \{-1, 1\}$ (l'$1$ di $D$ non è colpito da nessuno, ed è permesso).

**I simboli del prof.** Sia $f : A \to B$.

$$f(C) := \{\, f(x) : x \in C \,\} \quad (C \subseteq A) \qquad\qquad f^{-1}(D) := \{\, x \in A : f(x) \in D \,\} \quad (D \subseteq B)$$

Se $C = A$ si parla di **immagine di $f$**. Il simbolo $f^{-1}(D)$ esiste sempre: **non** vuol dire che $f$ sia invertibile.

**A cosa serve.** L'immagine di $f$ serve per la suriettività. La controimmagine è il nome preciso di **risolvere un'equazione o disequazione**: risolvere $x^2 - 1 = 0$ è calcolare $F^{-1}(\{0\})$; zeri e segno nello studio di funzione sono controimmagini.

---

## 4. Iniettive, suriettive, biiettive (slide 7–8)

**L'idea, con due controlli sulla colonna dei risultati.**

| | controllo | se passa |
|---|---|---|
| iniettiva | nessun risultato si ripete (numeri diversi → risultati diversi) | $f(x) = y$ ha **al massimo una** soluzione |
| suriettiva | ogni numero dell'arrivo $B$ compare tra i risultati | $f(x) = y$ ha **almeno una** soluzione |
| biiettiva | tutti e due | $f(x) = y$ ha **esattamente una** soluzione |

**Con i numeri.**
- $x^2$ su $\{-2,-1,0,1,2\}$: risultati $4,1,0,1,4$ → il $1$ e il $4$ si ripetono → **non iniettiva**.
- $2x+1$ sugli stessi $x$: risultati $-3,-1,1,3,5$, nessuno si ripete → **iniettiva**.
- $x^2$ con arrivo $\{0,1,4\}$ → **suriettiva**; con arrivo $\{0,1,2,3,4\}$ mancano $2$ e $3$ → **non suriettiva**. Stessi risultati, cambia solo $B$.

**I simboli del prof.** $f : A \to B$ si dice

- **iniettiva** se $x_1 \neq x_2 \implies f(x_1) \neq f(x_2)$, o equivalentemente $f(x_1) = f(x_2) \implies x_1 = x_2$;
- **suriettiva** se il codominio coincide con l'immagine: $\forall\, y \in B\ \ \exists\, x \in A : y = f(x)$;
- **biiettiva** se è sia iniettiva che suriettiva.

**Esempio della slide 8** ($\mathbb{R}^+_0$ = reali $\geq 0$), stessa legge $x^2$:

| funzione | dominio | codominio | iniettiva | suriettiva | |
|---|---|---|---|---|---|
| $f$ | $\mathbb{R}$ | $\mathbb{R}$ | no: $f(-2) = f(2) = 4$ | no: $-1$ non è mai un quadrato | né l'una né l'altra |
| $g$ | $\mathbb{R}^+_0$ | $\mathbb{R}$ | sì (niente negativi in partenza) | no: manca $-1$ | solo iniettiva |
| $h$ | $\mathbb{R}^+_0$ | $\mathbb{R}^+_0$ | sì | sì: $y = (\sqrt{y})^2$ | **biiettiva** |

Dominio o codominio diversi ⇒ funzioni diverse.

**A cosa serve.** Prossima lezione (slide 14): $f$ è **invertibile se e solo se è biiettiva**. L'inversa di $h$ è $\sqrt{y}$; allo stesso modo nascono $\ln x$, $\arcsin x$, $\arctan x$.

---

## 5. Lemma delle funzioni iniettive (slide 9)

**L'idea.** Se $f$ è iniettiva, in $f(a) = f(b)$ si può **"togliere la $f$"**.

**Prima con i numeri.** Il cubo è iniettivo ($-2,-1,0,1,2 \mapsto -8,-1,0,1,8$): da $a^3 = 8 = 2^3$ segue $a = 2$.

**Poi con le lettere.**

$$(x+1)^3 = (2x)^3 \iff x + 1 = 2x \iff x = 1 \qquad \text{verifica: } 2^3 = 8 = 2^3$$

**I simboli del prof.**

> **Lemma.** Se $f : A \to B$ è iniettiva, allora per ogni $x, y \in A$: $\quad f(x) = f(y) \iff x = y$.

Dimostrazione: $\Leftarrow$ vale perché $f$ è una funzione (stesso $x$, stesso risultato); $\Rightarrow$ vale perché $f$ è iniettiva.

**A cosa serve.** Risolvere equazioni: $e^a = e^b \iff a = b$, $\ln a = \ln b \iff a = b$. **Attenzione**: il quadrato su $\mathbb{R}$ non è iniettivo, quindi da $a^2 = b^2$ non segue $a = b$ (es. $(-2)^2 = 2^2$).

---

## 6. Funzioni reali e dominio naturale (slide 10)

**L'idea.** La calcolatrice dà "Errore" per alcuni numeri (es. divisione per zero): il **dominio naturale** è l'insieme dei numeri per cui non dà errore.

**Con i numeri.** $k(x) = \dfrac{x+3}{x-1}$

| $x$ | $x+3$ | $x-1$ | $k(x)$ |
|:-:|:-:|:-:|:-:|
| $0$ | $3$ | $-1$ | $-3$ |
| $1$ | $4$ | $0$ | **errore** |
| $2$ | $5$ | $1$ | $5$ |
| $3$ | $6$ | $2$ | $3$ |

$x - 1 = 0 \iff x = 1$, quindi $D = \mathbb{R} \setminus \{1\} = (-\infty, 1) \cup (1, +\infty)$: tutta la retta con un buco in $1$.

**I simboli del prof.** **Funzioni reali di una variabile reale**: dominio e codominio sono sottoinsiemi di $\mathbb{R}$. **Dominio naturale**: il più grande $D \subseteq \mathbb{R}$ tale che $f(x)$ ha senso per ogni $x \in D$.

**A cosa serve.** È il primo passo dello studio di funzione d'esame. Regole: frazione → denominatore $\neq 0$; radice quadrata → argomento $\geq 0$; logaritmo → argomento $> 0$.

---

## Esercizi svolti (21/10/2026 – 08/11/2026)

### Esercizio 1 – È un grafico di funzione? (mio, non del prof)

**Testo:** $A = \{-1,0,1,2\}$, $B = \{-1,0,1,2,3\}$, $G = \{(-1,3), (0,3), (1,-1), (2,0)\}$. È un grafico di funzione? Quanto vale $G(0)$?

**Mia risposta:** sì; $G(0) = 3$ (tabella ricavata dal grafico sul tablet).

**Esito:** ✅. Nota: non c'era nessuna formula da trovare, la funzione **è** l'elenco delle coppie.

### Esercizio 2 – Restrizione (mio)

**Testo:** $F(x) = x^2 - 1$ su $A$, $C = \{-1, 0\}$. Scrivi il grafico di $F|_C$.

**Mia risposta:** $(-1,2), (0,-1), (1,0), (2,3)$.

**Esito:** ❌ la restrizione tiene solo le $x$ di $C$, e $F(-1) = (-1)^2 - 1 = 0$ (non $2$):
$$F|_C = \{(-1, 0),\ (0, -1)\}$$

### Esercizio 3 – Immagine (mio)

**Testo:** $F(x) = x^2 - 1$, $C = \{0,1,2\}$. Calcola $F(C)$.

**Mia risposta:** $-1, 0, 3$.

**Esito:** ✅ $F(C) = \{-1, 0, 3\}$ (da scrivere tra graffe).

### Esercizio 4 – Controimmagine (mio)

**Testo:** $F(x) = x^2 - 1$ su $A = \{-1,0,1,2\}$, $D = \{0, 3\}$. Calcola $F^{-1}(D)$.

**Mia risposta:** $\{-1, 1, 2\}$.

**Esito:** ✅

### Esercizi di avviamento su iniettiva / suriettiva / biiettiva (miei)

| Domanda | Mia risposta | Esito |
|---|---|---|
| $g(x) = x^2 + 5$ su $\{-2,\dots,2\}$: iniettiva? | no: $9$ da $-2$ e $2$, $6$ da $-1$ e $1$ | ✅ |
| stessa $g$, arrivo $B = \{5,6,7,8,9\}$: suriettiva? | no, mancano $7$ e $8$ | ✅ |
| $g(x) = x^2 + 5$ su $\{0,1,2\}$, arrivo $\{5,6,9\}$: biiettiva? | sì | ✅ ($5, 6, 9$, nessuna ripetizione, nessun mancante) |

(La prima spiegazione delle tre definizioni, e poi l'esempio con bambini e sedie, non li avevo capiti: rifatte una alla volta con le tabelle dei risultati.)

### Esercizi 5–7 – $x^2$ con domini e codomini diversi (del prof, slide 8)

| Funzione | Domanda | Mia risposta | Esito |
|---|---|---|---|
| $f : \mathbb{R} \to \mathbb{R}$ | iniettiva? | no: $2$ e $-2$ | ✅ |
| $f : \mathbb{R} \to \mathbb{R}$ | suriettiva? | sì | ❌ $x^2 \geq 0$, quindi $-1$ non è mai un risultato: **non suriettiva** |
| $g : \mathbb{R}^+_0 \to \mathbb{R}$ | iniettiva? | sì | ✅ $-2$ non sta più nel dominio |
| $g : \mathbb{R}^+_0 \to \mathbb{R}$ | suriettiva? | no | ✅ |
| $h : \mathbb{R}^+_0 \to \mathbb{R}^+_0$ | biiettiva? | "non può" | ❌ è **biiettiva**: ogni $y \geq 0$ è un quadrato, $y = (\sqrt{y})^2$ (es. $2 = (\sqrt 2)^2$), non serve un quadrato perfetto |

### Ripasso del 02/11/2026 (miei)

$F(x) = x^2 - 1$ su $A = \{-2,-1,0,1\}$.

| Domanda | Mia risposta | Esito |
|---|---|---|
| colonna dei risultati | $3, 0, -1, 0$ | ✅ |
| iniettiva? | no, $-1$ e $1$ ("no è biiettiva") | ✅ non iniettiva; e quindi nemmeno biiettiva |
| immagine $F(A)$ | $3, 0, -1$ | ✅ $\{-1, 0, 3\}$ |
| con $B = \{-1,0,1,2,3\}$: suriettiva? | no, mancano $1$ e $2$ | ✅ |
| $F^{-1}(\{0\})$ | $-1$ e $1$ | ✅ $\{-1, 1\}$: è risolvere $x^2 - 1 = 0$ |

### Esercizio 8 – Lemma delle iniettive (mio)

**Testo:** usando che il cubo è iniettivo, risolvi $(x+2)^3 = (3x)^3$.

**Mia risposta:** $x = 1$.

**Esito:** ✅ $x + 2 = 3x \iff 2 = 2x \iff x = 1$; verifica $3^3 = 27 = 3^3$.

### Esercizio 9 – Dominio naturale (del prof, slide 10)

**Testo:** dominio naturale di $h(x) = \dfrac{2x+1}{x-2}$.

**Mia risposta:** $D = \{x \in \mathbb{R} : x \neq 2\} = \mathbb{R} \setminus \{2\}$.

**Esito:** ✅ ($h(2) = \frac{5}{0}$ non esiste).

### Esercizio 10 – Dominio naturale (mio)

**Testo:** dominio naturale di $m(x) = \dfrac{x+4}{2x-6}$.

**Mia risposta:** $D = \{x \in \mathbb{R} : x \neq 3\} = \mathbb{R} \setminus \{3\}$.

**Esito:** ✅ $2x - 6 = 0 \iff 2x = 6 \iff x = 3$.

---

## Dubbi aperti

- **Da verificare sul video:** la lezione alla lavagna del 02/10 è stata ricostruita dalle slide 2–10; esempi e disegni a griglia sono miei, non del prof.
- **Da ripassare:** sostituire e semplificare con i negativi, $(-1)^2 = +1$ (Esercizio 2).
- **Da ripassare:** suriettività su $\mathbb{R}$: controllare se esistono numeri dell'arrivo mai raggiunti (i negativi per $x^2$) e ricordare che ogni $y \geq 0$ è un quadrato tramite $\sqrt{y}$ (Esercizi 5–7).
- **Distinguere le parole:** "non iniettiva" e "non biiettiva" non sono la stessa domanda (ripasso del 02/11).

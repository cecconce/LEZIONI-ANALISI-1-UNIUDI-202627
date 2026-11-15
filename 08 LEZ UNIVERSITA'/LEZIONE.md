# 08 LEZ UNIVERSITA' – Grafico dell'inversa, funzioni monotone, valore assoluto

- **Docente:** prof. Lorenzo Freddi – Analisi Matematica 1, Università di Udine, a.a. 2026/27
- **Data della lezione:** 07/10/2026, videolezioni ore 8:33 (1 h 5 min) e ore 9:44 (37 min)
- **Studiata in chat:** 12/11/2026, 14/11/2026, 15/11/2026

## Argomenti trattati

La lezione riprende le dimostrazioni sull'inversa e arriva fino agli esercizi sul valore assoluto (**pres_02, slide 13–14 e 16–24**).

1. Ripresa delle dimostrazioni: unicità dell'inversa e invertibile $\iff$ biiettiva; esercizio $f^{-1}(C) = \{f^{-1}(y) : y \in C\}$ (slide 13–14)
2. Grafico della funzione inversa (slide 16–17)
3. Funzioni monotone (slide 18)
4. Monotonia della funzione inversa (slide 19)
5. Funzioni monotone e disequazioni (slide 20)
6. La funzione valore assoluto (slide 21)
7. Proprietà del valore assoluto, dalla 1 alla 8 (slide 22)
8. Disuguaglianza triangolare, dimostrazione passando ai quadrati (slide 23)
9. Esercizi sul valore assoluto (slide 24)

## Materiali su Drive (solo link)

- [2026_pres_02_funzioni.pdf](https://drive.google.com/file/d/10cclpI1x6npMY6ImQ7oINCC6LCPRbUuO/view) – slide del prof. Freddi (questa lezione: slide 13–14 e 16–24)

---

## 1. Ripresa delle dimostrazioni (slide 13–14)

**L'idea.** Se $f$ è "metti il cappotto", l'inversa è "togli il cappotto": c'è un solo modo di disfare $f$. Per poterla disfare servono le due regole del guardaroba: nessun numero dato a due cappotti, nessun numero rimasto senza cappotto.

**Con i numeri.** $f(x) = 2x + 3$, supponendo due inverse $g_1$, $g_2$ e provandole su $y = 5$:

| Passo | Cosa scrivo | Perché |
|---|---|---|
| 1 | $g_1(5) = a$ | è solo un nome |
| 2 | $f(a) = f(g_1(5)) = 5$ | $f \circ g_1 = \mathrm{id}_B$ |
| 3 | $g_2(f(a)) = a$ | $g_2 \circ f = \mathrm{id}_A$ |
| 4 | $g_2(5) = a$ | sostituisco $f(a) = 5$ |

**I simboli del prof.** Unicità, con ogni "=" giustificato:

$$g_1 \overset{(1)}{=} \mathrm{id}_A \circ g_1 \overset{(2)}{=} (g_2 \circ f) \circ g_1 \overset{(3)}{=} g_2 \circ (f \circ g_1) \overset{(4)}{=} g_2 \circ \mathrm{id}_B \overset{(5)}{=} g_2$$

| = | Giustificazione |
|---|---|
| (1) | $\mathrm{id}_A$ lascia $g_1(y)$ com'è |
| (2) | $g_2$ è inversa: $g_2 \circ f = \mathrm{id}_A$ |
| (3) | la composizione è associativa |
| (4) | $g_1$ è inversa: $f \circ g_1 = \mathrm{id}_B$ |
| (5) | $\mathrm{id}_B$ lascia $y$ com'è |

**Invertibile $\iff$ biiettiva.**
- ($\Rightarrow$) Iniettiva: $f(x_1) = f(x_2) \Rightarrow f^{-1}(f(x_1)) = f^{-1}(f(x_2)) \Rightarrow x_1 = x_2$. Suriettiva: dato $y$, prendo $x = f^{-1}(y)$ e $f(x) = y$ (con i numeri: $f^{-1}(9) = 3$, $f(3) = 9$).
- ($\Leftarrow$) Per ogni $y$ esiste un $x$ con $f(x) = y$ (suriettiva) ed è uno solo (iniettiva): pongo $g(y) = x$.

**Esercizio per casa, $f^{-1}(C) = \{f^{-1}(y) : y \in C\}$.** A sinistra la controimmagine (gli $x$ che $f$ manda dentro $C$), a destra ogni $y \in C$ riportato indietro con l'inversa. Con $f(x) = 2x + 3$ su $\{1, 2, 3\}$ e $C = \{5, 9\}$: sinistra $f(1) = 5$ sì, $f(2) = 7$ no, $f(3) = 9$ sì $\to \{1, 3\}$; destra $f^{-1}(5) = 1$, $f^{-1}(9) = 3 \to \{1, 3\}$.

**A cosa serve.** Dà senso al simbolo unico $f^{-1}$ ($\sqrt{x}$, $\ln x$, $\arcsin x$) e dà il test pratico per sapere se l'inversa esiste. La tecnica "suppongo che siano due e mostro che coincidono" torna nell'unicità del limite.

---

## 2. Grafico della funzione inversa (slide 16–17)

**L'idea.** Leggere la tabella al contrario: sul grafico ogni punto scambia le sue due coordinate.

**Con i numeri.** $f(x) = 2x + 3$, $f^{-1}(y) = \dfrac{y - 3}{2}$:

| Grafico di $f$ | Grafico di $f^{-1}$ |
|:-:|:-:|
| $(0, 3)$ | $(3, 0)$ |
| $(1, 5)$ | $(5, 1)$ |
| $(2, 7)$ | $(7, 2)$ |

**Disegno.**

```
        y=x  (specchio)
   f   /
   |  /   f⁻¹
   | /  ___/
   |/__/
───/──────────
  /
```

**I simboli del prof.**

$$(a, b) \in \operatorname{graf}(f) \iff b = f(a) \iff a = f^{-1}(b) \iff (b, a) \in \operatorname{graf}(f^{-1})$$

Equivale a scambiare gli assi oppure a riflettere il grafico rispetto alla bisettrice del primo e terzo quadrante, $y = x$.

**A cosa serve.** Disegnare $\sqrt{x}$ da $x^2$, $\ln x$ da $e^x$, $\arcsin x$ da $\sin x$ senza fare conti: serve nello studio di funzione.

---

## 3. Funzioni monotone (slide 18)

**L'idea.** Una scala che sale sempre è crescente; se ha pianerottoli è crescente solo "debolmente". Lo stesso in discesa.

**Con i numeri.**

| Tipo | $x=1$ | $x=2$ | $x=3$ | $x=4$ |
|---|:-:|:-:|:-:|:-:|
| strettamente crescente | $2$ | $4$ | $6$ | $8$ |
| strettamente decrescente | $12$ | $11$ | $10$ | $9$ |
| debolmente crescente (non decrescente) | $1$ | $1$ | $3$ | $3$ |
| debolmente decrescente (non crescente) | $7$ | $7$ | $5$ | $5$ |

**I simboli del prof.** Per $x_1 < x_2$ nel dominio:

| Tipo | Condizione |
|---|---|
| strettamente crescente | $f(x_1) < f(x_2)$ |
| strettamente decrescente | $f(x_1) > f(x_2)$ |
| debolmente crescente | $f(x_1) \le f(x_2)$ |
| debolmente decrescente | $f(x_1) \ge f(x_2)$ |

La differenza tra "stretta" e "debole" è solo $<$ contro $\le$.

**A cosa serve.** Risolvere disequazioni (punto 5); nello studio di funzione il segno della derivata dirà dove $f$ cresce e dove decresce.

---

## 4. Monotonia della funzione inversa (slide 19)

**L'idea.** L'inversa di una funzione che sale, sale anche lei; quella di una che scende, scende.

**Con i numeri.** $f(x) = 2x + 3$: $f^{-1}(5) = 1$, $f^{-1}(7) = 2$, $f^{-1}(9) = 3$ → crescente. $f(x) = 10 - x$: $f^{-1}(7) = 3$, $f^{-1}(9) = 1$ → decrescente.

**I simboli del prof.** Se $f$ è crescente (decrescente), anche $f^{-1}$ lo è. Dimostrazione (caso crescente), per assurdo: siano $y_1 < y_2$, $x_1 = f^{-1}(y_1)$, $x_2 = f^{-1}(y_2)$.

| Passo | Cosa scrivo | Perché |
|---|---|---|
| 1 | suppongo $x_1 \ge x_2$ | per assurdo |
| 2 | $f(x_1) \ge f(x_2)$ | $f$ crescente |
| 3 | $y_1 \ge y_2$ | $f(x_i) = y_i$ |
| 4 | impossibile | $y_1 < y_2$ |

Quindi $f^{-1}(y_1) < f^{-1}(y_2)$.

**A cosa serve.** Conoscere subito l'andamento di $\sqrt{x}$, $\ln x$ (crescenti) e $\arccos x$ (decrescente).

---

## 5. Funzioni monotone e disequazioni (slide 20)

**L'idea.** In una disequazione si "toglie" $f$ dai due lati: se $f$ sale il verso resta, se scende il verso si gira.

**Con i numeri.**

| | Disequazione | Confine | Soluzione |
|---|---|---|---|
| crescente $2x + 3$ | $2x + 3 \le 9$ | $f(3) = 9$ | $x \le 3$ (verso resta) |
| decrescente $10 - x$ | $10 - x \le 7$ | $f(3) = 7$ | $x \ge 3$ (verso girato) |

**I simboli del prof.**
- $f$ suriettiva e strettamente monotona $\Rightarrow$ $f$ invertibile.
- $f(x) \le f(y) \iff x \le y$ se $f$ è crescente; $f(x) \le f(y) \iff x \ge y$ se $f$ è decrescente.

**A cosa serve.** Spiega perché moltiplicando per un negativo il verso si gira ($x \mapsto -x$ è decrescente); si "tolgono" $\sqrt{\ }$, $e^x$, $\ln$ perché crescenti (pres_03).

---

## 6. La funzione valore assoluto (slide 21)

**L'idea.** È la distanza da zero, senza il verso: 3 km a est o 3 km a ovest sono sempre 3 km da casa.

**Con i numeri.**

| $x$ | $-3$ | $-2$ | $-1$ | $0$ | $1$ | $2$ | $3$ |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $\lvert x\rvert$ | $3$ | $2$ | $1$ | $0$ | $1$ | $2$ | $3$ |

**Disegno.** Una "V" con la punta in $(0, 0)$: a destra $y = x$, a sinistra $y = -x$.

**I simboli del prof.**

$$|x| = \begin{cases} x & \text{se } x \ge 0 \\ -x & \text{se } x < 0 \end{cases}$$

Attenzione alla seconda riga: $|-3| = -(-3) = +3$. Il modulo non è monotono su $\mathbb{R}$ né iniettivo ($|-3| = |3|$).

**A cosa serve.** $|x - y|$ è la distanza tra due numeri: la definizione di limite si scrive $|f(x) - L| < \varepsilon$.

---

## 7. Proprietà del valore assoluto (slide 22)

| N. | Proprietà | Controllo con i numeri |
|---|---|---|
| 1 | $\lvert x\rvert \ge 0$ | $\lvert -3\rvert = 3 \ge 0$ |
| 2 | $\lvert x\rvert = 0 \iff x = 0$ | solo $\lvert 0\rvert = 0$ |
| 3 | $\lvert x\rvert = \lvert -x\rvert$ | $\lvert 3\rvert = \lvert -3\rvert = 3$ |
| 4 | $\lvert x\rvert^2 = x^2$ | $\lvert -3\rvert^2 = 9 = (-3)^2$ |
| 5 | $\lvert xy\rvert = \lvert x\rvert\,\lvert y\rvert$ | $\lvert -6\rvert = 6 = 2 \cdot 3$ |
| 6 | $\left\lvert \frac{x}{y}\right\rvert = \frac{\lvert x\rvert}{\lvert y\rvert}$, $y \ne 0$ | $\lvert -2\rvert = 2 = \frac{6}{3}$ |
| 7 | $\lvert x+y\rvert \le \lvert x\rvert + \lvert y\rvert$ | disuguaglianza triangolare |
| 8 | $\lvert x-y\rvert \ge \big\lvert \lvert x\rvert - \lvert y\rvert \big\rvert$ | $x=5,\ y=-2$: $7 \ge 3$ |

**Dimostrazione della 8.** $|x| = |(x - y) + y| \le |x - y| + |y|$, quindi $|x| - |y| \le |x - y|$; scambiando $x$ e $y$, $|y| - |x| \le |x - y|$. Le due insieme, con $|a| \le k \iff -k \le a \le k$, danno la tesi.

**A cosa serve.** La 4 è il trucco della disuguaglianza triangolare; la 5 e la 6 servono a spezzare i moduli nei limiti; la 8 dice che se $f(x)$ è vicino a $L$ anche $|f(x)|$ è vicino a $|L|$.

---

## 8. Disuguaglianza triangolare (slide 23)

**L'idea.** Casa → bar → piazza: la distanza casa–piazza non supera mai la somma dei due tratti. Se torno indietro, sono più vicino di quanto ho camminato.

**Con i numeri.**

| $x$ | $y$ | $\lvert x+y\rvert$ | $\lvert x\rvert + \lvert y\rvert$ |
|:-:|:-:|:-:|:-:|
| $3$ | $5$ | $8$ | $8$ (stesso segno: uguali) |
| $3$ | $-5$ | $2$ | $8$ (segni opposti: minore) |

Passando ai quadrati con $x = 3$, $y = -5$: $(x+y)^2 = 9 - 30 + 25 = 4$ e $(|x| + |y|)^2 = 9 + 30 + 25 = 64$. Cambia solo il termine centrale.

**I simboli del prof.**

$$|x+y|^2 = (x+y)^2 = x^2 + 2xy + y^2 \le |x|^2 + 2|x|\,|y| + |y|^2 = (|x|+|y|)^2$$

perché $xy \le |xy| = |x|\,|y|$. Entrambi i membri sono $\ge 0$ e la radice è crescente, quindi $|x+y| \le |x| + |y|$.

**A cosa serve.** È lo strumento principe per le stime nei limiti; dimostrazione classica dell'orale.

---

## 9. Esercizi sul valore assoluto (slide 24)

**$|x| \le k \iff -k \le x \le k$ ($k \ge 0$).** "Sto a non più di 3 km da casa" = sono tra il km $-3$ e il km $3$. Dimostrazione nei due casi: per $x \ge 0$ diventa $x \le k$; per $x < 0$ diventa $-x \le k$, cioè $x \ge -k$. Serve a togliere i moduli: $|f(x) - L| < \varepsilon \iff L - \varepsilon < f(x) < L + \varepsilon$.

**$x = 0 \iff |x| < \varepsilon$ per ogni $\varepsilon > 0$.** Solo lo zero passa con tutte le soglie. ($\Rightarrow$) $|0| = 0 < \varepsilon$. ($\Leftarrow$) per contronominale: se $x \ne 0$, con $\varepsilon = \frac{|x|}{2}$ la disuguaglianza $|x| < \frac{|x|}{2}$ è falsa (con i numeri: $x = 0{,}6$, $\varepsilon = 0{,}3$). Serve per dimostrare che due numeri sono uguali, per esempio nell'unicità del limite.

**$|x + 3| - |2x - 1| \le x + 1$.** I moduli cambiano riga in $x = -3$ e in $x = \frac12$:

| Zona | Primo membro | Disequazione | Soluzione nella zona |
|---|---|---|---|
| A: $x < -3$ | $(-x-3) - (-2x+1) = x - 4$ | $-4 \le 1$, sempre vera | $x < -3$ |
| B: $-3 \le x < \frac12$ | $(x+3) - (-2x+1) = 3x + 2$ | $2x \le -1$ | $-3 \le x \le -\frac12$ |
| C: $x \ge \frac12$ | $(x+3) - (2x-1) = -x + 4$ | $-2x \le -3$ | $x \ge \frac32$ |

$$S = \left(-\infty, -\tfrac12\right] \cup \left[\tfrac32, +\infty\right)$$

Controlli: $x = -10$ sì, $x = 0$ no, $x = 1$ no, $x = 2$ sì.

---

## Esercizi svolti (12/11/2026 – 15/11/2026)

### Inversa e monotonia

| Domanda | Mia risposta | Esito |
|---|---|---|
| Nella catena dell'unicità, quale condizione si usa per $g_1$ e quale per $g_2$? (slide 13) | $f \circ g_1 = \mathrm{id}_B$, $g_2 \circ f = \mathrm{id}_A$ | ✅ |
| $A = \{1,2,3\}$, $B = \{5,7\}$, $1 \to 5$, $2 \to 7$, $3 \to 7$: ha l'inversa? (mio) | sì | ❌ il $7$ è ripetuto: **no** |
| $f^{-1}(C)$ con $f(x) = 2x+3$, $C = \{7, 9\}$ (prof, slide 13) | ho tenuto i sì/no del caso $C = \{5, 9\}$ | ❌ con $C$ nuovo si rifà da capo: $\{2, 3\}$ |
| Stesso esercizio con $C = \{5, 7\}$: sì/no per $x = 1, 2, 3$ | sì, sì, no | ✅ sinistra $\{1, 2\}$ |
| Stesso: $f^{-1}(5)$ e $f^{-1}(7)$ | $1$ e $2$ | ✅ destra $\{1, 2\}$ |
| $(4, 11)$ sta sul grafico di $f$: quale punto sta su quello di $f^{-1}$? (mio) | $(11, 4)$ | ✅ |
| Tabella $4, 4, 6$: che tipo di funzione? (mio) | debolmente crescente | ✅ |
| $f(x) = 10 - x$: $f^{-1}(7)$, $f^{-1}(9)$, monotonia (prof, slide 19) | $3$, $1$, decrescente | ✅ |
| $10 - x \le 8$ (mio) | $x = 2$ | ❌ è il confine; la soluzione è $x \ge 2$ |
| $10 - x \le 6$ (mio) | $x \ge 4$ | ✅ |

### Valore assoluto

| Domanda | Mia risposta | Esito |
|---|---|---|
| $\lvert -4\rvert$ con la riga giusta (mio) | $-4 < 0$, $\lvert -4\rvert = -(-4) = 4$ | ✅ |
| Proprietà 5 con $x = -3$, $y = 4$ (mio) | $\lvert -12\rvert = \lvert -3\rvert\,\lvert 4\rvert$ | ✅ $12 = 12$ |
| $\lvert x+y\rvert$ e $\lvert x\rvert + \lvert y\rvert$ con $x = -4$, $y = 1$ (mio) | $3$ e $9$ | ❌ $\lvert -4\rvert + \lvert 1\rvert = 5$ |
| Stesso con $x = -6$, $y = 2$ (mio) | $4$ e $8$ | ✅ |
| Proprietà 8 con $x = -7$, $y = 3$ (mio) | $10$ e $4$ | ✅ |
| $\lvert x\rvert \le 5$ (stessa forma della slide 24) | $-5 \le x \le 5$ | ✅ |
| $x = -0{,}6$: $\lvert x\rvert$, soglia del prof e verifica (slide 24) | $0{,}6$; $0{,}3$; no | ✅ (dopo aver rifatto la spiegazione con le tabelle) |

### Disequazione $|x+3| - |2x-1| \le x + 1$ (del prof, slide 24)

| Passo | Mia risposta | Esito |
|---|---|---|
| $x + 3 = 0$ | $-3$ | ✅ |
| $2x - 1 = 0$ | $\frac12$ | ✅ |
| Zona A, primo membro | $x - 4$ | ✅ |
| Zona A, $x - 4 \le x + 1$ | vero | ✅ tutta la zona |
| Zona B, primo membro | $x + 3 + 2x - 1 = 3x + 2$ | ✅ |
| Zona B, disequazione | $2x \le -1$, $x \le -\frac12$ | ✅ |
| Zona C, primo membro | $-x + 4$ | ✅ |
| Zona C, disequazione | $-2x \le -3$, $x \ge \frac32$ | ✅ |

**Risultato:** $x \le -\frac12$ oppure $x \ge \frac32$. ✅

---

## Dubbi aperti

- **Da verificare sul video:** l'esercizio $|x+3| - |2x-1| \le x + 1$ (slide 24) è stato svolto dal prof il 07/10 o lasciato per casa? Nella scheda non compare.
- **Da verificare sul video:** le dimostrazioni delle slide 13–14 sono del 06/10 o del 07/10 (dubbio della lezione 07, ancora aperto).
- **Da ripassare:** nelle disequazioni la soluzione è un insieme ($x \ge 2$), non solo il numero di confine.
- **Da ripassare:** se una regola non vale (risultato ripetuto), la risposta è "non ha l'inversa".
- **Da ripassare:** quando cambia l'insieme $C$, i "sì/no" vanno rifatti da capo.
- **Da ripassare:** in $|x| + |y|$ si prende il modulo di ciascuno e poi si somma.
- **Da rivedere:** $x = 0 \iff |x| < \varepsilon\ \forall \varepsilon > 0$ l'ho capito solo con le tabelle di soglie; da rifare con i simboli.

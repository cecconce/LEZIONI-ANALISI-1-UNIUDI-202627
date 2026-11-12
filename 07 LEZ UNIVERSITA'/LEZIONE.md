# 07 LEZ UNIVERSITA' – Funzione composta, funzione inversa, invertibile ⇔ biiettiva

- **Docente:** prof. Lorenzo Freddi – Analisi Matematica 1, Università di Udine, a.a. 2026/27
- **Data della lezione:** 06/10/2026, videolezioni ore 8:30 (1 h 12 min) e ore 9:54 (25 min)
- **Studiata in chat:** 08/11/2026, 10/11/2026, 11/11/2026, 12/11/2026

## Argomenti trattati

La lezione riparte da «Funzioni composte» e arriva fino agli esercizi sull'inversa (**pres_02, slide 11–15**).

1. Funzione composta $g \circ f$ (slide 11)
2. Funzione inversa e funzione invertibile; l'esempio $A = \{a\}$, $B = \{a, b\}$ (slide 12)
3. Teorema di unicità dell'inversa e notazione $f^{-1}$ (slide 13)
4. Teorema: $f$ è invertibile $\iff$ $f$ è biiettiva (slide 14)
5. Esercizi: inversa di $f(x) = 2x + 3$ e di $f(x) = ax + b$ (slide 15)

## Materiali su Drive (solo link)

- [2026_pres_02_funzioni.pdf](https://drive.google.com/file/d/10cclpI1x6npMY6ImQ7oINCC6LCPRbUuO/view) – slide del prof. Freddi (questa lezione: slide 11–15)

---

## 1. Funzione composta (slide 11)

**L'idea.** Una catena di montaggio con due macchine: l'uscita della prima entra nella seconda. Serve che la seconda macchina accetti tutto quello che esce dalla prima.

**Con i numeri.** Esempio del prof: $f(x) = x^2 + 1$ (macchina "dentro"), $g(y) = \sqrt{y}$ (macchina "fuori").

| $x$ | $f(x) = x^2 + 1$ | $g(f(x)) = \sqrt{\ \cdot\ }$ |
|:-:|:-:|:-:|
| $0$ | $1$ | $1$ |
| $1$ | $2$ | $\sqrt{2}$ |
| $2$ | $5$ | $\sqrt{5}$ |
| $3$ | $10$ | $\sqrt{10}$ |
| $-3$ | $10$ | $\sqrt{10}$ |

La colonna centrale è sempre $\geq 1$, quindi la radice non si blocca mai.

**Disegno.**

```
A ──f──▶ B ⊆ C ──g──▶ D
x ─────▶ f(x) ──────▶ g(f(x))
└──────────── g∘f ──────────┘
```

**I simboli del prof.** Se $f : A \to B$ e $g : C \to D$, con $B \subseteq C$:

$$g \circ f : A \to D, \qquad x \mapsto (g \circ f)(x) := g\big(f(x)\big)$$

Si legge **"g dopo f"**: si applica per prima la funzione più vicina alla $x$. Nell'esempio $h(x) = g(f(x)) = \sqrt{x^2 + 1}$. Il prof scrive $g(y)$ per ricordare che $g$ riceve il **risultato** di $f$.

**A cosa serve.** Spezzare una funzione complicata in pezzi semplici ("dentro" e "fuori"). Tornerà nella regola della catena per le derivate, $(g \circ f)' = g'(f(x)) \cdot f'(x)$, nei limiti, nell'integrazione per sostituzione e nel dominio dello studio di funzione (la condizione $B \subseteq C$). Serve subito per definire l'inversa.

---

## 2. Funzione inversa (slide 12)

**L'idea.** Un traduttore: $f$ traduce dall'italiano all'inglese, l'inversa dall'inglese all'italiano. Andata e ritorno riportano al punto di partenza.

**Con i numeri** (esempio mio): $f(x) = x + 5$ e $g(y) = y - 5$.

| $x$ | $f(x) = x + 5$ | $g(f(x))$ |
|:-:|:-:|:-:|
| $0$ | $5$ | $0$ ✔ |
| $2$ | $7$ | $2$ ✔ |
| $-3$ | $2$ | $-3$ ✔ |

Anche al contrario: $y = 7 \to g(7) = 2 \to f(2) = 7$ ✔.

**Disegno.**

```
     f
A ───────▶ B
  ◀───────
     g
```

**I simboli del prof.** $g : B \to A$ è **inversa** di $f : A \to B$ se

$$g \circ f = \mathrm{id}_A \qquad \text{e} \qquad f \circ g = \mathrm{id}_B$$

$f$ si dice **invertibile** se ha un'inversa.

**Esempio del prof:** tra $A = \{a\}$ e $B = \{a, b\}$ non esiste nessuna funzione invertibile. Ogni $g : B \to A$ manda tutto in $a$: la prima condizione funziona sempre, la seconda fallisce sempre (1 elemento contro 2). L'esempio mostra che **servono tutte e due** le condizioni.

**A cosa serve.** Risolvere $f(x) = y$ significa calcolare $x = f^{-1}(y)$. Radice, logaritmo, arcoseno e arcotangente sono tutte inverse.

---

## 3. Unicità dell'inversa (slide 13)

**L'idea.** Due traduttori perfetti danno la stessa risposta su ogni parola: sono lo stesso traduttore. Una funzione non può avere due inverse diverse.

**Con i numeri.**

| $x$ | $f(x)$ |
|:-:|:-:|
| $1$ | $10$ |
| $2$ | $20$ |

L'unica inversa è $10 \to 1$, $20 \to 2$. Se cambio una riga (per esempio $10 \to 2$), il ritorno si rompe: $g_2(f(1)) = g_2(10) = 2 \neq 1$ ✘.

**Attenzione: sono due cose diverse.**
- Non tutte le funzioni hanno un'inversa: se $1 \to 10$ e $2 \to 10$, al ritorno $10$ non sa dove andare.
- Se l'inversa c'è, è **una sola**.

**I simboli del prof.**

> **Teorema.** Se $f : A \to B$ è invertibile, la sua inversa è unica; si indica con $f^{-1}$.

**Dimostrazione.** Siano $g_1, g_2$ due inverse di $f$:

$$g_1 = \mathrm{id}_A \circ g_1 = (g_2 \circ f) \circ g_1 = g_2 \circ (f \circ g_1) = g_2 \circ \mathrm{id}_B = g_2$$

Si usano: $g_2 \circ f = \mathrm{id}_A$ ($g_2$ è inversa), lo spostamento delle parentesi (la composizione è associativa), $f \circ g_1 = \mathrm{id}_B$ ($g_1$ è inversa).

**A cosa serve.** Dà senso al simbolo $f^{-1}$ e alle parole "**la** radice", "**il** logaritmo". Per l'orale è una dimostrazione corta da sapere con la giustificazione di ogni "=".

---

## 4. Invertibile ⇔ biiettiva (slide 14)

**L'idea.** Il viaggio di ritorno può andare storto in due modi.

| problema | esempio | perché il ritorno fallisce |
|---|---|---|
| risultato ripetuto (non iniettiva) | $1 \to 10$, $2 \to 10$ | $10$ dovrebbe tornare in $1$ o in $2$? |
| numero dell'arrivo mancante (non suriettiva) | $1 \to 10$, $2 \to 20$, con $B = \{10, 20, 30\}$ | $30$ non ha da dove tornare |
| tutto a posto (biiettiva) | $1 \to 10$, $2 \to 20$, con $B = \{10, 20\}$ | ritorno $10 \to 1$, $20 \to 2$ ✔ |

**I simboli del prof.**

> **Teorema.** $f : A \to B$ è invertibile $\iff$ $f$ è biiettiva.

**Dimostrazione.**

($\Rightarrow$) *Iniettiva.* Con i numeri ($f(x) = x + 5$, $g(y) = y - 5$): se $f(x_1) = f(x_2) = 7$, allora $x_1 = g(7) = 2$ e $x_2 = g(7) = 2$. Con le lettere:

$$f(x_1) = f(x_2) \implies x_1 = f^{-1}(f(x_1)) = f^{-1}(f(x_2)) = x_2$$

(si usa $f^{-1} \circ f = \mathrm{id}_A$).

($\Rightarrow$) *Suriettiva.* Con i numeri: per $y = 20$ prendo $x = g(20) = 15$ e $f(15) = 20$ ✔. Con le lettere: dato $y \in B$, preso $x = f^{-1}(y)$ si ha $f(x) = f(f^{-1}(y)) = y$ (si usa $f \circ f^{-1} = \mathrm{id}_B$).

($\Leftarrow$) Se $f$ è biiettiva, per ogni $y \in B$ esiste (suriettività) un $x \in A$, unico (iniettività), con $f(x) = y$. Pongo $g(y) := x$, cioè **giro le frecce**:

| $x$ | $f(x)$ | | $y$ | $g(y)$ |
|:-:|:-:|---|:-:|:-:|
| $1$ | $20$ | | $10$ | $3$ |
| $2$ | $30$ | | $20$ | $1$ |
| $3$ | $10$ | | $30$ | $2$ |

La $g$ così costruita è l'inversa di $f$. $\blacksquare$

**A cosa serve.** Per sapere se una funzione ha l'inversa basta controllare le due regole, senza cercarla. Esempio: $x^2$ su $\mathbb{R}$ ha risultati ripetuti, quindi non ha inversa; ristretta a $[0, +\infty)$ ha come inversa $\sqrt{\ }$. Lo schema "$\Rightarrow$ e $\Leftarrow$" è il modello per le dimostrazioni dell'orale.

---

## 5. Esercizi sull'inversa (slide 15)

**Il metodo** (rivisto su $f(x) = x + 5$):

| passo | cosa si fa | con $x + 5$ |
|---|---|---|
| ① | scrivo $y = f(x)$ | $y = x + 5$ |
| ② | ricavo $x$ | $x = y - 5$ |
| ③ | quello che trovo è l'inversa | $f^{-1}(y) = y - 5$ |

Se al passo ② c'è **una sola** $x$ per ogni $y$, la funzione è biiettiva e quindi invertibile.

**I simboli del prof.** Per $f(x) = ax + b$ con $a \neq 0$:

$$f^{-1}(y) = \frac{y - b}{a}$$

Serve $a \neq 0$ perché all'ultimo passo si divide per $a$. Con $a = 0$ si ha $f(x) = b$ per ogni $x$: tutti i risultati sono uguali e manca il resto dell'arrivo, quindi non c'è inversa.

**A cosa serve.** È il metodo generale per trovare un'inversa: "ricavare la $x$". Le funzioni affini tornano nelle funzioni elementari (pres_04).

---

## Esercizi svolti (08/11/2026 – 12/11/2026)

### Esercizio 1 – Composta su un numero (sull'esempio del prof, slide 11)

**Testo:** con $f(x) = x^2 + 1$ e $g(y) = \sqrt{y}$, calcola $h(-3)$.

**Mia risposta:** $\sqrt{10}$.

**Esito:** ✅ $f(-3) = (-3)^2 + 1 = 10$, $h(-3) = \sqrt{10}$. Nota: anche $h(3) = \sqrt{10}$, quindi $h$ non è iniettiva.

### Esercizio 2 – Riconoscere "dentro" e "fuori" (mio)

**Testo:** $h(x) = \sqrt{x^2 + 4}$ è $g \circ f$: chi sono $f$ e $g$?

**Mia risposta:** $h(x) = g(f(x)) = g\big(\sqrt{x^2 + 4}\big) = \sqrt{x^2 + 4}$.

**Esito:** ❌ dentro $g$ va solo la funzione "dentro", senza radice: $f(x) = x^2 + 4$, $g(y) = \sqrt{y}$.

### Esercizi di avviamento sull'inversa (miei)

| Domanda | Mia risposta | Esito |
|---|---|---|
| $f(x) = x + 5$, $g(y) = y - 5$: calcola $f(g(-2))$ | $g(-2) = -7$, $f(-7) = -2$ | ✅ |
| $1 \to 10$, $2 \to 20$: quanto vale $f^{-1}(20)$? | $2$ | ✅ |
| $1 \to 30$, $2 \to 40$: ha l'inversa? | sì | ✅ uscite diverse, ritorno $30 \to 1$, $40 \to 2$ |
| $A = \{1,2,3\}$, $B = \{5,6\}$, $1 \to 5$, $2 \to 6$, $3 \to 6$: ha l'inversa? | "sì, risultato ripetuto" | ❌ il motivo è giusto, ma allora la risposta è **no** |
| $f(x) = x + 5$: se $f(x_1) = 12$, quanto vale $x_1$? | $7$ | ✅ $g(12) = 7$ |
| da quale $x$ parto per arrivare a $y = 3$? | $-2$ | ✅ $g(3) = -2$, $f(-2) = 3$ |
| tabella $1 \to 20$, $2 \to 30$, $3 \to 10$: quanto vale $f^{-1}(30)$? | $2$ | ✅ |

### Esercizio 3 – Inversa di $f(x) = 2x + 3$ (del prof, slide 15)

**Mia risposta:** $f^{-1}(y) = \dfrac{y - 3}{2}$.

**Esito:** ✅ Con i numeri: $f(4) = 11$, $f^{-1}(11) = \frac{8}{2} = 4$. Con le lettere: $f^{-1}(f(x)) = \frac{2x}{2} = x$ e $f(f^{-1}(y)) = (y - 3) + 3 = y$.

### Esercizio 4 – Inversa di $f(x) = ax + b$, $a \neq 0$ (del prof, per casa, slide 15)

**Mia risposta:** $x = \dfrac{y - b}{a}$.

**Esito:** ✅ Passaggio intermedio $y - b = ax$. Verifica: $f^{-1}(f(x)) = \frac{ax}{a} = x$ e $f(f^{-1}(y)) = (y - b) + b = y$. Con $a = 2$, $b = 3$ si ritrova l'Esercizio 3.

---

## Dubbi aperti

- **Da verificare sul video:** le dimostrazioni delle slide 13–14 sono state fatte il 06/10 o riprese il 07/10? Secondo la scheda il prof le riprende il 07/10.
- **Da rifare:** la dimostrazione dell'unicità con i simboli ($g_1 = \mathrm{id}_A \circ g_1 = \dots = g_2$), giustificando ogni "=". L'ho capita solo con le tabelle di numeri.
- **Da ripassare:** nella composta $g(f(x))$, dentro $g$ va solo la funzione "dentro" (Esercizio 2).
- **Da ripassare:** quando una regola non vale (risultato ripetuto o numero mancante), la risposta è "non ha l'inversa".

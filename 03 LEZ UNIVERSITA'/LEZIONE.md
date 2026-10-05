# 03 LEZ UNIVERSITA' – Logica: contronominale, quantificatori, insiemi

- **Docente:** prof. Lorenzo Freddi – Analisi Matematica 1, Università di Udine, a.a. 2026/27
- **Data della lezione:** 29/09/2026 (videolezione)
- **Studiata in chat:** 05/10/2026

## Argomenti trattati

1. Teorema della contronominale (slide 16)
2. Lemma: $n$ pari $\iff n^2$ pari, dimostrato con la contronominale (slide 17)
3. Predicati $P(x)$, quantificatori $\forall$ ed $\exists$, insiemi definiti da una proprietà (lavagna)
4. Insieme delle parti $\mathcal{P}(A)$ (lavagna, da studiare)

## Materiali su Drive (solo link)

- [2026_pres_01_logica_e_insiemi.pdf](https://drive.google.com/file/d/1K72wRUI-xyKGGE2JaSwpFnFshwy3CFT6/view?usp=drivesdk) – slide del prof. Freddi
- `2026_pres_02_funzioni.pdf` – slide della lezione successiva: **non ancora caricate su Drive**, link da aggiungere

---

## Teorema della contronominale

### L'enunciato

$$P \Longrightarrow Q \quad \text{equivale a} \quad (\text{non } Q) \Longrightarrow (\text{non } P)$$

La frase $(\text{non } Q) \Rightarrow (\text{non } P)$ si chiama **contronominale** di $P \Rightarrow Q$.
Le due frasi dicono **la stessa cosa**: se una è vera, è vera anche l'altra.

### Ricetta per costruirla

1. **Nego** tutti e due i pezzi ("non" = negazione = il contrario: V diventa F, F diventa V).
2. **Scambio** l'ordine.

Servono **tutte e due** le cose. Una sola non basta.

### L'idea, con un esempio

Il papà (onesto) promette: **"Se prendi 10, ti compro la bici."**

Il figlio torna a casa e la bici **non c'è**. Allora il figlio **non ha preso 10**.

| | Frase |
|---|---|
| Originale | se prendi 10 → bici |
| Contronominale | niente bici → non hai preso 10 |

### La regola dell'implicazione

"Se A, allora B" è **falsa solo in un caso**: A vera e B falsa.
(Il papà mente solo se il figlio prende 10 e la bici non arriva. Se il figlio prende 6, la promessa non dice niente: il papà non mente qualunque cosa faccia.)

| A | B | A ⇒ B |
|:-:|:-:|:-:|
| V | V | V |
| V | F | **F** |
| F | V | V |
| F | F | V |

### Dimostrazione con la tabella di verità (come nella slide)

$P$ = "ha preso 10", $Q$ = "c'è la bici".

| Caso | $P$ | $Q$ | $\text{non } Q$ | $\text{non } P$ | $P \Rightarrow Q$ | $(\text{non } Q) \Rightarrow (\text{non } P)$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | V | V | F | F | **V** | **V** |
| 2 | V | F | V | F | **F** | **F** |
| 3 | F | V | F | V | **V** | **V** |
| 4 | F | F | V | V | **V** | **V** |

Come si riempie:
1. $P$ e $Q$: tutte le 4 combinazioni (VV, VF, FV, FF).
2. $\text{non } Q$ e $\text{non } P$: ribalto le colonne $Q$ e $P$.
3. $P \Rightarrow Q$: F solo dove $P$ = V e $Q$ = F (caso 2).
4. $(\text{non } Q) \Rightarrow (\text{non } P)$: F solo dove $\text{non } Q$ = V e $\text{non } P$ = F (di nuovo caso 2).

**Le ultime due colonne sono uguali (V, F, V, V) → le due frasi sono equivalenti.** ∎

### Attenzione: le due frasi che NON sono equivalenti

Partendo da "divisibile per 4 → pari":

| Nome | Frase | Vera? |
|:-:|:-:|:-:|
| Originale | divisibile per 4 → pari | ✅ |
| **Contronominale** (nego e scambio) | non pari → non divisibile per 4 | ✅ sempre come l'originale |
| Inversa (solo scambio) | pari → divisibile per 4 | ❌ |
| Contraria (solo "non") | non divisibile per 4 → non pari | ❌ |

Controesempio per le due false: **6** (è pari ma non è divisibile per 4).

### A cosa serve davvero

È uno strumento di dimostrazione: se dimostrare $P \Rightarrow Q$ direttamente è difficile, dimostro $\text{non } Q \Rightarrow \text{non } P$.

Si usa anche negli esercizi:

- **Derivabilità.** Teorema: derivabile in $x_0$ ⇒ continua in $x_0$.
  Contronominale: **non continua** in $x_0$ ⇒ **non derivabile** in $x_0$.
  Uso: vedo un salto nel grafico → lì la derivata non esiste, senza fare conti.
  (L'inversa "continua ⇒ derivabile" è falsa: $f(x) = |x|$ in $0$ è continua ma ha una punta.)

- **Serie.** Teorema: $\sum a_n$ converge ⇒ $a_n \to 0$.
  Contronominale: $a_n \not\to 0$ ⇒ $\sum a_n$ **non converge**.
  Esempio: $\sum \frac{n}{n+1}$, il termine tende a $1$, quindi la serie non converge.
  (Attenzione: $a_n \to 0$ **non basta** per dire che converge.)

---

## Lemma: $n$ pari $\iff n^2$ pari

Un esempio in cui il prof **usa** la contronominale (slide 17).

Sia $n$ un numero intero. Allora

$$n \text{ pari} \iff n^2 \text{ pari}$$

Il simbolo $\iff$ vuol dire "vale nei due sensi". Bisogna dimostrare due frasi:

1. $n$ pari $\Rightarrow n^2$ pari
2. $n^2$ pari $\Rightarrow n$ pari

### Definizioni usate

- $n$ **pari**: esiste un intero $k$ tale che $n = 2k$
- $n$ **dispari**: esiste un intero $k$ tale che $n = 2k + 1$ ("un pari più uno")

### Frase 1: $n$ pari $\Rightarrow n^2$ pari (dimostrazione diretta)

Con i numeri: $4^2 = 16$, $6^2 = 36$, sono pari.

Con le lettere:

$$n = 2k \;\Longrightarrow\; n^2 = (2k)^2 = 4k^2 = 2\,(2k^2) \;\Longrightarrow\; n^2 \text{ pari}$$

### Frase 2: $n^2$ pari $\Rightarrow n$ pari (con la contronominale)

**Perché non direttamente:** da $n^2 = 2k$ dovrei fare $n = \sqrt{2k}$, e da lì non si capisce niente.

**Giro la frase** (nego e scambio):

$$n^2 \text{ pari} \Rightarrow n \text{ pari} \quad\longrightarrow\quad n \text{ dispari} \Rightarrow n^2 \text{ dispari}$$

Questa va da $n$ a $n^2$: basta elevare al quadrato, niente radici.

Con i numeri: $3^2 = 9$, $5^2 = 25$, $7^2 = 49$, sono dispari.

Con le lettere, usando $(a+b)^2 = a^2 + 2ab + b^2$:

$$n^2 = (2k+1)^2 = 4k^2 + 4k + 1 = \underbrace{2\,(2k^2 + 2k)}_{\text{pari}} + 1 \;\Longrightarrow\; n^2 \text{ dispari}$$

Controllo con $n = 7$ ($k = 3$): $4 \cdot 9 + 4 \cdot 3 + 1 = 36 + 12 + 1 = 49$ ✅

### Conclusione

- Dimostrato: $n$ dispari $\Rightarrow n^2$ dispari
- Per la contronominale: $n^2$ pari $\Rightarrow n$ pari
- Con la frase 1: $n$ pari $\iff n^2$ pari ∎

**Il succo:** la contronominale si usa quando la strada diretta è in salita. Giro la frase e la percorro in discesa.

---

## Predicati, quantificatori, insiemi definiti da una proprietà

Riassunto di quello che si vedeva alla lavagna.

### $P(x)$: una frase con una variabile

$P(x)$ è una frase che contiene una lettera. Da sola non è né vera né falsa: **dipende da cosa metto al posto della lettera**.

Esempio: $P(n)$ = "$n$ è pari"

| $n$ | $P(n)$ | V/F |
|:-:|:-:|:-:|
| 4 | "4 è pari" | V |
| 7 | "7 è pari" | F |
| 10 | "10 è pari" | V |

### I simboli

| Simbolo | Si legge |
|:-:|---|
| $\exists$ | **esiste** |
| $\forall$ | **per ogni** |
| $\in$ | appartiene a |
| $:$ | **tale che** |
| $\mathbb{N}$ | numeri naturali $\{0, 1, 2, 3, \dots\}$ (per il prof Freddi **lo 0 è incluso**) |

### "$n$ è pari" scritto in matematica

$$P(n): \quad \exists\, k \in \mathbb{N} : n = 2k$$

"Esiste un naturale $k$ tale che $n = 2k$."

| $n$ | Trovo $k$ con $n = 2k$? | $P(n)$ |
|:-:|:-:|:-:|
| 4 | sì, $k = 2$ | V |
| 7 | no, $7/2 = 3{,}5$ | F |
| 10 | sì, $k = 5$ | V |

### Un insieme costruito con una frase

$$\{\, n \in \mathbb{N} : \exists\, k \in \mathbb{N} : n = 2k \,\} = \{0, 2, 4, 6, \dots\}$$

"L'insieme dei naturali $n$ per cui la frase è vera" = i numeri pari.
Il primo "$:$" separa **chi** (i naturali) dalla **condizione** che devono rispettare.

### Esempio con $\forall$

"$\forall n \in \mathbb{N}$, $2n$ è pari" = "per ogni naturale $n$, il suo doppio è pari" (vera).

### A cosa serve

$\forall$ ed $\exists$ sono le parole su cui è scritta tutta l'Analisi. La definizione di limite (che chiedono all'orale) è: "**per ogni** $\varepsilon > 0$ **esiste** $\delta > 0$ tale che…". Se so leggere questi simboli, so leggere le definizioni.

### Da studiare: insieme delle parti

Alla lavagna: $\mathcal{P}(A) = \{ B : B \subseteq A \}$ = **insieme delle parti** di $A$ (o **potenza** di $A$).
Se $A$ ha $n$ elementi, $\mathcal{P}(A)$ ha $2^n$ elementi.

---

## Esercizi svolti (05/10/2026)

### Esercizio 1 – Contronominale

**Testo:** scrivi la contronominale di "se un numero è divisibile per 4, allora è pari".

**Mia risposta:** non è pari ⇒ non è divisibile per 4.

**Esito:** ✅ corretta. Verifica: 7 non è pari e infatti non è divisibile per 4.

### Esercizio 2 – Classificare le quattro frasi

**Testo:** partendo da "derivabile in $x_0$ ⇒ continua in $x_0$", dire di che tipo è "continua ⇒ derivabile" e se è vera.

**Mia risposta:**

| Tipo | Frase | Vera? |
|:-:|:-:|:-:|
| Contronominale | non continua ⇒ non derivabile | ✅ |
| Inversa | continua ⇒ derivabile | ❌ |
| Contraria | non derivabile ⇒ non continua | ❌ |

**Esito:** ✅ tutto corretto. "Continua ⇒ derivabile" è l'inversa, quindi falsa.
Controesempio: $f(x) = |x|$ in $x_0 = 0$ è continua ma non derivabile (c'è una punta).

### Esercizio 3 – Leggere un insieme

**Testo:** leggi in italiano $\{\, n \in \mathbb{N} : \exists\, k \in \mathbb{N} : n = 3k \,\}$ e scrivi i primi 4 numeri.

**Mia risposta:** $k = 1 \to 3$, $k = 2 \to 6$, $k = 3 \to 9$.

**Esito:** quasi corretta, due correzioni:
- **Manca lo 0**: per il prof $\mathbb{N}$ parte da $0$, e $k = 0$ dà $n = 0$. I primi 4 sono $0, 3, 6, 9$.
- Si legge "**esiste** un $k$", non "per ogni $k$" (il simbolo è $\exists$).

L'insieme è quello dei multipli di 3: $\{0, 3, 6, 9, 12, \dots\}$.

### Esercizio 4 – Aperto

**Testo:** scrivi la contronominale di "se $n^2$ non è multiplo di 3, allora $n$ non è multiplo di 3".

**Mia risposta:** _da fare_

---

## Dubbi aperti

- Insieme delle parti $\mathcal{P}(A)$: visto alla lavagna, non ancora spiegato in chat.
- Esercizio 4 (contronominale con i multipli di 3) ancora da risolvere.

# LEZIONI ANALISI 1 UNIUD 2026/27 — regole per chi aggiorna

Repository privato con le lezioni universitarie di Analisi Matematica 1 (Università di Udine, prof. Lorenzo Freddi, a.a. 2026/27) che Pierluigi Ceccon sta studiando. Scrivi sempre in italiano.

## Struttura
- Una cartella per lezione, numerata in ordine progressivo: `03 LEZ UNIVERSITA'`, `04 LEZ UNIVERSITA'`, `05 LEZ UNIVERSITA'` e così via (numero sempre a due cifre).
- In ogni cartella un file `LEZIONE.md` con: titolo e data della lezione, argomenti trattati, appunti e riassunto con parole di Pierluigi, esempi ed esercizi svolti (solo quelli che risultano da chat o documenti), dubbi aperti, link ai materiali su Drive.
- `README.md` in radice: elenco delle lezioni (numero, data, argomento, link alla cartella) e data dell'ultimo aggiornamento.

## Fonti
- Chat di Claude con titolo «NN LEZ UNIVERSITA'» (progetto Claude «ES ANALISI 1 UNIUD 02»): è lì che Pierluigi studia ogni lezione.
- Google Drive: cartella ANALISI 1 PROF. LORENZO FREDDI (id 1OgQIBe9c9f1YIxR2XMhxxLRMG_xvAXVC) per le slide del docente; cartella ANALISI 1 (id 1FPDiiLj8EaTNsb37LCXdhxmXUU1IMb--) per i documenti di Pierluigi.

## Regole
- Slide, dispense, eserciziari e temi d'esame del docente restano su Drive: nel repository vanno solo i link.
- Non inventare esercizi né argomenti: solo quello che risulta dalle chat o dai documenti.
- Non modificare le cartelle di lezioni già complete, salvo aggiunte reali (nuovi esercizi o dubbi risolti).
- Aggiorna sempre l'elenco e la data in README.md.

## Sito pubblico (repository cecconce/analisi-1-lezioni, GitHub Pages)
- Si costruisce con `python3 scripts/build_sito.py`: crea `sito/` con `index.html`, `style.css` e una pagina per lezione in `sito/lezioni/NN.html`.
- Lo script toglie da ogni LEZIONE.md le sezioni «Esercizi svolti» e «Dubbi aperti»: nel sito pubblico vanno solo appunti e riassunti.
- Dopo la build copia il contenuto di `sito/` (index.html, style.css, lezioni/) nella radice del repository pubblico cecconce/analisi-1-lezioni, poi commit e push. Non copiare nient'altro del repository privato.

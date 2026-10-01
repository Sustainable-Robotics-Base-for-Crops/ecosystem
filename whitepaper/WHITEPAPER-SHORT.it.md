# SMOR: verso uno standard diffondibile di robotica agricola al servizio dell’agroecologia

### Sustainable Robotics Base for Crops

Autore: Alexandre Prévault-Osmani — CTO e cofondatore di SABI AGRI

*Libro bianco · versione breve · settembre 2026 · licenza CC BY 4.0*

---

## Sommario

1. [Sintesi](#sintesi)
2. [Nozioni chiave](#nozioni-chiave)
3. [Tesi e posizionamento](#tesi-e-posizionamento)
4. [Che cosa frena la diffusione](#che-cosa-frena-la-diffusione)
5. [La visione SMOR](#la-visione-smor)
6. [Un’architettura di riferimento e una catena di prova aperta](#unarchitettura-di-riferimento-e-una-catena-di-prova-aperta)
7. [Il robot SRBC, una prima incarnazione](#il-robot-srbc-una-prima-incarnazione)
8. [Valutare ciò che conta per l’azienda agricola](#valutare-ciò-che-conta-per-lazienda-agricola)
9. [Un bene comune che appartiene al mondo contadino](#un-bene-comune-che-appartiene-al-mondo-contadino)
10. [Sicurezza, conformità e corresponsabilità](#sicurezza-conformità-e-corresponsabilità)
11. [Dal codice al bene comune: la roadmap](#dal-codice-al-bene-comune-la-roadmap)
12. [Limiti e appello](#limiti-e-appello)
13. [Riferimenti](#riferimenti)
14. [L’autore](#lautore)

---

## Sintesi

La robotica agricola promette di ridurre la fatica, di rispondere alle difficoltà di reclutamento e di rendere gli interventi più precisi. Dieci anni dopo l’arrivo dei primi robot nei campi, la sua diffusione resta tuttavia limitata. Una dimostrazione riuscita dice poco sulla disponibilità di una macchina nell’arco di una stagione, sulla qualità agronomica del suo lavoro o sulla sua sostenibilità nella vita quotidiana di un’azienda agricola. La sfida si sposta: far funzionare un robot conta ormai meno che creare le condizioni della sua adozione duratura.

Sosteniamo che la robotica debba servire in via prioritaria le aziende agricole piccole e medie, diversificate e in transizione agroecologica. A questo scopo proponiamo la visione SMOR — *Small, Modular, Open & Responsible* —, tradotta in un’architettura di riferimento, in una catena documentale aperta che collega ciò che il robot doveva fare a ciò che ha effettivamente fatto, in un metodo di valutazione, in un modello di bene comune che appartiene al mondo contadino e in una ripartizione esplicita delle responsabilità. Il robot SRBC ne è la prima incarnazione industriale. SMOR è un quadro da mettere alla prova: questo testo ne espone la tesi e le proposte, la versione completa ne porterà le prove.

---

## Nozioni chiave

- **ODD** (Operational Design Domain, dominio operativo di progetto): le condizioni per le quali una funzione autonoma è stata progettata e validata — appezzamento, suolo, meteo, pendenza, qualità della localizzazione, presenza di persone.
- **Ordine di missione**: file che descrive ciò che il robot deve fare, entro quali limiti e con quali reazioni ammesse.
- **Lavoro eseguito**: file che descrive ciò che il robot ha fatto, in quali condizioni incontrate e come l’azienda agricola giudica il risultato ottenuto.
- **Open Core**: modello in cui le interfacce e i componenti generici sono aperti, mentre l’implementazione materiale, la calibrazione e i servizi restano sotto la responsabilità del costruttore.

---

## Tesi e posizionamento

Dalla metà degli anni 2010 la robotica agricola è uscita dai laboratori per raggiungere i campi. I progressi nella percezione, nella navigazione e nell’automazione sono reali; la diffusione commerciale resta modesta rispetto alla diversità delle produzioni e al numero delle aziende agricole [1, 2]. Questo divario richiede un’altra definizione della maturità.

Il nostro approccio è semplice: la maturità di un robot agricolo si misura dalla sua **diffondibilità**, cioè dalla sua capacità di essere usato, mantenuto, riparato e migliorato sui tempi lunghi dell’agricoltura. Essa presuppone l’adeguatezza a un bisogno agronomico e umano chiaramente individuato, un costo accessibile, una sicurezza dimostrata in un dominio d’impiego esplicito, una manutenzione di prossimità e un’appropriazione reale da parte delle persone che lo utilizzano.

Assumiamo una scelta di posizionamento esplicita: la robotica agricola deve servire in via prioritaria le aziende agricole piccole e medie, in particolare quando sono diversificate e in transizione agroecologica. Le definiamo innanzitutto come imprese agricole a misura d’uomo, in cui chi coltiva conserva una capacità diretta di osservazione e di decisione sulle colture e sui suoli; la classificazione del censimento agricolo francese per produzione standard ne fornisce un riferimento statistico [3]. Queste aziende portano la diversità delle produzioni, la cura dei paesaggi, l’occupazione rurale e saperi radicati nel contesto. Sono anche le più esposte al costo del lavoro, alla fatica e alle barriere all’investimento.

Le pratiche agroecologiche richiedono più osservazione, più precisione e interventi più differenziati [4]. Questa intensità agronomica è difficile da sostenere quando il lavoro umano pesa come un costo di fronte alle economie di scala. La robotica può riequilibrare questo rapporto riducendo la fatica e rendendo possibili operazioni favorevoli ai suoli e agli ecosistemi: una semina precisa che prepara un diserbo meccanico precoce, passaggi ripetuti di un attrezzo leggero in una finestra breve, una macchina leggera dove la portanza del suolo lo richiede.

La stessa tecnologia può anche servire alla concentrazione dei mezzi di produzione, alla dipendenza da fornitori proprietari e alla rapida obsolescenza delle attrezzature [5, 6]. La direzione dipende dalle scelte di architettura, di modello economico e di governance. Il contrasto tra i cicli brevi del digitale e i tempi lunghi dell’agricoltura ne fa una questione strutturale: una macchina che non si può più capire, mantenere o adattare diventa un peso, anche se all’inizio era efficace.

Distinguiamo tre livelli: la **capacità tecnica** del robot (muoversi, seguire un filare, comandare un attrezzo in sicurezza), la **prestazione agronomica** in una finestra data (una semina regolare, una sarchiatura efficace) e l’**effetto agroecologico**, che si apprezza nel tempo alla scala del sistema colturale (input evitati, stato del suolo, biodiversità, condizioni di lavoro, autonomia dell’azienda, costo completo). Le valutazioni esistenti documentano soprattutto il primo livello; l’utilità di un robot per un’azienda agricola dipende dagli altri due.

> **Tesi**  
> La robotica agricola diventa una leva di diffusione dell’agroecologia quando è progettata per essere utile, accessibile, mantenibile, sicura, interoperabile e appropriabile, e quando sa dimostrare le proprie prestazioni in condizioni reali.

Aggiungiamo una convinzione di metodo: la diffusione è una questione di **rappresentazione** non meno che di misura. Finché l’intenzione agronomica e il risultato ottenuto sono descritti in vocabolari diversi, i ritorni dal campo restano isolati, i risultati di due costruttori incomparabili e le responsabilità non verificabili. Un vocabolario comune e versionato è la prima condizione di una conoscenza cumulativa.

---

## Che cosa frena la diffusione

Un robot agricolo lavora a contatto con sistemi viventi: suolo, vegetazione, meteo e organizzazione del lavoro variano nel corso di una stagione. Ogni prestazione va quindi riferita a un uso, a una configurazione e a un dominio d’impiego esplicito.

I freni sono noti e interdipendenti [1, 7]: la **robustezza** sull’arco di una stagione; la **sicurezza**, che richiede di rilevare le situazioni pericolose e di raggiungere uno stato sicuro; la **prestazione agronomica**, che si misura dalla qualità del lavoro dell’attrezzo più che dalla precisione della traiettoria; la **redditività**, che dipende dal tempo di supervisione, dalla manutenzione e dai fermi molto più che dal prezzo d’acquisto; l’**interoperabilità**, debole finché formati, interfacce e protocolli restano specifici di ciascun costruttore, e la **dipendenza tecnologica** che ne deriva. Lavori recenti mostrano che il tempo umano dedicato alla logistica e alla supervisione costituisce il vero problema della robotica di piccola scala [7].

L’agricoltura di precisione dispone già di standard preziosi, come ISOXML o ADAPT, per descrivere un compito e il lavoro realizzato [8, 9]. Sono stati concepiti per una persona alla guida, che si fa garante del dominio d’impiego. Con un robot una parte dell’osservazione e della decisione passa alla macchina, e la catena che va dall’intenzione all’esecuzione deve diventare esplicita: ciò che il robot deve fare, in quali condizioni è autorizzato a farlo, come reagisce agli imprevisti, ciò che ha incontrato e ciò che ha realizzato. L’industria riconosce questo bisogno, con il gruppo di lavoro AEF dedicato alle macchine autonome [10], così come la ricerca sul dominio operativo agricolo [11]. Consideriamo questi lavori convergenti e desideriamo contribuirvi con una proposta aperta, già utilizzata sul campo.

La letteratura che interroga la robotica dal punto di vista agroecologico concorda su un punto: la direzione resta aperta. La stessa tecnologia può condurre a flotte di piccole macchine al servizio di sistemi diversificati o a grandi macchine che consolidano le monocolture [6]. Portare funzionalità autonome nei sistemi agroecologici richiede di progettare con una diversità di attori, oltre una «mentalità monoculturale» [5], e le agricoltrici e gli agricoltori collocano la responsabilità, la sicurezza e il controllo dei dati tra le loro principali preoccupazioni [12]. Questi risultati fondano la nostra scelta di affidare alle contadine e ai contadini la decisione sull’uso della loro tecnologia e la sua garanzia.

---

## La visione SMOR

SMOR è un quadro di progettazione e di valutazione che collega le caratteristiche di un robot ai suoi effetti agronomici, economici, ambientali e sociali. Ha oggi lo statuto di una proposta da mettere alla prova del campo e del dibattito.

Privilegiamo la trazione e gli attuatori elettrici. Motori e attuatori elettrici si comandano finemente, restituiscono il loro stato e si integrano direttamente nei sistemi di diagnosi. L’elettricità può provenire dalla rete o essere prodotta in azienda, aprendo la strada a un’autonomia energetica totale o parziale; batterie e motori restano da valutare sull’intero ciclo di vita.

**Small: una scala adeguata.** Privilegiamo macchine la cui massa, potenza e ingombro restano proporzionati alle operazioni. Il nostro obiettivo dimensionale si colloca tra l’essere umano e il cavallo da tiro: tra 80 e 1 200 kg circa, meno di 10 km/h, qualche chilowatt, un’autonomia da mezza giornata a una giornata di lavoro, una bassissima tensione e, per i vettori leggeri, un investimento inferiore a 40 000 euro. Oltre questa soglia la massa riporta la macchina nel mondo del trattore, con la sua motorizzazione, la sua logistica e il suo prezzo. Questi valori sono obiettivi di progetto. Una massa contenuta riduce l’energia in gioco e facilita trasporto e manutenzione; l’effetto sul suolo dipende anche dalla pressione di contatto, dallo slittamento, dal numero di passaggi e dall’umidità [13]. Questa scala permette di disporre di più robot specializzati o condivisi tra aziende anziché di un’unica macchina dimensionata per l’operazione più pesante. Diventa un vantaggio economico duraturo quando il tempo umano per ettaro diminuisce davvero, il che richiede missioni affidabili senza sorveglianza continua e, nel tempo, la supervisione di più robot da parte di una sola persona.

**Modular: adattare, riparare, condividere.** Separiamo una base stabile (struttura, energia, comando, interfacce, sicurezza) da moduli adattati alle colture, agli attrezzi e ai contesti: cambiare attrezzo, organo di locomozione o sensore senza sostituire il vettore, far evolvere una funzione software senza ricostruire l’insieme, aggiornare una macchina al ritmo del calendario colturale. Questa modularità poggia su dimensioni, connettori, protocolli e formati documentati; senza di essi resterebbe ostaggio del fornitore iniziale.

**Open: una sovranità duratura.** Apriamo in via prioritaria le interfacce, i formati di missione e di dati, la documentazione e i componenti software generici, poi i progetti costruttivi quando la loro pubblicazione rafforza la riparabilità. L’Open Source che difendiamo è un metodo industriale: licenze esplicite, contratti versionati, test, documentazione, governance e versioni stabili. Garantisce alle aziende agricole una sovranità d’uso (diagnosticare, riparare, adattare, affidare la manutenzione a un altro fornitore), sposta la differenziazione dei costruttori verso l’integrazione, la sicurezza e il servizio, e permette di sviluppare competenze durature nelle officine dei territori.

**Responsible: un’innovazione che rende conto.** Una tecnologia diventa responsabile quando i suoi effetti sono anticipati, discussi, misurati e corretti con le persone interessate [14]. Questo principio impegna a coinvolgere le agricoltrici e gli agricoltori nella definizione dei bisogni e nella valutazione, a progettare la sicurezza fin dall’inizio, a documentare i limiti d’uso, a misurare i consumi di materia, di energia e di risorse digitali, a preservare la decisione contadina, a garantire la sovranità dell’azienda agricola sui propri dati e a rendere verificabile la ripartizione delle responsabilità.

Questi quattro principi formano un insieme. Un piccolo robot chiuso resta prigioniero e invecchia in fretta; una piattaforma aperta senza governance si frammenta; una macchina modulare ma troppo costosa non incide sulla diffusione. **SMOR propone una coerenza d’insieme: una robotica la cui prestazione si misura dalla capacità di rendere l’agroecologia praticabile, economicamente sostenibile e appropriabile nel tempo dal mondo contadino.**

---

## Un’architettura di riferimento e una catena di prova aperta

Un’architettura di riferimento fornisce una lingua comune: separa le funzioni e definisce le interfacce attraverso cui un componente può essere sostituito senza ricostruire il sistema. Ogni costruttore resta libero nelle proprie scelte materiali, purché rispetti i contratti comuni e i requisiti di sicurezza. Proponiamo sei livelli: energia e attuatori, controllo del veicolo, bus di campo documentati, calcolatore di bordo (ROS 2 ne costituisce oggi una base adeguata), percezione e localizzazione, missione e interfaccia utente. Un principio li attraversa tutti: **le funzioni critiche per la sicurezza restano indipendenti dal calcolatore generico e da qualsiasi connessione remota.** Le funzioni essenziali restano disponibili offline, e l’interfaccia rende visibili lo stato del robot, i suoi limiti e il motivo di ogni arresto.

Il contratto più strutturante è l’**interfaccia veicolo**, che descrive comandi, stati, capacità dell’attrezzo e guasti. Permette di adattare una stessa funzione di navigazione a più vettori e trasforma così un prodotto in piattaforma.

Il secondo contratto riguarda la missione. Proponiamo **JSON Agri**, un formato aperto pubblicato con licenza CC BY 4.0 [15], leggibile senza formazione informatica e verificabile dalle macchine. Esso organizza una catena di due documenti. L’**ordine di missione** descrive l’obiettivo agronomico e i suoi criteri di accettazione, la coppia vettore-attrezzo, il dominio d’impiego ammesso, la traiettoria, le zone autorizzate e le reazioni previste agli eventi: una batteria scarica provoca, per esempio, il ritorno alla zona di ricarica lungo percorsi autorizzati. Il **lavoro eseguito** collega questa intenzione alle condizioni incontrate, agli eventi, agli interventi umani, agli indicatori di prestazione e al giudizio agronomico dell’azienda agricola. Un’impronta digitale dell’ordine, ripresa nel lavoro eseguito, garantisce che l’esecuzione sia confrontata con la versione esatta della missione.

Tre scelte danno a questa catena la sua portata. Il dominio d’impiego ammesso e le condizioni incontrate condividono lo stesso vocabolario, così che ogni scarto può essere collegato a un rilevamento, a una decisione, a una responsabilità e a una prova. Le reazioni agli eventi formano un vocabolario chiuso: la macchina rifiuta ogni istruzione sconosciuta o assente dal catalogo validato dal costruttore, e la sua soglia minima di sicurezza resta fuori dalla portata di qualsiasi file. L’attestazione prodotta in simulazione certifica che un file ha superato controlli definiti, sotto ipotesi dichiarate; vale come prova di verifica, distinta da una certificazione.

La catena separa così tre validazioni: la **preparazione**, nell’editor di missione; la validazione **operativa**, a bordo, in cui il robot confronta la missione con la propria configurazione e con le condizioni confermate sul posto, conservando la libertà di rifiutare; la validazione della **prestazione**, dopo la missione, mediante il giudizio agronomico dell’azienda agricola. Questa separazione protegge da due confusioni costose: scambiare una simulazione per un’autorizzazione, o una missione conclusa per una prestazione riuscita. Regole di specifica pubbliche (un nucleo piccolo e stabile, dati mancanti segnalati come tali, compatibilità garantita, validazione offline), livelli di conformità e un validatore permettono a qualsiasi terza parte di verificare autonomamente la propria implementazione. JSON Agri completa così gli standard esistenti con la catena dell’autonomia che essi lasciano implicita.

---

## Il robot SRBC, una prima incarnazione

Il robot SRBC, sviluppato da SABI AGRI, mette alla prova questi principi su una macchina venduta e utilizzata sul campo. Questo vettore elettrico compatto, su ruote o su cingoli, pesa circa 250 kg nella versione cingolata e si colloca quindi nella fascia bassa del quadro SMOR. Porta attrezzi per la lavorazione leggera, la semina, la cura delle colture e il trasporto. La sua catena di sicurezza hardware funziona indipendentemente dal calcolatore, e le protezioni di alto livello (geofencing, visione di sicurezza) impongono i loro comandi alla navigazione mediante un arbitraggio di priorità. **La persona formata che conduce il robot definisce e rispetta il dominio d’impiego; il software di alto livello contribuisce a prevenire gli incidenti; il controllo di basso livello garantisce il ritorno a uno stato sicuro.**

Navigazione, localizzazione, geofencing, percezione di sicurezza, simulazione, formato JSON Agri ed editor di missione sono pubblicati sull’organizzazione GitHub [Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops), con licenza Apache 2.0 per il codice e CC BY 4.0 per le specifiche. Il robot che lavora sull’appezzamento esegue questo codice pubblico. Il software del controllore, il driver del veicolo, i contratti di comando, le calibrazioni e i servizi remoti restano sotto la responsabilità del costruttore: SRBC è un **Open Core industriale**, e ne descriviamo l’apertura così com’è.

Qualsiasi organizzazione esterna può così far funzionare da capo a fondo un robot simulato, preparare e validare una missione, osservare un robot reale attraverso un’interfaccia pubblicata, verificare la conformità dei propri file e riutilizzare ogni componente di navigazione. Le prossime tappe di apertura permetteranno di comandare il robot, di portare la pila software su altri veicoli e di costruire una macchina a partire dal codice pubblico.

---

## Valutare ciò che conta per l’azienda agricola

Una dimostrazione isolata fornisce un esempio; un protocollo documentato, ripetuto e comparabile fornisce una prova. Il nostro metodo collega ogni risultato a un’operazione agronomica, a una situazione di riferimento (lavoro manuale, trattore, pratica precedente), a un dominio d’impiego, a una configurazione e a un catalogo di indicatori versionato, tutti fissati prima della prova. Sostenuto dalla catena tra ordine di missione e lavoro eseguito, questo legame permette a terzi di ricalcolare ciò che pubblichiamo. Gli indicatori coprono la prestazione agronomica, la disponibilità, l’energia, la sicurezza, il tempo umano, il costo completo e gli effetti sul suolo; sono pubblicati con la loro convenzione di calcolo, la loro dispersione e la loro copertura. Un valore mancante è dichiarato come tale: l’assenza è un’informazione.

La macchina sa misurare la propria durata, la propria traiettoria, la propria energia e la qualità della propria localizzazione. Le grandezze che decidono dell’utilità per l’azienda agricola dipendono spesso da una persona: condizioni realmente incontrate, soddisfazione agronomica, tempo di supervisione, necessità di un secondo passaggio. Proponiamo di raccoglierle in tre momenti, là dove si trova la persona: alla preparazione, al caricamento sul robot e a fine missione, con uno strumento che precompila ciò che può e pone poche domande. Allo stesso modo, una grandezza misurata diventa un criterio quando qualcuno ne fissa la soglia nell’ordine di missione e la macchina sa come reagire al suo superamento.

Le nostre prime campagne strumentate confermano la fattibilità di questa catena tra robot, aziende agricole e attrezzi diversi. La base di prove progredirà con i suoi successi come con i suoi insuccessi, per stabilire dove, quando e a quali condizioni la robotica apporta un beneficio agroecologico reale.

---

## Un bene comune che appartiene al mondo contadino

Sosteniamo che l’ecosistema software della robotica agricola — formati di file, codice di guida, algoritmi decisionali, strumenti di missione e di tracciabilità — debba diventare un **bene comune che appartiene al mondo contadino e di cui il mondo contadino si appropria**.

Questo bene comune è anzitutto un vocabolario. Un’azienda agricola descrive la propria attesa in termini agronomici, un distributore in termini di servizio, un costruttore in termini di funzioni. Il primo compito del bene comune è permettere a questi attori di **descrivere, scambiare e contestare fatti negli stessi termini**. Il codice aperto rende questo vocabolario utilizzabile e prova, in funzionamento, che esso funziona; il vocabolario rende il codice sostituibile, e quindi il bene comune governabile. Un formato che più implementazioni sanno leggere sfugge a ogni appropriazione, compresa quella dell’azienda che lo ha avviato.

Per mondo contadino intendiamo le contadine e i contadini, così come le officine, i distributori, le cooperative, gli istituti e i costruttori che lavorano al loro servizio. Questa appartenenza si costruisce attraverso cinque proprietà verificabili:

- **resta aperto**: le licenze garantiscono il libero uso nel tempo, e il marchio protegge il senso dei termini;
- **sopravvive all’azienda che lo ha avviato**: depositi pubblici, storia e documentazione permettono ad altri di riprenderlo; nel tempo la sua proprietà è trasferita a una struttura senza scopo di lucro, indipendente da qualsiasi costruttore, di cui le contadine e i contadini e le loro organizzazioni sono membri di diritto;
- **si governa con le persone che serve**: le contadine e i contadini partecipano alle decisioni sulla sua finalità e dispongono di un diritto di contestazione;
- **restituisce i dati all’azienda agricola**: il lavoro eseguito appartiene all’azienda, che può leggerlo, conservarlo, condividerlo o tenerlo per sé senza passare da un fornitore [12];
- **si impara**: strumenti leggibili, formazioni tra pari e officine locali lo inscrivono nella tradizione dell’educazione popolare tecnica.

Le componenti di un robot richiedono gradi di apertura diversi. I **contratti comuni** (formati, indicatori, interfacce, criteri di conformità) sono aperti in via prioritaria; i **componenti generici** (navigazione, simulazione, diagnosi, editor) si sviluppano come beni comuni software; l’**integrazione industriale** e la catena di sicurezza spettano al costruttore; i **servizi e dati sensibili** mantengono un accesso controllato. La regola che rende difendibile un Open Core sta in una frase: **si aprono i contratti e la logica generica; si tengono l’implementazione materiale, la calibrazione e i servizi di flotta.** Il vantaggio di un costruttore risiede nella sua macchina, nella sua catena di sicurezza, nella sua rete di assistenza e nella sua capacità di mantenere gli impegni nel tempo.

L’apertura sposta il valore e i costi. Riduce la reimplementazione delle stesse basi e crea bisogni di manutenzione e di governance da finanziare. Vendita e noleggio di macchine, adattamento locale, contratti di servizio, versioni mantenute, formazione e accompagnamento alla conformità fanno vivere le imprese, purché rinuncino alla cattura attraverso dati trattenuti, abbonamenti indispensabili al funzionamento di base o interfacce chiuse artificialmente. Applichiamo Apache 2.0 al codice e CC BY 4.0 alle specifiche e ai testi; la questione di una reciprocità per alcune componenti sarà decisa collettivamente.

La governance segue l’uso. Le decisioni sul formato sono già tracciate pubblicamente, e una procedura scritta permette di contestarle. Più tappe, attivate da fatti osservabili, organizzano il seguito, a partire da un comitato delle versioni fin dalla prima implementazione di terzi, poi da un collegio degli usi dotato di un diritto di contestazione non appena un collettivo di agricoltrici e agricoltori, una cooperativa o un distributore dipende dal formato. L’ultima tappa trasferisce la proprietà del formato e del marchio alla struttura senza scopo di lucro descritta sopra; essa rende il bene comune indipendente dall’azienda che lo ha avviato, e la consideriamo una condizione di credibilità dell’insieme.

---

## Sicurezza, conformità e corresponsabilità

La conformità di una macchina autonoma ne struttura la progettazione, le prove e la sorveglianza per tutta la sua vita. La direttiva macchine 2006/42/CE si applica fino al 19 gennaio 2027, data dalla quale il regolamento (UE) 2023/1230 ne prende il posto [16]; la serie ISO 18497:2024 tratta delle macchine agricole autonome [17]. Il codice aperto facilita la verifica, la tracciabilità e la manutenzione. La sicurezza e la conformità restano invece legate a ogni macchina immessa sul mercato o messa in servizio, alla sua valutazione dei rischi, alle sue prove e alla sua configurazione validata. Una riparazione che preserva la conformità resta una riparazione, e l’apertura mira proprio a facilitarla; una modifica che crea un nuovo pericolo impegna la persona o l’entità che la realizza. I gruppi che mantengono il bene comune rispondono della qualità dei contributi; la validazione dell’integrazione spetta all’entità che mette in servizio la macchina.

Proponiamo di completare questa ripartizione regolamentare con una **corresponsabilità operativa**, che indichi per ogni fase chi decide, chi valida e quale prova viene conservata.

| Fase | Decide | Valida | Prova conservata |
|---|---|---|---|
| Scelta agronomica e finestra di lavoro | Agricoltrice/agricoltore | Agricoltrice/agricoltore | intenzione e criteri nell’ordine di missione |
| Mappa dell’appezzamento e ostacoli noti | Agricoltrice/agricoltore | Agricoltrice/agricoltore | mappa dell’appezzamento referenziata |
| Dominio d’impiego ammesso e reazioni agli eventi | Agricoltrice/agricoltore oppure operatore/operatrice | Soglia minima di sicurezza del costruttore | dominio e strategie nell’ordine |
| Aggancio dell’attrezzo e verifica prima della partenza | Operatore/operatrice | Operatore/operatrice | configurazione prevista e utilizzata |
| Esecuzione | Macchina, libera di rifiutare | Limiti del costruttore, arresto d’emergenza | eventi, azioni richieste ed eseguite |
| Giudizio sul risultato ottenuto | Agricoltrice/agricoltore | Agricoltrice/agricoltore | giudizio nel lavoro eseguito |

Una casella senza titolare è un risultato: segnala una lacuna da colmare. Una responsabilità intesa in modo diverso da due parti è anch’essa un risultato, da discutere apertamente. Questa corresponsabilità organizza la collaborazione quotidiana e lascia intera la responsabilità regolamentare del costruttore o dell’integratore. **Si tratta di rendere i saperi condivisibili mantenendo una responsabilità esplicita per ogni macchina messa in servizio.**

---

## Dal codice al bene comune: la roadmap

La diffusione di SMOR si misurerà dalla capacità di organizzazioni esterne di comprendere le interfacce, riprodurre una prova, adattare un componente, leggere un lavoro eseguito e mantenere una macchina indipendentemente dal suo sviluppatore. Procediamo in quattro tappe: **rendere visibile** ciò che esiste, con il suo stato e i suoi limiti; **rendere riproducibile** l’installazione e la simulazione di una missione; **rendere interoperabile** pubblicando contratti e test; **rendere diffondibile** costruendo prove, competenze e servizi sul campo.

Ne derivano cinque cantieri: consolidare la base aperta; pubblicare i contratti di comando e l’interfaccia veicolo, poi ottenere una seconda implementazione del formato da parte di un’organizzazione esterna, condizione per parlare di standard; costituire una base di prove verificata da un istituto indipendente, con costo completo e tempo umano misurati su più campagne; organizzare la sicurezza di ogni configurazione commercializzata; sviluppare competenze territoriali affinché aziende agricole, officine e distributori sappiano diagnosticare, riparare e formare a loro volta, perché si governa ciò che si comprende. L’adozione procede per cerchi, dall’uso interno ai partner di fiducia, poi alle integrazioni di terzi e a una diffusione ampia, e ogni passaggio dipende da criteri osservabili. I download indicano un interesse; la diffusione agricola si prova sul campo.

---

## Limiti e appello

Questo testo propone un quadro concettuale e tecnico; la dimostrazione del suo beneficio agronomico ed economico richiede campagne ripetute e osservazioni pluriennali, che la versione completa documenterà. Ne conosciamo i limiti: il quadro SMOR è un obiettivo di progetto; SRBC costituisce un primo caso di studio, portato da un gruppo coinvolto nel suo sviluppo; l’adozione di JSON Agri da parte di altri costruttori e la pubblicazione dell’interfaccia veicolo sono le prossime tappe; gli effetti sui suoli e sul mestiere contadino richiedono tempo per manifestarsi. È la situazione di un bene comune nascente. Lo pubblichiamo per riunire le implementazioni, le competenze e gli usi che lo faranno crescere.

Nulla impedisce di innovare in fretta e bene; tutto invita a farlo insieme [18]. Ciascuno può compiere un primo passo, alla propria scala:

- **agricoltrici, agricoltori e collettivi**: accogliere una missione strumentata, chiedere l’accesso agli ordini di missione e ai lavori eseguiti sui propri appezzamenti, dire a fine missione ciò che la macchina non può sapere;
- **distributori, officine, integratori**: imparare a leggere un file di missione, documentare un aggancio, segnalare un incidente con la sua configurazione, formare una vicina o un vicino;
- **costruttori di robot e di attrezzi**: implementare un lettore del formato, pubblicare un’interfaccia, anche modesta, con i suoi limiti;
- **istituti, laboratori, scuole**: condurre un protocollo, verificare una convenzione di calcolo, proporre una soglia fondata su osservazioni;
- **cooperative, enti territoriali, finanziatori pubblici**: sostenere le infrastrutture comuni (campi prova, formazione, documentazione, manutenzione degli standard) alla pari dell’acquisto di macchine;
- **comunità di sviluppo**: migliorare un componente, scrivere un test, mantenere una versione stabile, partecipare alla governance.

> **La tecnologia diventa progresso agricolo quando rafforza in modo duraturo la capacità delle contadine e dei contadini di comprendere, decidere e agire.**  
> Aprire la robotica significa dare al mondo agricolo i mezzi per partecipare alla sua progettazione, padroneggiarne l’uso e trasmetterne i saperi.

**Unirsi all’ecosistema**  
[github.com/Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops)

---

## Riferimenti

[1] Bechar, A., & Vigneault, C. (2016). Agricultural robots for field operations: Concepts and components. *Biosystems Engineering*, 149, 94–111. [https://doi.org/10.1016/j.biosystemseng.2016.06.014](https://doi.org/10.1016/j.biosystemseng.2016.06.014)

[2] Lowenberg-DeBoer, J., Huang, I. Y., Grigoriadis, V., & Blackmore, S. (2020). Economics of robots and automation in field crop production. *Precision Agriculture*, 21, 278–299. [https://doi.org/10.1007/s11119-019-09667-5](https://doi.org/10.1007/s11119-019-09667-5)

[3] Agreste. (2022). *Recensement agricole 2020 — Typologie des exploitations selon leur dimension économique* [Censimento agricolo 2020 — Tipologia delle aziende secondo la dimensione economica]. Ministero francese dell’Agricoltura. [https://agreste.agriculture.gouv.fr/agreste-web/disaron/RA2020_001/detail/](https://agreste.agriculture.gouv.fr/agreste-web/disaron/RA2020_001/detail/)

[4] Wezel, A., Bellon, S., Doré, T., Francis, C., Vallod, D., & David, C. (2009). Agroecology as a science, a movement and a practice. A review. *Agronomy for Sustainable Development*, 29(4), 503–515. [https://doi.org/10.1051/agro/2009004](https://doi.org/10.1051/agro/2009004)

[5] Ditzler, L., & Driessen, C. (2022). Automating Agroecology: How to Design a Farming Robot Without a Monocultural Mindset? *Journal of Agricultural and Environmental Ethics*, 35, 2. [https://doi.org/10.1007/s10806-021-09876-x](https://doi.org/10.1007/s10806-021-09876-x)

[6] Daum, T. (2021). Farm robots: ecological utopia or dystopia? *Trends in Ecology & Evolution*, 36(9), 774–777. [https://doi.org/10.1016/j.tree.2021.06.002](https://doi.org/10.1016/j.tree.2021.06.002)

[7] Spykman, O., Lowenberg-DeBoer, J., & Gandorfer, M. (2026). Crop robots as potential enablers of economical and biodiversity-smart small-scale farming. *Precision Agriculture*. [https://doi.org/10.1007/s11119-026-10367-0](https://doi.org/10.1007/s11119-026-10367-0)

[8] ISO. (2015). *ISO 11783-10:2015 — Tractors and machinery for agriculture and forestry — Serial control and communications data network — Part 10: Task controller and management information system data interchange*. [https://www.iso.org/standard/61581.html](https://www.iso.org/standard/61581.html)

[9] AgGateway. (2025). *ADAPT Standard 2.0 — Documentation*. [https://adaptstandard.org/docs/](https://adaptstandard.org/docs/)

[10] Agricultural Industry Electronics Foundation (AEF). (s.d.). *Autonomy in Agriculture (AUT) — project team, use cases and work items*. [https://www.aef-online.org/aef-aut/](https://www.aef-online.org/aef-aut/)

[11] Felske, M., Redenius, J., Happich, G., & Schöning, J. (2026). Towards an Agricultural Operational Design Domain: A Framework. *Smart Agricultural Technology*. [https://doi.org/10.1016/j.atech.2026.102246](https://doi.org/10.1016/j.atech.2026.102246)

[12] Holm, S., Pedersen, S. M., & Tamirat, T. W. (2024). Robots in agriculture — A case-based discussion of ethical concerns on job loss, responsibility, and data control. *Smart Agricultural Technology*, 9, 100633. [https://doi.org/10.1016/j.atech.2024.100633](https://doi.org/10.1016/j.atech.2024.100633)

[13] Batey, T. (2009). Soil compaction and soil management — a review. *Soil Use and Management*, 25(4), 335–345. [https://doi.org/10.1111/j.1475-2743.2009.00236.x](https://doi.org/10.1111/j.1475-2743.2009.00236.x)

[14] Stilgoe, J., Owen, R., & Macnaghten, P. (2013). Developing a framework for responsible innovation. *Research Policy*, 42(9), 1568–1580. [https://doi.org/10.1016/j.respol.2013.05.008](https://doi.org/10.1016/j.respol.2013.05.008)

[15] Sustainable Robotics Base for Crops. (2026). *Agri JSON format, version 3 — schema, profiles, vocabularies, indicator registry and documentation*. Licenza CC BY 4.0. [https://github.com/Sustainable-Robotics-Base-for-Crops/json_agri_format](https://github.com/Sustainable-Robotics-Base-for-Crops/json_agri_format)

[16] Parlamento europeo e Consiglio dell’Unione europea. (2023). *Regolamento (UE) 2023/1230 del 14 giugno 2023 relativo alle macchine*. [https://eur-lex.europa.eu/eli/reg/2023/1230/oj](https://eur-lex.europa.eu/eli/reg/2023/1230/oj)

[17] ISO. (2024). *ISO 18497, parti da 1 a 4 — Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery*. [https://www.iso.org/standard/82684.html](https://www.iso.org/standard/82684.html)

[18] Prévault-Osmani, A. (2026). *Manifesto per una robotica agricola aperta*. Sustainable Robotics Base for Crops. Licenza CC BY 4.0. [https://github.com/Sustainable-Robotics-Base-for-Crops/ecosystem/blob/main/manifesto/MANIFESTO.it.md](https://github.com/Sustainable-Robotics-Base-for-Crops/ecosystem/blob/main/manifesto/MANIFESTO.it.md)

---

## L’autore

**Alexandre Prévault-Osmani**  
CTO e cofondatore di SABI AGRI

Ingegnere di professione e contadino per percorso, Alexandre Prévault-Osmani lavora dal 2015 all’intersezione tra elettrificazione, robotica agricola, Open Source e agroecologia. Partecipa allo sviluppo del robot SRBC, presentato in questo testo come caso di studio.

**Contatto**

- GitHub: [Alexandre-PO](https://github.com/Alexandre-PO)
- LinkedIn: [alexandre-po](https://www.linkedin.com/in/alexandre-po)

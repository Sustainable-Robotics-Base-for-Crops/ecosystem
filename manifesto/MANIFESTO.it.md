# Manifesto per una robotica agricola aperta — Sustainable Robotics Base for Crops

L’ecosistema della robotica agricola ha bisogno di una base comune, aperta, sobria, sicura e documentata, capace di rispettare la diversità delle pratiche. È questo il senso di *Sustainable Robotics Base for Crops* (SRBC): costruire e condividere un fondamento software di produzione per robot agricoli autonomi, affinché il valore creato dalla tecnologia torni anche a chi la fa vivere — le contadine e i contadini — e alimenti una filiera giusta, manutenibile e duratura.

**Affermiamo che una robotica agricola aperta può contribuire ad accelerare l’adozione delle pratiche agroecologiche favorendo la diffusione di strumenti efficaci, appropriabili e sicuri. Le prestazioni agronomiche, ecologiche, economiche e sociali devono diventare chiaramente misurabili e soprattutto evitare di opporsi.**

Chiamiamo agricoltori, sviluppatori, costruttori, officine, integratori, ricercatori, cooperative e istituti di formazione a unirsi a questo impegno: pubblicare un’interfaccia, stabilizzare un formato, scrivere documentazione, eseguire una prova, formare un vicino. Nulla vieta di innovare in fretta e bene; tutto invita a farlo insieme.

La tecnologia non deve essere un ostacolo. Deve essere un ponte verso la durabilità dei sistemi agricoli.

---

## Perché aprire

Quando abbiamo fatto germogliare il progetto SABI AGRI nel 2015, l’obiettivo era già quello di diffondere attrezzature agricole al servizio di un’agricoltura più sostenibile e più sovrana. La nostra esperienza di costruttori di macchine elettriche e di robot agricoli ci ha confrontati con una realtà strutturale: la rapidità dei cicli digitali e il carattere chiuso di molte soluzioni creano una dipendenza sproporzionata per il mondo contadino.

Da un lato, l’obsolescenza dei supporti hardware e software non è in fase con i tempi lunghi dell’agricoltura. Dall’altro, le interfacce proprietarie chiudono gli utenti in una relazione squilibrata con i loro fornitori, a loro volta dipendenti dalle tecnologie dei propri fornitori. Una macchina che non può più essere compresa, mantenuta o adattata finisce per diventare un vincolo, anche quando era inizialmente performante.

Pensiamo che ogni azienda agricola debba poter beneficiare dei progressi tecnologici senza essere prigioniera di formati chiusi. Aprire significa rendere possibili la riparazione, l’adattamento e la trasmissione delle conoscenze al ritmo delle stagioni e dei territori.

## Per chi, e al servizio di cosa

Situamo l’ecosistema robotico SRBC al servizio delle piccole e medie aziende agricole, in particolare quando sono diversificate e impegnate in pratiche agroecologiche. Esse svolgono un ruolo essenziale nell’equilibrio degli ecosistemi, nella diversità delle produzioni, nel dinamismo dei territori e nel mantenimento di saperi contestualizzati. Tuttavia queste aziende sono anche particolarmente esposte alla penosità dei lavori fisici, al fabbisogno di manodopera e alle barriere di investimento.

Le pratiche agroecologiche richiedono spesso più osservazione, più precisione e più cura del suolo e del vivente. La robotica può contribuire a rendere queste pratiche economicamente accessibili riducendo la penosità e rendendo realizzabili operazioni favorevoli alle colture, ai suoli e agli ecosistemi. La decisione contadina può allora assumere tutta la sua importanza nella gestione degli ecosistemi.

Non tutta la robotica serve questa ambizione. A seconda della sua architettura e del suo modello economico, può rafforzare la concentrazione dei mezzi di produzione e la dipendenza tecnologica. La questione non è quindi adottare la robotica per principio, ma determinare al servizio di quali modelli agricoli è concepita, chi può accedervi, chi la comprende, chi ne fissa gli usi e chi ne cattura il valore.

## Che cos’è SRBC

*Sustainable Robotics Base for Crops* designa l’ecosistema pubblico di mattoni software sviluppati, tra l’altro, per il robot SRBC e, più in generale, per una robotica agricola interoperabile.

Non è una dimostrazione fuori dal campo. **Una parte sostanziale di questo codice è utilizzata in produzione**: navigazione, localizzazione, georeferenziazione, percezione, simulazione, formato di missione e strumenti associati. I repository sono pubblicati sull’organizzazione GitHub [Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops).

L’ecosistema SRBC è un insieme di pacchetti e strumenti versionati — principalmente sotto ROS 2 — concepiti per essere letti, verificati, riutilizzati o sostituiti in modo indipendente. I contratti aperti (formato di missione JSON Agri, interfacce di comunicazione, messaggi di navigazione) consentono a strumenti terzi, integratori e ricercatori di produrre o consumare missioni senza dipendere dai segreti di un unico costruttore.

Assumiamo un confine chiaro: **l’apertura riguarda innanzitutto le fondamenta generiche e le interfacce**; l’integrazione industriale e la catena di sicurezza propria della macchina restano sotto la responsabilità del costruttore. Aprire un bene comune deve accompagnarsi a una chiara catena di responsabilità, rendendo al contempo condivisibili le conoscenze necessarie all’interoperabilità, alla manutenzione e all’innovazione collettiva.

## Una progettazione proporzionata, modulare, aperta e responsabile

Perché una robotica serva l’agroecologia, le sue scelte di progettazione devono essere coerenti.

Privilegiamo macchine **proporzionate** agli usi: abbastanza capaci da rendere un servizio reale, abbastanza leggere e sobrie da restare accessibili, manutenibili e compatibili con la cura del suolo.

Privilegiamo la **modularità**: separare il portante, gli attrezzi, i sensori e le funzioni software, per riparare, adattare, fare retrofit e condividere senza ricostruire tutto a ogni evoluzione.

Privilegiamo l’**apertura**: interfacce pubbliche, documentazione, test, versionamento e licenze che permettono studio, uso, modifica e ridistribuzione. L’open source non è un fine in sé. È un metodo industriale per mettere in comune le fondamenta e preservare la sovranità d’uso nel tempo.

Privilegiamo infine un’innovazione **responsabile**: anticipare gli effetti sociali e ambientali, associare gli utenti, documentare i limiti d’impiego, governare con attenzione i dati agricoli e mantenere una responsabilità industriale esplicita su ogni macchina messa in servizio.

Questi principi non costituiscono un’etichetta. Costituiscono un’esigenza di coerenza: una tecnologia è utile solo se aumenta durevolmente la capacità delle contadine e dei contadini di comprendere, decidere e agire.

## Ciò che l’apertura apporta

In un settore frammentato, troppa energia è dedicata a reimplementare le stesse fondamenta. Mettere in comune questi mattoni non distrugge l’attività industriale: **la sposta**.

Per le contadine e i contadini, la posta è la sovranità d’uso: diagnosticare, riparare, far evolvere, scegliere un fornitore di servizi e conservare l’accesso ai dati. Per i costruttori, la differenziazione si sposta verso l’integrazione, la robustezza, la sicurezza dimostrata e il servizio. Per le officine e gli integratori, le interfacce documentate rendono possibili una competenza locale e una capillarità territoriale. Per la ricerca e l’insegnamento, i formati aperti permettono finalmente di confrontare, insegnare e trasmettere.

Un bene comune tecnologico ha bisogno di documentazione, manutenzione e governance. L’apertura è duratura solo se modelli economici — macchine, strumenti, servizi, formazione — consentono alle imprese di vivere senza ricreare la captività con altri mezzi.

Anche con un codice software aperto, sicurezza, conformità e responsabilità restano legate a ogni configurazione messa in servizio. Una funzione autonoma ha senso solo in un dominio d’impiego esplicito, con comportamenti prevedibili fuori dominio e prove di arresto sicuro. Rifiutiamo l’opposizione ingenua tra apertura e industrializzazione: industrializzare significa anche rendere riproducibili la qualità, la manutenzione, l’interoperabilità e la sicurezza.

## Appello

La diffusione di una robotica agricola al servizio dell’agroecologia si costruisce con e presso gli utenti, di concerto con i costruttori e le comunità tecniche.

Ognuno può contribuire secondo le proprie competenze: pubblicare un’interfaccia, documentare una procedura, proporre uno strumento compatibile, migliorare un mattone, ospitare una sperimentazione, formare un vicino, condividere ritorni d’uso accompagnati dai loro limiti.

**Aprire la robotica agricola significa rifiutare che diventi uno strumento di dipendenza. Significa dare al mondo agricolo i mezzi per partecipare alla sua concezione, per padroneggiarne gli usi e per trasmetterne le conoscenze.**

Unitevi all’ecosistema: [github.com/Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops)

---

## L’autore

**Autore: Alexandre Prévault-Osmani — CTO e cofondatore di SABI AGRI.**

Dal 2015 Alexandre Prévault-Osmani lavora all’intersezione tra elettrificazione, robotica agricola, open source e agroecologia. Sviluppa un approccio industriale volto a rendere le tecnologie agricole accessibili, interoperabili, manutenibili e appropriabili dal mondo contadino.

[GitHub](https://github.com/Alexandre-PO) · [LinkedIn](https://www.linkedin.com/in/alexandre-po)

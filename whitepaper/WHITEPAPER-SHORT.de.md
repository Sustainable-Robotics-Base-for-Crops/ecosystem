# SMOR: auf dem Weg zu einem verbreitungsfähigen Standard der Agrarrobotik im Dienst der Agrarökologie

### Sustainable Robotics Base for Crops

Autor: Alexandre Prévault-Osmani — CTO und Mitgründer von SABI AGRI

*Weißbuch · Kurzfassung · September 2026 · Lizenz CC BY 4.0*

---

## Inhalt

1. [Zusammenfassung](#zusammenfassung)
2. [Grundbegriffe](#grundbegriffe)
3. [These und Positionierung](#these-und-positionierung)
4. [Was die Verbreitung bremst](#was-die-verbreitung-bremst)
5. [Die SMOR-Vision](#die-smor-vision)
6. [Eine Referenzarchitektur und eine offene Nachweiskette](#eine-referenzarchitektur-und-eine-offene-nachweiskette)
7. [Der SRBC-Roboter, eine erste Verkörperung](#der-srbc-roboter-eine-erste-verkörperung)
8. [Bewerten, was für den Betrieb zählt](#bewerten-was-für-den-betrieb-zählt)
9. [Ein Commons, das der bäuerlichen Welt gehört](#ein-commons-das-der-bäuerlichen-welt-gehört)
10. [Sicherheit, Konformität und Mitverantwortung](#sicherheit-konformität-und-mitverantwortung)
11. [Vom Code zum Commons: die Roadmap](#vom-code-zum-commons-die-roadmap)
12. [Grenzen und Aufruf](#grenzen-und-aufruf)
13. [Literatur](#literatur)
14. [Über den Autor](#über-den-autor)

---

## Zusammenfassung

Agrarrobotik verspricht, körperliche Belastung zu verringern, auf Schwierigkeiten bei der Personalgewinnung zu antworten und präzisere Eingriffe zu ermöglichen. Zehn Jahre nach den ersten Robotern auf den Feldern bleibt ihre Verbreitung dennoch gering. Eine gelungene Vorführung sagt wenig über die Verfügbarkeit einer Maschine während einer Saison, über die agronomische Qualität ihrer Arbeit oder über ihre Tragfähigkeit im Alltag eines Betriebs. Die Herausforderung verschiebt sich: Einen Roboter zum Laufen zu bringen, zählt heute weniger, als die Bedingungen für seine dauerhafte Einführung zu schaffen.

Wir vertreten die Auffassung, dass Robotik vorrangig kleinen und mittleren diversifizierten Betrieben zugutekommen soll, die sich in einem agrarökologischen Wandel befinden. Dafür schlagen wir die SMOR-Vision vor — *Small, Modular, Open & Responsible* —, umgesetzt in eine Referenzarchitektur, eine offene Dokumentenkette, die verbindet, was der Roboter tun sollte und was er tatsächlich getan hat, eine Bewertungsmethode, ein Commons-Modell, das der bäuerlichen Welt gehört, und eine ausdrückliche Verteilung der Verantwortung. Der SRBC-Roboter ist ihre erste industrielle Verkörperung. SMOR ist ein Rahmen, der sich bewähren muss: Dieser Text legt These und Vorschläge dar, die vollständige Fassung wird die Nachweise liefern.

---

## Grundbegriffe

- **ODD** (Operational Design Domain, Einsatzbereich): die Bedingungen, unter denen eine autonome Funktion entworfen und validiert wurde — Parzelle, Boden, Wetter, Hangneigung, Lokalisierungsqualität, Anwesenheit von Personen.
- **Missionsauftrag**: Datei, die beschreibt, was der Roboter tun soll, in welchen Grenzen und mit welchen zulässigen Reaktionen.
- **Geleistete Arbeit**: Datei, die beschreibt, was der Roboter getan hat, unter welchen angetroffenen Bedingungen und wie der Betrieb die erbrachte Leistung beurteilt.
- **Open Core**: Modell, bei dem Schnittstellen und generische Bausteine offen sind, während materielle Umsetzung, Kalibrierung und Dienste in der Verantwortung des Herstellers bleiben.

---

## These und Positionierung

Seit Mitte der 2010er Jahre hat die Agrarrobotik die Labore verlassen und die Felder erreicht. Die Fortschritte in Wahrnehmung, Navigation und Automatisierung sind real; die kommerzielle Verbreitung bleibt gemessen an der Vielfalt der Produktionen und der Zahl der Betriebe bescheiden [1, 2]. Diese Lücke verlangt nach einer anderen Definition von Reife.

Unser Ansatz ist einfach: Die Reife eines Agrarroboters bemisst sich an seiner **Verbreitungsfähigkeit**, also an seiner Fähigkeit, über die langen Zeiträume der Landwirtschaft genutzt, gewartet, repariert und verbessert zu werden. Sie setzt die Passung zu einem klar benannten agronomischen und menschlichen Bedarf voraus, erschwingliche Kosten, nachgewiesene Sicherheit in einem ausdrücklichen Einsatzbereich, Wartung in der Nähe und eine echte Aneignung durch die Menschen, die ihn nutzen.

Wir treffen eine ausdrückliche Positionierungsentscheidung: Agrarrobotik soll vorrangig kleinen und mittleren Betrieben zugutekommen, insbesondere wenn sie diversifiziert sind und sich in einem agrarökologischen Wandel befinden. Wir definieren sie zuerst als landwirtschaftliche Unternehmen menschlichen Maßstabs, in denen die Person, die das Land bewirtschaftet, eine direkte Fähigkeit zur Beobachtung und Entscheidung über Kulturen und Böden behält; die Klassifikation der französischen Agrarstrukturerhebung nach Standardoutput liefert dafür einen statistischen Anhaltspunkt [3]. Diese Betriebe tragen die Vielfalt der Produktion, die Pflege der Landschaften, die ländliche Beschäftigung und kontextbezogenes Wissen. Sie sind zugleich am stärksten den Arbeitskosten, der körperlichen Belastung und den Investitionshürden ausgesetzt.

Agrarökologische Praktiken verlangen mehr Beobachtung, mehr Präzision und differenziertere Eingriffe [4]. Diese agronomische Intensität ist schwer durchzuhalten, wenn menschliche Arbeit gegenüber Skaleneffekten als bloßer Kostenfaktor zählt. Robotik kann dieses Verhältnis neu ausbalancieren, indem sie Belastung verringert und Arbeiten ermöglicht, die Böden und Ökosystemen zugutekommen: eine präzise Aussaat, die eine frühe mechanische Unkrautregulierung vorbereitet, wiederholte Überfahrten eines leichten Geräts in einem kurzen Zeitfenster, eine leichte Maschine dort, wo die Tragfähigkeit des Bodens es verlangt.

Dieselbe Technologie kann auch der Konzentration der Produktionsmittel, der Abhängigkeit von proprietären Anbietern und der schnellen Obsoleszenz der Ausrüstung dienen [5, 6]. Die Richtung hängt von Entscheidungen über Architektur, Geschäftsmodell und Governance ab. Der Gegensatz zwischen den kurzen Zyklen der Digitaltechnik und den langen Zeiträumen der Landwirtschaft macht dies zu einer strukturellen Frage: Eine Maschine, die man nicht mehr verstehen, warten oder anpassen kann, wird zur Belastung, selbst wenn sie anfangs leistungsfähig war.

Wir unterscheiden drei Ebenen: die **technische Fähigkeit** des Roboters (fahren, einer Reihe folgen, ein Gerät sicher steuern), die **agronomische Leistung** in einem gegebenen Zeitfenster (eine gleichmäßige Aussaat, ein wirksames Hacken) und die **agrarökologische Wirkung**, die sich über die Zeit auf der Ebene des Anbausystems zeigt (vermiedene Betriebsmittel, Bodenzustand, Biodiversität, Arbeitsbedingungen, Autonomie des Betriebs, Vollkosten). Bestehende Bewertungsverfahren dokumentieren vor allem die erste Ebene; über den Nutzen eines Roboters für einen Betrieb entscheiden die beiden anderen.

> **These**  
> Agrarrobotik wird zu einem Hebel für die Verbreitung der Agrarökologie, wenn sie nützlich, zugänglich, wartbar, sicher, interoperabel und aneignungsfähig gestaltet ist und ihre Leistung unter realen Bedingungen nachweisen kann.

Wir fügen eine methodische Überzeugung hinzu: Verbreitung ist ebenso eine Frage der **Darstellung** wie der Messung. Solange agronomische Absicht und erzieltes Ergebnis in unterschiedlichen Vokabularen beschrieben werden, bleiben Rückmeldungen aus dem Feld vereinzelt, die Ergebnisse zweier Hersteller unvergleichbar und die Verantwortlichkeiten unüberprüfbar. Ein gemeinsames, versioniertes Vokabular ist die erste Bedingung für kumulatives Wissen.

---

## Was die Verbreitung bremst

Ein Agrarroboter arbeitet im Kontakt mit lebendigen Systemen: Boden, Vegetation, Wetter und Arbeitsorganisation verändern sich innerhalb einer Saison. Jede Leistung muss daher auf eine Nutzung, eine Konfiguration und einen ausdrücklichen Einsatzbereich bezogen werden.

Die Hürden sind bekannt und hängen voneinander ab [1, 7]: die **Robustheit** über eine ganze Saison; die **Sicherheit**, die verlangt, gefährliche Situationen zu erkennen und einen sicheren Zustand zu erreichen; die **agronomische Leistung**, die sich eher an der Arbeitsqualität des Geräts als an der Präzision der Fahrspur misst; die **Wirtschaftlichkeit**, die weit mehr von Überwachungszeit, Wartung und Stillstand abhängt als vom Kaufpreis; die **Interoperabilität**, schwach, solange Formate, Schnittstellen und Protokolle herstellerspezifisch bleiben, und die daraus folgende **technologische Abhängigkeit**. Neuere Arbeiten zeigen, dass die menschliche Zeit für Logistik und Überwachung das eigentliche Problem der kleinskaligen Robotik ist [7].

Die Präzisionslandwirtschaft verfügt bereits über wertvolle Standards wie ISOXML oder ADAPT, um einen Auftrag und die ausgeführte Arbeit zu beschreiben [8, 9]. Sie wurden für eine Person am Steuer entworfen, die den Einsatzbereich verantwortet. Mit einem Roboter geht ein Teil der Beobachtung und Entscheidung auf die Maschine über, und die Kette von der Absicht zur Ausführung muss ausdrücklich werden: was der Roboter tun soll, unter welchen Bedingungen er dazu befugt ist, wie er auf Unvorhergesehenes reagiert, was er angetroffen und was er geleistet hat. Die Industrie erkennt diesen Bedarf an, mit dem AEF-Arbeitsfeld zu autonomen Maschinen [10], ebenso die Forschung zum landwirtschaftlichen Einsatzbereich [11]. Wir betrachten diese Arbeiten als konvergent und möchten mit einem offenen, bereits im Feld genutzten Vorschlag dazu beitragen.

Die Literatur, die Robotik aus agrarökologischer Sicht befragt, ist sich in einem Punkt einig: Die Richtung ist offen. Dieselbe Technologie kann zu Flotten kleiner Maschinen im Dienst diversifizierter Systeme führen oder zu großen Maschinen, die Monokulturen festigen [6]. Autonome Funktionen in agrarökologische Systeme zu bringen, verlangt eine Gestaltung mit vielfältigen Beteiligten, jenseits einer „monokulturellen Denkweise“ [5], und Landwirtinnen und Landwirte zählen Verantwortung, Sicherheit und Datenhoheit zu ihren wichtigsten Anliegen [12]. Diese Ergebnisse begründen unsere Entscheidung, den Bäuerinnen und Bauern die Entscheidung über die Nutzung ihrer Technologie und deren Gewähr anzuvertrauen.

---

## Die SMOR-Vision

SMOR ist ein Gestaltungs- und Bewertungsrahmen, der die Eigenschaften eines Roboters mit seinen agronomischen, wirtschaftlichen, ökologischen und sozialen Wirkungen verbindet. Derzeit hat er den Status eines Vorschlags, der sich im Feld und in der Diskussion bewähren muss.

Wir setzen überwiegend auf elektrischen Antrieb und elektrische Aktoren. Elektromotoren und -zylinder lassen sich fein steuern, melden ihren Zustand zurück und fügen sich direkt in Diagnosesysteme ein. Der Strom kann aus dem Netz kommen oder auf dem Betrieb erzeugt werden, was den Weg zu einer vollständigen oder teilweisen Energieautonomie öffnet; Batterien und Motoren sind dennoch über ihren Lebenszyklus zu bewerten.

**Small: ein angemessener Maßstab.** Wir bevorzugen Maschinen, deren Masse, Leistung und Abmessungen den Arbeiten angemessen bleiben. Unser dimensionales Ziel liegt zwischen Mensch und Zugpferd: etwa 80 bis 1 200 kg, unter 10 km/h, wenige Kilowatt, eine Autonomie von einem halben bis zu einem ganzen Arbeitstag, Kleinspannung und für leichte Trägerfahrzeuge eine Investition unter 40 000 Euro. Darüber hinaus führt die Masse die Maschine in die Welt des Traktors zurück, mit dessen Motorisierung, Logistik und Preis. Diese Werte sind Gestaltungsziele. Eine begrenzte Masse verringert die beteiligte Energie und erleichtert Transport und Wartung; die Wirkung auf den Boden hängt zudem von Kontaktdruck, Schlupf, Zahl der Überfahrten und Feuchte ab [13]. Dieser Maßstab erlaubt mehrere spezialisierte oder zwischen Betrieben geteilte Roboter statt einer einzigen Maschine, die für die schwerste Arbeit ausgelegt ist. Zu einem dauerhaften wirtschaftlichen Vorteil wird er, wenn die menschliche Zeit je Hektar tatsächlich sinkt, was zuverlässige Missionen ohne ständige Überwachung und auf Dauer die Überwachung mehrerer Roboter durch eine einzige Person voraussetzt.

**Modular: anpassen, reparieren, gemeinsam nutzen.** Wir trennen eine stabile Basis (Struktur, Energie, Steuerung, Schnittstellen, Sicherheit) von Modulen, die an Kulturen, Geräte und Kontexte angepasst sind: Gerät, Fahrwerk oder Sensor wechseln, ohne das Trägerfahrzeug zu ersetzen, eine Softwarefunktion weiterentwickeln, ohne das Ganze neu zu bauen, eine Maschine im Rhythmus des Anbaukalenders nachrüsten. Diese Modularität beruht auf dokumentierten Abmessungen, Steckverbindungen, Protokollen und Formaten; ohne sie bliebe sie dem ursprünglichen Anbieter ausgeliefert.

**Open: Souveränität auf Dauer.** Wir öffnen vorrangig Schnittstellen, Missions- und Datenformate, Dokumentation und generische Softwarebausteine, dann die Konstruktionspläne, wenn ihre Veröffentlichung die Reparierbarkeit stärkt. Das Open Source, für das wir eintreten, ist eine industrielle Methode: ausdrückliche Lizenzen, versionierte Verträge, Tests, Dokumentation, Governance und stabile Versionen. Es sichert den Betrieben Nutzungssouveränität (diagnostizieren, reparieren, anpassen, durch einen anderen Dienstleister warten lassen), verlagert die Differenzierung der Hersteller auf Integration, Sicherheit und Service und ermöglicht dauerhafte Kompetenz in den Werkstätten der Regionen.

**Responsible: eine rechenschaftspflichtige Innovation.** Eine Technologie wird verantwortungsvoll, wenn ihre Wirkungen mit den Betroffenen vorausgesehen, diskutiert, gemessen und korrigiert werden [14]. Dieses Prinzip verpflichtet dazu, Landwirtinnen und Landwirte an der Bedarfsbestimmung und Bewertung zu beteiligen, Sicherheit von Anfang an zu gestalten, Einsatzgrenzen zu dokumentieren, den Verbrauch an Material, Energie und digitalen Ressourcen zu messen, die bäuerliche Entscheidung zu bewahren, die Datenhoheit des Betriebs zu sichern und die Verteilung der Verantwortung überprüfbar zu machen.

Diese vier Prinzipien bilden ein Ganzes. Ein kleiner geschlossener Roboter bleibt gefangen und altert schnell; eine offene Plattform ohne Governance zerfällt; eine modulare, aber zu teure Maschine bleibt ohne Wirkung auf die Verbreitung. **SMOR schlägt eine Gesamtkohärenz vor: eine Robotik, deren Leistung sich daran bemisst, Agrarökologie praktikabel, wirtschaftlich tragfähig und dauerhaft für die bäuerliche Welt aneignungsfähig zu machen.**

---

## Eine Referenzarchitektur und eine offene Nachweiskette

Eine Referenzarchitektur liefert eine gemeinsame Sprache: Sie trennt die Funktionen und definiert die Schnittstellen, über die sich eine Komponente ersetzen lässt, ohne das System neu zu bauen. Jeder Hersteller bleibt in seinen Hardwareentscheidungen frei, sofern er die gemeinsamen Verträge und Sicherheitsanforderungen einhält. Wir schlagen sechs Schichten vor: Energie und Aktoren, Fahrzeugsteuerung, dokumentierte Feldbusse, Bordrechner (ROS 2 bildet dafür heute eine geeignete Grundlage), Wahrnehmung und Lokalisierung, Mission und Benutzeroberfläche. Ein Prinzip zieht sich durch alle: **Sicherheitsrelevante Funktionen bleiben unabhängig vom Universalrechner und von jeder Fernverbindung.** Wesentliche Funktionen bleiben offline verfügbar, und die Oberfläche macht den Zustand des Roboters, seine Grenzen und die Ursache jedes Halts sichtbar.

Der wichtigste Vertrag ist die **Fahrzeugschnittstelle**, die Befehle, Zustände, Gerätefähigkeiten und Fehler beschreibt. Sie erlaubt es, dieselbe Navigationsfunktion an mehrere Trägerfahrzeuge anzupassen, und macht so aus einem Produkt eine Plattform.

Der zweite Vertrag betrifft die Mission. Wir schlagen **JSON Agri** vor, ein offenes, unter CC BY 4.0 veröffentlichtes Format [15], lesbar ohne IT-Ausbildung und maschinell überprüfbar. Es organisiert eine Kette aus zwei Dokumenten. Der **Missionsauftrag** beschreibt das agronomische Ziel und seine Abnahmekriterien, die Kombination aus Trägerfahrzeug und Gerät, den zulässigen Einsatzbereich, die Fahrspur, die erlaubten Zonen und die vorgesehenen Reaktionen auf Ereignisse: Eine schwache Batterie löst etwa eine Rückkehr zur Ladezone über zulässige Wege aus. Die **geleistete Arbeit** verbindet diese Absicht mit den angetroffenen Bedingungen, den Ereignissen, den menschlichen Eingriffen, den Leistungsindikatoren und der agronomischen Beurteilung durch den Betrieb. Ein digitaler Fingerabdruck des Auftrags, in die geleistete Arbeit übernommen, garantiert, dass die Ausführung mit der exakten Version der Mission verglichen wird.

Drei Entscheidungen geben dieser Kette ihre Tragweite. Zulässiger Einsatzbereich und angetroffene Bedingungen teilen dasselbe Vokabular, sodass jede Abweichung mit einer Erkennung, einer Entscheidung, einer Verantwortung und einem Nachweis verknüpft werden kann. Die Reaktionen auf Ereignisse bilden ein geschlossenes Vokabular: Die Maschine verweigert jede Anweisung, die unbekannt ist oder im vom Hersteller validierten Katalog fehlt, und ihre Sicherheitsuntergrenze bleibt für jede Datei unerreichbar. Die in der Simulation erzeugte Bescheinigung belegt, dass eine Datei definierte Prüfungen unter benannten Annahmen bestanden hat; sie gilt als Prüfnachweis, verschieden von einem Zertifikat.

Die Kette trennt so drei Validierungen: die **Vorbereitung** im Missionseditor; die **operative** Validierung an Bord, bei der der Roboter die Mission mit seiner Konfiguration und den vor Ort bestätigten Bedingungen abgleicht und die Freiheit zur Verweigerung behält; die Validierung der **Leistung** nach der Mission durch die agronomische Beurteilung des Betriebs. Diese Trennung schützt vor zwei kostspieligen Verwechslungen: eine Simulation für eine Genehmigung zu halten oder eine abgeschlossene Mission für eine gelungene Leistung. Öffentliche Spezifikationsregeln (ein kleiner, stabiler Kern, fehlende Daten als solche gekennzeichnet, garantierte Kompatibilität, Offline-Validierung), Konformitätsstufen und ein Validator erlauben jeder dritten Partei, ihre Implementierung eigenständig zu prüfen. JSON Agri ergänzt so die bestehenden Standards um die Autonomiekette, die sie unausgesprochen lassen.

---

## Der SRBC-Roboter, eine erste Verkörperung

Der von SABI AGRI entwickelte SRBC-Roboter erprobt diese Prinzipien an einer Maschine, die verkauft und im Feld eingesetzt wird. Dieses kompakte elektrische Trägerfahrzeug auf Rädern oder Ketten wiegt in der Kettenversion rund 250 kg und liegt damit im unteren Bereich des SMOR-Rahmens. Es trägt Geräte für leichte Bodenbearbeitung, Aussaat, Kulturpflege und Transport. Seine Hardware-Sicherheitskette arbeitet unabhängig vom Rechner, und die übergeordneten Schutzfunktionen (Geofencing, Sicherheitsvision) setzen ihre Befehle über eine Prioritätsarbitrierung gegenüber der Navigation durch. **Die geschulte Person, die den Roboter bedient, legt den Einsatzbereich fest und hält ihn ein; die übergeordnete Software trägt dazu bei, Vorfälle zu vermeiden; die untergeordnete Steuerung garantiert die Rückkehr in einen sicheren Zustand.**

Navigation, Lokalisierung, Geofencing, Sicherheitswahrnehmung, Simulation, das Format JSON Agri und die Missionseditoren sind auf der GitHub-Organisation [Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops) veröffentlicht, unter Apache 2.0 für den Code und CC BY 4.0 für die Spezifikationen. Der Roboter, der auf der Parzelle arbeitet, führt diesen öffentlichen Code aus. Die Steuerungssoftware, der Fahrzeugtreiber, die Steuerungsverträge, die Kalibrierungen und die Ferndienste bleiben in der Verantwortung des Herstellers: SRBC ist ein **industrieller Open Core**, und wir beschreiben seine Offenheit so, wie sie ist.

Jede externe Organisation kann damit einen simulierten Roboter durchgängig betreiben, eine Mission vorbereiten und validieren, einen realen Roboter über eine veröffentlichte Schnittstelle beobachten, die Konformität ihrer Dateien prüfen und jeden Navigationsbaustein wiederverwenden. Die nächsten Öffnungsschritte werden es ermöglichen, den Roboter zu steuern, den Software-Stack auf andere Fahrzeuge zu übertragen und eine Maschine aus öffentlichem Code aufzubauen.

---

## Bewerten, was für den Betrieb zählt

Eine einzelne Vorführung liefert ein Beispiel; ein dokumentiertes, wiederholtes und vergleichbares Protokoll liefert einen Nachweis. Unsere Methode verknüpft jedes Ergebnis mit einer agronomischen Arbeit, einer Referenzsituation (Handarbeit, Traktor, frühere Praxis), einem Einsatzbereich, einer Konfiguration und einem versionierten Indikatorenkatalog, die alle vor dem Versuch festgelegt werden. Getragen von der Kette aus Missionsauftrag und geleisteter Arbeit, erlaubt diese Verknüpfung Dritten, das von uns Veröffentlichte nachzurechnen. Die Indikatoren umfassen agronomische Leistung, Verfügbarkeit, Energie, Sicherheit, menschliche Zeit, Vollkosten und Bodenwirkungen; sie werden mit ihrer Berechnungskonvention, ihrer Streuung und ihrer Abdeckung veröffentlicht. Ein fehlender Wert wird als solcher ausgewiesen: Das Fehlen ist eine Information.

Die Maschine kann ihre Dauer, ihre Fahrspur, ihre Energie und die Qualität ihrer Lokalisierung messen. Die Größen, die über den Nutzen für den Betrieb entscheiden, hängen oft von einer Person ab: tatsächlich angetroffene Bedingungen, agronomische Zufriedenheit, Überwachungszeit, Bedarf an einer zweiten Überfahrt. Wir schlagen vor, sie zu drei Zeitpunkten zu erfassen, dort, wo sich die Person befindet: bei der Vorbereitung, beim Laden auf den Roboter und am Ende der Mission, mit einem Werkzeug, das vorausfüllt, was es kann, und wenige Fragen stellt. Ebenso wird eine gemessene Größe zum Kriterium, wenn jemand ihren Schwellenwert im Missionsauftrag festlegt und die Maschine weiß, wie sie bei seiner Überschreitung reagiert.

Unsere ersten instrumentierten Kampagnen bestätigen die Machbarkeit dieser Kette über verschiedene Roboter, Betriebe und Geräte hinweg. Die Nachweisbasis wird mit ihren Erfolgen wie mit ihren Misserfolgen wachsen, um festzustellen, wo, wann und unter welchen Bedingungen Robotik einen echten agrarökologischen Nutzen bringt.

---

## Ein Commons, das der bäuerlichen Welt gehört

Wir vertreten die Auffassung, dass das Software-Ökosystem der Agrarrobotik — Dateiformate, Code zur Spurführung, Entscheidungsalgorithmen, Missions- und Rückverfolgungswerkzeuge — zu einem **Commons werden soll, das der bäuerlichen Welt gehört und das die bäuerliche Welt sich aneignet**.

Dieses Commons ist zuerst ein Vokabular. Ein Betrieb beschreibt seine Erwartung in agronomischen Begriffen, ein Händler in Begriffen des Service, ein Hersteller in Begriffen von Funktionen. Die erste Aufgabe des Commons ist es, diesen Beteiligten zu ermöglichen, **Tatsachen in denselben Begriffen zu beschreiben, auszutauschen und anzufechten**. Offener Code macht dieses Vokabular nutzbar und beweist im Betrieb, dass es funktioniert; das Vokabular macht den Code austauschbar und damit das Commons steuerbar. Ein Format, das mehrere Implementierungen lesen können, entzieht sich jeder Vereinnahmung, auch durch das Unternehmen, das es ins Leben gerufen hat.

Unter bäuerlicher Welt verstehen wir die Bäuerinnen und Bauern sowie die Werkstätten, Händler, Genossenschaften, Institute und Hersteller, die in ihrem Dienst arbeiten. Diese Zugehörigkeit entsteht durch fünf überprüfbare Eigenschaften:

- **es bleibt offen**: Lizenzen sichern die freie Nutzung auf Dauer, und die Marke schützt den Sinn der Begriffe;
- **es überdauert das Unternehmen, das es ins Leben gerufen hat**: öffentliche Repositorien, Historie und Dokumentation erlauben es anderen, es weiterzuführen; auf Dauer wird sein Eigentum einer gemeinnützigen Struktur übertragen, unabhängig von jedem Hersteller, deren geborene Mitglieder die Bäuerinnen und Bauern und ihre Organisationen sind;
- **es wird mit den Menschen gesteuert, denen es dient**: Bäuerinnen und Bauern wirken an den Entscheidungen über seinen Zweck mit und verfügen über ein Einspruchsrecht;
- **es gibt die Daten dem Betrieb zurück**: Die geleistete Arbeit gehört dem Betrieb, der sie lesen, aufbewahren, weitergeben oder für sich behalten kann, ohne über einen Anbieter zu gehen [12];
- **es lässt sich erlernen**: lesbare Werkzeuge, Schulungen unter Gleichen und lokale Werkstätten stellen es in die Tradition der technischen Volksbildung.

Die Bestandteile eines Roboters verlangen unterschiedliche Grade der Offenheit. **Gemeinsame Verträge** (Formate, Indikatoren, Schnittstellen, Konformitätskriterien) werden vorrangig geöffnet; **generische Bausteine** (Navigation, Simulation, Diagnose, Editoren) entwickeln sich als Software-Commons; **industrielle Integration** und Sicherheitskette liegen beim Hersteller; **sensible Dienste und Daten** behalten einen kontrollierten Zugang. Die Regel, die einen Open Core vertretbar macht, passt in einen Satz: **Man öffnet die Verträge und die generische Logik; man behält die materielle Umsetzung, die Kalibrierung und die Flottendienste.** Der Vorteil eines Herstellers liegt in seiner Maschine, seiner Sicherheitskette, seinem Servicenetz und seiner Fähigkeit, seine Zusagen auf Dauer einzuhalten.

Offenheit verlagert Wert und Kosten. Sie verringert die erneute Implementierung derselben Grundlagen und schafft Bedarf an Wartung und Governance, der finanziert werden muss. Verkauf und Vermietung von Maschinen, lokale Anpassung, Serviceverträge, gepflegte Versionen, Schulung und Begleitung bei der Konformität tragen die Unternehmen, sofern sie auf Gefangenschaft durch zurückgehaltene Daten, für den Grundbetrieb unverzichtbare Abonnements oder künstlich geschlossene Schnittstellen verzichten. Wir wenden Apache 2.0 auf den Code und CC BY 4.0 auf Spezifikationen und Texte an; die Frage einer Gegenseitigkeit für bestimmte Bestandteile wird gemeinsam entschieden.

Die Governance folgt der Nutzung. Entscheidungen zum Format werden bereits öffentlich festgehalten, und ein schriftliches Verfahren erlaubt es, sie anzufechten. Mehrere Stufen, ausgelöst durch beobachtbare Tatsachen, ordnen das Weitere, beginnend mit einem Versionsausschuss ab der ersten Implementierung durch Dritte, dann einem Kollegium der Nutzungen mit Einspruchsrecht, sobald ein Zusammenschluss von Landwirtinnen und Landwirten, eine Genossenschaft oder ein Händler vom Format abhängt. Die letzte Stufe überträgt das Eigentum an Format und Marke auf die oben beschriebene gemeinnützige Struktur; sie macht das Commons unabhängig von dem Unternehmen, das es ins Leben gerufen hat, und wir betrachten sie als Bedingung für die Glaubwürdigkeit des Ganzen.

---

## Sicherheit, Konformität und Mitverantwortung

Die Konformität einer autonomen Maschine prägt ihre Gestaltung, ihre Prüfungen und ihre Überwachung während ihrer gesamten Lebensdauer. Die Maschinenrichtlinie 2006/42/EG gilt bis zum 19. Januar 2027, danach übernimmt die Verordnung (EU) 2023/1230 [16]; die Normenreihe ISO 18497:2024 behandelt autonome Landmaschinen [17]. Offener Code erleichtert Prüfung, Rückverfolgbarkeit und Wartung. Sicherheit und Konformität bleiben dagegen an jede in Verkehr gebrachte oder in Betrieb genommene Maschine gebunden, an ihre Risikobeurteilung, ihre Prüfungen und ihre validierte Konfiguration. Eine Reparatur, die die Konformität wahrt, bleibt eine Reparatur, und Offenheit soll sie gerade erleichtern; eine Änderung, die eine neue Gefährdung schafft, verpflichtet die Person oder Stelle, die sie vornimmt. Die Teams, die das Commons pflegen, verantworten die Qualität der Beiträge; die Validierung der Integration obliegt der Stelle, die die Maschine in Betrieb nimmt.

Wir schlagen vor, diese regulatorische Verteilung um eine **operative Mitverantwortung** zu ergänzen, die für jeden Schritt festlegt, wer entscheidet, wer validiert und welcher Nachweis aufbewahrt wird.

| Schritt | Entscheidet | Validiert | Aufbewahrter Nachweis |
|---|---|---|---|
| Agronomische Wahl und Arbeitsfenster | Landwirtin/Landwirt | Landwirtin/Landwirt | Absicht und Kriterien im Missionsauftrag |
| Parzellenkarte und bekannte Hindernisse | Landwirtin/Landwirt | Landwirtin/Landwirt | referenzierte Parzellenkarte |
| Zulässiger Einsatzbereich und Reaktionen auf Ereignisse | Landwirtin/Landwirt oder Bedienperson | Sicherheitsuntergrenze des Herstellers | Einsatzbereich und Strategien im Auftrag |
| Geräteanbau und Prüfung vor dem Start | Bedienperson | Bedienperson | geplante und genutzte Konfiguration |
| Ausführung | Maschine, frei zur Verweigerung | Herstellergrenzen, Not-Halt | Ereignisse, angeforderte und ausgeführte Aktionen |
| Beurteilung der erbrachten Leistung | Landwirtin/Landwirt | Landwirtin/Landwirt | Beurteilung in der geleisteten Arbeit |

Ein Feld ohne Zuständigkeit ist ein Ergebnis: Es zeigt eine zu behebende Lücke an. Eine von zwei Parteien unterschiedlich verstandene Verantwortung ist ebenfalls ein Ergebnis, das offen zu besprechen ist. Diese Mitverantwortung ordnet die tägliche Zusammenarbeit und lässt die regulatorische Verantwortung des Herstellers oder Integrators vollständig bestehen. **Es geht darum, Wissen teilbar zu machen und zugleich eine ausdrückliche Verantwortung für jede in Betrieb genommene Maschine aufrechtzuerhalten.**

---

## Vom Code zum Commons: die Roadmap

Die Verbreitung von SMOR wird sich an der Fähigkeit externer Organisationen messen, die Schnittstellen zu verstehen, einen Versuch zu wiederholen, einen Baustein anzupassen, eine geleistete Arbeit zu lesen und eine Maschine unabhängig von ihrem Entwickler zu warten. Wir gehen in vier Stufen vor: **sichtbar machen**, was existiert, mit Status und Grenzen; **reproduzierbar machen**, wie eine Mission installiert und simuliert wird; **interoperabel machen**, indem Verträge und Tests veröffentlicht werden; **verbreitungsfähig machen**, indem Nachweise, Kompetenzen und Dienste im Feld aufgebaut werden.

Daraus ergeben sich fünf Arbeitsfelder: die offene Basis festigen; die Steuerungsverträge und die Fahrzeugschnittstelle veröffentlichen und dann eine zweite Implementierung des Formats durch eine externe Organisation erreichen, Voraussetzung, um von einem Standard zu sprechen; eine von einem unabhängigen Institut geprüfte Nachweisbasis aufbauen, mit über mehrere Kampagnen gemessenen Vollkosten und menschlicher Zeit; die Sicherheit jeder vermarkteten Konfiguration organisieren; regionale Kompetenzen entwickeln, damit Betriebe, Werkstätten und Händler diagnostizieren, reparieren und ihrerseits schulen können, denn man steuert, was man versteht. Die Einführung schreitet in Kreisen voran, von der internen Nutzung über vertrauenswürdige Partner bis zu Integrationen durch Dritte und einer breiten Verbreitung, wobei jeder Übergang von beobachtbaren Kriterien abhängt. Downloadzahlen zeigen Interesse; landwirtschaftliche Verbreitung beweist sich im Feld.

---

## Grenzen und Aufruf

Dieser Text schlägt einen konzeptionellen und technischen Rahmen vor; der Nachweis seines agronomischen und wirtschaftlichen Nutzens verlangt wiederholte Kampagnen und mehrjährige Beobachtungen, die die vollständige Fassung dokumentieren wird. Wir kennen seine Grenzen: Der SMOR-Rahmen ist ein Gestaltungsziel; SRBC ist eine erste Fallstudie, getragen von einem Team, das an seiner Entwicklung beteiligt ist; die Übernahme von JSON Agri durch weitere Hersteller und die Veröffentlichung der Fahrzeugschnittstelle sind die nächsten Schritte; Wirkungen auf Böden und auf den bäuerlichen Beruf brauchen Zeit, um sichtbar zu werden. Das ist die Lage eines entstehenden Commons. Wir veröffentlichen es, um die Implementierungen, Kompetenzen und Nutzungen zu sammeln, die es wachsen lassen.

Nichts hindert daran, schnell und gut zu innovieren; alles lädt dazu ein, es gemeinsam zu tun [18]. Alle können einen ersten Schritt tun, im eigenen Maßstab:

- **Landwirtinnen, Landwirte und Zusammenschlüsse**: eine instrumentierte Mission aufnehmen, Zugang zu den Missionsaufträgen und geleisteten Arbeiten auf den eigenen Parzellen verlangen, am Ende einer Mission sagen, was die Maschine nicht wissen kann;
- **Händler, Werkstätten, Integratoren**: eine Missionsdatei lesen lernen, einen Geräteanbau dokumentieren, einen Vorfall mit seiner Konfiguration melden, eine Nachbarin oder einen Nachbarn schulen;
- **Hersteller von Robotern und Geräten**: einen Leser für das Format implementieren, eine Schnittstelle veröffentlichen, auch eine bescheidene, mit ihren Grenzen;
- **Institute, Labore, Bildungseinrichtungen**: ein Protokoll durchführen, eine Berechnungskonvention prüfen, einen auf Beobachtungen gestützten Schwellenwert vorschlagen;
- **Genossenschaften, Gebietskörperschaften, öffentliche Geldgeber**: gemeinsame Infrastrukturen fördern (Versuchsflächen, Ausbildung, Dokumentation, Pflege der Standards), gleichrangig mit dem Kauf von Maschinen;
- **Entwicklungsgemeinschaften**: einen Baustein verbessern, einen Test schreiben, eine stabile Version pflegen, an der Governance mitwirken.

> **Technologie wird zu landwirtschaftlichem Fortschritt, wenn sie dauerhaft die Fähigkeit der Bäuerinnen und Bauern stärkt, zu verstehen, zu entscheiden und zu handeln.**  
> Die Robotik zu öffnen heißt, der landwirtschaftlichen Welt die Mittel zu geben, an ihrer Gestaltung mitzuwirken, ihre Nutzung zu beherrschen und ihr Wissen weiterzugeben.

**Dem Ökosystem beitreten**  
[github.com/Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops)

---

## Literatur

[1] Bechar, A., & Vigneault, C. (2016). Agricultural robots for field operations: Concepts and components. *Biosystems Engineering*, 149, 94–111. [https://doi.org/10.1016/j.biosystemseng.2016.06.014](https://doi.org/10.1016/j.biosystemseng.2016.06.014)

[2] Lowenberg-DeBoer, J., Huang, I. Y., Grigoriadis, V., & Blackmore, S. (2020). Economics of robots and automation in field crop production. *Precision Agriculture*, 21, 278–299. [https://doi.org/10.1007/s11119-019-09667-5](https://doi.org/10.1007/s11119-019-09667-5)

[3] Agreste. (2022). *Recensement agricole 2020 — Typologie des exploitations selon leur dimension économique* [Agrarstrukturerhebung 2020 — Betriebstypologie nach wirtschaftlicher Größe]. Französisches Landwirtschaftsministerium. [https://agreste.agriculture.gouv.fr/agreste-web/disaron/RA2020_001/detail/](https://agreste.agriculture.gouv.fr/agreste-web/disaron/RA2020_001/detail/)

[4] Wezel, A., Bellon, S., Doré, T., Francis, C., Vallod, D., & David, C. (2009). Agroecology as a science, a movement and a practice. A review. *Agronomy for Sustainable Development*, 29(4), 503–515. [https://doi.org/10.1051/agro/2009004](https://doi.org/10.1051/agro/2009004)

[5] Ditzler, L., & Driessen, C. (2022). Automating Agroecology: How to Design a Farming Robot Without a Monocultural Mindset? *Journal of Agricultural and Environmental Ethics*, 35, 2. [https://doi.org/10.1007/s10806-021-09876-x](https://doi.org/10.1007/s10806-021-09876-x)

[6] Daum, T. (2021). Farm robots: ecological utopia or dystopia? *Trends in Ecology & Evolution*, 36(9), 774–777. [https://doi.org/10.1016/j.tree.2021.06.002](https://doi.org/10.1016/j.tree.2021.06.002)

[7] Spykman, O., Lowenberg-DeBoer, J., & Gandorfer, M. (2026). Crop robots as potential enablers of economical and biodiversity-smart small-scale farming. *Precision Agriculture*. [https://doi.org/10.1007/s11119-026-10367-0](https://doi.org/10.1007/s11119-026-10367-0)

[8] ISO. (2015). *ISO 11783-10:2015 — Tractors and machinery for agriculture and forestry — Serial control and communications data network — Part 10: Task controller and management information system data interchange*. [https://www.iso.org/standard/61581.html](https://www.iso.org/standard/61581.html)

[9] AgGateway. (2025). *ADAPT Standard 2.0 — Documentation*. [https://adaptstandard.org/docs/](https://adaptstandard.org/docs/)

[10] Agricultural Industry Electronics Foundation (AEF). (o. J.). *Autonomy in Agriculture (AUT) — project team, use cases and work items*. [https://www.aef-online.org/aef-aut/](https://www.aef-online.org/aef-aut/)

[11] Felske, M., Redenius, J., Happich, G., & Schöning, J. (2026). Towards an Agricultural Operational Design Domain: A Framework. *Smart Agricultural Technology*. [https://doi.org/10.1016/j.atech.2026.102246](https://doi.org/10.1016/j.atech.2026.102246)

[12] Holm, S., Pedersen, S. M., & Tamirat, T. W. (2024). Robots in agriculture — A case-based discussion of ethical concerns on job loss, responsibility, and data control. *Smart Agricultural Technology*, 9, 100633. [https://doi.org/10.1016/j.atech.2024.100633](https://doi.org/10.1016/j.atech.2024.100633)

[13] Batey, T. (2009). Soil compaction and soil management — a review. *Soil Use and Management*, 25(4), 335–345. [https://doi.org/10.1111/j.1475-2743.2009.00236.x](https://doi.org/10.1111/j.1475-2743.2009.00236.x)

[14] Stilgoe, J., Owen, R., & Macnaghten, P. (2013). Developing a framework for responsible innovation. *Research Policy*, 42(9), 1568–1580. [https://doi.org/10.1016/j.respol.2013.05.008](https://doi.org/10.1016/j.respol.2013.05.008)

[15] Sustainable Robotics Base for Crops. (2026). *Agri JSON format, version 3 — schema, profiles, vocabularies, indicator registry and documentation*. Lizenz CC BY 4.0. [https://github.com/Sustainable-Robotics-Base-for-Crops/json_agri_format](https://github.com/Sustainable-Robotics-Base-for-Crops/json_agri_format)

[16] Europäisches Parlament & Rat der Europäischen Union. (2023). *Verordnung (EU) 2023/1230 vom 14. Juni 2023 über Maschinen*. [https://eur-lex.europa.eu/eli/reg/2023/1230/oj](https://eur-lex.europa.eu/eli/reg/2023/1230/oj)

[17] ISO. (2024). *ISO 18497, Teile 1 bis 4 — Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery*. [https://www.iso.org/standard/82684.html](https://www.iso.org/standard/82684.html)

[18] Prévault-Osmani, A. (2026). *Manifest für eine offene Agrarrobotik*. Sustainable Robotics Base for Crops. Lizenz CC BY 4.0. [https://github.com/Sustainable-Robotics-Base-for-Crops/ecosystem/blob/main/manifesto/MANIFESTO.de.md](https://github.com/Sustainable-Robotics-Base-for-Crops/ecosystem/blob/main/manifesto/MANIFESTO.de.md)

---

## Über den Autor

**Alexandre Prévault-Osmani**  
CTO und Mitgründer von SABI AGRI

Ingenieur von Beruf und Landwirt von seinem Werdegang her, arbeitet Alexandre Prévault-Osmani seit 2015 an der Schnittstelle von Elektrifizierung, Agrarrobotik, Open Source und Agrarökologie. Er wirkt an der Entwicklung des SRBC-Roboters mit, der in diesem Text als Fallstudie dient.

**Kontakt**

- GitHub: [Alexandre-PO](https://github.com/Alexandre-PO)
- LinkedIn: [alexandre-po](https://www.linkedin.com/in/alexandre-po)

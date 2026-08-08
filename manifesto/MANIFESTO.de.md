# Manifest für eine offene Agrarrobotik — Sustainable Robotics Base for Crops

Die Agrarrobotik braucht eine gemeinsame Basis, die offen, sparsam, sicher und dokumentiert ist und die Vielfalt der Praktiken respektieren kann. Das ist der Sinn von *Sustainable Robotics Base for Crops* (SRBC): eine produktive Softwaregrundlage für autonome Agrarroboter zu schaffen und zu teilen, damit der durch Technologie geschaffene Wert auch zu denen zurückkehrt, die sie lebendig machen — den Landwirtinnen und Landwirten — und eine gerechte, wartbare und dauerhafte Wertschöpfungskette speist.

**Wir bekräftigen, dass eine offene Agrarrobotik die Verbreitung agroökologischer Praktiken beschleunigen kann, indem sie die Diffusion aneignungsfähiger, wirksamer und sicherer Werkzeuge ermöglicht. Agronomische, ökologische, wirtschaftliche und soziale Leistung müssen klar messbar werden — und dürfen sich nicht länger gegenseitig ausschließen.**

Wir rufen Landwirtinnen und Landwirte, Entwicklerinnen und Entwickler, Hersteller, Werkstätten, Integratoren, Forschende, Genossenschaften und Bildungseinrichtungen auf, sich diesem Einsatz anzuschließen: eine Schnittstelle veröffentlichen, ein Format stabilisieren, Dokumentation schreiben, einen Versuch durchführen, eine Nachbarin oder einen Nachbarn schulen. Nichts hindert daran, schnell und gut zu innovieren; alles lädt dazu ein, es gemeinsam zu tun.

Technologie darf kein Hindernis sein. Sie muss eine Brücke zur Dauerhaftigkeit landwirtschaftlicher Systeme sein.

---

## Warum öffnen

Als wir 2015 das Projekt SABI AGRI keimen ließen, bestand das Ziel bereits darin, Agrartechnik im Dienst einer nachhaltigeren und souveräneren Landwirtschaft zu verbreiten. Unsere Erfahrung als Hersteller elektrischer Maschinen und Agrarroboter hat uns mit einer strukturellen Realität konfrontiert: Die Geschwindigkeit digitaler Zyklen und der geschlossene Charakter vieler Lösungen erzeugen eine unverhältnismäßige Abhängigkeit für die bäuerliche Welt.

Einerseits ist die Obsoleszenz von Hard- und Softwareträgern nicht im Einklang mit den langen Zeiträumen der Landwirtschaft. Andererseits schließen proprietäre Schnittstellen die Nutzerinnen und Nutzer in ein unausgewogenes Verhältnis zu ihren Lieferanten ein — die ihrerseits von den Technologien ihrer eigenen Lieferanten abhängen. Eine Maschine, die nicht mehr verstanden, gewartet oder angepasst werden kann, wird am Ende zur Belastung, selbst wenn sie anfangs leistungsfähig war.

Wir sind der Ansicht, dass jeder Betrieb von technologischen Fortschritten profitieren können muss, ohne in geschlossenen Formaten gefangen zu sein. Öffnen heißt, Reparatur, Anpassung und Wissensweitergabe im Rhythmus der Jahreszeiten und Territorien möglich zu machen.

## Für wen, und im Dienst wovon

Wir stellen das robotische Ökosystem SRBC in den Dienst kleiner und mittlerer Betriebe, insbesondere wenn sie diversifiziert und in agroökologischen Praktiken engagiert sind. Sie spielen eine wesentliche Rolle für das ökologische Gleichgewicht, die Produktionsvielfalt, die Dynamik der Territorien und den Erhalt kontextbezogenen Wissens. Zugleich sind diese Betriebe besonders den Arbeitskosten, der körperlichen Belastung und Investitionsbarrieren ausgesetzt.

Agroökologische Praktiken erfordern oft mehr Beobachtung, mehr Präzision und mehr Sorgfalt für Böden und lebendige Systeme. Robotik kann dazu beitragen, diese Praktiken wirtschaftlich zugänglich zu machen: nicht indem sie die bäuerliche Entscheidung ersetzt, sondern indem sie die Belastung verringert und Operationen ermöglicht, die Kulturen, Böden und Ökosystemen zugutekommen.

Nicht jede Robotik dient diesem Anspruch. Je nach Architektur und Geschäftsmodell kann sie die Konzentration der Produktionsmittel und die technologische Abhängigkeit verstärken. Es geht also nicht darum, Robotik aus Prinzip zu übernehmen, sondern zu klären, welchen landwirtschaftlichen Modellen sie dient, wer Zugang hat, wer sie versteht, wer ihre Nutzungen festlegt und wer den geschaffenen Wert aneignet.

## Was SRBC ist

*Sustainable Robotics Base for Crops* bezeichnet das öffentliche Ökosystem von Softwarebausteinen, die unter anderem für den SRBC-Roboter und allgemeiner für eine interoperable Agrarrobotik entwickelt werden.

Das ist keine Demonstration abseits der Praxis. **Ein wesentlicher Teil dieses Codes wird in der Produktion eingesetzt**: Navigation, Lokalisierung, Geofencing, Wahrnehmung, Simulation, Missionsformat und zugehörige Werkzeuge. Die Repositories werden unter der GitHub-Organisation [Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops) veröffentlicht.

Das SRBC-Ökosystem ist eine Menge versionierter Pakete und Werkzeuge — vorwiegend unter ROS 2 —, die gelesen, geprüft, wiederverwendet oder unabhängig ersetzt werden können. Offene Verträge (Missionsformat JSON Agri, Kommunikationsschnittstellen, Navigationsnachrichten) ermöglichen es Drittanbieter-Werkzeugen, Integratoren und Forschenden, Missionen zu erzeugen oder zu nutzen, ohne von den Geheimnissen eines einzelnen Herstellers abhängig zu sein.

Wir ziehen eine klare Grenze: **Die Öffnung betrifft zuerst die generischen Grundlagen und Schnittstellen**; die industrielle Integration sowie die maschinenspezifische Sicherheitskette bleiben in der Verantwortung des Herstellers. Ein Commons zu öffnen heißt nicht, Verantwortung zu verwässern. Es heißt, das für Interoperabilität, Wartung und kollektive Innovation notwendige Wissen teilbar zu machen.

## Eine proportionierte, modulare, offene und verantwortungsvolle Gestaltung

Damit Robotik der Agroökologie dient, müssen ihre Entwurfsentscheidungen kohärent sein.

Wir bevorzugen Maschinen, die ihren Nutzungen **proportioniert** sind: leistungsfähig genug, um einen echten Dienst zu erbringen, leicht und sparsam genug, um zugänglich, wartbar und mit der Pflege des Bodens vereinbar zu bleiben.

Wir bevorzugen **Modularität**: Träger, Geräte, Sensoren und Softwarefunktionen zu trennen, um zu reparieren, anzupassen, nachzurüsten und zu teilen, ohne bei jeder Weiterentwicklung alles neu aufzubauen.

Wir bevorzugen **Offenheit**: öffentliche Schnittstellen, Dokumentation, Tests, Versionierung und Lizenzen, die Studium, Nutzung, Änderung und Weiterverteilung erlauben. Open Source ist kein Selbstzweck. Es ist eine industrielle Methode, um Grundlagen zu bündeln und Nutzungssouveränität auf Dauer zu bewahren.

Wir bevorzugen schließlich eine **verantwortungsvolle** Innovation: soziale und ökologische Wirkungen vorwegnehmen, Nutzerinnen und Nutzer einbeziehen, Einsatzgrenzen dokumentieren, landwirtschaftliche Daten behutsam steuern und eine klare industrielle Verantwortung für jede in Betrieb genommene Maschine aufrechterhalten.

Diese Prinzipien sind kein Label. Sie sind eine Anforderung an Kohärenz: Eine Technologie ist nur dann nützlich, wenn sie dauerhaft die Fähigkeit der Landwirtinnen und Landwirte stärkt zu verstehen, zu entscheiden und zu handeln.

## Was Offenheit verändert — und was nicht

In einem fragmentierten Sektor wird zu viel Energie darauf verwendet, dieselben Grundlagen erneut zu implementieren. Diese Bausteine zu teilen zerstört die industrielle Tätigkeit nicht: **sie verlagert sie**.

Für Landwirtinnen und Landwirte geht es um Nutzungssouveränität: diagnostizieren, reparieren, weiterentwickeln, einen Dienstleister wählen und den Datenzugang behalten. Für Hersteller verlagert sich die Differenzierung auf Integration, Robustheit, nachgewiesene Sicherheit und Service. Für Werkstätten und Integratoren machen dokumentierte Schnittstellen lokale Kompetenz und territoriale Reichweite möglich. Für Forschung und Lehre ermöglichen offene Formate endlich Vergleich, Lehre und Weitergabe.

Ein technologisches Commons braucht Dokumentation, Wartung und Governance. Offenheit ist nur dann nachhaltig, wenn wirtschaftliche Modelle — Maschinen, Werkzeuge, Dienstleistungen, Ausbildung — Unternehmen ermöglichen zu leben, ohne Gefangenschaft auf andere Weise neu zu erzeugen.

Selbst bei offenem Softwarecode bleiben Sicherheit, Konformität und Verantwortung an jede in Betrieb genommene Konfiguration gebunden. Eine autonome Funktion hat nur in einem expliziten Einsatzbereich Sinn, mit vorhersehbarem Verhalten außerhalb dieses Bereichs und mit Nachweisen eines sicheren Halts. Wir lehnen die naive Gegenüberstellung von Offenheit und Industrialisierung ab: Industrialisieren heißt auch, Qualität, Wartung, Interoperabilität und Sicherheit reproduzierbar zu machen.

## Aufruf

Die Verbreitung einer Agrarrobotik im Dienst der Agroökologie entsteht mit und bei den Nutzerinnen und Nutzern, gemeinsam mit Herstellern und technischen Gemeinschaften.

Jede und jeder kann nach den eigenen Kompetenzen beitragen: eine Schnittstelle veröffentlichen, ein Verfahren dokumentieren, ein kompatibles Werkzeug vorschlagen, einen Baustein verbessern, ein Experiment aufnehmen, eine Nachbarin oder einen Nachbarn schulen, Nutzungserfahrungen samt ihrer Grenzen teilen.

**Die Agrarrobotik zu öffnen heißt, zu verweigern, dass sie zu einem Instrument der Abhängigkeit wird. Es heißt, der Landwirtschaft die Mittel zu geben, an ihrer Gestaltung teilzunehmen, ihre Nutzungen zu beherrschen und ihr Wissen weiterzugeben.**

Treten Sie dem Ökosystem bei: [github.com/Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops)

---

*Dieses Manifest bringt den Geist des SRBC-Ökosystems zum Ausdruck. Eine ausführlichere Entwurfsdoktrin sowie die zugehörigen Bewertungs- und Diffusionsmethoden werden später veröffentlicht.*

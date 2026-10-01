# SMOR : vers un standard diffusable de la robotique agricole au service de l’agroécologie

### Sustainable Robotics Base for Crops

Auteur : Alexandre Prévault-Osmani — CTO et cofondateur de SABI AGRI

*Livre blanc · version courte · septembre 2026 · licence CC BY 4.0*

---

## Sommaire

1. [Résumé](#résumé)
2. [Repères](#repères)
3. [Thèse et positionnement](#thèse-et-positionnement)
4. [Ce qui freine la diffusion](#ce-qui-freine-la-diffusion)
5. [La vision SMOR](#la-vision-smor)
6. [Une architecture de référence et une chaîne de preuve ouverte](#une-architecture-de-référence-et-une-chaîne-de-preuve-ouverte)
7. [Le robot SRBC, une première incarnation](#le-robot-srbc-une-première-incarnation)
8. [Évaluer ce qui compte pour la ferme](#évaluer-ce-qui-compte-pour-la-ferme)
9. [Un commun qui appartient au monde paysan](#un-commun-qui-appartient-au-monde-paysan)
10. [Sûreté, conformité et co-responsabilité](#sûreté-conformité-et-co-responsabilité)
11. [Du code au commun : la feuille de route](#du-code-au-commun--la-feuille-de-route)
12. [Limites et appel](#limites-et-appel)
13. [Références](#références)
14. [À propos de l’auteur](#à-propos-de-lauteur)

---

## Résumé

La robotique agricole promet de réduire la pénibilité, de répondre aux difficultés de recrutement et de rendre possibles des interventions plus précises. Dix ans après l’arrivée des premiers robots dans les champs, sa diffusion reste pourtant confidentielle. La réussite d’une démonstration renseigne peu sur la disponibilité d’une machine pendant une saison, sur la qualité agronomique de son travail ou sur sa viabilité dans le quotidien d’une ferme. L’enjeu se déplace : faire fonctionner un robot compte désormais moins que créer les conditions de son adoption durable.

Nous soutenons que la robotique doit bénéficier en priorité aux petites et moyennes exploitations diversifiées engagées dans une transition agroécologique. Nous proposons pour cela la vision SMOR — *Small, Modular, Open & Responsible* — traduite en une architecture de référence, une chaîne documentaire ouverte qui relie ce que le robot devait faire à ce qu’il a réellement fait, une méthode d’évaluation, un modèle de commun appartenant au monde paysan et une répartition explicite des responsabilités. Le robot SRBC en constitue une première incarnation industrielle. SMOR est un cadre à mettre à l’épreuve : ce texte en expose la thèse et les propositions, la version complète en apportera les preuves.

---

## Repères

- **ODD** (domaine de conception opérationnelle) : conditions dans lesquelles une fonction autonome a été conçue et validée — parcelle, sol, météo, pente, qualité de localisation, présence de personnes.
- **Ordre de mission** : fichier qui décrit ce que le robot doit faire, dans quelles limites et avec quelles réactions autorisées.
- **Travail réalisé** : fichier qui décrit ce que le robot a fait, dans quelles conditions rencontrées, et comment la ferme apprécie le service rendu.
- **Open Core** : modèle où les interfaces et les briques génériques sont ouvertes, tandis que la réalisation matérielle, la calibration et les services restent sous la responsabilité du constructeur.

---

## Thèse et positionnement

Depuis le milieu des années 2010, la robotique agricole a quitté les laboratoires pour les champs. Les progrès en perception, en navigation et en automatisation sont réels ; la diffusion commerciale reste modeste au regard de la diversité des productions et du nombre d’exploitations [1, 2]. Cet écart appelle une autre définition de la maturité.

Notre approche est simple : la maturité d’un robot agricole se mesure à sa **diffusabilité**, c’est-à-dire à sa capacité à être utilisé, maintenu, réparé et amélioré dans le temps long de l’agriculture. Elle suppose une adéquation à un besoin agronomique et humain clairement identifié, un coût accessible, une sûreté démontrée dans un domaine explicite, une maintenance possible à proximité et une appropriation réelle par les personnes qui l’utilisent.

Nous faisons un choix de positionnement explicite : la robotique agricole doit bénéficier en priorité aux petites et moyennes exploitations, en particulier lorsqu’elles sont diversifiées et engagées dans une transition agroécologique. Nous les définissons d’abord comme des entreprises agricoles à taille humaine, où la personne qui cultive conserve une capacité directe d’observation et de décision sur ses cultures et ses sols ; la classification du recensement agricole par production brute standard en fournit un repère statistique [3]. Ces fermes portent la diversité des productions, l’entretien des territoires, l’emploi rural et des savoir-faire contextualisés. Elles sont aussi les plus exposées au coût du travail, à la pénibilité et aux barrières d’investissement.

Les pratiques agroécologiques demandent davantage d’observation, de précision et d’interventions différenciées [4]. Cette intensité agronomique devient difficile à tenir lorsque le travail humain est compté comme un simple coût face aux économies d’échelle. La robotique peut rééquilibrer cette situation en réduisant la pénibilité et en rendant réalisables des opérations favorables aux sols et aux écosystèmes : un semis précis qui prépare un désherbage mécanique précoce, des passages répétés d’un outil léger dans une fenêtre courte, une machine légère là où la portance du sol l’exige.

La même technologie peut aussi servir la concentration des moyens de production, la dépendance envers des fournisseurs propriétaires et l’obsolescence rapide des équipements [5, 6]. La trajectoire dépend des choix d’architecture, de modèle économique et de gouvernance. Le décalage entre les cycles courts du numérique et les temps longs de l’agriculture en fait un enjeu structurel : une machine que l’on cesse de pouvoir comprendre, entretenir ou adapter devient une contrainte, même lorsqu’elle était performante au départ.

Nous distinguons trois niveaux : la **capacité technique** du robot (se déplacer, suivre un rang, commander un outil en sécurité), le **service agronomique** obtenu dans une fenêtre donnée (un semis régulier, un binage efficace) et l’**impact agroécologique**, qui s’observe sur la durée à l’échelle du système de culture (intrants évités, état du sol, biodiversité, conditions de travail, autonomie de la ferme, coût complet). Les dispositifs d’évaluation existants documentent surtout le premier niveau ; ce sont les deux suivants qui décident de l’intérêt d’un robot pour une ferme.

> **Thèse**  
> La robotique agricole deviendra un levier de diffusion de l’agroécologie à condition d’être conçue pour être utile, accessible, maintenable, sûre, interopérable et appropriable, et de pouvoir démontrer ses performances dans des conditions réelles.

Nous y ajoutons une conviction de méthode : la diffusion est autant un problème de **représentation** que de mesure. Tant que l’intention agronomique et le résultat obtenu restent décrits dans des vocabulaires différents, les retours de terrain restent isolés, les résultats de deux constructeurs restent incomparables et les responsabilités restent impossibles à examiner. Un vocabulaire commun et versionné est la condition première d’une connaissance cumulative.

---

## Ce qui freine la diffusion

Un robot agricole travaille au contact du vivant : sol, végétation, météo et organisation du travail varient au cours d’une même saison. Toute performance doit donc être rapportée à un usage, à une configuration et à un domaine de fonctionnement explicite.

Les verrous sont connus et interdépendants [1, 7] : la **robustesse** sur une saison entière ; la **sûreté**, qui impose de détecter les situations dangereuses et de rejoindre un état sûr ; la **performance agronomique**, qui se juge à la qualité du travail de l’outil davantage qu’à la précision de la trajectoire ; la **viabilité économique**, qui dépend du temps de supervision, de la maintenance et des immobilisations bien plus que du prix d’achat ; l’**interopérabilité**, faible tant que formats, interfaces et journaux restent propres à chaque constructeur, et la **dépendance technologique** qui en découle. Les travaux récents montrent que le temps humain de logistique et de supervision est le véritable sujet à résoudre pour la robotique à petite échelle [7].

L’agriculture de précision dispose déjà de standards précieux, comme ISOXML ou ADAPT, pour décrire une tâche et le travail appliqué [8, 9]. Ils ont été conçus pour une personne aux commandes, garante du domaine d’emploi. Avec un robot, une partie de l’observation et de la décision passe à la machine, et la chaîne qui relie l’intention à l’exécution doit devenir explicite : ce que le robot doit faire, dans quelles conditions il y est autorisé, comment il réagit à un imprévu, ce qu’il a rencontré et ce qu’il a réalisé. L’industrie reconnaît ce besoin, avec le chantier de l’AEF consacré aux machines autonomes [10], tout comme la recherche sur le domaine de fonctionnement agricole [11]. Nous considérons ces travaux comme convergents et souhaitons y contribuer avec une proposition ouverte, déjà utilisée sur le terrain.

La littérature qui interroge la robotique du point de vue de l’agroécologie converge sur un point : la trajectoire reste ouverte. La même technologie peut conduire à des flottes de petites machines au service de systèmes diversifiés ou à de grandes machines consolidant des monocultures [6]. Apporter des fonctionnalités autonomes dans des systèmes agroécologiques suppose de concevoir avec une diversité de parties prenantes, en s’affranchissant d’un « esprit monocultural » [5], et les agriculteur·ices placent la responsabilité, la sûreté et la maîtrise des données parmi leurs premières préoccupations [12]. Ces conclusions fondent notre choix de confier aux paysan·nes la décision et la garantie des usages de la technologie qu’ils et elles utilisent.

---

## La vision SMOR

SMOR est un cadre de conception et d’évaluation qui relie les caractéristiques d’un robot à ses effets agronomiques, économiques, écologiques et sociaux. À ce stade, il a le statut d’une proposition soumise à l’épreuve du terrain et de la discussion.

Nous faisons le choix d’une traction et d’effecteurs principalement électriques. Moteurs et vérins électriques se commandent finement, renvoient leur état et s’intègrent directement aux systèmes de diagnostic. L’électricité peut venir du réseau ou être produite sur la ferme, ce qui ouvre la voie à une autonomie énergétique totale ou partielle ; batteries et moteurs doivent pour autant être évalués sur leur cycle de vie.

**Small : une échelle proportionnée.** Nous privilégions des machines dont la masse, la puissance et le gabarit restent proportionnés aux opérations. Notre cible dimensionnelle se situe entre l’humain et le cheval de trait : d’environ 80 à 1 200 kg, moins de 10 km/h, quelques kilowatts, une autonomie d’une demi-journée à une journée, une très basse tension et, pour les porteurs légers, un investissement inférieur à 40 000 euros. Au-delà, la masse ramène la machine dans le monde du tracteur, avec sa motorisation, sa logistique et son prix. Ces valeurs sont des cibles de conception. Une masse limitée réduit l’énergie en jeu et facilite le transport et la maintenance ; l’effet sur le sol dépend aussi de la pression de contact, du glissement, du nombre de passages et de l’humidité [13]. Cette échelle permet plusieurs robots spécialisés, ou partagés entre fermes, plutôt qu’une machine unique dimensionnée pour l’opération la plus lourde. Elle devient un avantage économique durable lorsque le temps humain par hectare baisse effectivement, ce qui suppose des missions fiables sans surveillance continue et, à terme, la supervision de plusieurs robots par une seule personne.

**Modular : adapter, réparer, mutualiser.** Nous séparons un socle stable (structure, énergie, commande, interfaces, sûreté) de modules adaptés aux cultures, aux outils et aux contextes : changer d’outil, de train roulant ou de capteur sans remplacer le porteur, faire évoluer une fonction logicielle sans reconstruire l’ensemble, rétrofiter une machine en respectant le calendrier cultural. Cette modularité repose sur des dimensions, des connectiques, des protocoles et des formats documentés ; sans eux, elle resterait à la merci du fournisseur initial.

**Open : la souveraineté dans la durée.** Nous ouvrons en priorité les interfaces, les formats de mission et de données, la documentation et les briques logicielles génériques, puis les plans lorsque leur publication renforce la réparabilité. L’Open Source que nous défendons est une méthode industrielle : licences explicites, contrats versionnés, tests, documentation, gouvernance et versions stables. Il garantit aux fermes la souveraineté d’usage (diagnostiquer, réparer, adapter, faire maintenir par un autre prestataire), déplace la différenciation des fabricants vers l’intégration, la sûreté et le service, et rend possible une compétence durable dans les ateliers des territoires.

**Responsible : une innovation redevable.** Une technologie devient responsable lorsque ses effets sont anticipés, discutés, mesurés et corrigés avec les personnes qu’elle concerne [14]. Ce principe engage à associer les agriculteur·ices aux besoins et à l’évaluation, à concevoir la sûreté dès l’origine, à documenter les limites d’emploi, à mesurer les consommations de matière, d’énergie et de ressources numériques, à préserver la décision paysanne, à garantir la maîtrise des données par la ferme et à rendre vérifiable la répartition des responsabilités.

Ces quatre principes forment un tout. Un petit robot fermé reste captif et vieillit vite ; une plateforme ouverte sans gouvernance se fragmente ; une machine modulaire trop chère reste sans effet sur la diffusion. **SMOR propose une cohérence d’ensemble : une robotique dont la performance se mesure à sa capacité à rendre l’agroécologie praticable, économiquement viable et durablement appropriable par le monde paysan.**

---

## Une architecture de référence et une chaîne de preuve ouverte

Une architecture de référence donne un langage commun : elle sépare les fonctions et définit les interfaces qui permettent de remplacer un composant sans reconstruire le système. Chaque constructeur reste libre de ses choix matériels, dès lors qu’il respecte les contrats communs et les exigences de sûreté. Nous proposons six couches : énergie et actionneurs, commande du véhicule, bus de terrain documentés, calcul embarqué (ROS 2 en constitue aujourd’hui un socle pertinent), perception et localisation, mission et interface utilisateur. Un principe les traverse : **les fonctions qui engagent la sûreté restent indépendantes du calculateur généraliste et de toute connexion distante.** Les fonctions essentielles restent disponibles hors connexion et l’interface rend visibles l’état du robot, ses limites et la cause de chaque arrêt.

Le contrat le plus structurant est l’**interface véhicule**, qui décrit commandes, états, capacités des outils et défauts. Elle permet à une même fonction de navigation de s’adapter à plusieurs porteurs, et transforme ainsi un produit en plateforme.

Le second contrat porte sur la mission. Nous proposons **JSON Agri**, un format ouvert publié sous licence CC BY 4.0 [15], lisible sans formation informatique et vérifiable par une machine. Il organise une chaîne en deux documents. L’**ordre de mission** décrit l’objectif agronomique et ses critères d’acceptation, le couple porteur–outil, le domaine de fonctionnement autorisé, la trajectoire, les zones permises et les réactions prévues face aux événements : une batterie faible, par exemple, déclenche un retour vers la zone de charge par des chemins autorisés. Le **travail réalisé** relie cette intention aux conditions rencontrées, aux événements, aux interventions humaines, aux indicateurs du service rendu et à l’appréciation agronomique de la ferme. Une empreinte numérique de l’ordre, recopiée dans le travail réalisé, garantit que l’on compare l’exécution à la version exacte de la mission.

Trois choix donnent à cette chaîne sa portée. Le domaine autorisé et les conditions rencontrées partagent le même vocabulaire, de sorte que tout écart puisse être relié à une détection, une décision, une responsabilité et une preuve. Les réactions aux événements forment un vocabulaire fermé : la machine refuse toute instruction inconnue ou absente du catalogue validé par son constructeur, et son plancher de sûreté reste hors de portée de tout fichier. L’attestation produite en simulation prouve qu’un fichier a passé des vérifications définies, sous des hypothèses identifiées ; elle a valeur de preuve de vérification, distincte d’un certificat.

La chaîne sépare ainsi trois validations : la **préparation**, dans l’éditeur de mission ; la validation **opérationnelle**, à bord, où le robot confronte la mission à sa configuration et aux conditions confirmées sur place, et garde la liberté de refuser ; la validation du **service**, après la mission, par l’appréciation agronomique de la ferme. Cette séparation protège de deux confusions coûteuses : prendre une simulation pour une autorisation, ou une mission achevée pour un service réussi. Des règles de spécification publiques (noyau petit et stable, donnée absente déclarée comme telle, compatibilité garantie, validation hors ligne), des niveaux de conformité et un validateur permettent à tout tiers de vérifier son implémentation en autonomie. JSON Agri complète ainsi les standards existants en décrivant la chaîne d’autonomie qu’ils laissent implicite.

---

## Le robot SRBC, une première incarnation

Le robot SRBC, conçu par SABI AGRI, éprouve ces principes sur une machine commercialisée et utilisée sur le terrain. Ce porteur électrique compact, sur roues ou sur chenilles, pèse de l’ordre de 250 kg en configuration chenillée, dans la partie basse de l’enveloppe SMOR. Il reçoit des outils de préparation légère du sol, de semis, d’entretien des cultures et de transport. Sa chaîne de sûreté matérielle fonctionne indépendamment du calculateur, et les fonctions de protection de haut niveau (géorepérage, vision de sécurité) imposent leur commande à la navigation par un arbitrage de priorité. **La personne formée qui opère le robot définit et respecte le domaine d’usage ; le logiciel de haut niveau contribue à éviter l’incident ; la commande bas niveau garantit le retour vers un état sûr.**

La navigation, la localisation, le géorepérage, la perception de sécurité, la simulation, le format JSON Agri et les éditeurs de mission sont publiés sur l’organisation GitHub [Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops), sous licence Apache 2.0 pour le code et CC BY 4.0 pour les spécifications. Le robot qui travaille en parcelle exécute ce code public. L’automate, le pilote du véhicule, les contrats de commande, les calibrations et les services distants restent sous la responsabilité du constructeur : SRBC est un **Open Core industriel**, et nous décrivons son ouverture telle qu’elle est.

Toute organisation extérieure peut ainsi faire rouler un robot simulé de bout en bout, préparer et valider une mission, observer un robot réel par une interface publiée, vérifier la conformité de ses fichiers et réutiliser chaque brique de navigation. Les prochaines étapes d’ouverture permettront de commander le robot, de porter la pile logicielle sur d’autres véhicules et d’assembler une machine à partir du code public.

---

## Évaluer ce qui compte pour la ferme

Une démonstration isolée produit un exemple ; un protocole documenté, répété et comparable produit une preuve. Notre méthode relie chaque résultat à une opération agronomique, à une situation de référence (travail manuel, tracteur, pratique antérieure), à un domaine de fonctionnement, à une configuration et à un catalogue d’indicateurs versionné, fixés avant l’essai. Portée par la chaîne ordre de mission – travail réalisé, cette relation permet à un tiers de recalculer ce que nous publions. Les indicateurs couvrent le service agronomique, la disponibilité, l’énergie, la sûreté, le temps humain, le coût complet et les effets sur le sol ; ils sont publiés avec leur convention de calcul, leur dispersion et leur couverture. Une valeur manquante est déclarée comme telle : l’absence est une information.

La machine sait mesurer ses durées, sa trajectoire, son énergie et la qualité de sa localisation. Les grandeurs qui décident du bénéfice pour la ferme dépendent souvent d’une personne : conditions réellement rencontrées, satisfaction agronomique, temps de supervision, besoin d’un second passage. Nous proposons de les recueillir à trois moments, là où la personne se trouve : à la préparation, au chargement sur le robot et en fin de mission, avec un outil qui préremplit ce qui peut l’être et pose peu de questions. De même, une grandeur mesurée devient un critère lorsque quelqu’un en fixe le seuil dans l’ordre de mission et que la machine sait comment réagir à son franchissement.

Nos premières campagnes instrumentées confirment la faisabilité de cette chaîne entre robots, fermes et outils différents. La base de preuves progressera avec ses réussites comme avec ses échecs, pour établir où, quand et à quelles conditions la robotique apporte un bénéfice agroécologique réel.

---

## Un commun qui appartient au monde paysan

Nous soutenons que l’écosystème logiciel de la robotique agricole — formats de fichiers, code de suivi de trajectoire, algorithmes de décision, outils de mission et de traçabilité — doit devenir un **commun qui appartienne au monde paysan et dont le monde paysan se saisisse**.

Ce commun est d’abord un vocabulaire. Une ferme décrit son attente en termes agronomiques, un distributeur en termes de service, un fabricant en termes de fonctions. Le rôle premier du commun est de permettre à ces parties prenantes de **décrire, échanger et contester des faits** dans les mêmes termes. Le code ouvert rend ce vocabulaire utilisable et prouve en production qu’il fonctionne ; le vocabulaire rend le code substituable, et donc le commun gouvernable. Un format que plusieurs implémentations savent lire échappe à toute confiscation, y compris par l’entreprise qui l’a lancé.

Par monde paysan, nous entendons les paysan·nes et les ateliers, distributeurs, coopératives, instituts et fabricants qui travaillent à leur service. Cette appartenance se construit par cinq propriétés vérifiables :

- **il reste ouvert** : les licences garantissent un usage libre dans la durée, et la marque protège le sens des mots ;
- **il survit à l’entreprise qui l’a lancé** : dépôts publics, historique et documentation permettent de le reprendre ; à terme, sa propriété sera confiée à une structure sans but lucratif, distincte de tout fabricant, dont les paysan·nes et leurs organisations seront membres de droit ;
- **il se gouverne avec les personnes qu’il sert** : les paysan·nes siègent dans les décisions qui touchent sa finalité et disposent d’un droit de contestation ;
- **il rend les données à la ferme** : le travail réalisé appartient à l’exploitation, qui peut le lire, le conserver, le transmettre ou le garder pour elle sans passer par un fournisseur [12] ;
- **il s’apprend** : outils lisibles, formations entre pairs et ateliers locaux l’inscrivent dans la tradition de l’éducation populaire technique.

Les composantes d’un robot appellent des degrés d’ouverture différents. Les **contrats communs** (formats, indicateurs, interfaces, critères de conformité) s’ouvrent en priorité ; les **briques génériques** (navigation, simulation, diagnostic, éditeurs) se développent comme des communs logiciels ; l’**intégration industrielle** et la chaîne de sûreté relèvent du fabricant ; les **services et données sensibles** gardent un accès contrôlé. La règle qui rend un Open Core défendable tient en une phrase : **on ouvre les contrats et la logique générique ; on garde la réalisation matérielle, la calibration et les services de flotte.** L’avantage d’un constructeur réside dans sa machine, sa chaîne de sûreté, son réseau de service et sa capacité à tenir ses engagements dans la durée.

L’ouverture déplace la valeur et les coûts. Elle réduit la réimplémentation des mêmes fondations et crée des besoins de maintenance et de gouvernance qu’il faut financer. Vente et location de machines, adaptation locale, contrats de service, versions maintenues, formation, accompagnement à la conformité font vivre les entreprises, à condition de s’interdire la captivité par des données retenues, des abonnements indispensables au fonctionnement de base ou des interfaces fermées artificiellement. Nous appliquons Apache 2.0 au code et CC BY 4.0 aux spécifications et aux textes ; la question d’une réciprocité pour certains actifs sera tranchée collectivement.

La gouvernance suit l’usage. Les décisions relatives au format sont aujourd’hui consignées publiquement, et une procédure écrite permet de les contester. Plusieurs paliers, déclenchés par des faits observables, organisent la suite, en commençant par un comité des versions dès la première implémentation tierce, puis un collège des usages doté d’un droit de contestation dès qu’un collectif d’agriculteur·ices, une coopérative ou un distributeur dépend du format. Le dernier palier transfère la propriété du format et de la marque à la structure sans but lucratif décrite plus haut ; il rend le commun indépendant de l’entreprise qui l’a lancé, et nous le tenons pour une condition de crédibilité de l’ensemble.

---

## Sûreté, conformité et co-responsabilité

La conformité d’une machine autonome structure sa conception, ses essais et son suivi pendant toute sa durée de vie. La directive Machines 2006/42/CE s’applique jusqu’au 19 janvier 2027, puis le règlement (UE) 2023/1230 prend le relais [16] ; la série ISO 18497:2024 traite des machines agricoles autonomes [17]. L’ouverture du code facilite l’audit, la traçabilité et la maintenance. La sûreté et la conformité, elles, restent attachées à chaque machine mise sur le marché ou en service, à son analyse des risques, à ses essais et à sa configuration validée. Une réparation qui préserve la conformité reste une réparation, et l’ouverture doit précisément la faciliter ; une modification qui crée un danger nouveau engage la personne ou l’entité qui la réalise. Les équipes qui maintiennent le commun répondent de la qualité des contributions ; la validation de l’intégration revient à l’entité qui met la machine en service.

Nous proposons de compléter cette répartition réglementaire par une **co-responsabilité opérationnelle**, qui précise pour chaque étape qui décide, qui valide et quelle preuve est conservée.

| Étape | Décide | Valide | Preuve conservée |
|---|---|---|---|
| Choix agronomique et fenêtre de travail | Paysan·ne | Paysan·ne | intention et critères dans l’ordre de mission |
| Carte de la parcelle et obstacles connus | Paysan·ne | Paysan·ne | carte de parcelle référencée |
| Domaine autorisé et réactions aux événements | Paysan·ne ou opérateur·ice | Plancher de sûreté du fabricant | domaine et stratégies de l’ordre |
| Montage de l’outil et vérification avant départ | Opérateur·ice | Opérateur·ice | configuration prévue et utilisée |
| Exécution | Machine, libre de refuser | Limites du fabricant, arrêt d’urgence | événements, actions demandées et appliquées |
| Appréciation du service rendu | Paysan·ne | Paysan·ne | appréciation consignée dans le travail réalisé |

Une case sans titulaire est un résultat : elle signale un manque à traiter. Une responsabilité comprise différemment par deux parties est également un résultat, à discuter ouvertement. Cette co-responsabilité organise la coopération au quotidien et laisse entière la responsabilité réglementaire du fabricant ou de l’intégrateur. **L’enjeu est de rendre les connaissances partageables tout en maintenant une responsabilité explicite sur chaque machine mise en service.**

---

## Du code au commun : la feuille de route

La diffusion de SMOR se mesurera à la capacité d’organisations extérieures à comprendre les interfaces, reproduire un essai, adapter une brique, lire un travail réalisé et maintenir une machine en autonomie vis-à-vis de son concepteur. Nous avançons en quatre niveaux : **rendre visible** ce qui existe, avec son statut et ses limites ; **rendre reproductible** l’installation et la simulation d’une mission ; **rendre interopérable** en publiant les contrats et les tests ; **rendre diffusable** en construisant les preuves, les compétences et les services de terrain.

Cinq volets en découlent : consolider le socle ouvert ; publier les contrats de commande et l’interface véhicule, puis obtenir une seconde implémentation du format par une organisation extérieure, condition pour parler de standard ; construire une base de preuves relue par un institut indépendant, avec coût complet et temps humain mesurés sur plusieurs campagnes ; organiser la sûreté de chaque configuration commercialisée ; développer les compétences territoriales, pour que les fermes, les ateliers et les distributeurs sachent diagnostiquer, réparer et former à leur tour, car on gouverne ce que l’on comprend. Le déploiement progresse par cercles, de l’usage interne aux partenaires de confiance, puis aux intégrations tierces et à la diffusion élargie, chaque passage dépendant de critères observables. Le nombre de téléchargements signale un intérêt ; la diffusion agricole se prouve sur le terrain.

---

## Limites et appel

Ce texte propose un cadre conceptuel et technique ; la démonstration de ses bénéfices agronomiques et économiques demande des campagnes répétées et des suivis pluriannuels, que la version complète documentera. Nous en connaissons les limites : l’enveloppe SMOR est une cible de conception ; SRBC constitue un premier cas d’étude, porté par une équipe engagée dans son développement ; l’adoption de JSON Agri par d’autres constructeurs et la publication de l’interface véhicule constituent les prochaines étapes ; les effets sur les sols et le métier paysan demandent du temps pour être observés. C’est la situation d’un commun naissant. Nous la publions pour rallier les implémentations, les compétences et les usages qui lui permettront de grandir.

Rien n’empêche d’innover vite et bien ; tout invite à le faire ensemble [18]. Chacun et chacune peut faire un premier pas, à sa mesure :

- **agriculteur·ices et collectifs** : accueillir une mission instrumentée, exiger l’accès aux ordres de mission et aux travaux réalisés sur ses parcelles, dire en fin de mission ce que la machine ignore ;
- **distributeurs, ateliers, intégrateurs** : apprendre à lire un fichier de mission, documenter un montage d’outil, remonter un incident avec sa configuration, former un voisin ou une voisine ;
- **fabricants de robots et d’outils** : implémenter un lecteur du format, publier une interface, même modeste, avec ses limites ;
- **instituts, laboratoires, établissements d’enseignement** : exécuter un protocole, auditer une convention de calcul, proposer un seuil fondé sur des observations ;
- **coopératives, collectivités, financeurs publics** : soutenir les infrastructures communes (sites d’essai, formation, documentation, maintenance des standards) au même titre que l’achat de machines ;
- **communautés de développement** : améliorer une brique, écrire un test, maintenir une version stable, participer à la gouvernance.

> **La technologie devient un progrès agricole lorsqu’elle augmente durablement la capacité des paysan·nes à comprendre, décider et agir.**  
> Ouvrir la robotique, c’est donner au monde agricole les moyens de participer à sa conception, d’en maîtriser les usages et d’en transmettre les connaissances.

**Rejoindre l’écosystème**  
[github.com/Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops)

---

## Références

[1] Bechar, A., & Vigneault, C. (2016). Agricultural robots for field operations: Concepts and components. *Biosystems Engineering*, 149, 94–111. [https://doi.org/10.1016/j.biosystemseng.2016.06.014](https://doi.org/10.1016/j.biosystemseng.2016.06.014)

[2] Lowenberg-DeBoer, J., Huang, I. Y., Grigoriadis, V., & Blackmore, S. (2020). Economics of robots and automation in field crop production. *Precision Agriculture*, 21, 278–299. [https://doi.org/10.1007/s11119-019-09667-5](https://doi.org/10.1007/s11119-019-09667-5)

[3] Agreste. (2022). *Recensement agricole 2020 — Typologie des exploitations selon leur dimension économique*. Ministère de l’Agriculture et de la Souveraineté alimentaire. [https://agreste.agriculture.gouv.fr/agreste-web/disaron/RA2020_001/detail/](https://agreste.agriculture.gouv.fr/agreste-web/disaron/RA2020_001/detail/)

[4] Wezel, A., Bellon, S., Doré, T., Francis, C., Vallod, D., & David, C. (2009). Agroecology as a science, a movement and a practice. A review. *Agronomy for Sustainable Development*, 29(4), 503–515. [https://doi.org/10.1051/agro/2009004](https://doi.org/10.1051/agro/2009004)

[5] Ditzler, L., & Driessen, C. (2022). Automating Agroecology: How to Design a Farming Robot Without a Monocultural Mindset? *Journal of Agricultural and Environmental Ethics*, 35, 2. [https://doi.org/10.1007/s10806-021-09876-x](https://doi.org/10.1007/s10806-021-09876-x)

[6] Daum, T. (2021). Farm robots: ecological utopia or dystopia? *Trends in Ecology & Evolution*, 36(9), 774–777. [https://doi.org/10.1016/j.tree.2021.06.002](https://doi.org/10.1016/j.tree.2021.06.002)

[7] Spykman, O., Lowenberg-DeBoer, J., & Gandorfer, M. (2026). Crop robots as potential enablers of economical and biodiversity-smart small-scale farming. *Precision Agriculture*. [https://doi.org/10.1007/s11119-026-10367-0](https://doi.org/10.1007/s11119-026-10367-0)

[8] ISO. (2015). *ISO 11783-10:2015 — Tracteurs et matériels agricoles et forestiers — Réseaux de commande et de communication de données en série — Partie 10 : Échange de données entre le contrôleur de tâches et le système d’information de gestion*. [https://www.iso.org/standard/61581.html](https://www.iso.org/standard/61581.html)

[9] AgGateway. (2025). *ADAPT Standard 2.0 — Documentation*. [https://adaptstandard.org/docs/](https://adaptstandard.org/docs/)

[10] Agricultural Industry Electronics Foundation (AEF). (s. d.). *Autonomy in Agriculture (AUT) — project team, use cases and work items*. [https://www.aef-online.org/aef-aut/](https://www.aef-online.org/aef-aut/)

[11] Felske, M., Redenius, J., Happich, G., & Schöning, J. (2026). Towards an Agricultural Operational Design Domain: A Framework. *Smart Agricultural Technology*. [https://doi.org/10.1016/j.atech.2026.102246](https://doi.org/10.1016/j.atech.2026.102246)

[12] Holm, S., Pedersen, S. M., & Tamirat, T. W. (2024). Robots in agriculture — A case-based discussion of ethical concerns on job loss, responsibility, and data control. *Smart Agricultural Technology*, 9, 100633. [https://doi.org/10.1016/j.atech.2024.100633](https://doi.org/10.1016/j.atech.2024.100633)

[13] Batey, T. (2009). Soil compaction and soil management — a review. *Soil Use and Management*, 25(4), 335–345. [https://doi.org/10.1111/j.1475-2743.2009.00236.x](https://doi.org/10.1111/j.1475-2743.2009.00236.x)

[14] Stilgoe, J., Owen, R., & Macnaghten, P. (2013). Developing a framework for responsible innovation. *Research Policy*, 42(9), 1568–1580. [https://doi.org/10.1016/j.respol.2013.05.008](https://doi.org/10.1016/j.respol.2013.05.008)

[15] Sustainable Robotics Base for Crops. (2026). *Agri JSON format, version 3 — schéma, profils, vocabulaires, registre d’indicateurs et documentation*. Licence CC BY 4.0. [https://github.com/Sustainable-Robotics-Base-for-Crops/json_agri_format](https://github.com/Sustainable-Robotics-Base-for-Crops/json_agri_format)

[16] Parlement européen & Conseil de l’Union européenne. (2023). *Règlement (UE) 2023/1230 du 14 juin 2023 relatif aux machines*. [https://eur-lex.europa.eu/eli/reg/2023/1230/oj](https://eur-lex.europa.eu/eli/reg/2023/1230/oj)

[17] ISO. (2024). *ISO 18497, parties 1 à 4 — Machines et tracteurs agricoles — Sécurité des machines partiellement automatisées, semi-autonomes et autonomes*. [https://www.iso.org/standard/82684.html](https://www.iso.org/standard/82684.html)

[18] Prévault-Osmani, A. (2026). *Manifeste pour une robotique agricole ouverte*. Sustainable Robotics Base for Crops. Licence CC BY 4.0. [https://github.com/Sustainable-Robotics-Base-for-Crops/ecosystem/blob/main/manifesto/MANIFESTO.fr.md](https://github.com/Sustainable-Robotics-Base-for-Crops/ecosystem/blob/main/manifesto/MANIFESTO.fr.md)

---

## À propos de l’auteur

**Alexandre Prévault-Osmani**  
CTO et cofondateur de SABI AGRI

Ingénieur par son métier et paysan par son parcours, Alexandre Prévault-Osmani travaille depuis 2015 à l’intersection de l’électrification, de la robotique agricole, de l’Open Source et de l’agroécologie. Il participe au développement du robot SRBC, présenté dans ce texte comme cas d’étude.

**Contact**

- GitHub : [Alexandre-PO](https://github.com/Alexandre-PO)
- LinkedIn : [alexandre-po](https://www.linkedin.com/in/alexandre-po)

# Manifeste pour une robotique agricole ouverte — Sustainable Robotics Base for Crops

L’écosystème de la robotique agricole a besoin d’une base commune, ouverte, frugale, sûre et documentée, capable de respecter la diversité des pratiques. C’est le sens de *Sustainable Robotics Base for Crops* (SRBC) : construire et partager un socle logiciel de production pour des robots agricoles autonomes, afin que la valeur créée par la technologie revienne aussi à ceux qui la font vivre — les paysans — et irrigue une filière juste, maintenable et durable.

**Nous affirmons qu’une robotique agricole ouverte peut accélérer l’adoption des pratiques agroécologiques en rendant possibles la diffusion d’outils appropriables, efficaces et sûrs. Performance agronomique, écologique, économique et sociale doivent devenir clairement mesurables et surtout éviter de s’opposer.**

Nous appelons agriculteurs, développeurs, fabricants, ateliers, intégrateurs, chercheurs, coopératives et établissements d’enseignement à rejoindre cet effort : publier une interface, stabiliser un format, écrire une documentation, exécuter un essai, former un voisin. Rien n’interdit d’innover vite et bien ; tout invite à le faire ensemble.

La technologie ne doit pas être une entrave. Elle doit être un pont vers la durabilité des systèmes agricoles.

---

## Pourquoi ouvrir

Lorsque nous avons fait germer le projet SABI AGRI en 2015, l’objectif était déjà de diffuser des agroéquipements au service d’une agriculture plus durable et plus souveraine. Notre expérience de constructeur de machines électriques et de robots agricoles nous a confrontés à une réalité structurelle : la rapidité des cycles numériques et le caractère fermé de nombreuses solutions créent une dépendance disproportionnée pour le monde paysan.

D’une part, l’obsolescence des supports matériels et logiciels n’est pas en phase avec les temps longs de l’agriculture. D’autre part, les interfaces propriétaires enferment les utilisateurs dans une relation déséquilibrée avec leurs fournisseurs, eux-mêmes dépendants des technologies de leurs propres fournisseurs. Une machine qui ne peut plus être comprise, entretenue ou adaptée finit par devenir une contrainte, même lorsqu’elle était initialement performante.

Nous pensons que chaque exploitation doit pouvoir bénéficier des avancées technologiques sans être captive de formats fermés. Ouvrir, c’est rendre possible la réparation, l’adaptation et la transmission des connaissances au rythme des saisons et des territoires.

## Pour qui, et au service de quoi

Nous situons l’écosystème robotique SRBC au service des petites et moyennes exploitations, en particulier lorsqu’elles sont diversifiées et engagées dans des pratiques agroécologiques. Elles jouent un rôle essentiel dans l’équilibre des écosystèmes, la diversité des productions, le dynamisme des territoires et le maintien de savoir-faire contextualisés. Cependant ces exploitations sont aussi particulièrement exposées au coût du travail, à la pénibilité des travaux physiques et aux barrières d’investissement.

Les pratiques agroécologiques demandent souvent davantage d’observation, de précision et de soin apporté aux sols et au vivant. La robotique peut contribuer à rendre ces pratiques économiquement accessibles : non en remplaçant la décision paysanne, mais en réduisant la pénibilité et en rendant réalisables des opérations favorables aux cultures, aux sols et aux écosystèmes.

Toute robotique ne sert pas cette ambition. Selon son architecture et son modèle économique, elle peut renforcer la concentration des moyens de production et la dépendance technologique. L’enjeu n’est donc pas d’adopter la robotique par principe, mais de déterminer au service de quels modèles agricoles elle est conçue, qui peut y accéder, qui la comprend, qui en fixe les usages, et qui en capte la valeur.

## Ce qu’est SRBC

*Sustainable Robotics Base for Crops* désigne l’écosystème public de briques logicielles développées entre autres pour le robot SRBC et, plus largement, pour une robotique agricole interopérable.

Ce n’est pas une démonstration hors sol. **Une part substantielle de ce code est utilisée en production** : navigation, localisation, géorepérage, perception, simulation, format de mission et outils associés. Les dépôts sont publiés sur l’organisation GitHub [Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops).

L’écosystème SRBC est un ensemble de packages et d’outils versionnés — principalement sous ROS 2 — conçus pour être lus, audités, réutilisés ou remplacés indépendamment. Les contrats ouverts (format de mission JSON Agri, interfaces de communication, messages de navigation) permettent à des outils tiers, des intégrateurs et des chercheurs de produire ou de consommer des missions sans dépendre des secrets d’un constructeur unique.

Nous assumons une frontière claire : **l’ouverture porte d’abord sur les fondations génériques et les interfaces** ; l’intégration industrielle ainsi que la chaîne de sûreté propre à la machine restent sous la responsabilité du constructeur. Ouvrir un commun ne signifie pas diluer la responsabilité. Cela signifie rendre partageables les connaissances nécessaires à l’interopérabilité, à la maintenance et à l’innovation collective.

## Une conception proportionnée, modulaire, ouverte et responsable

Pour qu’une robotique serve l’agroécologie, ses choix de conception doivent être cohérents.

Nous privilégions des machines **proportionnées** aux usages : suffisamment capables pour rendre un service réel, suffisamment légères et sobres pour rester accessibles, maintenables et compatibles avec le soin apporté aux sols.

Nous privilégions la **modularité** : séparer le porteur, les outils, les capteurs et les fonctions logicielles, afin de réparer, adapter, rétrofiter et mutualiser sans tout reconstruire à chaque évolution.

Nous privilégions l’**ouverture** : interfaces publiques, documentation, tests, versionnage et licences permettant l’étude, l’usage, la modification et la redistribution. L’Open Source n’est pas une fin en soi. C’est une méthode industrielle pour mutualiser les fondations et préserver la souveraineté d’usage dans la durée.

Nous privilégions enfin une innovation **responsable** : anticiper les effets sociaux et environnementaux, associer les utilisateurs, documenter les limites d’emploi, maîtriser les données agricoles, et maintenir une responsabilité industrielle explicite sur chaque machine mise en service.

Ces principes ne constituent pas un label. Ils constituent une exigence de cohérence : une technologie n’est utile que si elle augmente durablement la capacité des paysans à comprendre, décider et agir.

## Ce que change — et ne change pas — l’ouverture

Dans un secteur fragmenté, trop d’énergie est consacrée à réimplémenter les mêmes fondations. Mutualiser ces briques ne détruit pas l’activité industrielle : **elle la déplace**.

Pour les paysans, l’enjeu est la souveraineté d’usage : diagnostiquer, réparer, faire évoluer, choisir un prestataire et conserver l’accès aux données. Pour les fabricants, la différenciation se déplace vers l’intégration, la robustesse, la sûreté démontrée et le service. Pour les ateliers et intégrateurs, les interfaces documentées rendent possible une compétence locale et une capillarité territoriale. Pour la recherche et l’enseignement, des formats ouverts permettent enfin de comparer, d’enseigner et de transmettre.

Un commun technologique a besoin de documentation, de maintenance et de gouvernance. L’ouverture n’est durable que si des modèles économiques — machines, outils, services, formation — permettent aux entreprises de vivre sans recréer la captivité par d’autres moyens.

Même avec un code logiciel ouvert, la sûreté, la conformité et la responsabilité restent attachées à chaque configuration mise en service. Une fonction autonome n’a de sens que dans un domaine d’emploi explicite, avec des comportements prévisibles hors domaine et des preuves d’arrêt sûr. Nous refusons l’opposition naïve entre ouverture et industrialisation : industrialiser, c’est aussi rendre reproductibles la qualité, la maintenance, l’interopérabilité et la sûreté.

## Appel

La diffusion d’une robotique agricole au service de l’agroécologie se construit avec et chez les utilisateurs, de concert avec les constructeurs et les communautés techniques.

Chacun peut contribuer selon ses compétences : publier une interface, documenter une procédure, proposer un outil compatible, améliorer une brique, accueillir une expérimentation, former un voisin, partager des retours d’usage accompagnés de leurs limites.

**Ouvrir la robotique agricole, c’est refuser qu’elle devienne un instrument de dépendance. C’est donner au monde agricole les moyens de participer à sa conception, d’en maîtriser les usages et d’en transmettre les connaissances.**

Rejoignez l’écosystème : [github.com/Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops)

---

*Ce manifeste exprime l’état d’esprit de l’écosystème SRBC. Une doctrine de conception plus détaillée, ainsi que les méthodes d’évaluation et de diffusion associées, seront publiées ultérieurement.*

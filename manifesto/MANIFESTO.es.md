# Manifiesto por una robótica agrícola abierta — Sustainable Robotics Base for Crops

El ecosistema de la robótica agrícola necesita una base común, abierta, sobria, segura y documentada, capaz de respetar la diversidad de las prácticas. Ese es el sentido de *Sustainable Robotics Base for Crops* (SRBC): construir y compartir un fundamento de software de producción para robots agrícolas autónomos, a fin de que el valor creado por la tecnología vuelva también a quienes la hacen vivir — las campesinas y los campesinos — e irrigue una cadena justa, mantenible y duradera.

**Afirmamos que una robótica agrícola abierta puede contribuir a acelerar la adopción de las prácticas agroecológicas favoreciendo la difusión de herramientas eficaces, apropiables y seguras. Los rendimientos agronómicos, ecológicos, económicos y sociales deben volverse claramente medibles y, sobre todo, dejar de oponerse.**

Llamamos a agricultoras y agricultores, desarrolladores, fabricantes, talleres, integradores, investigadores, cooperativas y centros de formación a unirse a este esfuerzo: publicar una interfaz, estabilizar un formato, escribir documentación, ejecutar un ensayo, formar a un vecino. Nada impide innovar rápido y bien; todo invita a hacerlo juntos.

La tecnología no debe ser un obstáculo. Debe ser un puente hacia la durabilidad de los sistemas agrícolas.

---

## Por qué abrir

Cuando hicimos germinar el proyecto SABI AGRI en 2015, el objetivo ya era difundir agroequipos al servicio de una agricultura más sostenible y más soberana. Nuestra experiencia como fabricantes de máquinas eléctricas y de robots agrícolas nos ha confrontado con una realidad estructural: la rapidez de los ciclos digitales y el carácter cerrado de muchas soluciones crean una dependencia desproporcionada para el mundo campesino.

Por un lado, la obsolescencia de los soportes de hardware y software no está en fase con los tiempos largos de la agricultura. Por otro, las interfaces propietarias encierran a las personas usuarias en una relación desequilibrada con sus proveedores, a su vez dependientes de las tecnologías de sus propios proveedores. Una máquina que ya no puede comprenderse, mantenerse o adaptarse termina por convertirse en una constricción, incluso cuando inicialmente era performante.

Pensamos que cada explotación debe poder beneficiarse de los avances tecnológicos sin quedar cautiva de formatos cerrados. Abrir es hacer posibles la reparación, la adaptación y la transmisión de conocimientos al ritmo de las estaciones y de los territorios.

## Para quién, y al servicio de qué

Situamos el ecosistema robótico SRBC al servicio de las pequeñas y medianas explotaciones, en particular cuando están diversificadas y comprometidas con prácticas agroecológicas. Desempeñan un papel esencial en el equilibrio de los ecosistemas, la diversidad de las producciones, el dinamismo de los territorios y el mantenimiento de saberes contextualizados. Sin embargo, estas explotaciones también están particularmente expuestas a la penosidad de las labores físicas, a las necesidades de mano de obra y a las barreras de inversión.

Las prácticas agroecológicas suelen exigir más observación, más precisión y más cuidado del suelo y de lo vivo. La robótica puede contribuir a hacer estas prácticas económicamente accesibles reduciendo la penosidad y haciendo realizables operaciones favorables a los cultivos, a los suelos y a los ecosistemas. La decisión campesina puede entonces adquirir toda su importancia en la gestión de los ecosistemas.

No toda robótica sirve a esta ambición. Según su arquitectura y su modelo económico, puede reforzar la concentración de los medios de producción y la dependencia tecnológica. El reto no es, por tanto, adoptar la robótica por principio, sino determinar al servicio de qué modelos agrícolas se concibe, quién puede acceder a ella, quién la comprende, quién fija sus usos y quién capta el valor que genera.

## Qué es SRBC

*Sustainable Robotics Base for Crops* designa el ecosistema público de ladrillos de software desarrollados, entre otros, para el robot SRBC y, más ampliamente, para una robótica agrícola interoperable.

No es una demostración al margen del campo. **Una parte sustancial de este código se utiliza en producción**: navegación, localización, geovallado, percepción, simulación, formato de misión y herramientas asociadas. Los repositorios se publican en la organización GitHub [Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops).

El ecosistema SRBC es un conjunto de paquetes y herramientas versionados — principalmente bajo ROS 2 — concebidos para ser leídos, auditados, reutilizados o sustituidos de forma independiente. Los contratos abiertos (formato de misión JSON Agri, interfaces de comunicación, mensajes de navegación) permiten a herramientas de terceros, integradores e investigadores producir o consumir misiones sin depender de los secretos de un único fabricante.

Asumimos una frontera clara: **la apertura se centra primero en los fundamentos genéricos y las interfaces**; la integración industrial y la cadena de seguridad propia de la máquina siguen bajo la responsabilidad del fabricante. Abrir un común debe acompañarse de una cadena de responsabilidad clara, haciendo al mismo tiempo compartibles los conocimientos necesarios para la interoperabilidad, el mantenimiento y la innovación colectiva.

## Un diseño proporcionado, modular, abierto y responsable

Para que una robótica sirva a la agroecología, sus elecciones de diseño deben ser coherentes.

Privilegiamos máquinas **proporcionadas** a los usos: suficientemente capaces para prestar un servicio real, suficientemente ligeras y sobrias para seguir siendo accesibles, mantenibles y compatibles con el cuidado del suelo.

Privilegiamos la **modularidad**: separar el portador, las herramientas, los sensores y las funciones de software, a fin de reparar, adaptar, hacer retrofit y mutualizar sin reconstruir todo en cada evolución.

Privilegiamos la **apertura**: interfaces públicas, documentación, pruebas, versionado y licencias que permiten el estudio, el uso, la modificación y la redistribución. El open source no es un fin en sí mismo. Es un método industrial para mutualizar los fundamentos y preservar la soberanía de uso a lo largo del tiempo.

Privilegiamos, por último, una innovación **responsable**: anticipar los efectos sociales y ambientales, asociar a las personas usuarias, documentar los límites de empleo, gobernar con cuidado los datos agrícolas y mantener una responsabilidad industrial explícita sobre cada máquina puesta en servicio.

Estos principios no constituyen una etiqueta. Constituyen una exigencia de coherencia: una tecnología solo es útil si aumenta de forma duradera la capacidad de las campesinas y los campesinos para comprender, decidir y actuar.

## Lo que aporta la apertura

En un sector fragmentado, se dedica demasiada energía a reimplementar los mismos fundamentos. Mutualizar estos ladrillos no destruye la actividad industrial: **la desplaza**.

Para las campesinas y los campesinos, lo que está en juego es la soberanía de uso: diagnosticar, reparar, hacer evolucionar, elegir un prestador y conservar el acceso a los datos. Para los fabricantes, la diferenciación se desplaza hacia la integración, la robustez, la seguridad demostrada y el servicio. Para los talleres e integradores, las interfaces documentadas hacen posible una competencia local y una capilaridad territorial. Para la investigación y la enseñanza, los formatos abiertos permiten por fin comparar, enseñar y transmitir.

Un común tecnológico necesita documentación, mantenimiento y gobernanza. La apertura solo es duradera si modelos económicos — máquinas, herramientas, servicios, formación — permiten a las empresas vivir sin recrear la cautividad por otros medios.

Incluso con un código de software abierto, la seguridad, la conformidad y la responsabilidad siguen ligadas a cada configuración puesta en servicio. Una función autónoma solo tiene sentido en un dominio de empleo explícito, con comportamientos previsibles fuera de ese dominio y pruebas de parada segura. Rechazamos la oposición ingenua entre apertura e industrialización: industrializar es también hacer reproducibles la calidad, el mantenimiento, la interoperabilidad y la seguridad.

## Llamamiento

La difusión de una robótica agrícola al servicio de la agroecología se construye con y entre las personas usuarias, de concierto con los constructores y las comunidades técnicas.

Cada cual puede contribuir según sus competencias: publicar una interfaz, documentar un procedimiento, proponer una herramienta compatible, mejorar un ladrillo, acoger una experimentación, formar a un vecino, compartir retornos de uso acompañados de sus límites.

**Abrir la robótica agrícola es negarse a que se convierta en un instrumento de dependencia. Es dar al mundo agrícola los medios para participar en su concepción, dominar sus usos y transmitir sus conocimientos.**

Únanse al ecosistema: [github.com/Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops)

---

## Sobre el autor

**Autor: Alexandre Prévault-Osmani — CTO y cofundador de SABI AGRI.**

Desde 2015, Alexandre Prévault-Osmani trabaja en la intersección de la electrificación, la robótica agrícola, el open source y la agroecología. Desarrolla un enfoque industrial orientado a hacer que las tecnologías agrícolas sean accesibles, interoperables, mantenibles y apropiables por el mundo campesino.

[GitHub](https://github.com/Alexandre-PO) · [LinkedIn](https://www.linkedin.com/in/alexandre-po)

# SMOR: hacia un estándar difundible de robótica agrícola al servicio de la agroecología

### Sustainable Robotics Base for Crops

Autor: Alexandre Prévault-Osmani — CTO y cofundador de SABI AGRI

*Libro blanco · versión corta · septiembre de 2026 · licencia CC BY 4.0*

---

## Sumario

1. [Síntesis](#síntesis)
2. [Nociones clave](#nociones-clave)
3. [Tesis y posicionamiento](#tesis-y-posicionamiento)
4. [Qué frena la difusión](#qué-frena-la-difusión)
5. [La visión SMOR](#la-visión-smor)
6. [Una arquitectura de referencia y una cadena de prueba abierta](#una-arquitectura-de-referencia-y-una-cadena-de-prueba-abierta)
7. [El robot SRBC, una primera encarnación](#el-robot-srbc-una-primera-encarnación)
8. [Evaluar lo que importa para la explotación](#evaluar-lo-que-importa-para-la-explotación)
9. [Un común que pertenece al mundo campesino](#un-común-que-pertenece-al-mundo-campesino)
10. [Seguridad, conformidad y corresponsabilidad](#seguridad-conformidad-y-corresponsabilidad)
11. [Del código al común: la hoja de ruta](#del-código-al-común-la-hoja-de-ruta)
12. [Límites y llamamiento](#límites-y-llamamiento)
13. [Referencias](#referencias)
14. [Sobre el autor](#sobre-el-autor)

---

## Síntesis

La robótica agrícola promete reducir la penosidad, responder a las dificultades de contratación y hacer más precisas las intervenciones. Diez años después de la llegada de los primeros robots a los campos, su difusión sigue siendo, sin embargo, limitada. Una demostración exitosa dice poco sobre la disponibilidad de una máquina a lo largo de una campaña, sobre la calidad agronómica de su trabajo o sobre su viabilidad en la vida cotidiana de una explotación. El reto se desplaza: hacer funcionar un robot cuenta hoy menos que crear las condiciones de su adopción duradera.

Sostenemos que la robótica debe servir prioritariamente a las explotaciones pequeñas y medianas, diversificadas y en transición agroecológica. Para ello proponemos la visión SMOR — *Small, Modular, Open & Responsible* —, traducida en una arquitectura de referencia, una cadena documental abierta que vincula lo que el robot debía hacer con lo que realmente hizo, un método de evaluación, un modelo de común que pertenece al mundo campesino y un reparto explícito de responsabilidades. El robot SRBC es su primera encarnación industrial. SMOR es un marco que debe ponerse a prueba: este texto expone su tesis y sus propuestas, la versión completa aportará sus pruebas.

---

## Nociones clave

- **ODD** (Operational Design Domain, dominio operativo de diseño): las condiciones para las que una función autónoma ha sido diseñada y validada — parcela, suelo, meteorología, pendiente, calidad de la localización, presencia de personas.
- **Orden de misión**: archivo que describe lo que el robot debe hacer, dentro de qué límites y con qué reacciones admitidas.
- **Trabajo realizado**: archivo que describe lo que el robot hizo, en qué condiciones encontradas y cómo juzga la explotación el servicio prestado.
- **Open Core**: modelo en el que las interfaces y los componentes genéricos son abiertos, mientras que la implementación material, la calibración y los servicios quedan bajo la responsabilidad del fabricante.

---

## Tesis y posicionamiento

Desde mediados de la década de 2010, la robótica agrícola ha salido de los laboratorios para llegar a los campos. Los avances en percepción, navegación y automatización son reales; la difusión comercial sigue siendo modesta frente a la diversidad de las producciones y al número de explotaciones [1, 2]. Esta brecha exige otra definición de la madurez.

Nuestro enfoque es sencillo: la madurez de un robot agrícola se mide por su **difundibilidad**, es decir, por su capacidad de ser utilizado, mantenido, reparado y mejorado en los tiempos largos de la agricultura. Supone la adecuación a una necesidad agronómica y humana claramente identificada, un coste accesible, una seguridad demostrada en un dominio de uso explícito, un mantenimiento de proximidad y una apropiación real por parte de las personas que lo utilizan.

Asumimos una elección de posicionamiento explícita: la robótica agrícola debe servir prioritariamente a las explotaciones pequeñas y medianas, en particular cuando están diversificadas y en transición agroecológica. Las definimos ante todo como empresas agrícolas a escala humana, en las que quien trabaja la tierra conserva una capacidad directa de observación y de decisión sobre los cultivos y los suelos; la clasificación del censo agrario francés por producción estándar ofrece una referencia estadística [3]. Estas explotaciones sostienen la diversidad de las producciones, el cuidado de los paisajes, el empleo rural y saberes contextualizados. Son también las más expuestas al coste del trabajo, a la penosidad y a las barreras de inversión.

Las prácticas agroecológicas exigen más observación, más precisión e intervenciones más diferenciadas [4]. Esta intensidad agronómica es difícil de sostener cuando el trabajo humano pesa como un coste frente a las economías de escala. La robótica puede reequilibrar esta relación reduciendo la penosidad y haciendo posibles operaciones favorables a los suelos y a los ecosistemas: una siembra precisa que prepara una escarda mecánica temprana, pasadas repetidas de un apero ligero en una ventana corta, una máquina ligera allí donde la capacidad portante del suelo lo exige.

La misma tecnología puede servir también a la concentración de los medios de producción, a la dependencia de proveedores propietarios y a la obsolescencia rápida de los equipos [5, 6]. La dirección depende de las elecciones de arquitectura, de modelo económico y de gobernanza. El contraste entre los ciclos cortos de lo digital y los tiempos largos de la agricultura lo convierte en una cuestión estructural: una máquina que ya no se puede comprender, mantener o adaptar se vuelve una carga, aunque al principio fuera eficaz.

Distinguimos tres niveles: la **capacidad técnica** del robot (desplazarse, seguir una hilera, accionar un apero con seguridad), el **rendimiento agronómico** en una ventana dada (una siembra regular, una escarda eficaz) y el **efecto agroecológico**, que se aprecia en el tiempo a escala del sistema de cultivo (insumos evitados, estado del suelo, biodiversidad, condiciones de trabajo, autonomía de la explotación, coste completo). Las evaluaciones existentes documentan sobre todo el primer nivel; la utilidad de un robot para una explotación depende de los otros dos.

> **Tesis**  
> La robótica agrícola se convierte en una palanca de difusión de la agroecología cuando se diseña para ser útil, accesible, mantenible, segura, interoperable y apropiable, y cuando sabe demostrar su rendimiento en condiciones reales.

Añadimos una convicción de método: la difusión es una cuestión de **representación** tanto como de medida. Mientras la intención agronómica y el resultado obtenido se describan en vocabularios distintos, los retornos de campo seguirán aislados, los resultados de dos fabricantes serán incomparables y las responsabilidades, inverificables. Un vocabulario común y versionado es la primera condición de un conocimiento acumulativo.

---

## Qué frena la difusión

Un robot agrícola trabaja en contacto con sistemas vivos: el suelo, la vegetación, la meteorología y la organización del trabajo varían a lo largo de una campaña. Todo rendimiento debe, por tanto, referirse a un uso, a una configuración y a un dominio de uso explícito.

Los frenos son conocidos e interdependientes [1, 7]: la **robustez** a lo largo de una campaña; la **seguridad**, que exige detectar las situaciones peligrosas y alcanzar un estado seguro; el **rendimiento agronómico**, que se mide por la calidad del trabajo del apero más que por la precisión de la trayectoria; la **rentabilidad**, que depende del tiempo de supervisión, del mantenimiento y de las paradas mucho más que del precio de compra; la **interoperabilidad**, débil mientras formatos, interfaces y protocolos sigan siendo propios de cada fabricante, y la **dependencia tecnológica** que se deriva de ello. Trabajos recientes muestran que el tiempo humano dedicado a la logística y a la supervisión constituye el verdadero problema de la robótica a pequeña escala [7].

La agricultura de precisión dispone ya de estándares valiosos, como ISOXML o ADAPT, para describir una tarea y el trabajo realizado [8, 9]. Fueron concebidos para una persona al volante, que garantiza el dominio de uso. Con un robot, una parte de la observación y de la decisión pasa a la máquina, y la cadena que va de la intención a la ejecución debe hacerse explícita: lo que el robot debe hacer, en qué condiciones está autorizado a hacerlo, cómo reacciona ante los imprevistos, lo que encontró y lo que realizó. La industria reconoce esta necesidad, con el grupo de trabajo de la AEF dedicado a las máquinas autónomas [10], al igual que la investigación sobre el dominio operativo agrícola [11]. Consideramos que estos trabajos son convergentes y deseamos contribuir a ellos con una propuesta abierta, ya utilizada en el campo.

La literatura que interroga la robótica desde el punto de vista agroecológico coincide en un punto: la dirección sigue abierta. La misma tecnología puede conducir a flotas de pequeñas máquinas al servicio de sistemas diversificados o a grandes máquinas que consolidan los monocultivos [6]. Aportar funcionalidades autónomas a los sistemas agroecológicos supone diseñar con una diversidad de actores, más allá de una «mentalidad monocultural» [5], y las agricultoras y los agricultores sitúan la responsabilidad, la seguridad y el control de los datos entre sus principales preocupaciones [12]. Estos resultados fundamentan nuestra elección de confiar a las campesinas y los campesinos la decisión sobre el uso de su tecnología y su garantía.

---

## La visión SMOR

SMOR es un marco de diseño y de evaluación que vincula las características de un robot con sus efectos agronómicos, económicos, ambientales y sociales. Tiene hoy el estatus de una propuesta que debe ponerse a prueba en el campo y en el debate.

Privilegiamos la tracción y los actuadores eléctricos. Los motores y actuadores eléctricos se controlan con finura, informan de su estado y se integran directamente en los sistemas de diagnóstico. La electricidad puede proceder de la red o producirse en la explotación, lo que abre el camino a una autonomía energética total o parcial; baterías y motores deben evaluarse en todo su ciclo de vida.

**Small: una escala adecuada.** Privilegiamos máquinas cuya masa, potencia y dimensiones se mantienen proporcionadas a las operaciones. Nuestro objetivo dimensional se sitúa entre el ser humano y el caballo de tiro: entre 80 y 1 200 kg aproximadamente, menos de 10 km/h, unos pocos kilovatios, una autonomía de media jornada a una jornada de trabajo, muy baja tensión y, para los portadores ligeros, una inversión inferior a 40 000 euros. Más allá, la masa devuelve la máquina al mundo del tractor, con su motorización, su logística y su precio. Estos valores son objetivos de diseño. Una masa contenida reduce la energía en juego y facilita el transporte y el mantenimiento; el efecto sobre el suelo depende también de la presión de contacto, del patinaje, del número de pasadas y de la humedad [13]. Esta escala permite disponer de varios robots especializados o compartidos entre explotaciones en lugar de una única máquina dimensionada para la operación más pesada. Se convierte en una ventaja económica duradera cuando el tiempo humano por hectárea disminuye realmente, lo que exige misiones fiables sin vigilancia continua y, con el tiempo, la supervisión de varios robots por una sola persona.

**Modular: adaptar, reparar, compartir.** Separamos una base estable (estructura, energía, control, interfaces, seguridad) de módulos adaptados a los cultivos, a los aperos y a los contextos: cambiar de apero, de tren de rodaje o de sensor sin sustituir el portador, hacer evolucionar una función de software sin reconstruir el conjunto, actualizar una máquina al ritmo del calendario de cultivo. Esta modularidad se apoya en dimensiones, conectores, protocolos y formatos documentados; sin ellos, quedaría como rehén del proveedor inicial.

**Open: una soberanía duradera.** Abrimos prioritariamente las interfaces, los formatos de misión y de datos, la documentación y los componentes de software genéricos, y después los planos de construcción cuando su publicación refuerza la reparabilidad. El Open Source que defendemos es un método industrial: licencias explícitas, contratos versionados, pruebas, documentación, gobernanza y versiones estables. Garantiza a las explotaciones una soberanía de uso (diagnosticar, reparar, adaptar, confiar el mantenimiento a otro proveedor), desplaza la diferenciación de los fabricantes hacia la integración, la seguridad y el servicio, y permite desarrollar competencias duraderas en los talleres de los territorios.

**Responsible: una innovación que rinde cuentas.** Una tecnología se vuelve responsable cuando sus efectos se anticipan, se debaten, se miden y se corrigen con las personas afectadas [14]. Este principio compromete a implicar a las agricultoras y los agricultores en la definición de las necesidades y en la evaluación, a diseñar la seguridad desde el principio, a documentar los límites de uso, a medir los consumos de materia, de energía y de recursos digitales, a preservar la decisión campesina, a garantizar la soberanía de la explotación sobre sus datos y a hacer verificable el reparto de responsabilidades.

Estos cuatro principios forman un todo. Un robot pequeño y cerrado queda cautivo y envejece deprisa; una plataforma abierta sin gobernanza se fragmenta; una máquina modular pero demasiado cara no incide en la difusión. **SMOR propone una coherencia de conjunto: una robótica cuyo rendimiento se mide por su capacidad de hacer la agroecología practicable, económicamente viable y apropiable a largo plazo por el mundo campesino.**

---

## Una arquitectura de referencia y una cadena de prueba abierta

Una arquitectura de referencia proporciona una lengua común: separa las funciones y define las interfaces a través de las cuales un componente puede sustituirse sin reconstruir el sistema. Cada fabricante sigue siendo libre en sus elecciones materiales, siempre que respete los contratos comunes y los requisitos de seguridad. Proponemos seis capas: energía y actuadores, control del vehículo, buses de campo documentados, ordenador de a bordo (ROS 2 constituye hoy una base adecuada), percepción y localización, misión e interfaz de usuario. Un principio las atraviesa todas: **las funciones críticas para la seguridad permanecen independientes del ordenador generalista y de cualquier conexión remota.** Las funciones esenciales siguen disponibles sin conexión, y la interfaz hace visibles el estado del robot, sus límites y el motivo de cada parada.

El contrato más estructurante es la **interfaz de vehículo**, que describe órdenes, estados, capacidades del apero y fallos. Permite adaptar una misma función de navegación a varios portadores y convierte así un producto en plataforma.

El segundo contrato se refiere a la misión. Proponemos **JSON Agri**, un formato abierto publicado bajo licencia CC BY 4.0 [15], legible sin formación informática y verificable por las máquinas. Organiza una cadena de dos documentos. La **orden de misión** describe el objetivo agronómico y sus criterios de aceptación, el par portador-apero, el dominio de uso admitido, la trayectoria, las zonas autorizadas y las reacciones previstas ante los eventos: una batería baja provoca, por ejemplo, el regreso a la zona de carga por caminos autorizados. El **trabajo realizado** vincula esta intención con las condiciones encontradas, los eventos, las intervenciones humanas, los indicadores de rendimiento y el juicio agronómico de la explotación. Una huella digital de la orden, recogida en el trabajo realizado, garantiza que la ejecución se compara con la versión exacta de la misión.

Tres elecciones dan a esta cadena su alcance. El dominio de uso admitido y las condiciones encontradas comparten el mismo vocabulario, de modo que cada desviación puede vincularse a una detección, una decisión, una responsabilidad y una prueba. Las reacciones ante los eventos forman un vocabulario cerrado: la máquina rechaza toda instrucción desconocida o ausente del catálogo validado por el fabricante, y su suelo de seguridad queda fuera del alcance de cualquier archivo. La atestación producida en simulación certifica que un archivo ha superado controles definidos, bajo hipótesis declaradas; vale como prueba de verificación, distinta de una certificación.

La cadena separa así tres validaciones: la **preparación**, en el editor de misiones; la validación **operativa**, a bordo, en la que el robot confronta la misión con su configuración y con las condiciones confirmadas in situ, conservando la libertad de rechazar; la validación del **rendimiento**, tras la misión, mediante el juicio agronómico de la explotación. Esta separación protege de dos confusiones costosas: tomar una simulación por una autorización, o una misión terminada por un servicio logrado. Reglas de especificación públicas (un núcleo pequeño y estable, datos ausentes señalados como tales, compatibilidad garantizada, validación sin conexión), niveles de conformidad y un validador permiten a cualquier tercero verificar de forma autónoma su implementación. JSON Agri completa así los estándares existentes con la cadena de la autonomía que estos dejan implícita.

---

## El robot SRBC, una primera encarnación

El robot SRBC, desarrollado por SABI AGRI, pone a prueba estos principios en una máquina vendida y utilizada en el campo. Este portador eléctrico compacto, sobre ruedas u orugas, pesa unos 250 kg en su versión de orugas y se sitúa, por tanto, en la parte baja del marco SMOR. Lleva aperos de laboreo ligero, siembra, cuidado de cultivos y transporte. Su cadena de seguridad material funciona con independencia del ordenador, y las protecciones de alto nivel (geocercado, visión de seguridad) imponen sus órdenes a la navegación mediante un arbitraje de prioridad. **La persona formada que conduce el robot define y respeta el dominio de uso; el software de alto nivel contribuye a prevenir los incidentes; el control de bajo nivel garantiza el regreso a un estado seguro.**

La navegación, la localización, el geocercado, la percepción de seguridad, la simulación, el formato JSON Agri y los editores de misión están publicados en la organización de GitHub [Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops), bajo licencia Apache 2.0 para el código y CC BY 4.0 para las especificaciones. El robot que trabaja en la parcela ejecuta este código público. El software del controlador, el controlador del vehículo, los contratos de mando, las calibraciones y los servicios remotos permanecen bajo la responsabilidad del fabricante: SRBC es un **Open Core industrial**, y describimos su apertura tal como es.

Cualquier organización externa puede así hacer funcionar de principio a fin un robot simulado, preparar y validar una misión, observar un robot real a través de una interfaz publicada, verificar la conformidad de sus archivos y reutilizar cada componente de navegación. Las próximas etapas de apertura permitirán controlar el robot, llevar la pila de software a otros vehículos y construir una máquina a partir del código público.

---

## Evaluar lo que importa para la explotación

Una demostración aislada aporta un ejemplo; un protocolo documentado, repetido y comparable aporta una prueba. Nuestro método vincula cada resultado a una operación agronómica, a una situación de referencia (trabajo manual, tractor, práctica anterior), a un dominio de uso, a una configuración y a un catálogo de indicadores versionado, todos fijados antes del ensayo. Apoyado en la cadena entre orden de misión y trabajo realizado, este vínculo permite a terceros recalcular lo que publicamos. Los indicadores cubren el rendimiento agronómico, la disponibilidad, la energía, la seguridad, el tiempo humano, el coste completo y los efectos sobre el suelo; se publican con su convención de cálculo, su dispersión y su cobertura. Un valor ausente se declara como tal: la ausencia es una información.

La máquina sabe medir su duración, su trayectoria, su energía y la calidad de su localización. Las magnitudes que deciden la utilidad para la explotación dependen a menudo de una persona: condiciones realmente encontradas, satisfacción agronómica, tiempo de supervisión, necesidad de una segunda pasada. Proponemos recogerlas en tres momentos, allí donde se encuentra la persona: en la preparación, en la carga en el robot y al final de la misión, con una herramienta que rellena de antemano lo que puede y hace pocas preguntas. Del mismo modo, una magnitud medida se convierte en criterio cuando alguien fija su umbral en la orden de misión y la máquina sabe cómo reaccionar cuando se supera.

Nuestras primeras campañas instrumentadas confirman la viabilidad de esta cadena entre robots, explotaciones y aperos diferentes. La base de pruebas progresará con sus éxitos y con sus fracasos, para establecer dónde, cuándo y en qué condiciones la robótica aporta un beneficio agroecológico real.

---

## Un común que pertenece al mundo campesino

Sostenemos que el ecosistema de software de la robótica agrícola — formatos de archivo, código de guiado, algoritmos de decisión, herramientas de misión y de trazabilidad — debe convertirse en un **común que pertenece al mundo campesino y del que el mundo campesino se apropia**.

Este común es ante todo un vocabulario. Una explotación describe su expectativa en términos agronómicos, un distribuidor en términos de servicio, un fabricante en términos de funciones. La primera tarea del común es permitir a estos actores **describir, intercambiar y rebatir hechos en los mismos términos**. El código abierto hace utilizable este vocabulario y demuestra, en funcionamiento, que funciona; el vocabulario hace sustituible el código y, por tanto, gobernable el común. Un formato que varias implementaciones saben leer escapa a toda apropiación, incluida la de la empresa que lo inició.

Por mundo campesino entendemos las campesinas y los campesinos, así como los talleres, los distribuidores, las cooperativas, los institutos y los fabricantes que trabajan a su servicio. Esta pertenencia se construye mediante cinco propiedades verificables:

- **sigue abierto**: las licencias garantizan el libre uso a largo plazo, y la marca protege el sentido de los términos;
- **sobrevive a la empresa que lo inició**: repositorios públicos, historial y documentación permiten a otros retomarlo; con el tiempo, su propiedad se transfiere a una estructura sin ánimo de lucro, independiente de cualquier fabricante, de la que las campesinas y los campesinos y sus organizaciones son miembros de pleno derecho;
- **se gobierna con las personas a las que sirve**: las campesinas y los campesinos participan en las decisiones sobre su finalidad y disponen de un derecho de impugnación;
- **devuelve los datos a la explotación**: el trabajo realizado pertenece a la explotación, que puede leerlo, conservarlo, compartirlo o guardarlo para sí sin pasar por un proveedor [12];
- **se aprende**: herramientas legibles, formaciones entre pares y talleres locales lo inscriben en la tradición de la educación popular técnica.

Los componentes de un robot requieren grados de apertura diferentes. Los **contratos comunes** (formatos, indicadores, interfaces, criterios de conformidad) se abren prioritariamente; los **componentes genéricos** (navegación, simulación, diagnóstico, editores) se desarrollan como comunes de software; la **integración industrial** y la cadena de seguridad corresponden al fabricante; los **servicios y datos sensibles** mantienen un acceso controlado. La regla que hace defendible un Open Core cabe en una frase: **se abren los contratos y la lógica genérica; se conservan la implementación material, la calibración y los servicios de flota.** La ventaja de un fabricante reside en su máquina, su cadena de seguridad, su red de servicio y su capacidad de cumplir sus compromisos en el tiempo.

La apertura desplaza el valor y los costes. Reduce la reimplementación de las mismas bases y crea necesidades de mantenimiento y de gobernanza que hay que financiar. La venta y el alquiler de máquinas, la adaptación local, los contratos de servicio, las versiones mantenidas, la formación y el acompañamiento en la conformidad hacen vivir a las empresas, siempre que renuncien a la captura mediante datos retenidos, suscripciones indispensables para el funcionamiento básico o interfaces cerradas artificialmente. Aplicamos Apache 2.0 al código y CC BY 4.0 a las especificaciones y a los textos; la cuestión de una reciprocidad para ciertos componentes se decidirá colectivamente.

La gobernanza sigue al uso. Las decisiones sobre el formato ya se registran públicamente, y un procedimiento escrito permite impugnarlas. Varias etapas, activadas por hechos observables, organizan lo que sigue, empezando por un comité de versiones desde la primera implementación de terceros, y después un colegio de usos dotado de un derecho de impugnación en cuanto un colectivo de agricultoras y agricultores, una cooperativa o un distribuidor dependa del formato. La última etapa transfiere la propiedad del formato y de la marca a la estructura sin ánimo de lucro descrita más arriba; hace al común independiente de la empresa que lo inició, y la consideramos una condición de credibilidad del conjunto.

---

## Seguridad, conformidad y corresponsabilidad

La conformidad de una máquina autónoma estructura su diseño, sus ensayos y su vigilancia durante toda su vida. La Directiva de máquinas 2006/42/CE se aplica hasta el 19 de enero de 2027, fecha a partir de la cual el Reglamento (UE) 2023/1230 toma el relevo [16]; la serie ISO 18497:2024 trata de las máquinas agrícolas autónomas [17]. El código abierto facilita la verificación, la trazabilidad y el mantenimiento. La seguridad y la conformidad siguen ligadas, en cambio, a cada máquina comercializada o puesta en servicio, a su evaluación de riesgos, a sus ensayos y a su configuración validada. Una reparación que preserva la conformidad sigue siendo una reparación, y la apertura aspira precisamente a facilitarla; una modificación que crea un nuevo peligro compromete a la persona o entidad que la realiza. Los equipos que mantienen el común responden de la calidad de las contribuciones; la validación de la integración corresponde a la entidad que pone la máquina en servicio.

Proponemos completar este reparto reglamentario con una **corresponsabilidad operativa**, que indique para cada etapa quién decide, quién valida y qué prueba se conserva.

| Etapa | Decide | Valida | Prueba conservada |
|---|---|---|---|
| Elección agronómica y ventana de trabajo | Agricultora/agricultor | Agricultora/agricultor | intención y criterios en la orden de misión |
| Mapa de la parcela y obstáculos conocidos | Agricultora/agricultor | Agricultora/agricultor | mapa de la parcela referenciado |
| Dominio de uso admitido y reacciones ante eventos | Agricultora/agricultor u operador/a | Suelo de seguridad del fabricante | dominio y estrategias en la orden |
| Enganche del apero y verificación antes de la salida | Operador/a | Operador/a | configuración prevista y utilizada |
| Ejecución | Máquina, libre de rechazar | Límites del fabricante, parada de emergencia | eventos, acciones solicitadas y ejecutadas |
| Juicio sobre el servicio prestado | Agricultora/agricultor | Agricultora/agricultor | juicio en el trabajo realizado |

Una casilla sin titular es un resultado: señala una laguna que hay que cubrir. Una responsabilidad entendida de forma distinta por dos partes es también un resultado, que debe debatirse abiertamente. Esta corresponsabilidad organiza la colaboración cotidiana y deja intacta la responsabilidad reglamentaria del fabricante o del integrador. **Se trata de hacer compartibles los saberes manteniendo una responsabilidad explícita para cada máquina puesta en servicio.**

---

## Del código al común: la hoja de ruta

La difusión de SMOR se medirá por la capacidad de organizaciones externas de comprender las interfaces, reproducir un ensayo, adaptar un componente, leer un trabajo realizado y mantener una máquina con independencia de su desarrollador. Avanzamos en cuatro etapas: **hacer visible** lo que existe, con su estado y sus límites; **hacer reproducible** la instalación y la simulación de una misión; **hacer interoperable** publicando contratos y pruebas; **hacer difundible** construyendo pruebas, competencias y servicios en el campo.

De ello se derivan cinco líneas de trabajo: consolidar la base abierta; publicar los contratos de mando y la interfaz de vehículo, y después obtener una segunda implementación del formato por parte de una organización externa, condición para hablar de estándar; constituir una base de pruebas verificada por un instituto independiente, con coste completo y tiempo humano medidos a lo largo de varias campañas; organizar la seguridad de cada configuración comercializada; desarrollar competencias territoriales para que explotaciones, talleres y distribuidores sepan diagnosticar, reparar y formar a su vez, porque se gobierna lo que se comprende. La adopción avanza por círculos, del uso interno a los socios de confianza, después a las integraciones de terceros y a una difusión amplia, y cada paso depende de criterios observables. Las descargas indican un interés; la difusión agrícola se demuestra en el campo.

---

## Límites y llamamiento

Este texto propone un marco conceptual y técnico; la demostración de su beneficio agronómico y económico requiere campañas repetidas y observaciones plurianuales, que la versión completa documentará. Conocemos sus límites: el marco SMOR es un objetivo de diseño; SRBC constituye un primer caso de estudio, impulsado por un equipo implicado en su desarrollo; la adopción de JSON Agri por otros fabricantes y la publicación de la interfaz de vehículo son las próximas etapas; los efectos sobre los suelos y sobre el oficio campesino necesitan tiempo para manifestarse. Es la situación de un común naciente. Lo publicamos para reunir las implementaciones, las competencias y los usos que lo harán crecer.

Nada impide innovar rápido y bien; todo invita a hacerlo juntos [18]. Cada cual puede dar un primer paso, a su escala:

- **agricultoras, agricultores y colectivos**: acoger una misión instrumentada, exigir el acceso a las órdenes de misión y a los trabajos realizados en sus parcelas, decir al final de la misión lo que la máquina no puede saber;
- **distribuidores, talleres, integradores**: aprender a leer un archivo de misión, documentar un enganche, señalar un incidente con su configuración, formar a una vecina o a un vecino;
- **fabricantes de robots y de aperos**: implementar un lector del formato, publicar una interfaz, aunque sea modesta, con sus límites;
- **institutos, laboratorios, centros de formación**: llevar a cabo un protocolo, verificar una convención de cálculo, proponer un umbral basado en observaciones;
- **cooperativas, administraciones territoriales, financiadores públicos**: apoyar las infraestructuras comunes (parcelas de ensayo, formación, documentación, mantenimiento de los estándares) al mismo nivel que la compra de máquinas;
- **comunidades de desarrollo**: mejorar un componente, escribir una prueba, mantener una versión estable, participar en la gobernanza.

> **La tecnología se convierte en progreso agrícola cuando refuerza de forma duradera la capacidad de las campesinas y los campesinos de comprender, decidir y actuar.**  
> Abrir la robótica es dar al mundo agrícola los medios para participar en su diseño, dominar su uso y transmitir sus saberes.

**Unirse al ecosistema**  
[github.com/Sustainable-Robotics-Base-for-Crops](https://github.com/Sustainable-Robotics-Base-for-Crops)

---

## Referencias

[1] Bechar, A., & Vigneault, C. (2016). Agricultural robots for field operations: Concepts and components. *Biosystems Engineering*, 149, 94–111. [https://doi.org/10.1016/j.biosystemseng.2016.06.014](https://doi.org/10.1016/j.biosystemseng.2016.06.014)

[2] Lowenberg-DeBoer, J., Huang, I. Y., Grigoriadis, V., & Blackmore, S. (2020). Economics of robots and automation in field crop production. *Precision Agriculture*, 21, 278–299. [https://doi.org/10.1007/s11119-019-09667-5](https://doi.org/10.1007/s11119-019-09667-5)

[3] Agreste. (2022). *Recensement agricole 2020 — Typologie des exploitations selon leur dimension économique* [Censo agrario 2020 — Tipología de las explotaciones según su dimensión económica]. Ministerio francés de Agricultura. [https://agreste.agriculture.gouv.fr/agreste-web/disaron/RA2020_001/detail/](https://agreste.agriculture.gouv.fr/agreste-web/disaron/RA2020_001/detail/)

[4] Wezel, A., Bellon, S., Doré, T., Francis, C., Vallod, D., & David, C. (2009). Agroecology as a science, a movement and a practice. A review. *Agronomy for Sustainable Development*, 29(4), 503–515. [https://doi.org/10.1051/agro/2009004](https://doi.org/10.1051/agro/2009004)

[5] Ditzler, L., & Driessen, C. (2022). Automating Agroecology: How to Design a Farming Robot Without a Monocultural Mindset? *Journal of Agricultural and Environmental Ethics*, 35, 2. [https://doi.org/10.1007/s10806-021-09876-x](https://doi.org/10.1007/s10806-021-09876-x)

[6] Daum, T. (2021). Farm robots: ecological utopia or dystopia? *Trends in Ecology & Evolution*, 36(9), 774–777. [https://doi.org/10.1016/j.tree.2021.06.002](https://doi.org/10.1016/j.tree.2021.06.002)

[7] Spykman, O., Lowenberg-DeBoer, J., & Gandorfer, M. (2026). Crop robots as potential enablers of economical and biodiversity-smart small-scale farming. *Precision Agriculture*. [https://doi.org/10.1007/s11119-026-10367-0](https://doi.org/10.1007/s11119-026-10367-0)

[8] ISO. (2015). *ISO 11783-10:2015 — Tractors and machinery for agriculture and forestry — Serial control and communications data network — Part 10: Task controller and management information system data interchange*. [https://www.iso.org/standard/61581.html](https://www.iso.org/standard/61581.html)

[9] AgGateway. (2025). *ADAPT Standard 2.0 — Documentation*. [https://adaptstandard.org/docs/](https://adaptstandard.org/docs/)

[10] Agricultural Industry Electronics Foundation (AEF). (s. f.). *Autonomy in Agriculture (AUT) — project team, use cases and work items*. [https://www.aef-online.org/aef-aut/](https://www.aef-online.org/aef-aut/)

[11] Felske, M., Redenius, J., Happich, G., & Schöning, J. (2026). Towards an Agricultural Operational Design Domain: A Framework. *Smart Agricultural Technology*. [https://doi.org/10.1016/j.atech.2026.102246](https://doi.org/10.1016/j.atech.2026.102246)

[12] Holm, S., Pedersen, S. M., & Tamirat, T. W. (2024). Robots in agriculture — A case-based discussion of ethical concerns on job loss, responsibility, and data control. *Smart Agricultural Technology*, 9, 100633. [https://doi.org/10.1016/j.atech.2024.100633](https://doi.org/10.1016/j.atech.2024.100633)

[13] Batey, T. (2009). Soil compaction and soil management — a review. *Soil Use and Management*, 25(4), 335–345. [https://doi.org/10.1111/j.1475-2743.2009.00236.x](https://doi.org/10.1111/j.1475-2743.2009.00236.x)

[14] Stilgoe, J., Owen, R., & Macnaghten, P. (2013). Developing a framework for responsible innovation. *Research Policy*, 42(9), 1568–1580. [https://doi.org/10.1016/j.respol.2013.05.008](https://doi.org/10.1016/j.respol.2013.05.008)

[15] Sustainable Robotics Base for Crops. (2026). *Agri JSON format, version 3 — schema, profiles, vocabularies, indicator registry and documentation*. Licencia CC BY 4.0. [https://github.com/Sustainable-Robotics-Base-for-Crops/json_agri_format](https://github.com/Sustainable-Robotics-Base-for-Crops/json_agri_format)

[16] Parlamento Europeo y Consejo de la Unión Europea. (2023). *Reglamento (UE) 2023/1230, de 14 de junio de 2023, relativo a las máquinas*. [https://eur-lex.europa.eu/eli/reg/2023/1230/oj](https://eur-lex.europa.eu/eli/reg/2023/1230/oj)

[17] ISO. (2024). *ISO 18497, partes 1 a 4 — Agricultural machinery and tractors — Safety of partially automated, semi-autonomous and autonomous machinery*. [https://www.iso.org/standard/82684.html](https://www.iso.org/standard/82684.html)

[18] Prévault-Osmani, A. (2026). *Manifiesto por una robótica agrícola abierta*. Sustainable Robotics Base for Crops. Licencia CC BY 4.0. [https://github.com/Sustainable-Robotics-Base-for-Crops/ecosystem/blob/main/manifesto/MANIFESTO.es.md](https://github.com/Sustainable-Robotics-Base-for-Crops/ecosystem/blob/main/manifesto/MANIFESTO.es.md)

---

## Sobre el autor

**Alexandre Prévault-Osmani**  
CTO y cofundador de SABI AGRI

Ingeniero de profesión y campesino por trayectoria, Alexandre Prévault-Osmani trabaja desde 2015 en la intersección de la electrificación, la robótica agrícola, el Open Source y la agroecología. Participa en el desarrollo del robot SRBC, presentado en este texto como caso de estudio.

**Contacto**

- GitHub: [Alexandre-PO](https://github.com/Alexandre-PO)
- LinkedIn: [alexandre-po](https://www.linkedin.com/in/alexandre-po)

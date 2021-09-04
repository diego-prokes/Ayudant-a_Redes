# Cableado Estructurado

[TOC]



## Definición

El cableado estructurado es tal y como la palabra lo indica un tipo de cableado, el cuál debe seguir la norma TIA/EIA 568 para considerarse bien instalado. Se utiliza en edificio o recintos, con el objetivo de implantar una red de telecomunicaciones de área local que permita un intercambio de información veloz entre los computadores computadores conectados a ella.

Esta estructura contiene una combinación de cables trenzados (UTP/STP/FTP) , fibras ópticas (FO) y/o cables coaxiales, conectores, canalizaciones y otros dispositivos. Ellos deben cumplir ciertos estándares universales para que puedan ser fácilmente entendidos por instaladores, administradores de redes y cualquier otro técnico que trabaje con ellos.

## Elementos de cableado estructurado

A la hora de instalar el cableado estructurado de una red de área local, red LAN, se deben tener en consideración las características y el diseño del lugar en el que se va a instalar. También es importante considerar el crecimiento futura de dicha instalación, por lo que la cantidad y la capacidad de los cables seleccionados ha de satisfacer las necesidades de ampliación futuras.

### Cableado horizontal

La norma del [EIA](https://es.wikipedia.org/wiki/Electronic_Industries_Alliance)/[TIA](https://es.wikipedia.org/w/index.php?title=Telecommunications_in_Industry_Association&action=edit&redlink=1) 568A define el cableado horizontal de la siguiente forma: el sistema de cableado horizontal es la porción del sistema de cableado de telecomunicaciones que se extiende del área de trabajo al cuarto de telecomunicaciones o viceversa.

El cableado horizontal se compone de dos elementos básicos: rutas y espacios verticales (también llamado "sistemas de pasada de datos horizontal"). Las rutas y espacios horizontales son utilizados para distribuir y soportar cable horizontal y conectar hardware entre la salida del área de trabajo y el cuarto de telecomunicaciones. Estas rutas y espacios son los "contenedores" del cableado horizontal.

1. Si existiera cielo raso suspendido se recomienda la utilización de canaletas para transportar los cables horizontales.
2. Una tubería de ¾ [pulgadas](https://es.wikipedia.org/wiki/Pulgada) por cada dos cables UTP.
3. Una tubería de 1 pulgada por cada cable de dos fibras ópticas.
4. Los radios mínimos de curvatura deben ser bien implementados.

El cableado horizontal incluye:

- Las salidas (cajas/placas/conectores) de telecomunicaciones en el área de trabajo (en inglés: *work area outlets*, **WAO**).
- Cables y conectores de transición instalados entre las salidas del área de trabajo y el cuarto de telecomunicaciones.
- Paneles (*patch panels*) y cables de empalme utilizados para configurar las conexiones de cableado horizontal en el cuarto de telecomunicaciones.

Se deben hacer ciertas consideraciones a la hora de seleccionar el cableado horizontal: contiene la mayor cantidad de cables individuales en el edificio.

#### Consideraciones de diseño

Los costes en materiales, mano de obra e interrupción de labores al hacer cambios en el cableado horizontal pueden ser muy altos. Para evitar estos costes, el cableado horizontal debe ser capaz de manejar una amplia gama de aplicaciones de usuario. La distribución horizontal debe ser diseñada para facilitar el mantenimiento y la relocalización de áreas de trabajo. El diseñador también debe considerar incorporar otros sistemas de información del edificio (por ej. televisión por cable, control ambiental, seguridad, audio, alarmas y sonido) al seleccionar y diseñar el cableado horizontal.

#### Topología

La norma EIA/TIA 568A hace las siguientes recomendaciones en cuanto a la topología del cableado horizontal:

- El cableado horizontal debe seguir una topología estrella.
- Cada toma/conector de telecomunicaciones del área de trabajo debe conectarse a una interconexión en el cuarto de telecomunicaciones.

La distancia horizontal máxima no debe exceder 90 m. La distancia se mide desde la terminación mecánica del medio en la interconexión horizontal en el cuarto de telecomunicaciones hasta la toma/conector de telecomunicaciones en el área de trabajo. Además se recomiendan las siguientes distancias: se separan 10 m para los cables del área de trabajo y los cables del cuarto de telecomunicaciones (cordones de parcheo, [*jumpers*](https://es.wikipedia.org/wiki/Jumper_(informática)) y cables de equipo).

#### Medios reconocidos

Se reconocen cinco tipos de cable para el sistema de cableado horizontal:

- Cables de [par trenzado sin blindar](https://es.wikipedia.org/wiki/Unshielded_Twisted_Pair) (UTP) de 100 [ohmios](https://es.wikipedia.org/wiki/Ohmio) y cuatro pares.
- Cables de [par trenzado apantallado](https://es.wikipedia.org/w/index.php?title=Foiled_Twisted_Pair&action=edit&redlink=1) (FTP) de 120 [ohmios](https://es.wikipedia.org/wiki/Ohmio) y cuatro pares.
- Cables de [par trenzado blindado](https://es.wikipedia.org/wiki/Shielded_Twisted_Pair) (STP) de 150 [ohmios](https://es.wikipedia.org/wiki/Ohmio) y cuatro pares.
- Cables de [fibra óptica](https://es.wikipedia.org/wiki/Fibra_óptica) multimodo de 62.5/125 μm y 50/125 μm.
- Cables de [fibra óptica](https://es.wikipedia.org/wiki/Fibra_óptica) monomodo de 9/125 μm.

### Cableado vertical o *backbone*

El sistema de cableado vertical proporciona interconexiones entre cuartos de entrada y servicios del edificio, cuartos de equipos y cuartos de telecomunicaciones. El cableado del *backbone* incluye la conexión vertical (Las canalizaciones Backbone pueden ser verticales u horizontales) entre pisos en edificios de varios pisos. El cableado del *backbone* incluye medios de transmisión (cables), puntos principales e intermedios de conexión cruzada y terminaciones mecánicas. El cableado vertical realiza la interconexión entre los diferentes gabinetes de telecomunicaciones y entre estos y la sala de equipamiento. En este componente del sistema de cableado ya no resulta económico mantener la estructura general utilizada en el cableado horizontal, sino que es conveniente realizar instalaciones independientes para la telefonía y datos. Esto se ve reforzado por el hecho de que, si fuera necesario sustituir el *backbone*, ello se realiza con un coste relativamente bajo, y causando muy pocas molestias a los ocupantes del edificio. El *backbone* telefónico se realiza habitualmente con cable telefónico multipar. Para definir el *backbone* de datos es necesario tener en cuenta cuál será la disposición física del equipamiento. Normalmente, el tendido físico del *backbone* se realiza en forma de estrella, es decir, se interconectan los gabinetes con uno que se define como centro de la estrella, en donde se ubica el equipamiento electrónico más complejo.

El *backbone* de datos se puede implementar con cables UTP y/o con fibra óptica. En el caso de decidir utilizar UTP, el mismo será de categoría 5e, 6 o 6A y se dispondrá un número de cables desde cada gabinete al gabinete seleccionado como centro de estrella.

Actualmente, la diferencia de coste provocada por la utilización de fibra óptica se ve compensada por la mayor flexibilidad y posibilidad de crecimiento que brinda esta tecnología. Se construye el *backbone* llevando un cable de fibra desde cada gabinete al gabinete centro de la estrella. Si bien para una configuración mínima Ethernet basta con utilizar cable de dos fibras, resulta conveniente utilizar cable con mayor cantidad de fibras (6 a 12) ya que la diferencia de coste no es importante y se posibilita por una parte disponer de conductores de reserva para el caso de falla de algunos, y por otra parte, la utilización en el futuro de otras topologías que requieren más conductores, como FDDI o sistemas resistentes a fallas. La norma EIA/TIA 568 prevé la ubicación de la transmisión de cableado vertical a horizontal, y la ubicación de los dispositivos necesarios para lograrla, en habitaciones independientes con puerta destinada a tal fin, ubicadas por lo menos una por piso, denominadas armarios de telecomunicaciones. Se utilizan habitualmente gabinetes estándar de 19 pulgadas de ancho, con puertas, de aproximadamente 50 cm de profundidad y de una altura entre 1,5 y 2 metros. En dichos gabinetes se dispone generalmente de las siguientes secciones:

- Acometida de los puestos de trabajo: dos cables UTP llegan desde cada puesto de trabajo.
- Acometida del *backbone* telefónico: cable multipar que puede terminar en regletas de conexión o en *patch panels*.
- Acometida del *backbone* de datos: cables de fibras ópticas que se llevan a una bandeja de conexión adecuada.

### Cuarto de entrada de servicios de cableado

- En cables, accesorios de conexión, dispositivos de protección, y demás equipos es necesario para conectar el edificio a servicios externos. Puede contener el punto de demarcación. Ofrecen protección eléctrica establecida por códigos eléctricos aplicables. Deben ser diseñadas de acuerdo a la norma EIA/TIA-569-A. Los requerimientos de instalación son:
  - Precauciones en el manejo del cable UTP
  - Evitar tensiones en el cable
  - Los cables no deben en rutarse en grupos muy apretados
  - Utilizar rutas de cable y accesorios apropiados 100 ohmios UTP y STP
  - No giros con un ángulo menor de 90.

### Sistema de puesta a tierra

El sistema de puesta a tierra y puenteo establecido en estándar ANSI/TIA/EIA-607 es un componente importante de cualquier sistema de cableado estructurado moderno. El gabinete deberá disponer de una toma de tierra, conectada a la tierra general de la instalación eléctrica, para efectuar las conexiones de todo equipamiento. El conducto de tierra no siempre se halla indicado en planos y puede ser único para ramales o circuitos que pasen por las mismas cajas de pase, conductos o bandejas. Los cables de tierra de seguridad serán puesto.

### Velocidad según la categoría de la red

Artículo principal: *[Cable de par trenzado](https://es.wikipedia.org/wiki/Cable_de_par_trenzado)*

- [categoría 1](https://es.wikipedia.org/wiki/Cable_de_Categoría_1): se utiliza para comunicaciones telefónicas y no es adecuado para la transmisión de datos ya que sus velocidades no alcanzan los 512 [kbit](https://es.wikipedia.org/wiki/Kbit)/s.

- [categoría 2](https://es.wikipedia.org/wiki/Cable_de_Categoría_2): puede transmitir datos a velocidades de hasta 4 [Mbit](https://es.wikipedia.org/wiki/Mbit)/s.

- [categoría 3](https://es.wikipedia.org/wiki/Cable_de_Categoría_3): se utiliza en redes 10BaseT y puede transmitir datos a velocidades de hasta 10 Mbit/s.

- [categoría 4](https://es.wikipedia.org/wiki/Cable_de_Categoría_4): se utiliza en redes Token Ring y puede transmitir datos a velocidades de hasta 16 Mbit/s.

- [categoría 5](https://es.wikipedia.org/wiki/Cable_de_Categoría_5): puede transmitir datos a velocidades de hasta 100 Mbit/s.

- [categoría 5e](https://es.wikipedia.org/wiki/Cable_de_Categoría_5e): puede transmitir datos a velocidades de hasta 1000 Mbit/s.

- [categoría 6](https://es.wikipedia.org/wiki/Cable_de_categoría_6): Redes de alta velocidad hasta 1 [Gbit](https://es.wikipedia.org/wiki/Gbit)/s.

- [categoría 6A](https://es.wikipedia.org/wiki/Cable_de_categoría_6): Redes de alta velocidad hasta 10 Gbit/s.

- [categoría 7](https://es.wikipedia.org/wiki/Cable_de_Categoría_7): Redes de alta velocidad de hasta 10 Gbit/s y frecuencias hasta 600 MHz

- [categoría 7A](https://es.wikipedia.org/wiki/Cable_de_categoría_7A): Redes de alta velocidad de hasta 10 Gbit/s y frecuencias hasta 1000 MHz

- [categoría 8](https://es.wikipedia.org/w/index.php?title=Cable_de_categoría_8&action=edit&redlink=1): Redes de alta velocidad de hasta 40 Gbit/s y frecuencias hasta 2000 MHz

## Imagen de ejemplo

  <img src="./1 assets/1 Cableado Estructurado.png" style="zoom: 50%;" />

## Bibliogrfía

[Conoce los diferentes Tipos de Cableado Estructurado (termired.com)](https://termired.com/conoce-los-diferentes-tipos-de-cableado-estructurado/)

[¿Qué es el Cableado Estructurado y por qué es importante? - TIP Engineer](http://www.tipengineer.com/categoria-blog/telecomunicaciones-categoria-blog/que-es-el-cableado-estructurado-y-por-que-es-importante/)

[Cableado estructurado - Wikipedia, la enciclopedia libre](https://es.wikipedia.org/wiki/Cableado_estructurado)

[Difference Between TIA/EIA 568A and TIA/EIA 568B (antaira.com)](https://www.antaira.com/Blog-Difference-Between-TIA-EIA-68A-and-TIA-EIA-568B)

[TIA-568B - Wikipedia, la enciclopedia libre](https://es.wikipedia.org/wiki/TIA-568B)

[ANSI/TIA-568 - Wikipedia](https://en.wikipedia.org/wiki/ANSI/TIA-568)

[Norma EIA: ¿En qué consiste, por qué surge y a quién afecta? (atlascomunicaciones.com)](https://atlascomunicaciones.com/norma-eia/)

[¿Cuál es el propósito de la norma EIA/TIA 568A? - Página web de elcapored (jimdofree.com)](https://elcapored.jimdofree.com/normas-568a-568b/)

[Todo lo que necesitas saber sobre el cableado estructurado | CadLan](https://www.cadlan.com/noticias/todo-lo-que-debes-saber-sobre-el-cableado-estructurado/)
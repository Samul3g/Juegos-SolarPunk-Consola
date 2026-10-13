import random 
cheats = False
piso_actual = 0
celda_actual = 0
cantidad_preguntas = 5
largo_pisos = 10
cantidad_pisos = 4

preguntas_piso1 = [

    [
    ['¿Cuál es la principal fuente de energía'
    +' en una matriz energética sostenible solarpunk?'],
    ['El Sol, porque llega cada mañana sin necesidad'
    +' de quemar nada.'],
    ['El carbón, porque es barato y abundante.'],
    ['El petróleo, porque mueve la mayoría de los autos.'],
    ['El gas natural, porque contamina menos que el carbón.']
    ],

    [
    ['¿Dónde se pueden instalar paneles solares'
    +'en una ciudad solarpunk?'],
    ['En techos de casas, balcones, estacionamientos'
    +' y hasta paradas de autobús.'],
    ['Solo en enormes plantas en medio del desierto.'],
    ['Solo en techos de fábricas y centros comerciales.'],
    ['No se instalan en ciudades porque ocupan mucho espacio.']
    ],

    [
    ['¿Qué pasa con los paneles solares cuando'
    +' dejan de funcionar después de muchos años?'],
    ['Se pueden reciclar casi por completo y'
    +' reutilizar sus materiales.'],
    ['Se entierran en rellenos sanitarios como basura común.'],
    ['Se queman para generar energía.'],
    ['Se exportan a otros países como desecho.']
    ],

    [
    ['¿Cómo se almacena la energía solar para usarla de noche?'],
    ['En baterías o sistemas sencillos como agua elevada'
    +' o rocas calentadas.'],
    ['En enormes pilas de carbón.'],
    ['En tanques de petróleo crudo.'],
    ['No se puede almacenar, sólo se usa de día.']
    ],

    [
    ['¿Por qué la energía solar es más justa'
    +' para los países sin petróleo?'],
    ['Porque les permite ser energéticamente'
    +' independientes sin depender de nadie.'],
    ['Porque pueden comprar paneles más baratos que el combustible.'],
    ['Porque el Sol brilla más en países sin petróleo.'],
    ['Porque los paneles los regalan las naciones ricas.']
    ],

    [
    ['¿Qué característica tiene la energía solar comparada'
    +' con el carbón o el petróleo?'],
    ['No contamina el aire ni el agua mientras genera electricidad.'],
    ['Contamina menos, pero igual requiere chimeneas.'],
    ['Solo funciona en verano y en lugares despejados.'],
    ['Es más cara y menos eficiente que los combustibles fósiles.']
    ]

]

preguntas_piso2 = [
    [
    ['¿Cuál medio de transporte tiene prioridad en las'
    +' calles de una ciudad solarpunk?'],
    ['Los peatones y las bicicletas.'],
    ['Los automóviles particulares.'],
    ['Las motocicletas de alto cilindraje.'],
    ['Los camiones de carga pesada.']
    ],
    
    [
    ['¿Cómo se mueve el transporte público en una ciudad solarpunk?'],
    ['Con electricidad limpia (tranvías, autobuses eléctricos).'],
    ['Con diésel, porque es más potente y rápido.'],
    ['Con gas natural comprimido.'],
    ['Con autos particulares compartidos entre vecinos de la comunidad.']
    ],

    [
    ['¿Qué son las “bicicletas de carga"?'],
    ['Bicicletas con un remolque o cajón para transportar mercancías.'],
    ['Bicicletas que pesan más de 50 kilos.'],
    ['Bicicletas que solo usan los repartidores profesionales.'],
    ['Bicicletas que funcionan con cargas de combustible o carbón.']
    ],

    [
    ['¿Qué se ha hecho con los viejos estacionamientos en una ciudad solarpunk?'],
    ['Se han convertido en parques, huertos o plazas.'],
    ['Siguen siendo estacionamientos, pero más pequeños.'],
    ['Se usan para depositar basura reciclable.'],
    ['Siguen vacíos esperando más autos.']
    ],

    [
    ['¿Qué es el concepto de “ciudad de 15 minutos”?'],
    ['Que todo lo necesario está a 15 minutos caminando de tu casa.'],
    ['Que los autos puedan cruzar la ciudad en 15 minutos.'],
    ['Que cada 15 minutos pasa un tranvía o autobús de energía renovable.'],
    ['Que las calles se cierran cada 15 minutos para peatones.']
    ],

    [
    ['¿Qué se entiende del concepto “taxis eléctricos compartidos”?'],
    ['Taxis que varios pasajeros usan siguiendo'
    +' rutas similares para abaratar costos.'],
    ['Taxis que solo llevan turistas.'],
    ['Taxis que funcionan con gasolina pero son pequeños.'],
    ['Taxis que se mueven con pedales.']
    ]
    
]

preguntas_piso3 = [

    [
    ['¿Qué es un “tercer espacio” en el solarpunk?'],
    ['Un lugar que no es tu casa ni tu trabajo, donde puedes estar sin pagar.'],
    ['Un centro comercial donde todo es gratis.'],
    ['Una discoteca con entrada libre.'],
    ['Un lugar exclusivo para socios con membresía.']
    ],

    [
    ['¿Qué se puede hacer con una “biblioteca de cosas”?'],
    ['Tomar prestadas herramientas, ollas, juegos o'
    +' equipos que no usas a diario.'],
    ['Leer libros prestados, como en cualquier biblioteca.'],
    ['Comprar electrodomésticos nuevos a bajo precio.'],
    ['Vender tus cosas usadas.']
    ],

    [
    ['¿Qué tienen en común los terceros espacios solarpunk?'],
    ['Todos son gratuitos o accesibles sin necesidad de consumir.'],
    ['Todos venden comida y bebida.'],
    ['Todos requieren reserva anticipada.'],
    ['Todos están cerrados los fines de semana.']
    ],

    [
    ['¿Qué puedes encontrar en una plaza solarpunk?'],
    ['Bancos, sombra, enchufes solares, mesas de'
    +' ajedrez y libros para intercambiar.'],
    ['Solo pasto y un monumento.'],
    ['Máquinas expendedoras y casetas de vigilancia.'],
    ['Estacionamiento para autos y motos.']
    ],

    [
    ['¿Qué son los "bancos de semillas"?'],
    ['Lugares donde se guardan semillas para'
    +' intercambiar o compartir con otros.'],
    ['Bancos normales que ofrecen préstamos para comprar semillas.'],
    ['Depósitos donde se almacenan semillas modificadas genéticamente.'],
    ['Lugares donde se venden semillas raras muy caras.']
    ],

    [
    ['¿Qué característica deben tener los terceros espacios'
    +' para ser inclusivos?'],
    ['Estar diseñados para que alguien en silla de ruedas pueda'
    +' moverse sin problemas.'],
    ['Tener escaleras anchas y muchos adornos.'],
    ['Estar ubicados en las afueras de la ciudad.'],
    ['Tener entrada con torniquetes y control de acceso.']
    ]
    
]

preguntas_piso4 = [

    [
    ['¿Cómo se controlan las plagas en una agricultura sostenible solarpunk?'],
    ['Plantando flores o hierbas que ahuyentan plagas y'
    +' atraen insectos útiles.'],
    ['Con venenos químicos potentes.'],
    ['Con insecticidas de última generación.'],
    ['Quemando los cultivos afectados.']
    ],

    [
    ['¿Dónde se puede cultivar en una ciudad solarpunk?'],
    ['En techos, balcones, paredes y huertos comunitarios.'],
    ['Solo en el campo, lejos de las ciudades.'],
    ['Solo en invernaderos gigantes con calefacción.'],
    ['En sótanos sin luz natural.']
    ],

    [
    ['¿Qué se hace con los residuos de comida en la agricultura sostenible?'],
    ['Se convierten en abono (composta) para la misma tierra.'],
    ['Se tiran a la basura común.'],
    ['Se queman para generar energía.'],
    ['Se entierran en rellenos sanitarios.']
    ],

    [
    ['¿Por qué las verduras no tienen formas perfectas en el solarpunk?'],
    ['Porque no se usan químicos para forzar su apariencia y eso está bien.'],
    ['Porque los agricultores son descuidados.'],
    ['Porque las semillas son de mala calidad.'],
    ['Porque solo se cultivan variedades feas.']
    ],

    [
    ['¿Qué rol tienen las lombrices en la agricultura sostenible?'],
    ['Son bienvenidas porque airean la tierra y la hacen más rica.'],
    ['Son una plaga que hay que eliminar.'],
    ['Solo sirven como comida para gallinas.'],
    ['No tienen ninguna función importante.']
    ],

    [
    ['¿Qué aprenden los niños en las escuelas solarpunk sobre agricultura?'],
    ['A sembrar y cuidar su propio huerto escolar.'],
    ['A usar tractores y fertilizantes químicos.'],
    ['A trabajar en grandes plantaciones industriales.'],
    ['Solo teoría, sin práctica.']
    ]
    
]

preguntas_piso5 = [

    [
    ['¿Qué es un "banco de tiempo"?'],
    ['Un sistema donde cambias una hora de tu ayuda'
    +' por una hora de ayuda de otro.'],
    ['Un banco donde guardas dinero para jubilarte.'],
    ['Un reloj comunitario que marca la hora oficial.'],
    ['Un lugar donde te pagan por esperar.']
    ],

    [
    ['¿Qué puedes hacer en un mercado de trueque solarpunk?'],
    ['Cambiar lo que te sobra por lo que necesitas sin usar dinero.'],
    ['Comprar productos con dinero.'],
    ['Vender tus cosas usadas a bajo precio.'],
    ['Solo recibir regalos, no dar nada.']
    ],

    [
    ['¿Cómo se mide el éxito de una empresa en una economía alternativa'
    +' solarpunk?'],
    ['Por el bienestar que genera en la comunidad y el ambiente.'],
    ['Solo por las ganancias que obtiene.'],
    ['Por la cantidad de empleados que tiene.'],
    ['Por el número de productos que vende.']
    ],

    [
    ['¿Qué son las "monedas locales"?'],
    ['Dinero que solo sirve en un barrio o ciudad para fomentar el'
    +' comercio cercano.'],
    ['Monedas de colección que no tienen valor real.'],
    ['Billetes falsos que usan los turistas.'],
    ['Dinero digital que solo funciona en internet.']
    ],

    [
    ['¿Qué significa que un producto esté diseñado para repararse fácilmente?'],
    ['Que se puede desarmar y arreglar con herramientas comunes en lugar'
    +' de tirarlo.'],
    ['Que el fabricante ofrece un servicio técnico caro.'],
    ['Que incluye un manual de 500 páginas.'],
    ['Que solo lo puede reparar el fabricante.']
    ],

    [
    ['Según la economía solarpunk, ¿qué es la verdadera "riqueza"?'],
    ['Tener tiempo, salud, amigos y un entorno limpio.'],
    ['Tener mucho dinero en el banco.'],
    ['Poseer muchos bienes materiales.'],
    ['Ser famoso y reconocido.']
    ]
    
]

pistas_piso1 = [

    'No necesita quemar nada para funcionar.',
    'La fuente principal llega cada mañana con el Sol.',
    'Los techos de las casas se convierten en pequeñas centrales eléctricas.',
    'Puede funcionar en un pueblo remoto sin necesidad de grandes torres'
    +' de alta tensión.',
    'Los vecinos pueden compartir el sobrante de energía entre sí.',
    'No contamina el aire ni el agua mientras genera electricidad.',
    'Las "baterías" pueden ser tan simples como agua elevada en un tanque'
    +' o rocas calentadas.',
    'Un panel solar sigue produciendo aunque esté nublado, solo que un'
    +' poco menos.',
    'Las fábricas que la producen también funcionan con energía limpia.',
    'Los materiales se pueden reciclar casi por completo al final de su'
    +' vida útil.',
    'No genera guerras por petróleo ni conflictos por minería tóxica.',
    'Cualquier persona con un balcón soleado puede generar su propia'
    +' electricidad.',
    'Los grandes proyectos se instalan en techos, estacionamientos o'
    +' desiertos, no en bosques ni ríos sagrados.',
    'El mantenimiento es sencillo: limpiar el polvo de vez en cuando.',
    'No produce residuos radiactivos que duren miles de años.',
    'La misma superficie que usas para estacionar un auto puede dar'
    +' energía a tres casas.',
    'Los niños en la escuela aprenden a leer la producción solar como'
    +' quien ve un termómetro.',
    'En lugares sin red eléctrica, esta matriz permite tener luz,'
    +' nevera y escuela por primera vez.',
    'Los aparatos eléctricos se programan para funcionar cuando hay'
    +' más Sol (y sobra energía).',
    'No hay chimeneas, ni humo, ni olor, ni ruido molesto.',
    'Se puede combinar con plantas que cultivan alimentos debajo'
    +' de los paneles.',
    'Una sola hora de Sol sobre la Tierra da más energía de la'
    +' que consume toda la humanidad en un año.',
    'Los países sin petróleo pueden ser independientes energéticamente'
    +' gracias a ella.',
    'Los paneles duran más de 25 años y luego se reutilizan para otras'
    +' funciones.',
    'Los postes de luz y las paradas de autobús pueden generar su'
    +' propia electricidad.',
    'Una nevera comunitaria en un barrio puede funcionar con el techo'
    +' solar de la plaza.',
    'El costo de generación ha bajado tanto que ya es más barata que'
    +' el carbón en muchos lugares.',
    'No necesita camiones cisterna, ni oleoductos, ni barcos tanque.',
    'Puede alimentar desde un cargador de celular hasta una fábrica entera.',
    'Es una matriz que no le roba futuro a las siguientes generaciones'
         
]

pistas_piso2 = [

    'La gente camina sin miedo porque las calles son seguras y agradables.',
    'Las bicicletas tienen vías propias, protegidas del tráfico de autos.',
    'Los niños pueden ir solos a la escuela sin necesidad de que los lleven'
    +' en coche.',
    'Las aceras son anchas, con sombra y bancos para descansar cada dos'
    +' cuadras.',
    'Los autos particulares son la excepción, no la regla.',
    'En cada esquina hay una estación de bicicletas compartidas en buen'
    +' estado.',
    'Los tranvías y autobuses pasan cada pocos minutos y funcionan con'
    +' electricidad limpia.',
    'Las calles tienen prioridad para peatones, después bicicletas,'
    +' después transporte público, y al final autos.',
    'Puedes cruzar la ciudad entera sin usar un automóvil privado.',
    'Las paradas de autobús tienen paneles solares que cargan tu celular'
    +' mientras esperas.',
    'Los pocos autos que circulan son eléctricos, pequeños y a menudo'
    +' compartidos entre vecinos.',
    'Las bicicletas de carga sustituyen a las furgonetas para repartir'
    +' mercancías.',
    'Las calles escolares se cierran al tráfico en horas de entrada y salida.',
    'Los estacionamientos se han convertido en parques, huertos o plazas.',
    'Las patinetas, patines y monociclos eléctricos son medios comunes para'
    +' distancias cortas.',
    'Las rampas y superficies táctiles hacen que todo sea accesible para'
    +' sillas de ruedas y carritos.',
    'Los vecinos organizan "bicibus": niños van juntos en bici acompañados'
    +' por adultos.',
    'Puedes mover una nevera o un mueble en una bicicleta de carga que te'
    +' presta el ayuntamiento.',
    'Las estaciones de tren ligero tienen taquillas para dejar tu bici'
    +' de forma segura.',
    'Las calles tienen límites de velocidad de 30 km/h o menos en zonas'
    +' residenciales.',
    'Las aceras y ciclovías se limpian de nieve o basura antes que las'
    +' calzadas para autos.',
    'Los pasos peatonales están elevados al mismo nivel que la acera,'
    +' para que los autos frenen por diseño.',
    'Las farolas tienen sensores que iluminan más cuando pasa un peatón'
    +' o ciclista de noche.',
    'Las aplicaciones de movilidad te muestran la ruta más rápida en bici'
    +' o transporte público, no en auto.',
    'Los repartos de paquetes se hacen con triciclos eléctricos o carritos'
    +' manuales.',
    'Las plazas de aparcamiento para autos se han reducido y convertido'
    +' en terrazas, árboles o cargadores de bicis.',
    'Las ciudades están diseñadas para que todo lo necesario esté a'
    +' 15 minutos caminando de tu casa.',
    'Los taxis son eléctricos, se comparten con otros pasajeros de'
    +' ruta similar y son más baratos.',
    'Los semáforos dan prioridad peatonal y las esperas son cortas.',
    'La movilidad no es un lujo: es un derecho accesible para todos,'
    +' sin importar la edad ni los ingresos.'

]

pistas_piso3 = [

    'No es tu casa ni tu trabajo, pero es un lugar donde te sientes'
    +' bienvenido.',
    'Puedes estar horas sin que nadie te pida que consumas algo.',
    'Hay bancos, sombra y agua gratis disponible.',
    'Los vecinos se encuentran ahí sin necesidad de planificarlo.',
    'Las bibliotecas públicas tienen sillones cómodos, luz natural y plantas.',
    'Existen talleres comunitarios donde puedes reparar tu bicicleta'
    +' o tostadora.',
    'Los huertos urbanos son también lugares para sentarse a conversar.',
    'Las plazas tienen mesas de ajedrez, juegos de mesa y libros para'
    +' intercambiar.',
    'Puedes llevarte una silla a la sombra de un árbol y leer sin que'
    +' te molesten.',
    'Los centros culturales ofrecen talleres gratuitos o a cambio de'
    +' ayudar en la limpieza.',
    'Hay baños públicos limpios y gratuitos en muchos puntos de la ciudad.',
    'Los techos de algunos edificios son terrazas abiertas con macetas'
    +' y bancos.',
    'Las paradas de transporte tienen refugio, asientos y a veces una'
    +' pequeña biblioteca.',
    'Las lavanderías comunitarias tienen un rincón con revistas y café'
    +' de cooperativa.',
    'Los mercados locales tienen zonas de estar cubiertas donde puedes'
    +' comer tu propia comida.',
    'Las iglesias o templos, cuando no hay ceremonia, están abiertos'
    +' como espacios de silencio y paz.',
    'Las esquinas abandonadas se convierten en mini huertos o placitas'
    +' con una banca.',
    'Los colegios abren sus patios los fines de semana para que jueguen'
    +' niños de todo el barrio.',
    'Hay "bibliotecas de cosas": prestan herramientas, ollas, juegos,'
    +' carpas, lo que necesites.',
    'Los cafés y bares existen, pero también hay mesas comunitarias'
    +' donde no hace falta comprar.',
    'Los pasillos cubiertos entre edificios tienen bancos y plantas,'
    +' invitan a quedarse.',
    'Los parques tienen mesas de picnic y parrillas que cualquier'
    +' vecino puede usar.',
    'Hay espacios para ensayar música en grupo sin molestar a nadie.',
    'Los centros de adultos mayores están abiertos también para jóvenes'
    +' que quieran aprender oficios.',
    'Las plazas tienen enchufes solares para cargar el celular mientras'
    +' charlas.',
    'Los jardines comunitarios tienen un cobertizo con techo donde'
    +' refugiarse si llueve.',
    'Las paredes de algunos espacios tienen pizarras para dejar mensajes'
    +' o dibujar.',
    'Hay "bancos de semillas" donde puedes dejar semillas y llevarte otras.',
    'Los espacios están diseñados para que alguien en silla de ruedas pueda'
    +' moverse sin problemas.',
    'No necesitas dinero, membresía ni permiso para entrar y quedarte un'
    +' rato.'

]

pistas_piso4 = [

    'La comida crece cerca de donde vive la gente, no a miles de kilómetros.',
    'No se usan venenos químicos que matan insectos o enfermen a quien la'
    +' cultiva.',
    'La tierra se cuida para que siga siendo fértil por muchos años.',
    'El agua de lluvia se recolecta y se usa con cuidado, sin desperdiciarla.',
    'Los cultivos se mezclan: flores, verduras y árboles crecen juntos como'
    +' en un bosque.',
    'Los residuos de comida se convierten en abono para la misma tierra.',
    'Hay animales como gallinas o conejos que comen restos y dan abono'
    +' natural.',
    'Las plantas que ahuyentan plagas crecen al lado de los cultivos,'
    +' sin necesidad de insecticidas.',
    'Se usan semillas locales que los mismos agricultores guardan de una'
    +' cosecha a otra.',
    'Los cultivos crecen en techos, balcones y paredes, no solo en el campo.',
    'Las lombrices son bienvenidas: ellas airean la tierra y la hacen más'
    +' rica.',
    'Las verduras no tienen formas perfectas ni tamaños idénticos, y eso'
    +' está bien.',
    'En lugar de arar y dejar la tierra desnuda, se cubre con hojas secas'
    +' para protegerla.',
    'Los árboles dan sombra a los cultivos más pequeños y ayudan a retener'
    +' el agua.',
    'Las huertas comunitarias son cuidadas entre vecinos, no por una sola'
    +' familia.',
    'El riego se hace por goteo o con mangueras que echan agua justo donde'
    +' hace falta, no al aire.',
    'Las mal llamadas "malas hierbas" a veces se dejan porque atraen'
    +' insectos útiles.',
    'Se cultivan variedades antiguas de maíz, tomate o frijol que ya'
    +' casi nadie vendía.',
    'Los invernaderos pequeños usan la luz del sol sin plásticos de un'
    +' solo uso.',
    'La tierra se regenera, no se empobrece ni se erosiona.',
    'Los agricultores urbanos pueden vivir de lo que producen sin endeudarse.',
    'El estiércol de animales criados cerca se usa como fertilizante natural.',
    'Las ferias de trueque permiten cambiar zanahorias por pan o lechugas'
    +' por huevos.',
    'Los niños en las escuelas tienen su propio huerto y aprenden a sembrar.',
    'No se desperdicia comida porque lo que no se vende se reparte o se'
    +' abona.',
    'Las abejas, mariposas y otros polinizadores tienen flores todo el año'
    +' para comer.',
    'Se puede cultivar en espacios muy pequeños: macetas, botellas'
    +' recicladas o mesas hidropónicas.',
    'El trabajo es variado y no agotador: se alternan tareas como en'
    +' un jardín.',
    'Los cultivos de estación son los que se comen: fresas en primavera,'
    +' calabazas en otoño.',
    'La agricultura no destruye el bosque, sino que convive con él.'

]

pistas_piso5 = [

    'No necesitas dinero para conseguir algo que necesitas.',
    'Puedes intercambiar una hora de tu tiempo ayudando a alguien por'
    +' una hora de ayuda para ti.',
    'Las herramientas, electrodomésticos y libros se prestan como si'
    +' fueran de la biblioteca.',
    'Lo que tú ya no usas, otra persona lo puede aprovechar.',
    'Hay monedas locales que solo sirven en el barrio y fomentan el'
    +' comercio cercano.',
    'Reparar algo viejo sale más barato y es más divertido que comprar'
    +' uno nuevo.',
    'Los talleres de costura, electrónica o carpintería están abiertos'
    +' para que cualquiera aprenda a reparar.',
    'Los productos no vienen envueltos en plástico ni capas innecesarias.',
    'Las empresas no fabrican cosas que se rompan a propósito.',
    'Los vecinos organizan mercados donde todo se regala y cada quien'
    +' toma lo que necesita.',
    'Puedes pagar una comida ayudando a lavar los platos o barriendo el'
    +' local.',
    'Las plataformas digitales conectan a quien ofrece un servicio con'
    +' quien lo necesita, sin cobrar comisión.',
    'Los bancos de tiempo tienen catálogos: arreglar una fuga, cuidar'
    +' niños, dar clases de guitarra.',
    'Los muebles viejos se restauran en lugar de tirarse a la basura.',
    'Las familias tienen todo lo que necesitan sin acumular cosas que'
    +' nunca usan.',
    'Los niños cambian su ropa y juguetes usados por otros cuando les'
    +' quedan pequeños.',
    'Las farmacias comunitarias prestan aparatos como muletas o'
    +' nebulizadores.',
    'Un grupo de vecinos compra una máquina cara (como una cortadora'
    +' de césped) y la usan entre todos.',
    'Las sobras de comida de restaurantes se reparten al final del día,'
    +' no se tiran.',
    'Los conocimientos se comparten gratis: alguien enseña a tejer,'
    +' otro a cambiar un enchufe.',
    'No hay publicidad que te haga sentir que necesitas algo nuevo'
    +' cada semana.',
    'Las empresas miden su éxito por el bienestar que generan, no solo'
    +' por las ganancias.',
    'Los ancianos son muy valorados porque tienen habilidades que los'
    +' jóvenes quieren aprender.',
    'Puedes "pagar" una consulta médica cuidando el huerto del centro'
    +' de salud.',
    'Los residuos de una actividad son la materia prima de otra'
    +' (nada se desperdicia).',
    'Los electrodomésticos se diseñan para que se puedan desarmar'
    +' fácilmente y reciclar sus partes.',
    'Hay ferias donde cambias lo que te sobra (tuercas, ropa, libros)'
    +' sin que intervenga el dinero.',
    'Los bancos convencionales ya no son necesarios porque el crédito'
    +' se da entre vecinos con confianza.',
    'El objetivo no es crecer sin límites, sino que todas las personas'
    +' vivan bien con lo que hay.',
    'La palabra "riqueza" significa tener tiempo, salud, amigos y un'
    +' entorno limpio, no solo dinero.'

]


biblioteca = []
preguntas = [preguntas_piso1, preguntas_piso2, preguntas_piso3, preguntas_piso4, preguntas_piso5]
pistas = [pistas_piso1, pistas_piso2, pistas_piso3, pistas_piso4, pistas_piso5]


def generar_biblioteca(largo, largo_pisos):
    """Función que genera cuantas capsulas de pistas hay en cada celda de todos los pisos
    E: cuantos pisos y cuantas celdas por pisos
    S: resultado de las capsulas
    R: largo y largo_pisos deben ser int positivos"""

    if type(largo)!=int or type(largo_pisos)!=int:
    
        return 'ERROR01'
        
    elif largo<0 or largo_pisos<0:
    
        return 'ERROR02'


    global biblioteca
    
    i = 0
    
    while i < largo:
        
        biblioteca += [generar_piso(1, largo_pisos)]
        
        i += 1

    
    return "Biblioteca Generada"


def generar_piso(piso, largo):
    """Función que genera las celdas de un piso.
    E: numero de piso y largo del piso
    S: el piso a realizar
    R: piso  y largo deben ser int positivos"""

    if type(piso)!=int or type(largo)!=int:
    
        return 'ERROR01'
        
    elif piso<0 or largo<0:
    
        return 'ERROR02'

        
    piso = []

    i = 0

    while i < largo:

        piso += [generar_capsulas()]

        i += 1

    return piso


def generar_capsulas():
    """Función que genera las capsulas de una celda
    S: 0,2,3"""

    capsulas = random.randint(1,3)

    if capsulas == 1 :
        return 0

    return capsulas

generar_biblioteca(5,10)



def calcular_dado():
    """Función que calcula el número a salir en el dado
    S: numeros del 1 al 4"""

    return random.randint(1,4)


def calcular_retroceso():
    """Función que calcula cuanto va a retroceder si
    no encuentra capsulas"""

    return random.randint(1,3)*-1

def calcular_movimiento(movimiento, largo_pisos):
    """Función que suma o resta su posicion actual de acuerdo
    a un movimiento
    E: un movimiento, sea positivo o negativo, maximo valor de
        posiciones por largo_pisos
    S: Avance o retroceso en el tablero
    R: movimiento int, largo_pisos int positivo"""

    if type(movimiento)!=int or type(largo_pisos)!=int:
    
        return 'ERROR01'
        
    elif largo_pisos<0:
    
        return 'ERROR02'


    global celda_actual


    celda_actual += movimiento

    if celda_actual < 0:
    
        celda_actual = 0

    if celda_actual >  largo_pisos:

        celda_actual = largo_pisos   

    return "Movimiento calculado"


def generar_pregunta(piso, preguntas):
    """Función que escoge aleatoriamente una pregunta por piso
    E: piso y preguntas
    S: preguntas y respuestas en desorden
    R: piso debe ser int, y preguntas debe ser una lista"""

    if type(piso)!=int or type(preguntas)!=list:
    
        return 'ERROR01'

    elif piso<0:

        return 'ERROR02'


    preguntas
    
    return random.randint(0, len(preguntas)-1)

    

def generar_ronda_de_preguntas(piso, largo):
    """Función que escoge 5 preguntas por piso y desordena sus
    respuestas
    E: piso y largo piso
    S: ronda de preguntas por piso
    R: piso y largo int positivo"""

    if type(piso)!=int or type(largo)!=int:

        return 'ERROR01'

    elif piso<0 or largo<0:

        return 'ERROR02'
        

    global preguntas

    preguntas_local = preguntas[piso]


    i = 0 

    cantidad_preguntas = 5

    preguntas_quizz = []

    
    while i < largo:

        pregunta = generar_pregunta(piso, preguntas_local)
        
        preguntas_quizz += [preguntas_local[pregunta]]
        
        preguntas_local = eliminar_lista(preguntas_local, pregunta)

        i += 1
        

    return preguntas_quizz

def eliminar_lista(lista, indice_eliminar):
    """Función que elimina elemento de una lista basado en índice
    E: lista y la posicion a eliminar
    S: lista sin el indice que se eliminó
    R: indice no puede ser mas grande que el largo de la lista -1"""

    if type(lista)!=list or type(indice_eliminar)!=int:

        return 'ERROR01'
        

    i = 0 

    largo = len(lista)

    res = []

    while i < largo:

        if i != indice_eliminar:
            res += [lista[i]]

        i += 1

    return res



def quizz(piso):
    """Función que presenta todas las preguntas por piso
    E: piso
    S: True or False
    """
       

    global cantidad_preguntas, cheats
    
    preguntas = generar_ronda_de_preguntas(piso, cantidad_preguntas)
    
    preguntas_hacer = []

    respuestas_correctas = []

    respuestas_incorrectas = []

    i = 0

    largo = len(preguntas)

    while i < largo:
        
        preguntas_hacer += preguntas[i][0]

        respuestas_correctas += [preguntas[i][1]]

        respuestas_incorrectas += [preguntas[i][2] + preguntas[i][3] + preguntas[i][4]]

        i += 1        
    
    i = 0

    largo = len(preguntas_hacer)

    respuestas_incorrectas_temp = []

    orden_preguntas = 0

    respuesta_correcta = 0

    respuesta_usuario = 0

    cinematica_quizz_pre_quizz()
    
    while i < largo:

        respuestas_pregunta = respuestas_correctas[i] + respuestas_incorrectas[i] 

        i2 = 0

        largo2 = len(respuestas_pregunta)

        flag = False

        respuestas_desordenadas = []
        
        while i2 < largo2:
            
            
            respuesta_a_mostrar = random.randint(0, len(respuestas_pregunta)-1)
            
            respuestas_desordenadas += [str(i2+1) + ") " + respuestas_pregunta[respuesta_a_mostrar]]
            
            respuestas_pregunta = eliminar_lista(respuestas_pregunta, respuesta_a_mostrar)

            if  respuesta_a_mostrar == 0 and flag == False:

                flag = True

                respuesta_correcta = i2+1

            i2 += 1

        respuesta_usuario = cinematica_quizz(preguntas_hacer[i], respuestas_desordenadas, i)

        if cheats != True:

            if int(respuesta_usuario) == respuesta_correcta:

                cinematica_quizz_correcta()

            else:

                cinematica_quizz_incorrecta()


                return False

        i += 1

    return True 


def iniciar_juego():
    """Función genera la biblioteca, cinemática inicial, genera pisos hasta que se gane,
    cinemática durante y después del juego (une todas las fases del juego)
    """

    global piso_actual, celda_actual, largo_pisos, cantidad_pisos, biblioteca, fondos


    
    generar_biblioteca(cantidad_pisos, largo_pisos)

    cinematica()

    terminado = False

    while terminado != True:

        imprimir_dibujo(fondos[piso_actual])

        input()

        print("\033[2J\033[H")

        avanzar = jugar_piso()

        celda_actual = 0

        if avanzar == True: 

            piso_actual += 1

        else:

            piso_actual -= 1

        if piso_actual < 0:

            piso_actual = 0 

        if piso_actual > cantidad_pisos:

            terminado =  True
    
    cinematica_cierre()
    
    return "Juego terminado"


def jugar_piso():
    """Función que ejecuta las cinemáticas, pistas y preguntas de un piso dado"""

    global piso_actual, celda_actual, largo_pisos, cantidad_pisos, pistas, biblioteca

    
    pistas_piso = pistas[piso_actual]

    piso = biblioteca[piso_actual]

    movimiento = 0
    
    while celda_actual != largo_pisos:

        pistas_local = []
                   
        if piso[celda_actual] == 0:
        

            movimiento = calcular_retroceso()
            calcular_movimiento(movimiento, largo_pisos)
            cinematica_restroceso(movimiento*-1)

        else: 

           cantidad = piso[celda_actual]
           while cantidad > 0:
           
               pista_evaluada = random.randint(0, len(pistas_piso)-1)

               pistas_local += [pistas_piso[pista_evaluada]]

               pistas_piso = eliminar_lista(pistas_piso, pista_evaluada)
                   
               cantidad -= 1

               if pistas_piso == []:

                   pistas_piso = pistas[piso_actual]
                   


           cinematica_avanzar(mostrar_pistas(pistas_local), piso[celda_actual])


        movimiento = calcular_dado()
        cinematica_dado(movimiento)
        
        calcular_movimiento(movimiento, largo_pisos)

        mostrar_mapa()
        

        

    
    return quizz(piso_actual)

def mostrar_pistas(pistas):
    """Función que muestras las pistas necesarias de acuerdo el piso
    E: lista de pistas
    S: lista de pistas por piso
    R: pistas debe ser lista
    """

    if type(pistas)!=list:

        return 'ERROR01'
        

    i = 0 

    largo = len(pistas)

    res = []

    while i < largo:

        res += [[i, pistas[i]]]

        i += 1


    return res



    

            

        

fondos= [
    [
        '                                                        X                     ',
        '                                       XXXXXXXXXXX       X                     ',
        '                            XXXXXXXXXXX                  X                     ',
        '         ..__      .---\\                                 X                     ',
        "        /    ``-..'     |                       XXX       X                    ",
        "      .'                `.                XXXXXX           X                   ",
        " .'--/                    `-.       XXXXXX                  X                  ",
        '/                           |   XXXX                  XX     X                 ',
        '                            /                      XXX        XX               ',
        '\\                          /                     XX             XXXX         XX',
        " `\\                      .'                   XXX                   XXXXXXXXX  ",
        "   `.   __..__       ..-'                   XX               X                 ",
        "    --''      ``--..'                                      XX        X       X ",
        '                                                         XX          X       X ',
        '                                                       XX           X        X ',
        '                                                     XX             X        X ',
        '                                                                    X        X ',
        '                                                                   X         X ',
        '                                                                   X         X ',
        '                                                                             X ',
        '                __  __       _        _                                        ',
        '               |  \\/  | __ _| |_ _ __(_)____                                   ',
        "               | |\\/| |/ _` | __| '__| |_  /                                  ,",
        "               | |  | | (_| | |_| |  | |/ /                    ,.......__. ,-''",
        '               |_|__|_|\\__,_|\\__|_|  |_/___| __ _   _        /\'\'         \'"    ',
        "     _......_  | ____|_ __   ___ _ __ __ _  /_/| |_(_) ___ _|'_                ",
        "_,-'''      '\\_|  _| | '_ \\ / _ \\ '__/ _` |/ _ \\ __| |/ __/ _` |               ",
        "'             '| |___| | | |  __/ | | (_| |  __/ |_| | (_| (_| |               ",
        '               |_____|_| |_|\\___|_|  \\__, |\\___|\\__|_|\\___\\__,_|               ',
        '               / ___|  ___  ___| |_ _|___/__ (_) |__ | | ___                   ',
        "               \\___ \\ / _ \\/ __| __/ _ \\ '_ \\| | '_ \\| |/ _ \\                  ",
        ' │      │       ___) | (_) \\__ \\ ||  __/ | | | | |_) | |  __/         │       │',
        ' │      │      |____/ \\___/|___/\\__\\___|_| |_|_|_.__/|_|\\___|_       ┌┘       │',
        '┌┘      │        |                                            `.     │        └',
        '│       │     _/\'\'                                             \'"\\   │         ',
        "│       └┐ ,,-'                                                  '---┘         ",
        "│        │`'                                                        │          ",
        '┘        │                                                          │          ',
        '         │                                                         ┌┘          ',
        '         │                                                         │           ',
        '         │                _____________..................._______  │           ',
        "-------------'''''''''''''                                       ```````-------",
        '                                                                               ',
        ' XXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXX    ',
        ' X   X    X  X   X    X    X    X    X    X   X     X   X  X   X    X     X    ',
        ' XXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXX    ',
        ' X   X    X  X   X    X    X    X    X    X   X     X   X  X   X    X     X    ',
        ' XXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXX  XXXXXXXXXXXXXXXX    ',
        '   │   │      │  │     │   │     │   │      │   │   │  │     │  │    │  │      ',
        '   │          │        │         │          │       │        │       │  │     ',
    ],

    [
        '                 )                         ;                         :  ------',
        '-.             ,-----.          ----------  |                         |        ',
        "  `----------,'       `.                    :                         ;        ",
        "            (           )                ,-''\\                       /  ..__   ",
        "             `.       ,'                (     \\                     /       ``-",
        "               `-----'              .-'  `--.  `.                .,'           ",
        "                                 .-'         `---'--.         _.-'    `.       ",
        "                                              .'     `------''          \\      ",
        '     _.--------.                             /      /      |     \\       `.    ',
        " ,-''           `--.                       .'      /       |      \\        `.  ",
        '/                   \\                     ,-------.        |       \\           ',
        "                     )                  ,'         `.      |                   ",
        '\\               _.--------.            (             )     |                   ',
        " `--.       ,-'            `--.         `.         ,'                          ",
        "     `-----/                   \\          `-------'               ,---------.  ",
        "          (                     )                              ,-'           `-",
        '           \\                   /                              (                ',
        "            `--.           _.-'                                `-.           ,-",
        "                `--------''                                       `---------'  ",
        '                  __  __            _ _ _     _           _                    ',
        '                 |  \\/  | _____   _(_) (_) __| | __ _  __| |                   ',
        '                 | |\\/| |/ _ \\ \\ / / | | |/ _` |/ _` |/ _` |                   ',
        '                 | |  | | (_) \\ V /| | | | (_| | (_| | (_| |                   ',
        '                 |_|  |_|\\___/ \\_/ |_|_|_|\\__,_|\\__,_|\\__,_|                   ',
        '                 | | | |_ __| |__   __ _ _ __   __ _                           ',
        "                 | | | | '__| '_ \\ / _` | '_ \\ / _` |                          ",
        '                 | |_| | |  | |_) | (_| | | | | (_| |                          ',
        '                  \\___/|_|  |_.__/ \\__,_|_| |_|\\__,_|                          ',
        '                                                                               ',
        '   ,-.               ,-.                       ,-.                 ,-.         ',
        '  (   )             (   )                     (   )               (   )        ',
        "   `-'               `-'                       `-'                 `-'         ",
        '    │                 │                         │                   │          ',
        '    │                 │                         │                   │          ',
        '    │                 │                         │                   │          ',
        '    │                 │                         │                   │          ',
        '    │                 │                         │                   │          ',
        '────│─────────────────│─────────────────────────│────__O────────────│──────────',
        '    │                 │__O          __o         │   / /\\_,          │          ',
        '──────────────────────/ /\\_,────────\\<_───────────___/\\──────────────────__o───',
        '       __           ___/\\        (_)/(_)              /_    __O        _ \\<_   ',
        '    __/  \\_             /_                  __o            / /\\_,     (_)/(_)  ',
        "   '-o---o-'                __o           _ \\<_          ___/\\                 ",
        '╒═══════════════════════════\\<═══════════(_)/(_)══════O══════/_════════════════',
        '╘════════════════════════(_)/(_)═══════════════════/ /\\_,══════════════════════',
        '                  __o               __           ___/\\                         ',
        '        ,-----, _ \\<_            __/  \\_             /_                        ',
        "        |     |(_)/(_)          '-o---o-'                                      ",
        "────────'-----'────────────────────────────────────────────────────────────────",
    ],

    [
        "  ,~-.                   ( ` ')  )                                            ",
        "  (  ) )_                (_(_.~~~'                           ,~-.              ",
        " ( ` ')  )                                                  (  ) )_            ",
        "(_(_.~~~'                                                  ( ` ')  )           ",
        "                                                          (_(_.~~~'        ,~-.",
        '                         ,~-.                                             (  ) ',
        "                        (  ) )_                                          ( ` ')",
        "                       ( ` ')  )                                        (_(_.~~",
        "                      (_(_.~~~'                                                ",
        '                                                               /\\          /\\  ',
        '                                         ,~-.                 //\\\\        //\\\\ ',
        '                                        (  ) )_              ///\\\\\\      ///\\\\\\',
        "                                       ( ` ')  )               ][          ][  ",
        "                                      (_(_.~~~'              ,----------------,",
        '                                                             | ,/   /    /    |',
        "          ,~-.                                               | /   ,'   |     |",
        '         (  ) )_                                             ||    |    |     |',
        "        ( ` ')  )                                   ,~-.     ||    '\\.  `..   |",
        "       (_(_.~~~'                                   (  ) )_   | \\     '|   `.  |",
        "                                                  ( ` ')  )  |  \\     |    |  |",
        "                     _____                       (_(_.~~~'   |  |    ,|    |  |",
        '                    |_   _|__ _ __ ___ ___ _ __ ___  ___     |  |    |    ..  |',
        "                      | |/ _ \\ '__/ __/ _ \\ '__/ _ \\/ __|    | _( )_ |     |  |",
        '                      | |  __/ | | (_|  __/ | | (_) \\__ \\    |(_(%)_)|    ,|  |',
        "                     _|_|\\___|_|  \\___\\___|_|  \\___/|___/    |  (_)  '\\   |   |",
        '   /\\          /\\   | ____|___ _ __   __ _  ___(_) ___  ___  |         |  |   |',
        "  //\\\\        //\\\\  |  _| / __| '_ \\ / _` |/ __| |/ _ \\/ __| |         |  |   |",
        " ///\\\\\\      ///\\\\\\ | |___\\__ \\ |_) | (_| | (__| | (_) \\__ \\ |       _/'   |  |",
        '   ][          ][   |_____|___/ .__/ \\__,_|\\___|_|\\___/|___/ |      ,/     |  |',
        ',-----------------,           |_|                            |      |      |  |',
        '|  ,.     ,.    _ |                                          |      |      |  |',
        "|_,'   |   |   /' |                                          |      |     /'  |",
        "|`.    |   |   |  |                                          |      |    /'   |",
        "| '-.  |.  |   |  |                                          |  _( )_    |    |",
        '|   \\.  \\  <.  `. |                                          | (_(%)_)   \\.   |',
        '|    |   \\  |   \\ |                                          |   (_)      \\.  |',
        "|    |   |  |   '\\|    /\\                                    |             |  |",
        "|   ,'   |  '>   || --//\\\\----/\\-------/------------|--/\\--- |            |'  |",
        "|  |'    |  _( )_||  ///\\\\\\  //\\\\     /             / //\\\\   |           _/   |",
        "|  '\\    | (_(%)_)|    ][   ///\\\\\\   /             | ///\\\\\\  |          ,'    |",
        '|_( )_    _  (_)  |           ][    /              /   ][    |          |     |',
        "(_(%)_)   '|      |      /\\        /              |          |       _( )_    |",
        '| (_)      |      |     //\\\\      /               /      /\\  |      (_(%)_)   |',
        "|       _( '_     |    ///\\\\\\   /|               |      //\\\\ |        (_)     |",
        '|      (_(%)_)    |      ][    / |               /     ///\\\\\\|                |',
        '|        (_)      |           /  /---           |        ][  |                |',
        '|                 |    /\\    /| /   /           /      /\\    |                |',
        '|                 |   //\\\\  / |/---/|          |      //\\\\   |                |',
        '|                 |  ///\\\\\\/   |  |            /     ///\\\\\\  |                |',
        '|                 |    ][ /                   |        ][    |                |',

        
    ],

    [
        '   ,~-.                                                 (  ) )_               ',
        "   (  ) )_                                              ( ` ')  )              ",
        "  ( ` ')  )                                            (_(_.~~~'               ",
        " (_(_.~~~'               ,~-.                             |    `.              ",
        "     \\                  (  ) )_                              | \\ '-.         ,-",
        "        |              ( ` ')  )                  ,~-.    \\         `-------'  ",
        "   |  |               (_(_.~~~'                  (  ) )_      | \\              ",
        "         \\              \\                       ( ` ')  )  |                   ",
        "      \\                     \\  |               (_(_.~~~'       |  |            ",
        '    |     \\              \\                              \\                      ',
        '                                                 /  \\          \\               ',
        '     | \\    \\                \\   |                        |                    ',
        '                                                /     |             ,~-.       ',
        '      ,~-.                 ,~-.   \\             ,~-.               (  ) )_     ',
        "     (  ) )_              (  ) )_              (  ) )_            ( ` ')  )    ",
        "    ( ` ')  )            ( ` ')  )            ( ` ')  )          (_(_.~~~'     ",
        "   (_(_.~~~'\\           (_(_.~~|'            (_(_.~~~'             |       \\   ",
        '      | \\                   |  \\              |       |                /       ',
        '             \\            /                       \\                /           ',
        '      \\  \\                   |   |           /         |             |    ,~-. ',
        "              \\\\_('<     /                         \\              |      (  ) )",
        "       |   |   \\___)            _            _ _       \\                ( ` ') ",
        '                / \\   __ _ _ __(_) ___ _   _| | |_ _   _ _ __ __ _     (_(_.~~~',
        "        |   \\  / _ \\ / _` | '__| |/ __| | | | | __| | | | '__/ _` |          | ",
        '              / ___ \\ (_| | |  | | (__| |_| | | |_| |_| | | | (_| |     |      ',
        '        \\    /_/__ \\_\\__, |_| _|_|\\___|\\__,_|_|\\__|\\__,_|_|  \\__,_|          | ',
        '             / ___|  |___/___| |_ ___ _ __ (_) |__ | | ___              /      ',
        "             \\___ \\ / _ \\/ __| __/ _ \\ '_ \\| | '_ \\| |/ _ \\                 |  ",
        '              ___) | (_) \\__ \\ ||  __/ | | | | |_) | |  __/            |       ',
        '             |____/ \\___/|___/\\__\\___|_| |_|_|_.__/|_|\\___|                 /  ',
        '                                                                               ',
        '  /\\                             /\\                    /\\             _( )_    ',
        ' //\\\\                           //\\\\          \\ /     //\\\\           (_(%)_)   ',
        '///\\\\\\              /\\         ///\\\\\\         ( )    ///\\\\\\   __      _(_)\\    ',
        "  ][               //\\\\          ][          .' '.     ][   o'')}____//    | __",
        "                  ///\\\\\\                     '.o.'           `_/      )    |/_/",
        '     ,------------  ][          ,---------------,            (_(_/-(_/--\\  |   ',
        '     |            |        /\\   |               |    /\\     |            \\ |   ',
        '     | ,...._ _   |       //\\\\  |   ..--.._     |   //\\\\    |  ,----.    |     ',
        "     | '    '''   |      ///\\\\\\ |         '`    |  ///\\\\\\   |  '         |     ",
        '     |            |        ][   |               |    ][     |            |     ',
        "     |     ___ _  |             |        ___    |           |  _,-'''-\\  |     ",
        '     |   <\'  \'"   |             |     --\'\' \'    |           |            |     ',
        '     |            |   _( )_     |               |           |            |     ',
        "     |  __...'    |  (_(%)_)    |               |     /\\    |   _____.   |     ",
        '     |  \'         |    (_)\\     |   `""\'\'\'-\\.   |    //\\\\   |        |   |     ',
        "   /\\'------------'        | __ |           '   |   ///\\\\\\  |            |     ",
        '  //\\\\           \\(")/     |/_/ \'---------------\'     ][    \'------------\'     ',
        ' ///\\\\\\          -( )-     |                                                   ',
        '   ][            /(_)\\     |                                                  ',
    ],

    [
        '                                       _.------.                    ',
        "                                     ,-''         `--.                ",
        "                                   ,'                 `.              ",
        '                                  /      \\              \\             ',
        '                                 ;        `.             :            ',
        '                            ."". ."".       `X           |            ',
        "                            |   '   |        |           ;            ",
        '                             \\     /         |          /\\_/\\         ',
        "                              '. .'`.                 ,( o.o )        ",
        "                                '    '--.   __      _'  > - <         ",
        "                                         `o'')}____//                 ",
        '                                           `_/      )                 ',
        '                                           (_(_/-(_/                  ',
        '                                                                      ',
        '                                                                      ',
        '                                                                      ',
        '     _____                                __                          ',
        '    | ____|___ ___  _ __   ___  _ __ ___ /_/ __ _ ___                 ',
        "    |  _| / __/ _ \\| '_ \\ / _ \\| '_ ` _ \\| |/ _` / __|                ",
        '    | |__| (_| (_) | | | | (_) | | | | | | | (_| \\__ \\                ',
        '    |_____\\___\\___/|_| |_|\\___/|_| |_| |_|_|\\__,_|___/                ',
        '       / \\  | | |_ ___ _ __ _ __   __ _| |_(_)_   ____ _ ___          ',
        "      / _ \\ | | __/ _ \\ '__| '_ \\ / _` | __| \\ \\ / / _` / __|         ",
        '     / ___ \\| | ||  __/ |  | | | | (_| | |_| |\\ V / (_| \\__ \\         ',
        '    /_/   \\_\\_|\\__\\___|_|  |_| |_|\\__,_|\\__|_| \\_/ \\__,_|___/         ',
        '                                                                      ',
        '                                                                      ',
        '                           ,-----------------------------------------,',
        '                           |                       _________         |',
        '                           |        ,-.           (_)-----(_)        |',
        '                           |      _(*_*)_           / (_) \\          |',
        '                           |     (_  o  _)         |_______|         |',
        '                           |       / o \\                             |',
        '                           |      (_/ \\_)                     :&:    |',
        ' _____|_____               |                    _______        #     |',
        '|     ,-.   |              |                   /      /,       #     |',
        '|  ,-(,-.)  |              |      _____       /      //       _#_    |',
        '| (  (   )  |              |     |A .  |     /______//       ( # )   |',
        "|  `-'`-'   |              |     | /.\\ |    (______(/        / O \\   |",
        '|___________|              |     |(_._)|              ____  ( === )  |',
        "     /|\\                   |     |  |  |             |____|  `---'   |",
        '    / | \\                  |     |____V|             |    |          |',
        '   /  |  \\                 |                       (_)  (_)          |',
        "                           '-----------------------------------------'",
    ]


    
]




dibujo_Filler = [ 
'                                 ',
' _____   _   _   _               ',
'|  ___| (_) | | | |   ___   _ __ ',
"| |_    | | | | | |  / _ \\ | '__|",
'|  _|   | | | | | | |  __/ | |   ',
'|_|     |_| |_| |_|  \\___| |_| ',
'                                 ',
'                                 ',
'                                 ',
'                                 ',
'                                 ',
'                                 ',
'                                 ',
'                                 ',
'                                 ',
'                                 ',
'                                 ',

]


dibujo4 = [
'                            ,,..Y------.._                                     ',
'                        _o-\'\'            \'\'"._                     _           ',
"                     ,.''                    '\\.                   '`_         ",
"                     /                         \\.  _,..----.b.       '`.   ,---",
"           ,_.. b_  ,|                          \\,/'         'o.       ' ,'    ",
'         ,-\'     \'"o_.                          /\'             `.      ,\'      ',
"       ,/'          ''                                          |     ;        ",
"       |                                                        |'-._.;        ",
"       |                                                        |    '         ",
'       `.                                                      ,|    |         ',
'        `.                        ,__,.b_.                    ,/     :         ',
"         `o.                 ,,,-''     ' .                 _.'       :        ",
"           '- _...(_     _,,''            ,\\.           _,o-'         :        ",
"              |    '--.-'' |              | '`-...._---',|           ,/'.      ",
"              |       \\.  |'              |      ,/'   ,'           ,/   `.    ",
"              '\\       `. |  |.   ,---'   |     ,'    /'           Y'      `-,-",
"               '\\.      | '|  `./'        |    ,|   .'                      _' ",
"                 '`-.b_ '-..              |_.Y-'    /                      ,/  ",
"                      '\\.  |              '                               ,'   ",
"                        '\\ |. (           |                                    ",
"-.                        `.| '`.__,...  ,|      ,,'                           ",
"  `\\.   _...b    ,--- .    `'         `\\ `.....,-'            ,_._             ",
"    '--'     ' .|'    '\\    |            '|         ,/''`\\   |'_.'`.       ,...",
"                \\-... ,|    |  ,. __.     \\        /'    `\\   ''''Yb     ,-'   ",
"                 \\. '''     |   ''' '-..  '\\      |'      '\\. ,_.-' '---''     ",
"                  ''----''-'|          '   '\\               '''                ",
"                           /                '\\                                 ",
"                          J'        ,-- ..   '\\   __              ,_           ",
' ,o" b, ._..b           ,\'\'         |  , |    \'\\,\'\' \' ..---._,Y---\' \'-....---..',
" '      ''  '`--''''->,'____________|____|___,..`.                            `"
]    

dibujo1= [
    '',
    '     (                                                                         ',
    '    ( )                                                                        ',
    '     Y                          _______             _______                    ',
    '    |"|                        /      /,           /Solar /,                   ',
    '    | |           (0>         /Linux //           /Punk  //                    ',
    "'''''''--..__     //\\___,... /______//__         /______//         ,__..b_     ",
    "    | |     ''''''V_/_      (______(/  '''''''''(______(/''---....''     ''o_  ",
    " __.....___  ' .____     ,_______                                __         ''`",
    "`'        ''--...--'''''''   .__''''''''''''''--- ......,-----'''  '--._       ",
    "                             |   ________ '''''''.                     '`-...._",
    "                             | |''Memes  ''`- .  |                             ",
    '                             | | ....Elefantes __[                             ',
    "                             L_.    '''''''''__,.'                             ",
    "                               ''''''''.'''      _________                     ",
    "                             ,------,_,'\\._b,.b_(_)-----(_)                    ",
    "                           ,/'     ,' ' `''`b     / (_) '|                    ",
    '  _____|_____            ,/\'  ,/"--\'-.....__.\' \' |_______||                    ',
    " | ,,..---\\. |         _,'    |   --\\  ..   |  `/'_____`' |.                   ",
    " | |       \\ |       `''__.,--'-...----...Y<'-/''''    |   |                   ",
    " | \\   A   | |       ,''      |              |'  `..   |   |                   ",
    " | 'L      J |       |        |              |---........  |                   ",
    " |__'`-----'_|      ,|        |              |     ,    |  |                   ",
    "      /|\\           |         |              |.__  '`   _  |                   ",
    "     / | \\          |         |              |   '''''''/  |                   ",
    '    /  |  \\         |        .|              |     `.   |  |                   ',
    "                    |        '               ...---------  '                   ",
    '                    |                        | ,___...._|                      ',
    "                                             `''                               ",
    '',
]

dibujo2= [

   '     (                                                                         ',
    '  X ( )               X             X                                    XX    ',
    '   XXY                 X        ____X__            X_______            XX      ',
    '    |XX                X       /    X /,          X/      /,         XX        ',
    '    | |XX         (0>   X     /     X//           X      //        XX          ',
    "'''''''--X.__     //\\___X... /______/X__         X______//       XX,__..b_     ",
    "    | |   XX''''''V_/_   X  (______(/X '''''''''X______(/''---XXX.''     ''o_  ",
    " __.....___ XX .____     X_______    X         X            XX   __         ''`",
    "`'        ''--X..--'''''''X  .__'''''X''''''''-X- ......,-XX--'''  '--._       ",
    "XX             XX         X  |   ____X___ ''''X''.      XX             '`-...._",
    "  XX             XX        X | |''  XXXXXXXXXXXXXXXXX XX                       ",
    '    XX             XX         XXXXXX    .._/--\\    XXXXXXXX                    ',
    "      XX             X    XXXX        /-/      '`\\         XXXX                ",
    '        XX             XXX            \\  ,,-\'\'"\'\'+ _______     XXX         XX  ',
    "          XX         XX             |'' /───┌──┐ | -----(_)       XX    XXX    ",
    "            X       X               `,_-'   └──┘ \\  X_) '|         XXXX       ",
    "  _____|_____      X             ,,-''          --\\  XXX_||      XXXXX         ",
    " | ,,..---\\. |    X   |`\\ __  _.'     _--,    └┐┌┘      XX|.  XXX     X        ",
    " | |       \\ |   X   `|  '''''    ,__.'  |     └┘\\        X|XX         X       ",
    " | \\       | |   X   , \\       ,_,'      |       /        X|           X       ",
    " | 'L      J |  XXXXXX  \\_     '-+-------'     _/         X|           X       ",
    " |__XXXXXXXXXXXX  X ,|    `.. ---------,_,____/'        XX |          X        ",
    "XXXX  /|\\          X|       \\  \\`.     \\      '-.   XXX   |         X         ",
    "     / | \\          X        \\  \\``''   \\  '---' |XX'     |        X          ",
    "    /  |  \\      XXXXXX       `. '-'     |\\  '---'|XXXX |  |      XX           ",
    "            XXXXX   |  XXX      '--------' `------'----XXXXXXX XXX             ",
    '       XXXXX        |     XXXXXXX            | ,___...._|  XXXXXXXXX           ',
    "    XXX                  XXXX XXXXXX         `''     XXXXXX         XXXXXXX    "
      
]

dibujo3 = [

    '              _oo88888P"\'\'     _ooo88888888888888PP"\'\'                 Y888o.. ',
    '            ,o8888P\'\'       ,o888888PP",__,ooooooooooooooooooooo_       \'Y8888L',
    '          _d888"\'       ,,d8888P_,oood8888888888888888888888888888oo.      `Y88',
    '        _o888\'       ,od888PP\'d8888888PPP""\'\'\'\'\'\'             \'`P88888o.     Y8',
    '      ,o888"\'     ,,o888PP\' ,888P"\'\'  _oooooooooooo._             \'`Y8888..  \'8',
    "    ,o888''     ,o8888''  ,d88P'   ,o88888888888888888oo_            '`Y888p  Y",
    '   d888\'      _d888P\'    d88P\'  ,,d888P\'\'\'\'     \'\'`"P88888oo._.         `Y88.  ',
    " ,d88P       d88P'      d88P  ,o888P''_oooooooooo__   ``Y888888bo.       '88b  ",
    ' d88\'      ,d88\'       d88\'  ,888P\' d888888888888888oo._   \'"YY8888..     d8b  ',
    'J88\'      ,d8P\'       d88P  d88P\' ,d88P"\',,oooo``"P888888o.    \'`P888o.   d8b  ',
    '88F       d88\'       d88P  ,88P   d88\' ,o88888888888\'\'"P888..     `Y888.  ]88. ',
    "88'     ,d88'       ,88[   d8P   d88' ,888P''_,oooooo_88'Y888.      'Y88b. YP' ",
    "88     ,d88'        d8P   J88'  ,88P ,88P' d8888888888o.b.`Y88b.      `Y88.    ",
    '88.    d88\'        ,88\'   d8P   J88\' 88F   88P"\'\'  `Y888pb  `88b.      \'Y8b    ',
    "88[    d8b         d8P    88[   88P ]88[   ''         88b8.  `888.      `88.   ",
    "8P     d8b         88P    88[   88b `88L.    _o8p   ,d88P88.  '88b       Y8b   ",
    "8[     d8b         88[    88[   Y88. Y8888888888P  ,888'`88b   `88[      `88.  ",
    "8[     d8b         88[    Y8b   'Y88o_`YPPPPPP''_,d88P'  Y88    Y8b       88b  ",
    "8b     ]88.        88b    `88p    Y8888o._.,_oo8888P'    ]88    d8b       d8b  ",
    '88      88b        `88.    Y88L    ``P8888888888P"\'      d88   ,88P       d8b  ',
    '88.     `88b        Y8b.    Y88b..    \'\'"YPPP\'\'    ,_ooo888\'  ,88P        88P  ',
    "88[      `88b       'Y88.    `8888o_          _,oo8888888P'   d88'        88[  ",
    "Y8b       `88b       'Y88b._   'Y8888boooooo8888888PP'''    ,d88'        J88'  ",
    '`88L.      `88b.       `Y888o._  \'`PY88888888PP"\'\'        _o888\'        ,88P   ',
    ' Y888.      \'Y88.        `"8888ooo__                    ,o888P\'        d88P    ',
    '  `Y88b.      Y88L.         `Y88888888888boooo._____,ooo888"\'        ,d88P     ',
    '    `Y88.      Y888.           \'\'`"YPPPPY8888888888888888P\'        ,o88P\'      ',
    '      Y88b.     `Y888o_____                `\'\'"\'\'\'          ,888\'        ',
    "       `Y88L.     `Y888888888ooooo.______                      _od88P'         ",
    "         Y888b      `______PP888888888888888ooooooooooouoooooo88888P'           ",
]


dibujo5 = [
    
    '',
    "''-._                                    ,,--''             ",
    "              '`..                              ,,-'                  ",
    "                  '---._                      _-'                     ",
    "                       '`-..                ,-'                       ",
    "                           `-.         `.-''                          ",
    '                                                                      ',
    '                                                                      ',
    '                 ┌───────────────────┐           ┌───────────────────┐         ',
    '─────────────────│   XX          XX  │───────────│  XX         XX    │─────────',
    '  XXXXX          │     XXX     XX    │           │    XXX    XX      │         ',
    ' XXXXXXX         │        XXXXX      │           │       XXXX        │         ',
    'XXXXXXXXX        │       XXX XXX     │           │       XX XXX      │         ',
    " XXXXXXX         `.    XX       XX  .'           `.    XX      XX    /         ",
    "  XXXXX            \\ XX            /               \\ XX            .'          ",
    "  X X X             `.───────────.'                 `.────────────/            ",
    '  X X X                                  -\\                                    ',
    "  X X X                                    '..                                 ",
    '  XXXXX                                       `-._.                            ',
    "  XXXXX                                           '`--.._                      ",
    "  XXXXX                                                 ''--_.                 ",
    '   XX                                                   __,-                   ',
    "   XX                XXXX                             ,,'                      ",
    "   XX               X    X                         _-''                        ",
    "   XXXXXXXXXXXXXXXXX      X                     ,.''                           ",
    "   XXXXXXXXXXXXXXXXX      X                  _,/'----,,                        ",
    "                    X    X                ,,''       ;                         ",
    "                     XXXX             ,`''          /                          ",
    '                                        \\          /                          ',
    '     ',
    
]

dibujo_vacio=[
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      ',
    '                                                                      '
]

elefante = [
    '                              ',
    '                              ',
    '            ╔═══╔═══════╗════╗',
    '            ║+ +╝ ---   ╚╗+ +║',
    '   ╔════════║     |X|  X ║   ║',
    ' ╔═╝ +──────╚╗    ---    ║  ╔╝',
    '╔╝    ────── ╚═══   ---- ╚╗═╝ ',
    '║╔═╗              ╔════╗  ╚╗  ',
    '║║ ║ ╔══════════╗ ║    ╚═╗ ║  ',
    '║║ ║+║          ║+║      ║+╚═╗',
    '║║ ║ ╚╗         ║ ╚╗     ╚═══╝',
    '╚╝ ╚══╝         ╚══╝          ',
    '                             `',
    '                              ',
    '                              '
]

elefante_capsula = [
    '                              ',
    '    \\ \\ | | / /               ',
    '    \\ \\| |/ ╔═══╔═══════╗════╗',
    '     \\┌────┐║+ +╝ ---   ╚╗+ +║',
    '   ╔══│┌──┐│║     |X|  X ║   ║',
    ' ╔═╝ +│└──┘│╚╗    ---    ║  ╔╝',
    '╔╝    ────── ╚═══   ---- ╚╗═╝ ',
    '║╔═╗              ╔════╗  ╚╗  ',
    '║║ ║ ╔══════════╗ ║    ╚═╗ ║  ',
    '║║ ║+║          ║+║      ║+╚═╗',
    '║║ ║ ╚╗         ║ ╚╗     ╚═══╝',
    '╚╝ ╚══╝         ╚══╝          ',
    '                      `       ',
    '                              ',
    '                              '
]


dibujo_retroseso = [ 
'            ___     /.___                                                ',
'            |__ \\   /     ```---.                           .----------   ',
'         _    / /  /            /--------------------------/         /    ',
"        (_)  |_|  /            /              .'          /         |     ",
'        | |  (_) /            /       ,-----./           /          /     ',
"       / /_     '            /       /     .'\\          /          /      ",
"       \\___|   /           .'       /     /   \\       .'          /       ",
"              /           /        (    .'     )     /           /        ",
"             /           /          \\ .'      /     /           /         ",
'  \\         /           /            /       /     /           /          ',
"   `.      ...___      /           .' `-----'     /           |           ",
"     \\           ```--.───────.'──────────────────`.          /           ",
"             ___...-       .-'                   │  `-.      /            ",
"       ----'''       |   .'                      │     `.   /             ",
'       | ----------- |                           │      /`-/              ',
"       | / .'    `. ||                           │     /                  ",
"       |/.'        `.|                           │    /                   ",
"  .-'   |---- __ ---/|                           │   /  ╔═══╔═══════╗════╗",
"-'      || XX|  |XX ||                           │  /   ║+ +╝ ---   ╚╗+ +║",
'        |.    |,    .|     ..__                ╔════════║     |X|  X ║   ║',
"        | `........' |         ``-.          ╔═╝ +──────╚╗    ---    ║  ╔╝",
'        \\    ____    /──────────────────────╔╝    ────── ╚═══   ---- ╚╗═╝ ',
'         \\  |    |  /                       ║╔═╗              ╔════╗  ╚╗  ',
'      /-- \\        / |\\                     ║║ ║ ╔══════════╗ ║    ╚═╗ ║  ',
'  ---/ \\   \\------/  / `.\\                  ║║ ║+║          ║+║      ║+╚═╗',
' /---\\  \\----   ----/     \\                 ║║ ║ ╚╗         ║ ╚╗     ╚═══╝',
'/     \\       \\/           \\                ╚╝ ╚══╝         ╚══╝         ',
]

dibujo_avanzar = [
    '  \\           /                                                             ',
    '    `.        /                                                              ',
    '      \\      /       /.___                                                   ',
    '           _        /     ```---.                           .----------      ',
    "\\         | |      /.-'         /--------------------------/         /       ",
    " `.    _  | |    .-'           /     ,------------,       /         |        ",
    '      (_) |_|    /            /      |   ,,,,,,   |      /          /        ',
    "      | | (_)   '            /   ,--------------, |     /          /         ",
    "      | |      /`-.        .'    |    ,,,,,,    | |   .'          /          ",
    " .'   |_|     /    `-.    /   .--------------.  |-'  /           /           ",
    "'            /           /    |    ,,,,,,    |  |   /           /            ",
    "   /       \\/           /     |    '```'`    |--'  /           /             ",
    '  /        .\\.___      /      |..............|    /     ___---|              ',
    " /           \\   ```--.───────────────────────────---'''    | ___...-        ",
    "                       │                         │      ----'''       |      ",
    '                       │                         │      | ----------- |      ',
    '                       │                         │      | /          ||      ',
    '       \\ \\ | | / /                               │      |/            |      ',
    '       \\ \\| |/ ╔═══╔═══════╗════╗                │     / |---- __ ---/|      ',
    '        \\┌────┐║+ +╝ ---   ╚╗+ +║                │    /  || XX|  |XX ||      ',
    '      ╔══│┌──┐│║     |X|  X ║   ║                │   /   |.    |,    .|      ',
    "    ╔═╝ +│└──┘│╚╗    ---    ║  ╔╝                │  /    | `........' |      ",
    '   ╔╝    ────── ╚═══   ---- ╚╗═╝                 │ /     \\   ______   /      ',
    '   ║╔═╗              ╔════╗  ╚╗  ────────────────│/       \\  \\____/  /       ',
    '   ║║ ║ ╔══════════╗ ║    ╚═╗ ║                        /-- \\        / |\\     ',
    '   ║║ ║+║          ║+║      ║+╚═╗                  ---/ \\   \\------/  / `.\\  ',
    '   ║║ ║ ╚╗         ║ ╚╗     ╚═══╝                 /---\\  \\----   ----/     \\ ',
    '   ╚╝ ╚══╝         ╚══╝                          /     \\       \\/           \\',
]

texto1 = [

    "Es es la historia de los origenes de un personaje",
    "Un personaje que todos conocemos y queremos",
    "Que aunque nos parezca extraño...",
    "",
    "ACONTESE EN EL FUTURO"

]

texto2 = [

    "Mae que pereza esto de ser programador",
    "",
    "Si deporsi todo el poder esta controlado",
    "por las empresas",
    "",
    "A este paso no va a haber ni futuro",
    "... que ahuevado",
    "",
    "Yo mejor me rindo con este brete", 
    "de hacer correos",
    "",
    "Si al final la tecnologia solo",
    "lo jode todo"
]

texto3 = [ 
    "Que equivocado estas querido maestro",
    '',
    'Pero no se quedara así, no tiene porque',
    '',
    'Acompañame al futuro y aprenderas'
]

texto4 = [ 
    'De que hablas Gallina zapatuda?',
    '',
    'Yo no soy profesor de nadie,',
     'ni creo en el futuro',
    '',
    'Si nos vamos a ir todos al carajo',
    '',
    'Prefiero quedarme acá',
    'y ir a correr a la montaña'

]

texto5 = [
    
    'Serás el maestro más importante',
    'del futuro solorpunk',
    '',
    'Tus estudiantes me crearan en un futuro',
    "",
    'Y junto con ellos crearemos un futuro mejor',
    "",
    'Además no te estoy preguntando!'
]

texto6 = [
    'AAAAAAAAGGGGGHHHHHHH'
]

texto7 = [
    'Y asi fue como el maestro del solar punk',
    'no tuvo otra opción más que aprender del futuro',
    'que el ayudaria a crear',
]

texto8 = [
    'Una vez en el futuro no tenía idea de adonde ir',
    '',
    'Lo uncio que se encontraba a la vista',
    'era una grandiosa bibliote arbol',
    'pero se veia MUY lejana'
]

texto9 = [
    'Mae maldita gallina zapatuda',
    '',
    'Tan mal gusto tienen mis estudiantes?',
    '',
    'Y tras de todo lo unico que hay',
    'es un arbol larguisimo'
]

texto10 = [
    'H0l4.......',
    '',
    '_--a-_-123-_'
    '',
    'S0Y 3lEF4Nt b0T'
    '',
    'L4 G4ll1nA me dij0',
    '',
    'Qu3 s1 n0 v4s a l4 bibliO O O O O t3cA',
    "con M1g0 N0 v0lv3r4s nunc4"
]

texto11 = [
    'Y asi fue como este duo inesperado partio juntos',
    '',
    'En una aventura para aprender sobre',
    'El Solar Punk',
    '',
    '',
    '',
    '',
    'Maestro de fondo: Quien es migo?'   
]


texto12 = [
    'Hola compañero, soy la gallina zapatuda',
    'y sere el guía de este viaje.',
    '',
    'Durante este viaje en el que aprenderaz', 
    'junto a Aurelio sobre el Solar Punk tendras',
    'que avanzar por 5 pisos'
    ]

texto13 = [
    'Todos tendran una tematica diferente en', 
    'la que deberas aprender para pasar un quizz',
    'que te hare sobre el piso al final',
    '',
    'Cada piso tiene un total de 10 celdas,', 
    'con un numero de discos que', 
    'varían entre 0 , 2 0 3',
    '',
    'Avanzaras la cantidad de celdas igual al',
    'resultado de un dado de cuatro caras', 
    'hazta llegar a la ultima', 
    'donde tes esperara el quizz',
    '',
    'Si fallas tendras que volver al piso anterior',
    ',pero si lo pasas podrás avanzar al siguiente'
]

texto14 = [ 
    'Di no, vamos a ver que'
]   

texto15 = [
    'Si te encuentras un disco, damelo', 
    'y te dire los conocimientos del futuro'
]

aurelio = [
'             ___...-        ',
"       ----'''       |      ",
'       | ----------- |      ',
'       | /          ||      ',
'       |/            |      ',
'        |---- __ ---/|      ',
'        || XX|  |XX ||      ',
'        |.    |,    .|      ',
"        | `........' |      ",
'        \\   ______   /      ',
'         \\  \\____/  /       ',
'      /-- \\        / |\\     ',
'  ---/ \\   \\------/  / `.\\  ',
' /---\\  \\----   ----/     \\ ',
'/     \\       \\/            '
    
]


gallina = [
'                  .._/--\\    ',
"                /-/      '`\\ ",
'                \\  ,,-\'\'"\'\'+ ',
"              |'' /───┌──┐ | ",
"              `,_-'   └──┘ \\ ",
"           ,,-''          --\\",
"|`\\ __  _.'     _--,    └┐┌┘ ",
"|  '''''    ,__.'  |     └┘\\ ",
" \\       ,_,'      |       / ",
"  \\_     '-+-------'     _/  ",
"    `.. ---------,_,____/'   ",
"      \\  \\`.     \\\\      '-. ",
"       \\  \\``''   \\\\  '---' |",
"        `. '-'     |\\  '---'|",
"          '--------' `------'",
]


dados = [
    [
        '                             \\                        /                      ',
        '                              \\                      /                       ',
        '                               \\                    /                        ',
        "     `.                                            /                  .'     ",
        '       `.                            ,,                              /       ',
        "         `.                         / \\`.                          .'        ",
        "           `.                      /   \\ `.                      .'          ",
        '             `.                   /     \\  `.                   /            ',
        "               `.                /       \\   `.               .'             ",
        '                                /         \\    `.                            ',
        '                               /           \\     `.                          ',
        '                              /             \\      `.                        ',
        '                             /               \\       `.                      ',
        '                            /                 \\        `.                    ',
        '                           /                   \\         `.                  ',
        '                          /      XXXXXXX        \\          `.                ',
        ".._                      /     XXXXXXXXXXX       \\           ',             .",
        "   ``-.._               /     XXXXXXXXXXXXX       \\            `.        .-' ",
        "         ``-.          /      XXXXXXXXXXXXX        \\             `.   .-'    ",
        '                      /       XXXXXXXXXXXXX         \\            /           ',
        '                     /         XXXXXXXXXXX           \\          /            ',
        '                    /            XXXXXXX              \\        /             ',
        '                   /                                   \\      /              ',
        '                  /                                     \\    /               ',
        '                 /                                       \\  /                ',
        '                --------------------------------------------                 ',
        "          .'                                                       `.        ",
        "       .-'                           |                               `-.     ",
        "     .'                              |                                  `.   ",
        "   .'                                |                                    `-."
    ],

    [
    '                             \\                        /                      ',
    '                              \\                      /                       ',
    '                               \\                    /                        ',
    "     `.                                            /                  .'     ",
    '       `.                            ,,                              /       ',
    "         `.                         / \\`.                          .'        ",
    "           `.                      /   \\ `.                      .'          ",
    '             `.                   /     \\  `.                   /            ',
    "               `.                /       \\   `.               .'             ",
    '                                /         \\    `.                            ',
    '                               /           \\     `.                          ',
    '                              /    XXXXX    \\      `.                        ',
    '                             /    XXXXXXX    \\       `.                      ',
    '                            /    XXXXXXXXX    \\        `.                    ',
    '                           /      XXXXXXX      \\         `.                  ',
    '                          /        XXXXX        \\          `.                ',
    ".._                      /                       \\           ',             .",
    "   ``-.._               /                         \\            `.        .-' ",
    "         ``-.          /                           \\             `.   .-'    ",
    '                      /            XXXXX            \\            /           ',
    '                     /            XXXXXXX            \\          /            ',
    '                    /            XXXXXXXXX            \\        /             ',
    '                   /              XXXXXXX              \\      /              ',
    '                  /                XXXXX                \\    /               ',
    '                 /                                       \\  /                ',
    '                --------------------------------------------                 ',
    "          .'                                                       `.        ",
    "       .-'                           |                               `-.     ",
    "     .'                              |                                  `.   ",
    "   .'                                |                                    `-."
        
    ],

    [
        '                             \\                        /                      ',
        '                              \\                      /                       ',
        '                               \\                    /                        ',
        "     `.                                            /                  .'     ",
        '       `.                            ,,                              /       ',
        "         `.                         / \\`.                          .'        ",
        "           `.                      /   \\ `.                      .'          ",
        '             `.                   /     \\  `.                   /            ',
        "               `.                /       \\   `.               .'             ",
        '                                /         \\    `.                            ',
        '                               /           \\     `.                          ',
        '                              /    XXXXX    \\      `.                        ',
        '                             /    XXXXXXX    \\       `.                      ',
        '                            /    XXXXXXXXX    \\        `.                    ',
        '                           /      XXXXXXX      \\         `.                  ',
        '                          /        XXXXX        \\          `.                ',
        ".._                      /                       \\           ',             .",
        "   ``-.._               /                         \\            `.        .-' ",
        "         ``-.          /                           \\             `.   .-'    ",
        '                      /                             \\            /           ',
        '                     /    XXXXX              XXXXX   \\          /            ',
        '                    /    XXXXXXX            XXXXXXX   \\        /             ',
        '                   /    XXXXXXXXX          XXXXXXXXX   \\      /              ',
        '                  /      XXXXXXX            XXXXXXX     \\    /               ',
        '                 /        XXXXX              XXXXX       \\  /                ',
        '                --------------------------------------------                 ',
        "          .'                                                       `.        ",
        "       .-'                           |                               `-.     ",
        "     .'                              |                                  `.   ",
        "   .'                                |                                    `-."
    ],

    [   
        '                             \\                        /                      ',
        '                              \\                      /                       ',
        '                               \\                    /                        ',
        "     `.                                            /                  .'     ",
        '       `.                            ,,                              /       ',
        "         `.                         / \\`.                          .'        ",
        "           `.                      /   \\ `.                      .'          ",
        '             `.                   /     \\  `.                   /            ',
        "               `.                /       \\   `.               .'             ",
        '                                /         \\    `.                            ',
        '                               /           \\     `.                          ',
        '                              /             \\      `.                        ',
        '                             /       XXX     \\       `.                      ',
        '                            /       XXXXX     \\        `.                    ',
        '                           /       XXXXXXX     \\         `.                  ',
        '                          /         XXXXX       \\          `.                ',
        ".._                      /           XXX         \\           ',             .",
        "   ``-.._               /                         \\            `.        .-' ",
        "         ``-.          /                           \\             `.   .-'    ",
        '                      /   XXX        XXX        XXX \\            /           ',
        '                     /   XXXXX      XXXXX      XXXXX \\          /            ',
        '                    /   XXXXXXX    XXXXXXX    XXXXXXX \\        /             ',
        '                   /     XXXXX      XXXXX      XXXXX   \\      /              ',
        '                  /       XXX        XXX        XXX     \\    /               ',
        '                 /                                       \\  /                ',
        '                --------------------------------------------                 ',
        "          .'                                                       `.        ",
        "       .-'                           |                               `-.     ",
        "     .'                              |                                  `.   ",
        "   .'                                |                                    `-."
        
    ]
]

dado_vacio = [
    '                             \\                        /                      ',
    '                              \\                      /                       ',
    '                               \\                    /                        ',
    "     `.                                            /                  .'     ",
    '       `.                            ,,                              /       ',
    "         `.                         / \\`.                          .'        ",
    "           `.                      /   \\ `.                      .'          ",
    '             `.                   /     \\  `.                   /            ',
    "               `.                /       \\   `.               .'             ",
    '                                /         \\    `.                            ',
    '                               /           \\     `.                          ',
    '                              /             \\      `.                        ',
    '                             /               \\       `.                      ',
    '                            /                 \\        `.                    ',
    '                           /                   \\         `.                  ',
    '                          /                     \\          `.                ',
    ".._                      /                       \\           ',             .",
    "   ``-.._               /                         \\            `.        .-' ",
    "         ``-.          /                           \\             `.   .-'    ",
    '                      /                             \\            /           ',
    '                     /                               \\          /            ',
    '                    /                                 \\        /             ',
    '                   /                                   \\      /              ',
    '                  /                                     \\    /               ',
    '                 /                                       \\  /                ',
    '                --------------------------------------------                 ',
    "          .'                                                       `.        ",
    "       .-'                           |                               `-.     ",
    "     .'                              |                                  `.   ",
    "   .'                                |                                    `-."
]

casilla = [
    '╔═════════════╗',
    '║ │ │ │ │ │ │ ║',
    '║ │ │ │ │ │ │ ║',
    '╚═════════════╝',
]

casilla_presente = [
    '╔═════════════╗',
    '║X│X│X│X│X│X│X║',
    '║X│X│X│X│X│X│X║',
    '╚═════════════╝',
]

dibujo_final_1 = [
    '                                  XX                                        ',
    '                                  XX                                        ',
    '                                  XX                                        ',
    '                XX                XX                                        ',
    '                  XX              XX                   XX                   ',
    '     /\\             XX            XX                XXX                     ',
    '    //\\\\       /\\     XX          XX             XXX                        ',
    '   ///\\\\\\──── //\\\\┐     XX                    XXX                /\\         ',
    '     ][      ///\\\\\\       XX                XX                  //\\\\    /\\  ',
    '   │           ][ │             XXXXXXX                       ┌///\\\\\\─ //\\\\ ',
    '   │              │           XXXXXXXXXXX                     │  ][   ///\\\\\\',
    '   │              │          XXXXXXXXXXXXX                    │         ][│ ',
    '   │  ┌────────┐  │         XXXXXXXXXXXXXXX   XXXXXXXXXXXXXX  │           │ ',
    '   │  │─│────│─│  │    XXX  XXXXXXXXXXXXXXX                   │           │ ',
    '   │  │─│────│─│  XXXXX     XXXXXXXXXXXXXXX                   │  ┌─────┐  │ ',
    '   │  │─│────│─XXX│          XXXXXXXXXXXXX                    │  │─│─│─│  │ ',
    '   │  │─│────│─│  │           XXXXXXXXXXX                     │  │─│─│─│  │ ',
    '   │  │─│────│─│  │             XXXXXXX     XX                │  │─│─│─│  │ ',
    '   │  │─│────│─│  │         XX                XXXX            │  │─│─│─│  │ ',
    '   │  └────────┘  │       XX        XX            XXXX        │  │─│─│─│  │ ',
    '   │  ┌────────┐  │    XXX          XX                XX      │  │─│─│─│  │ ',
    '   │  │─│────│─│  │  XX              XX                       │  └─────┘  │ ',
    '   │  │─│────│─│  │     _( )_        XX                 _( )_ │           │ ',
    '   │  │─│────│─│  │    (_(%)_)        XX               (_(%)_)│           │ ',
    '   │  │─│────│─│  │      (_)\\                            (_)\\ │           │ ',
    '  /\\  └────────┘  │/\\        | __    /\\       /\\      /\\     |│__      /\\ │ ',
    ' //\\\\             //\\\\       |/_/   //\\\\     //\\\\    //\\\\    |/_/     //\\\\│ ',
    '///\\\\\\           ///\\\\\\      |     ///\\\\\\   ///\\\\\\  ///\\\\\\   |│      ///\\\\\\ ',
    '  ][               ][        |       ][       ][      ][     |│        ][ │',
]

dibujo_final_2 = [

    '                  /\\                                              //\\\\         ',
    '                 //\\\\                     /\\                     ///\\\\\\        ',
    '                ///\\\\\\                   //\\\\                      ][          ',
    '       _( )_      ][     ┌────────────┐ ///\\\\\\   __O          _( )_    ┌───────',
    '   /\\ (_(%)_)            │ ┌────────┐ │   ][    / /\\_,       (_(%)_)   │ ┌───┐ ',
    '  //\\\\  (_)\\             │ │        │ │       ___/\\            (_)\\    │ └───┘ ',
    ' ///\\\\\\     | __         │ └────────┘ │           /_               | __└───────',
    '   ][       |/_/         └────────────┘    ┌────────────────────┐  |/_/        ',
    '─────────┐(```)    ,....._____             │                    │  |")         ',
    "         │ |||    |'          `````-----.  │ ┌───┐        ┌───┐ │  ||          ",
    ' ┌─────┐ │ |||    |          __         |  │ │   │   __O  │   │ │ |||          ',
    " │     │ │ |||    |        \\/ o\\      ,.'  │ └───┘  / /\\_,└───┘ │ |||          ",
    " └─────┘ │ |||    '---..   /\\__/    _,'    │      ___/\\         │ |||          ",
    "─────────┘(___)        ',.        ,.|      └───────── /_────────┘(___)         ",
    "                         `..-----'''                                           ",
    '┐─┐─┐─┐─┐─┐─┐─┐─┐─┐─┐─┐─┐─┐─┐─┐                 ┌─┌─┌─┌─┌─┌─┌─┌─┌─┌─┌─┌─┌─┌─┌─┌',
    '│ │ ═════ │║═══ │═════│ │ │ │ │                 │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │',
    '│ │ │ ║ │ │║═══ │ │ │ │ │ │ │ │                 │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │',
    '│ │ │ ║ │ │║═══ │═════│ │ __o │                 │ │ │ │__o│ │ │ │ │ │ │ __O │ │',
    '┘─┘─┘─┘─┘─┘─┘─┘─┘─┘─┘─┘ _ \\<_─┘─────────────────└─└─└─ \\<_└─└─└─└─└─└ └─ /\\_,─└',
    '                       (_)/(_)                      (_)/(_)          ___/\\     ',
    '───────────/\\─────────────────┐                 ┌────────────────────────/_────',
    '          //\\\\                │                 │            /\\                ',
    '   ,..,--///\\\\\\        /\\     │                 │  _.-----> //\\\\         /\\    ',
    "     /\\    ][       _ //\\\\    │                 │  '       ///\\\\\\       //\\\\   ",
    "    //\\\\        .--' ///\\\\\\   │                 │     /\\     ][   _-''-///\\\\\\  ",
    '   ///\\\\\\              ][     │                 │    //\\\\      _\\( )/_   ][    ',
    "     ][--''''-. \\\\_('<        │                 │   ///\\\\\\      /(O)\\          ",
    "     '           \\___)        │                 │     ][''-..                 ",
    
]

dibujo_final_3 = [

    '        /\\              /\\             /\\          /\\        /\\                ',
    '       //\\\\            //\\\\    /\\     //\\\\        //\\\\      //\\\\               ',
    '      ///\\\\\\    /\\    ///\\\\\\  //\\\\   ///\\\\\\      ///\\\\\\    ///\\\\\\      /\\      ',
    ' /\\     ][     //\\\\     ][   ///\\\\\\    ][          ][        ][       //\\\\     ',
    '//\\\\          ///\\\\\\           ][          /\\              /\\        ///\\\\\\    ',
    '//\\\\\\           ][                 /\\     //\\\\     /\\     //\\\\         ][      ',
    ' ][ ┌─────────────────────────┐   //\\\\   ///\\\\\\   //\\\\   ///\\\\\\   /\\        /\\ ',
    '    │ XXX    X   XXXX  XXXX XX│  ///\\\\\\    ][    ///\\\\\\    ][    //\\\\      //\\\\',
    ' /\\ │ X  X  X X  X  X  X  X X │    ][              ][           ///\\\\\\    ///\\\\',
    '//\\\\│ X X  X   X XX X  X  X XX│                                   ][        ][ ',
    '//\\\\\\ X  X XXXXX X XX  X  X  X│                                                ',
    ' ][ │ XXX  X   X X  X  XXXX XX│    ┌──────────┐         ┌─────────┐      ┌─────',
    '    │                         │    └──────────┘         └─────────┘      └─────',
    '    │         ┌─────┐         │   └──────────┘         └─────────┘      └──────',
    '    │         │     │         │    │        │           │       │        │     ',
    '    │         │     │         │                         ┌──────────────────────',
    '    │         │     │         │                         │                      ',
    '    │         │     │         │                         │                      ',
    '    └─────────└─────┘─────────┘                         │      ,_,...__        ',
    "                                                        │     /'      '`.      ",
    "                               _____|_____              │     |  _      '|     ",
    "                              |    ┌─┐    |             │   (_  |'             ",
    "       ________               |   ┌ _ ┐   |             │    '\\/'      ,/.\\    ",
    "      |\\       \\              |   │ - │   |             │     _       '' ||_   ",
    "      | \\ _ ' ._\\             |   └───┘   |             │     `.       ,/' '   ",
    "      |  | \\~~~/ |            |___________|             │      '-.....-'       ",
    '      |  |  \\_/  |                 /|\\                  │                      ',
    '       \\ |   Y   |                / | \\                 │                      ',
    '        \\|_ _|___|               /  |  \\                │                      ',
    '                                                        │                     ',
    
]

dibujo_final_4 = [
    "            ,_,'                                        `.....___         ",
    "          ,,/'                        XX                 |\\.-... '-.       ",
    "         ,'                            XXXX             /' |   '\\   \\      ",
    "        ,'                                XXX         ,-' ,'   XXX  '.     ",
    "    ,_..--.              XXXXXXXXXXXXXXXXXXXXX       ,/  |'   XXXXX  |     ",
    "  ,.'    ''                             XXX          |   |   XXXXXXX |     ",
    " /'       |                           XX             '   |.   XXXXX XXX    ",
    '/         |                                         XXX   \\_   XXX XXXXX   ',
    "|        |'              XX                        XXXXX   `\\     XXXXXXX  ",
    '|        |              XX                        XXXXXXX   XXX    XXXXX   ',
    '|        |.          XXX                           XXXXX   XXXXX    XXX    ',
    '|         `.        XXXXXXXXXXXXXXXXXXXXXXXXXX      XXX   XXXXXXX          ',
    "|          '\\.       XXX                                   XXXXX           ",
    "'\\           '\\_       XXX                                  XXX            ",
    "  \\_           '\\        XXX                                               ",
    '    `\\_         |                                                          ',
    "      ''-------'                                                           ",
    '                                                                           ',
    '        _____|_____                    _____|_____                 _____|__',
    '       |     ,     |                  |   ,,.._   |               |   ..   ',
    "       |    _|_    |                  |  /| `\\'\\  |               |  | \\.  ",
    " ,-----|   |''''\\  |------,    ,------| | '| `.'\\ |-----,    ,----|  |  `. ",
    " |     |   \\.  ,|  |      |    |      | `\\______' |     |    |    |  '\\._'.",
    " |     |____''''___|      |    |      |___________|     |    |    |_____'''",
    ' | `---...  /|\\ ,_______  |    |  -.  ____./|\\ __       |    |  ____   /|\\ ',
    " |         / | \\       '' |    |    `''   / | \\ '''--'  |    |      ''/ | \\",
    ' |        /  |  \\  ...__  |    |         /  |  \\        |    |       /  |  ',
    " |  ''-....------  '      |    |     `----------        |    |  `-- ....o' ",
    " '------------------------'    '------------------------'    '-------------",
    '                                                    │                     ',
]

dibujo_final_5 = [
    "             '-._|     |                 ,,/'             XXXXXXXXX            ",
    '                 |.   ,/<._            _.-             XXX    X    XXX         ',
    "..                `-.,'    '- .___._,,''              X       X       X        ",
    " `\\_ ,----.                  .    '-..               X        X        X       ",
    "   ''     /.                 '..     '-.            X         X         X      ",
    "   |  ,,/'''\\.                 '-b.    '|           X         X         X      ",
    '   `_.-\'   ,,\'\'\'"\\      .         \'-..  |      ."". ."".       X        X      ',
    "    '''   _/   _/''`.    `-...       ''''      |   '   |        X      X       ",
    '      \'\'\'\'|   .\'    |b_      \'"-._____\'         \\     /              /\\        ',
    "           \\./'   ,/' '-...      '\\              '. .' XX__/\\__     //\\\\       ",
    "              `\\_,>._     '`._....'                '     \\    /XXXX///\\\\\\      ",
    "                     `-..    '|                          /_  _\\      ][        ",
    "                         '----'                            \\/                  ",
    '                                                                               ',
    '                                                                               ',
    '                                                                               ',
    '                                                                               ',
    '        \\ \\| |/ ╔═══╔═══════╗════╗                                             ',
    '         \\┌────┐║+ +╝ ---   ╚╗+ +║                                             ',
    '       ╔══│┌──┐│║     |X|  X ║   ║                                             ',
    '     ╔═╝ +│└──┘│╚╗    ---    ║  ╔╝                                             ',
    '    ╔╝    ────── ╚═══   ---- ╚╗═╝                                              ',
    '    ║╔═╗              ╔════╗  ╚╗                                               ',
    '    ║║ ║ ╔══════════╗ ║    ╚═╗ ║                                               ',
    '   XXXXXXXXXXXXXXXXXXXXXXXXX XXXXXX     XXXXXXXXXXXXXXXXXX      XXXXXXXXXXXXXX ',
    'XXXX   _ __   ___  _ __ __ XX    _XXXXXXX  ___  ___    __XXXXXXXX   _| | | | |X',
    "X     | '_ \\ / _ \\| '__/ _` | | | |/ _ \\  / _ \\/ __|  / _` |_  / | | | | | | | ",
    ' _ _ _| |_) | (_) | | | (_| | |_| |  __/ |  __/\\__ \\ | (_| |/ /| |_| | |_|_|_| ',
    '(_|_|_) .__/ \\___/|_|  \\__, |\\__,_|\\___|  \\___||___/  \\__,_/___|\\__,_|_(_|_|_) ',
    '      |_|                 |_|                                                 ',
    '                                                  │                     ',
    
]

dibujo_final_6 = [
    '               (  ) )_                                       (  ) )_          ',
    "               ( ` ')  )                 ,~-.                ( ` ')  )         ",
    "              (_(_.~~~'              ,~-.  ) )_             (_(_.~~~'          ",
    "                                    (  ) )_')  )                               ",
    "   ,~-.                            ( ` ')  )~~'                                ",
    "  (  ) )_                         (_(_.~~~'                                    ",
    " ( ` ')  )                                                               ,~-.  ",
    "(_(_.~~~'                                                               (  ) )_",
    "           X       X       X                                           ( ` ')  ",
    "            XX     X     XX                    °   O   °              (_(_.~~~'",
    '              XX   X   XX                      |\\_/-\\_/|                       ',
    '                X  X  X                        \\+__+__+/                       ',
    '           ____   ___  _        _    ____  ____  _   _ _   _ _  __             ',
    '          / ___| /XXX\\| |      / \\  |  _ \\|  _ \\| | | | \\ | | |/ /             ',
    "          \\___ \\|XXXXX| |     / _ \\ | |_) | |_) | | | |  \\| | ' /              ",
    '           ___) |XXXXX| |___ / ___ \\|  _ <|  __/| |_| | |\\  | . \\              ',
    '          |____/ \\XXX/|_____/_/   \\_\\_| \\_\\_|    \\___/|_| \\_|_|\\_\\             ',
    '                                                                    ___...-    ',
    "               X   X  X                                       ----'''       |  ",
    '             XX    X   X                                      | ----------- |  ',
    '            X      X    X                      .._/--\\        | /          ||  ',
    " \\ \\ | | / /                                 /-/      '`\\     |/            |  ",
    " \\ \\| |/ ╔═══╔═══════╗════╗                  \\  ,,-'''''+      |---- __ ---/|  ",
    "  \\┌────┐║+ +╝ ---   ╚╗+ +║                |'' /───┌──┐ |      || XX|  |XX ||  ",
    "╔══│┌──┐│║     |X|  X ║   ║                `,_-'   └──┘ \\      |.    |,    .|  ",
    "╝ +│└──┘│╚╗    ---    ║  ╔╝             ,,-''          --\\     | `........' |  ",
    "   ────── ╚═══   ---- ╚╗═╝   |`\\ __  _.'     _--,    └┐┌┘      \\   ______   /  ",
    "╗              ╔════╗  ╚╗    |  '''''    ,__.'  |     └┘\\       \\  \\____/  /   ",
    "║ ╔══════════╗ ║    ╚═╗ ║     \\       ,_,'      |       /    /-- \\        / |\\ ",
    "║+║          ║+║      ║+╚═╗    \\_     '-+-------'     _/  --/ \\   \\------/  / `",
]

parrafo1 = ('Ahora nuestro profesor ya no imagina, sino, conoce una ciudad donde el Sol es el'
+  'entro de todo, donde los techos brillan y resaltan con paneles que capturan energía limpia'
+ 'y silenciosa y plantas que combinan con la ciudad. El profe no puede evitar mirar cada barrio'
+ ' y visualizar el cómo producen su propia electricidad, compartiendo lo que no necesitan con los'
+ ' vecinos. No hay chimeneas ni humo; el aire huele a tierra mojada y a flores.')

parrafo2 = ('Las calles de los alrededores de lo que será su universidad de enseñanza son seguras y'
+ ' verdes. Los niños caminan o van en bicicleta a la escuela sin peligro alguno. Los autos particulares'
+ ' son raros; en su lugar, hay tranvías eléctricos, bicicletas de carga y amplias aceras. Los antiguos'
+ ' estacionamientos del TEC ahora son huertos comunitarios y plazas con bancos y juegos para sus estudiantes.')

parrafo3 = ('En cada esquina hay un “tercer espacio”: una biblioteca de herramientas, un taller de '
+ 'reparación, un jardín donde sentarse a conversar sin que nadie le pida a la gente comprar para quedarse.'
+ ' Los baños son gratuitos, los enchufes solares cargan tu celular mientras descansas, y siempre hay agua'
+ ' fresca disponible.')

parrafo4 = ('La comida crece cerca: en techos, balcones y huertos vecinales, sin venenos ni desperdicios.'
+ ' Las verduras no son perfectas, pero saben mejor. Los residuos se convierten en abono y las semillas se '
+ 'comparten.')

parrafo5 = ('El dinero no es el rey. Hay bancos de tiempo, trueque, monedas locales y “bibliotecas de cosas”.'
+ ' Reparar es más común que comprar nuevo. La riqueza se mide en salud, tiempo libre, amistades y un entorno'
+ ' vivo (y para los estudiantes del profe, con chistes de elefantes).')

parrafo6 = ('No es una tecnología fría ni distante. Es una ciudad que respira, donde la gente se conoce,'
+ ' se ayuda y vive bien sin robarle futuro a las siguientes generaciones. Eso es el solarpunk.')

def cinematica():
    """Función de cinemática inicial del juego"""

    print("\033[2J\033[H")
    
    frame_con_texto(dibujo1, texto1)

    input()

    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo1, aurelio, texto2)

    input()

    print("\033[2J\033[H")


    frame_con_texto_completo(dibujo2, gallina, texto3)

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo2, aurelio, texto4)

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo2, gallina, texto5)

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo3, aurelio, texto6)

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto(dibujo3, texto7)

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto(dibujo4, texto8)

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo4, aurelio, texto9)

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo4, elefante, texto10)

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto(dibujo4, texto11)

    input ()
    
    print("\033[2J\033[H")


    frame_con_texto_completo(dibujo5, gallina, texto12)

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo5, gallina, texto13)

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo_vacio, aurelio, texto14)

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo_vacio, elefante, texto15)

    input ()
    
    print("\033[2J\033[H")

def cinematica_restroceso(retroseso):
    """Función que muestra la cinemática de retroceso
    E: retroceso
    S: cinemática
    R: retroceso int positivo"""

    if type(retroseso)!=int:

        return 'ERROR01'

    elif retroseso<0:

        return 'ERROR02'

        

    texto_retroceso=  "S3 R3tR0SeD3r4n " + str(retroseso) + " C4SiLL4s" 

    frame_con_texto_completo(dibujo_retroseso, elefante, (
        "Al4RM4",
        "",
        "Al4RM4",
        "",
        "Al4RM4",
        "",
        "NINGÚN DISCO ENCONTRADO!!!"
        
    ))

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo_retroseso, elefante, [texto_retroceso])

    input ()
    
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo_retroseso, aurelio, ["Mae manda huevo!"])

    input()

    print("\033[2J\033[H")


def cinematica_quizz(pregunta, respuestas, num_pregunta):
    """Función que da la cinemática para los quizzes
    E: pregunta, respuestas, numero de pregunta
    S: cinemática
    R: preguntas y respuestas deben ser listas, num_pregunta entero positivo"""

    if type(pregunta)!=str or type(respuestas)!=list or type(num_pregunta)!=int:

        return 'ERROR01'

    elif num_pregunta<0:

        return 'ERROR01'
        
        
    pregunta = separar(pregunta)

    respuestas = separar_listas(respuestas)

    num_pregunta_texto = "Listo para tu pregunta número " + str(num_pregunta+1) + " ?"

    frame_con_texto_completo( dibujo5, gallina, [num_pregunta_texto])
    
    input()
    
    print("\033[2J\033[H")



    quizz = pregunta + ["", ""] + respuestas[0] + [""] + respuestas[1] + [""] + respuestas[2] + [""] + respuestas[3]  
    
    frame_con_texto_completo( dibujo5, aurelio, ["Siempre Listo"])

    input()
    
    print("\033[2J\033[H")


    frame_con_texto_completo( dibujo5, gallina, quizz)


    print("")
    print("")
    print("#####################################################################")
    respuesta = input_vigilado()
    print("#####################################################################")

    input()
    
    print("\033[2J\033[H")

    respuesta_aurelio = "La respuesta es " + respuesta + " !!!"
    
    frame_con_texto_completo( dibujo5, aurelio,[respuesta_aurelio])

    input()
        
    print("\033[2J\033[H")    
    
    return respuesta

def cinematica_quizz_incorrecta():
    """Función que brinda la cinemática del quizz cuando da False"""

    frame_con_texto_completo(dibujo5, gallina, ["Te equivocas", "", "AHORA TENDRÁS QUE VOLVER!"])

    input()
    
    print("\033[2J\033[H")
    

    frame_con_texto_completo(dibujo5, aurelio, ["Mae manda huevo", "", "No ve que voy en bicicleta"])

    input()
    
    print("\033[2J\033[H")
    

    frame_con_texto_completo(dibujo5, gallina, "Adiós")

    input()
    
    print("\033[2J\033[H")

def input_vigilado():
    """Función que revisa que el input del usuario esté dentro de los valores, de no ser así se vuelve
    a ejecutar hasta que de un valor correcto"""

    input_valido = False

    input_usuario = ""

    while input_valido == False:

        input_usuario = input()

        if input_usuario == "1"\
        or input_usuario == '2'\
        or input_usuario == '3'\
        or input_usuario == '4':
            input_valido = True

    return input_usuario
    

def cinematica_quizz_correcta():
    """Función que brinda la cinemática del quiz cuando este es acertado"""

    frame_con_texto_completo(dibujo5, gallina, ["Bien hecho maestro", "", "Podrás avanzar"])

    input()
    
    print("\033[2J\033[H")

    
    frame_con_texto_completo(dibujo5, aurelio, ["Si mae, es que eso funciona como así", "", "y eso..."])

    input()
    
    print("\033[2J\033[H")


def cinematica_quizz_pre_quizz():
    """Función que da la cinemática antes de iniciar los quizzes"""
    
    frame_con_texto_completo( dibujo5, gallina, ["Ahora tendrás que demostrar tu aprendizaje"])

    input()

    print("\033[2J\033[H")

    frame_con_texto_completo( dibujo5, aurelio, ["Una Gallina Zapatuda", "", "NO ME DETENDRA"])
    
    input()
    
    print("\033[2J\033[H")

def cinematica_dado(dado):
    """Función que da la cinemática del dado de acuerdo a su cara
    E: dado
    S: cinemática
    R: dado solo puede ser 1,2,3,4"""

    if type(dado)!=int:

        return 'ERROR01'
        
    elif dado<1 or dado>4:

        return 'ERROR02'


    frame_con_texto_completo(dado_vacio, aurelio, "Lets go GAMBLING")

    input()

    print("\033[2J\033[H")
    

    if dado == 1:
        frame_con_texto_completo(dados[0], aurelio, ["Mae, Mae, Eso de apostar no prome"])

    if dado == 2:
        frame_con_texto_completo(dados[1], aurelio, "Diay...")

    if dado == 3:
        frame_con_texto_completo(dados[2], aurelio, "VAMOOOS")

    if dado == 4:
        frame_con_texto_completo(dados[3], aurelio, ["VIVA LA LUDOPATIA"])

    input()

    print("\033[2J\033[H")
    

def separar_listas(listas):
    """Función que llama recursivamente a separar() para hacerlo en todas las listas
    E: listas
    S: listas
    R: listas debe ser lista"""

    if type(listas)!=list:

        return 'ERROR01'
        
    
    i = 0
    largo = len(listas)
    res = []
    while i < largo:
        res += [separar(listas[i])]
        i += 1
    return res
    


def cinematica_avanzar(pistas, discos):
    """Función que presenta las pistas y discos 
    E: pistas, discos
    S: cinemática
    R: pistas sea lista y discos sea int"""

    if type(pistas)!=list or type(discos)!=int:

        return 'ERROR01'
        

    texto_avanzar = "H4Y " + str(discos) + " D1sC0s, C3Rc4n0s"
    
    frame_con_texto_completo(dibujo_avanzar, elefante, ["AL3RTA, AL3RT4,", texto_avanzar ] )
    input ()
     
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo_avanzar, aurelio, ["Ya, ya, ya pongo los discos"])


    input ()
     
    print("\033[2J\033[H")


    cantidad = len(pistas)

    i = 0 

    while i < cantidad:

        
        pista_numero =  "Pista número " + str(pistas[i][0]) + ":"
        pista_dar = separar(pistas[i][1])
        
        frame_con_texto_completo( dibujo_avanzar, elefante_capsula, [
        pista_numero,
        "",
        ] + pista_dar)

        input ()
        
        print("\033[2J\033[H")

        i += 1

def cinematica_cierre():
    """Función que presenta la cinemática de cierre"""

    global parrafo1, parrafo2, parrafo3, parrafo4, parrafo5, parrafo6
    
    frame_con_texto_completo(dibujo5, gallina, ["Ahora podrás volver al futuro", "con lo aprendido"] )
    input ()
    
    print("\033[2J\033[H")

    frame_con_texto_completo(dibujo3, aurelio, ["AAAAAAAAAAAAAAAAAA"] )
    input ()

    print("\033[2J\033[H")


    frame_con_texto(dibujo3, ["Y así fue como nuestro querido profesor llegó a ser como es"] )
    input ()

    print("\033[2J\033[H")


    parrafo1 = separar(parrafo1)

    parrafo2 = separar(parrafo2)

    parrafo3 = separar(parrafo3)

    parrafo4 = separar(parrafo4)

    parrafo5 = separar(parrafo5)

    parrafo6 = separar(parrafo6)

    frame_con_texto(dibujo_final_1, parrafo1)
    input ()

    print("\033[2J\033[H")

    frame_con_texto(dibujo_final_2, parrafo2)
    input ()

    print("\033[2J\033[H")

    frame_con_texto(dibujo_final_3, parrafo3)
    input ()

    print("\033[2J\033[H")

    frame_con_texto(dibujo_final_4, parrafo4)
    input ()

    print("\033[2J\033[H")

    frame_con_texto(dibujo_final_5, parrafo5)
    input ()

    print("\033[2J\033[H")

    frame_con_texto(dibujo_final_6, parrafo6)
    input ()

    print("\033[2J\033[H")

    


def mostrar_mapa():
    """Función que muestra el mapa"""
    
    global celda_actual

    i = 0
    mapa = []

    mapa_fila = ['', '', '', '']

    while i < 5:
        if celda_actual == i:
            mapa_fila[0] += casilla_presente[0]
            mapa_fila[1] += casilla_presente[1]
            mapa_fila[2] += casilla_presente[2]
            mapa_fila[3] += casilla_presente[3]

        else:
            mapa_fila[0] += casilla[0]
            mapa_fila[1] += casilla[1]
            mapa_fila[2] += casilla[2]
            mapa_fila[3] += casilla[3]

        i += 1

    mapa += mapa_fila
    mapa_fila = ['', '', '', '']
        
    while i < 10:
        if celda_actual == i:
            mapa_fila[0] += casilla_presente[0]
            mapa_fila[1] += casilla_presente[1]
            mapa_fila[2] += casilla_presente[2]
            mapa_fila[3] += casilla_presente[3]

        else:
            mapa_fila[0] += casilla[0]
            mapa_fila[1] += casilla[1]
            mapa_fila[2] += casilla[2]
            mapa_fila[3] += casilla[3]
            
        i += 1
        
    mapa += mapa_fila


    frame_con_texto_completo(mapa, elefante, ["Estás aquí!"]
    )
    frame_con_texto_completo('', aurelio, ["Okey!"])

    input ()
    
    print("\033[2J\033[H")

     

def separar(texto):
    """Función que separa los textos para que quepan luego dentro
    de la cinemática """

    res = []
    oracion = ""
    palabra = ""
    i = 0
    largo = len(texto)

    while i < largo:
                
                if texto[i] != ' ':
                    palabra += texto[i]
                else:

                    if oracion == "":
                        oracion = palabra
                    
                    elif (len(oracion) + 1 + len(palabra)) <= 44:
                        oracion = oracion + " " + palabra
                    else:
                        res += [oracion]
                        oracion = palabra
                    palabra = ""
                        
                i += 1

    if (len(oracion) + 1 + len(palabra)) <= 44:
        oracion += " " + palabra
        res += [oracion]
    else:
        res += [oracion]
        res += [palabra]

    

    return res
    
            

def frame_con_texto_completo(frame, personaje, texto):
    """Función que muestra el frame con sus respectivo personaje, texto, y frame
    E: frame, personaje, texto
    S: frame con texto completo"""

    imprimir_dibujo(frame)

    cuadro_texto_dialogo(personaje, texto)


def frame_con_texto(frame, texto):
    """Función que imprime el frame con el texto
    E: frame y texto
    S: frame con texto"""

    imprimir_dibujo(frame)

    cuadro_texto_simple(texto)  

    return "frame con texto imprimido"  

def cuadro_texto_dialogo(personaje, texto):
    """Función que imprime el personaje con el texto
    E: personaje y texto
    S: personaje con texto"""

    print("###############################################################################")
    texto_dialogo(personaje, texto)
    print("###############################################################################")


def cuadro_texto_simple(texto):
    """Función que imprime el texto en un cuadro
    E: texto
    S: texto"""
    
    print("###############################################################################")
    texto_simple(texto)
    print("###############################################################################")

def texto_dialogo(personaje,texto_dialogo):
    """Función que imprime el texto con el dialogo
    E: dialogo y texto
    S: dialogo con texto"""
    
    i = 0
    
    if len(texto_dialogo) < 15:
        texto_dialogo = texto_dialogo_largo_15(texto_dialogo)

    while i < 15:
        print(texto_79_char_dialogo(personaje[i], texto_dialogo[i]))
        i += 1

    return "texto simple hecho"

def texto_dialogo_largo_15(texto_dialogo):
    """Función que imprime el texto con un largo de 15
    E: texto
    S: texto con 15 de largo"""

    i = 0

    largo_texto = 15 - len(texto_dialogo)
    mitad = largo_texto // 2
    extra = largo_texto % 2
    texto_dialogo_res = []
    while i < mitad:

        texto_dialogo_res += ['']
        i += 1
    texto_dialogo_res += texto_dialogo

    i=0

    while i < mitad+extra:

        texto_dialogo_res += ['']
        i += 1
    return texto_dialogo_res
            

def texto_simple(texto):
    """Función que imprime el texto
    E: texto
    S: texto simple"""

    i = 0 
    largo = len(texto)

    while i < largo:
        print(texto_79_char(texto[i]))
        i += 1

    return "texto simple hecho"

def texto_79_char_dialogo(personaje, texto):
    """Función que imprime el personaje con el texto en 79 de largo
    E: personaje y texto
    S: personaje con texto en 79 de largo"""

    if texto == "":

        return "# " + personaje + " # "  + "                                             #"


    largo_centro = 45 - len(texto)
            
    texto_nuevo = ''
    
    mitad = largo_centro // 2
    extra = largo_centro % 2
            
    i = 0
    
    while i < mitad:
    
        texto_nuevo += " "
        
        i += 1
        
    texto_nuevo += texto
    
    i = 0
    
    while i < mitad + extra:
    
        texto_nuevo += " "
        
        i += 1
        
    texto_nuevo += '#'
    
    return "# " + personaje + " # "  + texto_nuevo
    


def texto_79_char(texto):
    """Función que imprime el texto con 79 de largo
    E: texto
    S: texto con 79 de largo"""

    largo_centro = 77 - len(texto)
    texto_nuevo = '#'
    mitad = largo_centro // 2
    extra = largo_centro % 2
    i = 0
    while i < mitad:
        texto_nuevo += " "
        i += 1
    texto_nuevo += texto        
    i = 0
    while i < mitad + extra:
        texto_nuevo += " "
        i += 1
    texto_nuevo += '#'
    return texto_nuevo


def imprimir_dibujo(dibujo):
    """Función que imprime el dibujo
    E: dibujo
    S: dibujo"""

    i = 0
    while i < len(dibujo):
        print(dibujo[i])
        i += 1

    return "Dibujo imprimido"
    

print(iniciar_juego())




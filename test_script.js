
const EDITION = "2026-10-30";
const DATA = [
  {
    "kind": [
      "beca"
    ],
    "name": "FUAS — Admisión 2027 (Gratuidad y Beneficios Estatales)",
    "org": "Mineduc",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Formulario único para optar a Gratuidad, becas de arancel (Bicentenario, Juan Gómez Millas, BEA, etc.) y créditos FSCU. Obligatorio para estudiantes nuevos y quienes aún no tienen beneficio de arancel.",
    "fund": "100% de arancel regulado y matrícula (Gratuidad) o arancel de referencia",
    "req": "Pertenecer a los deciles/tramos socioeconómicos exigidos por cada beneficio (hasta el 60% para Gratuidad; 70-80% para becas); requisitos académicos según beneficio.",
    "deadline": "2026-11-05",
    "status": "abierta",
    "apply": "https://fuas.cl",
    "src": "https://portal.beneficiosestudiantiles.cl",
    "note": "Plazo extendido al 5 de nov. NSE: 17-dic-2026 · Preselección: 15-ene-2027 · Asignación: 10-mar-2027 · Apelación: 10–25 mar 2027."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Gratuidad Universitaria",
    "org": "Mineduc",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Financia matrícula y arancel regulado durante la duración formal de la carrera en instituciones adscritas (la UTFSM está adscrita).",
    "fund": "100% arancel regulado + matrícula durante años formales",
    "req": "Hogar dentro del 60% de menores ingresos; completar FUAS; no poseer título profesional previo.",
    "deadline": "2026-11-05",
    "status": "abierta",
    "apply": "https://fuas.cl",
    "src": "https://portal.beneficiosestudiantiles.cl/gratuidad",
    "note": "Postulación y renovación vía FUAS."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Beca Bicentenario",
    "org": "Mineduc",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Cubre el arancel de referencia en universidades del CRUCh y privadas acreditadas por al menos 4 años.",
    "fund": "Arancel de referencia anual",
    "req": "Hasta el 70% de menores ingresos; puntaje PAES según bases.",
    "deadline": "2026-11-05",
    "status": "abierta",
    "apply": "https://fuas.cl",
    "src": "https://portal.beneficiosestudiantiles.cl",
    "note": "Vía FUAS."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Beca Juan Gómez Millas",
    "org": "Mineduc",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Beca de arancel dirigida a estudiantes de sectores vulnerables que ingresan a instituciones de educación superior acreditadas.",
    "fund": "Hasta ~$1.150.000 anuales de arancel",
    "req": "Hasta el 70% de menores ingresos; puntaje PAES y notas de enseñanza media.",
    "deadline": "2026-11-05",
    "status": "abierta",
    "apply": "https://fuas.cl",
    "src": "https://portal.beneficiosestudiantiles.cl",
    "note": "Vía FUAS."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Beca Excelencia Académica (BEA)",
    "org": "Mineduc",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Premia al 10% de mejor rendimiento de la promoción de egreso de enseñanza media de colegios subvencionados.",
    "fund": "Hasta ~$1.150.000 anuales",
    "req": "Estar dentro del 10% mejor NEM de la promoción de egreso; hasta el 80% de menores ingresos; completar FUAS.",
    "deadline": "2026-11-05",
    "status": "abierta",
    "apply": "https://fuas.cl",
    "src": "https://portal.beneficiosestudiantiles.cl",
    "note": "Asignación automática cruzando notas con Mineduc tras completar FUAS."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Beca Hijos de Profesionales de la Educación",
    "org": "Mineduc",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Beneficio de arancel para hijos/as de profesores o asistentes de la educación en colegios subvencionados.",
    "fund": "Hasta ~$500.000 anuales",
    "req": "Padre o madre docente/asistente de la educación; NEM ≥ 5,5; hasta el 80% de menores ingresos.",
    "deadline": "2026-11-05",
    "status": "abierta",
    "apply": "https://fuas.cl",
    "src": "https://portal.beneficiosestudiantiles.cl",
    "note": "Vía FUAS."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Fondo Solidario de Crédito Universitario (FSCU) / Nuevo FES",
    "org": "Mineduc",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Crédito para universidades del Consejo de Rectores (CRUCh, incluida la USM). Tasa de interés fija del 2% anual con pago contingente al ingreso.",
    "fund": "Cubre hasta el 100% del arancel de referencia no cubierto por becas",
    "req": "Hasta el 80% de menores ingresos; puntaje PAES mínimo; FUAS.",
    "deadline": "2026-11-05",
    "status": "abierta",
    "apply": "https://fuas.cl",
    "src": "https://portal.beneficiosestudiantiles.cl",
    "note": "El FES (Financiamiento para la Educación Superior) se encuentra en tramitación legislativa como sucesor."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Beca de Alimentación para la Educación Superior (BAES)",
    "org": "JUNAEB",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Tarjeta electrónica mensual (Edenred/Sodexo) para compra de productos alimenticios.",
    "fund": "~$45.000 mensuales durante 10 meses al año",
    "req": "Asignación automática para beneficiarios de Gratuidad o becas de arancel en los deciles 1 al 6.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.junaeb.cl/beca-de-alimentacion-para-la-educacion-superior-baes",
    "src": "https://www.junaeb.cl",
    "note": "No requiere postulación independiente; se activa con matrícula validada."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Beca Presidente de la República (Educación Superior)",
    "org": "JUNAEB",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Aporte monetario mensual de libre disposición. En educación superior opera como beneficio de renovación para quienes la obtuvieron en enseñanza media.",
    "fund": "~1,24 UTM mensuales en 10 cuotas (~$80.000/mes)",
    "req": "Tener la beca desde enseñanza media; promedio universitario mínimo ≥ 5,0; tramo socioeconómico RSH.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.junaeb.cl/beca-presidente-de-la-republica",
    "src": "https://www.junaeb.cl",
    "note": "Período de renovación entre noviembre y enero (fecha estimada)."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Beca Indígena (Educación Superior)",
    "org": "JUNAEB",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Aporte monetario de libre disposición para estudiantes de ascendencia indígena acreditada por CONADI.",
    "fund": "~$654.000 anuales distribuidos en 10 cuotas",
    "req": "Acreditación de calidad indígena (CONADI); promedio ponderado ≥ 4,5; RSH hasta 60%.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.junaeb.cl/beca-indigena",
    "src": "https://www.junaeb.cl",
    "note": "Convocatoria anual de postulación y renovación entre noviembre y enero (fecha estimada)."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Beca Residencia Indígena",
    "org": "JUNAEB",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Valparaíso",
    "desc": "Subsidio para cubrir gastos de arriendo o pensión para estudiantes indígenas que se trasladan desde sus localidades de origen a estudiar a Valparaíso.",
    "fund": "Aporte mensual de arriendo (~$100.000/mes) o cupo en hogar universitario",
    "req": "Calidad indígena; estudiar en una comuna distinta a la de residencia familiar; RSH hasta 60%.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.junaeb.cl/beca-residencia-indigena",
    "src": "https://www.junaeb.cl",
    "note": "Postulación anual en marzo (fecha estimada)."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Tarjeta Nacional Estudiantil (TNE Pase Escolar)",
    "org": "JUNAEB",
    "area": "Becas estatales",
    "scope": "Chile",
    "city": "Valparaíso / Gran Santiago",
    "desc": "Pase que garantiza tarifa rebajada en el transporte público (metro de Valparaíso, microbuses y metro de Santiago) las 24 horas, los 365 días del año.",
    "fund": "Rebaja del ~66% en pasajes de transporte público",
    "req": "Estudiante regular de educación superior; fotografía y pago de revalidación anual a través de la universidad.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.tne.cl",
    "src": "https://www.tne.cl",
    "note": "Revalidación de sello anual entre marzo y mayo de cada año."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Arancel Ajustado por Nivel Socioeconómico — UTFSM",
    "org": "UTFSM · Dirección de Relaciones Estudiantiles",
    "area": "Becas USM",
    "scope": "Chile",
    "city": "Valparaíso / Santiago",
    "desc": "Beneficio institucional que recalcula y reduce el arancel real para aquellos estudiantes que no cuentan con Gratuidad, según su tramo de ingresos.",
    "fund": "Rebaja sustancial del arancel anual según tramo socioeconómico",
    "req": "Estudiante regular de pregrado diurno; acreditación socioeconómica mediante el portal SIREB USM.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://sireb.usm.cl",
    "src": "https://usm.cl",
    "note": "Convocatoria informada por la DRE hacia fin de año lectivo (fecha estimada)."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Beca de Matrícula USM",
    "org": "UTFSM · DRE",
    "area": "Becas USM",
    "scope": "Chile",
    "city": "Valparaíso / Santiago",
    "desc": "Exención porcentual del arancel básico semestral de matrícula para estudiantes sin gratuidad.",
    "fund": "75% (deciles 1–4), 50% (decil 5) y 25% (decil 6) del valor de la matrícula",
    "req": "No contar con beneficio estatal que cubra el derecho básico de matrícula; RSH acreditado.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://sireb.usm.cl",
    "src": "https://usm.cl",
    "note": "Porcentajes oficiales vigentes. Tramitar vía asistente social del campus."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Becas Internas de Apoyo UTFSM (Casino, Residencia y Materiales)",
    "org": "UTFSM · DRE / Red Alumni",
    "area": "Becas USM",
    "scope": "Chile",
    "city": "Valparaíso / Santiago",
    "desc": "Conjunto de beneficios complementarios: almuerzo diario en casino institucional, subsidios de residencia y préstamos de equipos computacionales/TIC.",
    "fund": "Almuerzos diarios cubiertos + subsidio de mantención",
    "req": "Evaluación de vulnerabilidad con la Asistente Social de la DRE; alumno regular.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://sireb.usm.cl",
    "src": "https://usm.cl",
    "note": "Postulaciones periódicas en portal SIREB."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Ayudantías Remuneradas Depto. de Física UTFSM",
    "org": "UTFSM · Departamento de Física",
    "area": "Becas USM",
    "scope": "Chile",
    "city": "Valparaíso",
    "desc": "Ayudantías de cátedra, laboratorio y apoyo a la investigación en los cursos de física para ingenierías (FIS 100, 110, 120, física moderna, etc.).",
    "fund": "Remuneración mensual fijada por horas semanales cronológicas",
    "req": "Haber aprobado la asignatura con calificación destacada; postular en el llamado departamental.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://fis.usm.cl",
    "src": "https://fis.usm.cl",
    "note": "Llamado abierto al inicio de cada semestre (marzo y agosto)."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Intercambio Estudiantil UTFSM (Convenios Bilaterales / Erasmus+)",
    "org": "UTFSM · Dirección de Relaciones Internacionales (DRI)",
    "area": "Movilidad internacional",
    "scope": "Internacional",
    "city": "Alemania, Francia, España, Japón, etc.",
    "desc": "Semestre o año académico de intercambio en prestigiosas universidades internacionales socias con exención de arancel en destino y cupos de beca Erasmus+ KA171.",
    "fund": "Exención total de arancel en la universidad de destino + posibles fondos Erasmus+ (~€850/mes + viaje)",
    "req": "Tener al menos el 40-50% del plan de estudios aprobado; promedio ponderado destacado; certificado de idioma (inglés/alemán/francés).",
    "deadline": null,
    "status": "reabre",
    "apply": "https://usm.cl/internacional/",
    "src": "https://usm.cl",
    "note": "Dos convocatorias por año (apertura en abril para intercambio el 1º semestre siguiente; apertura en septiembre para el 2º semestre)."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Becas Alianza del Pacífico — Movilidad de Pregrado",
    "org": "AGCID Chile · Alianza del Pacífico",
    "area": "Movilidad internacional",
    "scope": "Internacional",
    "city": "México, Colombia o Perú",
    "desc": "Financia pasantías académicas de un semestre en universidades de México (e.g. UNAM, Tecnológico de Monterrey), Colombia o Perú.",
    "fund": "Pasajes aéreos ida y vuelta + estipendio mensual de manutención + seguro médico internacional",
    "req": "Estudiante regular de pregrado con ≥50% de la carrera aprobada; promedio mínimo exigido por bases; carta de aceptación de la universidad socia.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://alianzapacifico.net/becas/",
    "src": "https://www.agci.cl",
    "note": "Apertura habitual entre marzo y abril; cierre de postulaciones en mayo (fecha estimada)."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "ELAP — Emerging Leaders in the Americas Program",
    "org": "Gobierno de Canadá (Global Affairs Canada)",
    "area": "Movilidad internacional",
    "scope": "Internacional",
    "city": "Canadá (varias provincias)",
    "desc": "Becas de intercambio de 4 a 6 meses para realizar un semestre de estudios o un proyecto de investigación en universidades canadienses de primer nivel.",
    "fund": "CAD 11.100 a CAD 12.700 (cubre pasajes, visado, seguro y manutención)",
    "req": "La universidad canadiense de destino debe tener convenio con la UTFSM e ingresar la postulación institucional a nombre del alumno.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.educanada.ca/scholarships-bourses/can/institutions/elap-pfla.aspx",
    "src": "https://www.educanada.ca",
    "note": "Convocatoria anual con cierre en las instituciones canadienses hacia marzo (fecha estimada)."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Becas Santander Estudios y Movilidad Internacional",
    "org": "Banco Santander · Santander Open Academy",
    "area": "Movilidad internacional",
    "scope": "Internacional",
    "city": "Iberoamérica / Global",
    "desc": "Becas de movilidad internacional de pregrado y programas de formación online intensiva en habilidades digitales, inglés y liderazgo.",
    "fund": "Hasta €3.000 para becas de movilidad presencial / cursos gratuitos certificados",
    "req": "Estudiante de pregrado en universidad convenida (la USM participa); postulación en plataforma oficial.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://app.santanderopenacademy.com",
    "src": "https://www.santanderopenacademy.com",
    "note": "Monitorear las distintas convocatorias activas a lo largo de todo el año."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "DAAD — Becas para Cursos Universitarios de Verano en Alemania",
    "org": "DAAD Chile (Servicio Alemán de Intercambio Académico)",
    "area": "Movilidad internacional",
    "scope": "Internacional",
    "city": "Alemania (varias universidades)",
    "desc": "Cursos de 4 a 6 semanas durante el verano alemán (junio–agosto) para perfeccionar el idioma y conocer los ecosistemas de investigación de Alemania (Max Planck, Fraunhofer, Helmholtz).",
    "fund": "Beca de €1.061 + asignación para gastos de viaje + seguro médico",
    "req": "Estudiantes de pregrado con al menos dos años concluidos; nivel de alemán B1 comprobable.",
    "deadline": "2026-12-01",
    "status": "abierta",
    "apply": "https://www.daad.cl/es/encontrar-becas/becas-en-alemania/",
    "src": "https://www.daad.cl",
    "note": "Cierre habitual a inicios de diciembre de cada año. Nota: el programa DAAD RISE Germany está restringido a Norteamérica/UK y no acepta postulantes de Chile."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Beca MEXT de Pregrado (Gobierno de Japón)",
    "org": "Embajada de Japón en Chile / Monbukagakusho",
    "area": "Movilidad internacional",
    "scope": "Internacional",
    "city": "Japón (Tokio, Kioto, Osaka, etc.)",
    "desc": "Beca completa para realizar una carrera universitaria completa de 5 años en Japón (incluye 1 año preparatorio intensivo de idioma japonés).",
    "fund": "100% matrícula + estipendio mensual (~117.000 JPY) + pasajes aéreos ida y vuelta",
    "req": "Nacionalidad chilena; 17 a 24 años; rendir exámenes de matemáticas, inglés y física/química en la Embajada.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.cl.emb-japan.go.jp/itpr_es/cultura_becas_estudiar.html",
    "src": "https://www.cl.emb-japan.go.jp",
    "note": "Abre entre abril y junio de cada año. Solo aplicable si se desea reiniciar la formación universitaria en Japón."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Global Korea Scholarship (GKS Pregrado)",
    "org": "Instituto Nacional de Educación Internacional de Corea (NIIED)",
    "area": "Movilidad internacional",
    "scope": "Internacional",
    "city": "Corea del Sur",
    "desc": "Beca integral para estudios universitarios en Corea del Sur con año previo de idioma coreano.",
    "fund": "Cobertura completa de arancel, subsidio mensual, seguro y pasajes",
    "req": "Menores de 25 años con rendimiento académico de excelencia.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.studyinkorea.go.kr",
    "src": "https://www.studyinkorea.go.kr",
    "note": "Convocatoria anual vía Embajada de Corea en Santiago entre septiembre y octubre."
  },
  {
    "kind": [
      "beca"
    ],
    "name": "Becas Women in Mining & Programas STEM Mineros",
    "org": "WIM Chile · BHP · Codelco · Antofagasta Minerals",
    "area": "Becas privadas",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Iniciativas de mentoría, financiamiento parcial de estudios y acceso prioritario a prácticas para alumnas de ingenierías duras.",
    "fund": "Asignaciones económicas y mentorías especializadas",
    "req": "Ser alumna regular de una carrera de ingeniería afín a la minería y tecnología.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://wimchile.cl",
    "src": "https://wimchile.cl",
    "note": "Monitorear llamados periódicos en portales de WIM Chile y mineras."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "Mitacs Globalink Research Internship",
    "org": "Mitacs Canadá",
    "area": "General",
    "scope": "Internacional",
    "city": "Canadá (varias universidades)",
    "desc": "Pasantía de investigación intensiva de 12 semanas (mayo a octubre) junto a profesores de universidades canadienses líderes en física, datos y materiales.",
    "fund": "Totalmente financiada: pasajes aéreos, alojamiento en campus, estipendio de manutención y seguro",
    "req": "Chile es país elegible oficial; ser estudiante de pregrado full-time con 1 a 3 semestres restantes; inglés o francés fluido.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.mitacs.ca/our-programs/globalink-research-internship-students/",
    "src": "https://www.mitacs.ca",
    "note": "La cohorte 2027 cerró en septiembre de 2026; la convocatoria para el ciclo 2028 abrirá en agosto–septiembre de 2027 (fecha estimada)."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "Student Summer Research Fellowship (SSRF)",
    "org": "ETH Zürich · Department of Computer Science (D-INFK)",
    "area": "Complejidad y datos",
    "scope": "Internacional",
    "city": "Zúrich, Suiza",
    "desc": "Pasantía de investigación de verano (julio y agosto 2027) en algoritmos, computación cuántica, machine learning y sistemas complejos.",
    "fund": "Beca de CHF 1.750/mes + reembolso de pasajes aéreos + alojamiento cubierto",
    "req": "Estudiantes de pregrado o máster de cualquier país con sólidas bases computacionales, matemáticas o de física teórica.",
    "deadline": "2026-12-16",
    "status": "abierta",
    "apply": "https://inf.ethz.ch/studies/summer-research-fellowship.html",
    "src": "https://ethz.ch",
    "note": "Portal de postulación abierto del 1 de noviembre al 16 de diciembre de 2026 a las 13:00 CET. ¡Confirmado!"
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "Excellence Research Internship Program (ERIP)",
    "org": "EPFL (École Polytechnique Fédérale de Lausanne)",
    "area": "General",
    "scope": "Internacional",
    "city": "Lausana, Suiza",
    "desc": "Pasantía de investigación de 2 a 3 meses en prestigiosos laboratorios de física, microelectrónica, fotónica y materiales de la EPFL.",
    "fund": "CHF 1.800 mensuales hasta por 3 meses + exención de costos académicos",
    "req": "Estudiantes de pregrado matriculados fuera de Suiza con expedientes de alto rendimiento académico.",
    "deadline": "2026-11-30",
    "status": "abierta",
    "apply": "https://www.epfl.ch/education/international/en/exchange-programs/excellence-research-internship-program/",
    "src": "https://www.epfl.ch",
    "note": "Cierre habitual hacia el 30 de noviembre; cartas de recomendación requeridas. (Fecha estimada)."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "Kupcinet-Getz International Summer Science School",
    "org": "Weizmann Institute of Science",
    "area": "General",
    "scope": "Internacional",
    "city": "Rehovot, Israel",
    "desc": "8 semanas de inmersión en investigación (16 de junio al 12 de agosto de 2027) trabajando en proyectos de frontera en física pura y aplicada, biofísica y matemáticas.",
    "fund": "Alojamiento completo en el campus + estipendio semanal + seguro",
    "req": "Estudiantes de pregrado avanzados con excelente rendimiento de cualquier nacionalidad.",
    "deadline": "2027-01-20",
    "status": "abierta",
    "apply": "https://www.weizmann.ac.il/feinberg/kupcinet-getz-program",
    "src": "https://www.weizmann.ac.il",
    "note": "Portal de postulación abre formalmente el 20 de diciembre de 2026 y cierra el 20 de enero de 2027."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "OIST Research Internship Program",
    "org": "Okinawa Institute of Science and Technology (OIST)",
    "area": "General",
    "scope": "Internacional",
    "city": "Okinawa, Japón",
    "desc": "Estadía de investigación de 2 a 6 meses en unidades avanzadas de física cuántica, biofísica, fotónica y neurociencia computacional.",
    "fund": "Totalmente financiada: 2.400 JPY/día hábil + pasajes aéreos + alojamiento amoblado + seguro",
    "req": "Estudiantes de pregrado (en sus últimos 2 años) o máster de cualquier país.",
    "deadline": "2027-04-15",
    "status": "abierta",
    "apply": "https://admissions.oist.jp/research-internship",
    "src": "https://www.oist.jp",
    "note": "Dos convocatorias anuales: la ronda de primavera cierra el 15 de abril de 2027 (para pasantías entre octubre y marzo)."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "Visiting Student Research Program (VSRP)",
    "org": "KAUST (King Abdullah University of Science and Technology)",
    "area": "General",
    "scope": "Internacional",
    "city": "Thuwal, Arabia Saudita",
    "desc": "Pasantías de 3 a 6 meses en laboratorios de última generación en energía solar, nanotecnología, supercómputo y física de materiales.",
    "fund": "Totalmente financiada: USD $1.000/mes de estipendio + pasaje aéreo + alojamiento privado + cobertura médica completa",
    "req": "Estudiantes de pregrado que hayan completado su 3er año con promedio destacado e inglés fluido.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://vsrp.kaust.edu.sa/",
    "src": "https://vsrp.kaust.edu.sa/",
    "note": "Postulación abierta todo el año en modalidad rolling; se recomienda postular al menos 4 meses antes de la fecha tentativa de inicio."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "CERN Summer Student Programme (Non-Member States Track)",
    "org": "CERN (Organización Europea para la Investigación Nuclear)",
    "area": "Física de partículas y nuclear",
    "scope": "Internacional",
    "city": "Ginebra, Suiza",
    "desc": "8 a 13 semanas durante el verano europeo integrándose a experimentos del Gran Colisionador de Hadrones (LHC), física de aceleradores, detectores y computación.",
    "fund": "Subsidio diario de ~90 CHF/día (~€2.800/mes) + pasajes aéreos ida y vuelta + seguro médico",
    "req": "Estudiantes de física o ingeniería con al menos 3 años de estudios universitarios concluidos; dominio de inglés o francés; Chile postula como Estado no miembro.",
    "deadline": "2027-01-26",
    "status": "abierta",
    "apply": "https://careers.cern/summer",
    "src": "https://home.cern",
    "note": "Apertura a principios de noviembre y cierre habitual a fines de enero. Solicitar cartas de recomendación con anticipación (fecha estimada)."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "CERN openlab Summer Student Programme",
    "org": "CERN openlab",
    "area": "Complejidad y datos",
    "scope": "Internacional",
    "city": "Ginebra, Suiza",
    "desc": "9 semanas trabajando en proyectos de informática y computación científica de vanguardia (HPC, IA aplicada a física de partículas y arquitecturas cuánticas).",
    "fund": "Estipendio de manutención (~90 CHF/día) + subsidio de viaje",
    "req": "Estudiantes de ingeniería, ciencias de la computación, física o matemáticas de cualquier nacionalidad.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://openlab.cern/summer-student-programme",
    "src": "https://openlab.cern",
    "note": "Convocatoria anual con cierre habitual a fines de enero (fecha estimada)."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "MPIA Summer Internship",
    "org": "Max Planck Institute for Astronomy (MPIA)",
    "area": "Astronomía",
    "scope": "Internacional",
    "city": "Heidelberg, Alemania",
    "desc": "Pasantías de 2 a 3 meses (entre mayo y septiembre) en astrofísica observacional, instrumentación astronómica de precisión y modelamiento numérico.",
    "fund": "Estipendio mensual de ~€1.000 netos + cobertura de gastos de viaje y apoyo para encontrar alojamiento",
    "req": "Estudiantes de pregrado o máster en física, astronomía o ingeniería; buen dominio del inglés.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.mpia.de/students/internships",
    "src": "https://www.mpia.de",
    "note": "El llamado para el verano 2027 abre habitualmente entre diciembre y enero, cerrando a inicios de febrero (fecha estimada)."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "Undergraduate Research Internship — IMPRS Physics of Light",
    "org": "Max Planck Institute for the Science of Light (MPL)",
    "area": "Óptica y fotónica",
    "scope": "Internacional",
    "city": "Erlangen, Alemania",
    "desc": "Investigación de vanguardia en óptica cuántica, biofotónica, fibras ópticas de cristal fotónico e interacción luz-materia.",
    "fund": "Beca de investigación de ~€992/mes + apoyo para costos de viaje internacional",
    "req": "Estudiantes de pregrado con al menos 4 semestres aprobados; permanecer matriculado en su universidad de origen durante la pasantía.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://mpl.mpg.de/career/students",
    "src": "https://www.mpg.de",
    "note": "Convocatoria anual de invierno; se tramita en contacto con la International Max Planck Research School (IMPRS)."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "Max Planck School Matter to Life — URO Program",
    "org": "Max Planck School Matter to Life",
    "area": "Biofísica",
    "scope": "Internacional",
    "city": "Heidelberg / Göttingen / Múnich, Alemania",
    "desc": "10 semanas en laboratorios de vanguardia de la Sociedad Max Planck investigando en biofísica molecular, materia activa, biología sintética y física de la materia condensada biológica.",
    "fund": "Gastos de viaje internacional cubiertos + alojamiento financiado + subsidio mensual de manutención",
    "req": "Estudiantes de pregrado excepcionales de todo el mundo en física, ingeniería biomédica o química.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://mattertolife.maxplanckschools.org/",
    "src": "https://mattertolife.maxplanckschools.org/",
    "note": "Convocatoria anual de invierno (fecha estimada). Excelente encaje para el perfil de biofísica."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Prácticas en Fusión Nuclear — IPP Max Planck",
    "org": "Max Planck Institute for Plasma Physics (IPP)",
    "area": "Energía y plasmas",
    "scope": "Internacional",
    "city": "Garching y Greifswald, Alemania",
    "desc": "Prácticas de investigación en física de plasmas y fusión nuclear en los experimentos Wendelstein 7-X (stellarator) y ASDEX Upgrade (tokamak).",
    "fund": "Asignación para estudiantes según convenio (consultar con el grupo receptor)",
    "req": "Estudiantes con al menos 3 semestres aprobados en física o ingeniería con bases en electromagnetismo y física de fluidos.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.ipp.mpg.de/career",
    "src": "https://www.ipp.mpg.de",
    "note": "Admisión continua (rolling) para estadías de investigación técnica y tesis."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Pasantías por Contacto Directo — MPI-PKS & MPI-DS",
    "org": "Max Planck for the Physics of Complex Systems & Dynamics and Self-Organization",
    "area": "Complejidad y datos",
    "scope": "Internacional",
    "city": "Dresde / Gotinga, Alemania",
    "desc": "Investigación teórica y computacional en sistemas no lineales, caos cuántico, biofísica teórica y redes complejas.",
    "fund": "Financiamiento evaluado individualmente por cada director de departamento o líder de grupo",
    "req": "Contacto directo mediante carta de interés académico, CV y referencias de profesores guía.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.pks.mpg.de",
    "src": "https://www.ds.mpg.de",
    "note": "No cuentan con portal masivo; las pasantías se acuerdan directamente con los líderes científicos."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Pasantías Científicas en ISTA (Austria)",
    "org": "Institute of Science and Technology Austria",
    "area": "General",
    "scope": "Internacional",
    "city": "Klosterneuburg (Viena), Austria",
    "desc": "Pasantías individuales de investigación en física de la materia condensada, óptica cuántica y biofísica acordadas directamente con investigadores principales.",
    "fund": "Salario mensual de estudiante de investigación según convenio colectivo austríaco",
    "req": "Pregrado avanzado en física o afines; carta de interés y acuerdo previo con el PI.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://ista.ac.at/en/jobs/",
    "src": "https://ista.ac.at",
    "note": "Nota: El programa centralizado ISTernship se encuentra temporalmente en pausa; las estadías se gestionan directamente con cada profesor."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "Directorio General de Pasantías de la Sociedad Max Planck",
    "org": "Max Planck Gesellschaft (MPG)",
    "area": "General",
    "scope": "Internacional",
    "city": "Alemania (más de 80 institutos)",
    "desc": "La Sociedad Max Planck opera de forma descentralizada: no existe un único formulario global, sino que cada uno de sus 85 institutos abre vacantes específicas para estudiantes en su portal 'Jobs & Careers'.",
    "fund": "Generalmente remuneradas (~€900–€1.200/mes) o cubiertas por becas de acogida",
    "req": "Estudiantes universitarios con buen rendimiento e inglés avanzado.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.mpg.de/en/institutes",
    "src": "https://www.mpg.de",
    "note": "Usa este enlace como catálogo maestro para buscar el instituto exacto de tu especialidad (óptica, biofísica, astrofísica, etc.)."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Programa PIA (Investigación en Astronomía de Verano)",
    "org": "NSF NOIRLab · CTIO · Cerro Pachón",
    "area": "Astronomía",
    "scope": "Chile",
    "city": "La Serena",
    "desc": "Pasantía de investigación de verano (del 18 de enero al 19 de marzo de 2027) junto a astrónomos e ingenieros de Cerro Tololo, Gemini Sur y el Observatorio Vera C. Rubin.",
    "fund": "Estipendio mensual + alojamiento completo en el recinto de La Serena",
    "req": "Nacionalidad chilena o residencia permanente; cursando 3er año o superior en física, ingeniería o astronomía.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://noirlab.edu/public/careers/",
    "src": "https://noirlab.edu",
    "note": "La convocatoria para el verano 2027 cerró el 4 de octubre de 2026. La próxima abrirá en agosto–septiembre de 2027."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Tu Práctica es Central — Banco Central de Chile",
    "org": "Banco Central de Chile",
    "area": "Econofísica y finanzas",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Prácticas de verano o semestre en las divisiones de Estudios Monetarios, Mercados Financieros, Estadísticas y Tecnologías de la Información. Manejo de series de tiempo, modelamiento y analítica.",
    "fund": "Asignación económica mensual + almuerzo en casino institucional",
    "req": "Ser estudiante regular o egresado sin titularse; contar con carta de práctica obligatoria de la universidad y seguro escolar contra accidentes; Python, R o SQL valorados.",
    "deadline": null,
    "status": "abierta",
    "apply": "https://www.bcentral.cl/el-banco/trabaja-con-nosotros",
    "src": "https://www.bcentral.cl",
    "note": "El proceso abre anualmente entre octubre y noviembre para prácticas que inician en enero. ¡Revisar de inmediato en su portal!"
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Prácticas en Observatorio ALMA (Radioastronomía)",
    "org": "ALMA Observatory (JAO)",
    "area": "Astronomía",
    "scope": "Chile",
    "city": "Santiago (Vitacura) / San Pedro de Atacama",
    "desc": "Proyectos de práctica en ingeniería electrónica, criogenia de receptores de microondas, sistemas de control distribuido y procesamiento de señales astronómicas.",
    "fund": "Asignación económica + traslados y estadía en campamento OSF para faenas en Atacama",
    "req": "Alumno regular en últimos años de ingeniería civil; seguro escolar vigente.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.almaobservatory.org/es/trabaja-con-nosotros/",
    "src": "https://www.almaobservatory.org",
    "note": "Las oportunidades se publican periódicamente en el portal de empleos de ALMA."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Prácticas y Summer Students ESO Chile",
    "org": "European Southern Observatory (ESO)",
    "area": "Astronomía",
    "scope": "Chile",
    "city": "Santiago / Observatorios Paranal y La Silla",
    "desc": "Prácticas en mantenimiento e ingeniería mecánica/óptica (MSE), operaciones científicas y sistemas de software del Very Large Telescope (VLT) y del futuro ELT.",
    "fund": "Asignación de práctica mensual + vuelos y alojamiento en base astronómica",
    "req": "Estudiantes de universidades chilenas en últimos años de ingeniería; inglés técnico.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://recruitment.eso.org/",
    "src": "https://www.eso.org",
    "note": "Convocatorias de verano en octubre y postulaciones para prácticas regulares a lo largo del año."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Vera C. Rubin Observatory (LSST)",
    "org": "Rubin Observatory / NOIRLab",
    "area": "Astronomía",
    "scope": "Chile",
    "city": "La Serena / Cerro Pachón",
    "desc": "Prácticas en el observatorio que capturará el mayor censo óptico del cielo: pipelines de procesamiento masivo de datos, software de control y óptica de gran campo.",
    "fund": "Asignación mensual de práctica",
    "req": "Estudiante avanzado de ingeniería civil física, informática o afines; dominio de Linux/Python.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://rubinobservatory.org/about/careers",
    "src": "https://rubinobservatory.org",
    "note": "Revisar convocatorias abiertas en NOIRLab Careers."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Observatorio Las Campanas (LCO) & Giant Magellan Telescope",
    "org": "Carnegie Science / GMTO",
    "area": "Astronomía",
    "scope": "Chile",
    "city": "La Serena / Vallenar",
    "desc": "Prácticas en mecánica de precisión, mantenimiento de instrumentos ópticos/infrarrojos y desarrollo tecnológico para el futuro Telescopio Gigante de Magallanes (GMT).",
    "fund": "Asignación económica mensual",
    "req": "Estudiante universitario regular; seguro escolar al día; contacto con jefatura técnica.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.lco.cl",
    "src": "https://www.lco.cl",
    "note": "Postulaciones espontáneas enviando CV al departamento de operaciones técnicas."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "CCTVal — Centro Científico Tecnológico de Valparaíso",
    "org": "UTFSM · Campus Casa Central",
    "area": "Física de partículas y nuclear",
    "scope": "Chile",
    "city": "Valparaíso",
    "desc": "Centro propio de la USM. Desarrollo de detectores para el experimento ATLAS en CERN, electrónica rápida, supercómputo y física médica experimental. Ideal para articular práctica industrial/profesional con la memoria de título.",
    "fund": "Posibilidad de estipendio o ayudantía de investigación según proyecto FONDECYT/Basal",
    "req": "Ser estudiante regular de Ingeniería Civil Física de la UTFSM.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://cctval.cl",
    "src": "https://www.usm.cl",
    "note": "Contactar directamente a los profesores e investigadores del centro en el campus Casa Central."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "AC3E — Centro Avanzado de Ingeniería Eléctrica y Electrónica",
    "org": "UTFSM",
    "area": "Óptica y fotónica",
    "scope": "Chile",
    "city": "Valparaíso",
    "desc": "Centro de excelencia USM con líneas en fotónica, conversión de energía renovable, instrumentación biomédica y control inteligente de sistemas.",
    "fund": "Asignación de investigación según proyecto disponible",
    "req": "Estudiante regular USM con buen avance curricular.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://ac3e.usm.cl",
    "src": "https://ac3e.usm.cl",
    "note": "Revisar convocatorias en su sitio web o acercarse a los laboratorios en Valparaíso."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Comisión Chilena de Energía Nuclear (CCHEN)",
    "org": "CCHEN (Gobierno de Chile)",
    "area": "Física de partículas y nuclear",
    "scope": "Chile",
    "city": "Santiago (Centros La Reina y Lo Aguirre)",
    "desc": "Prácticas en los reactores nucleares de investigación RECH-1, física de plasmas densos, protección radiológica, dosimetría y aplicaciones de radioisótopos en salud e industria.",
    "fund": "Asignación mensual según disponibilidad presupuestaria",
    "req": "Carta de solicitud de práctica de la universidad y certificado de seguro escolar.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.cchen.cl",
    "src": "https://www.cchen.cl",
    "note": "Postular a través de la sección 'Trabaja con Nosotros' o contacto con Recursos Humanos."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "CINV — Centro Interdisciplinario de Neurociencia de Valparaíso",
    "org": "Universidad de Valparaíso",
    "area": "Biofísica",
    "scope": "Chile",
    "city": "Valparaíso",
    "desc": "Biofísica computacional y experimental: estudio electrofisiológico de canales iónicos, termorrecepción, modelamiento físico de membranas y redes neuronales. Ubicado en Playa Ancha, muy cerca de la USM.",
    "fund": "Posible viático de proyecto de investigación",
    "req": "Estudiantes de ingeniería física interesados en biofísica y simulación molecular; contacto con investigadores.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://cinv.uv.cl",
    "src": "https://cinv.uv.cl",
    "note": "Excelente alternativa regional para convalidar práctica profesional o tesis de biofísica."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Fundación Ciencia & Vida",
    "org": "Fundación Ciencia & Vida / USS",
    "area": "Biofísica",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Modelamiento bioinformático, biología estructural y desarrollo de plataformas biofísicas aplicadas a la biotecnología.",
    "fund": "Apoyo según proyecto activo",
    "req": "Entrevista previa y coordinación con investigador responsable.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://cienciavida.org",
    "src": "https://cienciavida.org",
    "note": "Contactar a los laboratorios de bioinformática estructural."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Biomedical Neuroscience Institute (BNI)",
    "org": "Universidad de Chile",
    "area": "Biofísica",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Microscopía avanzada de fluorescencia, análisis óptico de señalización sináptica y análisis físico de imágenes celulares complejas.",
    "fund": "Apoyo de laboratorio",
    "req": "Conocimientos en óptica, procesamiento de señales y física estadística básica.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.bni.cl",
    "src": "https://www.bni.cl",
    "note": "Coordinar con investigadores principales de líneas ópticas."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Física Médica y Radioterapia — Fundación Arturo López Pérez (FALP)",
    "org": "Fundación Arturo López Pérez",
    "area": "Física médica",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Servicio de Física Médica en el centro oncológico líder de Chile: calibración de aceleradores lineales, planificación 3D de radioterapia (IMRT, VMAT) y control de calidad dosimétrico.",
    "fund": "Convenio de práctica profesional",
    "req": "Estudiante de últimos años de ingeniería civil física con asignaturas de física de radiaciones / física nuclear aprobadas.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.falp.cl",
    "src": "https://www.falp.cl",
    "note": "Contactar al Departamento de Física Médica de FALP."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Física Médica en Grandes Clínicas Privadas",
    "org": "Clínica Alemana · Red de Salud UC CHRISTUS",
    "area": "Física médica",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Prácticas profesionales en departamentos de imagenología avanzada (resonancia magnética, TAC, medicina nuclear PET/CT) y radioterapia.",
    "fund": "Asignación según convenio clínico",
    "req": "Seguro escolar + vacunas requeridas para recintos de salud; coordinación previa con la jefatura de física médica.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.alemana.cl",
    "src": "https://www.ucchristus.cl",
    "note": "Postulaciones mediante los departamentos de docencia e investigación clínica de cada institución."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Siemens Healthineers Chile",
    "org": "Siemens Healthineers",
    "area": "Física médica",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Prácticas en el área de ingeniería de servicio y aplicaciones clínicas para equipos de diagnóstico por imágenes (resonadores magnéticos, tomógrafos, angiógrafos y ultrasonido).",
    "fund": "Práctica remunerada + beneficios de movilización",
    "req": "Estudiante regular de ingeniería; alto perfil técnico y analítico.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://jobs.siemens-healthineers.com/",
    "src": "https://www.siemens-healthineers.com/cl",
    "note": "Postulaciones a través de su portal corporativo de empleos."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "GE HealthCare Chile",
    "org": "GE HealthCare",
    "area": "Física médica",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Soporte técnico, mantenimiento y calibración de sistemas electromédicos de imagenología y medicina nuclear.",
    "fund": "Práctica remunerada",
    "req": "Estudiante de ingeniería civil; seguro escolar.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://careers.gehealthcare.com/",
    "src": "https://www.gehealthcare.com/",
    "note": "Revisar vacantes de pasantías e internships en Chile."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Instituto Milenio de Investigación en Óptica (MIRO)",
    "org": "ANID Instituto Milenio MIRO",
    "area": "Cuántica",
    "scope": "Chile",
    "city": "Concepción / Santiago",
    "desc": "Investigación de vanguardia en óptica cuántica, comunicación cuántica, estructuración espacial de luz y metrología óptica.",
    "fund": "Apoyo financiero mediante becas de pregrado de proyectos Milenio",
    "req": "Interés demostrado en óptica o física cuántica; contacto con investigadores asociados a MIRO.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://miro.cl",
    "src": "https://miro.cl",
    "note": "Reúne a investigadores de la UdeC, UChile, USACH y otras casas de estudio."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Center for Optics and Photonics (CEFOP)",
    "org": "Universidad de Concepción",
    "area": "Óptica y fotónica",
    "scope": "Chile",
    "city": "Concepción",
    "desc": "Desarrollo de sensores ópticos industriales, instrumentación optoelectrónica y redes de telecomunicaciones por fibra óptica.",
    "fund": "Asignación de proyecto según fondo de investigación",
    "req": "Estudiante avanzado de ingeniería civil física o afines.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.cefop.cl",
    "src": "https://www.cefop.cl",
    "note": "Consultar directamente las vacantes de verano para estudiantes."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "CEDENNA — Nanociencia y Nanotecnología",
    "org": "Centro para el Desarrollo de la Nanociencia y la Nanotecnología",
    "area": "Materiales y nanotecnología",
    "scope": "Chile",
    "city": "Santiago (USACH)",
    "desc": "Líneas de síntesis y caracterización de nanomateriales magnéticos, películas delgadas, nanofísica y empaques activos.",
    "fund": "Posibilidad de beca de tesista o viático de pasantía",
    "req": "Estudiante de física o ingeniería de materiales.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.cedenna.cl",
    "src": "https://www.cedenna.cl",
    "note": "Enviar manifestación de interés al área de vinculación de CEDENNA."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Laboratorios Experimentales Depto. de Física UTFSM",
    "org": "UTFSM · Casa Central",
    "area": "Materiales y nanotecnología",
    "scope": "Chile",
    "city": "Valparaíso",
    "desc": "Laboratorios de materia condensada, magnetismo, películas delgadas y óptica aplicada en la misma universidad.",
    "fund": "Convalidable académicamente; eventual ayudantía",
    "req": "Aprobación de la Jefatura de Carrera de Ingeniería Civil Física para convalidar funciones en laboratorios internos.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://fisica.usm.cl",
    "src": "https://fisica.usm.cl",
    "note": "Verifica previamente si el reglamento de tu plan permite prácticas internas y bajo qué condiciones."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Comisión para el Mercado Financiero (CMF)",
    "org": "CMF (Regulador Financiero de Chile)",
    "area": "Econofísica y finanzas",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Prácticas en áreas de análisis de riesgo sistémico, supervisión prudencial de bancos y aseguradoras, y modelamiento estocástico de mercados.",
    "fund": "Asignación mensual de práctica",
    "req": "Estudiante regular con formación matemática y estadística sólida.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.cmfchile.cl",
    "src": "https://www.cmfchile.cl",
    "note": "Postulaciones periódicas en su sección de convocatorias laborales."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Riesgo Financiero y Analytics Cuantitativo en Grandes Bancos",
    "org": "Banco BCI · Banco Santander · BICE · Banco Itaú",
    "area": "Econofísica y finanzas",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Equipos de Quantitative Risk, modelamiento de scoring crediticio, análisis de riesgo de mercado y mesas de dinero. El perfil analítico y resolutivo del ingeniero físico es altamente demandado.",
    "fund": "Práctica profesional remunerada (~$350.000–$550.000/mes)",
    "req": "Dominio de Python, SQL o R; modelos de probabilidad y estadística.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.bci.cl/trabaja-en-bci",
    "src": "https://www.santander.cl",
    "note": "Buscar 'Práctica Riesgo Cuantitativo' o 'Data Science' en sus portales y LinkedIn."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "LarrainVial & Administradoras de Fondos de Pensiones",
    "org": "LarrainVial · AFPs (Habitat, Provida, Cuprum)",
    "area": "Econofísica y finanzas",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Optimización estocástica de carteras de inversión, modelos de valoración de derivados financieros y métricas de volatilidad de activos globales.",
    "fund": "Práctica remunerada",
    "req": "Interés en finanzas cuantitativas y habilidades avanzadas en modelamiento matemático.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.larrainvial.com",
    "src": "https://www.larrainvial.com",
    "note": "Enviar postulación a través de sus plataformas de talento joven."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Centro de Energía FCFM — Universidad de Chile",
    "org": "Universidad de Chile",
    "area": "Energía y plasmas",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Modelamiento de redes eléctricas de potencia, penetración de energías renovables no convencionales (ERNC), electromovilidad y almacenamiento en baterías.",
    "fund": "Asignación según proyectos FONDEF o consultorías",
    "req": "Bases de física de fluidos, electromagnetismo y programación numérica.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://centroenergia.cl",
    "src": "https://centroenergia.cl",
    "note": "Coordinación directa con investigadores de proyectos."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "SERC Chile — Solar Energy Research Center",
    "org": "SERC Chile (ANID FONDAP)",
    "area": "Energía y plasmas",
    "scope": "Chile",
    "city": "Santiago / Antofagasta",
    "desc": "Investigación aplicada al potencial solar único del Desierto de Atacama: radiación solar, ensuciamiento (soiling) de paneles fotovoltaicos y concentración solar térmica.",
    "fund": "Viáticos de pasantía según línea de investigación",
    "req": "Estudiantes de ingeniería con interés en física de radiación y energía solar.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://sercchile.cl",
    "src": "https://sercchile.cl",
    "note": "Centro multiinstitucional con presencia en varias universidades socias."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Fraunhofer Chile Research — Centro de Tecnologías para Energía Solar (CSET)",
    "org": "Fraunhofer Chile",
    "area": "Energía y plasmas",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "I+D aplicada en desalinización solar, calor de proceso industrial, modelamiento fotovoltaico y producción de hidrógeno verde.",
    "fund": "Asignación mensual de práctica",
    "req": "Estudiante regular de ingeniería civil; manejo de simulación numérica.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.fraunhofer.cl",
    "src": "https://www.fraunhofer.cl",
    "note": "Publicaciones de vacantes en su sección de convocatorias."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "ACERA — Asociación Chilena de Energías Renovables y Almacenamiento",
    "org": "ACERA A.G.",
    "area": "Energía y plasmas",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Estudios técnicos y regulatorios de la matriz eléctrica nacional, análisis estadístico de vertimientos de energía y transición energética limpia.",
    "fund": "Asignación mensual",
    "req": "Capacidad de análisis de grandes volúmenes de datos energéticos.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://acera.cl",
    "src": "https://acera.cl",
    "note": "Postulaciones espontáneas al área de estudios."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Prácticas en Empresas de Generación Eléctrica (Enel, Engie, AES Andes)",
    "org": "Enel Chile · ENGIE Energía Chile · AES Andes",
    "area": "Energía y plasmas",
    "scope": "Chile",
    "city": "Santiago / Faenas en diversas regiones",
    "desc": "Prácticas operativas y de ingeniería en monitoreo de parques eólicos y solares, subestaciones eléctricas, análisis de fallas y telemetría de activos renovables.",
    "fund": "Asignación económica mensual (~$250.000–$400.000)",
    "req": "Alumno regular; seguro escolar al día.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.enel.cl",
    "src": "https://www.engie.cl",
    "note": "Campañas formales de reclutamiento de verano abiertas entre septiembre y noviembre."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "ENAP — Refinería Aconcagua (Concón)",
    "org": "Empresa Nacional del Petróleo (ENAP)",
    "area": "Energía y plasmas",
    "scope": "Chile",
    "city": "Concón (Región de Valparaíso)",
    "desc": "Prácticas industriales y profesionales en una de las plantas industriales más grandes de la región: instrumentación industrial, control de procesos térmicos, mecánica de fluidos y mantenimiento predictivo. A minutos de Valparaíso.",
    "fund": "Asignación mensual de práctica + transporte de acercamiento",
    "req": "Estudiante regular de ingeniería civil; seguro escolar.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.enap.cl",
    "src": "https://www.enap.cl",
    "note": "Convocatoria anual de prácticas de verano para estudiantes de la V Región."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Codelco — Programa Corporativo de Prácticas y Memorias",
    "org": "Corporación Nacional del Cobre de Chile",
    "area": "Minería",
    "scope": "Chile",
    "city": "Divisiones Ventanas (V Región), Andina, El Teniente, Norte",
    "desc": "Prácticas en automatización, física de procesos metalúrgicos, modelamiento de macizos rocosos y sensores de monitoreo continuo en faenas subterráneas y a rajo abierto. División Ventanas y Andina están en la misma Región de Valparaíso.",
    "fund": "Asignación mensual + transporte + alojamiento y alimentación en faenas cordilleranas/norte",
    "req": "Alumno regular en los últimos semestres; carta de patrocinio de la universidad.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.codelco.com/practicas-y-memorias",
    "src": "https://www.codelco.com",
    "note": "Proceso de verano abre habitualmente entre agosto y octubre. Consultar disponibilidad en su portal."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "BHP Chile (Minera Escondida y Spence)",
    "org": "BHP",
    "area": "Minería",
    "scope": "Chile",
    "city": "Santiago / Antofagasta",
    "desc": "Programas formales de práctica de verano y práctica profesional en centros integrados de operaciones remotas (CIO), automatización de perforadoras y procesamiento de minerales.",
    "fund": "Práctica remunerada de alto nivel + traslados a faena en avión",
    "req": "Estudiante de ingeniería civil en últimos dos años.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://careers.bhp.com",
    "src": "https://www.bhp.com",
    "note": "Convocatorias de verano abiertas en primavera en su portal global de talentos."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Anglo American Chile (Los Bronces y El Soldado)",
    "org": "Anglo American",
    "area": "Minería",
    "scope": "Chile",
    "city": "Santiago / Nogales (Región de Valparaíso)",
    "desc": "Operación Los Bronces y Mina El Soldado (ubicada en la provincia de Quillota, V Región). Prácticas en gestión tecnológica, eficiencia hídrica y monitoreo de relaves con sensores ópticos e instrumentación física.",
    "fund": "Asignación económica de práctica + traslados",
    "req": "Alumno regular de ingeniería.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.angloamerican.com/careers",
    "src": "https://www.angloamerican-chile.cl",
    "note": "Postulaciones a través del portal de reclutamiento de Anglo American."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Antofagasta Minerals (Grupo Luksic)",
    "org": "Antofagasta Minerals (Los Pelambres, Centinela, Antucoya)",
    "area": "Minería",
    "scope": "Chile",
    "city": "Santiago / IV y II Región",
    "desc": "Prácticas en analítica avanzada de procesos de molienda y flotación, monitoreo geotécnico de taludes con radares e instrumentación de plantas desoladoras de agua de mar.",
    "fund": "Asignación mensual + pasajes y viáticos a faena",
    "req": "Estudiante regular de ingeniería civil; seguro escolar.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.aminerals.cl",
    "src": "https://www.aminerals.cl",
    "note": "Campañas formales de atracción de talento publicadas en su sitio web."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "SQM & Albemarle — Industria del Litio y Salares",
    "org": "SQM · Albemarle Chile",
    "area": "Minería",
    "scope": "Chile",
    "city": "Salar de Atacama / Antofagasta / Santiago",
    "desc": "Física de evaporación y balance hídrico en salares, termodinámica de salmueras ricas en litio, cristalización fraccionada y monitoreo ambiental por satélite e interferometría.",
    "fund": "Práctica remunerada + vuelos y campamento en el norte",
    "req": "Estudiantes de ingeniería con fuerte base físico-química y analítica.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.sqm.com",
    "src": "https://www.albemarle.com",
    "note": "Postulación a través de sus plataformas corporativas durante el segundo semestre."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Servicio Hidrográfico y Oceanográfico de la Armada (SHOA)",
    "org": "Armada de Chile",
    "area": "Geofísica y clima",
    "scope": "Chile",
    "city": "Valparaíso (Playa Ancha)",
    "desc": "Ubicado en Valparaíso. Operación del Sistema Nacional de Alarma de Mareas (SNAM): modelamiento de propagación de ondas de tsunami, mecánica de fluidos geofísicos, batimetría acústica e instrumentación mareográfica.",
    "fund": "Práctica formativa institucional",
    "req": "Nacionalidad chilena; estudiante regular de ingeniería; contacto con el departamento técnico.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.shoa.cl",
    "src": "https://www.shoa.cl",
    "note": "Excelente encaje de geofísica y física de fluidos en la misma ciudad universitaria."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Centro Sismológico Nacional (CSN)",
    "org": "Universidad de Chile",
    "area": "Geofísica y clima",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Procesamiento de ondas sísmicas en tiempo real, física de la ruptura cosísmica, calibración de acelerómetros y estaciones sismológicas satelitales en todo Chile.",
    "fund": "Apoyo según proyectos activos",
    "req": "Formación en física ondulatoria, métodos computacionales y series de tiempo.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.csn.uchile.cl",
    "src": "https://www.csn.uchile.cl",
    "note": "Contactar al área de investigación y redes del CSN."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Dirección Meteorológica de Chile (DMC)",
    "org": "DMC (DGAC)",
    "area": "Geofísica y clima",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Modelamiento numérico de la atmósfera, física de nubes y radiación, radares meteorológicos Doppler y análisis de escenarios de cambio climático en Chile.",
    "fund": "Práctica institucional convalidable",
    "req": "Estudiante regular de física o ingeniería con bases en termodinámica y fluidos.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.meteochile.gob.cl",
    "src": "https://www.meteochile.gob.cl",
    "note": "Solicitud formal a través de Recursos Humanos de la DGAC."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "SpaceLab UChile (Laboratorio de Exploración Espacial)",
    "org": "FCFM Universidad de Chile",
    "area": "Espacial y defensa",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Diseño, ensamblaje y prueba de satélites cubesat de la serie SUCHAI: física de plasma en la ionósfera, comportamiento térmico de componentes en el vacío espacial y enlaces de telecomunicaciones satelitales.",
    "fund": "Apoyo de proyecto de investigación",
    "req": "Estudiantes con habilidades en instrumentación física, electrónica o simulación numérica.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://spel.ing.uchile.cl",
    "src": "https://spel.ing.uchile.cl",
    "note": "Contactar al equipo de ingenieros e investigadores del laboratorio SPEL."
  },
  {
    "kind": [
      "ind",
      "prof"
    ],
    "name": "ASMAR — Astilleros y Maestranzas de la Armada",
    "org": "ASMAR",
    "area": "Espacial y defensa",
    "scope": "Chile",
    "city": "Valparaíso y Talcahuano",
    "desc": "Planta de Valparaíso y Astillero de Talcahuano: ensayos no destructivos por ultrasonido y radiografía industrial en cascos de buques, metrología de precisión y física de materiales navales.",
    "fund": "Asignación según bases institucionales",
    "req": "Nacionalidad chilena; estudiante de ingeniería civil; seguro escolar.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.asmar.cl",
    "src": "https://www.asmar.cl",
    "note": "Contacto con el departamento de capacitación y RRHH de ASMAR."
  },
  {
    "kind": [
      "ind",
      "prof"
    ],
    "name": "ENAER — Empresa Nacional de Aeronáutica",
    "org": "ENAER",
    "area": "Espacial y defensa",
    "scope": "Chile",
    "city": "Santiago (El Bosque)",
    "desc": "Ensayos mecánicos y caracterización de materiales compuestos aeronáuticos, pruebas de fatiga estructural, aviónica y calibración de instrumental de vuelo.",
    "fund": "Asignación mensual de práctica",
    "req": "Nacionalidad chilena; alumno regular de ingeniería.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.enaer.cl",
    "src": "https://www.enaer.cl",
    "note": "Postulaciones mediante la gerencia de Recursos Humanos."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Fundación Data Observatory (Astrodatos y Ciencias de la Tierra)",
    "org": "Data Observatory Chile",
    "area": "Complejidad y datos",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Consorcio público-privado impulsado por los Ministerios de Ciencia y Economía y Amazon Web Services: ingesta y análisis de petabytes de datos astronómicos (ALMA, Rubin), climáticos y de recursos hídricos.",
    "fund": "Práctica remunerada",
    "req": "Dominio avanzado de Python, computación en la nube (AWS), algoritmos de machine learning.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://dataobservatory.net",
    "src": "https://dataobservatory.net",
    "note": "Postulaciones a través de su sitio web y canales de empleo científico."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Centro de Modelamiento Matemático (CMM)",
    "org": "Universidad de Chile / CNRS",
    "area": "Complejidad y datos",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Centro de excelencia internacional (Unidad Mixta Internacional CNRS): física computacional, dinámica de sistemas complejos, algoritmos de optimización para minería y biofísica computacional.",
    "fund": "Asignación de investigación según laboratorio",
    "req": "Excelente base matemática y algorítmica; contacto con investigadores.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.cmm.uchile.cl",
    "src": "https://www.cmm.uchile.cl",
    "note": "Coordinación directa con los laboratorios y áreas temáticas del CMM."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Mercado Libre, NotCo & Falabella Tech (Equipos de Data Science)",
    "org": "Startups y Empresas Tech en Chile",
    "area": "Complejidad y datos",
    "scope": "Chile",
    "city": "Santiago (modalidad híbrida/remota)",
    "desc": "Equipos avanzados de Data Science, Machine Learning y Algoritmos de Predicción. La rigurosidad analítica y matemática de los ingenieros civiles físicos es altamente apreciada para modelar redes neuronales y optimización a gran escala.",
    "fund": "Práctica remunerada competitiva (~$400.000–$650.000/mes) + equipamiento",
    "req": "Habilidades sólidas en Python, estructuras de datos, probabilidad y estadística.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://careers-meli.mercadolibre.com",
    "src": "https://www.linkedin.com/jobs",
    "note": "Buscar vacantes de 'Intern / Práctica Data Science' en sus portales de talento."
  },
  {
    "kind": [
      "ind"
    ],
    "name": "Portales Generales de Práctica Industrial",
    "org": "Bolsa de Empleo USM · Practicas.cl · LinkedIn",
    "area": "Industria y manufactura",
    "scope": "Chile",
    "city": "Nacional",
    "desc": "Plataformas de búsqueda continua para Práctica Industrial (I) en industrias manufactureras, laboratorios de control de calidad, plantas químicas, embotelladoras y fundiciones a lo largo de todo Chile.",
    "fund": "Asignaciones variables según empresa",
    "req": "CV en formato ingeniería actualizado; certificado de alumno regular.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.linkedin.com/jobs",
    "src": "https://www.usm.cl",
    "note": "Revisar semanalmente con alertas de búsqueda configuradas."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "MPQ — Max Planck Institute of Quantum Optics",
    "org": "Max Planck Society",
    "area": "Cuántica",
    "scope": "Internacional",
    "city": "Garching, Alemania",
    "desc": "Pasantías de investigación en computación cuántica, óptica cuántica, simulación y attosegundos (laboratorios de Immanuel Bloch, Ignacio Cirac, etc.).",
    "fund": "Estipendio mensual (~€900–1.100/mes) según grupo de investigación",
    "req": "Estudiante avanzado de física, ingeniería o afines; excelente expediente y carta de motivación.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.mpq.mpg.de/career",
    "src": "https://www.mpq.mpg.de",
    "note": "Postulación por contacto directo con directores de división o vía portal de vacantes."
  },
  {
    "kind": [
      "beca",
      "prof"
    ],
    "name": "MPI for Biophysics (Pasantías de investigación)",
    "org": "Max Planck Institute of Biophysics",
    "area": "Biofísica",
    "scope": "Internacional",
    "city": "Frankfurt am Main, Alemania",
    "desc": "Biofísica molecular y estructural, biología de membranas, criomicroscopía electrónica y simulación de dinámica molecular.",
    "fund": "Contrato de estudiante de investigación / estipendio mensual",
    "req": "Pregrado en física, biofísica o química; interés en modelamiento o técnicas experimentales avanzadas.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.biophys.mpg.de/career",
    "src": "https://www.biophys.mpg.de",
    "note": "Revisar posiciones abiertas para estudiantes de pregrado (HiWi / intern) o contactar al PI."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Quantitative Trading / Research Internships",
    "org": "Jane Street · Citadel · Susquehanna (SIG)",
    "area": "Econofísica y finanzas",
    "scope": "Internacional",
    "city": "Nueva York / Londres / Remoto",
    "desc": "Trading cuantitativo y modelamiento estocástico de mercados. Buscan activamente físicos y matemáticos por su habilidad en resolución de problemas complejos.",
    "fund": "Altamente remunerada (salario competitivo global + pasajes + alojamiento corporativo)",
    "req": "Habilidades excepcionales en matemáticas, probabilidad, algoritmos (Python/C++/OCaml).",
    "deadline": "2026-12-31",
    "status": "abierta",
    "apply": "https://www.janestreet.com/join-jane-street/programs-and-events/",
    "src": "https://www.janestreet.com",
    "note": "Postulaciones abiertas para el verano del hemisferio norte (jun–ago 2027). Muy selectivo."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Advanced Analytics & Quant Consulting",
    "org": "McKinsey QuantumBlack · BCG X Chile",
    "area": "Econofísica y finanzas",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Consultoría estratégica de analítica avanzada, machine learning aplicado y modelamiento predictivo en minería, retail y banca chilena.",
    "fund": "Práctica pagada (arriba del mercado local)",
    "req": "Estudiante de ingeniería civil en últimos años; sólidos conocimientos en Python, estadística y modelamiento.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://www.mckinsey.com/capabilities/quantumblack/careers",
    "src": "https://www.mckinsey.com",
    "note": "Postulaciones a través de los portales de talento joven de McKinsey y BCG Chile."
  },
  {
    "kind": [
      "prof"
    ],
    "name": "Laboratorio de Biofísica y Materia Condensada Blanda",
    "org": "FCFM U. de Chile / PUC Física",
    "area": "Biofísica",
    "scope": "Chile",
    "city": "Santiago",
    "desc": "Estudios experimentales y teóricos de reología celular, motilidad bacteriana, pinzas ópticas y materia activa.",
    "fund": "Posible viático / financiamiento de proyecto FONDECYT/Millennium",
    "req": "Contacto directo con el profesor guía; convalidable como práctica profesional previa autorización USM.",
    "deadline": null,
    "status": "permanente",
    "apply": "https://fisica.fcfm.uchile.cl",
    "src": "https://fisica.fcfm.uchile.cl",
    "note": "Convenios interuniversitarios facilitan la estadía de investigación de verano."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Colbún — Energía Renovable y Almacenamiento",
    "org": "Colbún S.A.",
    "area": "Energía y plasmas",
    "scope": "Chile",
    "city": "Quillota (V Región) / Santiago / Faenas",
    "desc": "Prácticas en plantas de generación térmica, parques solares/eólicos, sistemas BESS de baterías y optimización del despacho energético.",
    "fund": "Asignación mensual de práctica + transporte",
    "req": "Alumno regular; seguro escolar vigente.",
    "deadline": null,
    "status": "reabre",
    "apply": "https://www.colbun.cl/trabaja-con-nosotros",
    "src": "https://www.colbun.cl",
    "note": "Complejo Nehuenco en Quillota queda muy cercano a Valparaíso. Convocatoria de verano ~octubre."
  },
  {
    "kind": [
      "prof",
      "ind"
    ],
    "name": "Laboratorio de Información Cuántica UdeC",
    "org": "Universidad de Concepción",
    "area": "Cuántica",
    "scope": "Chile",
    "city": "Concepción",
    "desc": "Líneas de investigación en óptica cuántica experimental, comunicación cuántica satelital y criptografía (QKD).",
    "fund": "Apoyo de proyecto según disponibilidad",
    "req": "Contacto con investigadores del grupo de óptica/cuántica.",
    "deadline": null,
    "status": "permanente",
    "apply": "http://optica.udec.cl/",
    "src": "http://optica.udec.cl/",
    "note": "Colaboran estrechamente con el Instituto Milenio MIRO."
  }
];

const today = new Date(); today.setHours(0,0,0,0);
const fmt = new Intl.DateTimeFormat("es-CL",{day:"numeric",month:"short",year:"numeric"});
document.getElementById("editionLabel").textContent = "Base: " + EDITION + " · Fecha actual: " + fmt.format(today);
document.getElementById("editionFoot").textContent = EDITION;

const KIND = {beca:"Beca", ind:"Práctica industrial", prof:"Práctica profesional"};
const favs = new Set(JSON.parse(localStorage.getItem("radarICF_favs")||"[]"));
const saveFavs = ()=>localStorage.setItem("radarICF_favs", JSON.stringify([...favs]));

DATA.forEach(o=>{
  o.id = o.name;
  if(o.deadline){
    o._days = Math.ceil((new Date(o.deadline+"T23:59:59") - today)/864e5);
    if(o._days < 0){
      o.status = "reabre";
      o.note = (o.note ? o.note+" " : "") + "(plazo cerrado)";
      o.deadline = null;
      o._days = null;
    }
  }
});

const order = {abierta:0, permanente:1, reabre:2};
DATA.sort((a,b)=>order[a.status]-order[b.status] || (a._days??999)-(b._days??999));

function badge(o){
  if(o.status==="permanente") return {cls:"b-gray", main:"Permanente", sub:"postulación continua"};
  if(o.status==="reabre") return {cls:"b-purple", main:"Reabre pronto", sub:"vigilar portal"};
  const d = o._days;
  const cls = d<=7 ? "b-red" : d<=21 ? "b-orange" : "b-green";
  return {cls, main:fmt.format(new Date(o.deadline+"T12:00:00")), sub: d===0?"¡hoy!":d===1?"mañana":d+" días"};
}

const state = {kind:"all", q:"", area:"all", scope:"all", status:"all"};

function buildTabs(){
  const defs=[
    ["all","Todo",DATA.length],
    ["beca","Becas",DATA.filter(o=>o.kind.includes("beca")).length],
    ["ind","Práctica industrial",DATA.filter(o=>o.kind.includes("ind")).length],
    ["prof","Práctica profesional",DATA.filter(o=>o.kind.includes("prof")).length],
    ["fav","⭐ Favoritos",favs.size]
  ];
  document.getElementById("tabs").innerHTML = defs.map(([k,l,n])=>{
    return `<div class="tab${state.kind===k?' on':''}" data-k="${k}"><div class="n">${n}</div><div class="l">${l}</div></div>`;
  }).join("");
}
document.getElementById("tabs").addEventListener("click", e=>{
  const t = e.target.closest(".tab"); if(!t) return;
  state.kind = t.dataset.k;
  render();
});

// Dropdown de áreas con conteos
function buildAreaSelect(){
  const select = document.getElementById("areaSelect");
  const areas = [...new Set(DATA.map(o=>o.area))].sort();
  select.innerHTML = `<option value="all">Todas las áreas (${DATA.length})</option>` + 
    areas.map(a=>{
      const count = DATA.filter(o=>o.area===a).length;
      return `<option value="${a}">${a} (${count})</option>`;
    }).join("");
  
  select.addEventListener("change", e=>{
    state.area = e.target.value;
    render();
  });
}
buildAreaSelect();

function buildChips(id, items, key){
  const c = document.getElementById(id);
  [["all","Todas"],...items.map(x=>Array.isArray(x)?x:[x,x])].forEach(([v,l])=>{
    const el = document.createElement("span");
    el.className = "chip" + (v==="all"?" on":"");
    el.textContent = l;
    el.dataset.val = v;
    c.appendChild(el);
  });
  c.addEventListener("click", e=>{
    if(!e.target.dataset.val) return;
    state[key] = e.target.dataset.val;
    c.querySelectorAll(".chip").forEach(ch=>ch.classList.toggle("on", ch.dataset.val===state[key]));
    render();
  });
}
buildChips("fScope", ["Chile","Internacional"], "scope");
buildChips("fStatus", [["abierta","Abiertas"],["permanente","Permanentes"],["reabre","Reabren"]], "status");

document.getElementById("search").addEventListener("input", e=>{
  state.q = e.target.value.toLowerCase().trim();
  render();
});

const esc = s => (s||"").replace(/[&<>"]/g, c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

function match(o){
  if(state.kind==="fav" ? !favs.has(o.id) : (state.kind!=="all" && !o.kind.includes(state.kind))) return false;
  if(state.area!=="all" && o.area!==state.area) return false;
  if(state.scope!=="all" && o.scope!==state.scope) return false;
  if(state.status!=="all" && o.status!==state.status) return false;
  if(state.q){
    const hay = (o.name+" "+o.org+" "+o.city+" "+o.desc+" "+o.area+" "+(o.req||"")+" "+(o.note||"")).toLowerCase();
    if(!hay.includes(state.q)) return false;
  }
  return true;
}

function getGCalUrl(o){
  if(!o.deadline) return null;
  const d = o.deadline.replace(/-/g,"");
  const dates = d + "/" + d;
  const title = encodeURIComponent("Deadline: " + o.name);
  const details = encodeURIComponent(o.desc + "\n\nEnlace: " + o.apply);
  const loc = encodeURIComponent(o.org + " (" + o.city + ")");
  return `https://calendar.google.com/calendar/render?action=TEMPLATE&text=${title}&dates=${dates}&details=${details}&location=${loc}`;
}

function card(o){
  const b = badge(o);
  const mainKind = o.kind[0];
  const kt = o.kind.map(k=>`<span class="tag t-${k}">${KIND[k]}</span>`).join("");
  const gcal = getGCalUrl(o);
  
  return `<div class="card k-${mainKind}${favs.has(o.id)?' fav':''}">
    <div class="card-top">
      <div>
        <div class="inst">${esc(o.name)}</div>
        <div class="pi">${esc(o.org)}</div>
      </div>
      <div class="badge ${b.cls}">${esc(b.main)}<small>${esc(b.sub)}</small></div>
    </div>
    <div class="tags">
      ${kt}
      <span class="tag area">${esc(o.area)}</span>
      <span class="tag">📍 ${esc(o.city)}</span>
      <span class="tag">${esc(o.scope)}</span>
    </div>
    <div class="desc">${esc(o.desc)}</div>
    <div class="fund">💰 ${esc(o.fund)}</div>
    ${o.req ? `<div class="req"><b>Requisitos:</b> ${esc(o.req)}</div>` : ""}
    ${o.note ? `<div class="note">${esc(o.note)}</div>` : ""}
    <div class="links">
      <a class="lnk apply" href="${esc(o.apply)}" target="_blank" rel="noopener">Postular / Info</a>
      <a class="lnk src" href="${esc(o.src)}" target="_blank" rel="noopener">Fuente</a>
      ${gcal ? `<a class="lnk cal" href="${gcal}" target="_blank" rel="noopener" title="Agendar deadline en Google Calendar">📅</a>` : ""}
      <button class="star${favs.has(o.id)?' on':''}" data-id="${esc(o.id)}" title="Guardar en favoritos">★</button>
    </div>
  </div>`;
}

document.getElementById("grid").addEventListener("click", e=>{
  const s = e.target.closest(".star"); if(!s) return;
  const id = s.dataset.id;
  favs.has(id) ? favs.delete(id) : favs.add(id);
  saveFavs();
  render();
});

function buildCounters(list){
  const ab = list.filter(o=>o.status==="abierta");
  const defs = [
    ["c-red", ab.filter(o=>o._days<=7).length, "≤ 7 días"],
    ["c-orange", ab.filter(o=>o._days>7 && o._days<=21).length, "≤ 21 días"],
    ["c-green", ab.length, "con plazo abierto"],
    ["c-gray", list.filter(o=>o.status==="permanente").length, "permanentes"],
    ["c-purple", list.filter(o=>o.status==="reabre").length, "reabren pronto"]
  ];
  document.getElementById("counters").innerHTML = defs.map(([c,n,l])=>{
    return `<div class="counter ${c}"><b>${n}</b>${l}</div>`;
  }).join("");
}

function render(){
  buildTabs();
  const list = DATA.filter(match);
  buildCounters(list);
  document.getElementById("grid").innerHTML = list.map(card).join("");
  document.getElementById("empty").style.display = list.length ? "none" : "block";
}

// Modal
const modalOverlay = document.getElementById("modalOverlay");
document.getElementById("btnModal").addEventListener("click", ()=>modalOverlay.classList.add("open"));
document.getElementById("modalClose").addEventListener("click", ()=>modalOverlay.classList.remove("open"));
modalOverlay.addEventListener("click", e=>{ if(e.target===modalOverlay) modalOverlay.classList.remove("open"); });

// Exportar favoritos
document.getElementById("btnExport").addEventListener("click", ()=>{
  if(favs.size===0){
    alert("No tienes favoritos guardados aún. Haz clic en la estrella ⭐ de cualquier oportunidad para guardarla.");
    return;
  }
  const favItems = DATA.filter(o=>favs.has(o.id));
  let text = "=== MIS OPORTUNIDADES GUARDADAS (RADAR ICF UTFSM) ===\n\n";
  favItems.forEach((o, i)=>{
    text += `${i+1}. ${o.name} — ${o.org}\n`;
    text += `   Área: ${o.area} | Ámbito: ${o.scope} (${o.city})\n`;
    text += `   Plazo: ${o.deadline || o.status}\n`;
    text += `   Postular: ${o.apply}\n\n`;
  });
  navigator.clipboard.writeText(text).then(()=>{
    alert(`¡Se copiaron ${favItems.length} favoritos al portapapeles! Puedes pegarlos en WhatsApp, Notion o donde prefieras.`);
  }).catch(()=>{
    console.log(text);
    alert(text);
  });
});

render();

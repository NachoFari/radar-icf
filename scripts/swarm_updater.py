"""
Radar ICF - Multi-Agent Swarm Updater Architecture
--------------------------------------------------
Define la distribución de los 25 subagentes de investigación
por áreas temáticas para rastrear nuevas convocatorias, pasantías y becas.

Distribución del Enjambre (25 subagentes):
- Grupo 1 (5 agentes): Centros Internacionales (CERN, DESY, Max Planck, Weizmann, OIST).
- Grupo 2 (5 agentes): Minería, Energía e Industria (Codelco, BHP, SQM, ENAP, SGS).
- Grupo 3 (5 agentes): Deep Tech, Cuántica & Hardware (Synopsys, CoreDevX, SeQure Quantum, Lihuen).
- Grupo 4 (5 agentes): Portales de Prácticas y Empleo en Chile (FirstJob, Tu Práctica es Central, Laborum, etc.).
- Grupo 5 (5 agentes): Becas de Movilidad y Organismos Estatales/Privados (ANID, Santander, DAAD, MEXT).
"""

SWARM_CLUSTERS = {
    "Centros Internacionales": [
        {"target": "CERN Summer Student Programme", "url": "https://careers.cern/summer"},
        {"target": "DESY Summer Student Program", "url": "https://summerstudents.desy.de"},
        {"target": "Max Planck Summer Internships (IMPRS/MPI)", "url": "https://www.mpg.de"},
        {"target": "OIST Research Internship (Japón)", "url": "https://admissions.oist.jp"},
        {"target": "Weizmann Kupcinet-Getz International Summer School", "url": "https://www.weizmann.ac.il/feinberg"}
    ],
    "Minería e Industria Base": [
        {"target": "Codelco Programa Prácticas", "url": "https://www.codelco.com"},
        {"target": "BHP Minerals Americas Internships", "url": "https://careers.bhp.com"},
        {"target": "SQM Prácticas Universitarias", "url": "https://www.sqm.com"},
        {"target": "ENAP Refinerías y Energía", "url": "https://www.enap.cl"},
        {"target": "SGS & Bureau Veritas (END)", "url": "https://www.sgs.com"}
    ],
    "Deep Tech & Cuántica": [
        {"target": "Synopsys Chile Semiconductor R&D", "url": "https://www.synopsys.com"},
        {"target": "CoreDevX Applied Computing", "url": "https://coredevx.com"},
        {"target": "SeQure Quantum Hardware", "url": "https://sequrequantum.com"},
        {"target": "Lihuen Quantum Computing", "url": "https://lihuenquantum.cl"},
        {"target": "MiningTAG / Enaex Robótica", "url": "https://miningtag.com"}
    ],
    "Portales de Prácticas Chile": [
        {"target": "Tu Práctica es Central (Gobierno)", "url": "https://tupracticaescentral.serviciocivil.cl"},
        {"target": "FirstJob Chile Programas Trainee y Prácticas", "url": "https://firstjob.me"},
        {"target": "Laborum & Trabajando.com (Física e Ingeniería)", "url": "https://www.laborum.cl"},
        {"target": "Get on Board (Data Science y Software)", "url": "https://www.getonbrd.com"},
        {"target": "LinkedIn Jobs (Ingeniería Física Chile)", "url": "https://www.linkedin.com/jobs"}
    ],
    "Becas y Organismos de Movilidad": [
        {"target": "ANID Chile (Pasantías y Becas)", "url": "https://anid.cl"},
        {"target": "Becas Santander Movilidad Internacional", "url": "https://app.santanderopenacademy.com"},
        {"target": "DAAD Chile (Alemania - WISE e intercambios)", "url": "https://www.daad.cl"},
        {"target": "Embajada de Japón en Chile (MEXT Pregrado y Posgrado)", "url": "https://www.cl.emb-japan.go.jp"},
        {"target": "Fulbright Chile (Oportunidades EEUU)", "url": "https://www.fulbright.cl"}
    ]
}

if __name__ == "__main__":
    total_agents = sum(len(agents) for agents in SWARM_CLUSTERS.values())
    print(f"Arquitectura de Enjambre configurada: {total_agents} subagentes listos.")
    for cluster, agents in SWARM_CLUSTERS.items():
        print(f"  • {cluster}: {len(agents)} subagentes")

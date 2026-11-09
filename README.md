# 📡 Radar de Ingeniería Física (Chile)

[![GitHub Pages Deployment](https://github.com/NachoFari/radar-icf/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/NachoFari/radar-icf/actions/workflows/deploy-pages.yml)
[![Licencia](https://img.shields.io/badge/licencia-MIT-blue.svg)](LICENSE)
[![Hecho por](https://img.shields.io/badge/Creador-NachoFari-ff6b35.svg)](https://github.com/NachoFari)

Directorio interactivo de **prácticas industriales**, **prácticas profesionales**, **becas y pasantías de investigación** internacionales y **descuentos/perks universitarios**, enfocado en estudiantes avanzados (3er a 5to año) de **Ingeniería Física** e **Ingeniería Civil Física** de universidades chilenas (UTFSM, PUC, UChile, UdeC, USACH, etc.).

🌐 **Sitio Web en Vivo (GitHub Pages):**  
👉 **[https://nachofari.github.io/radar-icf/](https://nachofari.github.io/radar-icf/)**

---

## 🎯 Contenido y Categorías

El catálogo cuenta con **105 oportunidades activas**, categorizadas en:

1. **🏭 Práctica Industrial (I):**  
   Plantas mineras, refinerías, manufactura, ensayos no destructivos (END), geofísica de prospección e instrumentación en terreno (Codelco, BHP, SQM, ENAP, SGS, TÜV Rheinland).
2. **🔬 Práctica Profesional (II):**  
   Empresas Deep Tech, hardware cuántico, semiconductores, observatorios astronómicos, centros de I+D y finanzas cuantitativas (Synopsys Chile, SeQure Quantum, CoreDevX, ALMA, ESO, Banco Central, CCTVal).
3. **✈️ Becas y Pasantías Internacionales:**  
   Programas de verano totalmente remunerados y becas de estadía en el extranjero (CERN Summer Student, DESY, Max Planck, DAAD WISE, Weizmann Kupcinet-Getz, OIST Japón, Becas MEXT Japón).
4. **🎁 Descuentos y Beneficios Estudiantiles:**  
   Perks de software profesional, crédito cloud y hardware usando tu correo institucional (`@usm.cl` u otros correos universitarios):
   - **GitHub Student Developer Pack:** Copilot gratis, JetBrains Pro, $200 USD en DigitalOcean, dominios gratis.
   - **Wolfram Mathematica & MATLAB:** Licencias completas de campus universitario.
   - **Autodesk, Microsoft Azure ($100 USD), Notion Plus, Figma Pro, ANSYS Student.**
   - **Spotify, YouTube Premium y Apple Music para Estudiantes (50% desc.).**
   - **Samsung Portal Estudiantes (hasta 40% de descuento en tablets y laptops).**

---

## 🚀 Cómo publicar en tu GitHub Pages (Paso a Paso)

Solo necesitas 2 minutos para tenerlo publicado bajo tu usuario de GitHub:

### Paso 1: Crear el repositorio en GitHub
1. Entra a [github.com/new](https://github.com/new).
2. Nómbralo **`radar-icf`**.
3. Déjalo **Público** y **NO marques** "Initialize with README" (ya tenemos todo listo aquí).
4. Haz clic en **Create repository**.

### Paso 2: Vincular y Subir
Abre tu terminal en esta carpeta y ejecuta:
```bash
git remote add origin https://github.com/NachoFari/radar-icf.git
git push -u origin main
```

### Paso 3: Activar GitHub Pages
1. En tu repositorio en GitHub, ve a **Settings** > **Pages** (en la barra lateral izquierda).
2. En **Build and deployment > Source**, selecciona:
   - **GitHub Actions** (recomendado, usará el workflow automático `.github/workflows/deploy-pages.yml` ya incluido).
   - *O bien*, selecciona **Deploy from a branch** > branch **main** > folder **/(root)** y haz clic en **Save**.
3. ¡Listo! En ~1 minuto tu página estará activa en:  
   **`https://nachofari.github.io/radar-icf/`**

---

## 🤖 Actualización Continua y Enjambre de Subagentes

El Radar cuenta con dos mecanismos de actualización periódica:

### 1. Enjambre de 25 Subagentes en Antigravity
Cuando desees hacer un barrido masivo de convocatorias y portales, puedes pedirle a Antigravity:
> *"Actualiza el radar ejecutando el enjambre de 25 subagentes"* o utilizar el comando `/schedule`.

El coordinador divide las tareas en 5 clústeres especializados:
- **Clúster 1 (5 agentes):** Centros Internacionales (CERN, DESY, Max Planck, Weizmann, OIST).
- **Clúster 2 (5 agentes):** Minería, Energía e Industria (Codelco, BHP, SQM, ENAP, SGS).
- **Clúster 3 (5 agentes):** Deep Tech, Cuántica & Hardware (Synopsys, CoreDevX, SeQure Quantum, Lihuen).
- **Clúster 4 (5 agentes):** Portales de Empleo y Prácticas en Chile (FirstJob, Tu Práctica es Central, Laborum, etc.).
- **Clúster 5 (5 agentes):** Organismos de Becas y Movilidad (ANID, Santander, DAAD, Embajadas MEXT).

Los subagentes actualizan las fechas de cierre en `data/data.json`, detectan llamados caducados, agregan nuevas empresas y compilan el `index.html`.

### 2. GitHub Actions Semanal (Cloud)
El repositorio incluye el workflow `.github/workflows/weekly-audit.yml` configurado para ejecutarse automáticamente todos los **lunes a las 09:00 AM (hora de Chile)**, auditando la vigencia de los plazos de postulación y la salud del catálogo.

---

## 💻 Desarrollo Local

Para modificar datos o el diseño localmente:

```bash
# 1. Agregar o editar datos en data/data.json
# 2. Compilar el archivo único index.html con el tema NaTex Studio
python generate_natex_theme.py

# 3. El archivo index.html se genera automáticamente listo para abrir en cualquier navegador
```

---

## 👤 Créditos y Autoría

- **Desarrollador y Curador:** [NachoFari](https://github.com/NachoFari)
- **Tema Visual:** NaTex Studio Dark Palette (Ember Orange `#ff6b35` + Cyan `#38bdf8` + Charcoal `#0e0f13`)
- **Arquitectura:** Single-file zero-dependency responsive HTML + Vanilla JS + CSS Grid.

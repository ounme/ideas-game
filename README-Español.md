# BELIVEME: README

*Simulación basada en agentes de propagación de ideas a través de la psicología de la personalidad*

## Visión general

**BELIVEME** modela cómo las ideas se propagan, transforman y moldean comunidades. El motor combina:
- **Rasgos de personalidad** (OCEAN + Inteligencia);  
- **Dinámica de ideas** (contenido, tono emocional, distorsión);  
- **Mecanismos sociales** (influencia, adaptación, evolución).

## Componentes principales

### 1. Clase `Idea`
Representa un concepto propagable con:
- `core`: esencia textual;  
- `effects`: impactos en parámetros (p. ej., `{'C': +8, 'A': +5}`);  
- `complexity`: 0–100 (afecta la distorsión durante la transmisión);  
- `emotion`: tono emocional (p. ej., "reverencia");  
- `weight`: fuerza de la idea en la comunidad (crece con la adopción).

### 2. Clase `Agent`
Cada agente tiene 6 rasgos (0–100):
- **O** (Openness) — receptividad a nuevas experiencias;  
- **C** (Conscientiousness) — seguimiento de reglas, fiabilidad;  
- **E** (Extraversion) — actividad social;  
- **A** (Agreeableness) — empatía, amabilidad;  
- **N** (Neuroticism) — sensibilidad a amenazas;  
- **I** (Intelligence) — pensamiento crítico.

**Métodos principales**:
- `calculate_social_weight()`: calcula influencia (E×0.4 + C×0.3 + I×0.3);  
- `transmit_idea()`: envía idea con distorsión y adaptación;  
- `adapt_idea()`: modifica idea según rasgos fuente/receptor;  
- `receive_idea()`: aplica efectos con filtros (p. ej., C alto resiste cambios negativos);  
- `evolve_idea()`: actualiza complejidad y emoción de la idea post-transmisión.

### 3. Clase `Community`
Gestiona la población de agentes y la simulación:
- `add_idea()`: inyecta nuevas ideas en el sistema;  
- `step()`: ejecuta un ciclo de simulación (selección fuente → receptor → transmisión → actualización);  
- `update_history()`: registra valores promedio de rasgos;  
- `plot_history()`: visualiza tendencias de parámetros.

## Flujo de simulación

1. **Inicialización**  
   - Crear `Community(size=N)`;  
   - Añadir instancias `Idea` iniciales.

2. **Ciclo (`step()`)**  
   a. **Agente fuente** aleatorio seleccionado (debe tener ideas);  
   b. **Idea** aleatoria elegida de las creencias de la fuente;  
   c. **Receptor** seleccionado mediante probabilidad ponderada (E de la fuente × A del receptor);  
   d. **Transmisión**:  
      - Distorsión aplicada (basada en complejidad de idea e I de la fuente);  
      - Idea adaptada a rasgos fuente/receptor;  
      - Receptor actualiza rasgos y adopta idea;  
      - Idea evoluciona (complejidad/emoción cambia).  
   e. Promedios de rasgos registrados.

3. **Terminación**  
   - Después de `num_steps`, graficar resultados e imprimir estadísticas.

## Salida

1. **Registro de consola**  
   ```
   Шаг 0: средний O=49.4, C=48.9, E=50.0  
   ...  
   Симуляция завершена (100 шагов).
   ```

2. **Gráficos**  
   - Gráfico de líneas de valores promedio OCEAN+I sobre pasos.

3. **Estadísticas finales**  
   - Media/mín/máx para cada rasgo entre agentes;  
   - Tasas de adopción de ideas (p. ej., *"Соблюдай завет": 22/30 agentes*);  
   - Top 5 líderes sociales (por `social_weight`).

## Uso

1. **Instalar dependencias**  
   ```bash
   pip install matplotlib
   ```

2. **Ejecutar simulación**  
   ```bash
   python main.py
   ```

3. **Personalizar**  
   - Modificar `Community(size)` e ideas iniciales en el bloque `__main__`;  
   - Ajustar valores `effects`, `complexity` y `emotion` de las ideas.

## Parámetros y ajuste

- **Rasgos de agentes**: Inicializados aleatoriamente dentro de rangos (p. ej., O: 30–70);  
- **Distorsión**: `±0.1 × (complexity / 100)`, reducida por I de fuente, aumentada por N de receptor;  
- **Reglas de adaptación**:  
  - A alto (fuente) → suaviza texto núcleo;  
  - O bajo (receptor) → reduce complejidad;  
  - N alto (receptor) → intensifica emoción;  
- **Evolución de ideas**: `weight × 1.01` por transmisión; complejidad ±5% basada en O de fuente.

## Licencia

Licencia MIT. Ver archivo `LICENSE`.  
Copyright (c) 2024 Nickita Panin.  
*Dedicado a la gloria de Dios.*

## Contribución

Ver `HELPME.md` para formas de mejorar código, documentación o compartir el proyecto.

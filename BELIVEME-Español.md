### BELIVEME  
*Un simulador de propagación de ideas en grupos sociales a través de la lente de la psicología de la personalidad*

#### Acerca del proyecto  

**BELIVEME** es una simulación basada en agentes que modela cómo las ideas se propagan, transforman e influyen en una comunidad. La mecánica central gira en torno a la interacción de:  
- **perfiles psicológicos de los agentes** (el modelo Big Five + inteligencia);  
- **dinámica de ideas** (contenido, tono emocional, complejidad);  
- **mecanismos sociales** (influencia, confianza, conflicto).

#### Características principales  

- **Psicología realista de agentes**: cada agente tiene rasgos OCEAN (Apertura, Responsabilidad, Extraversión, Amabilidad, Neuroticismo) y una puntuación de inteligencia.  
- **Evolución de ideas**: durante la transmisión, una idea se distorsiona, se adapta a la personalidad del receptor y puede volverse más o menos compleja.  
- **Influencia social**: los agentes con alta Extraversión (E) e Inteligencia (I) propagan ideas más rápido.  
- **Conflicto y sinergia**: algunas ideas se refuerzan mutuamente, mientras que otras se suprimen.  
- **Visualización dinámica**: los gráficos muestran cambios en los parámetros de la comunidad y la propagación de ideas a lo largo del tiempo.

#### Objetivos de la simulación  

1. Explorar cómo los rasgos de personalidad afectan la percepción y transmisión de ideas.  
2. Demostrar los mecanismos de "viralidad" de las ideas en diferentes grupos sociales.  
3. Mostrar cómo los conflictos de ideas conducen a la polarización o consolidación de la comunidad.  
4. Proporcionar una herramienta para experimentar con escenarios sociales.

#### Cómo funciona  

**1. Agentes**  
Cada agente se define por seis parámetros (0–100):  
- **O (Openness)** — apertura a nuevas experiencias;  
- **C (Conscientiousness)** — responsabilidad, adhesión a normas;  
- **E (Extraversion)** — extraversión, actividad social;  
- **A (Agreeableness)** — amabilidad, empatía;  
- **N (Neuroticism)** — neuroticismo, sensibilidad a amenazas;  
- **I (Intelligence)** — inteligencia, pensamiento crítico.

**2. Ideas**  
Una idea es un objeto con los siguientes atributos:  
- **`core`** — la esencia (texto);  
- **`effects`** — impacto en los parámetros del agente (p. ej., `{'C': +8, 'A': +5}`);  
- **`complexity`** — complejidad (0–100), que afecta la distorsión durante la transmisión;  
- **`emotion`** — tono emocional (p. ej., "reverencia", "ira");  
- **`weight`** — la "fuerza" de la idea dentro de la comunidad.

**3. Mecánica de transmisión**  
1. **Selección de fuente**: un agente aleatorio que tenga ideas en sus creencias.  
2. **Selección de receptor**: basada en la Extraversión de la fuente y la Amabilidad del receptor.  
3. **Distorsión**: cambio aleatorio del contenido (depende de la complejidad de la idea y la inteligencia de la fuente).  
4. **Adaptación**: la idea se ajusta al estilo de la fuente (p. ej., se suaviza si A es alto).  
5. **Adopción**: el receptor aplica los efectos de la idea considerando sus propios parámetros (p. ej., un C alto resiste cambios negativos).  
6. **Evolución**: la idea cambia de complejidad y tono emocional después de la transmisión.

**4. Dinámica comunitaria**  
- **Líderes sociales**: los agentes con alto E, C e I ejercen una influencia más fuerte.  
- **Propagación de ideas**: se rastrea el número de agentes que adoptan cada idea.  
- **Actualizaciones de parámetros**: los valores promedio de OCEAN e I se actualizan en cada paso de simulación.

### BELIVEME  
*Ein Simulator für Ideenverbreitung in sozialen Gruppen durch die Linse der Persönlichkeitspsychologie*

#### Über das Projekt  

**BELIVEME** ist eine agentenbasierte Simulation, die modelliert, wie Ideen sich verbreiten, transformieren und eine Gemeinschaft beeinflussen. Die Kernmechanik dreht sich um das Zusammenspiel von:  
- **psychologischen Profilen der Agenten** (das Big-Five-Modell + Intelligenz);  
- **Ideendynamik** (Inhalt, emotionaler Ton, Komplexität);  
- **sozialen Mechanismen** (Einfluss, Vertrauen, Konflikt).

#### Hauptmerkmale  

- **Realistische Agentenpsychologie**: Jeder Agent hat OCEAN-Eigenschaften (Offenheit, Gewissenhaftigkeit, Extraversion, Verträglichkeit, Neurotizismus) und einen Intelligenzwert.  
- **Ideenentwicklung**: Während der Übertragung wird eine Idee verzerrt, passt sich der Persönlichkeit des Empfängers an und kann komplexer oder einfacher werden.  
- **Sozialer Einfluss**: Agenten mit hoher Extraversion (E) und Intelligenz (I) verbreiten Ideen schneller.  
- **Konflikt und Synergie**: Einige Ideen verstärken sich gegenseitig, während andere sich unterdrücken.  
- **Dynamische Visualisierung**: Grafiken zeigen Veränderungen der Gemeinschaftsparameter und Ideenverbreitung über die Zeit.

#### Simulationsziele  

1. Erforschen, wie Persönlichkeitsmerkmale die Wahrnehmung und Übertragung von Ideen beeinflussen.  
2. Die "Viralitäts"-Mechanismen von Ideen in verschiedenen sozialen Gruppen demonstrieren.  
3. Zeigen, wie Ideenkonflikte zu Polarisierung oder Konsolidierung der Gemeinschaft führen.  
4. Ein Werkzeug für Experimente mit sozialen Szenarien bereitstellen.

#### Wie es funktioniert  

**1. Agenten**  
Jeder Agent wird durch sechs Parameter definiert (0–100):  
- **O (Openness)** — Offenheit für neue Erfahrungen;  
- **C (Conscientiousness)** — Gewissenhaftigkeit, Normentreue;  
- **E (Extraversion)** — Extraversion, soziale Aktivität;  
- **A (Agreeableness)** — Verträglichkeit, Empathie;  
- **N (Neuroticism)** — Neurotizismus, Empfindlichkeit gegenüber Bedrohungen;  
- **I (Intelligence)** — Intelligenz, kritisches Denken.

**2. Ideen**  
Eine Idee ist ein Objekt mit folgenden Attributen:  
- **`core`** — das Wesen (Text);  
- **`effects`** — Auswirkungen auf Agentenparameter (z.B. `{'C': +8, 'A': +5}`);  
- **`complexity`** — Komplexität (0–100), beeinflusst Verzerrung bei Übertragung;  
- **`emotion`** — emotionaler Ton (z.B. "Ehrfurcht", "Zorn");  
- **`weight`** — die "Stärke" der Idee innerhalb der Gemeinschaft.

**3. Übertragungsmechanik**  
1. **Quellenauswahl**: ein zufälliger Agent mit Ideen in seinen Überzeugungen.  
2. **Empfängerauswahl**: basierend auf der Extraversion der Quelle und der Verträglichkeit des Empfängers.  
3. **Verzerrung**: zufällige Inhaltsänderung (abhängig von Ideenkomplexität und Quellintelligenz).  
4. **Anpassung**: die Idee passt sich dem Stil der Quelle an (z.B. wird weicher bei hohem A).  
5. **Übernahme**: der Empfänger wendet die Effekte der Idee unter Berücksichtigung seiner eigenen Parameter an (z.B. hohes C widersteht negativen Änderungen).  
6. **Evolution**: die Idee ändert Komplexität und emotionalen Ton nach der Übertragung.

**4. Gemeinschaftsdynamik**  
- **Soziale Führer**: Agenten mit hohem E, C und I üben stärkeren Einfluss aus.  
- **Ideenverbreitung**: die Anzahl der Agenten, die jede Idee übernehmen, wird verfolgt.  
- **Parameteraktualisierungen**: durchschnittliche OCEAN- und I-Werte werden bei jedem Simulationsschritt aktualisiert.

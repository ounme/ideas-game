# BELIVEME: README

*Agentenbasierte Simulation der Ideenverbreitung durch Persönlichkeitspsychologie*

## Überblick

**BELIVEME** modelliert, wie Ideen sich verbreiten, transformieren und Gemeinschaften formen. Die Engine kombiniert:
- **Persönlichkeitsmerkmale** (OCEAN + Intelligenz);  
- **Ideendynamik** (Inhalt, emotionaler Ton, Verzerrung);  
- **Soziale Mechanismen** (Einfluss, Anpassung, Evolution).

## Hauptkomponenten

### 1. `Idea`-Klasse
Repräsentiert ein verbreitbares Konzept mit:
- `core`: textuelle Essenz;  
- `effects`: Parameterauswirkungen (z.B. `{'C': +8, 'A': +5}`);  
- `complexity`: 0–100 (beeinflusst Verzerrung bei Übertragung);  
- `emotion`: emotionaler Ton (z.B. "Ehrfurcht");  
- `weight`: Stärke der Idee in der Gemeinschaft (wächst mit Akzeptanz).

### 2. `Agent`-Klasse
Jeder Agent hat 6 Eigenschaften (0–100):
- **O** (Openness) — Aufgeschlossenheit für neue Erfahrungen;  
- **C** (Conscientiousness) — Regeltreue, Zuverlässigkeit;  
- **E** (Extraversion) — soziale Aktivität;  
- **A** (Agreeableness) — Empathie, Freundlichkeit;  
- **N** (Neuroticism) — Empfindlichkeit gegenüber Bedrohungen;  
- **I** (Intelligence) — kritisches Denken.

**Kernmethoden**:
- `calculate_social_weight()`: berechnet Einfluss (E×0.4 + C×0.3 + I×0.3);  
- `transmit_idea()`: sendet Idee mit Verzerrung und Anpassung;  
- `adapt_idea()`: modifiziert Idee basierend auf Quellen-/Empfängereigenschaften;  
- `receive_idea()`: wendet Effekte mit Filtern an (z.B. hohes C widersteht negativen Änderungen);  
- `evolve_idea()`: aktualisiert Ideenkomplexität und Emotion nach Übertragung.

### 3. `Community`-Klasse
Verwaltet die Agentenpopulation und Simulation:
- `add_idea()`: fügt neue Ideen ins System ein;  
- `step()`: führt einen Simulationszyklus aus (Quelle → Empfängerauswahl → Übertragung → Update);  
- `update_history()`: zeichnet durchschnittliche Eigenschaftswerte auf;  
- `plot_history()`: visualisiert Parametertrends.

## Simulationsablauf

1. **Initialisierung**  
   - `Community(size=N)` erstellen;  
   - Anfängliche `Idea`-Instanzen hinzufügen.

2. **Zyklus (`step()`)**  
   a. Zufälliger **Quell-Agent** ausgewählt (muss Ideen besitzen);  
   b. Zufällige **Idee** aus Überzeugungen der Quelle gewählt;  
   c. **Empfänger** über gewichtete Wahrscheinlichkeit ausgewählt (E der Quelle × A des Empfängers);  
   d. **Übertragung**:  
      - Verzerrung angewendet (basierend auf Ideenkomplexität und Quellen-I);  
      - Idee an Quellen-/Empfängereigenschaften angepasst;  
      - Empfänger aktualisiert Eigenschaften und übernimmt Idee;  
      - Idee entwickelt sich (Komplexität/Emotion ändert sich).  
   e. Eigenschaftsdurchschnitte protokolliert.

3. **Beendigung**  
   - Nach `num_steps` Ergebnisse plotten und Statistiken ausgeben.

## Ausgabe

1. **Konsolenprotokoll**  
   ```
   Шаг 0: средний O=49.4, C=48.9, E=50.0  
   ...  
   Симуляция завершена (100 шагов).
   ```

2. **Grafiken**  
   - Liniendiagramm der durchschnittlichen OCEAN+I-Werte über Schritte.

3. **Finale Statistiken**  
   - Mittelwert/Min/Max für jede Eigenschaft über alle Agenten;  
   - Ideenakzeptanzraten (z.B. *"Соблюдай завет": 22/30 Agenten*);  
   - Top 5 soziale Führer (nach `social_weight`).

## Verwendung

1. **Abhängigkeiten installieren**  
   ```bash
   pip install matplotlib
   ```

2. **Simulation ausführen**  
   ```bash
   python main.py
   ```

3. **Anpassen**  
   - `Community(size)` und anfängliche Ideen im `__main__`-Block ändern;  
   - `effects`, `complexity` und `emotion`-Werte der Ideen anpassen.

## Parameter & Abstimmung

- **Agenteneigenschaften**: Zufällig initialisiert innerhalb von Bereichen (z.B. O: 30–70);  
- **Verzerrung**: `±0.1 × (complexity / 100)`, reduziert durch Quellen-I, erhöht durch Empfänger-N;  
- **Anpassungsregeln**:  
  - Hohes A (Quelle) → weicht Kerntext auf;  
  - Niedriges O (Empfänger) → senkt Komplexität;  
  - Hohes N (Empfänger) → intensiviert Emotion;  
- **Ideenentwicklung**: `weight × 1.01` pro Übertragung; Komplexität ±5% basierend auf Quellen-O.

## Lizenz

MIT-Lizenz. Siehe `LICENSE`-Datei.  
Copyright (c) 2024 Nickita Panin.  
*Gott zur Ehre gewidmet.*

## Beiträge

Siehe `HELPME.md` für Möglichkeiten, Code, Dokumentation zu verbessern oder das Projekt zu teilen.

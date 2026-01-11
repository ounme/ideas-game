# BELIVEME: README

*Simulation basée sur des agents de la propagation d'idées à travers la psychologie de la personnalité*

## Aperçu

**BELIVEME** modélise comment les idées se propagent, se transforment et façonnent les communautés. Le moteur combine :
- **Traits de personnalité** (OCEAN + Intelligence) ;  
- **Dynamique des idées** (contenu, tonalité émotionnelle, distorsion) ;  
- **Mécanismes sociaux** (influence, adaptation, évolution).

## Composants principaux

### 1. Classe `Idea`
Représente un concept propageable avec :
- `core` : essence textuelle ;  
- `effects` : impacts sur les paramètres (par ex., `{'C': +8, 'A': +5}`) ;  
- `complexity` : 0–100 (affecte la distorsion pendant la transmission) ;  
- `emotion` : tonalité émotionnelle (par ex., "révérence") ;  
- `weight` : force de l'idée dans la communauté (augmente avec l'adoption).

### 2. Classe `Agent`
Chaque agent a 6 traits (0–100) :
- **O** (Openness) — réceptivité aux nouvelles expériences ;  
- **C** (Conscientiousness) — respect des règles, fiabilité ;  
- **E** (Extraversion) — activité sociale ;  
- **A** (Agreeableness) — empathie, gentillesse ;  
- **N** (Neuroticism) — sensibilité aux menaces ;  
- **I** (Intelligence) — pensée critique.

**Méthodes principales** :
- `calculate_social_weight()` : calcule l'influence (E×0.4 + C×0.3 + I×0.3) ;  
- `transmit_idea()` : envoie l'idée avec distorsion et adaptation ;  
- `adapt_idea()` : modifie l'idée selon les traits source/destinataire ;  
- `receive_idea()` : applique les effets avec filtres (par ex., C élevé résiste aux changements négatifs) ;  
- `evolve_idea()` : met à jour la complexité et l'émotion de l'idée post-transmission.

### 3. Classe `Community`
Gère la population d'agents et la simulation :
- `add_idea()` : injecte de nouvelles idées dans le système ;  
- `step()` : exécute un cycle de simulation (sélection source → destinataire → transmission → mise à jour) ;  
- `update_history()` : enregistre les valeurs moyennes des traits ;  
- `plot_history()` : visualise les tendances des paramètres.

## Flux de simulation

1. **Initialisation**  
   - Créer `Community(size=N)` ;  
   - Ajouter des instances `Idea` initiales.

2. **Cycle (`step()`)**  
   a. **Agent source** aléatoire sélectionné (doit posséder des idées) ;  
   b. **Idée** aléatoire choisie parmi les croyances de la source ;  
   c. **Destinataire** sélectionné via probabilité pondérée (E de la source × A du destinataire) ;  
   d. **Transmission** :  
      - Distorsion appliquée (basée sur la complexité de l'idée et I de la source) ;  
      - Idée adaptée aux traits source/destinataire ;  
      - Destinataire met à jour ses traits et adopte l'idée ;  
      - Idée évolue (complexité/émotion change).  
   e. Moyennes des traits enregistrées.

3. **Terminaison**  
   - Après `num_steps`, tracer les résultats et afficher les statistiques.

## Sortie

1. **Journal console**  
   ```
   Шаг 0: средний O=49.4, C=48.9, E=50.0  
   ...  
   Симуляция завершена (100 шагов).
   ```

2. **Graphiques**  
   - Graphique linéaire des valeurs moyennes OCEAN+I sur les étapes.

3. **Statistiques finales**  
   - Moyenne/min/max pour chaque trait à travers les agents ;  
   - Taux d'adoption des idées (par ex., *"Соблюдай завет" : 22/30 agents*) ;  
   - Top 5 leaders sociaux (par `social_weight`).

## Utilisation

1. **Installer les dépendances**  
   ```bash
   pip install matplotlib
   ```

2. **Exécuter la simulation**  
   ```bash
   python main.py
   ```

3. **Personnaliser**  
   - Modifier `Community(size)` et les idées initiales dans le bloc `__main__` ;  
   - Ajuster les valeurs `effects`, `complexity` et `emotion` des idées.

## Paramètres et réglage

- **Traits des agents** : Initialisés aléatoirement dans des plages (par ex., O : 30–70) ;  
- **Distorsion** : `±0.1 × (complexity / 100)`, réduite par I de la source, augmentée par N du destinataire ;  
- **Règles d'adaptation** :  
  - A élevé (source) → adoucit le texte de base ;  
  - O faible (destinataire) → abaisse la complexité ;  
  - N élevé (destinataire) → intensifie l'émotion ;  
- **Évolution des idées** : `weight × 1.01` par transmission ; complexité ±5% basée sur O de la source.

## Licence

Licence MIT. Voir fichier `LICENSE`.  
Copyright (c) 2024 Nickita Panin.  
*Dédié à la gloire de Dieu.*

## Contribution

Voir `HELPME.md` pour des moyens d'améliorer le code, la documentation ou partager le projet.

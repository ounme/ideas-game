### BELIVEME  
*Un simulateur de propagation d'idées dans les groupes sociaux à travers le prisme de la psychologie de la personnalité*

#### À propos du projet  

**BELIVEME** est une simulation basée sur des agents qui modélise comment les idées se propagent, se transforment et influencent une communauté. La mécanique principale tourne autour de l'interaction de :  
- **profils psychologiques des agents** (le modèle Big Five + intelligence) ;  
- **dynamique des idées** (contenu, tonalité émotionnelle, complexité) ;  
- **mécanismes sociaux** (influence, confiance, conflit).

#### Caractéristiques principales  

- **Psychologie réaliste des agents** : chaque agent possède des traits OCEAN (Ouverture, Conscience, Extraversion, Agréabilité, Névrosisme) et un score d'intelligence.  
- **Évolution des idées** : lors de la transmission, une idée se déforme, s'adapte à la personnalité du destinataire et peut devenir plus ou moins complexe.  
- **Influence sociale** : les agents avec une Extraversion (E) et une Intelligence (I) élevées propagent les idées plus rapidement.  
- **Conflit et synergie** : certaines idées se renforcent mutuellement, tandis que d'autres se suppriment.  
- **Visualisation dynamique** : les graphiques montrent les changements dans les paramètres de la communauté et la propagation des idées au fil du temps.

#### Objectifs de la simulation  

1. Explorer comment les traits de personnalité affectent la perception et la transmission des idées.  
2. Démontrer les mécanismes de "viralité" des idées dans différents groupes sociaux.  
3. Montrer comment les conflits d'idées conduisent à la polarisation ou à la consolidation de la communauté.  
4. Fournir un outil pour expérimenter avec des scénarios sociaux.

#### Comment ça fonctionne  

**1. Agents**  
Chaque agent est défini par six paramètres (0–100) :  
- **O (Openness)** — ouverture aux nouvelles expériences ;  
- **C (Conscientiousness)** — conscience, adhésion aux normes ;  
- **E (Extraversion)** — extraversion, activité sociale ;  
- **A (Agreeableness)** — agréabilité, empathie ;  
- **N (Neuroticism)** — névrosisme, sensibilité aux menaces ;  
- **I (Intelligence)** — intelligence, pensée critique.

**2. Idées**  
Une idée est un objet avec les attributs suivants :  
- **`core`** — l'essence (texte) ;  
- **`effects`** — impact sur les paramètres des agents (par ex., `{'C': +8, 'A': +5}`) ;  
- **`complexity`** — complexité (0–100), affectant la distorsion pendant la transmission ;  
- **`emotion`** — tonalité émotionnelle (par ex., "révérence", "colère") ;  
- **`weight`** — la "force" de l'idée au sein de la communauté.

**3. Mécanique de transmission**  
1. **Sélection de la source** : un agent aléatoire possédant des idées dans ses croyances.  
2. **Sélection du destinataire** : basée sur l'Extraversion de la source et l'Agréabilité du destinataire.  
3. **Distorsion** : changement aléatoire du contenu (dépend de la complexité de l'idée et de l'intelligence de la source).  
4. **Adaptation** : l'idée s'ajuste au style de la source (par ex., s'adoucit si A est élevé).  
5. **Adoption** : le destinataire applique les effets de l'idée en considérant ses propres paramètres (par ex., un C élevé résiste aux changements négatifs).  
6. **Évolution** : l'idée change de complexité et de tonalité émotionnelle après la transmission.

**4. Dynamique de la communauté**  
- **Leaders sociaux** : les agents avec un E, C et I élevés exercent une influence plus forte.  
- **Propagation des idées** : le nombre d'agents adoptant chaque idée est suivi.  
- **Mises à jour des paramètres** : les valeurs moyennes OCEAN et I sont mises à jour à chaque étape de simulation.

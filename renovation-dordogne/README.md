# Rénovation maison bord de Dordogne — mode d'emploi

Projet d'estimation et de suivi de la rénovation d'une maison achetée 60 000 € en Gironde, au bord de la Dordogne.

## Arborescence

```
renovation-dordogne/
├── CLAUDE.md              contexte projet, chargé automatiquement par les agents
├── 00-contexte/           fiche du bien, DDT du notaire, plans
├── 01-diagnostic/         état des lieux issu des photos, un fichier par zone
├── 02-prix/               base de prix unitaires sourcés
├── 03-chiffrage/          budget détaillé + comparaison des scénarios
├── 04-devis/              devis reçus et leurs analyses
├── 05-reglementaire/      PPRI, urbanisme, SPANC, aides
├── 06-planning/           ordonnancement du chantier
└── photos/                photos par zone (voir photos/README.md)
```

## Par où commencer

1. Remplir `00-contexte/fiche-bien.md` — au moins commune, surface et usage prévu
2. Déposer le **DDT du notaire** dans `00-contexte/`
3. Prendre les photos selon `photos/README.md`
4. Lancer les agents

## Lancer les agents

Il suffit de le demander en langage naturel dans une session Claude Code ouverte à la racine du dépôt. Exemples :

| Ce que tu veux | Ce que tu tapes |
|---|---|
| Vérifier les points bloquants | « Lance `reno-reglementaire` sur la commune de X, adresse Y » |
| Analyser des photos | « Lance `reno-diagnostic-photo` sur `photos/reseaux/` » |
| Obtenir des prix | « Lance `reno-prix-marche` sur le lot électricité » |
| Chiffrer | « Lance `reno-chiffrage` » |
| Calculer les aides | « Lance `reno-aides` » |
| Analyser un devis | « Lance `reno-analyse-devis` sur `04-devis/devis-elec-dupont.pdf` » |
| Planifier | « Lance `reno-planning` » |

Plusieurs agents peuvent tourner en parallèle quand ils ne dépendent pas les uns des autres — typiquement `reno-reglementaire`, `reno-prix-marche` et `reno-diagnostic-photo` en même temps.

## Ordre des dépendances

```
reno-reglementaire ─┐
                    ├─→ reno-chiffrage ─→ reno-planning
reno-diagnostic-photo ┤                 └─→ reno-analyse-devis
reno-prix-marche ─────┘
reno-aides ─────────────→ (arbitrage pro / auto-rénovation)
```

## Ce que ces agents ne font pas

Ils ne remplacent **pas** une visite d'homme de l'art. Sur une maison en pierre en bord de rivière, deux sujets se tranchent sur place et pas sur photo : **l'humidité ascensionnelle** et **l'état de la structure**. Les agents les signalent, les chiffrent en ordre de grandeur, et recommandent l'expertise — ils ne concluent pas à sa place.

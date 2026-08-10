# Base de prix unitaires

> Alimentée par l'agent `reno-prix-marche`. Ne pas écrire de prix ici sans source ni date.
> Marché visé : maison individuelle, artisans locaux, Gironde / Libournais / vallée de la Dordogne.

## Conventions

- Trois valeurs par ligne : **bas / moyen / haut**. Jamais une valeur unique.
- **HT et TTC**, avec le taux de TVA retenu explicité.
- Rappel TVA : entreprise **10 %** (logement > 2 ans), **5,5 %** (amélioration énergétique éligible), matériaux achetés en direct par le particulier **20 %**.
- Part fourniture / part pose indiquée au moins en pourcentage — c'est ce qui permet de chiffrer le scénario auto-rénovation.
- Abattement main-d'œuvre régional appliqué : à préciser par l'agent, ligne par ligne. Jamais d'abattement sur la fourniture.
- Chaque ligne porte ses sources (URL + date de consultation) et un niveau de confiance.

## Format d'une ligne

```
| Désignation | Unité | PU bas | PU moyen | PU haut | Fourn. % | HT/TTC | TVA | Confiance | Sources |
```

---

## Lot 01 — Électricité

*Non renseigné. Lancer `reno-prix-marche` sur le lot électricité.*

## Lot 02 — Plomberie / sanitaire

*Non renseigné.*

## Lot 03 — Assainissement

*Non renseigné. Ne chiffrer qu'après confirmation en mairie du raccordement au tout-à-l'égout.*

## Lot 04 — Chauffage / ECS

*Non renseigné.*

## Lot 05 — Couverture / zinguerie

*Non renseigné.*

## Lot 06 — Menuiseries extérieures

*Non renseigné.*

## Lot 07 — Traitement de l'humidité

*Non renseigné.*

## Lot 08 — Isolation

*Non renseigné.*

## Lot 09 — Plâtrerie / doublage

*Non renseigné.*

## Lot 10 — Sols

*Non renseigné.*

## Lot 11 — Peinture / finitions

*Non renseigné.*

## Lot 12 — Menuiseries intérieures

*Non renseigné.*

## Lot 13 — Dépose / évacuation gravats

*Non renseigné.*

## Prestations intellectuelles

| Prestation | Base | Fourchette | Source |
|---|---|---|---|
| Maître d'œuvre | % du montant HT des travaux | à confirmer | *à sourcer* |
| Architecte | % du montant HT des travaux | à confirmer | *à sourcer* |
| Étude de sol (ANC) | forfait | à confirmer | *à sourcer* |
| Attestation Consuel | forfait | à confirmer | *à sourcer* |
| Assurance dommage-ouvrage | % du montant des travaux | à confirmer | *à sourcer* |

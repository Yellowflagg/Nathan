# Projet — Rénovation maison bord de Dordogne (Gironde)

## Contexte

Maison achetée **60 000 €** par l'oncle de Nathan, au bord de la Dordogne, en **Gironde (33)**.
État général déclaré comme correct : sol en bon état, murs probablement à reprendre, **certains câbles électriques coupés**, **certaines arrivées d'eau coupées**.

**Objectif prioritaire : rendre le bien habitable** — eau chaude et froide, électricité aux normes, évacuations, chauffage, une salle de bain, une cuisine, hors d'eau / hors d'air. Le confort vient après.

## Sorties attendues

Une estimation de budget selon **quatre scénarios** :

- **A** — travaux pilotés par un **maître d'œuvre**
- **B** — **artisans consultés en direct**, lot par lot, coordination par le maître d'ouvrage
- **C** — **auto-rénovation** intégrale
- **D** — **hybride** : pro sur les lots techniques et éligibles aux aides, auto-rénovation sur le reste

## Agents du projet

| Agent | Rôle |
|---|---|
| `reno-diagnostic-photo` | Analyse les photos → constats + quantités |
| `reno-prix-marche` | Recherche web → prix unitaires sourcés et régionalisés |
| `reno-chiffrage` | Métré × prix → budget et scénarios A/B/C/D |
| `reno-aides` | Recherche web → aides mobilisables et aides perdues en auto-réno |
| `reno-reglementaire` | PPRI, urbanisme, SPANC, NF C 15-100, termites, assurances |
| `reno-analyse-devis` | Analyse et comparaison des devis reçus |
| `reno-planning` | Ordonnancement du chantier, arbitrage pro / soi-même |

## Enchaînement recommandé

1. `reno-reglementaire` **en premier** — un classement en zone rouge de PPRI ou une absence de tout-à-l'égout peut invalider une partie du programme avant tout chiffrage
2. `reno-diagnostic-photo` au fur et à mesure de l'arrivée des photos
3. `reno-prix-marche` sur les lots identifiés
4. `reno-chiffrage` une fois 1–3 disponibles
5. `reno-aides` avant tout arbitrage pro / auto-rénovation
6. `reno-planning` une fois le chiffrage stabilisé
7. `reno-analyse-devis` à chaque devis reçu

## Règles de travail communes

- **Toujours des fourchettes**, jamais un montant unique. Un budget de rénovation d'ancien annoncé au millier près est faux.
- **HT et TTC séparés**, avec le taux de TVA écrit. Rappel : entreprise 10 % (ou 5,5 % énergétique), matériaux achetés en direct **20 %**.
- **Toute donnée réglementaire ou tarifaire vient d'une source consultée en session**, avec URL et date. Rien de mémoire : les barèmes d'aides et les prix matériaux changent en cours d'année.
- **Provision pour aléas 12 % minimum**, 15 % tant qu'il reste des inconnues structurelles ou d'humidité.
- **Une donnée manquante se signale, elle ne s'invente pas.**
- Aucun agent ne remplace un homme de l'art : toute suspicion structurelle ou d'humidité déclenche une recommandation d'expertise sur place.

## ⚠️ Limite d'environnement constatée le 10/08/2026

L'environnement d'exécution applique une **politique réseau restrictive** : seuls les dépôts de paquets (pypi, npm…) sont joignables. **`WebFetch` échoue en `EGRESS_BLOCKED` sur tous les domaines publics** (service-public.fr, georisques.gouv.fr, anil.org, batiprix.com, sites de distributeurs…). Vérifié par test direct : `service-public.fr` et `georisques.gouv.fr` renvoient un code 000, `pypi.org` renvoie 200.

Conséquence sur ce projet :
- Les agents de recherche ne disposent que de **`WebSearch`**, c'est-à-dire d'**extraits de résultats**, pas de lectures de pages complètes.
- **Aucune source officielle ne peut être consultée** : ni le règlement du PPRI, ni géorisques, ni les barèmes d'aides sur service-public.fr / France Rénov'.
- **Plafonner la confiance à « moyenne »** sur toute donnée obtenue dans ces conditions, et l'écrire. C'est ce qui a été fait pour les lots 01 et 02.
- **Ne jamais présenter une règle de droit ou un barème d'aide obtenu par simple extrait de recherche comme établi.** Sur le réglementaire et les aides, l'écart entre un extrait et le texte applicable est trop coûteux.

Pour lever la limite : changer la politique réseau de l'environnement sur claude.ai/code (voir https://code.claude.com/docs/en/claude-code-on-the-web). Tant qu'elle n'est pas levée, le PPRI et les aides doivent être vérifiés à la main par le maître d'ouvrage.

## Vigilances propres à ce bien

- **Zone inondable** : bord de Dordogne → PPRI très probable. À vérifier sur `georisques.gouv.fr` avant tout le reste. Impacte les matériaux du RDC, la position du tableau électrique et des prises, l'assurabilité, la revente.
- **Termites** : Gironde en zone déclarée par arrêté préfectoral.
- **Humidité ascensionnelle** : maison en pierre en bord de rivière → risque n°1. Un doublage posé sur un mur humide est un lot perdu.
- **Assainissement** : si pas de tout-à-l'égout, +8 000 à 12 000 € et contrôle SPANC. À confirmer en mairie.
- **DDT du notaire** (DPE, état parasitaire, élec, gaz, plomb, amiante) : à déposer dans `00-contexte/`. C'est le document le plus utile du dossier, il prime sur toute lecture de photo.

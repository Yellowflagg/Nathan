# Chiffrage détaillé — 2, lieu-dit Robin, 33350 Castillon-la-Bataille

**Établi le 10/08/2026** par `reno-chiffrage`.
Entrées : `00-contexte/fiche-bien.md`, `01-diagnostic/synthese.md` (**révisions incluses, elles font foi**), `02-prix/base-prix.md`, `05-reglementaire/cadre.md`.
Script de calcul réexécutable : `03-chiffrage/calcul.py`. Tous les totaux ci-dessous en sortent.

---

## ⚠️ À LIRE AVANT TOUT CHIFFRE

**Aucune ligne de la base de prix ne dépasse la confiance « moyenne ».** `WebFetch` a été bloqué par la politique réseau de l'environnement pendant toute la constitution de la base : les prix viennent d'**extraits de résultats de recherche**, pas de lectures de pages complètes. Deux exceptions seulement, en confiance haute : **E-09** (Consuel, tarif réglementé) et **E-09b** (mise en service Enedis, grille du 01/08/2026).

**Ce budget sert à cadrer un programme et à négocier des devis. Il n'engage aucune dépense.** Un écart de 30 % entre ce document et un devis réel n'est pas une anomalie.

---

## 1. Le programme retenu : une remise en service, pas une rénovation lourde

Les trois séries de photos et les retours de terrain ont **fait tomber** l'essentiel du programme initialement redouté. Ce qui est **conservé et non chiffré** :

| Élément conservé | Constat | Conséquence budgétaire |
|---|---|---|
| Carrelages de sol, terre cuite et grès, toutes pièces | C-01, C-04, C-06, C-07, C-13, C-15 | **Lot 10 réduit à des reprises ponctuelles** |
| Menuiseries extérieures PVC / alu double vitrage | synthèse « Menuiseries » | **Lot 06 = 0 €** |
| Toiture, tuiles canal — orage sans entrée d'eau | révision « test à la pluie » | **Lot 05 = 0 €**, réserve écrite ci-dessous |
| WC fonctionnel, faïence, réservoir | C-04 | P-07 = 0 € |
| Douche carrelée, receveur intact, robinetterie | C-05 (reclassé COSMÉTIQUE) | P-06 = 0 € en programme « décent » |
| Évier double grès, faïence murale cuisine | C-06, C-07 | remplacement non chiffré |
| Plinthes carrelées | C-01 | M-02 = 0 € |

**Le diagnostic humidité a été révisé et écarté** : la maison est vide depuis 7 ans, elle ne produit pas de vapeur d'eau. C-05, C-08 et C-09 sont **reclassés COSMÉTIQUE**.
→ **Aucune ligne d'injection de barrière étanche, de drainage périphérique ou de cuvelage n'est ouverte.** La ventilation est retenue **à titre préventif seulement**, pour l'emménagement.

### ⚠️ Le curage D-02 n'est PAS appliqué

La ligne D-02 « curage léger d'un logement » vaut 23,00 / 36,80 / 55,20 €/m² habitable. **Appliquée aux 85 m², elle produirait 1 955 à 4 692 € HT de dépense fictive.** L'agent prix l'a signalée comme la faute de chiffrage la plus coûteuse du dossier, et il a raison : il n'y a **rien à curer** ici.

**Le bon métré est une liste de postes déposés, pas une surface :**

| Poste déposé | Où chiffré |
|---|---|
| Appareil gaz mural + canalisations propane | CH-05 (lot 04) |
| Papiers peints | PL-06 (lot 09), niveau confortable |
| Tableau électrique + coffret divisionnaire | E-05 (dépose incluse) — le coffret C-18 **reste non chiffré** |
| PABX Stratel (C-02), boîtier éventré (C-01) | intégré à la dépose du lot 01, valeur négligeable |
| Dalles béton des regards (si ANC) | intégré à A-10 (lot 03) |
| Évacuation | D-03a (+ D-03c en confortable) |

---

## 2. Métré retenu et hypothèses

| Donnée | Valeur | Statut |
|---|---|---|
| Surface habitable | 85 m² | fiche-bien, **ferme** |
| Programme | T2 ou petit T3 + garage + buanderie + véranda | C-20, **à confirmer au plan** |
| Circuits électriques existants | 13 au tableau principal + 1 coffret divisionnaire | C-17, C-18, **ferme** |
| Linéaire de ré-aiguillage | 150 ml (13–16 circuits × ~10 m) | **hypothèse de travail** |
| Linéaire PER (EF + ECS) | 70 ml | **hypothèse de travail** |
| Évacuation PVC Ø100 en reprise | 8 ml | **hypothèse de travail** |
| Points d'eau à desservir | 5 : évier, lavabo, douche, WC, lave-linge | C-04/C-05/C-06/C-23, **ferme** |
| Enduit décroûté à reprendre | 2,5 m² + 3 ml de saignée ouverte | C-11, **ferme** |
| Murs tapissés | 130 m² | **hypothèse non métrée** |
| Surface de combles | 85 m² | **NON DOCUMENTÉE** — aucune vue des combles |
| Portes intérieures | 4 | **hypothèse — nombre non établi** |

---

## 3. Chiffrage — niveau « DÉCENT ET VIVABLE »

Objectif prioritaire : hors d'eau / hors d'air, électricité aux normes NF C 15-100 série 2024, eau chaude et froide, évacuations, 1 SDB, 1 cuisine, chauffage, murs sains.

Tous les PU sont **HT, fourniture + pose par une entreprise**, repris tels quels de `02-prix/base-prix.md` (abattement régional déjà appliqué à la source). Le taux de TVA est écrit sur chaque ligne. **Aucun HT n'est additionné à un TTC.**

### Lot 00 — Prestations et obligations préalables

| Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA | Source PU | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Diagnostic amiante avant travaux (DAT) | 1 | forfait | 350 | 350 | 350 | 350 | 350 | 350 | 20 % | base-prix, note D-01 | cadre.md § 8.2 |
| **Sous-total** | | | | | | **350** | **350** | **350** | | | |
| **TTC** | | | | | | **420** | **420** | **420** | | | |

> **Valeur ponctuelle sourcée, pas une fourchette.** Le DAT est une **obligation distincte du DDT du notaire**, à la charge du maître d'ouvrage. Bâti antérieur à 1997 → **aucune dépose de revêtement collé ne doit démarrer avant.** Il conditionne PL-06, PL-02 et toute intervention sur les colles de carrelage.

### Lot 01 — Électricité — hypothèse **ré-aiguillage sur fourreaux existants**

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| E-05 | Tableau 3 rangées équipé, dépose ancien incluse | 1 | ens | 621 | 1 052 | 1 912 | 621 | 1 052 | 1 912 | 10 % | C-17 / C-03 |
| E-06 | Mise à la terre : piquet, cuivre nu 25 mm², barrette, mesure | 1 | ens | 188 | 395 | 752 | 188 | 395 | 752 | 10 % | C-17 |
| E-02 | Point lumineux simple allumage | 10 | point | 66 | 113 | 188 | 660 | 1 130 | 1 880 | 10 % | C-17 |
| E-03 | Point lumineux va-et-vient | 2 | point | 113 | 169 | 263 | 226 | 338 | 526 | 10 % | C-17 / C-20 |
| E-04 | Prise 16 A + T sur circuit existant | 24 | u | 65 | 108 | 168 | 1 560 | 2 592 | 4 032 | 10 % | C-17 |
| E-07 | Circuit spécialisé 32 A (plaque) | 1 | u | 123 | 189 | 283 | 123 | 189 | 283 | 10 % | C-17 |
| E-07b | Circuit spécialisé 20 A (four, LL, LV, ballon) | 4 | u | 85 | 123 | 165 | 340 | 492 | 660 | 10 % | C-17 / C-23 |
| E-08 | Ré-aiguillage conducteurs sur fourreaux existants | 150 | ml | 4,70 | 8,40 | 14,00 | 705 | 1 260 | 2 100 | 10 % | C-23 |
| E-09 | Attestation Consuel jaune (avec visite) | 1 | forfait | 120,56 | 120,56 | 194,68 | 121 | 121 | 195 | 20 % | cadre.md § 5.2 |
| E-09b | Mise en service Enedis, compteur Linky, à distance | 1 | forfait | 1,50 | 1,50 | 1,50 | 2 | 2 | 2 | 20 % | 3e série photos |
| | **Sous-total HT** | | | | | | **4 545** | **7 570** | **12 341** | | |
| | **Sous-total TTC** | | | | | | **5 012** | **8 339** | **13 595** | | |

**Notes de méthode, lot 01 :**
- **E-08 est un proxy assumé.** La base ne porte aucune ligne « ré-aiguillage sur fourreau existant ». E-08 (tirage apparent, sans saignée) est la ligne la plus proche du geste réel ; E-08b (encastré, saignée + rebouchage) serait franchement majorant. **À confirmer par devis.**
- **La plus-value E-01b (encastrement en pierre) ne s'applique pas** : la maison est en **parpaing** (C-11). C'est l'économie la mieux établie du dossier.
- **Risque de double compte signalé** : E-02 et E-04 incluent une part de cheminement local ; E-08 a été volontairement limité aux **antennes principales tableau → première boîte** (150 ml et non 250). Si le devis facture les deux au réel, arbitrer.
- ⚠️ **Alerte borne haute.** La somme ligne à ligne culmine à **12 341 € HT**, au-dessus du repère « refonte complète 5 000–10 500 € HT » du constat C-17 **et** au-dessus de la variante E-01 haute (10 540 € HT). **À la borne haute, retenir le ratio E-01, pas la somme des lignes.**

**Variante — refonte totale du câblage** (si les conducteurs ont été tirés hors des fourreaux, C-23) :

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA |
|---|---|---|---|---|---|---|---|---|---|---|
| E-01 | Rénovation électrique complète, refonte totale — **hors plus-value pierre** | 85 | m² hab | 57 | 90 | 124 | 4 845 | 7 650 | 10 540 | 10 % |

> E-01 **se substitue** à E-02 / E-03 / E-04 / E-07 / E-07b / E-08 (3 614 / 6 001 / 9 481 € HT). Elle **ne se substitue pas** à E-05, E-06, E-09, E-09b.
> **Delta de la variante : +1 231 / +1 649 / +1 059 € HT.** L'écart entre ré-aiguillage et refonte totale est donc **de l'ordre de 1 000 à 1 700 € HT seulement** — bien moins spectaculaire que la crainte portée au constat C-23. C'est un résultat important : **ce n'est pas ce point qui fera basculer le budget.** Un électricien tranchera en une visite.

### Lot 02 — Plomberie / sanitaire

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| P-01 | Alimentation PER Ø16 sous fourreau, EF + ECS | 70 | ml | 7,60 | 11,30 | 14,20 | 532 | 791 | 994 | 10 % | C-23 |
| P-05 | Point d'eau complet (lavabo, douche, WC, lave-linge) | 4 | u | 94 | 189 | 283 | 376 | 756 | 1 132 | 10 % | C-04 / C-05 / C-23 |
| P-09 | Plomberie cuisine : évier + LV, robinet d'arrêt | 1 | ens | 302 | 472 | 661 | 302 | 472 | 661 | 10 % | C-06 / C-07 |
| P-04 | Évacuation PVC Ø100/110, reprise ponctuelle | 8 | ml | 42,50 | 66,10 | 94,40 | 340 | 529 | 755 | 10 % | C-19 / siphons à sec |
| | **Sous-total HT** | | | | | | **1 550** | **2 548** | **3 542** | | |
| | **Sous-total TTC** | | | | | | **1 705** | **2 803** | **3 896** | | |

**Notes, lot 02 :**
- **Non-cumul respecté** : P-09 couvre la cuisine, P-05 est compté **4 fois** (et non 5) pour ne pas doubler l'évier.
- **P-05 doit être lu en haut de fourchette** : la base l'écrit explicitement — le bas de fourchette suppose un piquage court sur réseau vivant, ce qui n'est pas la situation (réseau **volé par tronçons**, C-23).
- **Contrôle de cohérence — et il révèle un écart qu'il faut expliquer.** Ce lot ressort à **18–42 €/m² habitable**, sous le ratio de contrôle de la base (50–110 €/m² HT) et très sous la pré-estimation « 6 000–10 000 € » portée au constat C-23. **La raison est réelle** : le bien conserve WC, douche, évier et faïences — on repose un réseau, on ne crée pas une salle de bain ni une cuisine. La pré-estimation supposait l'inverse.
- **Variante P-11** — si un contrôle visuel au compteur et sous évier révèle du **plomb ou de l'acier galvanisé** (présence **non vérifiée**) :

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA |
|---|---|---|---|---|---|---|---|---|---|---|
| P-11 | Dépose réseau plomb/galva + pose neuf + reprise des supports | 70 | ml | 103 | 136 | 168 | 7 210 | 9 520 | 11 760 | 10 % |

> P-11 **se substitue** à P-01. Le lot 02 passe alors à **8 228 – 14 308 € HT** — et c'est cette variante, et elle seule, **qui recoupe la pré-estimation 6 000–10 000 €** du constat C-23. **Un contrôle visuel de dix minutes tranche un écart de 7 000 à 11 000 €.** C'est l'action au meilleur rendement du dossier après la mesure des fissures.

### Lot 03 — Assainissement → **voir § 5, branche A** (non tranché)

### Lot 04 — Chauffage / ECS

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CH-05 | Dépose installation propane (appareil, canalisations, attestation PG) | 1 | forfait | 267 | 401 | 592 | 267 | 401 | 592 | 10 % | C-06 / C-22 |
| CH-01 | Panneau rayonnant en remplacement de convecteur | 4 | u | 244 | 390 | 683 | 976 | 1 560 | 2 732 | 10 % | C-21 |
| CH-02 | Ballon ECS électrique 150 L stéatite, fourni posé | 1 | u | 582 | 757 | 922 | 582 | 757 | 922 | 10 % | C-06 / C-22 |
| | **Sous-total HT** | | | | | | **1 825** | **2 718** | **4 246** | | |
| | **Sous-total TTC** | | | | | | **2 008** | **2 990** | **4 671** | | |

**Notes, lot 04 :**
- **Arbitrage énergie tranché par le diagnostic** : le propane en bouteilles est l'énergie de chauffage la plus chère du marché, avec manutention. Face à 4 départs convecteurs déjà câblés (C-21) et au **coefficient d'énergie primaire de l'électricité passé de 2,3 à 1,9 au 01/01/2026** (cadre.md § 7.4), **il n'y a pas de raison de conserver le propane** autrement que pour la cuisson. Dépose retenue.
- **CH-01 et CH-02 n'ouvrent droit à AUCUNE aide et restent à TVA 10 %.** C'est ce qui les rend intéressants en auto-rénovation (voir `scenarios.md`, scénario D).
- CH-01 ne doit **pas** être engagé avant E-05 : les 4 circuits sont en 10 A sur une installation de 1980 sans différentiel 30 mA.
- **Options d'arbitrage énergie, hors périmètre du niveau « décent »** : CH-03 chauffe-eau thermodynamique (2 313/3 516/5 550 € HT, **TVA 5,5 %, MPR 400–1 200 € + CEE 150–600 €, RGE obligatoire**) et CH-04 poêle à granulés (3 225/5 067/7 371 € HT, **TVA 5,5 %, MPR 750–1 250 € + CEE 250 €, RGE + Flamme Verte 7★ + tubage inox Ø80/100**). Deux conduits existants sont repérés (C-06, C-13) → **faire vérifier état, section et dévoiements par un fumiste avant tout devis de poêle** : c'est ce diagnostic-là qui fixe le prix.

### Lot 05 — Couverture / zinguerie — **0 €**

> **Réserve écrite, à ne pas escamoter.** Le lot est mis à zéro sur deux éléments concordants : (a) **un orage et de fortes pluies la nuit précédente sans aucune entrée d'eau constatée à l'intérieur** — c'est un essai en conditions réelles, de meilleure qualité qu'une interprétation d'image ; (b) absence de déformation et de tuile manquante sur les vues disponibles (C-10, C-16).
> **Ce qui n'est pas couvert par cette réserve** : **les 4 pans ne sont pas documentés** (une seule face l'est) et **les combles n'ont jamais été vus de l'intérieur**. Une nuit de pluie teste une direction de vent et une intensité, pas toutes les configurations.
> **Si un désordre apparaît**, les lignes sont prêtes : V-07 reprise ponctuelle (144/268/440 € HT) et V-07b recherche de fuite + reprise d'étanchéité (421/796/1 310 € HT). **Elles sont couvertes par la provision pour aléas de 15 %**, pas par une ligne dédiée.
> *Le bloc « Lot 05 » de la base de prix est par ailleurs **non renseigné** — aucune ligne de couverture au m² n'existe. Une réfection réelle serait à chiffrer de zéro.*

### Lot 06 — Menuiseries extérieures — **0 €**

> PVC / alu, **double vitrage**, manœuvre correcte sur les vues disponibles. Le lot, chiffré 6 000 à 11 000 € en pré-estimation, **tombe**.
> *Réserve mineure : si la parcelle s'avère en abords de monument historique (cadre.md § 4.2, probabilité jugée faible), tout remplacement futur passerait en DP avec avis conforme de l'ABF. Sans objet tant qu'on ne remplace rien.*

### Lot 07 — Ventilation — **préventive, aucune injection, aucun drainage**

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| V-02 | VMC simple flux hygroréglable type B, pro RGE | 1 | ens | 853 | 1 280 | 1 896 | 853 | 1 280 | 1 896 | **5,5 %** | révision « VMC préventive » |
| V-05 | Entrée d'air en menuiserie, pièce principale | 3 | u | 87 | 145 | 290 | 261 | 435 | 870 | 10 % | menuiseries étanches conservées |
| V-06b | Traitement complet fongicide + peinture anti-moisissures (plafond douche) | 4 | m² | 37,80 | 56,60 | 75,50 | 151 | 226 | 302 | 10 % | C-05 |
| | **Sous-total HT** | | | | | | **1 265** | **1 941** | **3 068** | | |
| | **Sous-total TTC** | | | | | | **1 353** | **2 078** | **3 289** | | |

**Notes, lot 07 :**
- **Le raisonnement est inversé par rapport au diagnostic initial, et c'est délibéré.** Aujourd'hui la maison est sèche **parce qu'elle est vide**. Le jour où quelqu'un y habite, la production de vapeur redémarre d'un coup (~10 L/jour) dans un bâti des années 1980 **sans VMC** et avec des menuiseries double vitrage étanches. C'est la configuration qui **fabrique** de la condensation. **La VMC est chiffrée pour ne pas créer un désordre, pas pour en réparer un.**
- **⚠️ Écart de TVA à signaler explicitement, il est contre-intuitif** :

| Ligne | TVA | Total TTC bas / moy / haut | Aides |
|---|---|---|---|
| **V-02** — hygroréglable **type B** | **5,5 %** (logement > 2 ans **+ pro RGE**) | 900 / 1 350 / 2 000 € | MPR/CEE *non confirmés en session* |
| **V-01** — autoréglable | **10 %** | 470 / 782 / 1 251 € | **aucune** |

> Seule l'**hygroréglable B** est entrée dans le champ du taux réduit (arrêté du 4 décembre 2024, cité par la base — **texte non vérifié directement, `WebFetch` bloqué**). Beaucoup de devis affichent 5,5 % à tort sur de l'autoréglable. **Le surcoût V-02 vs V-01 est de +426 à +759 € HT, dont une partie est reprise par l'écart de TVA** — et l'hygro B module le débit sur le taux d'humidité, ce qui est exactement la réponse au risque d'emménagement. **V-02 retenue.**
- **V-05 est le poste le plus souvent oublié, et son oubli ruine la VMC.** Sans entrées d'air neuf en pièces sèches, l'extraction tire l'air par les défauts d'étanchéité, les débits s'effondrent. Sur des menuiseries double vitrage étanches, c'est structurant. *Réserve technique : sur certaines menuiseries alu à rupture de pont thermique, l'usinage en place n'est pas possible — à faire vérifier.*
- **Aucune ligne d'injection (≈ 100 €/ml) ni de drainage périphérique (160–400 €/ml) n'est ouverte.** Les écarter, c'est plusieurs milliers d'euros non engagés. **Si un humidimètre contredisait le diagnostic sur place, ce bloc serait à rouvrir.**

### Lot 09 — Plâtrerie (niveau décent : fermeture seule)

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PL-02 | Reprise d'enduit sur parpaing décroûté | 2,5 | m² | 28,70 | 47,80 | 76,40 | 72 | 120 | 191 | 10 % | C-11 |
| PL-03b | Rebouchage de saignée déjà ouverte | 3,0 | ml | 8,30 | 13,90 | 22,20 | 25 | 42 | 67 | 10 % | C-11 |
| | **Sous-total HT** | | | | | | **97** | **161** | **258** | | |
| | **Sous-total TTC** | | | | | | **106** | **177** | **283** | | |

> ⚠️ **Ce sous-total est irréaliste tel quel, et il faut le dire.** Aucun artisan ne se déplace pour 160 € de travaux. **Attendez-vous à un minimum d'intervention ou à un forfait de déplacement qui écrasera le prix unitaire** — montant **non sourcé** pour le Libournais. La bonne stratégie est de **grouper PL-02, PL-03b et la branche B1 dans un seul passage**, et de demander à l'artisan ce qu'il facture pour une demi-journée sur place.
> **Séquencement impératif (C-11)** : ne refermer qu'**après** arbitrage sur le passage des réseaux.
> **PL-03b est une valeur construite**, pas sourcée (confiance faible, assumée par la base).

### Lot 10 — Sols — **reprises ponctuelles seulement**

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S-01a | Intervention de remplacement ponctuel de carreaux (1 à 5) | 1 | forfait | 186 | 269 | 371 | 186 | 269 | 371 | 10 % | C-13 / C-15 |
| S-02 | Réfection de joints de carrelage — pièces d'eau | 12 | m² | 14,90 | 26,10 | 46,60 | 179 | 313 | 559 | 10 % | C-05 / C-04 |
| | **Sous-total HT** | | | | | | **365** | **582** | **930** | | |
| | **Sous-total TTC** | | | | | | **401** | **640** | **1 023** | | |

> **S-03 ragréage = 0 €, hors périmètre.** Il n'y a pas de sol à ragréer.
> **Action gratuite prioritaire** : **chercher les carreaux de réserve** (garage, buanderie, comble). Sur une maison des années 1970-80, il y a très souvent un carton d'origine. Sans lui, la teinte ne sera jamais raccord et la reprise se verra plus que le carreau cassé. **Cette question compte plus que le prix.**
> S-01b (carreau supplémentaire) est une **valeur construite**, confiance faible.

### Lot 13 — Dépose / évacuation

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| D-03a | Benne 8 m³ gravats / inertes, rendue + enlèvement + traitement, 7 j | 1 | u | 180 | 280 | 380 | 180 | 280 | 380 | **20 %** | C-11 / C-15 |
| **D-02** | **Curage léger au m² — NON APPLIQUÉ** | 0 | m² hab | 23,00 | 36,80 | 55,20 | **0** | **0** | **0** | — | voir § 1 |
| | **Sous-total HT** | | | | | | **180** | **280** | **380** | | |
| | **Sous-total TTC** | | | | | | **216** | **336** | **456** | | |

**Le tri est facturé en sus, et lourdement.** Surcoûts sourcés à la base :

| Surcoût | Impact |
|---|---|
| Benne mélangée vs benne triée mono-matériau | la triée coûte **30 à 50 % moins cher** |
| Gravats mis dans une benne déchets verts → reclassement DIB | **+40 à 80 %** |
| Dépassement du tonnage inclus | **15 à 30 €/tonne** |
| Déchets dépassant le bord de benne | refus d'enlèvement, ou **+50 à 100 €** |
| Location au-delà de 7 jours | **5 à 15 €/jour** |
| Saisonnalité | tarifs plus compétitifs **de novembre à février** |

> **⚠️ Le plâtre n'est PAS un inerte.** Il est refusé en filière inerte dans la plupart des centres. C'est l'erreur classique du particulier qui jette ses chutes de BA13 dans la benne à gravats — et elle se paie au reclassement DIB.
> **Deux leviers locaux gratuits** : le bien dispose d'un **bac USTOM** (C-13), et le **garage offre une capacité de stockage tampon** permettant d'attendre une benne pleine plutôt que d'en louer deux à moitié vides.
> **TVA 20 % retenue par prudence** (particulier contractant en direct avec un loueur = prestation de service). **Si l'entreprise de travaux refacture la benne dans son marché, elle suit le 10 %** — soit 198 / 308 / 418 € TTC. **Point non vérifié sur source fiscale officielle.**
> **Ne pas poser une benne sur une dalle qui couvre une fosse** (C-15).

### Total du niveau « DÉCENT ET VIVABLE », hors lot 03

| | Bas | Moyen | Haut |
|---|---|---|---|
| **HT** | **10 177 €** | **16 151 €** | **25 115 €** |
| **TTC** | **11 221 €** | **17 783 €** | **27 634 €** |

---

## 4. Chiffrage — incrément « CONFORTABLE »

Ce niveau **s'ajoute** au précédent. Il ne le remplace pas.

| Réf | Lot | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| E-10 | 01 | Coffret de communication grade 2 TV | 1 | ens | 191 | 363 | 621 | 191 | 363 | 621 | 10 % | C-02 |
| I-01 | 08 | Isolation combles perdus par soufflage, **R ≥ 7**, pro RGE | 85 | m² | 21,00 | 31,00 | 43,00 | 1 785 | 2 635 | 3 655 | **5,5 %** | *combles non documentés* |
| PL-06 | 09 | Dépose de papier peint (détapissage) | 130 | m² | 6,40 | 11,00 | 18,40 | 832 | 1 430 | 2 392 | 10 % | C-07 / C-03 |
| PL-01 | 09 | Enduit de rebouchage + lissage | 130 | m² | 9,30 | 14,90 | 22,40 | 1 209 | 1 937 | 2 912 | 10 % | C-09 |
| S-02c | 10 | Réfection de joints, autres pièces | 20 | m² | 14,90 | 26,10 | 46,60 | 298 | 522 | 932 | 10 % | C-06 / C-07 / C-13 |
| PE-05 | 11 | Remise en peinture complète (murs + plafonds + boiseries) | 85 | m² hab | 35,40 | 65,20 | 102,50 | 3 009 | 5 542 | 8 712 | 10 % | C-07 / C-09 |
| M-01 | 12 | Bloc-porte intérieur fourni posé | 4 | u | 212 | 366 | 598 | 848 | 1 464 | 2 392 | 10 % | C-20 |
| D-03c | 13 | Benne 15 m³ tout-venant / DIB | 1 | u | 380 | 530 | 700 | 380 | 530 | 700 | **20 %** | PL-06 / M-01 |
| | | **Sous-total HT** | | | | | | **8 552** | **14 423** | **22 316** | | |
| | | **Sous-total TTC** | | | | | | **9 365** | **15 800** | **24 454** | | |

**Substitution optionnelle** — radiateurs à inertie au lieu de panneaux rayonnants :

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Delta HT vs CH-01 | TVA |
|---|---|---|---|---|---|---|---|---|
| CH-01b | Radiateur à inertie (remplace CH-01) | 4 | u | 372 | 686 | 1 372 | **+512 / +1 184 / +2 756** | 10 % |

> Cette substitution est **retenue dans le niveau confortable** des scénarios. Elle n'ouvre **aucune aide** et reste à **TVA 10 %** — c'est un choix de confort et de DPE, pas un choix subventionné.

**Pièges de cumul respectés :**
- **PE-05 est un ratio englobant** : il contient PE-01 à PE-04. **Aucune de ces lignes n'est ajoutée.**
- PE-05 inclut une « préparation courante », **pas** une remise en état : **PL-06 et PL-01 s'ajoutent** et sont bien comptés séparément.
- **V-06b inclut déjà la peinture anti-moisissures** du plafond de la douche : ces 4 m² ne sont pas repeints deux fois. *(L'imprécision résiduelle sur 4 m² dans le ratio PE-05 est inférieure à la précision du chiffrage.)*
- **M-02 plinthes = 0 €** : plinthes carrelées conservées (C-01). *Réserve : si un doublage intérieur était un jour retenu, il déplacerait le nu du mur et rendrait ces plinthes inutilisables — ce n'est pas le cas ici.*
- **I-03 / I-04 doublage intérieur = 0 €**, hors périmètre : l'humidité étant écartée, il n'y a pas de mur à doubler.

> ⚠️ **I-01 : la surface de combles est une hypothèse, pas un métré.** **Aucune vue des combles n'existe à ce jour.** Volume, accessibilité, état de charpente, présence d'un plancher, ventilation en sous-face : tout est inconnu. **Ne pas engager cette ligne avant d'être monté.** Épaisseur à écrire au devis : **245 à 300 mm** de laine soufflée pour R = 7, pas « 30 cm » par convention.

### Total du niveau « CONFORTABLE » (décent + incrément + substitution inertie), hors lot 03

| | Bas | Moyen | Haut |
|---|---|---|---|
| **HT** | **19 241 €** | **31 758 €** | **50 187 €** |
| **TTC** | **21 149 €** | **34 886 €** | **55 119 €** |

*(hors branche B1, ajoutée au § 6)*

---

## 5. BRANCHE A — Assainissement : **non tranché**, les deux cas chiffrés séparément

Le SIEA de l'Est du Libournais exerce **à la fois** la compétence assainissement collectif (14 communes sur 27 raccordées) **et** la compétence SPANC. Le lieu-dit Robin est un **écart de coteau** : l'hypothèse ANC est sérieuse mais **non établie**. **Seul le SPANC tranche.**

### Branche A1 — raccordement au réseau collectif

**Coût du lot 03 au titre de la réhabilitation ANC : 0 €.**

**Mais A1 n'est PAS gratuite**, et ces postes ne sont chiffrés dans aucune source disponible :

| Poste | Statut |
|---|---|
| Boîte de branchement | **À CHIFFRER — donnée manquante** |
| Tranchée jusqu'au domaine public | **À CHIFFRER — donnée manquante** |
| Mise en séparatif EP / EU (une maison ancienne a souvent les eaux mêlées) | **À CHIFFRER — donnée manquante** |
| **PFAC** (participation pour le financement de l'assainissement collectif) | **À CHIFFRER — montant fixé par délibération, à demander au SIEA** |

> **Deux règles à connaître avant d'espérer économiser** : le raccordement est **obligatoire dans un délai de deux ans** (art. L. 1331-1 CSP), et tant que le propriétaire ne s'est pas raccordé, **il doit payer une somme au moins équivalente à la redevance** qu'il aurait acquittée. Différer ne rapporte rien.
> **Action : un appel au SIEA — 05 57 74 55 21 — tranche la branche A et donne la grille PFAC.** C'est l'action de plus fort rendement du dossier après le contrôle plomb/galva.

### Branche A2 — réhabilitation ANC complète *(hypothèse la plus probable au vu du diagnostic)*

**Chiffrage retenu — forfait englobant A-10, sans aucun cumul :**

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A-10 | Réhabilitation ANC complète : étude, fosse toutes eaux, traitement, terrassement, vidange et comblement de l'existant, contrôles | 1 | forfait | 5 170 | 8 460 | 13 630 | 5 170 | 8 460 | 13 630 | 10 % | C-19 / C-15 / C-13 |
| | **TTC** | | | | | | **5 687** | **9 306** | **14 993** | | |

**⚠️ Les trois doubles comptes possibles, tous évités :**
1. **A-10 est un forfait englobant** — il ne se cumule **ni avec A-01** (étude de sol) **ni avec A-02 à A-09**. Rien ne lui a été ajouté.
2. **A-04 et A-04b incluent déjà la fosse toutes eaux** — A-02 ne doit pas leur être ajoutée.
3. **A-05 (micro-station) remplace** la fosse et le traitement aval — ni A-02 ni A-03 avec elle.

**Contrôle de cohérence par la voie détaillée** *(non cumulable avec A-10, présenté uniquement pour valider le forfait)* :

| Réf | Désignation | Qté | Total bas HT | Total moy HT | Total haut HT | TVA |
|---|---|---|---|---|---|---|
| A-01 | Étude de sol et de filière | 1 | 315 | 635 | 1 190 | **20 %** |
| A-04b | Fosse toutes eaux + **filtre à sable drainé** (inclut la fosse) | 1 | 4 675 | 6 078 | 7 480 | 10 % |
| A-07 | Vidange fosse existante par vidangeur agréé | 1 | 180 | 288 | 432 | 10 % |
| A-08 | Comblement d'ouvrage abandonné (fosse **et** puisard) | 2 | 558 | 1 024 | 1 488 | 10 % |
| A-09 | Contrôles SPANC conception + bonne exécution | 1 | 150 | 225 | 300 | *à confirmer* |
| | **Total HT** | | **5 878** | **8 250** | **10 890** | |

> **Les deux voies se recoupent à la valeur moyenne (8 460 vs 8 250 € HT, écart 2,5 %).** Le forfait A-10 est retenu parce qu'il porte une **borne haute plus honnête** (13 630 vs 10 890 € HT) : la borne haute n'est pas théorique ici — regards en intérieur de véranda et sous dalle béton fissurée, **accès pelle à vérifier**, sol qui n'infiltre visiblement plus. **Le facteur n° 1 est l'accessibilité du terrain à un engin**, pas le choix de la filière.
> **Le filtre à sable *drainé* est retenu dans la voie de contrôle** parce que l'existence d'un puisard saturé oriente vers un sol qui n'infiltre plus — **hypothèse à faire trancher par l'étude A-01, pas par un chiffrage.** Un drainé exige un **exutoire** (fossé, réseau pluvial) dont la disponibilité est à vérifier avant tout devis.
> **Séquencement, plus important que le prix** : le contrôle de bonne exécution se fait **fouilles ouvertes, avant remblaiement**. Un chantier rebouché avant passage du SPANC est un chantier à rouvrir.
> **Échéance impérative** : si le contrôle SPANC annexé à la vente conclut à la non-conformité, le **délai d'un an de mise en conformité court déjà** et n'est pas écartable par clause. **Vérifier immédiatement dans l'acte.**

---

## 6. BRANCHE B — Fissures de la véranda : **activité non mesurée**

Deux fissures verticales sur le même volume (C-14 traversante sur toute la hauteur, ~2,20 ml, coupant les blocs ; C-12 au-dessus du linteau de la porte). **Deux fissures verticales sur le même volume, ce n'est plus une coïncidence.**
L'information « la fissure était déjà là à l'achat » **ne renseigne pas sur l'activité** : ancienneté et activité sont deux choses différentes.

### B1 — hypothèse fissures **stabilisées**

| Réf | Désignation | Qté | U. | PU bas | PU moy | PU haut | Total bas | Total moy | Total haut | TVA | Constat |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PL-02 (proxy) | Reprise d'enduit sur fissures véranda | 2,0 | m² | 28,70 | 47,80 | 76,40 | 57 | 96 | 153 | 10 % | C-14 / C-12 |
| | **TTC** | | | | | | **63** | **105** | **168** | | |

> **PROXY assumé.** Le **mastic élastomère de rebouchage souple** — qui est justement ce qui distingue une reprise de fissure d'une reprise d'enduit ordinaire — **n'a aucune ligne dans la base de prix**. La part « souple » du traitement est donc **À CHIFFRER — donnée manquante**.
> Comme pour PL-02, ces 96 € ne paient pas un déplacement : **à grouper impérativement avec les autres postes de plâtrerie en un seul passage.**

### B2 — hypothèse fissures **actives**

**NON CHIFFRÉ — expertise structure requise.**

Aucun prix de reprise en sous-œuvre, de micropieux ou de longrine n'existe dans la base de prix. **Il n'en sera pas fabriqué.**

**Ordre de grandeur documenté, cité tel quel :**
- `01-diagnostic/synthese.md`, C-14 : *« quelques centaines d'euros de rebouchage si stabilisé, reprise en sous-œuvre par micropieux si actif — **chantier à cinq chiffres** »*
- `05-reglementaire/cadre.md`, § 9 : retrait-gonflement des argiles, *« fissuration, reprise en sous-œuvre — **chiffres à cinq zéros** »*

### Provision pour aléa structurel — **isolée, hors total**

| Poste | Montant | Nature |
|---|---|---|
| **Provision aléa structurel** | **10 000 €** | **borne basse de l'ordre de grandeur documenté** ci-dessus |

> **Ce n'est pas un prix de la base de prix, et ce n'est pas présenté comme tel.** C'est la borne basse d'un montant « à cinq chiffres », posée comme provision de cadrage.
> Elle est **portée sur une ligne séparée dans chaque scénario, hors total**, pour qu'elle puisse être **retirée d'un trait** le jour où la stabilité est prouvée.
> **Coût de la mesure qui permet de la retirer : proche de zéro.** Deux témoins plâtre en travers de chaque fissure, ou deux fissuromètres à quelques euros, datés au feutre. Relevé à 3 mois puis à 6 mois, en couvrant si possible un été.
> **C'est l'intérêt direct du maître d'ouvrage de faire cette mesure : elle allège le budget au lieu de l'alourdir.** Aucune autre action du dossier n'a ce rapport coût / enjeu.
> **Volet assurance, indépendant du chiffrage** : le retrait-gonflement des argiles est indemnisable au titre des **catastrophes naturelles**, mais uniquement si une **police multirisque habitation est active au moment de l'événement**. Après 7 ans d'inoccupation, la quasi-totalité des contrats excluent, résilient ou plafonnent très fortement. **Un bien laissé sans assurance est un bien qui ne pourra rien réclamer.**

---

## 7. Recettes — à porter en ligne de recette, **pas** en dépense négative

| Réf | Poste | Montant | Condition |
|---|---|---|---|
| CH-05b | Consignes de **4 bouteilles de propane ~35 kg** (C-22) | **16 – 40 €** | **sans** bulletin de consignation |
| CH-05b | idem | **140 – 360 €** | **avec** bulletin de consignation |

> **L'écart est presque d'un facteur 9, et l'action qui le déclenche est gratuite : réclamer les bulletins de consignation au vendeur.** Relever au préalable le distributeur et le numéro de collier sur chaque bouteille, et déterminer pleines ou vides (la tare est gravée sur le collier).
> **En attendant : rentrer dans l'abri les 2 bouteilles laissées à même le sol à l'extérieur**, debout, robinet fermé. Stockage non conforme et exposé au vol comme au choc thermique.

---

## 8. Provision pour aléas

**15 %, et non 12 %.** La règle du projet impose 12 % minimum et **15 % tant qu'il reste des inconnues structurelles ou d'humidité**. Ici :

| Inconnue | État |
|---|---|
| Activité des fissures C-14 / C-12 | **non mesurée** |
| Combles et 4 pans de toiture | **non documentés** |
| Nature du réseau de plomberie (plomb / galva ?) | **non vérifiée** |
| Zonage PPRI de la parcelle | **non tranché** (conditionne la hauteur du tableau et des prises) |
| Régime d'assainissement | **non tranché** |

La provision de 15 % est appliquée **sur le TTC des travaux**, hors provision structurelle et hors aides.

---

## 9. Lignes NON CHIFFRÉES faute de données

> Un budget avec des trous identifiés vaut mieux qu'un budget complet à moitié inventé. Chacune de ces lignes est **absente de la base de prix** ou repose sur une donnée que je n'ai pas.

### Postes de dépense non chiffrés

| # | Poste | Pourquoi | Impact estimé |
|---|---|---|---|
| 1 | **Coffret divisionnaire secondaire** (C-18, IP55, 4 disjoncteurs + C20, aucun différentiel) | Aucune ligne dans la base pour un petit coffret étanche | quelques centaines d'€ |
| 2 | **Branche A1** : boîte de branchement, tranchée, mise en séparatif, **PFAC** | Aucun montant sourcé — grille à demander au SIEA | **potentiellement lourd** |
| 3 | **Branche B2** : reprise en sous-œuvre / micropieux | Aucun prix dans la base — **expertise requise** | **cinq chiffres** (couvert par la provision isolée) |
| 4 | **Mastic élastomère souple** de rebouchage des fissures (B1) | Aucune ligne | faible |
| 5 | **P-04b** — évacuations Ø32–50 de raccordement d'appareils | *non trouvé* dans la base ; **ne pas appliquer le prix du Ø100, il serait très majorant** | faible à moyen |
| 6 | **Désinfection / vidange du ballon ECS** s'il est conservé (**risque légionelle** après 7 ans d'eau stagnante) | Aucune ligne dans la base | faible, mais **sanitaire, non optionnel** |
| 7 | **Minimum d'intervention / forfait de déplacement artisan** (PL-02, PL-03b, B1, S-01a) | Non sourcé pour le Libournais | **écrase les sous-totaux < 500 €** |
| 8 | **Traitement termites / état parasitaire** | Gironde entière en zone d'arrêté préfectoral ; aucune ligne dans la base ; **l'état parasitaire est dans le DDT, non lu** | **ne pas chiffrer à zéro par défaut** |
| 9 | **Décapage de peintures anciennes au plomb** (si PE-03 boiseries) | CREP non lu ; VLEP plomb divisée par 3 depuis le 09/04/2026 → surcoût entreprise | moyen |
| 10 | **A-08b** — extraction et évacuation complète d'une cuve abandonnée | *non trouvé* — ne pas l'estimer par majoration | moyen |
| 11 | **Tarif SPANC du SIEA Est du Libournais** (A-09) | Non trouvé — grille fixée par délibération | faible |
| 12 | **Barème déchèterie SMICVAL / USTOM** (D-04) | Non trouvé — **un appel de dix minutes vaut mieux que n'importe quelle fourchette** | faible |
| 13 | **Coefficient m³ → tonne des gravats** | Non sourcé — empêche d'anticiper les dépassements de tonnage en benne | faible |
| 14 | **Honoraires de maîtrise d'œuvre et d'architecte** | La base les porte « *à sourcer* ». Le taux 8–15 % utilisé au scénario A vient de la **mission de chiffrage**, pas d'une source de marché | **structurant sur A** |
| 15 | **Assurance dommage-ouvrage** | La base la porte « *à sourcer* ». Ordres de grandeur cadre.md : **2–3 % en rénovation, 3–5 % en autoconstruction** — sources secondaires | moyen |
| 16 | **CH-04c** — création d'un conduit de fumée complet | *non trouvé* — sans objet a priori (2 conduits existants) mais **à faire vérifier par un fumiste** | s.o. |

### Données de métré manquantes

| Donnée | Conséquence |
|---|---|
| **Nombre de portes intérieures** | M-01 chiffré sur une hypothèse de 4 |
| **Surface et accessibilité des combles** | I-01 chiffré sur une hypothèse de 85 m² — **aucune vue des combles** |
| **Surface réelle de murs tapissés** | PL-06 et PL-01 chiffrés sur 130 m² |
| **Plan des niveaux, nombre de pièces** | conditionne le nombre de points électriques, d'entrées d'air et la valeur locative |
| **Usage prévu du bien** (RP / locatif / secondaire) | **bloque tout le calcul des aides** |

### Données manquantes pour le scénario C (auto-rénovation)

**Colonne « matériaux seuls » absente de la base** — ces lignes sont exclues du total C et doivent être relevées en magasin :
E-07 (circuit 32 A) · E-07b ×4 (circuits 20 A) · E-10 (coffret com) · P-04 (évacuation PVC Ø100) · PL-06 (décolleuse vapeur + produit décolleur) · S-01a (carreaux de remplacement) · M-02 (plinthes).

**Temps d'auto-rénovation absent de la base** : **aucun h/unité n'existe sur les lots 01 (élec), 02 (plomberie), 03 (ANC), 04 (chauffage), 07 (ventilation).** Le volume d'heures donné au § scénarios est donc un **plancher**, portant sur les seuls lots 08 à 13.

---

## 10. Éligibilité aux aides, lot par lot — **aucun montant, par construction**

**`reno-aides` n'a pas encore tourné.** L'**usage prévu du bien** (résidence principale / locatif / résidence secondaire) reste inconnu, or **c'est le filtre n° 1** de tous les dispositifs. **Aucun montant d'aide n'est fabriqué ici.**

Chaque scénario porte une ligne **« Aides à déduire — non quantifiées »**.

| Lot | TVA applicable | Aide potentielle | Condition bloquante | **L'auto-rénovation fait-elle perdre une aide ?** |
|---|---|---|---|---|
| 01 Électricité | 10 % | **aucune** | — | **NON** — rien à perdre |
| 02 Plomberie | 10 % | **aucune** | — | **NON** |
| 03 ANC | 10 % (A-01 à 20 %) | Agence de l'eau Adour-Garonne **4 200 €/logement**, éco-PTZ, aide départementale | **Uniquement en opération groupée** portée par la collectivité — un propriétaire seul **ne peut pas la solliciter** | sans objet (terrassement non auto-réalisable) |
| 04 — CH-01 / CH-01b radiateurs | 10 % | **aucune** | — | **NON** |
| 04 — CH-02 ballon ECS électrique | 10 % | **aucune** | — | **NON** |
| 04 — CH-03 chauffe-eau thermodynamique | **5,5 %** | MPR 400–1 200 € + CEE 150–600 € | **RGE obligatoire** | **OUI, tout est perdu** |
| 04 — CH-04 poêle à granulés | **5,5 %** | MPR 750–1 250 € + CEE 250 € | **RGE + Flamme Verte 7★ + tubage inox isolé Ø80/100** | **OUI — de l'ordre de 1 700 à 2 300 €** |
| 05 Couverture | 10 % | aucune | — | sans objet (0 €) |
| 06 Menuiseries ext. | — | — | — | sans objet (0 €) |
| 07 — V-01 VMC autoréglable | 10 % | **aucune** | — | **NON** |
| 07 — **V-02 VMC hygro B** | **5,5 %** | MPR/CEE *non confirmés en session* | **RGE + logement > 2 ans** | **OUI (le taux réduit au minimum)** |
| 07 — V-05, V-06b | 10 % | aucune | — | **NON** |
| 08 — **I-01 isolation combles** | **5,5 %** | MPR + CEE, **montants non chiffrés en session** | **entreprise RGE — sans RGE, retour à 10 %** | **OUI** |
| 09 Plâtrerie | 10 % *(5,5 % possible en travail induit indissociable d'une isolation éligible)* | aucune en propre | à faire **acter sur le devis** | **NON** |
| 10 Sols | 10 % | aucune | — | **NON** |
| 11 Peinture | 10 % | aucune | — | **NON** |
| 12 Menuiseries int. | 10 % | aucune | — | **NON** |
| 13 Dépose / évacuation | 10 % ou 20 % *(voir note D-03)* | aucune | — | **NON** |

**Les lots où l'auto-rénovation ne perd AUCUNE aide — c'est ce qui construit le scénario D :**
> **01 Électricité · 02 Plomberie · 04 radiateurs électriques (CH-01/CH-01b) · 04 ballon ECS électrique (CH-02) · 07 entrées d'air et fongicide · 09 Plâtrerie · 10 Sols · 11 Peinture · 12 Menuiseries intérieures · 13 Dépose.**
> Sur ces lots, l'auto-rénovation ne perd **que** l'écart de TVA (20 % au lieu de 10 %) sur la part fourniture, et la garantie. Sur les lots à forte main-d'œuvre — peinture, détapissage, joints — c'est franchement gagnant.

**Les lots où l'auto-rénovation coûte des aides :**
> **V-02 (VMC hygro B)** · **I-01 (isolation combles)** · **CH-03 (CET)** · **CH-04 (poêle granulés)**. Sur CH-04 en valeur moyenne, la perte est de l'ordre de **1 700 à 2 300 €** — **avant même de compter la main-d'œuvre économisée.** Ce sont exactement les lots à confier à un pro RGE.

**Piste spécifique à ce bien, à instruire :** le logement est **vacant depuis 7 ans**. Plusieurs dispositifs (Anah, aides locales, primes communales ou intercommunales) visent spécifiquement les **logements vacants depuis plus de 2 ans remis en location**. **7 ans de vacance peuvent ouvrir des droits qu'un bien ordinaire n'a pas** — conditionné à la réponse sur l'usage.

**Fonds Barnier — l'alerte à retenir :** le plafond de **10 % de la valeur vénale** mord ici. Prix d'acquisition 60 000 € → assiette subventionnable de l'ordre de **6 000 €**, très loin des 36 000 € affichés. **Le fonds Barnier ne financera pas un gros programme sur ce bien.**

**Séquencement, et c'est un piège coûteux :** une aide sollicitée **après signature du devis** ou après travaux est en général **perdue**. Faire tourner `reno-aides` **avant tout engagement**.

---

## 11. Contrôles de cohérence effectués

| Contrôle | Résultat |
|---|---|
| Lot 01 ré-aiguillage (4 545 / 7 570 / 12 341 € HT) vs repères C-17 (mise en sécurité 1 500–3 000 ; refonte 5 000–10 500 € HT) | Cohérent en bas et moyen. **Borne haute au-dessus du repère → retenir le ratio E-01** |
| Lot 01 variante E-01 (4 845 / 7 650 / 10 540 € HT) vs repère refonte 5 000–10 500 € HT | **Cohérent** |
| Lot 02 (18–42 €/m² hab) vs ratio de contrôle 50–110 €/m² HT | **Sous le ratio** — cohérent avec la conservation des sanitaires. **La variante P-11 recoupe la pré-estimation C-23** |
| Lot 03 A-10 (5 170 / 8 460 / 13 630 € HT) vs voie détaillée (5 878 / 8 250 / 10 890 € HT) | **Écart de 2,5 % en valeur moyenne** — forfait validé |
| Lot 03 vs cadre.md (réhabilitation 5 000–15 000 €, jusqu'à 20 000 € en terrain difficile) | **Cohérent** |
| Lot 11 PE-05 vs recoupement indépendant (3,2 × surface habitable × 20,50 €/m²) | **Cohérent** |
| Provision aléas | **15 %** appliqués, conformément à la règle |
| Additions HT / TTC | **Aucune addition mixte** — vérifié ligne par ligne dans `calcul.py` |

---

## 12. Actions gratuites, par rendement décroissant

| # | Action | Ce qu'elle tranche | Coût |
|---|---|---|---|
| 1 | **Poser deux témoins plâtre** sur C-14 et C-12, relever à 3 et 6 mois | **Retire ou confirme la provision de 10 000 €** | quelques € |
| 2 | **Appeler le SIEA Est du Libournais** — 05 57 74 55 21 | **Branche A1 ou A2 : écart de 5 700 à 15 000 € TTC** + existence d'une opération groupée (forfait 4 200 €) | 0 € |
| 3 | **Contrôle visuel plomb/galva** au compteur et sous évier | **Variante P-11 : écart de 7 000 à 11 000 € HT** | 0 € |
| 4 | **Lire le DDT du notaire** et l'état des risques annexé à l'acte | PPRI, termites, plomb, amiante, DPE, rapport SPANC — **tout d'un coup** | 0 € |
| 5 | **Vérifier la couverture d'assurance** du bien inoccupé depuis 7 ans | Conditionne toute indemnisation CatNat sécheresse (C-14) | 0 € |
| 6 | **Monter dans les combles et photographier**, plus les 4 pans de toiture | Débloque I-01 et lève la réserve du lot 05 | 0 € |
| 7 | **Réclamer les bulletins de consignation** des 4 bouteilles au vendeur | Recette × 9 (16–40 € → 140–360 €) | 0 € |
| 8 | **Chercher les carreaux de réserve** (garage, buanderie, comble) | Rend la reprise S-01a invisible au lieu de visible | 0 € |
| 9 | **Répondre à la question de l'usage prévu** du bien | **Débloque tout le calcul des aides** | 0 € |
| 10 | **Ne pas résilier le contrat d'électricité** | Éviterait le déclenchement de plein droit du Consuel | 0 € |

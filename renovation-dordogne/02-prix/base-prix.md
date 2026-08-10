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

> **Bloc créé le 10/08/2026** — agent `reno-prix-marche`. Bien de référence : maison 85 m² habitables, Castillon-la-Bataille (33350), bâti ancien pierre, réseau partiellement coupé → hypothèse refonte totale.

### Avertissement méthodologique (vaut pour les lots 01 et 02)

1. **WebFetch était bloqué par la politique d'egress réseau pendant toute la session** (tous domaines testés : travaux.com, ootravaux.fr, habitatpresto.com, consuel.com, anil.org, batiprix.com, leroymerlin.fr, service-public.fr). Les chiffres ci-dessous proviennent des **extraits de résultats de recherche**, pas de lectures de pages complètes. Aucune ligne ne dépasse donc la confiance **moyenne**, sauf tarif réglementé.
2. **Convention HT/TTC.** La majorité des guides de prix grand public ne précisent pas leur base. Convention retenue : *valeur publiée non qualifiée = traitée comme HT*. C'est le choix prudent pour un budget (il majore le TTC). Les valeurs explicitement données TTC ont été ramenées en HT à 10 %. Chaque ligne indique ce qui a été fait.
3. **Abattement régional.** Sources croisées : l'Île-de-France facture +15 à +25 % vs province, et jusqu'à +44 % sur une rénovation électrique complète vs départements ruraux. Mais la Gironde n'est pas une région basse : le taux horaire électricien à Bordeaux est relevé à ~80 €/h TTC, au-dessus de la moyenne nationale (35–95 €/h). Castillon-la-Bataille est en Libournais rural, à ~45 km de Bordeaux : main-d'œuvre moins chère qu'en métropole, mais frais de déplacement et faible densité d'artisans qui rognent le gain. **Abattement retenu : −8 % sur la seule part main-d'œuvre**, milieu de la fourchette autorisée (−5 à −12 %). Réduit à −5 % sur les lignes dominées par la mobilisation (petites interventions, déplacements). **Jamais appliqué sur la fourniture.**
4. **Colonne « matériaux seuls TVA 20 % »** : issue de sources distributeur quand elles ont été obtenues, sinon **dérivée de la part fourniture du prix entreprise et signalée comme telle**. Un particulier n'a pas la remise pro : cette colonne est un plancher, pas une promesse.
5. Rappel TVA confirmé en session : **10 %** travaux d'amélioration sur logement achevé depuis plus de 2 ans réalisés par une entreprise (fourniture + pose facturées par elle), **5,5 %** amélioration énergétique éligible, **20 %** matériaux achetés en direct par le particulier. Depuis le 01/03/2025 l'attestation CERFA n'est plus exigée, une mention sur le devis suffit. **Aucune ligne du lot 01 n'est éligible au 5,5 %** : une rénovation électrique n'est pas un travail d'amélioration de la performance énergétique.

### Tableau — Lot 01

Tous les PU sont **HT, fourniture + pose par une entreprise**, après abattement régional. TTC calculé à **10 %**.

| Réf | Désignation | Unité | PU bas HT | PU moyen HT | PU haut HT | Fourn. / Pose | TTC 10 % (bas/moy/haut) | Matériaux seuls TTC 20 % | Confiance |
|---|---|---|---|---|---|---|---|---|---|
| E-01 | Rénovation électrique complète, refonte totale, bâti ancien — hors plus-value pierre | m² hab. | 57 | 90 | 124 | 40 / 60 | 63 / 99 / 136 | 30–50 €/m² | moyenne |
| E-01b | Plus-value encastrement en maçonnerie pierre / moellon | % | +20 % | +30 % | +40 % | — / 100 | idem | — | moyenne |
| E-02 | Point lumineux simple allumage, encastré, gaine ICTA, boîte DCL — hors luminaire | point | 66 | 113 | 188 | 25 / 75 | 73 / 124 / 207 | 15–35 € *(dérivé)* | moyenne |
| E-03 | Point lumineux commandé en va-et-vient (2 commandes + navettes) — hors luminaire | point | 113 | 169 | 263 | 25 / 75 | 124 / 186 / 289 | 25–55 € *(dérivé)* | moyenne |
| E-04 | Prise de courant 16 A + T, encastrée, sur circuit existant | u | 65 | 108 | 168 | 20 / 80 | 72 / 119 / 185 | 12–28 € *(dérivé)* | moyenne |
| E-05 | Tableau électrique 3 rangées équipé (≈15–20 départs), dépose ancien inclus | ens. | 621 | 1 052 | 1 912 | 45 / 55 | 683 / 1 157 / 2 103 | 400–750 € | moyenne |
| E-06 | Mise à la terre : piquet, conducteur cuivre nu 25 mm², barrette de coupure, mesure | ens. | 188 | 395 | 752 | 25 / 75 | 207 / 435 / 827 | 80–150 € | moyenne |
| E-07 | Circuit spécialisé 32 A (plaque de cuisson), câble 6 mm², boîte 32 A, protection | u | 123 | 189 | 283 | 30 / 70 | 135 / 208 / 311 | *non trouvé* | moyenne |
| E-07b | Circuit spécialisé 20 A (four, lave-linge, lave-vaisselle), câble 2,5 mm² | u | 85 | 123 | 165 | 30 / 70 | 94 / 135 / 182 | *non trouvé* | moyenne |
| E-08 | Tirage gaine ICTA + conducteurs, **apparent** (moulure/goulotte, combles, vide sanitaire) | ml | 4,70 | 8,40 | 14,00 | 15 / 85 | 5,20 / 9,20 / 15,40 | 0,20–2,00 €/ml | moyenne |
| E-08b | Tirage gaine ICTA + conducteurs, **encastré** en maçonnerie courante (saignée + rebouchage) | ml | 6,50 | 11,20 | 20,50 | 15 / 85 | 7,20 / 12,30 / 22,60 | 0,20–2,00 €/ml | faible |
| E-08c | Idem **encastré en pierre / moellon** | ml | *non trouvé* | *non trouvé* | *non trouvé* | — | — | — | — |
| E-09 | Attestation Consuel jaune (particulier, avec visite) — **tarif réglementé** | forfait | 120,56 | 120,56 | 194,68 | 0 / 100 | **144,67 / 144,67 / 233,62 TTC 20 %** | s.o. | **haute** |
| E-09b | Mise en service Enedis, compteur Linky, à distance — **tarif réglementé** | forfait | — | 1,50 | — | 0 / 100 | **1,80 TTC** | s.o. | **haute** |
| E-09c | Mise en service, compteur non communicant (5 j. ouvrés / express 2 j.) | forfait | 27,24 | — | 64,03 | 0 / 100 | **32,69 / — / 76,84 TTC** | s.o. | **haute** |
| E-10 | Coffret de communication grade 2 TV, fourni posé, hors prises RJ45 | ens. | 191 | 363 | 621 | 45 / 55 | 210 / 399 / 683 | *non trouvé* | faible |

### Détail, sources et réserves — Lot 01

**E-01 — Rénovation électrique complète au m².** Fourchettes nationales relevées : 50–120 €/m², 60–130 €/m² en rénovation complète, 8 000–12 000 € pour 100 m² (soit 80–120 €/m²), ~110 €/m² en moyenne pour une installation neuve. Base nationale retenue **60 / 95 / 130 €/m² HT**. Répartition fourniture/pose calée sur le coût matériaux relevé (30–50 €/m²) rapporté au total → **40 % / 60 %**. Abattement −8 % sur les 60 % de main-d'œuvre = **−4,8 % sur le total** → 57 / 90 / 124 €/m² HT. *Réserve : ces fourchettes sont des moyennes tous types de bâti confondus. Pour ce bien, la ligne E-01b s'ajoute.*
Sources (consultées le 10/08/2026) : [travaux.com — prix rénovation électrique](https://www.travaux.com/electricite/guide-des-prix/prix-renovation-electrique) · [abctravaux.org — tarif électricien au m² 2026](https://abctravaux.org/tarif-electricien-au-m%C2%B2-2026-renovation-et-neuf/) · [renovationman.com — rénovation électricité 100 m²](https://www.renovationman.com/renovation-electrique/prix-renovation-electricite-100-m2/) · [mon-electricien.org — rénovation électrique 100 m²](https://www.mon-electricien.org/prix-dune-renovation-electrique-pour-une-maison-de-100m2/) · [ootravaux.fr — installation électrique neuve](https://www.ootravaux.fr/installation-entretien/electricite/installation-electrique/cout-installation-electrique-neuve.html)

**E-01b — Plus-value pierre.** Sourcé : la pose encastrée coûte 30 à 50 % de plus que l'apparent (2 000 à 4 000 € d'écart sur 100 m²) ; les saignées majorent de 20 à 40 % ; en murs épais type granit/meulière certains électriciens **refusent d'encastrer** et imposent la pose en saillie. Retenu : **+20 / +30 / +40 % sur la part pose uniquement**. Pas d'abattement régional supplémentaire (déjà appliqué en E-01). *À trancher sur place : si l'oncle accepte moulures et passage par combles/vide sanitaire, cette plus-value tombe presque entièrement.*
Sources : [cross-construction.com — rénover l'électricité sans saignées](https://www.cross-construction.com/comment-renover-l-electricite-d-une-maison-de-1980-sans-faire-de-saignees-dans-tous-les-murs) · [arti-elec.com — refaire l'électricité sans saignée](https://arti-elec.com/mag/informations-generales/refaire-electricite-sans-saignee) · [laurentempereur.bzh — rénovation électrique maison ancienne](https://laurentempereur.bzh/blog/electricite/renovation-electrique-maison-ancienne-normes-prix-et-etapes-du-chantier/)

**E-02 / E-03 — Points lumineux.** Relevé : point lumineux 90 € en moyenne, 90–200 € ; pose de luminaire 60–250 € ; éclairage intérieur 150–250 € HT pose comprise ; 50–150 € par point en rénovation. Base nationale E-02 : **70 / 120 / 200 € HT**. E-03 (va-et-vient) construit comme E-02 + une seconde commande : interrupteur va-et-vient 5–15 € à l'achat, pose d'interrupteur 70–130 €, installation complète 80–250 € → base **120 / 180 / 280 € HT**. Fourniture 25 % / pose 75 %, abattement −8 % sur la pose = **−6 % sur le total**.
Sources : [mon-club-elec.fr — tarif électricien](https://www.mon-club-elec.fr/tarif-electricien-2025/) · [prix-travaux-m2.com — prix éclairage intérieur](https://www.prix-travaux-m2.com/prix-eclairage-interieur.php) · [btobjob.com — prix pose luminaire 2026](https://btobjob.com/blog/prix-pose-luminaire-en-2026-tarif-electricien-et-eclairage-interieur) · [travaux-electrique.fr — installation va-et-vient](https://www.travaux-electrique.fr/prix-installation-va-et-vient) · [mesdepanneurs.fr — prix pose interrupteur](https://www.mesdepanneurs.fr/blog/prix-pose-interrupteur)
*Réserve E-03 : aucune source ne donne un prix « point va-et-vient » clé en main. La ligne est une somme de deux composants sourcés séparément. Confiance moyenne basse — à confirmer par devis.*

**E-04 — Prise 16 A.** Relevé : ajout d'une prise (point complet) 70–120 € ; fourchette large 45–400 € ; **et une donnée très exploitable pour ce chantier** : 4 prises supplémentaires dans un salon = 280–380 € en apparent (70–95 €/prise) contre 550–720 € en encastré (138–180 €/prise), hors peinture. Base nationale **70 / 115 / 180 € HT**, ce qui cadre l'apparent en bas de fourchette et l'encastré en haut. Fourniture 20 % / pose 80 %, abattement = **−6,4 % sur le total**.
Sources : [mon-club-elec.fr](https://www.mon-club-elec.fr/tarif-electricien-2025/) · [prix-pose.com — prise électrique](https://www.prix-pose.com/prise-electrique) · [cross-construction.com](https://www.cross-construction.com/comment-renover-l-electricite-d-une-maison-de-1980-sans-faire-de-saignees-dans-tous-les-murs) · [ynspir.com — prix pose prise en rénovation](https://ynspir.com/conseils-decoration/renovation/prix-renovation/prix-de-pose-dune-prise-electrique-en-renovation/)

**E-05 — Tableau électrique.** Relevé : remplacement 400–1 500 € fourniture et pose ; 770–3 300 € TTC ; 800–2 000 € TTC ; 450–1 400 € installation comprise ; **par rangée** : 2 rangées 600–1 000 €, 3 rangées 900–1 400 €. Base nationale **650 / 1 100 / 2 000 € HT** pour un tableau 3 rangées équipé sur une maison de cette taille. Part fourniture validée par le détail matériel relevé pour une maison de 100 m² : coffret 4 rangées ~90 €, 2 interrupteurs différentiels 63 A ~100 € pièce, 2 ID 40 A ~70 € pièce, 1 disjoncteur 32 A ~16 €, 8 disjoncteurs 20 A et 7 de 16 A ~10 € pièce, soit **≈ 596 € de matériel** → fourniture ≈ 45 %. Abattement = **−4,4 % sur le total**.
Sources : [travaux.com — mise aux normes tableau](https://www.travaux.com/electricite/guide-des-prix/prix-de-mise-aux-normes-dun-tableau-electrique) · [btobjob.com — tableau électrique 450 à 2000 € 1 à 5 rangées](https://btobjob.com/blog/prix-tableau-electrique-2026-de-450-a-2000-1-a-5-rangees) · [tarifartisan.fr — prix tableau électrique](https://www.tarifartisan.fr/prix-tableau-electrique/) · [leroymerlin.fr — prix rénovation électrique 100 m² (détail matériel)](https://www.leroymerlin.fr/conseils/conseils-pratiques/quel-est-prix-de-renovation-electrique-une-maison-de-100m2.html) · [izi-by-edf.fr — tableau électrique maison 100 m²](https://izi-by-edf.fr/blog/prix-tableau-electrique-maison-100-m2)
*Note PPRI : si le bien est en zone inondable, la position du tableau doit être rehaussée. Impact non chiffré ici — à traiter avec `reno-reglementaire`.*

**E-06 — Mise à la terre.** Relevé : 180–650 € pose, raccordement barrette et mesure inclus ; 300–800 € TTC en moyenne ; 500–1 000 € en maison ancienne par piquet vertical ; **matériel seul 80–150 €** (piquet acier galvanisé ou cuivre, barrette de coupure, cuivre nu 25 mm², liaison vert-jaune 16 mm²). Base nationale **200 / 420 / 800 € HT**. Fourniture 25 % (cohérent avec 80–150 € de matériel), abattement = **−6 %**.
Sources : [sparx-elec.fr — installation piquet de terre, prix](https://www.sparx-elec.fr/installation-piquet-de-terre-prix/) · [allotravaux.com — mise à la terre obligatoire](https://www.allotravaux.com/mise-a-la-terre-obligatoire/) · [travaux.com — prise de terre maison ancienne](https://www.travaux.com/electricite/guide-des-prix/prix-installation-prise-de-terre-maison-ancienne) · [prix-travaux-m2.com — prise de terre](https://www.prix-travaux-m2.com/prix-installation-prise-de-terre.php)
*Nuance locale, non sourcée mais à vérifier : terrain alluvionnaire de bord de Dordogne → résistivité a priori favorable, donc plutôt bas de fourchette. Si substrat calcaire dur, plusieurs piquets ou boucle à fond de fouille → haut de fourchette. À confirmer par mesure.*

**E-07 / E-07b — Circuits spécialisés.** Relevé : chaque circuit spécialisé 100–250 € selon complexité ; plaque de cuisson 32 A **135–300 €** selon la distance au tableau ; four ou lave-linge **90–175 €**. Rappel norme : la NF C 15-100 impose au minimum 4 circuits spécialisés (1 × 32 A boîte de sortie de câble pour la plaque en monophasé, + 3 × 16/20 A). Bases nationales : 32 A **130 / 200 / 300 € HT**, 20 A **90 / 130 / 175 € HT**. Fourniture 30 %, abattement = **−5,6 %**.
Sources : [mon-electricien.org — installation électrique neuve](https://www.mon-electricien.org/prix-installation-electrique/) · [mon-electricien.org — pose prise en rénovation](https://www.mon-electricien.org/prix-de-pose-prise-electrique-en-renovation/) · [promotelec.com — circuits électriques spécialisés](https://www.promotelec.com/professionnels/fiche/habitat-focus-sur-les-circuits-electriques-specialises/) · [schema-electrique.net — circuits spécialisés NF C 15-100](https://www.schema-electrique.net/circuits-electriques-specialises.html)
*Matériaux seuls : disjoncteur 32 A ~16 € sourcé, mais le prix du câble 6 mm² au ml n'a pas été obtenu. **Non trouvé, à confirmer par devis ou relevé en magasin.***

**E-08 / E-08b / E-08c — Tirage de gaine.** Relevé : pose de câbles et gaines **5 à 15 €/ml** ; la pose encastrée coûte **+30 à 50 %** par rapport à l'apparent ; l'encastrement des gaines avec saignées représente **1 500 à 4 000 €** en forfait sur une maison ; surcoût **30 à 60 € par saignée** selon l'épaisseur et la dureté du support. Bases nationales : apparent **5 / 9 / 15 €/ml HT**, encastré courant = apparent +30 à 50 % → **7 / 12 / 22 €/ml HT**. Fourniture 15 % / pose 85 % (la gaine nue vaut 0,20–2,00 €/ml, 0,30–0,80 €/ml en diamètre standard), abattement = **−6,8 % sur le total**.
*E-08c : **non trouvé, à confirmer par devis.** Aucune source ne donne un prix au ml d'encastrement en pierre ou moellon. Les seuls repères disponibles sont le forfait 1 500–4 000 € et les 30–60 € par saignée, qui ne se convertissent pas honnêtement en €/ml. Ne pas interpoler.*
Sources : [prix-pose.com — câblage électrique](https://www.prix-pose.com/cablage-electrique) · [habitatpresto.com — rénovation électrique appartement 70 m²](https://www.habitatpresto.com/mag/electricite/prix-renovation-electrique-appartement-70m2) · [e-comptoirelectrique.com — gaine ICTA](https://www.e-comptoirelectrique.com/gaine-icta) · [cross-construction.com](https://www.cross-construction.com/comment-renover-l-electricite-d-une-maison-de-1980-sans-faire-de-saignees-dans-tous-les-murs)
*Prix de la gaine ICTA **préfilée** 3G2,5 Ø20 en couronne de 100 m : produit identifié chez Rexel, Point.P, 123elec, matérielelectrique.com, mais **aucun prix numérique n'a pu être obtenu** (fetch bloqué, tarifs derrière compte pro). Non trouvé, à relever en agence Rexel/CEDEO Libourne.*

**E-09 — Consuel.** **Tarif réglementé, seule ligne en confiance haute du lot.** Consuel jaune (logement) particulier : **144,67 € TTC**. Vert 76,37 €, violet 230,32 €. Contre-visite après non-conformité : **233,62 € TTC**. Grille en vigueur depuis le 02/09/2025, applicable en 2026 jusqu'à la prochaine revalorisation annuelle. Le dossier particulier fait **quasi systématiquement l'objet d'une visite sur place**, contrairement au dossier déposé par un professionnel. HT calculé à 20 % (le Consuel est une prestation de service, pas un travail immobilier) : **120,56 € HT** — *taux non confirmé explicitement en source, à vérifier sur la facture*.
*Réserve d'application : le Consuel jaune n'est exigé que pour une installation neuve ou une réfection totale avec nouveau raccordement. Sur une rénovation partielle sans intervention Enedis, il n'est pas systématiquement requis. Ici, refonte complète des deux réseaux → à prévoir.*
Sources : [jechange.fr — Consuel 2026](https://www.jechange.fr/energie/electricite/consuel) · [kelwatt.fr — Consuel tarifs 2026](https://www.kelwatt.fr/demenagement/consuel) · [papernest.com — attestation Consuel 2026](https://www.papernest.com/demarches-energie/decrypter/consuel/) · [electricite.net — Consuel](https://electricite.net/guides/demenagement/consuel)

**E-09b / E-09c — Mise en service.** Grille Enedis **en vigueur du 01/08/2026 au 31/07/2027** (indexation +0,9 % au 1er août) : mise en service sur compteur Linky **1,80 € TTC** sous 24 h à distance ; sur compteur non communicant **32,69 € TTC** sous 5 jours ouvrés ou **76,84 € TTC** en express sous 2 jours. Changement de puissance : 4,02 € TTC en Linky, 64,87 € TTC en compteur classique. Raccordement neuf à partir de **426,24 € après réfaction**, plus cher en **zone ZFB (rurale)** — ce qui est le cas de Castillon-la-Bataille. **Confiance haute : tarif réglementé, grille de moins de 15 jours.**
Sources : [gridlabs.fr — frais de mise en service Enedis 2026](https://www.gridlabs.fr/demenagement/frais-mise-service) · [fournisseurs-electricite.com — tarifs Enedis 2026](https://www.fournisseurs-electricite.com/enedis/tarifs) · [papernest.com — tarif Enedis 2026](https://www.papernest.com/demarches-energie/enedis/tarif/) · [prix-elec.com — tarifs Enedis 2026](https://prix-elec.com/energie/reseau/enedis/tarifs)
*Si le compteur du bien est ancien et hors service depuis longtemps, un raccordement / une modification de branchement peut être requis, bien au-delà de la simple mise en service. **Non chiffrable ici : à confirmer par une demande Enedis.***

**E-10 — Coffret de communication.** Relevé : installation estimée **150 à 650 €** hors travaux de rénovation, incluant coffret ou DTI et prise ; un devis réel cité à **2 000 € pour un coffret grade 2 + 8 prises RJ45** sur une maison de 200 m² avec cheminements encastrés et apparents, soit ordre de **170 €/prise RJ45 supplémentaire** tout compris. Base nationale **200 / 380 / 650 € HT** pour le coffret seul. Abattement = **−4,4 %**. **Confiance faible : seulement deux sources porteuses de chiffres exploitables, et le prix du coffret grade 2 TV nu n'a pas été obtenu malgré identification chez Leroy Merlin, Bricoman, 123elec et Hager.**
Sources : [monelectricite.pro — coût des coffrets de communication](https://monelectricite.pro/cout-coffret-de-communication/) · [prix-pose.com — prise téléphonique](https://www.prix-pose.com/prise-telephonique) · [123elec.com — coffrets grade 2 TV](https://www.123elec.com/coffrets-de-communication-vdi-tv/coffrets-de-communication/coffrets-de-communication-grade-2-tv.html)

### Contexte main-d'œuvre — Lot 01

Taux horaire électricien relevé le 10/08/2026 : national **35–95 € TTC/h** (45–70 € HT/h sur chantier planifié) ; **Gironde 59 €/h (dépannage simple) à 102 €/h (domotique/IRVE), courant 80 €/h TTC à Bordeaux**. C'est ce différentiel Bordeaux/national qui justifie de **ne pas descendre à −12 %** d'abattement : Castillon est rural, mais le bassin de main-d'œuvre reste celui de la métropole bordelaise.
Sources : [prix-electricien-maison.fr — Bordeaux](https://www.prix-electricien-maison.fr/bordeaux/) · [izi-by-edf.fr — taux horaire électricien](https://izi-by-edf.fr/blog/tarif-horaire-electricien) · [servicesartisans.fr — prix électricien 2026](https://servicesartisans.fr/blog/prix-electricien-2026-tarifs-travaux) · [adora-economie.fr — prix rénovation m² 2026 (écarts régionaux)](https://adora-economie.fr/prix-renovation-m2-2026.html) · [a-travaux-de-renovation.fr — baromètres départementaux](https://a-travaux-de-renovation.fr/prix-renovation)

---

## Lot 02 — Plomberie / sanitaire

> **Bloc créé le 10/08/2026** — agent `reno-prix-marche`. Mêmes conventions et mêmes réserves méthodologiques que le lot 01 (voir encadré ci-dessus). Hypothèse : arrivées d'eau coupées → reprise complète du réseau, dépose probable d'un existant plomb ou acier galvanisé.

### Tableau — Lot 02

Tous les PU sont **HT, fourniture + pose par une entreprise**, après abattement régional. TTC calculé à **10 %**.

| Réf | Désignation | Unité | PU bas HT | PU moyen HT | PU haut HT | Fourn. / Pose | TTC 10 % (bas/moy/haut) | Matériaux seuls TTC 20 % | Confiance |
|---|---|---|---|---|---|---|---|---|---|
| P-01 | Alimentation **PER** Ø16 sous fourreau, y c. raccords et fixations | ml | 7,60 | 11,30 | 14,20 | 30 / 70 | 8,40 / 12,40 / 15,60 | ~0,73 €/ml *(tube seul, hors raccords)* | moyenne |
| P-02 | Alimentation **multicouche** Ø16–20, y c. raccords à sertir | ml | 11,30 | 17,00 | 26,40 | 30 / 70 | 12,40 / 18,70 / 29,00 | 0,89–1,93 €/ml *(tube nu)* | faible |
| P-03 | Alimentation **cuivre** écroui/recuit, brasé | ml | 19,00 | 30,50 | 47,60 | 40 / 60 | 20,90 / 33,60 / 52,40 | *non trouvé* | moyenne |
| P-04 | Évacuation **PVC Ø100/110**, intérieur, fourni posé | ml | 42,50 | 66,10 | 94,40 | 30 / 70 | 46,80 / 72,70 / 103,80 | *non trouvé* | moyenne |
| P-04b | Évacuation PVC Ø32–50 (raccordement appareils) | ml | *non trouvé* | *non trouvé* | *non trouvé* | — | — | — | — |
| P-05 | **Point d'eau complet** : alimentation EF + ECS et évacuation, sur réseau existant | u | 94 | 189 | 283 | 30 / 70 | 104 / 208 / 312 | *dérivé : 34–102 €* | moyenne |
| P-06 | **Salle de bain complète, gamme fonctionnelle** 4–5 m² : douche, meuble-vasque, faïence partielle, pose incluse | ens. | 3 824 | 4 971 | 6 214 | 45 / 55 | 4 206 / 5 468 / 6 835 | *dérivé : 2 065–3 356 €* | moyenne |
| P-06b | **Salle de bain complète, gamme haute** : douche à l'italienne, robinetterie encastrée, carrelage toutes hauteurs | ens. | 6 979 | 9 560 | 12 906 | 45 / 55 | 7 677 / 10 516 / 14 197 | *dérivé : 3 769–6 969 €* | moyenne |
| P-07 | **WC classique au sol**, fourni posé sur attentes existantes | u | 143 | 248 | 381 | 40 / 60 | 157 / 272 / 419 | *dérivé : 69–183 €* | moyenne |
| P-08 | **WC suspendu** + bâti-support autoportant + habillage, fourni posé | u | 526 | 813 | 1 243 | 45 / 55 | 578 / 894 / 1 367 | 250–700 € | moyenne |
| P-09 | **Cuisine** : alimentation + évacuation évier, alimentation + évacuation lave-vaisselle, robinet d'arrêt — hors ml de réseau | ens. | 302 | 472 | 661 | 30 / 70 | 332 / 519 / 727 | *dérivé : 109–238 €* | faible |
| P-10 | **Ballon ECS électrique 150–200 L** stéatite, fourni posé, groupe de sécurité et support inclus | u | 658 | 1 016 | 1 597 | 60 / 40 | 724 / 1 118 / 1 757 | 600–1 716 € | moyenne |
| P-11 | **Dépose réseau plomb / acier galvanisé + pose réseau neuf + reprise des supports** | ml | 103 | 136 | 168 | 20 / 80 | 113 / 149 / 185 | s.o. | moyenne |
| P-11b | Dépose seule, sans repose | ml | *non trouvé* | *non trouvé* | *non trouvé* | — | — | — | — |

### Détail, sources et réserves — Lot 02

**P-01 / P-02 / P-03 — Réseaux d'alimentation, les trois matériaux distingués.**
Relevé national fourni-posé : **PER 9–13 €/ml**, également donné **8–15 €/ml fourni et posé** ; **multicouche 10–100 €/ml** selon diamètre et type de raccord ; **cuivre 11–50 €/ml**, dont **15–25 €/ml pour la seule pose**. Fourchette générale toutes matières 6–100 €/ml TTC, avec un surcoût annoncé de 30 à 50 % en Île-de-France et grandes métropoles — ce qui conforte l'abattement appliqué ici.
Bases nationales retenues : PER **8 / 12 / 15 € HT**, multicouche **12 / 18 / 28 € HT**, cuivre **20 / 32 / 50 € HT**. Fourniture 30 % (PER, multicouche) et 40 % (cuivre, matière chère). Abattement −8 % sur la main-d'œuvre = **−5,6 %** (PER, multicouche) et **−4,8 %** (cuivre) sur le total.
**Matériaux seuls, sourcés en distributeur** : PER Ø16 gainé bleu, couronne 100 m = **72,90 €**, soit **0,73 €/ml** ; multicouche nu Ø16 couronne 100 m à partir de **88,80 €** (0,89 €/ml), jusqu'à **193,00 € HT** (1,93 €/ml) ; version gainée 100 m à **307,00 € HT**. *Cuivre : prix au ml matériau non obtenu — **non trouvé, à confirmer**.*
**Point d'attention pour le scénario auto-rénovation** : l'écart entre 0,73 €/ml de tube et 12 €/ml fourni-posé n'est **pas** de la marge d'artisan. Ce sont les **raccords** (à sertir, à glissement), les collecteurs/nourrices, les fourreaux, les fixations et le temps de pose. Ne jamais chiffrer une auto-rénovation plomberie sur le seul prix du tube — c'est l'erreur classique.
*Réserve P-02 : la borne haute publiée à 100 €/ml correspond à de gros diamètres ou du réseau enterré, hors sujet ici. Confiance abaissée à **faible** faute d'une fourchette propre au Ø16–20 en habitation.*
Sources : [travaux.com — installation nouvelle tuyauterie](https://www.travaux.com/plomberie/guide-des-prix/prix-de-linstallation-dune-nouvelle-tuyauterie) · [tafsquare.com — prix pose de canalisation](https://www.tafsquare.com/fr/guides-de-prix/prix-pose-de-canalisation/) · [conseils.hellopro.fr — combien coûte un tuyau](https://conseils.hellopro.fr/combien-coute-un-tuyau-1732.html) · [travauxbricolage.fr — tuyauterie multicouche](https://www.travauxbricolage.fr/travaux-interieurs/plomberie/renovation-plomberie-prix-de-pose-dune-nouvelle-tuyauterie-multicouche/) · [discount-plomberie.com — tube multicouche nu Ø16 100 m](https://discount-plomberie.com/tube-et-raccords-multicouche-o16/1497-tube-multicouche-nu-16-8019495413136.html) · [plomberie-pro.com — prix du tuyau multicouche](https://www.plomberie-pro.com/conseils/plomberie/prix-du-tuyau-multicouche-comment-est-il-calcule) · [cedeo.fr — tubes multicouche nus](https://www.cedeo.fr/c/tubes-multicouche-nus/x4snv4_dig_2028098R7)

**P-04 / P-04b — Évacuations PVC.** Relevé : pose d'évacuation PVC **Ø100 ou Ø110 : 50–100 €/ml fourniture comprise** ; pose de canalisation 50–200 €/ml selon travaux ; en rénovation avec dépose, remise en état et raccords, le total monte à **120–180 €/ml** (voir P-11). Base nationale **45 / 70 / 100 € HT**, fourniture 30 %, abattement = **−5,6 %**.
*P-04b : **non trouvé, à confirmer par devis.** Aucune source ne distingue le petit diamètre Ø32–50 de raccordement d'appareil. Ne pas appliquer le prix du Ø100, il serait très majorant.*
Sources : [travaux.com — prix de pose d'une canalisation](https://www.travaux.com/plomberie/guide-des-prix/prix-de-pose-dune-canalisation) · [prix-pose.com — plomberie maison](https://www.prix-pose.com/plomberie-maison) · [btobjob.com — prix plomberie 2026, tableau complet](https://btobjob.com/blog/prix-plomberie-2026-tarifs-plombier-tableau-complet-des-travaux) · [renovationettravaux.fr — pose ou remplacement de canalisations](https://www.renovationettravaux.fr/prix-pose-remplacement-canalisation-tarifs-devis)

**P-05 — Point d'eau.** Relevé : création d'une arrivée d'eau ou d'une évacuation **90–300 € HT, fournitures et pose comprises** ; installation d'un évier ou lavabo 140–280 € ; alimentation lave-linge/lave-vaisselle par auto-perceur 90–100 €. Base nationale **100 / 200 / 300 € HT**, fourniture 30 %, abattement = **−5,6 %**.
*Sur ce bien précis, viser le haut de fourchette : arrivées coupées, murs pierre, réseau à recréer intégralement. Le bas de fourchette suppose un piquage court sur un réseau vivant, ce qui n'est pas la situation.*
Sources : [prix-travaux-m2.com — prix d'une arrivée ou évacuation d'eau](https://www.prix-travaux-m2.com/prix-arrivee-eau.php) · [monplombier.pro — tarif raccordement](https://monplombier.pro/tarif-raccordement/) · [travauxbricolage.fr — prix création arrivée et évacuation](https://www.travauxbricolage.fr/travaux-interieurs/plomberie/prix-creation-arrivee-et-evacuation/) · [travaux.com — raccordement plomberie évier de cuisine](https://www.travaux.com/plomberie/jobs/raccordement-plomberie-evier-cuisine)

**P-06 / P-06b — Salle de bain complète.** Relevé : **900–2 000 €/m² pose incluse** (estimations nationales), **1 000–3 000 €/m² TTC** selon taille, matériaux et ampleur ; pour une SDB standard de 5 m² : **4 500–10 000 € TTC** en rénovation complète, déclinée en entrée de gamme 4 500–6 000 €, milieu 6 000–8 000 €, haut 8 000–10 000 € ; fourchette large nationale 5 000–15 000 € TTC, et 3 500–25 000 € sur la source la plus étalée.
Ces valeurs étant **explicitement TTC**, elles ont été ramenées en HT à 10 % : gamme fonctionnelle 4 500–6 000 TTC → 4 090–5 455 HT ; gamme haute 8 000–15 000 TTC → 7 270–13 640 HT. Bases retenues : **P-06 4 000 / 5 200 / 6 500 € HT**, **P-06b 7 300 / 10 000 / 13 500 € HT**. Fourniture 45 % (équipements + carrelage), abattement = **−4,4 %**.
*Ligne tous corps d'état : elle inclut plomberie, faïence/carrelage, électricité de la pièce et évacuation. **Ne pas la cumuler avec P-05, P-07 et P-08 pour la même pièce** — double compte assuré.*
Sources : [lamaisonsaintgobain.fr — prix d'une salle de bain](https://www.lamaisonsaintgobain.fr/salles-de-bain/conseils/renovation-de-la-salle-de-bain/prix-d-une-salle-de-bain) · [hektorservices.com — prix salle de bain 2026, chiffres réels](https://hektorservices.com/blog/prix-salle-de-bain-2026-chiffres-reels) · [needhelp.com — prix rénovation salle de bain](https://www.needhelp.com/content/article/prix-renovation-salle-de-bain) · [lecoinrenov.fr — prix rénovation salle de bain 2026](https://lecoinrenov.fr/guide-prix/prix-renovation-salle-de-bain) · [wizzimmo.fr — prix rénovation salle de bain 2026](https://wizzimmo.fr/prix-renovation-salle-de-bain-2026/)

**P-07 / P-08 — WC.** Relevé : remplacement d'un **WC au sol : 150–400 €** matériel et main-d'œuvre compris. **WC suspendu : 400–1 300 €** matériel et pose, resserré à **550–1 300 €** en 2026 ; pack bâti-support autoportant + cuvette + chasse économique **200–600 €** ; **bâti-support seul 150–400 €** ; pose par un plombier **200–400 € en neuf, 200–700 € en rénovation**. Bases nationales : P-07 **150 / 260 / 400 € HT** (fourniture 40 %, abattement −4,8 %), P-08 **550 / 850 / 1 300 € HT** (fourniture 45 %, abattement −4,4 %). Matériaux seuls P-08 sourcés directement : **250–700 € TTC** (pack 200–600 € + habillage/plaque).
*P-07 est un prix de **remplacement sur attentes existantes**. Ici les réseaux sont coupés : ajouter P-05 et les ml de P-01/P-04.*
Sources : [prix-pose.com — WC suspendu](https://www.prix-pose.com/wc-suspendu) · [travaux.com — prix d'un WC suspendu](https://www.travaux.com/salles-de-bain-sanitaires/guide-des-prix/prix-dun-wc-suspendu) · [btobjob.com — remplacement WC, tarif plombier](https://btobjob.com/blog/prix-remplacement-wc-tarif-plombier-et-cout-pour-changer-des-toilettes) · [prix-travaux-m2.com — prix WC suspendus et pose](https://www.prix-travaux-m2.com/prix-wc-suspendu.php) · [plomberie-chauffage.info — WC suspendu pose comprise](https://www.plomberie-chauffage.info/prix-wc-suspendu-pose-comprise-le-budget-a-prevoir/)

**P-09 — Cuisine.** **Aucune source ne donne un forfait « plomberie cuisine » clé en main.** La ligne est une **somme de composants sourcés séparément** : raccordement évier 140–280 €, alimentation lave-vaisselle par auto-perceur 90–100 €, création d'arrivée ou d'évacuation 90–300 € HT. Somme cohérente : **320 / 500 / 700 € HT, hors ml de réseau** (à ajouter via P-01/P-02 et P-04). Fourniture 30 %, abattement = **−5,6 %**. **Confiance faible, méthode de construction assumée et signalée. À confirmer par devis.**
Sources : [travaux.com — raccordement plomberie évier de cuisine](https://www.travaux.com/plomberie/jobs/raccordement-plomberie-evier-cuisine) · [monplombier.pro — coût installer et raccorder un lavabo](https://monplombier.pro/cout-installer-raccorder-lavabo/) · [prix-travaux-m2.com — arrivée / évacuation d'eau](https://www.prix-travaux-m2.com/prix-arrivee-eau.php) · [lamaisonsaintgobain.fr — tarif plombier](https://www.lamaisonsaintgobain.fr/guides-travaux/plomberie-sanitaire/tarif-plombier-et-prix-des-travaux-de-plomberie)

**P-10 — Ballon d'eau chaude électrique.** Relevé : **équipement seul 200 L : 778–1 716 € TTC** ; ballon 200 L stéatite Atlantic ou Thermor **600–900 €** ; remplacement complet 200 L **700–1 800 € tout compris** (dépose, fourniture, pose) ; remplacement à l'identique **650–1 450 € pose et dépose comprises** ; **la pose ajoute 300–500 €** selon complexité et accessibilité du local technique. Valeurs à dominante TTC → HT à 10 % : 682 / 1 045 / 1 636. Base retenue **680 / 1 050 / 1 650 € HT**, fourniture 60 % (l'appareil domine), abattement −8 % sur les 40 % de pose = **−3,2 % sur le total**. Matériaux seuls sourcés directement : **600–1 716 € TTC** selon résistance (blindée ou stéatite) et marque.
**TVA : 10 %, pas 5,5 %.** Un chauffe-eau électrique à accumulation classique n'est pas un équipement d'amélioration de la performance énergétique éligible au taux réduit. Un **chauffe-eau thermodynamique** le serait — arbitrage à porter au lot 04 avec `reno-aides`, l'écart de TVA et l'éligibilité MaPrimeRénov' peuvent renverser la comparaison.
*Ici il s'agit d'une **création**, pas d'un remplacement : prévoir en plus le support ou trépied si pas de mur porteur disponible, et le circuit électrique dédié (voir E-07b). Ces postes ne sont pas dans la fourchette.*
Sources : [hellowatt.fr — prix chauffe-eau électrique](https://www.hellowatt.fr/chauffe-eau/electrique/prix) · [tarifartisan.fr — prix installation chauffe-eau](https://www.tarifartisan.fr/prix-installation-chauffe-eau/) · [renovationettravaux.fr — cumulus 200 L, prix](https://www.renovationettravaux.fr/cumulus-200l-prix-choix) · [thermor.fr — prix d'un chauffe-eau électrique](https://www.thermor.fr/nos-conseils/quel-est-le-prix-d-un-chauffe-eau-electrique) · [prix-pose.com — chauffe-eau électrique](https://www.prix-pose.com/chauffe-eau-electrique)

**P-11 / P-11b — Dépose de l'ancien réseau plomb / galvanisé.** Contexte sourcé : **environ 60 % des maisons françaises construites avant 1970 ont une plomberie en plomb ou en acier galvanisé à renouveler.** Le plomb est **interdit depuis 1995** en installation neuve et son remplacement est recommandé sans délai pour raison sanitaire ; l'acier galvanisé se corrode de l'intérieur (durée de vie 30–50 ans), réduit le débit et relargue des particules de rouille.
Le chiffre disponible est un **prix total** : en rénovation, dépose des canalisations existantes, démolition et remise en état des surfaces portent le coût à **120–180 €/ml**. Base nationale **110 / 145 / 180 € HT**, fourniture 20 %, abattement = **−6,4 %**.
*P-11b : **non trouvé, à confirmer par devis.** Aucune source n'isole le prix de la dépose seule. La déduire par soustraction serait une interpolation — non faite.*
*À vérifier sur place avant tout chiffrage : la présence effective de plomb ou de galvanisé. Le **DDT du notaire ne le dit pas** — le CREP porte sur les peintures au plomb, pas sur les canalisations. Contrôle visuel au compteur et sous évier, ou analyse d'eau.*
Sources : [renovbox.fr — prix rénovation plomberie 2026](https://renovbox.fr/prix/plomberie/renovation-plomberie/) · [travauxbtp.fr — guide rénovation plomberie maison](https://www.travauxbtp.fr/guides/guide-renovation-plomberie-maison) · [monplombier.pro — tarif remplacement tuyauterie](https://monplombier.pro/tarif-remplacement-tuyauterie/) · [travaux.com — réparation de canalisation](https://www.travaux.com/plomberie/guide-des-prix/prix-de-reparation-dune-canalisation)

### Repères de contrôle et main-d'œuvre — Lot 02

Ratios globaux relevés, à n'utiliser que pour **vérifier la cohérence** d'un chiffrage détaillé, jamais pour chiffrer :
- Plomberie complète : **50–110 €/m² HT** fournitures et pose, ou **60–130 €/m²**, ou 50–150 €/m² selon complexité.
- Maison de 100 m² : **3 000–8 000 € TTC** pour la seule tuyauterie (EF, ECS, évacuation), **8 000–20 000 € TTC** pour une rénovation plomberie complète avec dépose, réseaux neufs et raccordements sanitaires, **4 000–10 000 €** selon une troisième source.
- Canalisations encastrées en dalle ou mur béton : les saignées et rebouchages pèsent **20 à 40 % du devis total**.
- Taux horaire plombier : **40–90 € HT/h**, dont **40–60 €/h en province moyenne** contre 60–90 €/h en Île-de-France et grandes métropoles ; autres relevés 35–70 €/h et 45–80 €/h. C'est ce différentiel province/IdF qui fonde l'abattement.

Sources : [prix-travaux-m2.com — plomberie au m²](https://www.prix-travaux-m2.com/prix-plomberie-m2.php) · [renovbox.fr — rénovation plomberie 2026](https://renovbox.fr/prix/plomberie/renovation-plomberie/) · [travaux.com — prix d'une rénovation de plomberie](https://www.travaux.com/plomberie/guide-des-prix/prix-dune-renovation-de-plomberie) · [btobjob.com — prix plombier 2026](https://btobjob.com/blog/prix-plomberie-2026-tarifs-plombier-tableau-complet-des-travaux) · [needhelp.com — grille tarifaire plomberie](https://www.needhelp.com/content/article/grille-tarifaire-plomberie) · [thermocom.fr — tarif plombier 2026](https://thermocom.fr/tarif-plombier/)

### Rappel TVA — les deux lots

Sources : [entreprendre.service-public.gouv.fr — taux de TVA travaux de rénovation](https://entreprendre.service-public.gouv.fr/vosdroits/F23568?lang=fr) · [constructia.fr — TVA rénovation 5,5 ou 10 %, guide 2026](https://www.constructia.fr/blog/tva-renovation-5-5-ou-10-pourcent-guide-2026) · [manay.fr — TVA travaux 2026](https://www.manay.fr/blog/artisan/tva-travaux-10-ou-20/) · [france-artisan.fr — TVA réduite 2026](https://www.france-artisan.fr/tva-reduite) — consultées le 10/08/2026.

**Le piège du scénario C (auto-rénovation) :** les colonnes « matériaux seuls » sont à **TVA 20 %**, contre 10 % en entreprise. Sur une ligne où la fourniture pèse 45 %, l'écart de TVA mange à lui seul près de 5 % de l'économie de main-d'œuvre. À ne pas oublier dans la comparaison B/C/D. S'y ajoutent la perte des aides conditionnées à un professionnel RGE, et le fait qu'une installation électrique auto-réalisée passe au Consuel **avec visite systématique**.

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

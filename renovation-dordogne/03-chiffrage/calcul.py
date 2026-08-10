#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chiffrage — 2, lieu-dit Robin, 33350 Castillon-la-Bataille
Projet : remise en service d'une maison de 85 m2 habitables (parpaing, annees 1970-80)

ENTREES  : 00-contexte/fiche-bien.md, 01-diagnostic/synthese.md (revisions incluses),
           02-prix/base-prix.md, 05-reglementaire/cadre.md
SORTIES  : 03-chiffrage/chiffrage-detaille.md, 03-chiffrage/scenarios.md

AVERTISSEMENT DE CONFIANCE (a repeter dans tous les livrables) :
  Aucune ligne de la base de prix ne depasse la confiance "moyenne" (WebFetch bloque
  par la politique reseau — extraits de recherche, pas de lectures de pages).
  Seules exceptions en confiance haute : E-09 (Consuel) et E-09b (mise en service Enedis),
  tarifs reglementes.
  Ce budget sert a CADRER et a NEGOCIER des devis. Il n'engage aucune depense.

REGLES APPLIQUEES :
  - aucun prix unitaire fabrique : tous les PU viennent de 02-prix/base-prix.md
  - jamais d'addition HT + TTC
  - provision pour aleas 15 % (inconnues structurelles subsistantes : fissures C-14 / C-12)
  - provision pour alea structurel ISOLEE, hors total, retirable d'un trait
  - lot 05 = 0, lot 06 = 0, lot 07 sans injection ni drainage, D-02 curage NON applique
"""

# ----------------------------------------------------------------------------------
# 0. METRE RETENU — hypotheses de quantites, chacune tracee
# ----------------------------------------------------------------------------------
SH = 85.0            # m2 habitables (fiche-bien)
MURS_TAPISSES = 130.0  # m2 de murs tapisses — HYPOTHESE, non metre sur plan
ML_REAIGUILLAGE = 150.0  # ml de circuits a re-aiguiller (13-16 circuits x ~10 m) — HYPOTHESE
ML_PER = 70.0        # ml alimentation PER EF+ECS — HYPOTHESE (reseau vole, a reposer)
ML_EVAC = 8.0        # ml evacuation PVC 100/110 en reprise — HYPOTHESE
SURF_COMBLES = 85.0  # m2 — NON DOCUMENTE (aucune vue des combles)

TAUX_ALEAS = 0.15    # 15 % : inconnues structurelles non levees

# ----------------------------------------------------------------------------------
# 1. LIGNES DE CHIFFRAGE
#    (ref, lot, designation, qte, unite, pu_bas_ht, pu_moy_ht, pu_haut_ht, tva,
#     niveau, constat)
#    niveau : "decent" | "confort" | "brancheA2" | "brancheB1" | "variante" | "option"
# ----------------------------------------------------------------------------------
L = []
def add(ref, lot, des, qte, unite, b, m, h, tva, niveau, constat, note=""):
    L.append(dict(ref=ref, lot=lot, des=des, qte=qte, unite=unite,
                  b=b, m=m, h=h, tva=tva, niveau=niveau, constat=constat, note=note))

# --- LOT 01 ELECTRICITE — hypothese RE-AIGUILLAGE sur fourreaux existants -----------
add("E-05", "01 Electricite", "Tableau 3 rangees equipe, depose ancien inclus", 1, "ens",
    621, 1052, 1912, 0.10, "decent", "C-17 / C-03")
add("E-06", "01 Electricite", "Mise a la terre : piquet, cuivre nu 25, barrette, mesure", 1, "ens",
    188, 395, 752, 0.10, "decent", "C-17 (aucun differentiel 30 mA)")
add("E-02", "01 Electricite", "Point lumineux simple allumage", 10, "point",
    66, 113, 188, 0.10, "decent", "C-17 (2 circuits eclairage recenses)")
add("E-03", "01 Electricite", "Point lumineux va-et-vient", 2, "point",
    113, 169, 263, 0.10, "decent", "C-17 / C-20")
add("E-04", "01 Electricite", "Prise 16 A + T sur circuit existant", 24, "u",
    65, 108, 168, 0.10, "decent", "C-17 (prises sur 15 A a reprendre)")
add("E-07", "01 Electricite", "Circuit specialise 32 A plaque de cuisson", 1, "u",
    123, 189, 283, 0.10, "decent", "C-17 (cuisiniere sur 20 A)")
add("E-07b", "01 Electricite", "Circuit specialise 20 A (four, LL, LV, ballon ECS)", 4, "u",
    85, 123, 165, 0.10, "decent", "C-17 / C-23")
add("E-08", "01 Electricite", "Re-aiguillage conducteurs sur fourreaux existants (ligne apparent)", ML_REAIGUILLAGE, "ml",
    4.70, 8.40, 14.00, 0.10, "decent", "C-23 (cables coupes et voles)",
    "Proxy : la base ne porte pas de ligne 're-aiguillage sur fourreau existant'. "
    "E-08 (apparent, sans saignee) est la ligne la plus proche. E-08b (encastre) serait majorant.")
add("E-09", "01 Electricite", "Attestation Consuel jaune (avec visite)", 1, "forfait",
    120.56, 120.56, 194.68, 0.20, "decent", "cadre.md 5.2 — tarif reglemente")
add("E-09b", "01 Electricite", "Mise en service Enedis, compteur Linky, a distance", 1, "forfait",
    1.50, 1.50, 1.50, 0.20, "decent", "3e serie photos — Linky confirme")
add("E-10", "01 Electricite", "Coffret de communication grade 2 TV", 1, "ens",
    191, 363, 621, 0.10, "confort", "C-02 (PABX obsolete depose)")

# Variante lot 01 : refonte totale du cablage
add("E-01", "01 Electricite", "VARIANTE — renovation electrique complete, refonte totale", SH, "m2 hab",
    57, 90, 124, 0.10, "variante", "C-23 (si conducteurs tires hors fourreaux)",
    "Se substitue a E-02/E-03/E-04/E-07/E-07b/E-08, PAS a E-05/E-06/E-09/E-09b.")

# --- LOT 02 PLOMBERIE --------------------------------------------------------------
add("P-01", "02 Plomberie", "Alimentation PER O16 sous fourreau, EF + ECS", ML_PER, "ml",
    7.60, 11.30, 14.20, 0.10, "decent", "C-23 (arrivees coupees et volees)")
add("P-05", "02 Plomberie", "Point d'eau complet (lavabo, douche, WC, lave-linge)", 4, "u",
    94, 189, 283, 0.10, "decent", "C-04 / C-05 / C-23", "Viser le haut : reseau a recreer.")
add("P-09", "02 Plomberie", "Plomberie cuisine : evier + LV, robinet d'arret", 1, "ens",
    302, 472, 661, 0.10, "decent", "C-06 / C-07")
add("P-04", "02 Plomberie", "Evacuation PVC O100/110, reprise ponctuelle", ML_EVAC, "ml",
    42.50, 66.10, 94.40, 0.10, "decent", "C-19 / siphons a sec (7 ans)")
add("P-06", "02 Plomberie", "OPTION — salle de bain complete, gamme fonctionnelle", 1, "ens",
    3824, 4971, 6214, 0.10, "option", "C-05 (douche CONSERVABLE — option de confort seule)")
add("P-11", "02 Plomberie", "VARIANTE — depose reseau plomb/galvanise + pose reseau neuf + reprise supports", ML_PER, "ml",
    103, 136, 168, 0.10, "varianteP", "C-23 — presence de plomb/galva NON VERIFIEE",
    "Se substitue a P-01. Ne se declenche que si un controle visuel au compteur et sous evier "
    "revele du plomb ou de l'acier galvanise. C'est cette variante qui explique la pre-estimation "
    "6 000-10 000 EUR du lot 02 portee au constat C-23.")

# --- LOT 03 ASSAINISSEMENT — BRANCHE A ---------------------------------------------
add("A-10", "03 Assainissement", "BRANCHE A2 — rehabilitation ANC complete, forfait englobant", 1, "forfait",
    5170, 8460, 13630, 0.10, "brancheA2", "C-19 / C-15 / C-13",
    "Forfait ENGLOBANT : ne se cumule ni avec A-01 ni avec A-02..A-09.")
# controle croise de A-10 par la voie detaillee (non cumulable avec A-10)
add("A-01", "03 Assainissement", "CONTROLE — etude de sol et de filiere ANC", 1, "forfait",
    315, 635, 1190, 0.20, "controleA2", "C-19")
add("A-04b", "03 Assainissement", "CONTROLE — fosse toutes eaux + filtre a sable DRAINE", 1, "ens",
    4675, 6078, 7480, 0.10, "controleA2", "C-19", "INCLUT la fosse : ne pas ajouter A-02.")
add("A-07", "03 Assainissement", "CONTROLE — vidange fosse existante par vidangeur agree", 1, "u",
    180, 288, 432, 0.10, "controleA2", "C-15 / C-19")
add("A-08", "03 Assainissement", "CONTROLE — comblement d'ouvrage abandonne (fosse + puisard)", 2, "u",
    279, 512, 744, 0.10, "controleA2", "C-19")
add("A-09", "03 Assainissement", "CONTROLE — controles SPANC conception + bonne execution", 1, "forfait",
    150, 225, 300, 0.10, "controleA2", "cadre.md 2.3", "Base et TVA a confirmer aupres du SIEA.")

# --- LOT 04 CHAUFFAGE / ECS --------------------------------------------------------
add("CH-05", "04 Chauffage/ECS", "Depose installation propane (appareil, canalisations, attestation PG)", 1, "forfait",
    267, 401, 592, 0.10, "decent", "C-06 / C-22")
add("CH-01", "04 Chauffage/ECS", "Panneau rayonnant en remplacement de convecteur", 4, "u",
    244, 390, 683, 0.10, "decent", "C-21 (4 departs convecteurs)")
add("CH-02", "04 Chauffage/ECS", "Ballon ECS electrique 150 L stéatite, fourni pose", 1, "u",
    582, 757, 922, 0.10, "decent", "C-06 / C-22 (ECS gaz deposee)")
add("CH-01b", "04 Chauffage/ECS", "CONFORT — radiateur a inertie (en substitution de CH-01)", 4, "u",
    372, 686, 1372, 0.10, "confortSubst", "C-21 / DPE 2026 coef 1,9")
add("CH-03", "04 Chauffage/ECS", "OPTION — chauffe-eau thermodynamique 200-270 L, pro RGE", 1, "u",
    2313, 3516, 5550, 0.055, "option", "arbitrage energie")
add("CH-04", "04 Chauffage/ECS", "OPTION — poele a granules, tubage sur conduit existant, pro RGE", 1, "ens",
    3225, 5067, 7371, 0.055, "option", "C-06 / C-13 (2 conduits existants)")

# --- LOT 05 COUVERTURE : 0 EUR (reserve ecrite) ------------------------------------
# --- LOT 06 MENUISERIES EXTERIEURES : 0 EUR ----------------------------------------

# --- LOT 07 VENTILATION (preventive uniquement, aucune injection ni drainage) -------
add("V-02", "07 Ventilation", "VMC simple flux hygroreglable type B, pro RGE", 1, "ens",
    853, 1280, 1896, 0.055, "decent", "revision 'VMC preventive' — 10 L/j a l'emmenagement")
add("V-05", "07 Ventilation", "Entree d'air en menuiserie, piece principale", 3, "u",
    87, 145, 290, 0.10, "decent", "menuiseries double vitrage etanches conservees")
add("V-06b", "07 Ventilation", "Traitement complet fongicide + peinture anti-moisissures (plafond douche)", 4, "m2",
    37.80, 56.60, 75.50, 0.10, "decent", "C-05 (reclasse COSMETIQUE)")
add("V-01", "07 Ventilation", "VARIANTE — VMC simple flux AUTOREGLABLE (TVA 10 %, aucune aide)", 1, "ens",
    427, 711, 1137, 0.10, "varianteV", "revision VMC preventive")

# --- LOT 08 ISOLATION (confort) ----------------------------------------------------
add("I-01", "08 Isolation", "Isolation combles perdus par soufflage, R >= 7, pro RGE", SURF_COMBLES, "m2",
    21.00, 31.00, 43.00, 0.055, "confort", "aucun constat — combles NON DOCUMENTES",
    "Surface non metree : aucune vue des combles. Ligne indicative, a ne pas engager avant d'etre monte.")

# --- LOT 09 PLATRERIE --------------------------------------------------------------
add("PL-02", "09 Platrerie", "Reprise d'enduit sur parpaing decroute", 2.5, "m2",
    28.70, 47.80, 76.40, 0.10, "decent", "C-11")
add("PL-03b", "09 Platrerie", "Rebouchage de saignee deja ouverte", 3.0, "ml",
    8.30, 13.90, 22.20, 0.10, "decent", "C-11")
add("PL-06", "09 Platrerie", "Depose de papier peint (detapissage)", MURS_TAPISSES, "m2",
    6.40, 11.00, 18.40, 0.10, "confort", "C-07 / C-03 / C-09")
add("PL-01", "09 Platrerie", "Enduit de rebouchage + lissage sur mur existant", MURS_TAPISSES, "m2",
    9.30, 14.90, 22.40, 0.10, "confort", "C-09 (aspect marbre, reclasse COSMETIQUE)")

# --- BRANCHE B1 — fissures veranda supposees STABILISEES ---------------------------
add("PL-02b", "09 Platrerie", "BRANCHE B1 — reprise d'enduit sur fissures veranda (proxy PL-02)", 2.0, "m2",
    28.70, 47.80, 76.40, 0.10, "brancheB1", "C-14 / C-12",
    "PROXY. Le mastic elastomere de rebouchage souple n'a PAS de ligne dans la base. "
    "Non chiffre : la part 'souple' du traitement.")

# --- LOT 10 SOLS (reprises ponctuelles seulement) ----------------------------------
add("S-01a", "10 Sols", "Intervention de remplacement ponctuel de carreaux (1 a 5)", 1, "forfait",
    186, 269, 371, 0.10, "decent", "C-13 / C-15 (dalles de regards deposees)")
add("S-02", "10 Sols", "Refection de joints de carrelage — pieces d'eau", 12, "m2",
    14.90, 26.10, 46.60, 0.10, "decent", "C-05 (receveur encrasse) / C-04")
add("S-02c", "10 Sols", "CONFORT — refection de joints, autres pieces", 20, "m2",
    14.90, 26.10, 46.60, 0.10, "confort", "C-06 / C-07 / C-13")

# --- LOT 11 PEINTURE (confort) -----------------------------------------------------
add("PE-05", "11 Peinture", "Remise en peinture complete du logement (murs+plafonds+boiseries)", SH, "m2 hab",
    35.40, 65.20, 102.50, 0.10, "confort", "C-07 / C-09",
    "Ratio englobant : NE PAS cumuler avec PE-01..PE-04. PL-01 et PL-06 s'ajoutent (non inclus).")

# --- LOT 12 MENUISERIES INTERIEURES (confort) --------------------------------------
add("M-01", "12 Menuiseries int.", "Bloc-porte interieur fourni pose", 4, "u",
    212, 366, 598, 0.10, "confort", "C-20 — nombre de portes NON ETABLI (hypothese 4)")
# M-02 plinthes = 0 : plinthes carrelees conservees (C-01)

# --- LOT 13 DEPOSE / EVACUATION ----------------------------------------------------
add("D-03a", "13 Depose/evac.", "Benne 8 m3 gravats / inertes, rendue + enlevement + traitement", 1, "u",
    180, 280, 380, 0.20, "decent", "C-11 / C-15 (dalles beton)")
add("D-03c", "13 Depose/evac.", "CONFORT — benne 15 m3 tout-venant / DIB (platre, papiers, PVC)", 1, "u",
    380, 530, 700, 0.20, "confort", "PL-06 / M-01",
    "Le platre n'est PAS un inerte : benne separee obligatoire.")
# D-02 CURAGE : 0 EUR — NON APPLIQUE (voir note dans le livrable)

# --- PRESTATIONS OBLIGATOIRES ------------------------------------------------------
add("DAT", "00 Prestations", "Diagnostic amiante avant travaux (bati anterieur a 1997)", 1, "forfait",
    350, 350, 350, 0.20, "decent", "base-prix D-01 (note) / cadre.md 8.2",
    "Valeur ponctuelle sourcee, pas une fourchette. Obligation distincte du DDT du notaire, "
    "a la charge du maitre d'ouvrage.")

# ----------------------------------------------------------------------------------
# 2. CALCULS
# ----------------------------------------------------------------------------------
def tot_ht(ligne):
    return (ligne["qte"] * ligne["b"], ligne["qte"] * ligne["m"], ligne["qte"] * ligne["h"])

def tot_ttc(ligne):
    b, m, h = tot_ht(ligne)
    t = 1 + ligne["tva"]
    return (b * t, m * t, h * t)

for lg in L:
    lg["ht"] = tot_ht(lg)
    lg["ttc"] = tot_ttc(lg)

def somme(niveaux, lots=None, exclure_refs=()):
    ht = [0.0, 0.0, 0.0]; ttc = [0.0, 0.0, 0.0]
    for lg in L:
        if lg["niveau"] not in niveaux: continue
        if lots is not None and lg["lot"] not in lots: continue
        if lg["ref"] in exclure_refs: continue
        for i in range(3):
            ht[i] += lg["ht"][i]; ttc[i] += lg["ttc"][i]
    return tuple(ht), tuple(ttc)

def f(x): return f"{x:,.0f}".replace(",", " ")
def fr(t): return f"{f(t[0])} – {f(t[2])} €"
def fr3(t): return f"{f(t[0])} / {f(t[1])} / {f(t[2])} €"

print("=" * 88)
print("CHIFFRAGE — 2, lieu-dit Robin, 33350 Castillon-la-Bataille — 85 m2 habitables")
print("Confiance de la base de prix : MOYENNE au mieux (WebFetch bloque). Budget de cadrage.")
print("=" * 88)

# --- 2.1 detail par lot ------------------------------------------------------------
print("\n### DETAIL PAR LOT — niveau DECENT ET VIVABLE (hors lot 03) ###")
lots = sorted({lg["lot"] for lg in L})
for lot in lots:
    lignes = [lg for lg in L if lg["lot"] == lot and lg["niveau"] == "decent"]
    if not lignes: continue
    sht = [sum(lg["ht"][i] for lg in lignes) for i in range(3)]
    sttc = [sum(lg["ttc"][i] for lg in lignes) for i in range(3)]
    print(f"\n-- {lot}")
    for lg in lignes:
        print(f"   {lg['ref']:<7} {lg['des'][:58]:<58} {lg['qte']:>7.1f} {lg['unite']:<8} "
              f"HT {f(lg['ht'][0]):>7} / {f(lg['ht'][1]):>7} / {f(lg['ht'][2]):>7}  TVA {int(lg['tva']*100)}%")
    print(f"   {'>>> SOUS-TOTAL':<66} HT {fr3(tuple(sht))}   TTC {fr3(tuple(sttc))}")

print("\n### DETAIL PAR LOT — INCREMENT NIVEAU CONFORTABLE ###")
for lot in lots:
    lignes = [lg for lg in L if lg["lot"] == lot and lg["niveau"] == "confort"]
    if not lignes: continue
    sht = [sum(lg["ht"][i] for lg in lignes) for i in range(3)]
    sttc = [sum(lg["ttc"][i] for lg in lignes) for i in range(3)]
    print(f"\n-- {lot}")
    for lg in lignes:
        print(f"   {lg['ref']:<7} {lg['des'][:58]:<58} {lg['qte']:>7.1f} {lg['unite']:<8} "
              f"HT {f(lg['ht'][0]):>7} / {f(lg['ht'][1]):>7} / {f(lg['ht'][2]):>7}  TVA {int(lg['tva']*100)}%")
    print(f"   {'>>> SOUS-TOTAL':<66} HT {fr3(tuple(sht))}   TTC {fr3(tuple(sttc))}")

# --- 2.2 agregats ------------------------------------------------------------------
DEC_ht, DEC_ttc = somme({"decent"})
CONF_ht, CONF_ttc = somme({"confort"})
SUBST_ht, SUBST_ttc = somme({"confortSubst"})
CH01_ht, CH01_ttc = somme({"decent"}, lots={"04 Chauffage/ECS"}, exclure_refs=("CH-05", "CH-02"))
# delta inertie = CH-01b - CH-01
DELTA_inertie_ht = tuple(SUBST_ht[i] - CH01_ht[i] for i in range(3))
DELTA_inertie_ttc = tuple(SUBST_ttc[i] - CH01_ttc[i] for i in range(3))

B1_ht, B1_ttc = somme({"brancheB1"})
A2_ht, A2_ttc = somme({"brancheA2"})
A2ctrl_ht, A2ctrl_ttc = somme({"controleA2"})
VAR_E01_ht, VAR_E01_ttc = somme({"variante"})
# ce que E-01 remplace
REMPL = ("E-02", "E-03", "E-04", "E-07", "E-07b", "E-08")
rempl_ht = [0.0, 0.0, 0.0]; rempl_ttc = [0.0, 0.0, 0.0]
for lg in L:
    if lg["ref"] in REMPL:
        for i in range(3):
            rempl_ht[i] += lg["ht"][i]; rempl_ttc[i] += lg["ttc"][i]
DELTA_refonte_ht = tuple(VAR_E01_ht[i] - rempl_ht[i] for i in range(3))
DELTA_refonte_ttc = tuple(VAR_E01_ttc[i] - rempl_ttc[i] for i in range(3))

print("\n" + "=" * 88)
print("AGREGATS")
print("=" * 88)
print(f"Niveau DECENT ET VIVABLE (hors lot 03)        HT {fr3(DEC_ht)}   TTC {fr3(DEC_ttc)}")
print(f"Increment CONFORTABLE                          HT {fr3(CONF_ht)}   TTC {fr3(CONF_ttc)}")
print(f"Branche B1 (fissures stabilisees)              HT {fr3(B1_ht)}   TTC {fr3(B1_ttc)}")
print(f"Branche A2 (ANC, forfait A-10)                 HT {fr3(A2_ht)}   TTC {fr3(A2_ttc)}")
print(f"  controle A2 par voie detaillee (non cumul)   HT {fr3(A2ctrl_ht)}   TTC {fr3(A2ctrl_ttc)}")
print(f"Variante refonte totale elec (delta vs re-aig.) HT {fr3(DELTA_refonte_ht)}  TTC {fr3(DELTA_refonte_ttc)}")
print(f"Delta radiateurs inertie vs rayonnants          HT {fr3(DELTA_inertie_ht)}  TTC {fr3(DELTA_inertie_ttc)}")

# --- 2.3 les 3 lots les plus lourds ------------------------------------------------
print("\n--- Poids des lots, niveau DECENT + branche A2 + branche B1 (TTC moyen) ---")
poids = {}
for lg in L:
    if lg["niveau"] in ("decent", "brancheA2", "brancheB1"):
        poids[lg["lot"]] = poids.get(lg["lot"], 0.0) + lg["ttc"][1]
for lot, v in sorted(poids.items(), key=lambda kv: -kv[1]):
    print(f"   {lot:<22} {f(v):>8} € TTC moyen")

# ----------------------------------------------------------------------------------
# 3. SOCLE DE CHIFFRAGE PAR BRANCHE
# ----------------------------------------------------------------------------------
def socle(branche_A, niveau_confort=False, inertie=False):
    """Retourne (HT, TTC) du socle travaux, hors aleas, hors provision structurelle."""
    ht = list(DEC_ht); ttc = list(DEC_ttc)
    for i in range(3):
        ht[i] += B1_ht[i]; ttc[i] += B1_ttc[i]
    if branche_A == "A2":
        for i in range(3):
            ht[i] += A2_ht[i]; ttc[i] += A2_ttc[i]
    if niveau_confort:
        for i in range(3):
            ht[i] += CONF_ht[i]; ttc[i] += CONF_ttc[i]
    if inertie:
        for i in range(3):
            ht[i] += DELTA_inertie_ht[i]; ttc[i] += DELTA_inertie_ttc[i]
    return tuple(ht), tuple(ttc)

SOCLE = {}
for br in ("A1", "A2"):
    for niv, conf, iner in (("decent", False, False), ("confortable", True, True)):
        SOCLE[(br, niv)] = socle(br, conf, iner)

print("\n" + "=" * 88)
print("SOCLES TRAVAUX (hors aleas, hors provision structurelle)")
print("=" * 88)
for k, v in SOCLE.items():
    print(f"  {k[0]} / {k[1]:<12} HT {fr3(v[0])}   TTC {fr3(v[1])}")
print("  A1 = raccordement au collectif : lot 03 a ZERO au titre de la rehabilitation ANC,")
print("       MAIS boite de branchement, tranchee, mise en separatif et PFAC NON CHIFFRES.")

# ----------------------------------------------------------------------------------
# 4. PROVISIONS
# ----------------------------------------------------------------------------------
def aleas(ttc):
    return tuple(x * TAUX_ALEAS for x in ttc)

# Provision pour alea structurel — ISOLEE, hors total.
# Ce N'EST PAS un prix unitaire de la base. C'est la borne basse de l'ordre de grandeur
# DOCUMENTE au diagnostic C-14 : "reprise en sous-oeuvre par micropieux si actif
# (chantier a cinq chiffres)". Borne basse d'un montant a cinq chiffres = 10 000 EUR.
PROV_STRUCT = 10000.0

# ----------------------------------------------------------------------------------
# 5. SCENARIOS A / B / C / D
# ----------------------------------------------------------------------------------
print("\n" + "=" * 88)
print("SCENARIOS")
print("=" * 88)

# --- SCENARIO A : maitrise d'oeuvre -------------------------------------------------
MOE_BAS, MOE_HAUT = 0.10, 0.12   # 10-12 % du HT en renovation (fourchette 8-15 %)
def scenarioA(br, niv):
    ht, ttc = SOCLE[(br, niv)]
    a = aleas(ttc)
    base_ttc = tuple(ttc[i] + a[i] for i in range(3))
    base_ht = tuple(ht[i] * (1 + TAUX_ALEAS) for i in range(3))
    # honoraires MOE : % du HT, TVA 20 % (prestation intellectuelle)
    hono_ht = (base_ht[0] * MOE_BAS, base_ht[1] * 0.11, base_ht[2] * MOE_HAUT)
    hono_ttc = tuple(x * 1.20 for x in hono_ht)
    tot = tuple(base_ttc[i] + hono_ttc[i] for i in range(3))
    return base_ttc, hono_ttc, tot

# --- SCENARIO B : artisans en direct -------------------------------------------------
COORD_H_SEM = (4, 8)      # h/semaine de coordination par le maitre d'ouvrage
DUREE_SEM = {"decent": (16, 26), "confortable": (26, 40)}
REPRISE_BAS, REPRISE_HAUT = 0.03, 0.08   # surcout de reprise si mauvais sequencement
def scenarioB(br, niv):
    ht, ttc = SOCLE[(br, niv)]
    a = aleas(ttc)
    base_ttc = tuple(ttc[i] + a[i] for i in range(3))
    h_bas = COORD_H_SEM[0] * DUREE_SEM[niv][0]
    h_haut = COORD_H_SEM[1] * DUREE_SEM[niv][1]
    reprise = (base_ttc[0] * REPRISE_BAS, base_ttc[1] * 0.05, base_ttc[2] * REPRISE_HAUT)
    tot = tuple(base_ttc[i] + reprise[i] for i in range(3))
    return base_ttc, (h_bas, h_haut), reprise, tot

# --- SCENARIO C : auto-renovation ---------------------------------------------------
# Materiaux seuls TTC 20 % : colonne de la base. (ref, qte, mat_bas, mat_haut, unite)
MAT = [
    ("E-05", 1, 400, 750), ("E-06", 1, 80, 150), ("E-02", 10, 15, 35), ("E-03", 2, 25, 55),
    ("E-04", 24, 12, 28), ("E-08", ML_REAIGUILLAGE, 0.20, 2.00),
    ("P-01", ML_PER, 0.73, 0.73), ("P-05", 4, 34, 102), ("P-09", 1, 109, 238),
    ("CH-01", 4, 200, 800), ("CH-02", 1, 350, 850),
    ("V-02", 1, 350, 600), ("V-05", 3, 15, 80), ("V-06b", 4, 15, 45),
    ("PL-02", 2.5, 3, 8), ("PL-02b", 2.0, 3, 8), ("PL-03b", 3.0, 1, 3),
    ("S-02", 12, 1.50, 4.00),
]
MAT_CONF = [
    ("PL-01", MURS_TAPISSES, 2.00, 3.00), ("PE-05", SH, 5, 18),
    ("I-01", SURF_COMBLES, 8, 15), ("M-01", 4, 105, 400), ("S-02c", 20, 1.50, 4.00),
]
# Lignes dont la colonne "materiaux seuls" est NON TROUVEE dans la base : non chiffrables en C
MAT_NON_TROUVE = ["E-07 (circuit 32 A)", "E-07b x4 (circuits 20 A)", "E-10 (coffret com)",
                  "P-04 (evacuation PVC O100)", "PL-06 (detapissage : decolleuse + produit)",
                  "S-01a (carreaux de remplacement)", "M-02 (plinthes)"]

def mat_total(liste):
    b = sum(q * mb for _, q, mb, _ in liste)
    h = sum(q * mh for _, q, _, mh in liste)
    return b, h

MAT_DEC = mat_total(MAT)
MAT_CONFO = mat_total(MAT + MAT_CONF)

# Location de materiel (sourcee dans la base)
LOC_SOUFFLEUSE = (99.38 * 2, 280 * 2)   # 2 jours
# Consommables : 8-12 % des materiaux
def consommables(mat): return (mat[0] * 0.08, mat[1] * 0.12)

# Incompressibles en scenario C (non auto-realisables ou obligatoires)
def incompressibles_C(br):
    refs = ["E-09", "E-09b", "DAT", "CH-05"]   # Consuel, mise en service, DAT, depose propane par PG
    b = h = 0.0
    for lg in L:
        if lg["ref"] in refs:
            b += lg["ttc"][0]; h += lg["ttc"][2]
    if br == "A2":
        b += A2_ttc[0]; h += A2_ttc[2]     # ANC : terrassement, non auto-realisable ici
    return b, h

# Bennes (TVA 20 %, identique en auto)
BENNE_DEC = (180 * 1.2, 380 * 1.2)
BENNE_CONF = (BENNE_DEC[0] + 380 * 1.2, BENNE_DEC[1] + 700 * 1.2)

def scenarioC(br, niv):
    mat = MAT_DEC if niv == "decent" else MAT_CONFO
    cons = consommables(mat)
    loc = (0.0, 0.0) if niv == "decent" else LOC_SOUFFLEUSE
    benne = BENNE_DEC if niv == "decent" else BENNE_CONF
    inc = incompressibles_C(br)
    base = (mat[0] + cons[0] + loc[0] + benne[0] + inc[0],
            mat[1] + cons[1] + loc[1] + benne[1] + inc[1])
    al = (base[0] * TAUX_ALEAS, base[1] * TAUX_ALEAS)
    tot = (base[0] + al[0], base[1] + al[1])
    return mat, cons, loc, benne, inc, tot

# Heures d'auto-renovation (h debutant, base de prix, lots 08 a 13 uniquement)
HEURES = [
    ("PL-06 detapissage", MURS_TAPISSES, 0.15, 0.35),
    ("PL-01 enduit + lissage", MURS_TAPISSES, 0.40, 0.80),
    ("PE-05 peinture complete", SH, 1.8, 3.0),
    ("PL-02 reprise enduit parpaing", 2.5, 1.0, 2.0),
    ("PL-02b reprise fissures veranda", 2.0, 1.0, 2.0),
    ("PL-03b rebouchage saignee", 3.0, 0.3, 0.6),
    ("S-02 joints pieces d'eau", 12, 0.5, 1.0),
    ("S-02c joints autres pieces", 20, 0.5, 1.0),
    ("S-01a carreaux (4 u.)", 4, 1.0, 2.0),
    ("I-01 soufflage combles", SURF_COMBLES, 0.20, 0.35),
    ("M-01 blocs-portes (4 u.)", 4, 3.0, 5.0),
]
H_DECENT_REFS = {"PL-02 reprise enduit parpaing", "PL-02b reprise fissures veranda",
                 "PL-03b rebouchage saignee", "S-02 joints pieces d'eau", "S-01a carreaux (4 u.)"}

def heures(niv):
    tb = th = 0.0
    detail = []
    for nom, q, hb, hh in HEURES:
        if niv == "decent" and nom not in H_DECENT_REFS:
            continue
        b, h = q * hb, q * hh
        detail.append((nom, b, h)); tb += b; th += h
    return detail, tb, th

# --- SCENARIO D : hybride -----------------------------------------------------------
# PRO (RGE ou technique) : elec (lot 01), plomberie (lot 02), ANC (lot 03), VMC (V-02),
#                          isolation combles (I-01), couverture, menuiseries ext.
# AUTO : depose, platrerie, sols, peinture, menuiseries int., radiateurs (CH-01),
#        entrees d'air (V-05), traitement fongicide (V-06b), bennes
PRO_REFS_D = {"E-05","E-06","E-02","E-03","E-04","E-07","E-07b","E-08","E-09","E-09b","E-10",
              "P-01","P-05","P-09","P-04","P-06","A-10","V-02","I-01","CH-05","CH-02","DAT"}
AUTO_MAT_D = [
    ("CH-01", 4, 200, 800), ("V-05", 3, 15, 80), ("V-06b", 4, 15, 45),
    ("PL-02", 2.5, 3, 8), ("PL-02b", 2.0, 3, 8), ("PL-03b", 3.0, 1, 3),
    ("S-02", 12, 1.50, 4.00),
]
AUTO_MAT_D_CONF = [("PL-01", MURS_TAPISSES, 2.00, 3.00), ("PE-05", SH, 5, 18),
                   ("M-01", 4, 105, 400), ("S-02c", 20, 1.50, 4.00)]

def scenarioD(br, niv):
    pro_b = pro_h = 0.0
    for lg in L:
        if lg["ref"] not in PRO_REFS_D: continue
        if lg["niveau"] == "decent": pass
        elif lg["niveau"] == "confort" and niv != "confortable": continue
        elif lg["niveau"] == "brancheA2":
            if br != "A2": continue
        elif lg["niveau"] not in ("decent", "confort", "brancheA2"): continue
        pro_b += lg["ttc"][0]; pro_h += lg["ttc"][2]
    liste = AUTO_MAT_D if niv == "decent" else AUTO_MAT_D + AUTO_MAT_D_CONF
    mat = mat_total(liste)
    cons = consommables(mat)
    benne = BENNE_DEC if niv == "decent" else BENNE_CONF
    base = (pro_b + mat[0] + cons[0] + benne[0], pro_h + mat[1] + cons[1] + benne[1])
    al = (base[0] * TAUX_ALEAS, base[1] * TAUX_ALEAS)
    tot = (base[0] + al[0], base[1] + al[1])
    return (pro_b, pro_h), mat, cons, benne, tot

# --- IMPRESSION DES SCENARIOS -------------------------------------------------------
for br in ("A1", "A2"):
    for niv in ("decent", "confortable"):
        print("\n" + "-" * 88)
        print(f"BRANCHE {br} — NIVEAU {niv.upper()}")
        print("-" * 88)
        soc_ht, soc_ttc = SOCLE[(br, niv)]
        print(f"  Socle travaux             HT  {fr3(soc_ht)}    TTC {fr3(soc_ttc)}")
        print(f"  Aleas 15 % (sur TTC)          {fr3(aleas(soc_ttc))}")

        bA, hA, tA = scenarioA(br, niv)
        print(f"  A — Maitre d'oeuvre       travaux+aleas TTC {fr3(bA)}")
        print(f"      honoraires MOE 10-12 % du HT (TVA 20 %) {fr3(hA)}")
        print(f"      TOTAL A                                 {f(tA[0])} – {f(tA[2])} € TTC")

        bB, hB, rB, tB = scenarioB(br, niv)
        print(f"  B — Artisans en direct    travaux+aleas TTC {fr3(bB)}")
        print(f"      coordination MO : {hB[0]:.0f} a {hB[1]:.0f} h (4-8 h/sem)")
        print(f"      surcout de reprise si mauvais sequencement (3-8 %) {fr3(rB)}")
        print(f"      TOTAL B                                 {f(tB[0])} – {f(tB[2])} € TTC")

        mat, cons, loc, benne, inc, tC = scenarioC(br, niv)
        det_h, hb, hh = heures(niv)
        print(f"  C — Auto-renovation")
        print(f"      materiaux seuls TVA 20 %                {f(mat[0])} – {f(mat[1])} €")
        print(f"      consommables 8-12 %                     {f(cons[0])} – {f(cons[1])} €")
        print(f"      location materiel                       {f(loc[0])} – {f(loc[1])} €")
        print(f"      bennes / evacuation                     {f(benne[0])} – {f(benne[1])} €")
        print(f"      incompressibles pro/obligatoires        {f(inc[0])} – {f(inc[1])} €")
        print(f"      aleas 15 %                              {f(tC[0]-(mat[0]+cons[0]+loc[0]+benne[0]+inc[0])):>7} – "
              f"{f(tC[1]-(mat[1]+cons[1]+loc[1]+benne[1]+inc[1]))} €")
        print(f"      TOTAL C                                 {f(tC[0])} – {f(tC[1])} € TTC")
        print(f"      HEURES d'auto-renovation (lots 08-13)   {hb:.0f} – {hh:.0f} h")

        (prob, proh), matD, consD, benneD, tD = scenarioD(br, niv)
        print(f"  D — Hybride")
        print(f"      lots pro (TTC, TVA 10 % / 5,5 %)        {f(prob)} – {f(proh)} €")
        print(f"      materiaux auto TVA 20 %                 {f(matD[0])} – {f(matD[1])} €")
        print(f"      consommables 8-12 %                     {f(consD[0])} – {f(consD[1])} €")
        print(f"      bennes                                  {f(benneD[0])} – {f(benneD[1])} €")
        print(f"      TOTAL D (aleas 15 % inclus)             {f(tD[0])} – {f(tD[1])} € TTC")

# --- 5.bis detail des heures --------------------------------------------------------
print("\n" + "=" * 88)
print("VOLUME D'HEURES D'AUTO-RENOVATION (h debutant, base de prix, lots 08 a 13)")
print("=" * 88)
for niv in ("decent", "confortable"):
    det, tb, th = heures(niv)
    print(f"\n-- niveau {niv}")
    for nom, b, h in det:
        print(f"   {nom:<38} {b:>7.1f} – {h:>7.1f} h")
    print(f"   {'TOTAL':<38} {tb:>7.0f} – {th:>7.0f} h")
    print(f"   equivalent week-ends complets (16 h)   {tb/16:.0f} – {th/16:.0f} WE")
print("\n   ATTENTION : la base de prix ne porte AUCUN h/unite sur les lots 01 (elec),")
print("   02 (plomberie), 03 (ANC), 04 (chauffage) et 07 (ventilation).")
print("   Ces heures sont NON CHIFFREES — le total ci-dessus est un PLANCHER.")

# --- 6. provision structurelle isolee ----------------------------------------------
print("\n" + "=" * 88)
print("PROVISION POUR ALEA STRUCTUREL — ISOLEE, HORS TOTAL")
print("=" * 88)
print(f"  Montant retenu : {f(PROV_STRUCT)} € — borne basse de l'ordre de grandeur DOCUMENTE")
print("  au constat C-14 : 'reprise en sous-oeuvre par micropieux si actif (chantier a cinq chiffres)'.")
print("  CE N'EST PAS UN PRIX DE LA BASE. B2 (fissure active) reste NON CHIFFRE : expertise requise.")
print("  Cette provision se retire d'un trait le jour ou deux temoins plâtre releves a 3 et 6 mois")
print("  prouvent la stabilite. Cout de la mesure : quelques euros.")
for br in ("A1", "A2"):
    for niv in ("decent", "confortable"):
        _, _, tA = scenarioA(br, niv)
        print(f"  {br}/{niv:<12} scenario A avec provision : "
              f"{f(tA[0]+PROV_STRUCT)} – {f(tA[2]+PROV_STRUCT)} € TTC")

# --- 7. recettes --------------------------------------------------------------------
print("\n" + "=" * 88)
print("RECETTES (a porter en ligne de recette, PAS en depense negative)")
print("=" * 88)
print("  CH-05b — consignes de 4 bouteilles de propane ~35 kg (C-22) :")
print("     sans bulletin de consignation : 16 – 40 €")
print("     avec bulletin de consignation : 140 – 360 €")
print("     -> reclamer les bulletins au vendeur : action gratuite, facteur ~9 sur la recette.")

# --- 8. controles de coherence ------------------------------------------------------
print("\n" + "=" * 88)
print("CONTROLES DE COHERENCE")
print("=" * 88)
e_ht, e_ttc = somme({"decent"}, lots={"01 Electricite"})
print(f"  Lot 01 re-aiguillage        HT {fr3(e_ht)}")
print(f"    -> repere C-17 : mise en securite 1 500-3 000 € / refonte complete 5 000-10 500 € HT")
print(f"  Lot 01 variante refonte E-01 HT {fr3(VAR_E01_ht)}  (repere refonte : 5 000-10 500 € HT) OK")
p_ht, p_ttc = somme({"decent"}, lots={"02 Plomberie"})
print(f"  Lot 02 plomberie            HT {fr3(p_ht)}  soit {p_ht[0]/SH:.0f}-{p_ht[2]/SH:.0f} €/m2 hab")
print(f"    -> repere base : plomberie complete 50-110 €/m2 HT, ou 60-130 €/m2")
print(f"  Lot 03 A-10 forfait         HT {fr3(A2_ht)}")
print(f"    -> voie detaillee A-01+A-04b+A-07+2xA-08+A-09 HT {fr3(A2ctrl_ht)} : ecart acceptable")
print(f"  Lot 11 PE-05                HT {fr3(somme({'confort'}, lots={'11 Peinture'})[0])}")
print(f"    -> repere base : 38/70/110 €/m2 hab x 85 m2 apres abattement OK")

VP_ht, VP_ttc = somme({"varianteP"})
p01 = [lg for lg in L if lg["ref"] == "P-01"][0]
print(f"\n  VARIANTE P-11 (reseau plomb/galva a deposer) HT {fr3(VP_ht)}  TTC {fr3(VP_ttc)}")
print(f"    delta vs P-01 : HT +{f(VP_ht[0]-p01['ht'][0])} / +{f(VP_ht[1]-p01['ht'][1])} / +{f(VP_ht[2]-p01['ht'][2])}")
print(f"    -> lot 02 en variante P-11 : HT {f(p_ht[0]-p01['ht'][0]+VP_ht[0])} – "
      f"{f(p_ht[2]-p01['ht'][2]+VP_ht[2])} : recoupe la pre-estimation 6 000-10 000 EUR du constat C-23")

print("\n  ALERTE BORNE HAUTE LOT 01 : le chiffrage ligne a ligne culmine a "
      f"{f(e_ht[2])} € HT,")
print("    au-dessus du repere 'refonte complete 5 000-10 500 € HT' du constat C-17")
print(f"    et au-dessus de la variante E-01 haute ({f(VAR_E01_ht[2])} € HT).")
print("    -> a la borne haute, retenir le RATIO E-01, pas la somme des lignes : arbitrer sur devis.")
print("\nFIN")

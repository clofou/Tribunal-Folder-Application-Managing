from docxtpl import DocxTemplate
from essential_functions import amount_to_text_fr, split_int

demandeur_response, demandeur_suite_motif, demandeur_adjectif, demandeur_suite = "","", "", ""
def demMascOrFem(sexe):
    global demandeur_response, requerant_explique_propr, demandeur_suite, demandeur_repr, demandeur_adjectif
    if sexe=="m":
        demandeur_response = "Demandeur"
        demandeur_adjectif = "au demandeur"
        requerant_explique_propr= "le requerant explique qu'il est propriétaire d'une concession"

        if demandeur_repr == 'r':
            a = input("Demandeur Representé par qui?:  ")
            demandeur_suite = f", representé par {a}"
        elif demandeur_repr=='d':
            b = input("Demandeur Domicilié Ou:  ")
            demandeur_suite = f", domicilié à {b}"


    elif sexe=="f":
        demandeur_response = "Demanderesse"
        demandeur_adjectif = "à la demanderesse"
        if "Agence" in demandeur_name:
            requerant_explique_propr= "la requerante explique qu'elle gère une concession"
        else:
            requerant_explique_propr= "la requerante explique qu'elle est propriétaire d'une concession"
            if demandeur_repr == 'r':
                a = input("Representée par qui?:  ")
                demandeur_suite = f", representée par {a}"
            elif demandeur_repr=='d':
                b = input("Domiciliée Ou:  ")
                demandeur_suite = f", domiciliée à {b}"

nommee, il_elle = "", ""
defendeur_response, motif_defendeur_comparution,defendeur_comparution_response, defendeur_adjectif, defendeur_suite ="","", "", "", ""
def defMascOrFem(sexe):
    global nommee, il_elle, motif_defendeur_comparution,defendeur_response, defendeur_comparution,defendeur_adjectif, defendeur_suite, defendeur_comparution_response
    if sexe=="m":
        nommee = "le nommé"
        il_elle = "il"
        defendeur_response = "Défendeur"
        defendeur_adjectif = "au défendeur"
        if defendeur_comparution == 'o':
            defendeur_comparution_response = "Le défendeur comparant"
        else:
            motif_defendeur_comparution = "\nConstatons, la non comparution du défendeur ;"
            defendeur_comparution_response = "Le défendeur non comparant"
    
    elif sexe=="f":
        nommee = "la nommée"
        il_elle = "elle"
        defendeur_response = "Demanderesse"
        defendeur_adjectif = "à la demanderesse"
        if defendeur_comparution == 'o':
            defendeur_comparution_response = "La défenderesse comparante"
        else:
            defendeur_comparution_response = "La défenderesse non comparante"
            motif_defendeur_comparution = "\nConstatons, la non comparution de la défenderesse"



loyer_mensuel_response, retard_response,somme_total_response, reliquat_response = "", "", "", ""
def buildLoyerMensuel(montant, retard_y, reliquat_y):
    global loyer_mensuel_response, retard_response, reliquat_response, somme_total_response
    montant_number = int(montant.replace(".", ""))
    res = amount_to_text_fr(montant_number)
    loyer_mensuel_response = f"{res} ({montant})"
    retard_response = f"{amount_to_text_fr(int(retard_y))} ({retard_y})"
    somme_total = montant_number*int(retard_y)
    if reliquat_y == "o":
        g = input("Somme reliquat:  ")
        g_number = int(g.replace(".", ""))
        res_y = amount_to_text_fr(g_number)
        reliquat_response = f"{res_y} ({montant}) FCFA "
        somme_total += g_number
    somme_total_response = f"{amount_to_text_fr(somme_total)} ({split_int(somme_total, '.')})"



refere_date = "08 Décembre 2022"
ord = input("ORd:  ")
rg = input("RG:  ")
rc = input("RC:  ")
demandeur = input("Demandeur Masculin ou Feminin (m/f):  ")
demandeur_name = input("Nom demandeur:  ")
demandeur_repr = input("Demandeur represente ou domicilié? (r/d):  ")
defendeur = input("Defendeur Masculin ou Feminin (m/f):  ")
defendeur_name = input("Nom defendeur:  ")
quartier = input("Quartier:  ")
date_assignement = input("Date assignement:  ")
maitre = input("Huissier commissaire:  ")
loyer_mensuel = input("Loyer mensuel de:   ")
retard = input("Un retard de :   ")
reliquat = input("Y-a t-il reliquat ? (o/n):   ")
defendeur_comparution = input("Defendeur a t-il comparu:  ")
execution_sur_minute = input("Y a t-il execution sur minute? (o/n):   ")

demMascOrFem(demandeur)
defMascOrFem(defendeur)
buildLoyerMensuel(loyer_mensuel, retard, reliquat)
demandeur_suite_motif = demandeur_suite

doc = DocxTemplate("mimi_template.docx")
context = {
    'refere_date': refere_date,
    'ord': ord,
    'rg': rg,
    'rc': rc,
    'demandeur': demandeur_response,
    'demandeur_name': demandeur_name,
    'demandeur_suite': demandeur_suite,
    'defendeur': defendeur_response,
    'defendeur_name': defendeur_name,
    'quartier': quartier,
    'date_assignement': date_assignement,
    'maitre': maitre,
    'requerant_explique_propr': requerant_explique_propr,
    'loyer_mensuel': loyer_mensuel_response,
    'retard': retard_response,
    'reliquat': reliquat_response,
    'somme_total': somme_total_response,
    'defendeur_comparution': defendeur_comparution_response,
    'execution_sur_minute': "",
    'execution_sur_minute_contenu': "",
    'motif_defendeur_comparution': motif_defendeur_comparution,
    'demandeur_suite_motif': demandeur_suite_motif,
    'demandeur_adjectif': demandeur_adjectif,
    'defendeur_adjectif': defendeur_adjectif,
    'nommee': nommee,
    'il_elle': il_elle,
}
doc.render(context)
doc.save(f"result/REFERE ORD N°{ord} Mimi -Fatim ( Expulsion simple).docx")
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from docxtpl import DocxTemplate
from essential_functions import amount_to_text_fr, split_int

class MyApp(MDApp):

    ex, executoire, delais, ex_c, nommee, il_elle = "", "", "", "", "", ""
    defendeur_adjectif, defendeur_response, motif_defendeur_comparution,defendeur_comparution_response ="","","", ""
    loyer_mensuel_response, retard_response,somme_total_response, reliquat_response, defendeur_adjectif, defendeur_suite = "", "", "", "", "", ""
    demandeur_response, demandeur_suite_motif,requerant_explique_propr, demandeur_adjectif, demandeur_suite = "","","", "", ""

    def cu1(self, instance):
        self.rc.focus = True
    def cu2(self, instance):
        self.ord.focus = True
    def cu3(self, instance):
        self.sexe_demandeur.focus = True
    def cu4(self, instance):
        self.sexe_defendeur.focus = True
    def cu5(self, instance):
        self.nom_demandeur.focus = True
    def cu6(self, instance):
        self.nom_defendeur.focus = True
    def cu7(self, instance):
        self.domicilie_a_defendeur.focus = True
    def cu8(self, instance):
        self.date_assignement.focus = True
    def cu9(self, instance):
        self.maitre.focus = True
    def cu10(self, instance):
        self.loyer_mensuel.focus = True
    def cu11(self, instance):
        self.nombre_de_Mois.focus = True
    def cu12(self, instance):
        self.comparu.focus = True
    def cu13(self, instance):
        self.execution_sur.focus = True
    def cu14(self, instance):
        self.delai.focus = True

    def build(self):
        screen = FloatLayout()
        self.error = Label(text="", color=(1,0,0))
        spinner = Spinner(
            background_color=(0, 0.6, 0.7),
            text='Dossier: mimi',
            values=('Dossier: mimi', 'Dossier: pascal', 'Dossier: nema', 'Dossier: wouri', 'Dossier: cisse'),
            size_hint=(0.3, 0.05),
            pos_hint={'center_x': .25, 'center_y': .95}
        )
        self.error.pos_hint={'center_x': 0.1,'center_y': 0.9}
        self.logo = Image(source='logo.png')
        self.logo.pos_hint={'center_x': 0.14,'center_y': 0.55}
        screen.add_widget(self.logo)
        screen.add_widget(spinner)
        # ORD SECTION
        ord_section = GridLayout()
        ord_section.cols = 2
        ord_section.pos_hint={'center_x': 0.2,'center_y': 0.8}
        ord_section.size_hint = (0.2, 0.15)
        self.ord = TextInput(multiline=False)
        self.rg = TextInput(multiline=False)
        self.rg.bind(on_text_validate=self.cu1)
        self.rc = TextInput(multiline=False)
        ord_section.add_widget(Label(text="RG: ", color=(0,0,0)))
        ord_section.add_widget(self.rg)
        ord_section.add_widget(Label(text="RC: ", color=(0,0,0)))
        ord_section.add_widget(self.rc)
        self.rc.bind(on_text_validate=self.cu2)
        ord_section.add_widget(Label(text="Ord: ", color=(0,0,0)))
        ord_section.add_widget(self.ord)
        self.ord.bind(on_text_validate=self.cu3)
        # DELIBERE SECTION
        delibere_section = GridLayout()
        delibere_section.rows = 1
        delibere_section.pos_hint={'center_x': 0.7,'center_y': 0.9}
        delibere_section.size_hint = (0.5, 0.05)
        self.delibere = TextInput(multiline=False)
        delibere_section.add_widget(Label(text="Delibéré Le : ", color=(0,0,0)))
        delibere_section.add_widget(self.delibere)
        # DEMANDEUR DEFENDEUR
        dem_def_section = GridLayout()
        dem_def_section.pos_hint={'center_x': 0.6,'center_y': 0.6}
        dem_def_section.size_hint = (0.6, 0.25)
        dem_def_section.spacing = 12
        dem_def_section.cols=4
        self.sexe_demandeur = TextInput(multiline=False)
        self.sexe_defendeur = TextInput(multiline=False)
        self.nom_demandeur = TextInput(multiline=False)
        self.nom_defendeur = TextInput(multiline=False)
        self.represente_par = TextInput(multiline=False)
        self.sexe_demandeur.bind(on_text_validate=self.cu4)
        self.sexe_defendeur.bind(on_text_validate=self.cu5)
        self.nom_demandeur.bind(on_text_validate=self.cu6)
        self.nom_defendeur.bind(on_text_validate=self.cu7)
        self.domicilie_a_demandeur = TextInput(multiline=False)
        self.domicilie_a_defendeur = TextInput(multiline=False)
        self.domicilie_a_demandeur.bind(on_text_validate=self.cu7)
        self.domicilie_a_defendeur.bind(on_text_validate=self.cu8)
        self.represente_par.bind(on_text_validate=self.cu8)
        dem_def_section.add_widget(Label(text="Demandeur M/F : ", color=(0,0,0)))
        dem_def_section.add_widget(self.sexe_demandeur)
        dem_def_section.add_widget(Label(text="Defendeur M/F : ", color=(0,0,0)))
        dem_def_section.add_widget(self.sexe_defendeur)
        dem_def_section.add_widget(Label(text="Nom Demandeur : ", color=(0,0,0)))
        dem_def_section.add_widget(self.nom_demandeur)
        dem_def_section.add_widget(Label(text="Nom Defendeur : ", color=(0,0,0)))
        dem_def_section.add_widget(self.nom_defendeur)
        dem_def_section.add_widget(Label(text="représenté par : ", color=(0,0,0)))
        dem_def_section.add_widget(self.represente_par)
        dem_def_section.add_widget(Label(text="Défendeur domicilié à : ", color=(0,0,0)))
        dem_def_section.add_widget(self.domicilie_a_defendeur)
        dem_def_section.add_widget(Label(text="Demandeur domicilié à : ", color=(0,0,0)))
        dem_def_section.add_widget(self.domicilie_a_demandeur)
        # DATE ASSIGNEMENT MAITRE
        date_assi_section = GridLayout()
        date_assi_section.rows = 1
        date_assi_section.pos_hint={'center_x': 0.45,'center_y': 0.35}
        date_assi_section.size_hint = (0.8, 0.05)
        self.date_assignement = TextInput(multiline=False)
        self.maitre = TextInput(multiline=False)
        valider = Button(text="Génerer Le Fichier", color=(0.2, 1, 0.6))
        valider.bind(on_press=self.generer)
        self.date_assignement.bind(on_text_validate=self.cu9)
        self.maitre.bind(on_text_validate=self.cu10)
        date_assi_section.add_widget(Label(text="Date d'assignement: ", color=(0,0,0)))
        date_assi_section.add_widget(self.date_assignement)
        date_assi_section.add_widget(Label(text="Nom Huissier: ", color = (0,0,0)))
        date_assi_section.add_widget(self.maitre)
        date_assi_section.add_widget(Label(text=""))
        date_assi_section.add_widget(valider)
        # LOYER MENSUEL ET RELIQUAT
        loyer_section = GridLayout()
        loyer_section.cols = 2
        loyer_section.pos_hint={'center_x': 0.2,'center_y': 0.15}
        loyer_section.size_hint = (0.3, 0.15)
        self.loyer_mensuel = TextInput(multiline=False)
        self.nombre_de_Mois = TextInput(multiline=False)
        self.reliquat = TextInput(multiline=False)
        self.loyer_mensuel.bind(on_text_validate=self.cu11)
        self.nombre_de_Mois.bind(on_text_validate=self.cu12)
        loyer_section.add_widget(Label(text="Loyer Mensuel: ", color=(0,0,0)))
        loyer_section.add_widget(self.loyer_mensuel)
        loyer_section.add_widget(Label(text="Nombre de mois: ", color=(0,0,0)))
        loyer_section.add_widget(self.nombre_de_Mois)
        loyer_section.add_widget(Label(text="Reliquat: ", color=(0,0,0)))
        loyer_section.add_widget(self.reliquat)
        self.reliquat.bind(on_text_validate=self.cu12)
        # LOYER MENSUEL ET RELIQUAT
        reste_section = GridLayout()
        reste_section.cols = 2
        reste_section.pos_hint={'center_x': 0.7,'center_y': 0.15}
        reste_section.size_hint = (0.4, 0.15)
        self.comparu = TextInput(multiline=False)
        self.execution_sur = TextInput(multiline=False)
        self.delai = TextInput(multiline=False)
        self.comparu.bind(on_text_validate=self.cu13)
        self.execution_sur.bind(on_text_validate=self.cu14)
        reste_section.add_widget(Label(text="Defendeur comparu ? (o/n): ", color=(0,0,0)))
        reste_section.add_widget(self.comparu)
        reste_section.add_widget(Label(text="Execution Sur Minute ? (o/n) ", color=(0,0,0)))
        reste_section.add_widget(self.execution_sur)
        reste_section.add_widget(Label(text="Lui Donnons Un délai de : ", color=(0,0,0)))
        reste_section.add_widget(self.delai)

        
        screen.add_widget(ord_section)
        screen.add_widget(delibere_section)
        screen.add_widget(dem_def_section)
        screen.add_widget(date_assi_section)
        screen.add_widget(loyer_section)
        screen.add_widget(reste_section)
        screen.add_widget(self.error)
        return screen

    

    def demMascOrFem(self):
        if self.sexe_demandeur.text=="m":
            self.demandeur_response = "Demandeur"
            self.demandeur_adjectif = "au demandeur"
            self.requerant_explique_propr= "le requerant explique qu'il est propriétaire d'une concession"

            if self.represente_par.text != "":
                self.demandeur_suite = f", representé par {self.represente_par.text}"
            elif self.domicilie_a_demandeur.text!='':
                self.demandeur_suite = f", domicilié à {self.domicilie_a_demandeur.text}"
            if(self.execution_sur.text == 'o'):
                self.ex = "\nSur l'exécution sur minute avant enregistrement :"
                self.executoire = "\nDisons que cette décision est exécutoire sur minute ;"
                self.ex_c = """\nAu sens des dispositions de l'article 495 alinéa 3 du décret N°99-254/PRM du 13 Septembre 1999, portant code de procédure civile, commerciale et sociale, le juge peut ordonner, en cas de nécessité, que l'exécution aura lieu au seul vu de la minute et avant enregistrement.
Dans le cas de l'espèce, le requérant a sollicité qu'il plaise au tribunal, d'assortir la décision à intervenir d'une mesure d'exécution sur minute avant enregistrement ;
En l'espèce, s'agissant d'une exécution illégalement entamée, laquelle risque d'avoir des conséquences dommageables pour le requérant, si elle n'est pas arrêtée à temps, il est d'une extrême urgence que la présente ordonnance soit immédiatement exécutoire, afin de prévenir tout autre dommage imminent pouvant résulter de la continuation de ladite exécution ;
Dès lors, l'exécution de la présente ordonnance sur minute avant enregistrement, qui semble nécessaire et compatible avec la nature de l'affaire dont s'agit mérite ordonnée ;
"""

        elif self.sexe_demandeur.text=="f":
            self.demandeur_response = "Demanderesse"
            self.demandeur_adjectif = "à la demanderesse"
            if "Agence" in self.nom_demandeur.text:
                self.requerant_explique_propr= "la requerante explique qu'elle gère une concession"
            else:
                self.requerant_explique_propr= "la requerante explique qu'elle est propriétaire d'une concession"
                if self.represente_par.text != '':
                    self.demandeur_suite = f", representée par {self.represente_par.text}"
                elif self.domicilie_a_demandeur.text!='':
                    self.demandeur_suite = f", domiciliée à {self.domicilie_a_demandeur.text}"
            if(self.execution_sur.text == 'o'):
                self.ex = "\nSur l'exécution sur minute avant enregistrement :"
                self.executoire = "\nDisons que cette décision est exécutoire sur minute ;"
                self.ex_c = """\nAu sens des dispositions de l'article 495 alinéa 3 du décret N°99-254/PRM du 13 Septembre 1999, portant code de procédure civile, commerciale et sociale, le juge peut ordonner, en cas de nécessité, que l'exécution aura lieu au seul vu de la minute et avant enregistrement.
Dans le cas de l'espèce, la requérante a sollicité qu'il plaise au tribunal, d'assortir la décision à intervenir d'une mesure d'exécution sur minute avant enregistrement ;
En l'espèce, s'agissant d'une exécution illégalement entamée, laquelle risque d'avoir des conséquences dommageables pour la requérante, si elle n'est pas arrêtée à temps, il est d'une extrême urgence que la présente ordonnance soit immédiatement exécutoire, afin de prévenir tout autre dommage imminent pouvant résulter de la continuation de ladite exécution ;
Dès lors, l'exécution de la présente ordonnance sur minute avant enregistrement, qui semble nécessaire et compatible avec la nature de l'affaire dont s'agit mérite ordonnée ;
"""

    def defMascOrFem(self):
        if self.sexe_defendeur.text=="m":
            self.nommee = "le nommé"
            self.il_elle = "il"
            self.defendeur_response = "Défendeur"
            self.defendeur_adjectif = "du défendeur"
            if self.comparu.text == 'o':
                self.defendeur_comparution_response = "Le défendeur comparant"
            else:
                self.motif_defendeur_comparution = "\nConstatons, la non comparution du défendeur ;"
                self.defendeur_comparution_response = "Le défendeur non comparant"
        
        elif self.sexe_defendeur.text=="f":
            self.nommee = "la nommée"
            self.il_elle = "elle"
            self.defendeur_response = "Défenderesse"
            self.defendeur_adjectif = "de la défenderesse"
            if self.comparu.text == 'o':
                self.defendeur_comparution_response = "La défenderesse comparante"
            else:
                self.defendeur_comparution_response = "La défenderesse non comparante"
                self.motif_defendeur_comparution = "\nConstatons, la non comparution de la défenderesse ;"

    def buildLoyerMensuel(self,montant, retard_y):
        if montant != "" and retard_y != "":
            montant_number = int(montant)
            self.retard_response = f"{amount_to_text_fr(int(retard_y))} ({retard_y})"

        res = amount_to_text_fr(montant_number)
        self.loyer_mensuel_response = f"{res} ({split_int(montant, '.')})"
        somme_total = montant_number*int(retard_y)
        if self.reliquat.text != "":
            g_number = int(self.reliquat.text)
            res_y = amount_to_text_fr(g_number)
            self.reliquat_response = f"plus un reliquat de {res_y} ({split_int(self.reliquat.text, '.')}) FCFA "
            somme_total += g_number
        self.somme_total_response = f"{amount_to_text_fr(somme_total)} ({split_int(somme_total, '.')})"
        if self.delai.text != "":
            self.delais = f"\nLui accordons un délai de {amount_to_text_fr(int(self.delai.text))} ({self.delai.text}) mois pour vider les lieux ;"

    def generer(self, instance):
        if self.ord.text != "" and self.rg.text != "" and self.rc.text != "" and self.delibere.text != "" and self.sexe_demandeur.text != "" and self.sexe_defendeur.text != "" and self.nom_demandeur.text != "" and self.nom_defendeur.text != "" and self.domicilie_a_defendeur.text != "" and self.date_assignement.text != "" and self.maitre.text != "" and self.loyer_mensuel.text != "" and self.comparu.text != '' and self.execution_sur.text != '' :
            self.demMascOrFem()
            self.defMascOrFem()
            self.buildLoyerMensuel(self.loyer_mensuel.text, self.nombre_de_Mois.text)
            demandeur_suite_motif = self.demandeur_suite


            doc = DocxTemplate("mimi_template.docx")
            context = {
                'refere_date': self.delibere.text,
                'ord': self.ord.text,
                'rg': self.rg.text,
                'rc': self.rc.text,
                'demandeur': self.demandeur_response,
                'demandeur_name': self.nom_demandeur.text,
                'demandeur_suite': self.demandeur_suite,
                'defendeur': self.defendeur_response,
                'defendeur_name': self.nom_defendeur.text,
                'quartier': self.domicilie_a_defendeur.text,
                'date_assignement': self.date_assignement.text,
                'maitre': self.maitre.text,
                'requerant_explique_propr': self.requerant_explique_propr,
                'loyer_mensuel': self.loyer_mensuel_response,
                'retard': self.retard_response,
                'reliquat': self.reliquat_response,
                'somme_total': self.somme_total_response,
                'defendeur_comparution': self.defendeur_comparution_response,
                'execution_sur_minute': self.ex,
                'execution_sur_minute_contenu': self.ex_c,
                'motif_defendeur_comparution': self.motif_defendeur_comparution,
                'demandeur_suite_motif': demandeur_suite_motif,
                'demandeur_adjectif': self.demandeur_adjectif,
                'defendeur_adjectif': self.defendeur_adjectif,
                'nommee': self.nommee,
                'executoire': self.executoire,
                'delai': self.delais,
                'il_elle': self.il_elle,
            }
            doc.render(context)
            
            doc.save(f"mimi-Fatim/REFERE ORD N°{self.ord.text} Mimi -Fatim ( Expulsion simple).docx")
            self.ord.text = "" ; self.rg.text = "" ; self.rc.text = "" ; self.nom_demandeur.text = "" ; self.nom_defendeur.text = ""   ; self.loyer_mensuel.text = ""
            self.error.text, self.ex, self.ex_c, self.delais, self.reliquat_response, self.executoire = "", "", "", "", "", ""
            self.retard_response, self.defendeur_response, self.demandeur_response, self.somme_total_response, self.loyer_mensuel_response, self.defendeur_comparution_response = "","","","","",""
        else:
            self.error.text = "Erreur"

######################################################################
######################################################################
##############  PROGRAMME PRINCIPAL  #################################

if __name__=="__main__":
    MyApp().run()
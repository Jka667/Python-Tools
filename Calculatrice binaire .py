import tkinter as tk

entry1 = None
entry2 = None
entry3 = None
entry4 = None
entryCote = None
entryDecalage = None
complement2_entry = None
result_label = None

def is_binary(value):
    return all(bit == '0' or bit == '1' for bit in value)

def validate_binary_input(entry, label_text):
    value = entry.get()
    if not is_binary(value):
        result_label.config(text=f"Erreur: {label_text} doit contenir seulement des 0 ou 1.")
        return False
    return True

def aligner_bits(binaire1, binaire2):
    longueur_max = max(len(binaire1), len(binaire2))
    binaire1 = binaire1.zfill(longueur_max)
    binaire2 = binaire2.zfill(longueur_max)
    return binaire1, binaire2

def BinaireEnDecimal(binaire):
    decimal = 0

    if not is_binary(binaire):
        result_label.config(text="Erreur: Le nombre binaire doit contenir seulement des 0 ou 1.")
        return

    for i in range(len(binaire)):
        bit = int(binaire[i])
        puissance_deux = 2 ** (len(binaire) - 1 - i)
        decimal += bit * puissance_deux

    return decimal

def DecimalEnBinaire(nombre):
    binaire = ""
    while nombre > 0:
        reste = nombre % 2
        binaire = str(reste) + binaire
        nombre = nombre // 2
    return binaire if binaire else '0'

def somme():
    if not validate_binary_input(entry1, "Nombre binaire 1") or not validate_binary_input(entry2, "Nombre binaire 2"):
        return

    binaire1 = entry1.get()
    binaire2 = entry2.get()

    decimal1 = BinaireEnDecimal(binaire1)
    decimal2 = BinaireEnDecimal(binaire2)

    somme = decimal1 + decimal2
    somme_binaire = DecimalEnBinaire(somme)

    result_label.config(text=f"La somme de ces nombres en binaire est: {somme_binaire}")

def soustraction():
    if not validate_binary_input(entry1, "Nombre binaire 1") or not validate_binary_input(entry2, "Nombre binaire 2"):
        return

    binaire1 = entry1.get()
    binaire2 = entry2.get()

    decimal1 = BinaireEnDecimal(binaire1)
    decimal2 = BinaireEnDecimal(binaire2)

    if decimal1 >= decimal2:
        difference = decimal1 - decimal2
        result_label.config(text=f"La soustraction de ces nombres en binaire est: {DecimalEnBinaire(difference)}")
    else:
        difference = decimal2 - decimal1
        result_label.config(text=f"La soustraction de ces nombres en binaire est: {DecimalEnBinaire(difference)}")

def multiplication():
    if not validate_binary_input(entry1, "Nombre binaire 1") or not validate_binary_input(entry2, "Nombre binaire 2"):
        return

    binaire1 = entry1.get()
    binaire2 = entry2.get()
    binaire1, binaire2 = aligner_bits(binaire1, binaire2)
    decimal1 = BinaireEnDecimal(binaire1)
    decimal2 = BinaireEnDecimal(binaire2)
    produit = decimal1 * decimal2
    produit_binaire = DecimalEnBinaire(produit)
    result_label.config(text=f"Le produit de ces nombres en binaire est: {produit_binaire}")

def division():
    if not validate_binary_input(entry1, "Nombre binaire 1") or not validate_binary_input(entry2, "Nombre binaire 2"):
        return

    binaire1 = entry1.get()
    binaire2 = entry2.get()
    binaire1, binaire2 = aligner_bits(binaire1, binaire2)

    decimal1 = BinaireEnDecimal(binaire1)
    decimal2 = BinaireEnDecimal(binaire2)

    if decimal2 != 0:
        quotient = decimal1 // decimal2
        quotient_binaire = DecimalEnBinaire(quotient)
        result_label.config(text=f"Le quotient de ces nombres en binaire est: {quotient_binaire}")
    elif decimal2 > decimal1:
        quotient = decimal2 // decimal1
        result_label.config(text=f"Le quotient de ces nombres en binaire est: {DecimalEnBinaire(quotient)}")
    else:
        result_label.config(text="Erreur: Division par zéro.")

def decalage():
    if not validate_binary_input(entry1, "Nombre binaire 1"):
        return

    cote = entryCote.get()

    if cote not in ["G", "D"]:
        result_label.config(text="Veuillez choisir un côté valide G pour gauche D pour droite.")
        return

    decal = int(entry2.get())
    NoAdecaler = entryDecalage.get()

    if not is_binary(NoAdecaler):
        result_label.config(text="Erreur: Le nombre binaire doit contenir seulement des 0 ou 1.")
        return

    if cote == "G":
        flip = NoAdecaler.ljust(len(NoAdecaler) + decal, '0')
        decimal = BinaireEnDecimal(flip)
        result_label.config(text=f"Le nombre décalé à gauche en décimal est: {decimal} et en binaire: {flip}")
    elif cote == "D":
        flip = NoAdecaler.rjust(len(NoAdecaler) + decal, '0')
        flip = flip[:len(NoAdecaler)]
        decimal = BinaireEnDecimal(flip)
        result_label.config(text=f"Le nombre décalé à droite en décimal est: {decimal} et en binaire: {flip}")
    else:
        result_label.config(text="Veuillez choisir un côté valide (G pour gauche, D pour droite).")

def ET(binaire1, binaire2):
    if not validate_binary_input(entry3, "Nombre binaire 1 opération logique") or not validate_binary_input(entry4, "Nombre binaire 2 opération logique"):
        return

    resultat = ""
    binaire1, binaire2 = aligner_bits(binaire1, binaire2)
    for bit1, bit2 in zip(binaire1, binaire2):
        resultat += str(int(bit1) and int(bit2))
    result_label.config(text=f"Le résultat de l'opération ET logique est: {resultat}")

def OU(binaire1, binaire2):
    if not validate_binary_input(entry3, "Nombre binaire 1 opération logique") or not validate_binary_input(entry4, "Nombre binaire 2 opération logique"):
        return

    binaire1, binaire2 = aligner_bits(binaire1, binaire2)
    resultat = ""
    for bit1, bit2 in zip(binaire1, binaire2):
        resultat += str(int(bit1) or int(bit2))
    result_label.config(text=f"Le résultat de l'opération OU logique est: {resultat}")
    return resultat

def NON(binaire):
    if not validate_binary_input(entry3, "Nombre binaire opération logique!"):
        return

    resultat = ""
    for bit in binaire:
        resultat += str(int(not int(bit)))
    result_label.config(text=f"Le résultat de l'opération NON logique est: {resultat}")
    return resultat

def Complement2(binaire):
    if not validate_binary_input(complement2_entry, "Nombre binaire pour Complément à 2!"):
        return

    negation = NON(binaire)
    un = "1" + "0" * (len(binaire) - 1)
    addition = DecimalEnBinaire(BinaireEnDecimal(negation) + BinaireEnDecimal(un))
    result_label.config(text=f"Le résultat du COMPLÉMENT À 2 est: {addition}")
    return addition

def create_ui():
    global result_label
    global entry1, entry2, entry3, entry4, entryCote, complement2_entry,entryDecalage

    root = tk.Tk()
    root.title("Calculatrice binaire")

    elements_info = [
        ("Nombre binaire 1:", tk.Entry(root)),
        ("Nombre binaire 2 ou nombre de rang de décalage(si décalage) :", tk.Entry(root)),
        ("Nombre binaire 1 opération logique:", tk.Entry(root)),
        ("Nombre binaire 2 opération logique:", tk.Entry(root)),
        ("Entrez le côté à décaler G/D:", tk.Entry(root)),
        ("Nombre pour Complément à 2:", tk.Entry(root)),
        ("Entrez le nombre pour decalage : ", tk.Entry(root)),
        ("", None),  # Spacer
    ]

    for i, (label_text, element) in enumerate(elements_info):
        if label_text:
            label = tk.Label(root, text=label_text)
            label.grid(row=i, column=0, padx=5, pady=5, sticky="w")

        if element:
            element.grid(row=i, column=1, padx=5, pady=5)

    entry1 = elements_info[0][1]
    entry2 = elements_info[1][1]
    entry3 = elements_info[2][1]
    entry4 = elements_info[3][1]
    entryCote = elements_info[4][1]
    complement2_entry = elements_info[5][1]
    entryDecalage = elements_info[6][1]

    button_info = [
        ("Addition", somme),
        ("Soustraction", soustraction),
        ("Multiplication", multiplication),
        ("Division", division),
        ("ET (AND)", lambda: ET(entry3.get(), entry4.get())),
        ("NON (NOT)", lambda: NON(entry3.get())),
        ("OU (OR)", lambda: OU(entry3.get(), entry4.get())),
        ("Complément à 2", lambda: Complement2(complement2_entry.get())),
        ("Décalage", decalage),
    ]

    for i, (button_text, command) in enumerate(button_info):
        button = tk.Button(root, text=button_text, command=command)
        button.grid(row=len(elements_info) + i, column=0, padx=5, pady=5, sticky="ew")

    result_label = tk.Label(root, text="")
    result_label.grid(row=len(elements_info) + len(button_info), column=0, columnspan=2, pady=10, sticky="ew")

    root.mainloop()

create_ui()

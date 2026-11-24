import customtkinter as ctk
from tkinter import messagebox
from generator import generate_password
from evaluator import evaluate_password

# Config globale (mode sombre, style moderne)
ctk.set_appearance_mode("dark")   # "light" ou "system"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

# === Fonctions ===
def handle_generation():
    pwd = generate_password()
    entry_pwd.delete(0, "end")
    entry_pwd.insert(0, pwd)
    lbl_result.configure(text="✅ Mot de passe généré !", text_color="green")

def handle_evaluation():
    pas = entry_pwd.get().strip()
    if not pas:
        messagebox.showwarning("Erreur", "Veuillez entrer ou générer un mot de passe.")
        return

    result = evaluate_password(pas)
    feedback = "\n".join(f"- {fb}" for fb in result["feedback"])
    message = f"Score : {result['score']}/6\nNiveau : {result['strength']}"

    if feedback:
        message += f"\n\nSuggestions :\n{feedback}"

    lbl_result.configure(text=message, text_color="white")

    # Si mot de passe est très fort → proposer de quitter ou continuer
    if result["strength"] == "Très fort":
        if messagebox.askyesno("Succès", "✅ Mot de passe très fort atteint ! Voulez-vous quitter ?"):
            root.destroy()

def quitter():
    root.destroy()

# === Interface ===
root = ctk.CTk()
root.title("🔒 SecuPass - Gestionnaire de mots de passe")
root.geometry("600x400")

# Titre
label = ctk.CTkLabel(root, text="Bienvenue dans SecuPass", font=("Arial", 20, "bold"))
label.pack(pady=20)

# Zone de saisie
entry_pwd = ctk.CTkEntry(root, placeholder_text="Entrez ou générez un mot de passe", width=400, height=40)
entry_pwd.pack(pady=15)

# Boutons
frame_btns = ctk.CTkFrame(root)
frame_btns.pack(pady=10)

btn_gen = ctk.CTkButton(frame_btns, text="🔑 Générer", command=handle_generation, width=120, height=40, fg_color="#27ae60")
btn_gen.grid(row=0, column=0, padx=15)

btn_eval = ctk.CTkButton(frame_btns, text="📊 Évaluer", command=handle_evaluation, width=120, height=40, fg_color="#2980b9")
btn_eval.grid(row=0, column=1, padx=15)

btn_quit = ctk.CTkButton(frame_btns, text="❌ Quitter", command=quitter, width=120, height=40, fg_color="#c0392b")
btn_quit.grid(row=0, column=2, padx=15)

# Zone résultat
lbl_result = ctk.CTkLabel(root, text="", font=("Arial", 14), justify="left")
lbl_result.pack(pady=20)

root.mainloop()

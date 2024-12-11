import streamlit as st
from streamlit_option_menu import option_menu

# Fonction d'authentification
def authenticate(username, password):
    return username == "root" and password == "rootMDP"

# Fonction principale
def main():
    # Vérifie si l'utilisateur est authentifié
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        # Page de connexion
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if authenticate(username, password):
                st.session_state.authenticated = True
                st.success("Connexion réussie !")
            else:
                st.error("Identifiants incorrects.")
    else:
        # Ajout d'un bouton de déconnexion
        if st.sidebar.button("Déconnexion"):
            st.session_state.authenticated = False
            st.experimental_rerun()

        # Menu avec icônes
        page = option_menu(
            menu_title=None,
            options=["Accueil", "Album de photos"],  # Options du menu
            icons=["house", "camera"],  # Icônes associées
            default_index=0,
            orientation="horizontal",
        )

        # Affichage de la page sélectionnée
        if page == "Accueil":
            st.title("Bienvenue sur ma page")
            st.image(
                "https://github.com/Yas-rad/Streamlit-Partie-3-/blob/main/image%20welcome.jpg?raw=true", 
                caption="Image de bienvenue",
                use_column_width=True,
            )
        elif page == "Album de photos":
            st.title("Bienvenue dans l'album de mon chat")
            cols = st.columns(3)
            images =[
        "https://github.com/Yas-rad/Streamlit-Partie-3-/blob/main/photo%201.jpg?raw=true",
        "https://github.com/Yas-rad/Streamlit-Partie-3-/blob/main/Photo%202.jpg?raw=true",
        "https://github.com/Yas-rad/Streamlit-Partie-3-/blob/main/Photo%204.jpg?raw=true",
    ]
            for col, img_url in zip(cols, images):
                try : 
                    col.image(img_url, use_column_width=True)
                except FileNotFoundError:
                    col.error("Image non trouvée.")

# Point d'entrée du script
if __name__ == "__main__":
    main()

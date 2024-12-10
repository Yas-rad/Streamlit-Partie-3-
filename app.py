import streamlit as st
from streamlit_option_menu import option_menu

# Fonction d'authentification
def authenticate(username, password):
    return username == "root" and password == "password"

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
                "C:/Users/RADOUR/Documents/Wild Code School/S-11/image welcome",
                caption="Image de bienvenue",
                use_column_width=True,
            )
        elif page == "Album de photos":
            st.title("Album de photos")
            st.write("Voici quelques photos d'animaux !")
            cols = st.columns(3)
            images = [
                "C:/Users/RADOUR/Documents/Wild Code School/S-11/photo 1",
                "C:/Users/RADOUR/Documents/Wild Code School/S-11/photo 2",
                "C:/Users/RADOUR/Documents/Wild Code School/S-11/photo 3",
            ]
            for col, img_url in zip(cols, images):
                col.image(img_url, use_column_width=True)

# Point d'entrée du script
if __name__ == "__main__":
    main()

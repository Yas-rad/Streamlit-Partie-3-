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
                "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Ffr%2Fvid%25C3%25A9os%2Fapplaudir&psig=AOvVaw06ns5WHJHwR4UCkZyNfbuI&ust=1733876558685000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCNjghdn3m4oDFQAAAAAdAAAAABAc",
                caption="Image de bienvenue",
                use_column_width=True,
            )
        elif page == "Album de photos":
            st.title("Album de photos")
            st.write("Voici quelques photos d'animaux !")
            cols = st.columns(3)
            images = [
                "https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fbe_fr%2Fsearch%3Fk%3Dchat%2Bdrole&psig=AOvVaw0aNL6wXkalFoF-dQT5N9bx&ust=1733876461950000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPi6taf3m4oDFQAAAAAdAAAAABAE",
                "https://www.google.com/url?sa=i&url=https%3A%2F%2Fstock.adobe.com%2Fbe_fr%2Fsearch%3Fk%3Dchat%2Bdrole&psig=AOvVaw0aNL6wXkalFoF-dQT5N9bx&ust=1733876461950000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPi6taf3m4oDFQAAAAAdAAAAABAJ",
                "https://www.google.com/url?sa=i&url=https%3A%2F%2Fdepositphotos.com%2Ffr%2Fphotos%2Fchat-plage.html&psig=AOvVaw0aNL6wXkalFoF-dQT5N9bx&ust=1733876461950000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPi6taf3m4oDFQAAAAAdAAAAABAT",
            ]
            for col, img_url in zip(cols, images):
                col.image(img_url, use_column_width=True)

# Point d'entrée du script
if __name__ == "__main__":
    main()

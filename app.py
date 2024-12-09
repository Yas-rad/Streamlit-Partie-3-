import streamlit as st
from PIL import Image
def authenticate(username, password):
    return username == "root" and password == "password"
def main():
    # Définir une session pour l'état de connexion
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        st.title("Login")
        
        # Champs pour l'authentification
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if authenticate(username, password):
                st.session_state.authenticated = True
                st.success("Connexion réussie!")
            else:
                st.error("Identifiants invalides!")
        
        # Message d'erreur si les champs sont vides
        if username == "" or password == "":
            st.warning("Les champs username et mot de passe doivent être remplis.")
        return

    # Si l'utilisateur est authentifié
    st.sidebar.button("Déconnexion", on_click=lambda: setattr(st.session_state, "authenticated", False))

    # Navigation entre les pages
    st.sidebar.title(f"Bienvenue {username}")
    page = st.sidebar.radio("Menu", ["🏠 Accueil", "🐱 Les photos de mon chat"])

    if page == "🏠 Accueil":
        st.header("Bienvenue sur ma page")
        st.image("https://media.giphy.com/media/3o6Zt481isNVuQI1l6/giphy.gif", width=400)
    elif page == "🐱 Les photos de mon chat":
        st.header("Bienvenue dans l'album de mon chat 🐱")
        cols = st.columns(3)

        # Ajouter trois images dans une ligne
        images = [
            "https://placekitten.com/200/300",
            "https://placekitten.com/201/301",
            "https://placekitten.com/202/302",
        ]
        for col, img_url in zip(cols, images):
            col.image(img_url, use_column_width=True)


if __name__ == "__main__":
    main()

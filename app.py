import streamlit as st

def authenticate(username, password):
    return username == "root" and password == "password"

def main():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
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
        st.sidebar.button("Déconnexion", on_click=lambda: st.session_state.update(authenticated=False))
        st.sidebar.title("Menu")
        page = st.sidebar.radio("Navigation", ["Accueil", "Album de photos"])

        if page == "Accueil":
            st.title("Bienvenue sur la page d'accueil !")
            st.write("Ceci est votre page principale.")
        elif page == "Album de photos":
            st.title("Album de photos")
            st.write("Voici quelques photos d'animaux !")
            cols = st.columns(3)
            images = [
                "https://placekitten.com/200/300",
                "https://placekitten.com/201/300",
                "https://placekitten.com/202/300",
            ]
            for col, img_url in zip(cols, images):
                col.image(img_url, use_column_width=True)

if __name__ == "__main__":
    main()

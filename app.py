import streamlit as st


def ui_setup() -> None:
    st.set_page_config(
        page_title="Elastic Streamlit App",
        page_icon="./.streamlit/logo-elastic-glyph-color.svg",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    with open("./.streamlit/style.html", "r") as f:
        style = f.read()
    st.markdown(style, unsafe_allow_html=True)


def ui_sidebar() -> None:
    with st.sidebar:
        st.logo(".streamlit/logo-elastic-horizontal-color-reverse.png")
        st.markdown("_Sidebar options go here_")


def ui_main() -> None:
    with st.container():
        col1, col2, col3 = st.columns((1, 5, 1))
    with col2:
        st.header("Elastic Streamlit App", divider="grey")
        st.markdown("_Rest of app goes here_")

if __name__ == "__main__":
    ui_setup()
    ui_sidebar()
    ui_main()

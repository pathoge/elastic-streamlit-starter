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
        col1, col2, col3 = st.columns((1, 3, 1))
    with col2:
        st.header("Elastic Streamlit App", divider="grey")
        st.button("Click me", type="primary")
        st.text_input("Type some text here")
        st.radio("Radio buttons", options=[1, 2, 3], horizontal=True)
        with st.expander("Expand me"):
            st.markdown("### Markdown")
        st.slider("Slider")
        st.info("Informational message")
        
if __name__ == "__main__":
    ui_setup()
    ui_sidebar()
    ui_main()
import streamlit as st

from auth import login

from rag import load_index, get_chat_engine, extract_sources, find_image

from analytics import log_query

from PIL import Image

import os

import re

 

# ── Configurazione pagina ────────────────────────────────────

st.set_page_config(

    page_title="AMPS Study Assistant",

    page_icon="🎓",

    layout="centered"

)

 

# ── Inizializzazione sessione ────────────────────────────────

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "user_role" not in st.session_state:

    st.session_state.user_role = None

if "user_email" not in st.session_state:

    st.session_state.user_email = None

if "messaggi" not in st.session_state:

    st.session_state.messaggi = []

if "chat_engine" not in st.session_state:

    st.session_state.chat_engine = None

if "modalita" not in st.session_state:

    st.session_state.modalita = "💬 Chat"

if "hint_count" not in st.session_state:

    st.session_state.hint_count = 0

 

# ── Pagina di login ──────────────────────────────────────────

def show_login():

    st.title("🎓 AMPS Study Assistant")

    st.caption("Analysis and Management of Production Systems")

    st.divider()

    with st.form("login_form"):

        email = st.text_input("Email", placeholder="nome@studenti.polito.it")

        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Accedi", use_container_width=True)

        if submitted:

            if not email or not password:

                st.error("Inserisci email e password")

                return

            role, result = login(email, password)

            if role is None:

                st.error(result)

            elif role == "admin":

                st.session_state.logged_in = True

                st.session_state.user_role = "admin"

                st.session_state.user_email = email

                st.rerun()

            elif role == "student":

                st.session_state.logged_in = True

                st.session_state.user_role = "student"

                st.session_state.user_email = result

                st.rerun()

 

# ── Pagina chat ──────────────────────────────────────────────

def show_chat():

    # Header

    col1, col2 = st.columns([4, 1])

    with col1:

        st.title("🎓 AMPS Study Assistant")

    with col2:

        if st.button("Esci"):

            for key in list(st.session_state.keys()):

                del st.session_state[key]

            st.rerun()

 

    if st.session_state.user_role == "admin":

        st.info("👑 Sei loggato come admin. [Vai alla dashboard](/admin)")

 

    st.caption(f"Loggato come: {st.session_state.user_email}")

 

    # ── Selettore modalità ───────────────────────────────────

    st.divider()

    col1, col2, col3 = st.columns(3)

 

    with col1:

        if st.button(

            "💬 Chat",

            use_container_width=True,

            type="primary" if st.session_state.modalita == "💬 Chat" else "secondary"

        ):

            if st.session_state.modalita != "💬 Chat":

                st.session_state.modalita = "💬 Chat"

                st.session_state.chat_engine = None

                st.session_state.messaggi = []

                st.session_state.hint_count = 0

                st.rerun()

 

    with col2:

        if st.button(

            "💡 Hint",

            use_container_width=True,

            type="primary" if st.session_state.modalita == "💡 Hint" else "secondary"

        ):

            if st.session_state.modalita != "💡 Hint":

                st.session_state.modalita = "💡 Hint"

                st.session_state.chat_engine = None

                st.session_state.messaggi = []

                st.session_state.hint_count = 0

                st.rerun()

 

    with col3:

        if st.button(

            "📝 Quiz",

            use_container_width=True,

            type="primary" if st.session_state.modalita == "📝 Quiz" else "secondary"

        ):

            if st.session_state.modalita != "📝 Quiz":

                st.session_state.modalita = "📝 Quiz"

                st.session_state.chat_engine = None

                st.session_state.messaggi = []

                st.session_state.hint_count = 0

                st.rerun()

 

    # Descrizione modalità attiva

    if st.session_state.modalita == "💬 Chat":

        st.caption("📖 Modalità Chat — Risposte complete con citazioni delle fonti")

    elif st.session_state.modalita == "💡 Hint":

        st.caption("💡 Modalità Hint — Ti guido passo per passo senza darti la soluzione")

    else:

        st.caption("📝 Modalità Quiz — Domande a scelta multipla per prepararti all'esame")

 

    st.divider()

 

    # ── Carica indice e chat engine ──────────────────────────

    index = load_index()

    if st.session_state.chat_engine is None:

        st.session_state.chat_engine = get_chat_engine(

            index, st.session_state.modalita

        )

 

    # ── Storico messaggi ─────────────────────────────────────

    for msg in st.session_state.messaggi:

        with st.chat_message(msg["ruolo"]):

            st.markdown(msg["testo"])

            if msg.get("immagine") and os.path.exists(msg["immagine"]):

                img = Image.open(msg["immagine"])

                st.image(img, use_column_width=True)

 

    # ── Input utente ─────────────────────────────────────────

    if st.session_state.modalita == "💬 Chat":

        placeholder = "Fai una domanda sul corso..."

    elif st.session_state.modalita == "💡 Hint":

        placeholder = "Descrivi l'esercizio su cui vuoi aiuto..."

    else:

        placeholder = "Scrivi l'argomento su cui vuoi fare il quiz..."

 

    domanda = st.chat_input(placeholder)

 

    if domanda:

        with st.chat_message("user"):

            st.markdown(domanda)

        st.session_state.messaggi.append(

            {"ruolo": "user", "testo": domanda}

        )

 

        immagine = None

        testo = ""

 

        with st.chat_message("assistant"):

            with st.spinner("Cerco nel materiale del corso..."):

                try:

                    risposta = st.session_state.chat_engine.chat(domanda)

                    testo = str(risposta)

                except Exception as e:

                    testo = f"Errore: {str(e)}"

 

                st.markdown(testo)

 

                # Cerca immagine nella risposta

                immagine = find_image(testo)

                if not immagine:

                    nums = re.findall(r'image(\d+)', testo, re.IGNORECASE)

                    for num in nums:

                        for i in range(13):

                            folder = f"images_{i:02d}"

                            path = os.path.join(folder, f"image{num}_schema.jpg")

                            if os.path.exists(path):

                                immagine = path

                                break

                        if immagine:

                            break

 

                if immagine and os.path.exists(immagine):

                    img = Image.open(immagine)

                    st.image(img, caption=immagine, use_column_width=True)

 

                sources = extract_sources(testo)

                log_query(

                    st.session_state.user_email,

                    domanda,

                    sources

                )

 

        st.session_state.messaggi.append({

            "ruolo": "assistant",

            "testo": testo,

            "immagine": immagine

        })

 

# ── Router principale ────────────────────────────────────────

if not st.session_state.logged_in:

    show_login()

else:

    show_chat()
import streamlit as st

import plotly.express as px

import pandas as pd

from auth import login, load_users, add_user, remove_user, toggle_user, reset_password

from analytics import load_analytics, get_top_queries, get_top_sources, get_top_users, get_queries_per_day, export_csv

 

# ── Configurazione pagina ────────────────────────────────────

st.set_page_config(

    page_title="AMPS Admin Dashboard",

    page_icon="👑",

    layout="wide"

)

 

# ── Controllo accesso ────────────────────────────────────────

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

if "user_role" not in st.session_state:

    st.session_state.user_role = None

 

if not st.session_state.logged_in:

    st.title("👑 Admin Dashboard")

    st.warning("Devi essere loggato come admin per accedere a questa pagina.")

    with st.form("admin_login"):

        email = st.text_input("Email admin")

        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Accedi")

        if submitted:

            role, result = login(email, password)

            if role == "admin":

                st.session_state.logged_in = True

                st.session_state.user_role = "admin"

                st.session_state.user_email = email

                st.rerun()

            else:

                st.error("Credenziali non valide o non sei admin")

    st.stop()

 

if st.session_state.user_role != "admin":

    st.error("Accesso negato — solo per admin")

    st.stop()

 

# ── Dashboard ────────────────────────────────────────────────

col1, col2 = st.columns([4, 1])

with col1:

    st.title("👑 AMPS Admin Dashboard")

with col2:

    if st.button("Esci"):

        for key in list(st.session_state.keys()):

            del st.session_state[key]

        st.rerun()

 

tab1, tab2, tab3 = st.tabs(["📊 Statistiche", "👥 Utenti", "📋 Log Query"])

 

# ── TAB 1: Statistiche ───────────────────────────────────────

with tab1:

    logs = load_analytics()

    total_queries = len(logs)

 

    # Metriche generali

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric("Query totali", total_queries)

    with col2:

        users = load_users()

        st.metric("Studenti registrati", len(users))

    with col3:

        top_users = get_top_users(1)

        if top_users:

            st.metric("Utente più attivo", top_users[0][0].split("@")[0])

 

    st.divider()

 

    # Grafico query per giorno

    st.subheader("📈 Query per giorno")

    queries_per_day = get_queries_per_day()

    if queries_per_day:

        df_days = pd.DataFrame(

            list(queries_per_day.items()),

            columns=["Data", "Query"]

        )

        fig = px.bar(df_days, x="Data", y="Query", color_discrete_sequence=["#4F8BF9"])

        st.plotly_chart(fig, use_container_width=True)

    else:

        st.info("Nessuna query ancora registrata")

 

    st.divider()

 

    # Top slide citate

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📚 Slide più citate")

        top_sources = get_top_sources(10)

        if top_sources:

            df_sources = pd.DataFrame(top_sources, columns=["Slide", "Citazioni"])

            st.dataframe(df_sources, use_container_width=True)

        else:

            st.info("Nessuna citazione ancora")

 

    with col2:

        st.subheader("🔍 Argomenti più cercati")

        top_queries = get_top_queries(10)

        if top_queries:

            df_queries = pd.DataFrame(top_queries, columns=["Query", "Frequenza"])

            st.dataframe(df_queries, use_container_width=True)

        else:

            st.info("Nessuna query ancora")

 

    # Utenti più attivi

    st.divider()

    st.subheader("👥 Utenti più attivi")

    top_users = get_top_users(5)

    if top_users:

        df_users = pd.DataFrame(top_users, columns=["Email", "Query"])

        fig2 = px.bar(

            df_users, x="Email", y="Query",

            color_discrete_sequence=["#F97B4F"]

        )

        st.plotly_chart(fig2, use_container_width=True)

    else:

        st.info("Nessun utente ancora attivo")

 

# ── TAB 2: Gestione utenti ───────────────────────────────────

with tab2:

    st.subheader("👥 Studenti registrati")

    users = load_users()

 

    if users:

        df = pd.DataFrame([

            {

                "Email": email,

                "Attivo": "✅" if data["active"] else "❌",

                "Query": data.get("query_count", 0),

                "Creato": data.get("created_at", "")[:10]

            }

            for email, data in users.items()

        ])

        st.dataframe(df, use_container_width=True)

    else:

        st.info("Nessuno studente registrato")

 

    st.divider()

 

    # Aggiungi utente

    st.subheader("➕ Aggiungi studente")

    with st.form("add_user_form"):

        new_email = st.text_input("Email studente")

        new_password = st.text_input("Password temporanea", type="password")

        submitted = st.form_submit_button("Aggiungi")

        if submitted:

            if new_email and new_password:

                ok, msg = add_user(new_email, new_password)

                if ok:

                    st.success(msg)

                    st.rerun()

                else:

                    st.error(msg)

 

    st.divider()

 

    # Gestisci utente esistente

    st.subheader("⚙️ Gestisci studente")

    if users:

        selected = st.selectbox("Seleziona studente", list(users.keys()))

        col1, col2, col3 = st.columns(3)

        with col1:

            if st.button("Abilita/Disabilita"):

                ok, msg = toggle_user(selected)

                if ok:

                    st.success(msg)

                    st.rerun()

        with col2:

            if st.button("Rimuovi", type="primary"):

                ok, msg = remove_user(selected)

                if ok:

                    st.success(msg)

                    st.rerun()

                else:

                    st.error(msg)

        with col3:

            new_pwd = st.text_input("Nuova password", type="password", key="reset_pwd")

            if st.button("Reset password"):

                if new_pwd:

                    ok, msg = reset_password(selected, new_pwd)

                    if ok:

                        st.success(msg)

                    else:

                        st.error(msg)

 

# ── TAB 3: Log query ─────────────────────────────────────────

with tab3:

    st.subheader("📋 Ultime 50 query")

    logs = load_analytics()

    if logs:

        df_logs = pd.DataFrame(logs[-50:])

        st.dataframe(df_logs, use_container_width=True)

 

        st.divider()

        csv = export_csv()

        if csv:

            st.download_button(

                label="📥 Esporta tutto in CSV",

                data=csv,

                file_name="analytics_amps.csv",

                mime="text/csv"

            )

    else:

        st.info("Nessuna query ancora registrata")
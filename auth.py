import json

import os

import bcrypt

import streamlit as st

 

USERS_FILE = "data/users.json"

 

def init_users_file():

    """Crea il file utenti se non esiste"""

    if not os.path.exists("data"):

        os.makedirs("data")

    if not os.path.exists(USERS_FILE):

        with open(USERS_FILE, "w") as f:

            json.dump({}, f)

 

def load_users():

    """Carica tutti gli utenti"""

    init_users_file()

    with open(USERS_FILE, "r") as f:

        return json.load(f)

 

def save_users(users):

    """Salva tutti gli utenti"""

    with open(USERS_FILE, "w") as f:

        json.dump(users, f, indent=2)

 

def hash_password(password):

    """Cifra la password"""

    return bcrypt.hashpw(

        password.encode("utf-8"),

        bcrypt.gensalt()

    ).decode("utf-8")

 

def check_password(password, hashed):

    """Verifica la password"""

    return bcrypt.checkpw(

        password.encode("utf-8"),

        hashed.encode("utf-8")

    )

 

def add_user(email, password):

    """Aggiunge uno studente"""

    users = load_users()

    if email in users:

        return False, "Utente già esistente"

    users[email] = {

        "password": hash_password(password),

        "active": True,

        "created_at": str(__import__("datetime").datetime.now()),

        "query_count": 0

    }

    save_users(users)

    return True, "Utente aggiunto con successo"

 

def remove_user(email):

    """Rimuove uno studente"""

    users = load_users()

    if email not in users:

        return False, "Utente non trovato"

    del users[email]

    save_users(users)

    return True, "Utente rimosso"

 

def toggle_user(email):

    """Abilita/disabilita uno studente"""

    users = load_users()

    if email not in users:

        return False, "Utente non trovato"

    users[email]["active"] = not users[email]["active"]

    save_users(users)

    stato = "abilitato" if users[email]["active"] else "disabilitato"

    return True, f"Utente {stato}"

 

def reset_password(email, new_password):

    """Resetta la password di uno studente"""

    users = load_users()

    if email not in users:

        return False, "Utente non trovato"

    users[email]["password"] = hash_password(new_password)

    save_users(users)

    return True, "Password resettata"

 

def login(email, password):

    """

    Verifica le credenziali.

    Ritorna: ("admin", None), ("student", email), o (None, messaggio_errore)

    """

    # Controlla se è l'admin

    admin_email = st.secrets.get("ADMIN_EMAIL", "")

    admin_password = st.secrets.get("ADMIN_PASSWORD", "")

    if email == admin_email and password == admin_password:

        return "admin", None

 

    # Controlla se è uno studente

    users = load_users()

    if email not in users:

        return None, "Email non trovata"

    if not users[email]["active"]:

        return None, "Account disabilitato"

    if not check_password(password, users[email]["password"]):

        return None, "Password errata"

 

    # Aggiorna contatore query

    users[email]["query_count"] = users[email].get("query_count", 0)

    save_users(users)

    return "student", email
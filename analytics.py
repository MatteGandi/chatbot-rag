import json

import os

from datetime import datetime

 

ANALYTICS_FILE = "data/analytics.json"

 

def init_analytics_file():

    """Crea il file analytics se non esiste"""

    if not os.path.exists("data"):

        os.makedirs("data")

    if not os.path.exists(ANALYTICS_FILE):

        with open(ANALYTICS_FILE, "w") as f:

            json.dump([], f)

 

def log_query(user_email, query, sources_cited):

    """Registra una query nel log"""

    init_analytics_file()

    with open(ANALYTICS_FILE, "r") as f:

        logs = json.load(f)

    logs.append({

        "timestamp": str(datetime.now()),

        "user_email": user_email,

        "query": query,

        "sources_cited": sources_cited

    })

    with open(ANALYTICS_FILE, "w") as f:

        json.dump(logs, f, indent=2)

 

def load_analytics():

    """Carica tutti i log"""

    init_analytics_file()

    with open(ANALYTICS_FILE, "r") as f:

        return json.load(f)

 

def get_top_queries(n=10):

    """Restituisce le query più frequenti"""

    logs = load_analytics()

    from collections import Counter

    queries = [log["query"] for log in logs]

    return Counter(queries).most_common(n)

 

def get_top_sources(n=10):

    """Restituisce le slide più citate"""

    logs = load_analytics()

    from collections import Counter

    sources = []

    for log in logs:

        sources.extend(log.get("sources_cited", []))

    return Counter(sources).most_common(n)

 

def get_top_users(n=5):

    """Restituisce gli utenti più attivi"""

    logs = load_analytics()

    from collections import Counter

    users = [log["user_email"] for log in logs]

    return Counter(users).most_common(n)

 

def get_queries_per_day():

    """Restituisce il numero di query per giorno"""

    logs = load_analytics()

    from collections import Counter

    days = [log["timestamp"][:10] for log in logs]

    return dict(sorted(Counter(days).items()))

 

def export_csv():

    """Esporta i log in formato CSV"""

    import pandas as pd

    logs = load_analytics()

    if not logs:

        return None

    df = pd.DataFrame(logs)

    return df.to_csv(index=False).encode("utf-8")
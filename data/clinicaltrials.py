import requests
import pandas as pd

def fetch_oncology_trials():
    url = "https://clinicaltrials.gov/api/v2/studies"
    params = {
        "query.cond": "cancer",
        "query.term": "phase 3",
        "fields": "NCTId,BriefTitle,OverallStatus,Phase,LocationCountry",
        "pageSize": 1000,
        "format": "json"
    }
    response = requests.get(url, params=params)
    data = response.json()
    studies = data.get("studies", [])
    records = []
    for study in studies:
        protocol = study.get("protocolSection", {})
        locs = protocol.get("contactsLocationsModule", {}).get("locations", [])
        countries = list(set([l.get("country", "") for l in locs if l.get("country")]))
        for country in countries:
            records.append({"country": country, "source": "ClinicalTrials.gov"})
    return pd.DataFrame(records)

if __name__ == "__main__":
    df = fetch_oncology_trials()
    print(f"Fetched {len(df)} records")
    print(df.head(10))
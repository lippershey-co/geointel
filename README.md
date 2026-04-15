# GeoIntel — Geographic Intelligence Engine

> One AI agent. Any pharma world map on demand.

Open-source geographic intelligence for pharma and biotech. Type any question in plain English — get an interactive world map backed by live public data sources.

Built by [Lippershey](https://aistack.bio) · AGPL-3.0 licensed

---

## What it does

GeoIntel transforms natural language queries into interactive pharma world maps:

- Phase 3 oncology trial density by country
- Cancer mortality burden vs trial access gaps
- Drug approval timelines by regulatory agency
- R&D spend per capita by disease area
- And any other pharma intelligence query you can ask

## Data sources

All data is public, free, and open:

- ClinicalTrials.gov API
- WHO Global Health Observatory
- World Bank Open Data
- EMA Open Data
- OpenFDA / FAERS

## Run locally

```bash
git clone https://github.com/lippershey-co/geointel.git
cd geointel
python3 -m venv venv
source venv/bin/activate
pip3 install streamlit plotly pandas requests
python3 -m streamlit run app.py
```

## License

AGPL-3.0 — see [LICENSE](LICENSE). Commercial licence available for enterprise deployments that cannot comply with AGPL. Contact: hello@lippershey.co

## Disclaimer

See [DISCLAIMER.md](DISCLAIMER.md).

## Built with

Python · Streamlit · Plotly · ClinicalTrials.gov API

---

*Lippershey · GeoIntel· Open-source AI tools for pharma and biotech*

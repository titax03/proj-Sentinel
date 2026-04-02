<div align="center">

# 🚨 Project Sentinel
**AI-Powered, Zero-Latency Emergency Dispatch System**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![LLM Integration](https://img.shields.io/badge/AI-LLM_Powered-orange.svg)]()
[![Geocoding](https://img.shields.io/badge/Geocoding-GeoPy-success.svg)]()
[![Status](https://img.shields.io/badge/Status-Hackathon_Ready-brightgreen.svg)]()

*In an emergency control room, every second counts. Sentinel removes the human bottleneck by detecting threats, drafting evacuation scripts, and synthesizing broadcast audio in milliseconds.*

</div>

---

## ⚡ Why Sentinel? 
Traditional emergency systems rely on human operators to parse chaotic reports, verify locations, and manually trigger alerts. **Sentinel automates the dispatch pipeline.** It processes messy, real-world data streams, filters out noise, and prepares automated voice alerts for immediate deployment—all while running locally to protect sensitive government and citizen data.

## 🚀 Key Features & Technical Solutions

### 1. 🧠 Semantic Threat Detection (Solving the "Messy Human" Problem)
Real people in emergencies type with slang, typos, and panic (e.g., *"omg fire help plz at sec 62"*). Standard keyword matching fails here.
* **The Fix:** Sentinel utilizes advanced **LLM integration** to understand semantic context, accurately classifying intent and recognizing that "help" means "critical emergency" despite the formatting.

### 2. 📍 High-Speed Geocoding 
Maps need coordinates, not text. 
* **The Fix:** Uses **GeoPy** (OpenStreetMap’s Nominatim) to extract location strings and convert them into Latitude/Longitude. *Note: Optimized with a hardcoded dictionary for zero-latency live demo performance.*

### 3. 🛡️ Spam & Troll Filtering (Clustering & Confidence Scores)
A single automated alert based on a fake tweet is dangerous. 
* **The Fix:** Sentinel requires a cluster of at least **3 high-severity reports from the same 2km radius within a 10-minute window** to upgrade an event to "Verified," completely neutralizing isolated trolls.

### 4. 🔒 Privacy-First Architecture
For the demo, the local machine acts as the Government Command Center server. All heavy AI processing is handled locally, ensuring sensitive disaster data never leaks to public clouds. 

---

## 🛠️ Tech Stack
* **Language:** Python
* **AI/NLP:** LLM API (for semantic intent parsing)
* **Geocoding:** GeoPy / OpenStreetMap Nominatim
* **Data Simulation:** Custom Python CSV parser for live-feed emulation

---

## 🗺️ Deployment Roadmap (Vision)
Sentinel is designed to integrate with real-world telecom infrastructure. Citizens do not need to download a vulnerable, battery-draining app. 

* **Twilio Programmable Voice APIs:** For auto-dialing vulnerable citizens using standard voice calls (works on legacy "brick" phones).
* **WhatsApp Business API:** For localized voice-note broadcasts, utilizing existing infrastructure.
* **Cell Broadcast System (WEA):** The AI dashboard acts as the trigger to send localized text payloads directly to government cell towers, bypassing the internet entirely.

---

## 💻 Local Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/titax03/proj-Sentinel.git](https://github.com/titax03/proj-Sentinel.git)
   cd proj-Sentinel

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3.**Run the Simulation:**
   ```bash
   python main.py

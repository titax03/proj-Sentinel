<div align="center">

# 🚨 Project Sentinel
**Zero-Cloud AI Emergency Triage & Geospatial Dispatch System**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Local AI](https://img.shields.io/badge/AI-Llama_3.2_Local-orange.svg)]()
[![UI Framework](https://img.shields.io/badge/Frontend-Streamlit-red.svg)]()
[![Mapping](https://img.shields.io/badge/Mapping-Folium-success.svg)]()
[![Status](https://img.shields.io/badge/Status-Hackathon_Ready-brightgreen.svg)]()

*In an emergency control room, every second counts. Sentinel removes the human bottleneck by ingesting chaotic text data, mapping threat clusters dynamically, and synthesizing accessible broadcast audio in milliseconds—all without relying on public cloud APIs.*

</div>

---

## ⚡ Why Sentinel? 
Traditional emergency systems rely on human operators to parse chaotic reports, verify locations, and manually trigger alerts. **Sentinel automates the dispatch pipeline.** During a disaster, government agencies cannot legally send sensitive citizen data to public cloud servers like OpenAI. Furthermore, generic city alarms leave vulnerable populations—like the visually impaired—behind. Sentinel solves this by running state-of-the-art NLP entirely locally, ensuring **100% data sovereignty**, zero-latency processing, and automated text-to-speech accessibility.

## 🚀 Key Features

### 1. 🧠 Zero-Cloud Semantic Triage
Real people in emergencies type with slang, typos, and panic (e.g., *"omg fire help plz at sec 62"*). 
* **The Solution:** Sentinel utilizes a **local Llama 3 model via Ollama** to understand semantic context. It accurately classifies intent, extracts landmarks, and grades severity (Critical, Moderate, Low) without ever transmitting data over the internet.

### 2. 📍 Geospatial Threat Graphing 
Spreadsheets are useless to first responders during a crisis. 
* **The Solution:** Sentinel automatically plots extracted locations onto a dynamic, dark-mode **Folium map**. This transforms isolated text messages into a visual spatial graph, allowing dispatchers to instantly identify disaster chokepoints.

### 3. 🛡️ Spam Filtering & Cluster Verification
A single automated alert based on a fake tweet is dangerous. 
* **The Solution:** Sentinel visually clusters high-severity reports. By mapping incident density, it neutralizes isolated trolls and verifies genuine emergencies when multiple nodes trigger in a tight radius.

### 4. 🔊 Accessible Automated Dispatch
Maps don't help visually impaired citizens trapped in a disaster zone.
* **The Solution:** For every "Critical" zone detected, Sentinel uses **gTTS (Google Text-to-Speech)** to instantly draft and synthesize a localized MP3 audio warning, ready for immediate telecom deployment.

---

## 🛠️ Tech Stack
* **Language:** Python
* **AI Engine:** Llama 3.2 (running 100% locally via Ollama)
* **Frontend Dashboard:** Streamlit
* **Geospatial Mapping:** Folium & Streamlit-Folium
* **Audio Synthesis:** gTTS (Google Text-to-Speech)
* **Data Processing:** Pandas

---

## 🗺️ Deployment Roadmap (Enterprise Vision)
Sentinel is designed to integrate with real-world telecom infrastructure. Citizens do not need to download a vulnerable, battery-draining app. 

* **Twilio Programmable Voice APIs:** Sentinel acts as the trigger to push generated MP3 audio files to Twilio, auto-dialing vulnerable citizens using standard voice calls (works on legacy "brick" phones).
* **WhatsApp Business API:** For localized voice-note broadcasts, utilizing existing regional infrastructure.
* **Predictive Spread Mapping:** Future integration with localized weather APIs (wind speed/direction) to predict where fire/gas threats will move next.

---

## 💻 Local Setup & Installation

### 1. Prerequisites
* Python 3.8+
* [Ollama](https://ollama.com/) installed on your local machine.

### 2. Install the Local AI Model
Open your terminal and pull the Llama 3 model to your machine:
    ```bash
    
    ollama run llama3.2

## 💻 Local Setup & Installation

3. **Clone the repository:**
   ```bash
   git clone [https://github.com/titax03/proj-Sentinel.git](https://github.com/titax03/proj-Sentinel.git)
   cd proj-Sentinel

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

5.**Run the Simulation:**
   ```bash
   streamlit run app.py

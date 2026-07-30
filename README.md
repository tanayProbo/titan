<div align="center">

  <h1>⚡ TITAN-X Data Engine</h1>
  <p><b>Universal AI-Powered Data Acquisition Infrastructure</b></p>

  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
  [![Open Source](https://img.shields.io/badge/Open%20Source-%E2%9D%A4-red)](https://github.com/tanayProbo/titan)
  [![Stars](https://img.shields.io/github/stars/tanayProbo/titan?style=social)](https://github.com/tanayProbo/titan/stargazers)

</div>

---

## 🌟 What is TITAN-X?

**TITAN-X** is an enterprise-grade, open-source, AI-native platform designed for **unified data acquisition, web crawling, intelligent browser automation, API intelligence, and knowledge indexing at planetary scale**.

By combining modern web automation, computer vision, on-device mobile accessibility analysis, and Large Language Models, TITAN-X bridges the gap between unstructured, dynamic web content and structured, clean, enterprise-ready knowledge.

> *Standing on the shoulders of giants — combining the best of Crawlee, Firecrawl, Scrcpy, and Public APIs into one unified AI-native engine.*

---

## 🧩 Architecture Overview

```
[Target APIs / Sites / Android Devices]
       │
       ├── (Proxy / Traffic Intercept) ──► [Proxy Sniffer] ──► [Schema Generator] ──► [PostgreSQL]
       │
       ▼  (Dynamic Pages / Android Screen Frames)
[Crawler Node Fleet / Mobile ADB Agent]
       │
       ▼  (Raw Payloads via Apache Kafka)
[Ray Distributed AI Workers]
       ├──► [Cleaning Engine] ──────────► Markdown Output
       ├──► [Entity Extractor] ─────────► Knowledge Triples ──► [Neo4j Graph DB]
       └──► [Document Embedder] ────────► Vector Embeddings ──► [Qdrant Vector DB]
```

---

## 🚀 Core Subsystems

### 🕷️ `core/` — Web Crawler Fleet
Adaptive autoscaling crawler with concurrency-locked request queues, browser fingerprint spoofing, proxy rotation, and robust session virtualization. Powered by **Playwright** for dynamic SPA rendering.

### 🧠 `visual_agent/` — AI Visual Browser Agent
A vision-language model loop that **visually understands DOM representations and screenshots**. Iteratively drives web actions (click, type, scroll) via precise coordinates — no hardcoded selectors needed.

### 📱 `mobile/` — Android Mobile Automation
Inspired by Scrcpy's low-latency architecture. Captures on-device Android screen frames via ADB, decodes them frame-by-frame, and runs automated mobile accessibility inspections.

### 🌐 `api_intelligence/` — API Traffic Interceptor
Intercepts live HTTP traffic through a proxy sniffer to **auto-generate OpenAPI specs and JSON schemas** in real-time, without any manual documentation.

### 🔗 `free_api_integration/` — Public API Subsystem
- **API Registry**: Categorized index of 100s of public APIs (Weather, Finance, News, AI, etc.)
- **Connector Generator**: Auto-writes Python REST client code with rate-limiting & retries
- **Health Monitor**: Async concurrent endpoint pinging with ClickHouse telemetry logging
- **Schema Detector**: Dynamically infers type-safe schemas from live API responses
- **Auto-Documenter**: Generates Markdown API documentation automatically

### ⚙️ `pipeline/` — AI Data Pipeline
Processes raw crawled data through deep learning stages:
- `cleaning.py` → Extracts clean Markdown
- `entity_extractor.py` → Named entity recognition and knowledge graph triples
- `embedder.py` → Generates vector embeddings for semantic search

### 🗄️ `storage/` — Multi-Backend Storage
Adapters for **PostgreSQL**, **ClickHouse**, **Neo4j Graph DB**, and **Qdrant Vector DB**.

### 📊 `dashboard/` — Visual System Console
A real-time browser dashboard (`index.html` + `app.js`) to monitor crawler fleet health, API statuses, and pipeline throughput.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Web Crawling | Playwright, Requests, BeautifulSoup |
| AI Agents | Vision-Language Models (LLM loop) |
| Mobile Automation | ADB, Scrcpy-inspired frame decoder |
| Stream Processing | Apache Kafka |
| Distributed Compute | Ray |
| Relational DB | PostgreSQL |
| Analytical DB | ClickHouse |
| Vector DB | Qdrant |
| Graph DB | Neo4j |
| Orchestration | Kubernetes, Helm, Terraform |
| Language | Python 3.10+ |

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.10+
- Docker & Docker Compose
- Node.js (for the dashboard)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/tanayProbo/titan.git
cd titan

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the tests
pytest titan/tests/
```

---

## 🛡️ Security & Politeness

TITAN-X is designed to be **responsible by default**:
- 🤝 Automatically maps `robots.txt` and respects rate limits
- 🔒 Integrates with **HashiCorp Vault** for secure credential management
- 🧹 Inline **PII sanitization** scrubs phone numbers, addresses, and passwords from all outputs

---

## 🗺️ Roadmap

| Phase | Goal | Status |
|---|---|---|
| Phase 1 | Ingestion Core & Request Queuing | ✅ Done |
| Phase 2 | API Interceptor & Free API Integration | ✅ Done |
| Phase 3 | Mobile ADB & Visual Agent DOM Planner | ✅ Done |
| Phase 4 | ClickHouse Analytics, Ray Embedders, Tests | 🚧 In Progress |
| Phase 5 | Kubernetes Deployment & Helm Charts | 🔜 Planned |

---

## 🤝 Contributing

Contributions are what make the open-source community amazing! See [CONTRIBUTING.md](CONTRIBUTING.md) for how to get started. Please also read our [Code of Conduct](CODE_OF_CONDUCT.md).

---

## 📜 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

---

## 👤 Author

**Tanay Praveen Agrawal** — Co-Founder & CEO @ [FoundryX](https://github.com/tanayProbo)

---

<div align="center">
  <sub>⚡ Built for the future of AI data acquisition. If you find this useful, please consider giving it a ⭐!</sub>
</div>

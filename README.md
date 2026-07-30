<div align="center">

```
████████╗██╗████████╗ █████╗ ███╗   ██╗      ██╗  ██╗
╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗  ██║      ╚██╗██╔╝
   ██║   ██║   ██║   ███████║██╔██╗ ██║       ╚███╔╝ 
   ██║   ██║   ██║   ██╔══██║██║╚██╗██║       ██╔██╗ 
   ██║   ██║   ██║   ██║  ██║██║ ╚████║      ██╔╝ ██╗
   ╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝      ╚═╝  ╚═╝
```

### **Universal AI-Powered Data Acquisition Engine**
*Crawl anything. Understand everything. At any scale.*

<br/>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)](https://kafka.apache.org/)
[![Ray](https://img.shields.io/badge/Ray-028CF0?style=for-the-badge&logo=ray&logoColor=white)](https://www.ray.io/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)](https://kubernetes.io/)

<br/>

[![GitHub stars](https://img.shields.io/github/stars/tanayProbo/titan?style=social)](https://github.com/tanayProbo/titan/stargazers)
&nbsp;&nbsp;
[![GitHub last commit](https://img.shields.io/github/last-commit/tanayProbo/titan)](https://github.com/tanayProbo/titan/commits/main)

</div>

---

## 🧠 What is TITAN-X?

**TITAN-X** is an AI-native data acquisition engine I built from scratch — designed to turn the chaotic, unstructured web into clean, machine-ready knowledge.

It combines:
- ⚡ **Distributed web crawling** with stealth & proxy rotation
- 👁️ **Vision-Language Model browser automation** — no selectors needed
- 📱 **Android screen capture & automation** via ADB
- 🔍 **Live API traffic interception** with auto-generated OpenAPI specs
- 🧬 **Deep learning pipeline** for cleaning, entity extraction, and embedding
- 🗄️ **Multi-backend storage** — PostgreSQL, ClickHouse, Neo4j, Qdrant

> Built by studying and going beyond Crawlee, Firecrawl, Scrcpy, and the Public APIs catalog — then combining the best of all of them into one unified engine.

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              DATA SOURCES (Web / APIs / Android)            │
└────────────────────────┬────────────────────────────────────┘
                         │
         ┌───────────────┼───────────────────────┐
         ▼               ▼                       ▼
  ┌─────────────┐  ┌───────────────┐    ┌──────────────────┐
  │ Proxy / API │  │ Dynamic Pages │    │  Android Device  │
  │  Sniffer   │  │  (Playwright) │    │   (ADB + Frames) │
  └──────┬──────┘  └──────┬────────┘    └────────┬─────────┘
         │                │                       │
         ▼                ▼                       ▼
  ┌─────────────┐  ┌────────────────────────────────────────┐
  │   Schema    │  │         CRAWLER NODE FLEET             │
  │  Generator  │  │  (Autoscaling · Sessions · Fingerprints)│
  └──────┬──────┘  └──────────────────┬─────────────────────┘
         │                            │
         ▼                            ▼
  ┌────────────┐         ┌────────────────────────┐
  │ PostgreSQL │         │     Apache Kafka Bus    │
  └────────────┘         └─────────────┬──────────┘
                                       │
                          ┌────────────▼─────────────┐
                          │   RAY DISTRIBUTED WORKERS │
                          ├──────────────────────────-┤
                          │  cleaning.py  →  Markdown │
                          │  entity_extractor.py →    │
                          │     Knowledge Triples      │
                          │  embedder.py  →           │
                          │     Vector Embeddings      │
                          └──┬───────────┬────────────┘
                             │           │
                    ┌────────▼──┐   ┌────▼──────────┐
                    │  Neo4j   │   │  Qdrant Vector │
                    │ Graph DB │   │      DB        │
                    └──────────┘   └────────────────┘
```

---

## 📦 Module Breakdown

<table>
<tr>
<td width="50%">

### 🕷️ `core/` — Crawler Fleet
- `crawler.py` — Autoscaling Playwright crawler with dynamic SPA support
- `browser_pool.py` — Browser instance lifecycle & fingerprint spoofing
- `request_queue.py` — Concurrency-locked FIFO request queue with retry states
- `session_pool.py` — Isolated session virtualization with proxy rotation

</td>
<td width="50%">

### 🧠 `visual_agent/` — AI Browser Agent
- `agent_loop.py` — VLM-driven action loop (click / type / scroll) using screen coordinates
- `dom_parser.py` — Converts live DOM tree into structured VLM-readable format

No CSS selectors. No XPaths. Pure vision.

</td>
</tr>
<tr>
<td>

### 📱 `mobile/` — Android Automation
- `adb_client.py` — ADB device connection & command execution
- `frame_decoder.py` — H.264 frame capture & decoding (Scrcpy-inspired)
- `inspector.py` — On-device accessibility tree crawler

</td>
<td>

### 🌐 `api_intelligence/` — Traffic Interceptor
- `proxy_sniffer.py` — MITM proxy that captures live HTTP/S traffic
- `schema_generator.py` — Auto-generates OpenAPI specs & JSON schemas from intercepted requests — no manual documentation needed

</td>
</tr>
<tr>
<td>

### 🔗 `free_api_integration/` — Public API Engine
- `api_registry.py` — Index of 100+ categorized public APIs
- `connector_generator.py` — Auto-writes Python REST clients with retries
- `health_monitor.py` — Async endpoint pinging with ClickHouse telemetry
- `schema_detector.py` — Type-safe schema inference from live responses
- `auto_doc.py` — Generates Markdown API docs automatically

</td>
<td>

### ⚙️ `pipeline/` — AI Processing Pipeline
- `cleaning.py` — Strips HTML noise → clean Markdown (LLM-ready)
- `entity_extractor.py` — Named entity recognition → knowledge triples → Neo4j
- `embedder.py` — Chunk embeddings → Qdrant for semantic search

Powered by **Ray** for distributed GPU inference.

</td>
</tr>
<tr>
<td>

### 🗄️ `storage/` — Multi-Backend Adapters
- `postgres_client.py` — Relational data & crawl state
- `clickhouse_client.py` — High-speed analytics & telemetry logs
- `graph_client.py` — Neo4j knowledge graph interface
- `qdrant_client.py` — Vector similarity search

</td>
<td>

### 📊 `dashboard/` — Live Console
Real-time browser dashboard monitoring:
- Crawler fleet health & throughput
- API endpoint statuses
- Pipeline stage latencies
- Error rates & retry queues

</td>
</tr>
</table>

---

## ⚡ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Browser Automation** | Playwright | Dynamic SPA rendering & crawling |
| **AI Vision Agent** | Vision-Language Models | Coordinate-based page interaction |
| **Mobile** | ADB + MediaCodec | Android screen capture & control |
| **Data Extraction** | BeautifulSoup, Requests | Static HTML parsing |
| **Stream Bus** | Apache Kafka | Raw payload ingestion pipeline |
| **Distributed Compute** | Ray | GPU-accelerated AI processing |
| **NLP / Embeddings** | spaCy, sentence-transformers | Entity extraction & vector generation |
| **Relational DB** | PostgreSQL | Crawl state & structured storage |
| **Analytical DB** | ClickHouse | Billions of event logs at query speed |
| **Vector DB** | Qdrant | Semantic similarity search |
| **Graph DB** | Neo4j | Knowledge graph & entity relations |
| **Orchestration** | Kubernetes + Helm | Auto-scaling container fleet |
| **IaC** | Terraform | Cloud infrastructure provisioning |
| **Language** | Python 3.10+ | Everything |

---

## 🚀 Getting Started

### Prerequisites

```
Python 3.10+   Docker & Docker Compose   Node.js (for dashboard)
```

### Quick Setup

```bash
# Clone
git clone https://github.com/tanayProbo/titan.git
cd titan

# Virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install

# Run the test suite
pytest titan/tests/ -v
```

### Run the Crawler

```python
from titan.core.crawler import TitanCrawler

crawler = TitanCrawler(
    concurrency=10,
    stealth_mode=True,
    proxy_rotation=True
)
crawler.run(start_urls=["https://example.com"])
```

### Run the Visual Agent

```python
from titan.visual_agent.agent_loop import VisualAgent

agent = VisualAgent(model="gpt-4o")
agent.navigate("https://example.com")
agent.act("Find the login button and click it")
```

---

## 📍 Roadmap

```
✅ Phase 1  —  Ingestion Core & Request Queuing
✅ Phase 2  —  API Interceptor & Free API Integration  
✅ Phase 3  —  Mobile ADB Agent & Visual DOM Planner
🚧 Phase 4  —  ClickHouse Analytics · Ray Embedders · Full Test Suite
🔜 Phase 5  —  Kubernetes Deployment & Helm Charts
🔜 Phase 6  —  Multi-region Crawler Fleet · LLM Extraction Endpoints
```

---

## 🔒 Security & Ethics

TITAN-X is designed to be **responsible by default**:

- 🤝 Automatically respects `robots.txt` and per-domain rate limits
- 🔐 HashiCorp Vault integration for secure credential management
- 🧹 Inline PII sanitization — strips phone numbers, emails, addresses from all outputs
- 🎭 Fingerprint spoofing stays within legal ethical scraping boundaries

---

## 📂 Repository Structure

```
titan/
├── core/                   # Crawler fleet & session management
│   ├── crawler.py
│   ├── browser_pool.py
│   ├── request_queue.py
│   └── session_pool.py
├── visual_agent/           # VLM-powered browser agent
│   ├── agent_loop.py
│   └── dom_parser.py
├── mobile/                 # Android ADB automation
│   ├── adb_client.py
│   ├── frame_decoder.py
│   └── inspector.py
├── api_intelligence/       # Live traffic interception
│   ├── proxy_sniffer.py
│   └── schema_generator.py
├── free_api_integration/   # Public API engine
│   ├── api_registry.py
│   ├── connector_generator.py
│   ├── health_monitor.py
│   ├── schema_detector.py
│   └── auto_doc.py
├── pipeline/               # AI processing pipeline
│   ├── cleaning.py
│   ├── entity_extractor.py
│   └── embedder.py
├── storage/                # Multi-backend DB adapters
│   ├── postgres_client.py
│   ├── clickhouse_client.py
│   ├── graph_client.py
│   └── qdrant_client.py
├── dashboard/              # Real-time monitoring UI
├── deployment/             # Helm charts & Terraform IaC
│   ├── helm/
│   └── terraform/
├── docs/
│   └── blueprint.md        # Full system design blueprint
└── tests/                  # Test suite
```

---

## 👤 Author

<div align="center">

**Tanay Praveen Agrawal**

*Built this entirely from scratch*

[![GitHub](https://img.shields.io/badge/GitHub-tanayProbo-181717?style=for-the-badge&logo=github)](https://github.com/tanayProbo)
[![Email](https://img.shields.io/badge/Email-tanayagrawal129@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:tanayagrawal129@gmail.com)

</div>

---

## 📜 License

```
MIT License — Copyright © 2026 Tanay Praveen Agrawal
```

Free to use, modify, and distribute with attribution. See [LICENSE](LICENSE).

---

<div align="center">
  <br/>
  <sub>⚡ Built for the future of AI data acquisition.</sub>
  <br/>
  <sub>If TITAN-X is useful to you, consider dropping a ⭐ — it means a lot.</sub>
  <br/><br/>
</div>

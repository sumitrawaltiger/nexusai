# NexusAI — Multi-Agent SaaS Platform

> **2,000 days · 20 skills · Day 1 = 25 Aug 2026 · Ends 14 Feb 2032**
>
> Built one commit per day. Every skill learned goes directly into this platform.

---

## Repository Structure

This repo has **two completely separate sections** that never mix:

```
nexusai/
│
├── practice/                  ← SECTION 1: Skill practice workspace
│   ├── 01-python/             (Days   1–100  · 25 Aug 2026 – 2 Dec 2026)
│   ├── 02-fastapi/            (Days 101–200  · 3 Dec 2026 – 12 Mar 2027)
│   ├── 03-agentic-ai/         (Days 201–300  · 13 Mar 2027 – 20 Jun 2027)
│   ├── 04-javascript/         (Days 301–400  · 21 Jun 2027 – 28 Sep 2027)
│   ├── 05-typescript/         (Days 401–500  · 29 Sep 2027 – 6 Jan 2028)
│   ├── 06-react-js/           (Days 501–600  · 7 Jan 2028 – 15 Apr 2028)
│   ├── 07-next-js/            (Days 601–700  · 16 Apr 2028 – 24 Jul 2028)
│   ├── 08-react-native/       (Days 701–800  · 25 Jul 2028 – 1 Nov 2028)
│   ├── 09-databases/          (Days 801–900  · 2 Nov 2028 – 9 Feb 2029)
│   ├── 10-express-js/         (Days 901–1000 · 10 Feb 2029 – 19 May 2029)
│   ├── 11-j2se/               (Days 1001–1100 · 20 May 2029 – 27 Aug 2029)
│   ├── 12-spring-boot/        (Days 1101–1200 · 28 Aug 2029 – 5 Dec 2029)
│   ├── 13-kafka/              (Days 1201–1300 · 6 Dec 2029 – 15 Mar 2030)
│   ├── 14-microservices/      (Days 1301–1400 · 16 Mar 2030 – 23 Jun 2030)
│   ├── 15-automation-testing/ (Days 1401–1500 · 24 Jun 2030 – 1 Oct 2030)
│   ├── 16-devops/             (Days 1501–1600 · 2 Oct 2030 – 9 Jan 2031)
│   ├── 17-aws/                (Days 1601–1700 · 10 Jan 2031 – 19 Apr 2031)
│   ├── 18-sre/                (Days 1701–1800 · 20 Apr 2031 – 28 Jul 2031)
│   ├── 19-system-design/      (Days 1801–1900 · 29 Jul 2031 – 5 Nov 2031)
│   └── 20-dsa/                (Days 1901–2000 · 6 Nov 2031 – 14 Feb 2032)
│
└── project/                   ← SECTION 2: Actual NexusAI platform
    ├── agent-api/             FastAPI — Agent Orchestration API
    ├── agents/                LangChain · LangGraph · MCP agent library
    ├── sdk/                   TypeScript SDK (npm install nexusai)
    ├── dashboard/             React JS — web dashboard
    ├── marketing/             Next JS — public site + docs
    ├── mobile/                React Native — iOS + Android app
    ├── gateway/               Express JS — API Gateway + webhooks
    ├── java-backend/          Spring Boot — billing, users, subscriptions
    ├── db/                    Migrations, schemas, seed scripts
    ├── infra/
    │   ├── docker/            Dockerfiles for every service
    │   ├── helm/              Kubernetes Helm charts
    │   └── ci/                GitHub Actions workflows
    └── docs/                  Architecture decisions (ADRs), diagrams
```

---

## Section 1 — Practice

`practice/` is a **scratch workspace**. Raw exercises, tutorials, and experiments from each 100-day skill block. Code here is written to learn, not to ship. It can be messy. It's purely for building muscle memory.

**Rule:** nothing from `practice/` ever gets imported into `project/`. They are isolated.

Each skill folder contains day-by-day work files, e.g.:

```
practice/01-python/
├── day001-variables-loops.py
├── day002-functions-scope.py
├── day003-oop-classes.py
├── day010-file-io.py
├── day025-async-await.py
└── day100-final-project/
```

---

## Section 2 — Actual Project

`project/` is the **real NexusAI platform** — production-grade code built skill by skill as each phase is completed. Every service here is deployable.

### What is NexusAI?

A **multi-agent AI SaaS platform** that lets businesses deploy, orchestrate, and monitor intelligent AI agents for any workflow — customer support, data analysis, document processing, code review, sales outreach, and more.

Instead of one big model doing everything, NexusAI breaks business problems into specialised agents that collaborate: one agent researches, one writes, one reviews, one sends — all orchestrated by a central supervisor.

**The core promise:** any business, any workflow, AI agents working on it 24/7.

---

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        NexusAI Platform                         │
│                                                                  │
│  ┌──────────────┐    ┌───────────────────┐    ┌──────────────┐  │
│  │  React JS    │    │  React Native App │    │  Next JS     │  │
│  │  Dashboard   │    │  iOS + Android    │    │  Marketing   │  │
│  └──────┬───────┘    └────────┬──────────┘    └──────┬───────┘  │
│         └────────────────────┼───────────────────────┘           │
│                              │  REST / WebSocket                  │
│                    ┌─────────▼──────────┐                        │
│                    │   API Gateway       │                        │
│                    │   (Express JS)      │                        │
│                    └─────────┬──────────┘                        │
│         ┌────────────────────┼────────────────────┐              │
│  ┌──────▼──────┐   ┌────────▼───────┐   ┌───────▼──────┐       │
│  │ Agent       │   │ User & Billing  │   │ Analytics    │       │
│  │ Orchestrator│   │ (Spring Boot)   │   │ (Spring Boot)│       │
│  │ (FastAPI +  │   └────────────────┘   └──────────────┘       │
│  │  LangGraph) │                                                │
│  └──────┬──────┘                                                │
│  ┌──────▼──────────────────────────────────────────┐            │
│  │         Agent Runtime · LangChain · MCP          │            │
│  │  Researcher · Writer · Reviewer · Mailer agents  │            │
│  └──────────────────────────────────────────────────┘            │
│  ┌──────────────────────────────────────────────────┐            │
│  │  PostgreSQL · MongoDB · Redis · pgvector · S3    │            │
│  └──────────────────────────────────────────────────┘            │
│  ┌──────────────────────────────────────────────────┐            │
│  │  AWS EKS · RDS · ElastiCache · MSK · CloudFront  │            │
│  └──────────────────────────────────────────────────┘            │
└─────────────────────────────────────────────────────────────────┘
```

---

### How the Project Gets Built — Phase by Phase

Each skill phase adds one production layer to `project/`. Nothing sits idle.

| Phase | Skill | What gets added to `project/` |
|---|---|---|
| 1 | Python | `agents/` core utilities — text chunking, token counting, prompt helpers |
| 2 | FastAPI | `agent-api/` — REST + WebSocket API for agent execution |
| 3 | Agentic AI | `agents/` — LangGraph multi-agent pipelines, RAG, MCP tool calling |
| 4–5 | JS + TS | `sdk/` — typed npm package, CLI tool, webhook listener |
| 6 | React JS | `dashboard/` — web UI with live agent run streaming |
| 7 | Next JS | `marketing/` — landing page, pricing, MDX docs |
| 8 | React Native | `mobile/` — voice-to-agent, push notifications, camera input |
| 9 | Databases | `db/` — migrations, indexes, pgvector embeddings, Redis queues |
| 10 | Express JS | `gateway/` — API gateway, rate limiting, webhook relay |
| 11–12 | J2SE + Spring Boot | `java-backend/` — billing engine, user management, subscriptions (Spring Data JPA + Hibernate included) |
| 13 | Kafka | `java-backend/` — Kafka producers/consumers, event-driven billing events, Spring Kafka integration |
| 14 | Microservices | `java-backend/` split into 5 services, CQRS + event sourcing on top of Kafka |
| 15 | Automation Testing | `project/` — full test suite across all services |
| 16 | DevOps | `infra/docker/` + `infra/ci/` — Dockerfiles, GitHub Actions pipelines |
| 17 | AWS | `infra/helm/` — EKS deploy, RDS, ElastiCache, CloudFront, Route 53 |
| 18 | SRE | Prometheus + Grafana + SLOs + incident runbooks |
| 19 | System Design | Architecture review, ADRs, capacity planning docs |
| 20 | DSA | Performance optimisations applied across all services |

---

### Database Strategy

| Database | Role | Why |
|---|---|---|
| **PostgreSQL** | Users, teams, billing, subscriptions, run metadata | ACID guarantees for financial and user data |
| **MongoDB** | Agent run outputs, prompt/response pairs | Variable-length JSON — schemaless fits agent outputs perfectly |
| **Redis** | Session cache, rate limiting, Celery task queue, pub/sub | Sub-millisecond reads; async job queue for agent runs |
| **pgvector** | Long-term agent memory, RAG document embeddings | Vectors alongside relational data — no sync overhead |
| **S3** | User uploads, audio files, agent output files | Cheap, durable blob storage |

---

### AWS + Kubernetes Deployment

```
AWS Account
├── VPC (private subnets for services, public for ALB)
├── EKS — all services run as pods, auto-scaled by HPA
│   ├── agent-api pods      (FastAPI — scales on CPU)
│   ├── user-service pods   (Spring Boot)
│   ├── billing-service pods
│   ├── analytics-service pods
│   ├── gateway pods        (Express JS)
│   └── dashboard pods      (React, served via Nginx)
├── RDS PostgreSQL          (Multi-AZ, automated backups)
├── ElastiCache Redis       (cluster mode)
├── DocumentDB              (MongoDB-compatible)
├── MSK Kafka               (managed, multi-AZ)
├── S3                      (user uploads, static assets)
├── ECR                     (Docker image registry)
├── ALB                     (routes to EKS ingress)
├── CloudFront              (CDN for dashboard + marketing)
├── Route 53                (nexusai.io, app.nexusai.io, api.nexusai.io)
└── CloudWatch              (logs, metrics, alarms)
```

---

### System Design & DSA

**System Design** shapes every architectural decision throughout the 2,000 days:

| Decision | Concept |
|---|---|
| PostgreSQL + MongoDB + Redis instead of one DB | Polyglot persistence |
| Async agent runs via Celery + Kafka | Message queues, backpressure |
| Dashboard streams agent output live | WebSockets, fan-out |
| Billing service decoupled from agent service | Event-driven, eventual consistency |
| EKS auto-scales agent pods | Stateless design, horizontal scaling |
| Rate limiting on the API Gateway | Token bucket, Redis sliding window |

**DSA** directly improves the platform:

| DSA Topic | Where it appears |
|---|---|
| Graphs / BFS | LangGraph agent DAG traversal |
| Heaps | Agent job scheduler — priority queue per subscription tier |
| Hash Maps | Tool registry, API key lookup, rate limit counters |
| Sliding Window | Token budget tracking across conversation windows |
| Tries | Autocomplete in the agent builder |
| Binary Search | Time-range queries on run history logs |

---

## Daily Commit Discipline

- **1 commit per day** from Day 1 — either to `practice/` or `project/` (or both)
- **1 LeetCode problem per day** — 2,000 problems by Day 2,000 (13 Feb 2032)

## Study Routine

`4:00 AM wake → 4:00–4:30 AM fresh up → 4:30–7:30 AM IST study (3 hrs/day)`

---

Built by [Sumit Rawal](https://github.com/sumitrawaltiger) · Day 0: 24 Aug 2026

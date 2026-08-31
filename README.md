# NexusAI — Multi-Agent SaaS Platform

> **2,008 days · 6 phases · Day 1 = 1 Sep 2026 · Ends 29 Feb 2032**
>
> Built one commit per day. Every skill learned goes directly into this platform.

---

## Repository Structure

This repo has **two completely separate sections** that never mix:

```
nexusai/
│
├── practice/                    ← SECTION 1: Skill practice workspace
│   ├── 01-agentic-ai/           (Days    1–181  · 1 Sep 2026 – 28 Feb 2027)
│   ├── 02-typescript-stack/     (Days  182–731  · 1 Mar 2027 – 31 Aug 2028)
│   ├── 03-java-stack/           (Days  732–1096 · 1 Sep 2028 – 31 Aug 2029)
│   ├── 04-databases/            (Days 1097–1277 · 1 Sep 2029 – 28 Feb 2030)
│   ├── 05-devops-cloud/         (Days 1278–1642 · 1 Mar 2030 – 28 Feb 2031)
│   └── 06-interview-prep/       (Days 1643–2008 · 1 Mar 2031 – 29 Feb 2032)
│
└── project/                     ← SECTION 2: Actual NexusAI platform
    ├── agent-api/               FastAPI — Agent Orchestration API
    ├── agents/                  LangChain · LangGraph · MCP agent library
    ├── sdk/                     TypeScript SDK (npm install nexusai)
    ├── dashboard/               React JS — web dashboard
    ├── marketing/               Next JS — public site + docs
    ├── mobile/                  React Native — iOS + Android app
    ├── gateway/                 Express JS — API Gateway + webhooks
    ├── java-backend/            Spring Boot — billing, users, subscriptions
    ├── db/                      Migrations, schemas, seed scripts
    ├── infra/
    │   ├── docker/              Dockerfiles for every service
    │   ├── helm/                Kubernetes Helm charts
    │   └── ci/                  GitHub Actions workflows
    └── docs/                    Architecture decisions (ADRs), diagrams
```

---

## Section 1 — Practice

`practice/` is a **scratch workspace**. Raw exercises, tutorials, and experiments from each phase. Code here is written to learn, not to ship. It can be messy. It's purely for building muscle memory.

**Rule:** nothing from `practice/` ever gets imported into `project/`. They are isolated.

Each phase folder contains day-by-day work files, e.g.:

```
practice/01-agentic-ai/
├── day001-python-syntax.py
├── day002-oop-classes.py
├── day010-fastapi-basics.py
├── day025-langchain-intro.py
├── day050-rag-pipeline.py
└── day181-nexusai-agent-v1/
```

---

## Section 2 — Actual Project

`project/` is the **real NexusAI platform** — production-grade code built phase by phase as each skill is completed. Every service here is deployable.

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

Each phase adds one production layer to `project/`. Nothing sits idle.

| Phase | Period | What gets added to `project/` |
|---|---|---|
| **P1 · Agentic AI** | Days 1–181 · Sep 2026 – Feb 2027 | `agents/` — LangGraph multi-agent pipelines, RAG, MCP tool calling, CrewAI crews · `agent-api/` — FastAPI REST + WebSocket execution API |
| **P2 · TypeScript Full Stack** | Days 182–731 · Mar 2027 – Aug 2028 | `sdk/` — typed npm package + CLI · `dashboard/` — React web UI with live agent streaming · `marketing/` — Next.js landing page + MDX docs · `mobile/` — React Native iOS/Android app · `gateway/` — Express API gateway, rate limiting, webhooks |
| **P3 · Java Stack** | Days 732–1096 · Sep 2028 – Aug 2029 | `java-backend/` — Spring Boot billing, user management, subscriptions · Kafka producers/consumers for event-driven billing · microservices split with CQRS + event sourcing |
| **P4 · Databases** | Days 1097–1277 · Sep 2029 – Feb 2030 | `db/` — migrations, indexes, pgvector embeddings for long-term agent memory, Redis queues, MongoDB agent output schemas |
| **P5 · DevOps + Cloud** | Days 1278–1642 · Mar 2030 – Feb 2031 | `infra/docker/` — Dockerfiles for every service · `infra/ci/` — GitHub Actions pipelines · `infra/helm/` — EKS deploy, RDS, ElastiCache, CloudFront, Route 53 · Prometheus + Grafana + SLOs |
| **P6 · Interview Prep** | Days 1643–2008 · Mar 2031 – Feb 2032 | Performance optimisations (DSA applied across services) · Architecture review · ADRs · capacity planning docs |

---

### Database Strategy

| Database | Role | Why |
|---|---|---|
| **PostgreSQL** | Users, teams, billing, subscriptions, run metadata | ACID guarantees for financial and user data |
| **MongoDB** | Agent run outputs, prompt/response pairs | Variable-length JSON — schemaless fits agent outputs perfectly |
| **Redis** | Session cache, rate limiting, task queue, pub/sub | Sub-millisecond reads; async job queue for agent runs |
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

**System Design** shapes every architectural decision throughout all 2,008 days:

| Decision | Concept |
|---|---|
| PostgreSQL + MongoDB + Redis instead of one DB | Polyglot persistence |
| Async agent runs via Kafka | Message queues, backpressure |
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

## The 6-Phase Journey

| Phase | Days | Duration | Period | Stack |
|---|---|---|---|---|
| P1 · Agentic AI | 1–181 | 6 months | 1 Sep 2026 – 28 Feb 2027 | Python · FastAPI · LangChain · LangGraph · RAG · MCP · CrewAI |
| P2 · TypeScript Full Stack | 182–731 | 18 months | 1 Mar 2027 – 31 Aug 2028 | JS · TS · React · Next.js · React Native · Express · GraphQL · Playwright |
| P3 · Java Stack | 732–1096 | 12 months | 1 Sep 2028 – 31 Aug 2029 | J2SE · Spring Boot · Kafka · Microservices · Automation Testing |
| P4 · Databases | 1097–1277 | 6 months | 1 Sep 2029 – 28 Feb 2030 | PostgreSQL · MySQL · MongoDB · Redis · pgvector |
| P5 · DevOps + Cloud | 1278–1642 | 12 months | 1 Mar 2030 – 28 Feb 2031 | Docker · Kubernetes CKA · AWS · CI/CD · SRE · GitOps |
| P6 · Interview Prep | 1643–2008 | ~12 months | 1 Mar 2031 – 29 Feb 2032 | DSA Striver A2Z · NeetCode 150 · System Design HLD/LLD · 200+ mocks |

---

## Daily Commit Discipline

- **1 commit per day** from Day 1 — either to `practice/` or `project/` (or both)
- **1 LeetCode problem per day** — 2,000 problems by Day 2,000 (21 Feb 2032)

## Study Routine

`4:00 AM wake → 4:30–5:00 AM meditation → 5:00–8:00 AM IST study (3 hrs/day, 7 days/week)`

---

Built by [Sumit Rawal](https://github.com/sumitrawaltiger) · Day 0: 31 Aug 2026

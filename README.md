# NexusAI — Multi-Agent SaaS Platform

> **2,000 days · 20 skills · Day 0 = 8 Sep 2026 · Day 1 = 9 Sep 2026 · Ends 29 Feb 2032**
>
> Built one commit per day. Every skill learned goes directly into this platform.

---

## Repository Structure

This repo has **two completely separate sections** that never mix:

```
nexusai/
│
├── practice/                    ← SECTION 1: Skill practice workspace
│   ├── 01-python-fastapi/       (Days   1–100  · 9 Sep 2026 – 17 Dec 2026)
│   ├── 02-agentic-ai/           (Days 101–200  · 18 Dec 2026 – 27 Mar 2027)
│   ├── 03-javascript/           (Days 201–300  · 28 Mar 2027 – 5 Jul 2027)
│   ├── 04-typescript/           (Days 301–400  · 6 Jul 2027 – 13 Oct 2027)
│   ├── 05-react-js/             (Days 401–500  · 14 Oct 2027 – 21 Jan 2028)
│   ├── 06-next-js/              (Days 501–600  · 22 Jan 2028 – 30 Apr 2028)
│   ├── 07-react-native/         (Days 601–700  · 1 May 2028 – 8 Aug 2028)
│   ├── 08-express-js/           (Days 701–800  · 9 Aug 2028 – 16 Nov 2028)
│   ├── 09-playwright/           (Days 801–900  · 17 Nov 2028 – 24 Feb 2029)
│   ├── 10-databases/            (Days 901–1000 · 25 Feb 2029 – 4 Jun 2029)
│   ├── 11-j2se/                 (Days 1001–1100 · 5 Jun 2029 – 12 Sep 2029)
│   ├── 12-spring-boot/          (Days 1101–1200 · 13 Sep 2029 – 21 Dec 2029)
│   ├── 13-kafka/                (Days 1201–1300 · 22 Dec 2029 – 31 Mar 2030)
│   ├── 14-microservices/        (Days 1301–1400 · 1 Apr 2030 – 9 Jul 2030)
│   ├── 15-automation-testing/   (Days 1401–1500 · 10 Jul 2030 – 17 Oct 2030)
│   ├── 16-devops/               (Days 1501–1600 · 18 Oct 2030 – 25 Jan 2031)
│   ├── 17-aws/                  (Days 1601–1700 · 26 Jan 2031 – 5 May 2031)
│   ├── 18-sre/                  (Days 1701–1800 · 6 May 2031 – 13 Aug 2031)
│   ├── 19-system-design/        (Days 1801–1900 · 14 Aug 2031 – 21 Nov 2031)
│   └── 20-dsa/                  (Days 1901–2000 · 22 Nov 2031 – 29 Feb 2032)
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

`practice/` is a **scratch workspace**. Raw exercises, tutorials, and experiments from each skill. Code here is written to learn, not to ship. It can be messy. It's purely for building muscle memory.

**Rule:** nothing from `practice/` ever gets imported into `project/`. They are isolated.

Each skill folder contains day-by-day work files, e.g.:

```
practice/01-python-fastapi/
├── day001-python-syntax.py
├── day010-oop-classes.py
├── day050-fastapi-basics.py
└── day100-rest-api-project/
```

---

## Section 2 — Actual Project

`project/` is the **real NexusAI platform** — production-grade code built skill by skill as each is completed. Every service here is deployable.

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

### How the Project Gets Built — Skill by Skill

Each skill block adds one production layer to `project/`. Nothing sits idle.

| Skill | Period | What gets added to `project/` |
|---|---|---|
| **01 · Python + FastAPI** | Days 1–100 · Sep–Dec 2026 | `agent-api/` — FastAPI REST + WebSocket execution API |
| **02 · Agentic AI** | Days 101–200 · Dec 2026 – Mar 2027 | `agents/` — LangGraph multi-agent pipelines, RAG, MCP tool calling, CrewAI crews · NexusAI v1 |
| **03 · JavaScript** | Days 201–300 · Mar–Jul 2027 | JS fundamentals applied to `dashboard/` utilities and `sdk/` helpers |
| **04 · TypeScript** | Days 301–400 · Jul–Oct 2027 | `sdk/` — typed npm package + CLI fully in TypeScript |
| **05 · React JS** | Days 401–500 · Oct 2027 – Jan 2028 | `dashboard/` — React web UI with live agent streaming |
| **06 · Next JS** | Days 501–600 · Jan–Apr 2028 | `marketing/` — Next.js landing page + MDX docs |
| **07 · React Native** | Days 601–700 · May–Aug 2028 | `mobile/` — React Native iOS + Android app |
| **08 · Express JS** | Days 701–800 · Aug–Nov 2028 | `gateway/` — Express API gateway, rate limiting, webhooks |
| **09 · Playwright** | Days 801–900 · Nov 2028 – Feb 2029 | E2E tests across `dashboard/`, `marketing/`, `gateway/` — CI green gate |
| **10 · Databases** | Days 901–1000 · Feb–Jun 2029 | `db/` — migrations, indexes, pgvector embeddings, Redis queues, MongoDB schemas |
| **11 · J2SE** | Days 1001–1100 · Jun–Sep 2029 | Java fundamentals applied to `java-backend/` foundations |
| **12 · Spring Boot** | Days 1101–1200 · Sep–Dec 2029 | `java-backend/` — Spring Boot billing, user management, subscriptions |
| **13 · Kafka** | Days 1201–1300 · Dec 2029 – Mar 2030 | Kafka producers/consumers for event-driven billing across services |
| **14 · Microservices** | Days 1301–1400 · Apr–Jul 2030 | Microservices split with CQRS + event sourcing + Saga pattern |
| **15 · Automation Testing** | Days 1401–1500 · Jul–Oct 2030 | Full JUnit 5 + Mockito + Testcontainers test suite across all Java services |
| **16 · DevOps** | Days 1501–1600 · Oct 2030 – Jan 2031 | `infra/docker/` — Dockerfiles · `infra/ci/` — GitHub Actions pipelines · Helm charts |
| **17 · AWS** | Days 1601–1700 · Jan–May 2031 | EKS deploy, RDS, ElastiCache, CloudFront, Route 53 · full production deployment |
| **18 · SRE** | Days 1701–1800 · May–Aug 2031 | Prometheus + Grafana + SLOs · incident runbooks · capacity planning |
| **19 · System Design** | Days 1801–1900 · Aug–Nov 2031 | ADRs for every key architecture decision · diagrams · 50+ case study annotations |
| **20 · DSA** | Days 1901–2000 · Nov 2031 – Feb 2032 | Performance optimisations applied across services · portfolio polish · 200+ mock interviews |

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

## The 20-Skill Journey

| Skill | Days | Period | Technologies |
|---|---|---|---|
| 01 · Python + FastAPI | 1–100 | 9 Sep – 17 Dec 2026 | Python · FastAPI · OOP · async · REST APIs |
| 02 · Agentic AI | 101–200 | 18 Dec 2026 – 27 Mar 2027 | LangChain · LangGraph · RAG · MCP · CrewAI · n8n |
| 03 · JavaScript | 201–300 | 28 Mar – 5 Jul 2027 | DOM · async/await · closures · ES6+ · event loop |
| 04 · TypeScript | 301–400 | 6 Jul – 13 Oct 2027 | types · interfaces · generics · enums · decorators |
| 05 · React JS | 401–500 | 14 Oct 2027 – 21 Jan 2028 | hooks · context · React Router · Redux Toolkit |
| 06 · Next JS | 501–600 | 22 Jan – 30 Apr 2028 | App Router · server components · server actions · Vercel |
| 07 · React Native | 601–700 | 1 May – 8 Aug 2028 | Expo · React Navigation · Reanimated · EAS |
| 08 · Express JS | 701–800 | 9 Aug – 16 Nov 2028 | middleware · JWT auth · Prisma ORM · WebSockets |
| 09 · Playwright | 801–900 | 17 Nov 2028 – 24 Feb 2029 | E2E tests · page object model · API mocking · CI |
| 10 · Databases | 901–1000 | 25 Feb – 4 Jun 2029 | PostgreSQL · MySQL · MongoDB · Redis · pgvector |
| 11 · J2SE | 1001–1100 | 5 Jun – 12 Sep 2029 | Core Java · OOP · collections · streams · Java 17 |
| 12 · Spring Boot | 1101–1200 | 13 Sep – 21 Dec 2029 | Spring Data JPA · Hibernate · Spring Security · Cloud |
| 13 · Kafka | 1201–1300 | 22 Dec 2029 – 31 Mar 2030 | topics · partitions · consumer groups · Spring Kafka |
| 14 · Microservices | 1301–1400 | 1 Apr – 9 Jul 2030 | CQRS · event sourcing · Saga · service mesh · tracing |
| 15 · Automation Testing | 1401–1500 | 10 Jul – 17 Oct 2030 | JUnit 5 · Mockito · Testcontainers · REST-assured |
| 16 · DevOps | 1501–1600 | 18 Oct 2030 – 25 Jan 2031 | Docker · Kubernetes · Helm · ArgoCD · Terraform |
| 17 · AWS | 1601–1700 | 26 Jan – 5 May 2031 | AWS SAA · EKS · RDS · CloudFront · CKA |
| 18 · SRE | 1701–1800 | 6 May – 13 Aug 2031 | Prometheus · Grafana · SLO/SLA/SLI · incident response |
| 19 · System Design | 1801–1900 | 14 Aug – 21 Nov 2031 | HLD/LLD · CAP theorem · 50+ case studies |
| 20 · DSA | 1901–2000 | 22 Nov 2031 – 29 Feb 2032 | Striver A2Z · NeetCode 150 · 200+ mock interviews |

---

## Daily Commit Discipline

- **1 commit per day** from Day 1 — either to `practice/` or `project/` (or both)
- **1 LeetCode problem per day** — 2,000 problems by Day 2,000 (29 Feb 2032)

## Study Routine

`4:00 AM wake → 4:30–5:00 AM meditation → 5:00–8:00 AM IST study (3 hrs/day, 7 days/week)`

---

Built by [Sumit Rawal](https://github.com/sumitrawaltiger) · Day 0: 8 Sep 2026

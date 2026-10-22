# LeadFinder

> **Lead discovery and qualification pipeline for local businesses.**

LeadFinder is a data collection and lead qualification tool designed to discover potential customers by **location and business niche**, enrich the collected information, remove duplicates, and prioritize the resulting leads.

The current implementation uses **OpenStreetMap through the Overpass API** as its primary data source. The architecture is designed to support additional providers, with **2GIS** planned as the next data source.

---

## ✨ Overview

Finding relevant businesses manually is slow and often produces incomplete or inconsistent data.

LeadFinder automates this process by turning geographic business data into a structured list of potential leads.

The pipeline combines:

- 🔎 **Business discovery**
- 📍 **Location-based search**
- 🧹 **Data normalization**
- ♻️ **Duplicate detection**
- 🌐 **Website availability checks**
- 📊 **Lead scoring**
- 🏷️ **Lead prioritization**
- 📦 **Structured data export**

The goal is not simply to collect as many businesses as possible, but to produce a **clean, usable, and prioritized lead database**.

---

## 🏗️ Architecture

LeadFinder follows a source-independent processing pipeline:

```text
                    ┌──────────────────┐
                    │   Data Sources   │
                    ├──────────────────┤
                    │ OpenStreetMap    │
                    │  / Overpass      │
                    │                  │
                    │     2GIS         │
                    │    (planned)     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │     Parsing      │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Lead Model      │
                    │  Normalization   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Deduplication   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Website Checks   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    Lead Score    │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Classification  │
                    │ HOT / WARM / COLD│
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │      Export      │
                    │   CSV / JSON     │
                    └──────────────────┘
```

A key design principle is that **data sources are separated from the rest of the processing pipeline**.

This makes it possible to add new providers without duplicating the business logic responsible for cleaning, scoring, and exporting leads.

---

## 🔎 Data Sources

### OpenStreetMap / Overpass

OpenStreetMap is currently the primary source of business and geographic data.

The Overpass API is used to query relevant objects based on:

- geographic area;
- business category;
- available tags;
- location-related criteria.

The raw response is transformed into LeadFinder's internal lead model before entering the rest of the pipeline.

### 2GIS

**2GIS is planned as the next major data source.**

The intention is to use 2GIS alongside OpenStreetMap rather than replacing the existing provider.

Both sources will ultimately feed into the same internal model:

```text
OpenStreetMap ──┐
                ├──► Unified Lead Model ──► Processing
2GIS ───────────┘
```

This allows LeadFinder to combine information from multiple providers while keeping the rest of the system source-independent.

---

## 🧩 Core Components

### Source Layer

Responsible for communicating with external data providers.

Each provider is treated as an independent source and is responsible only for obtaining source-specific data.

This keeps provider-specific logic isolated from the rest of the application.

---

### Parser

Transforms raw provider responses into LeadFinder's internal representation.

The parser hides differences between external APIs and ensures that downstream components work with a consistent data structure.

---

### Lead Model

The Lead Model is the central data structure used throughout the pipeline.

A lead may contain:

- Business name
- Category
- Address
- City
- Phone number
- Website
- Geographic coordinates
- Source
- Source identifier
- Website status
- Additional metadata
- Lead score
- Lead priority

Not every source provides every field, so missing information is handled gracefully.

---

### Normalization

Raw business data often contains inconsistencies.

The normalization layer standardizes information such as:

- business names;
- addresses;
- phone numbers;
- URLs;
- categories;
- geographic information.

Normalized data makes subsequent deduplication, filtering, and scoring more reliable.

---

### Deduplication

The same organization may appear multiple times in source data.

LeadFinder identifies likely duplicates and consolidates them into unique leads.

This is particularly important when multiple sources are introduced, since the same business may exist in both OpenStreetMap and 2GIS.

The deduplication layer therefore becomes a key part of the multi-source architecture.

---

### Website Validation

When a lead contains a website, LeadFinder can perform an additional validation step.

The purpose is to determine whether the website is reachable and to collect useful signals for subsequent lead qualification.

Website checks are isolated from the main discovery process so that an unavailable or problematic website does not interrupt processing of the entire dataset.

Independent website checks can also be processed concurrently to improve overall throughput.

---

## 📊 Lead Scoring

LeadFinder goes beyond simple data collection by assigning a **score** to potential leads.

The score represents the overall quality or potential value of a lead based on the information available during processing.

Leads can then be grouped into priority levels:

| Priority | Meaning |
|---|---|
| 🔥 **HOT** | High-priority potential lead |
| 🟡 **WARM** | Potentially valuable lead |
| 🔵 **COLD** | Lower-priority lead |

This allows the final dataset to be sorted by relevance instead of treating every discovered business equally.

---

## 🔄 Processing Pipeline

The complete processing flow can be summarized as:

```text
Discover
   ↓
Parse
   ↓
Normalize
   ↓
Deduplicate
   ↓
Validate
   ↓
Score
   ↓
Classify
   ↓
Filter
   ↓
Export
```

Each stage has a clearly defined responsibility, making the system easier to extend and maintain.

---

## 🚀 Multi-Source Strategy

The long-term architecture is built around multiple independent data providers.

The current direction is:

```text
                 ┌─────────────────┐
                 │  OpenStreetMap  │
                 │    Overpass     │
                 └────────┬────────┘
                          │
                          ▼
                    ┌───────────┐
                    │           │
                    │   Lead    │
                    │  Finder   │
                    │           │
                    └─────┬─────┘
                          ▲
                          │
                 ┌────────┴────────┐
                 │      2GIS       │
                 │    Planned     │
                 └─────────────────┘
```

Adding another provider should only require implementing the provider-specific acquisition and parsing layer.

The rest of the pipeline remains shared.

This makes the system suitable for gradually expanding the number of available data sources without turning the application into a collection of source-specific implementations.

---

## 📦 Output

LeadFinder produces structured lead datasets suitable for further analysis and downstream processing.

Supported output formats include:

### CSV

Designed for:

- spreadsheet analysis;
- manual review;
- filtering and sorting;
- CRM preparation.

### JSON

Designed for:

- programmatic processing;
- integrations;
- downstream automation;
- preserving structured metadata.

---

## 🎯 Project Goals

LeadFinder is designed around four main objectives:

**1. Discover**

Find businesses matching a specific location and niche.

**2. Clean**

Turn inconsistent source data into a unified and structured dataset.

**3. Qualify**

Use available information to determine which businesses are more valuable potential leads.

**4. Prioritize**

Give users a practical shortlist instead of an unfiltered database.

---

## 🛣️ Roadmap

### Current

- [x] OpenStreetMap integration
- [x] Overpass-based discovery
- [x] Unified lead representation
- [x] Data normalization
- [x] Deduplication
- [x] Website validation
- [x] Lead scoring
- [x] Lead prioritization
- [x] CSV / JSON output

### Planned

- [ ] 2GIS integration
- [ ] Cross-source deduplication
- [ ] Improved multi-source enrichment
- [ ] Additional lead-quality signals
- [ ] Support for additional business data providers

---

## 💡 Design Philosophy

LeadFinder is intentionally built as a **pipeline rather than a single scraper**.

The distinction is important.

A scraper only answers:

> *"What businesses can I find?"*

LeadFinder aims to answer:

> *"What businesses can I find, which ones are unique, what information do I have about them, and which ones are worth looking at first?"*

This separation between **discovery, processing, enrichment, and qualification** is the foundation of the project's architecture.
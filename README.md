<div align="center">
    
**System/Software Architect | Full-Stack Developer | Taiwan**

[![Email](https://img.shields.io/badge/Email-jr.johnchang%40gmail.com-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:jr.johnchang@gmail.com)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0008--6249--1470-A6CE39?style=flat&logo=orcid&logoColor=white)](https://orcid.org/0009-0008-6249-1470)

*Building enterprise-grade applications with Clean Architecture design*

</div>

---

## 🏗️ Arcana Architecture Suite

A comprehensive collection of enterprise-grade reference architectures implementing **Clean Architecture**, **Offline-First** design, and **MVVM patterns** across multiple platforms.

```mermaid
flowchart TB
    subgraph Client["📱 Client Applications"]
        direction LR
        subgraph Mobile["Mobile"]
            iOS["🍎 iOS<br>SwiftUI + SwiftData"]
            Android["🤖 Android<br>Jetpack Compose"]
            HarmonyOS["🔷 HarmonyOS<br>ArkTS + ArkUI"]
        end
        subgraph Web["Web"]
            Angular["🅰️ Angular<br>Signals + RxJS"]
            React["⚛️ React<br>Hooks + Zustand"]
            Vue["💚 Vue<br>Composition API"]
        end
        subgraph Embedded["Embedded"]
            Embedded1["🔧 IoT Devices"]
        end
    end

    subgraph Cloud["☁️ Cloud Services"]
        direction LR
        SpringBoot["☕ Spring Boot<br>gRPC + REST + OSGi"]
        Python["🐍 Python<br>Flask + gRPC"]
        Go["🐹 Go<br>High Performance"]
        Rust["🦀 Rust<br>Memory Safety"]
        NodeJS["💚 Node.js<br>Express + Prisma"]
    end

    subgraph Core["🎯 Core Principles"]
        CA["Clean Architecture"]
        OF["Offline-First"]
        MVVM["MVVM I/O/E Pattern"]
    end

    Mobile --> Cloud
    Web --> Cloud
    Embedded --> Cloud
    Cloud --> Core
```

---

## 📱 Mobile Development

| Platform | Repository | Tech Stack | Description |
|:--------:|:-----------|:-----------|:------------|
| 🍎 | [**arcana-ios**](https://github.com/jrjohn/arcana-ios) | Swift, SwiftUI, SwiftData | Clean Architecture with Offline-First design and Analytics Tracking |
| 🤖 | [**arcana-android**](https://github.com/jrjohn/arcana-android) | Kotlin, Jetpack Compose, Hilt | Clean Architecture with Offline-First design and AOP Analytics |
| 🔷 | [**arcana-harmonyos**](https://github.com/jrjohn/arcana-harmonyos) | ArkTS, ArkUI | HarmonyOS NEXT application with Clean Architecture |

---

## 🌐 Web Development

| Framework | Repository | Tech Stack | Description |
|:---------:|:-----------|:-----------|:------------|
| 🅰️ | [**arcana-angular**](https://github.com/jrjohn/arcana-angular) | TypeScript, Angular, Signals | Production-ready with Offline-First capabilities and Enterprise Security |
| ⚛️ | [**arcana-react**](https://github.com/jrjohn/arcana-react) | TypeScript, React 19, Zustand | Enterprise-grade with MVVM Input/Output/Effect pattern |
| 💚 | [**arcana-vue**](https://github.com/jrjohn/arcana-vue) | TypeScript, Vue 3, Pinia | Modern Vue application with Composition API |

---

## ☁️ Cloud Services

| Language | Repository | Tech Stack | Description |
|:--------:|:-----------|:-----------|:------------|
| ☕ | [**arcana-cloud-springboot**](https://github.com/jrjohn/arcana-cloud-springboot) | Java, Spring Boot, gRPC | Dual-protocol (gRPC 2.5x faster), OSGi Plugin System, GraalJS SSR |
| 🐍 | [**arcana-cloud-python**](https://github.com/jrjohn/arcana-cloud-python) | Python, Flask, gRPC | gRPC-first architecture (2.78x faster), flexible deployment modes |
| 🐹 | [**arcana-cloud-go**](https://github.com/jrjohn/arcana-cloud-go) | Go, Gin/Fiber, gRPC | High-performance microservices with native concurrency |
| 🦀 | [**arcana-cloud-rust**](https://github.com/jrjohn/arcana-cloud-rust) | Rust, Actix/Axum | High-performance cloud services with memory safety |
| 💚 | [**arcana-cloud-nodejs**](https://github.com/jrjohn/arcana-cloud-nodejs) | Node.js, Express, Prisma | InversifyJS DI, gRPC-first (1.80x faster), dual-protocol support |

---

## 🔧 Embedded Systems

| Platform | Repository | Description |
|:--------:|:-----------|:------------|
| 🔌 | *Coming Soon* | IoT and embedded system implementations |

---

## 📊 GitHub Activity

<div align="center">

![Profile Views](https://komarev.com/ghpvc/?username=jrjohn&color=blueviolet&style=flat-square)
[![GitHub followers](https://img.shields.io/github/followers/jrjohn?style=flat-square&logo=github)](https://github.com/jrjohn?tab=followers)
[![GitHub stars](https://img.shields.io/github/stars/jrjohn?style=flat-square&logo=github)](https://github.com/jrjohn?tab=repositories)

</div>

---

<div align="center">

*"Architecture is not about frameworks and tools, it's about making the right decisions at the right time."*

**@ Nirvana | Taiwan**

</div>

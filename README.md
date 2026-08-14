<div align="center">
    
**System/Software Architect | Full-Stack Developer | Technical Lead | Taiwan**

[![Email](https://img.shields.io/badge/Email-jr.johnchang%40gmail.com-EA4335?style=flat&logo=gmail&logoColor=white)](mailto:jr.johnchang@gmail.com)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0008--6249--1470-A6CE39?style=flat&logo=orcid&logoColor=white)](https://orcid.org/0009-0008-6249-1470)

*Building enterprise-grade applications with Clean Architecture design*

*Turning ideas into reality*

</div>

---

## 🏗️ Arcana Architecture Suite

A comprehensive collection of enterprise-grade reference architectures implementing **Clean Architecture**, **Offline-First** design, and **MVVM patterns** across multiple platforms.

```mermaid
flowchart TB
    style Apps fill:none,stroke:none
    subgraph Apps[" "]
        direction LR
        subgraph Client["📱 Client Applications"]
            direction TB
            subgraph Desktop["Desktop"]
                Windows["🪟 Windows<br/>⭐ 9.0"]
                macOS["🍎 macOS<br/>⭐ 9.4"]
            end
            subgraph Web["Web"]
                Angular["🅰️ Angular<br/>⭐ 9.4"]
                React["⚛️ React<br/>⭐ 9.2"]
                Vue["💚 Vue<br/>⭐ 10.0"]
            end
            subgraph Mobile["Mobile"]
                iOS["🍎 iOS<br/>⭐ 9.5"]
                Android["🤖 Android<br/>⭐ 9.2"]
                HarmonyOS["🔷 HarmonyOS<br/>⭐ 9.2"]
            end
            Desktop ~~~ Web
            Web ~~~ Mobile
        end
        subgraph Embedded["🔌 Embedded Systems"]
            direction TB
            STM32["🛠️ STM32<br/>⭐ 7.5"]
            ESP32["📡 ESP32<br/>⭐ 8.3"]
            STM32 ~~~ ESP32
        end
        Client ~~~ Embedded
    end

    subgraph Cloud["☁️ Cloud Services"]
        direction LR
        SpringBoot["☕ Spring Boot<br/>⭐ 9.3"]
        Python["🐍 Python<br/>⭐ 9.2"]
        Go["🐹 Go<br/>⭐ 8.6"]
        Rust["🦀 Rust<br/>⭐ 9.0"]
        NodeJS["💚 Node.js<br/>⭐ 9.5"]
    end

    subgraph Core["🎯 Core Principles"]
        CA["Clean Architecture"]
        OF["Offline-First"]
        MVVM["MVVM I/O/E Pattern"]
    end

    Desktop --> Cloud
    Web --> Cloud
    Mobile --> Cloud
    Embedded --> Cloud
    Cloud --> Core
    click iOS "https://github.com/jrjohn/arcana-ios" _blank
    click Android "https://github.com/jrjohn/arcana-android" _blank
    click HarmonyOS "https://github.com/jrjohn/arcana-harmonyos" _blank
    click Angular "https://github.com/jrjohn/arcana-angular" _blank
    click React "https://github.com/jrjohn/arcana-react" _blank
    click Vue "https://github.com/jrjohn/arcana-vue" _blank
    click Windows "https://github.com/jrjohn/arcana-windows" _blank
    click macOS "https://github.com/jrjohn/arcana-macos" _blank
    click STM32 "https://github.com/jrjohn/arcana-embedded-stm32" _blank
    click ESP32 "https://github.com/jrjohn/arcana-embedded-esp32" _blank
    click SpringBoot "https://github.com/jrjohn/arcana-cloud-springboot" _blank
    click Python "https://github.com/jrjohn/arcana-cloud-python" _blank
    click Go "https://github.com/jrjohn/arcana-cloud-go" _blank
    click Rust "https://github.com/jrjohn/arcana-cloud-rust" _blank
    click NodeJS "https://github.com/jrjohn/arcana-cloud-nodejs" _blank
```

---

## 📱 Mobile Development

| Platform | Repository | Tech Stack | Description |
|:--------:|:-----------|:-----------|:------------|
| 🍎 | [**arcana-ios**](https://github.com/jrjohn/arcana-ios) | Swift, SwiftUI, SwiftData | Clean Architecture with Offline-First design and Analytics Tracking |
| 🤖 | [**arcana-android**](https://github.com/jrjohn/arcana-android) | Kotlin, Jetpack Compose, Hilt | Clean Architecture with Offline-First design and AOP Analytics |
| 🔷 | [**arcana-harmonyos**](https://github.com/jrjohn/arcana-harmonyos) | ArkTS, ArkUI | HarmonyOS NEXT application with Clean Architecture |

---

## 🖥️ Desktop Development

| Platform | Repository | Tech Stack | Description |
|:--------:|:-----------|:-----------|:------------|
| 🪟 | [**arcana-windows**](https://github.com/jrjohn/arcana-windows) | C#, WinUI 3, MVVM | Clean Architecture with Plugin System and CRDT-based Offline Sync |
| 🍎 | [**arcana-macos**](https://github.com/jrjohn/arcana-macos) | Swift, SwiftUI, SwiftData | Clean Architecture with Offline-First design and SwiftData persistence |

---

## 🌐 Web Development

| Framework | Repository | Tech Stack | Description |
|:---------:|:-----------|:-----------|:------------|
| 🅰️ | [**arcana-angular**](https://github.com/jrjohn/arcana-angular) | TypeScript, Angular, Signals | Production-ready with Offline-First capabilities and Enterprise Security |
| ⚛️ | [**arcana-react**](https://github.com/jrjohn/arcana-react) | TypeScript, React 19, Zustand | Enterprise-grade with MVVM Input/Output/Effect pattern |
| 💚 | [**arcana-vue**](https://github.com/jrjohn/arcana-vue) | TypeScript, Vue 3, Pinia | Modern Vue application with Composition API |

---

## 🔌 Embedded Systems

| Platform | Repository | Tech Stack | Description |
|:--------:|:-----------|:-----------|:------------|
| 🛠️ | [**arcana-embedded-stm32**](https://github.com/jrjohn/arcana-embedded-stm32) | C | STM32 embedded systems with Clean Architecture |
| 📡 | [**arcana-embedded-esp32**](https://github.com/jrjohn/arcana-embedded-esp32) | C++ | ESP32 IoT embedded systems development |

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

## 🏛️ DevOps & Quality

| Project | Repository | Tech Stack | Description |
|:-------:|:-----------|:-----------|:------------|
| 🏛️ | [**arcana-arch-qube**](https://github.com/jrjohn/arcana-arch-qube) | Python, Claude API | AI-powered Architecture Quality Gate — 21 rules, 14 profiles, CI/CD integration |

---

## 🤖 AI & Skills

| Project | Repository | Tech Stack | Description |
|:-------:|:-----------|:-----------|:------------|
| 🧠 | [**arcana-ai-agent**](https://github.com/jrjohn/arcana-ai-agent) | - | AI Agent implementation |
| ⚡ | [**arcana-skills**](https://github.com/jrjohn/arcana-skills) | HTML | Claude Skills for Software Developer |
| 🔧 | [**skills**](https://github.com/jrjohn/skills) | JavaScript | AI Skill implementation |

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

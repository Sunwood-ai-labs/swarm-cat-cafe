---
title: Cat Cafe Swarm AI Response System
emoji: 🐱
colorFrom: yellow
colorTo: orange
sdk: python
sdk_version: 3.11.4
app_file: main.py
pinned: false
license: mit
---

<p align="center">
  <img src="https://raw.githubusercontent.com/Sunwood-ai-labs/swarm-cat-cafe/refs/heads/main/docs/swarm-cat-cafe.png" width="100%">
  <h1 align="center">🐈 swarm-cat-cafe 🐈</h1>
</p>
<p align="center">
  <a href="https://github.com/Sunwood-ai-labs/swarm-cat-cafe">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/github-swarm--cat--cafe-blue?logo=github">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-cat-cafe/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/Sunwood-ai-labs/swarm-cat-cafe?color=green">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-cat-cafe/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Sunwood-ai-labs/swarm-cat-cafe?style=social">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-cat-cafe/releases">
    <img alt="GitHub release" src="https://img.shields.io/github/v/release/Sunwood-ai-labs/swarm-cat-cafe?include_prereleases&style=flat-square">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-cat-cafe/issues">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/Sunwood-ai-labs/swarm-cat-cafe">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-cat-cafe/pulls">
    <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-cat-cafe/network/members">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/Sunwood-ai-labs/swarm-cat-cafe?style=social">
  </a>
  <a href="https://github.com/Sunwood-ai-labs/swarm-cat-cafe/watchers">
    <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/Sunwood-ai-labs/swarm-cat-cafe?style=social">
  </a>
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Sunwood-ai-labs/swarm-cat-cafe">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/Sunwood-ai-labs/swarm-cat-cafe">
</p>
<h2 align="center">
  ～ AI Response System for Cat Cafes ～

<a href="https://github.com/Sunwood-ai-labs/swarm-cat-cafe/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
<a href="https://github.com/Sunwood-ai-labs/swarm-cat-cafe/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>
</h2>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/Swarm-FF4500?style=for-the-badge&logo=github" alt="Swarm">
</p>



## 🚀 Project Overview

This project implements an automated response system for cat cafes using the Swarm framework. Multiple AI agents collaborate to handle various customer inquiries.


## ✨ Main Features

- **Receptionist Agent:** Understands customer questions and transfers them to the appropriate agent.
- **Menu Guide Agent:** Answers questions about the cafe's menu.
- **Reservation Management Agent:** Manages the creation, confirmation, and cancellation of reservations.
- **Cat Information Agent:** Provides information about the cats in the cafe.


## 🔧 How to Use


### Setup

1. Clone or download the project.

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate  # Windows
```

3. Install the necessary packages:

```bash
pip install -r requirements.txt
```

4. Navigate to the directory containing `main.py`.


### Usage

Start the system with the following command:

```bash
python main.py
```

After starting, you can interact with the cat cafe's AI response system on the console.  Enter your questions and receive responses from the agents.


## 📦 Installation Instructions

1. Clone this repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```


## 🌿 Environment Setup

Follow these steps to set up the environment for this project:

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```
   This creates a virtual environment in the `.venv` directory.

2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate  # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

These steps will prepare the development environment for this project.


## 📚 Major Components

### 🤖 [Swarm](https://github.com/openai/swarm)
- A framework developed by OpenAI that allows multiple AI agents to collaborate to perform tasks.


## 🐈 Processing Flow


```mermaid
%%{init:{'theme':'base','themeVariables':{'primaryColor':'#024959','primaryTextColor':'#F2C335','primaryBorderColor':'#F2AE30','lineColor':'#A1A2A6','secondaryColor':'#593E25','tertiaryColor':'#F2C335','noteTextColor':'#024959','noteBkgColor':'#F2C335','textColor':'#024959','fontSize':'18px'}}}%%

graph LR
    A[Customer Inquiry] --> B{Receptionist Agent}
    B -- Menu-related questions --> C[Menu Guide Agent]
    B -- Reservation-related questions --> D[Reservation Management Agent]
    B -- Cat-related questions --> E[Cat Information Agent]
    C --> F[Response]
    D --> F
    E --> F
    F --> G[Response to Customer]

    class B,C,D,E agent;
    class A,G process;

```



## 🤝 Contributions

This project is open source and welcomes contributions from the community. Please help improve this project through bug reports, feature requests, and pull requests.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements


---
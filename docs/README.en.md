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
  <img src="docs/HarmonAI-III.png" width="100%">
  <h1 align="center">🐈 swarm-cat-cafe 🐈</h1>
</p>
<p align="center">
  <a href="https://github.com/your-username/swarm-cat-cafe">
    <img alt="GitHub Repo" src="https://img.shields.io/badge/github-swarm--cat--cafe-blue?logo=github">
  </a>
  <a href="https://github.com/your-username/swarm-cat-cafe/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/your-username/swarm-cat-cafe?color=green">
  </a>
  <a href="https://github.com/your-username/swarm-cat-cafe/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/your-username/swarm-cat-cafe?style=social">
  </a>
  <a href="https://github.com/your-username/swarm-cat-cafe/releases">
    <img alt="GitHub release" src="https://img.shields.io/github/v/release/your-username/swarm-cat-cafe?include_prereleases&style=flat-square">
  </a>
  <a href="https://github.com/your-username/swarm-cat-cafe/issues">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/your-username/swarm-cat-cafe">
  </a>
  <a href="https://github.com/your-username/swarm-cat-cafe/pulls">
    <img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square">
  </a>
  <a href="https://github.com/your-username/swarm-cat-cafe/network/members">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/your-username/swarm-cat-cafe?style=social">
  </a>
  <a href="https://github.com/your-username/swarm-cat-cafe/watchers">
    <img alt="GitHub watchers" src="https://img.shields.io/github/watchers/your-username/swarm-cat-cafe?style=social">
  </a>
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/your-username/swarm-cat-cafe">
  <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/your-username/swarm-cat-cafe">
</p>
<h2 align="center">
  ～ Cat Cafe AI Response System ～

<a href="https://github.com/your-username/swarm-cat-cafe/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
<a href="https://github.com/your-username/swarm-cat-cafe/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>
</h2>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/Swarm-FF4500?style=for-the-badge&logo=github" alt="Swarm">
</p>



## 🚀 Project Overview

This project implements an automated response system for a cat cafe using the Swarm framework. Multiple AI agents collaborate to handle various customer inquiries.


## ✨ Key Features

- **Receptionist Agent:** Understands customer questions and routes them to the appropriate agent.
- **Menu Guide Agent:** Answers questions about the cafe's menu.
- **Reservation Management Agent:** Manages the creation, confirmation, and cancellation of reservations.
- **Cat Information Agent:** Provides information about the cats at the cafe.


## 🔧 How to Use


### Setup

1. Clone or download the project.

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate  # Windows
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Navigate to the directory containing `main.py`.


### Usage

Start the system with the following command:

```bash
python main.py
```

After starting, you can interact with the cat cafe's AI response system on the console. Enter your questions and receive responses from the agents.


## 📦 Installation Instructions

1. Clone this repository.
2. Install the necessary dependencies:
   ```bash
   pip install -r requirements.txt
   ```


## 🌿 Environment Setup

To set up the environment for this project, follow these steps:

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   ```
   This will create a virtual environment in the `.venv` directory.

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
- A framework developed by OpenAI for multiple AI agents to collaborate and perform tasks.


## 🐈 Processing Flow


```mermaid
%%{init:{'theme':'base','themeVariables':{'primaryColor':'#024959','primaryTextColor':'#F2C335','primaryBorderColor':'#F2AE30','lineColor':'#A1A2A6','secondaryColor':'#593E25','tertiaryColor':'#F2C335','noteTextColor':'#024959','noteBkgColor':'#F2C335','textColor':'#024959','fontSize':'18px'}}}%%

graph LR
    A[Customer Inquiry] --> B{Receptionist Agent}
    B -- Menu-related question --> C[Menu Guide Agent]
    B -- Reservation-related question --> D[Reservation Management Agent]
    B -- Cat-related question --> E[Cat Information Agent]
    C --> F[Response]
    D --> F
    E --> F
    F --> G[Response to Customer]

    class B,C,D,E agent;
    class A,G process;

```



## 🤝 Contributions

This project is an open-source project and welcomes contributions from the community. Please help improve this project through bug reports, feature requests, and pull requests.

## 📄 License

This project is licensed under the MIT License.

## 🙏 Acknowledgements


---
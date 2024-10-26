---
title: 猫カフェ Swarm AI 応答システム
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
  ～ 猫カフェのためのAI応答システム ～

<a href="https://github.com/your-username/swarm-cat-cafe/blob/main/README.md"><img src="https://img.shields.io/badge/ドキュメント-日本語-white.svg" alt="JA doc"/></a>
<a href="https://github.com/your-username/swarm-cat-cafe/blob/main/docs/README.en.md"><img src="https://img.shields.io/badge/english-document-white.svg" alt="EN doc"></a>
</h2>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai" alt="OpenAI">
  <img src="https://img.shields.io/badge/Swarm-FF4500?style=for-the-badge&logo=github" alt="Swarm">
</p>



## 🚀 プロジェクト概要

このプロジェクトは、Swarmフレームワークを使用して猫カフェの自動応答システムを実装したものです。複数のAIエージェントが協力して、顧客からの様々な問い合わせに対応します。


## ✨ 主な機能

- 受付係エージェント: 顧客の質問を理解し、適切なエージェントに転送します。
- メニュー案内エージェント: カフェのメニューに関する質問に答えます。
- 予約管理エージェント: 予約の作成、確認、キャンセルを管理します。
- 猫の情報案内エージェント: カフェにいる猫たちの情報を提供します。


## 🔧 使用方法


### セットアップ

1. プロジェクトをクローンまたはダウンロードします。

2. 仮想環境を作成し、アクティベートします：

```bash
python -m venv venv
source venv/bin/activate  # Linuxの場合
venv\Scripts\activate  # Windowsの場合
```

3. 必要なパッケージをインストールします：

```bash
pip install -r requirements.txt
```

4. `main.py`があるディレクトリに移動します。


### 使用方法

以下のコマンドでシステムを起動します：

```bash
python main.py
```

起動後、コンソール上で猫カフェのAI応答システムとやり取りができます。質問を入力し、エージェントからの応答を受け取ることができます。


## 📦 インストール手順

1. このリポジトリをクローンします。
2. 必要な依存関係をインストールします：
   ```bash
   pip install -r requirements.txt
   ```


## 🌿 環境構築

このプロジェクトの環境を構築するには、以下の手順に従ってください：

1. 仮想環境を作成します：
   ```bash
   python3 -m venv .venv
   ```
   これにより、`.venv`ディレクトリに仮想環境が作成されます。

2. 仮想環境をアクティベートします：
   ```bash
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate  # Windows
   ```

3. 依存関係をインストールします：

   ```bash
   pip install -r requirements.txt
   ```

これらの手順により、このプロジェクトの開発環境が整います。


## 📚 主要コンポーネント

### 🤖 [Swarm](https://github.com/openai/swarm)
- OpenAIが開発した、複数のAIエージェントが協力してタスクを実行するためのフレームワーク


## 🐈 処理フロー


```mermaid
%%{init:{'theme':'base','themeVariables':{'primaryColor':'#024959','primaryTextColor':'#F2C335','primaryBorderColor':'#F2AE30','lineColor':'#A1A2A6','secondaryColor':'#593E25','tertiaryColor':'#F2C335','noteTextColor':'#024959','noteBkgColor':'#F2C335','textColor':'#024959','fontSize':'18px'}}}%%

graph LR
    A[顧客からの問い合わせ] --> B{受付係エージェント}
    B -- メニューに関する質問 --> C[メニュー案内エージェント]
    B -- 予約に関する質問 --> D[予約管理エージェント]
    B -- 猫に関する質問 --> E[猫の情報案内エージェント]
    C --> F[回答]
    D --> F
    E --> F
    F --> G[顧客への回答]

    class B,C,D,E agent;
    class A,G process;

```



## 🤝 コントリビューション

このプロジェクトはオープンソースプロジェクトとしてコミュニティからの貢献を歓迎しています。バグ報告、機能リクエスト、プルリクエストを通じて、このプロジェクトの改善にご協力ください。

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🙏 謝辞


---

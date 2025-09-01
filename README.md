# Election Voting App

Flask 製のシンプルな「政策動画 × 投票」アプリ。  
動画（`movies/`）を見ながらスワイプで賛否を付け、最後に候補 A/B/C のいずれかへ投票する。投票はテキスト保存し、API で集計結果を返す。フロントは `front.html` 単一ファイル（Plotly で結果表示）。

---

## Features
- 動画ビューア（スワイプ操作：右=賛成、左=反対）
- 候補 A/B/C への投票（ボタン）
- 投票結果の集計表示（棒グラフ、Plotly）
- 静的ファイルとして `movies/` 内の動画を配信
- シンプルなファイル永続化（`votes.txt`）

---

## Project Structure
├── app.py # Flask バックエンド（API/静的ファイル配信）
├── front.html # フロントエンド（UI・グラフ描画）
├── votes.txt # 投票データの保存先（1行1投票）
├── movies/ # 動画ファイル格納ディレクトリ（*.MP4 など）
├── requirements.txt # 依存パッケージ
└── README.md

## Requirements
- Python 3.8+
- (pip で以下を導入)
  - Flask
  - flask-cors

> 依存は `requirements.txt` に記載。

---

## Setup & Run

```bash
# 1) 取得
git clone <YOUR_REPO_URL>
cd election-voting-app

# 2) 依存インストール
pip install -r requirements.txt

# 3) サーバ起動
python app.py
# → http://localhost:5000 にアクセス
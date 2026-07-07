# 日本神経科学大会 硬式テニス交流会 HP

硬式テニス交流会の案内用の静的サイトです。GitHub Pages にそのまま公開できます。

## ファイル構成

```
jns-tennis/
├── content.yaml          # ★ 編集するのは基本このファイルだけ
├── build.py              # content.yaml → index.html を生成
├── index.html.template   # HTML の骨組み（通常は触らない）
├── index.html            # 生成物（build.py の出力）
├── requirements.txt      # ビルド用（初回のみ pip install）
├── css/style.css         # デザイン
├── js/main.js            # ナビ開閉・ギャラリーのライトボックス
├── images/               # ギャラリー画像
└── README.md
```

## 内容の更新手順

1. **`content.yaml` を編集**（日程・会場・参加費・リンクなど）
2. **ビルドを実行**

```bash
cd ~/Documents/jns-tennis
python3 -m venv .venv          # 初回のみ
.venv/bin/pip install -r requirements.txt   # 初回のみ
.venv/bin/python build.py
```

（venv 作成済みなら `.venv/bin/python build.py` だけで OK）

3. **`index.html` も一緒に commit & push**（GitHub Pages は静的ファイルをそのまま配信するため）

> `index.html` は直接編集しないでください。変更は `content.yaml` に書いてから `build.py` を実行します。

## content.yaml の主な項目

| セクション | 内容 |
|-----------|------|
| `site` | ページタイトル、説明文、フッター |
| `hero` | ヒーロー（開催回、日程・会場チップなど） |
| `about` | 概要文、ポイント3つ、主催・共催 |
| `access` | 日時・会場・アクセス、Google マップリンク |
| `schedule` | 当日タイムテーブル（`timeline` リスト） |
| `fee` | 参加費、持ち物リスト（`bring_items`） |
| `register` | 申込フォーム URL、連絡先メール |
| `gallery` | ギャラリー説明、画像パス |

### リンクを有効にする

`access.map`・`register.form`・`register.contact` には `placeholder: true/false` があります。

- `placeholder: true` … リンク無効（未設定のまま）
- `placeholder: false` に変更し、`url` / `email` を実際の値に設定 … リンク有効

```yaml
register:
  form:
    url: "https://forms.gle/xxxxxxxx"
    label: 申込フォームを開く
    placeholder: false
```

### ギャラリー写真の差し替え

1. `images/` に写真（jpg/png 等）を置く
2. `content.yaml` の `gallery.images` で `src` と `alt` を更新
3. `python3 build.py`

## ローカルプレビュー

```bash
python3 build.py
python3 -m http.server 8000
# ブラウザで http://localhost:8000 を開く
```

## GitHub Pages で公開

1. このフォルダを Git 管理にする

```bash
cd ~/Documents/jns-tennis
git init
git add .
git commit -m "Initial site"
git branch -M main
```

2. GitHub に公開リポジトリ（例: `jns-tennis`）を作成し、push

```bash
git remote add origin https://github.com/<ユーザー名>/jns-tennis.git
git push -u origin main
```

3. リポジトリの **Settings > Pages** で、Source を `Deploy from a branch`、Branch を `main` / `/(root)` に設定して保存

4. 数十秒後、`https://<ユーザー名>.github.io/jns-tennis/` で公開されます

## デザインを変えたい場合

レイアウトや CSS クラスを変えるときは `index.html.template` と `css/style.css` を編集し、再度 `python3 build.py` を実行してください。

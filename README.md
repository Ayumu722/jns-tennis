# 日本神経科学大会 硬式テニス交流会 HP

硬式テニス交流会の案内用の静的サイトです。ビルド不要（HTML/CSS/JSのみ）で、GitHub Pages にそのまま公開できます。

## ファイル構成

```
jns-tennis/
├── index.html        # 本体（全セクション）
├── css/style.css     # デザイン
├── js/main.js        # ナビ開閉・ギャラリーのライトボックス
├── images/           # ギャラリー用プレースホルダー画像（SVG）
└── README.md
```

## 内容の差し替え（プレースホルダー一覧）

`index.html` 内の `【...】` と「未設定」のリンクが仮の箇所です。確定情報に置き換えてください。

- 開催回・大会名: `第XX回 日本神経科学大会`
- 日時: `【日程未定】`（ヒーロー、日時・会場、各スケジュールの `【時刻未定】`）
- 会場・住所・最寄駅: `【テニスコート名・未定】` `【住所・未定】` `【最寄駅・未定】`
- 地図リンク: 「Google マップで開く（リンク未設定）」の `href="#"` を実URLに変更し、`data-placeholder` 属性を削除
- 主催・共催: `【主催団体名・未定】` `【未定】`
- 参加費: `¥【未定】`
- 申込フォーム: 「申込フォームを開く（リンク未設定）」の `href="#"` を Google フォーム等のURLに変更し、`data-placeholder` を削除
- 連絡先メール: `【連絡先メール・未定】`（`mailto:` も実アドレスに）
- ギャラリー写真: `images/gallery-*.svg` を実際の写真（jpg/png）に差し替え、`index.html` の `src`/`data-full` を更新

> リンクを有効化するときは、その要素から `data-placeholder` を必ず外してください（付いているとクリックが無効化されます）。

## ローカルプレビュー

```bash
cd ~/Documents/jns-tennis
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

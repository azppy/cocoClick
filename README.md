# cocoClick

### ◾️ 概要  
**cocoClick** は、指定した座標を記録し、後で自動クリックを再現するツールです。
<br>
### ◾️ インストール  
以下のコマンドを実行して、必要なライブラリをインストールしてください。  
```sh
poetry install
```

### ◾️ 使い方
**1. クリック座標の記録**

getxyt.py を実行し、記録したい場所をクリックします。

```sh
poetry run python getxyt.py
```
クリックしたモニターの座標と間隔が clicks.csv に保存されます。

**2. 記録した動作の再現**

cococlick.py を実行すると、記録したクリック動作が再現されます。

```sh
poetry run python cococlick.py
```

### ◾️ ファイル構成

getxyt.py : クリック座標と間隔を記録するスクリプト

cococlick.py : 記録したクリック動作を再現するスクリプト

clicks.csv : 記録された座標と間隔

poetry.lock

poetry.toml

pyproject.toml
<br>
<br>
<br>
<br>
*** ***注意事項*** ***

マルチモニター環境では、クリック座標が異なる場合があります。

自動クリックの使用は、利用規約違反になる場合があるため注意してください。

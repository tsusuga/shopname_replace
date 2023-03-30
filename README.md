# 概要
CSVファイルを元に、ejsファイルの置換をするスクリプト

## 使い方
1. csvディレクトリにsource.csvファイルを配置（フォーマット：　1列目に変更後の文字列、2列目に変更前の文字列）
2. targetディレクトリに置換対象のtxtファイルを配置
3. スクリプトを実行するとtarget/afterディレクトリに置換処理後ファイルが生成される

## 構造
<pre>
├─csv
    └─source.csv
└─target
    ├─_shopdata.ejs
    └─after
          └─after_change.ejs
</pre>

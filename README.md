
# 📂 File Encoding Detector

## 📋 概要
**File Encoding Detector**は、指定されたディレクトリ内のテキストファイル（`.txt`）の文字エンコーディングを検出し、その情報を出力するPythonスクリプトです。  
BOM（Byte Order Mark）や一般的な文字エンコーディングを基準にエンコーディングを特定します。

---

## 🚀 主な機能
1. **エンコーディング検出**
   - UTF-8, UTF-16, UTF-32（BOM付き）や、`utf-8`, `shift_jis`, `euc-jp`, `latin-1`などの一般的な文字エンコーディングを試行します。

2. **ディレクトリ内のテキストファイルをスキャン**
   - 指定されたディレクトリ内のすべてのテキストファイルを再帰的に検査します。

3. **情報の出力**
   - ファイルのパス、名前、エンコーディング情報をコンソールに表示します。
   - 必要に応じてCSVファイルに結果を保存できます。

---

## 🛠️ 使用方法

### 必要な環境
- Python 3.x

### 実行手順
1. **スクリプトのダウンロード**  
   このリポジトリをクローンまたはファイルをダウンロードします。
   ```bash
   git clone https://github.com/your-repo/file-encoding-detector.git
   cd file-encoding-detector
   ```

2. **依存関係の確認**  
   標準ライブラリのみを使用しているため、追加インストールは不要です。

3. **スクリプトの実行**
   ```bash
   python encoding_detector.py
   ```

4. **ディレクトリパスの入力**
   実行後、検査対象となるディレクトリのパスを入力します。
   ```
   検査するディレクトリのパスを入力: C:\example\directory
   ```

5. **結果の確認**
   ファイルのパス、名前、およびエンコーディングがコンソールに表示されます。
   必要に応じてCSV形式で結果を保存できます。

---

## 📂 サンプル出力

### コンソール出力
```
ファイルパス, ファイル名, ファイル文字コード
C:\example\directory, sample1.txt, utf-8
C:\example\directory, sample2.txt, shift_jis
C:\example\directory, sample3.txt, utf-16
```
---

## 📄 コード解説

### 主な関数
1. **`detect_encoding(file_path)`**
   - BOMを基準にエンコーディングを検出します。
   - BOMがない場合、一般的なエンコーディング（utf-8, shift_jisなど）を試行します。

2. **`try_encoding(file_path, encodings)`**
   - 指定されたエンコーディングリストを順に試行し、成功したエンコーディングを返します。

3. **`write_to_csv(file_info_list, output_csv_path)`**
   - 検出されたファイル情報をCSV形式で保存します。

4. **`print_file_info(file_info_list)`**
   - ファイルのパス、名前、エンコーディングをコンソールに表示します。

5. **`gather_file_info(directory_path)`**
   - 指定されたディレクトリ内のすべての`.txt`ファイルを再帰的に探索し、エンコーディング情報を収集します。

---

## ⚠️ 注意事項
1. **検査対象ファイル**
   - `.txt`拡張子のファイルのみが対象です。他の拡張子は無視されます。

2. **権限エラー**
   - アクセス権のないファイルまたはフォルダにアクセスするとエラーが発生する可能性があります。

3. **エンコーディングの不明性**
   - 指定されたエンコーディングリストに該当しない場合、`unknown` と表示されます。

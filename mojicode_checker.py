import os
import csv

def detect_encoding(file_path):
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read(4)
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
        return 'unknown'
    except OSError:
        print(f"ファイルが開けません: {file_path}")
        return 'unknown'

    # BOM 확인
    # UTF-32 BOM: FF FE 00 00 또는 00 00 FE FF
    if raw_data.startswith(b'\xff\xfe\x00\x00') or raw_data.startswith(b'\x00\x00\xfe\xff'):
        return 'utf-32'
    # UTF-16 BOM: FF FE 또는 FE FF
    elif raw_data.startswith(b'\xff\xfe') or raw_data.startswith(b'\xfe\xff'):
        return 'utf-16'
    # UTF-8 BOM: EF BB BF
    elif raw_data.startswith(b'\xef\xbb\xbf'):
        return 'utf-8-sig'

    # BOM이 없는 경우 일반적으로 시도할 인코딩 리스트
    common_encodings = ['utf-8', 'shift_jis', 'euc-jp', 'latin-1']
    return try_encoding(file_path, common_encodings)

def try_encoding(file_path, encodings):
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                f.read()
            return encoding
        except (UnicodeDecodeError, LookupError):
            continue
        except OSError:
            print(f"ファイルが開けません: {file_path}")
            return 'unknown'
    return 'unknown'

def write_to_csv(file_info_list, output_csv_path):
    try:
        with open(output_csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ファイルパス", "ファイル名", "ファイル文字コード"])
            for file_info in file_info_list:
                writer.writerow(file_info)
    except OSError as e:
        print(f"出力ファイルに書き込めません: {output_csv_path}")
        print(f"エラー詳細: {e}")

def print_file_info(file_info_list):
    try:
        print("ファイルパス, ファイル名, ファイル文字コード")
        for file_info in file_info_list:
            print(f"{file_info[0]}, {file_info[1]}, {file_info[2]}")
    except OSError as e:
        print(f"情報出力中にエラーが発生しました")
        print(f"エラー詳細: {e}")

def gather_file_info(directory_path):
    file_info_list = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            # sql 파일만 대상
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                encoding = detect_encoding(file_path)
                file_info_list.append([root, file, encoding])
    return file_info_list

def main():
    directory_path = input("検査するディレクトリのパスを入力: ")
    # 필요하다면 CSV 출력 경로를 받을 수 있습니다.
    # output_csv_path = input("CSVを保存するファイルパスを入力: ")
    
    file_info_list = gather_file_info(directory_path)
    print_file_info(file_info_list)

    # 필요시 CSV에 출력
    # write_to_csv(file_info_list, output_csv_path)
    # print(f"情報が {output_csv_path} に出力されました。")

    print("処理終了")

if __name__ == '__main__':
    main()

def convert_to_srt_time(seconds):
    """
    # 將秒數轉換為 SRT 時間格式 (00:00:00,000)
    # 參數 seconds: 以秒為單位的時間
    # 返回: SRT格式的時間字串
    """
    hours = int(seconds / 3600)
    minutes = int((seconds % 3600) / 60)
    secs = int(seconds % 60)
    millisecs = int((seconds - int(seconds)) * 1000)

    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millisecs:03d}"


def parse_time(time_str):
    """
    # 解析時間字串，支援兩種格式：
    # 1. 分:秒 (例如 "1:30")
    # 2. 時:分:秒 (例如 "1:00:04")
    # 返回: 總秒數
    """
    try:
        parts = time_str.strip().split(':')
        if len(parts) == 2:  # 格式是 分:秒
            minutes, seconds = map(int, parts)
            return minutes * 60 + seconds
        elif len(parts) == 3:  # 格式是 時:分:秒
            hours, minutes, seconds = map(int, parts)
            return hours * 3600 + minutes * 60 + seconds
        else:
            print(f"無效的時間格式: {time_str}")
            return 0
    except ValueError:
        print(f"時間格式錯誤: {time_str}")
        return 0


def is_time_format(line):
    """
    # 檢查是否為時間格式的行
    # 參數 line: 要檢查的文字行
    # 返回: 是否為時間格式
    """
    try:
        # 移除空白並檢查格式
        line = line.strip()
        parts = line.split(':')
        return len(parts) in [2, 3] and all(part.isdigit() for part in parts)
    except:
        return False


def text_to_srt(input_text):
    """
    # 將帶時間戳的文字轉換為SRT格式
    # 參數 input_text: 輸入的文字內容
    # 返回: SRT格式的字串
    """
    lines = input_text.split('\n')
    srt_content = []
    counter = 1
    current_time = None
    current_text = []

    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # 跳過空行
        if not line:
            i += 1
            continue

        try:
            # 如果是時間戳
            if is_time_format(line):
                # 如果已經有上一段，就處理它
                if current_time is not None and current_text:
                    # 找下一個時間戳
                    next_time = None
                    look_ahead = i
                    while look_ahead < len(lines):
                        if is_time_format(lines[look_ahead].strip()):
                            next_time = parse_time(lines[look_ahead].strip())
                            break
                        look_ahead += 1

                    # 如果沒有下一個時間戳，設定預設結束時間
                    if next_time is None:
                        next_time = parse_time(current_time) + 5

                    # 組合字幕文字（保留換行）
                    subtitle_text = '\n'.join(current_text)

                    # 建立 SRT 條目
                    srt_entry = (
                        f"{counter}\n"
                        f"{convert_to_srt_time(parse_time(current_time))} --> "
                        f"{convert_to_srt_time(next_time)}\n"
                        f"{subtitle_text}\n\n"
                    )
                    srt_content.append(srt_entry)
                    counter += 1

                # 開始新的一段
                current_time = line
                current_text = []
            else:
                # 如果不是時間戳且已有時間戳，則為字幕文字
                if current_time is not None:
                    current_text.append(line)

            i += 1

        except Exception as e:
            print(f"處理第 {i + 1} 行時發生錯誤: {str(e)}")
            i += 1

    # 處理最後一段
    if current_time is not None and current_text:
        subtitle_text = '\n'.join(current_text)
        srt_entry = (
            f"{counter}\n"
            f"{convert_to_srt_time(parse_time(current_time))} --> "
            f"{convert_to_srt_time(parse_time(current_time) + 5)}\n"
            f"{subtitle_text}\n\n"
        )
        srt_content.append(srt_entry)

    return ''.join(srt_content)


# 主程式
if __name__ == "__main__":
    try:
        # 讀取輸入檔案
        with open('C:/Users/qpsa7/Desktop/ChatGpt/241025.txt', 'r', encoding='utf-8') as file:
            input_text = file.read()

        # 轉換成SRT格式
        srt_output = text_to_srt(input_text)

        # 寫入輸出檔案
        with open('C:/Users/qpsa7/Desktop/ChatGpt/241025.srt', 'w', encoding='utf-8') as f:
            f.write(srt_output)

        print("轉換完成！檔案已儲存為 output.srt 🎉")

    except FileNotFoundError:
        print("找不到輸入檔案！請確認 input.txt 檔案存在 😅")
    except Exception as e:
        print(f"發生錯誤：{str(e)} 😱")

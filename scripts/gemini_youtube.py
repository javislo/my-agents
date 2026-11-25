#!/usr/bin/env python3
"""用 Gemini 直接讀 YouTube 影片（Google 端抓取，不會被 YouTube 擋）。
用法: python3 scripts/gemini_youtube.py <youtube_url> <mode: transcript|vision> [輸出檔]
金鑰由雲端環境的 Network secret 自動注入（header: x-goog-api-key），程式只送佔位值。
"""
import json, os, sys, urllib.request

MODEL = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")
PROMPTS = {
    "transcript": (
        "請輸出這支影片的完整逐字稿。格式：每行 `[mm:ss] 說話內容`，保留原語言；"
        "若非中文，於每行後附上 ` ｜ 繁中翻譯`。最後加一段「重點摘要」（5~10 點，繁體中文）。"
    ),
    "vision": (
        "請以繁體中文逐段分析這支影片，同時看畫面和聽聲音。每段格式：\n"
        "## [mm:ss–mm:ss] 段落標題\n- 畫面：鏡頭/操作/螢幕上出現的東西\n- 聲音：講了什麼\n"
        "- 技巧/關鍵知識：可以學起來的做法\n最後列出「整支影片的方法論」與「可直接照做的步驟清單」。"
    ),
}

def main():
    if len(sys.argv) < 3 or sys.argv[2] not in PROMPTS:
        sys.exit(__doc__)
    url, mode = sys.argv[1], sys.argv[2]
    body = {"contents": [{"parts": [{"file_data": {"file_uri": url}}, {"text": PROMPTS[mode]}]}]}
    req = urllib.request.Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json",
                 "x-goog-api-key": os.environ.get("GEMINI_API_KEY", "proxy-injected")},
    )
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Gemini API 錯誤 {e.code}: {e.read().decode()[:800]}")
    text = "".join(p.get("text", "") for c in data.get("candidates", [])
                   for p in c.get("content", {}).get("parts", []))
    out = f"# {mode}: {url}\n\n{text}\n"
    if len(sys.argv) > 3:
        open(sys.argv[3], "w", encoding="utf-8").write(out)
        print(f"已存到 {sys.argv[3]}")
    else:
        print(out)

if __name__ == "__main__":
    main()

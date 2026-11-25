---
name: youtube-transcript
description: 給 YouTube 連結就產出帶時間軸的逐字稿與重點摘要。當使用者貼 YouTube 連結並想知道影片講了什麼、要逐字稿或摘要時使用。
---
# YouTube 逐字稿（耳朵）

1. 從連結取出影片 ID（`v=` 後面或 `youtu.be/` 後面那串）。
2. 執行：`python3 scripts/gemini_youtube.py "<url>" transcript transcripts/<影片ID>.md`
3. 讀取輸出檔，用繁體中文回覆使用者摘要，並告知檔案位置。
4. 若有多支影片，逐支執行。完成後 `git add transcripts && git commit && git push`。

注意：雲端環境的 IP 會被 YouTube 擋，不要用 yt-dlp，一律走 Gemini。超過約 1 小時的影片可能超出免費額度，請先提醒使用者。

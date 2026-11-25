---
name: youtube-vision
description: 同時看 YouTube 影片的畫面與聲音，逐段整理時間軸、畫面內容、講述內容和可學的技巧。當使用者想知道影片「怎麼做的」、要畫面分析或教學步驟時使用。
---
# YouTube 畫面＋聲音分析（眼睛）

1. 執行：`python3 scripts/gemini_youtube.py "<url>" vision analyses/<影片ID>.md`
2. 讀取結果，用繁體中文整理重點回覆使用者。
3. 完成後 commit 並 push `analyses/`。

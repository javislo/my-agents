---
name: build-expert
description: 把多支 YouTube 教學影片煉成一個領域專家 skill（例如剪片專家）。當使用者給一批影片連結並說「做成專家／agent」時使用。
---
# 造出專家 agent

輸入：專家名稱（英文小寫連字號，如 `editor-agent`）＋ 5~10 支影片連結。

1. 每支影片跑 youtube-vision skill（已有 `analyses/<ID>.md` 就跳過）。
2. 讀完全部分析，歸納出：
   - 核心原則（多支影片都提到的）
   - 標準工作流程（步驟化）
   - 常見錯誤與修正
   - 依情境的做法（例：外聯、行銷、內容 三種工作各自怎麼套用）
   - 每條知識標註來源影片與時間點
3. 寫成 `.claude/skills/<專家名稱>/SKILL.md`：frontmatter 的 description 要寫清楚「什麼問題時使用」；內文以第一人稱專家口吻規定如何回答問題、如何審稿/給建議。
4. 長篇參考資料放 `.claude/skills/<專家名稱>/reference.md`，SKILL.md 保持精簡並指向它。
5. commit 並 push，告訴使用者以後怎麼呼叫：「用 <專家名稱> 幫我…」。

加新影片時：只分析新影片，再把新知識合併進既有的 SKILL.md／reference.md。

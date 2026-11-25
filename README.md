# my-agents
讓 Claude Code 看懂 YouTube，再自己造出專家 agent。
- `youtube-transcript`：逐字稿（耳朵）
- `youtube-vision`：畫面＋聲音分析（眼睛）
- `build-expert`：多支影片 → 專家 skill
所有 YouTube 讀取都透過 Gemini API（`scripts/gemini_youtube.py`），金鑰存在雲端環境的 Network secrets（header `x-goog-api-key`）。

# 小恐龍遊戲

這是一個使用 `Pygame` 庫開發的簡單小恐龍遊戲。玩家控制一個小恐龍在水平的地面上跳躍，避開隨機生成的障礙物。遊戲目標是獲得更高的分數並避免與障礙物發生碰撞。

## 特點

- **簡單的遊戲機制**：玩家只需控制小恐龍跳躍，避免障礙物。
- **分數系統**：每避開一個障礙物並保持生還，分數會逐漸增加。
- **隨機生成障礙物**：障礙物的高度和速度隨機生成，增添了遊戲的挑戰性。
- **背景音樂與音效**：背景音樂為遊戲增添氛圍，並且每當分數增加時會播放音效。
- **遊戲結束畫面**：當恐龍與障礙物碰撞時，遊戲會結束，顯示最終分數並提供重新開始的選項。

## 遊戲規則

1. **開始遊戲**：遊戲啟動後，小恐龍會在地面上移動，玩家可以按 `UP` 鍵讓恐龍跳躍。
2. **跳躍**：小恐龍會跳躍一段距離，並在跳躍結束後回到地面。
3. **避開障礙物**：隨機生成的障礙物會從右側移動過來，玩家需要避免與障礙物碰撞。
4. **遊戲結束**：如果小恐龍與障礙物碰撞，遊戲結束並顯示結束畫面，顯示最終分數並提供重新開始的選項。

## 如何運行

1. 確保已安裝 `Pygame` 庫：
   ```bash
   pip install pygame
   ```
2. 確保準備了必要的資源檔案：
   - `bgm.wav`：背景音樂文件
   - `score.wav`：分數音效文件
   - `dinosaur.png`：小恐龍圖片文件
   - `retry.jpg`：重新開始圖片文件

3. 運行程式：
   ```bash
   python dinosaur_game.py
   ```

## 遊戲畫面

遊戲視窗的大小為 800x400 像素，地面位於畫面的底部。隨著遊戲的進行，障礙物會不斷生成並向左移動。

- **分數顯示**：在畫面的右上角顯示當前分數。
- **重來按鈕**：當遊戲結束時，顯示一個可以點擊的重來按鈕。

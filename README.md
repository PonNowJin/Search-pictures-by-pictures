# Image Similarity Search System
這是一個基於 Flask 和 Vue.js 的圖片相似度搜尋系統。用戶可以通過上傳圖片或指定圖片路徑，並使用指定的搜尋方法（例如 cosine 相似度），來搜尋與目標圖片最相似的其他圖片。

## 主要功能
* 圖片搜尋：根據用戶提供的圖片，搜尋與其相似的圖片，並返回相似度分數。
* 支持不同的搜尋方法：例如使用 Cosine 相似度來計算圖片間的相似度。
* 結果展示：將搜尋結果（包括圖片路徑和相似度分數）在前端顯示。
* 後端 API：使用 Flask 提供圖片相似度搜尋的 API，前端通過 axios 發送請求。

## 技術架構
* 後端：使用 Python 的 Flask 框架來構建 API，負責圖片處理和相似度計算。
* 前端：使用 Vue.js 構建前端應用，通過與 Flask API 進行交互來顯示搜尋結果。
* 資料庫：圖片數據儲存和處理（使用 CSV 格式的資料文件）。

## 使用方法
### 後端（Flask）
**安裝依賴：** 在後端資料夾中，創建一個虛擬環境並安裝依賴：
```bash
python -m venv venv
source venv/bin/activate  # Windows 使用 venv\Scripts\activate
pip install -r requirements.txt

```
**運行後端服務：** 啟動 Flask 伺服器，監聽在本地端口 8066：
```bash
python app.py
```
**API 路徑：**
* POST /api/search: 用於接收圖片路徑和搜尋方法，返回最相似圖片的列表。

### 前端（Vue.js）
**安裝依賴：** 在前端資料夾中，使用以下命令來安裝依賴：
```bash
npm install
```
**運行前端服務：** 啟動 Vue.js 前端服務，通常運行在本地端口 8081：
```bash
npm run serve
```
**前端頁面：** 前端提供圖片選擇功能，並將圖片路徑傳遞給後端 API。搜尋結果會顯示圖片路徑及其相似度分數。

## API 詳細說明
POST /api/search
該端點接受一個 JSON 請求，並根據提供的圖片路徑進行相似圖片搜尋。
**請求範例：**
```bash
{
  "imgPath": "/path/to/your/image.jpg",
  "method": "CS",  # 目前支持的搜尋方法: 'ED', 'CS', 'PCC'
  "normalized": 1      # 可選：0（無正規化），1（min-max正規化），2（zScore正規化）
}
```
**回應範例：**
```bash
{
  "results": [
    {
      "imgPath": "/images/img_0.jpg",
      "score": 0.90
    },
    {
      "imgPath": "/images/img_1.jpg",
      "score": 0.85
    },
    {
      "imgPath": "/images/img_2.jpg",
      "score": 0.80
    }
  ]
}
```
## 開發與維護
1. **新增搜尋方法**：如果你希望支援更多圖片搜尋方法，可以在後端擴充對應的算法。
2. **增加圖片資料庫**：目前圖片數據是硬編碼的，若需要處理大量圖片，建議使用資料庫進行管理。

## 注意事項
* 在開發和生產環境中，請確保正確設置 CORS（跨來源資源共享）和其他安全配置，防止 API 被未授權的用戶訪問。
* 測試和確保後端服務正確返回圖片的相似度分數，並且前端能夠正確解析和顯示結果。

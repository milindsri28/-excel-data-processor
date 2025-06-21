# 📊 Excel Data Processor

Welcome! This app lets you upload Excel files, view and analyze the data in your browser, and stores everything securely in Firebase. When you close the site, your data is automatically cleared for privacy.

## What You Can Do
- **Upload Excel files** (.xlsx, .xls)
- **See your data instantly** in a sortable, searchable table
- **Get quick stats** about your data
- **Try with sample files** (included!)
- **No data left behind**: Everything is wiped when you close or refresh the page

## Quick Start

### 1. Clone and Install
```bash
git clone <your-repo-url>
cd kustodian
```

#### Backend
```bash
cd backend
pip install -r requirements.txt
cp env.example .env  # Add your Firebase info to .env
```

#### Frontend
```bash
cd frontend
npm install
```

### 2. Run Locally
- **Backend:**
  ```bash
  cd backend
  python main.py
  ```
- **Frontend:**
  ```bash
  cd frontend
  npm start
  ```

### 3. Try It Out
- Open [http://localhost:3000](http://localhost:3000)
- Upload your own Excel file, or use one of the sample files:
  - `sample_employee_data.xlsx`
  - `sample_sales_data.xlsx`
  - `sample_inventory_data.xlsx`
  - `sample_student_data.xlsx`
  - `sample_customer_data.xlsx`
  - `sample_weather_data.xlsx`
  - `sample_simple_data.xlsx`

## How It Works
- **Upload**: Drag & drop or select an Excel file
- **View**: Instantly see your data in a table
- **Analyze**: Get quick stats and search/filter
- **Privacy**: Data is cleared when you close or refresh the page

## Need Help?
- Make sure your Firebase info is correct in `.env`
- If you get errors, check your browser console or terminal for details
- For more info, see the deployment guide or open an issue

---

Enjoy exploring your Excel data! 🚀 
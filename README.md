# 🥦 Nutrito Prompt Server

**Nutrito Prompt Server** is a Python-based Flask backend that processes food-related images and data to provide nutritional analysis, ingredient evaluation, product comparisons, alternative suggestions, and smart grocery lists. This backend is a core component of the broader *Nutrito* ecosystem focused on promoting healthier lifestyle choices through intelligent food analysis.

---

## 📌 Table of Contents

- [✅ Features](#✅-features)
- [🧰 Tech Stack](#🧰-tech-stack)
- [📁 Project Structure](#📁-project-structure)
- [🛠️ Installation](#🛠️-installation)
- [🔐 Environment Variables](#🔐-environment-variables)
- [🚀 Running the Server](#🚀-running-the-server)
- [📡 API Endpoints](#📡-api-endpoints)
- [🧯 Error Handling](#🧯-error-handling)
- [🤝 Contributing](#🤝-contributing)
- [📄 License](#📄-license)
- [👤 Author](#👤-author)
- [📢 Acknowledgements](#📢-acknowledgements)

---

## ✅ Features

- 🔍 Extract text and ingredients from food packaging.
- 📊 Perform nutritional and ratio-based analysis.
- 🧠 Analyze health implications based on ingredients.
- 📸 Accept image inputs for intelligent comparison.
- 💡 Suggest alternative healthier food products.
- 🌍 Global and local ML-based product suggestions.
- 🧾 Generate smart shopping lists from prompts.

---

## 🧰 Tech Stack

- **Language**: Python 3.8+
- **Framework**: Flask
- **Image Processing**: Pillow (PIL)
- **Async Support**: asyncio
- **Modular Design**: Flask Blueprints
- **Data Handling**: JSON, BytesIO

---

## 📁 Project Structure

```
nutrito-prompt-server/
├── app.py                 # Main server file
├── requirements.txt       # Python dependencies
├── src/
│   ├── gen/
│   │   ├── chat.py
│   │   ├── searched.py
│   │   ├── alternative.py
│   │   ├── global_model.py
│   │   ├── local_model.py
│   │   ├── image_text.py
│   │   ├── compare.py
│   │   ├── shopping.py
│   └── routes/
│       └── rest_urls.py
```

---

## 🛠️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/nutrito-prompt-server.git
cd nutrito-prompt-server

# Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory with the following:

```ini
APP_CONFIG_KEY=your_secret_key
```

---

## 🚀 Running the Server

```bash
python app.py
```

Server will run on `http://127.0.0.1:5000/` by default.

---

## 📡 API Endpoints

### 🩺 Server Health Check
- **GET** `/api/checkServer`

### 📷 Initial Prompt Analysis
- **POST** `/api/initialPrompt`
- `Form-Data`: `image`

### ⚖️ Ratio Analysis
- **POST** `/api/ratioPrompt`
- `Form-Data`: `image`

### ❤️ Health Consideration
- **POST** `/api/healthPrompt`
- `Form-Data`: `image`

### 🧾 Conclusion Analysis
- **POST** `/api/conclusionPrompt`
- `Form-Data`: `image`

### ⚖️ Compare Products
- **POST** `/api/compareProducts`
- `Form-Data`: `image1`, `image2`

### 🔄 Alternative Suggestions (Text)
- **POST** `/api/getAlternative`
```json
{
  "product": "Product Name",
  "data": "Extracted ingredients or description"
}
```

### 🖼️ Alternative Suggestions (Image)
- **POST** `/api/imageAlternative`
- `Form-Data`: `image`

### 🌍 Global Product Alternatives
- **POST** `/api/generateAlternative`
```json
{
  "product": "Product Name",
  "data": "Extracted description"
}
```

### 🧠 Categorized Search
- **POST** `/api/catergoriedSearch`
```json
{
  "filterData": "value to filter",
  "option": "nutrient type"
}
```

### 🛍️ Smart Shopping List
- **POST** `/api/smartlist`
```json
{
  "message": "create a list with healthy snacks under 200 calories"
}
```

---

## 🧯 Error Handling

- **400 Bad Request** – Missing or invalid inputs.
- **500 Internal Server Error** – Server-side failure.

Example response:
```json
{
  "error": "No image file found in the request"
}
```

---

## 🤝 Contributing

Contributions are welcome!

```bash
# Fork and clone the repo
# Create a feature branch
# Commit and push your changes
# Open a Pull Request
```


---

## 👤 Author

**Om Jamnekar**  
📧 omjamnekar877@gmail.com

---

## 📢 Acknowledgements

- Flask – Web server framework
- Pillow – Image processing
- asyncio – Concurrency
- Team Nutrito – Vision & support

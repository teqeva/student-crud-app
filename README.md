# Students & Courses CRUD API (FastAPI + MySQL)

## 🚀 Setup
1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/student-crud-app.git
   cd student-crud-app
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
 3. Update MySQL credentials in app/database.py
 4. Run the server:
    ```bash
    uvicorn app.main:app --reload

    
  📌 API Endpoints
Students

- POST /students → Create student

- GET /students → List students

- PUT /students/{id} → Update student

- DELETE /students/{id} → Delete student

Courses

- POST /courses → Create course

- GET /courses → List courses

- PUT /courses/{id} → Update course

- DELETE /courses/{id} → Delete course

  
---



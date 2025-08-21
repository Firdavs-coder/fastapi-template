# FastAPI Template

A well-structured FastAPI template with authentication, error handling, file uploads, and background tasks. This template provides a solid foundation for building REST APIs with FastAPI.

## 🚀 Features

- **API Key Authentication**: Secure endpoints with header-based API key authentication
- **Global Error Handling**: Centralized error handling for validation errors, custom exceptions, and permission errors
- **File Upload Support**: Endpoints for image and video file uploads with validation
- **Form Data Processing**: User form handling with validation
- **Background Tasks**: Asynchronous background task processing
- **Modular Architecture**: Well-organized code structure with separation of concerns
- **Parameter Validation**: Comprehensive input validation using Pydantic and FastAPI

## 📁 Project Structure

```
fastapi-template/
├── app.py                 # FastAPI application setup
├── main.py               # Application entry point
├── requirements.txt      # Python dependencies
├── config/
│   └── config.py        # Configuration settings (empty template)
├── module/
│   ├── __init__.py
│   ├── dependencies.py  # Authentication dependencies
│   ├── params.py        # Request parameter classes
│   ├── errors/
│   │   ├── __init__.py
│   │   ├── errors.py    # Custom error classes
│   │   └── exceptions.py # Global exception handlers
│   └── routers/
│       ├── __init__.py
│       └── routers.py   # API route definitions
└── utils/               # Utility functions (empty)
```

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fastapi-template
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Running the Application

### Development Mode
```bash
python main.py
```

### Production Mode with Uvicorn
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

## 📖 API Documentation

Once the server is running, you can access:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔐 Authentication

All endpoints require an API key to be passed in the header:

```
ApiKey: 123
```

**Note**: The default API key is `"123"`. Change this in `module/dependencies.py` for production use.

## 📋 API Endpoints

### User Management

#### Create User
- **POST** `/create-user/`
- **Description**: Create a new user with form data
- **Parameters**:
  - `name`: String (2-50 characters, cannot be "John")
  - `email`: Valid email address
  - `age`: Integer (18-120)
  - `is_active`: Boolean
- **Content-Type**: `application/x-www-form-urlencoded`

### File Upload

#### Image Upload
- **POST** `/image/`
- **Description**: Upload and stream back an image file
- **Supported formats**: JPEG, PNG
- **Content-Type**: `multipart/form-data`

#### Video Upload
- **POST** `/video/`
- **Description**: Upload and download a video file
- **Supported formats**: MP4, MKV
- **Content-Type**: `multipart/form-data`

### Background Tasks

#### Send Notification
- **POST** `/notify/`
- **Description**: Trigger a background task that logs a notification

### Error Testing

#### Value Error
- **POST** `/value-error/`
- **Description**: Endpoint that intentionally raises a ValueError for testing error handling

## 🔧 Configuration

### Environment Variables
Add your configuration variables in `config/config.py`. The file is currently empty and ready for your settings.

### Authentication
To change the API key, modify the `authorize` function in `module/dependencies.py`:

```python
async def authorize(ApiKey: str = Header(...)):
    if ApiKey != "your-secret-key":  # Change this
        raise PermissionError("Unauthorized request")
```

## 🚨 Error Handling

The template includes comprehensive error handling:

- **Validation Errors (422)**: Automatic handling of request validation failures
- **Permission Errors (403)**: API key authentication failures
- **Custom Errors (400)**: Custom ValueError handling
- **Centralized Handling**: All errors return consistent JSON responses

### Error Response Format
```json
{
    "error": "Error type",
    "message": "Detailed error message"
}
```

## 🧪 Testing

### Using curl

**Create User:**
```bash
curl -X POST "http://localhost:8000/create-user/" \
  -H "ApiKey: 123" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "name=Alice&email=alice@example.com&age=25&is_active=true"
```

**Upload Image:**
```bash
curl -X POST "http://localhost:8000/image/" \
  -H "ApiKey: 123" \
  -F "image=@path/to/your/image.jpg"
```

**Send Notification:**
```bash
curl -X POST "http://localhost:8000/notify/" \
  -H "ApiKey: 123"
```

## 📦 Dependencies

- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation and settings management using Python type annotations
- **python-multipart**: Support for form data and file uploads

## 🎯 Next Steps

1. **Database Integration**: Add database models and ORM (SQLAlchemy, Tortoise ORM)
2. **Advanced Authentication**: Implement JWT tokens or OAuth2
3. **Testing**: Add unit and integration tests
4. **Logging**: Implement structured logging
5. **Docker**: Add Docker containerization
6. **Environment Management**: Add environment-specific configurations

## 📝 License

This template is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
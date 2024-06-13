
# BitPin Posts API

This project provides an API for creating, listing, and rating posts using Django and Django REST Framework. It includes JWT-based authentication and validation for user input.

## Project Setup

1. **Clone the Repository**

   ```bash
   git clone <repository_url>
   cd bitpin
   ```

2. **Create and Activate Virtual Environment**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the Server**

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Create Post

- **Endpoint**: `/api/create-post/`
- **Method**: POST
- **Input**:
  ```json
  {
      "title": "Post Title",
      "body": "Post body text"
  }
  ```
- **Response**: 
  ```json
  {
      "message": "Create Post Successfully."
  }
  ```

### List Posts

- **Endpoint**: `/api/list-posts/`
- **Method**: GET
- **Response**: 
  ```json
  [
      {
          "title": "Post Title",
          "body": "Post body text",
          "user": "username",
          "rate_ave": 0
      },
      ...
  ]
  ```

### Rate Post

- **Endpoint**: `/api/rate-post/`
- **Method**: POST
- **Input**:
  ```json
  {
      "post": 1,
      "rate": 5
  }
  ```
- **Response**: 
  ```json
  {
      "message": "Added Rate Successfully."
  }
  ```

## Testing

To run the tests, use the following command:

```bash
python manage.py test bitpin.posts.tests
```

### Test Scenarios

- **Create Post**: Test creating a new post with valid data.
- **List Posts**: Test retrieving all posts.
- **Rate Post**: Test rating a post while authenticated.
- **Create Post Unauthenticated**: Test creating a post without authentication.
- **Rate Post Unauthenticated**: Test rating a post without authentication.
- **Rate Non-existent Post**: Test rating a non-existent post.
- **Invalid Rate Value**: Test rating a post with an invalid rate value.

## Contact

For any questions or issues, please contact the project maintainer at [your-email@example.com].

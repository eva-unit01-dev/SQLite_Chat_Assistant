# SQLite_Chat_Assistant
Chat Assistant for SQLite Database for Ajackus

A natural language chat interface for querying an SQLite database containing employee and department information.

## How It Works

The chat assistant operates through three main components:

### 1. Database Layer
- Uses SQLite to store employee and department information
- Contains two primary tables:
  - Employees (ID, Name, Department, Salary, Hire_Date)
  - Departments (ID, Name, Manager)
- Automatically initializes with sample data on first run

### 2. Query Handler
- Processes natural language queries through pattern matching
- Converts natural language to SQL queries
- Supports various query types including:
  - Department employee listings
  - Manager lookups
  - Date-based employee filtering
  - Salary summations by department
- Formats database results into human-readable responses
- Implements error handling for invalid queries

### 3. Web Interface
- Flask-based web application
- Real-time chat interface
- Displays example queries for user reference
- Provides immediate feedback for all queries

## Running the Project Locally

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation Steps

1. Clone the repository:
```bash
git clone [repository-url]
cd [repository-name]
```

2. Create and activate a virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Access the application:
- Open your web browser
- Navigate to `http://localhost:5000`
- Start querying the database!

## Project Structure
```
├── app.py              # Main Flask application
├── database_setup.py   # Database initialization
├── query_handler.py    # Query processing logic
├── company.db          # SQLite database
├── requirements.txt    # Project dependencies
└── templates/
    └── index.html      # Web interface template
```

## Known Limitations

1. Query Understanding
- Limited to predefined query patterns
- May not understand complex or compound queries
- Sensitive to exact phrasing
- No support for fuzzy matching or typo correction

2. Database Constraints
- Fixed schema design
- No support for real-time data updates
- Limited to sample dataset unless manually updated
- No support for complex joins or nested queries

3. User Interface
- Basic error handling
- No support for query history
- Limited visualization options
- No export functionality for query results

## Suggestions for Improvement

1. Enhanced Natural Language Processing
- Implement NLP libraries for better query understanding
- Add support for more complex query patterns
- Include synonym recognition
- Add context awareness for follow-up questions

2. Database Functionality
- Add support for data modifications (INSERT, UPDATE, DELETE)
- Implement data validation and sanitization
- Add support for database backups
- Include more complex query capabilities

3. User Interface Enhancements
- Add data visualization options
- Implement query history and favorites
- Add export functionality for results
- Improve mobile responsiveness
- Add user authentication and personalization

4. Performance Optimizations
- Implement query caching
- Add database indexing
- Optimize large result set handling
- Add connection pooling

5. Security Improvements
- Implement input sanitization
- Add SQL injection prevention
- Add rate limiting
- Implement user authentication and authorization

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
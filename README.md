# Open Source Utilities

This repository contains small, useful utilities or libraries that can be used in various projects. The utilities include string manipulation functions, date-time utilities, and a simple API wrapper.

## Utilities

### String Utilities

Located in the `string_utils` directory, these functions help with common string operations.

#### Functions

- `reverse_string(s: str) -> str`: Return the reversed string.
- `is_palindrome(s: str) -> bool`: Check if a string is a palindrome.

### Date-Time Utilities

Located in the `datetime_utils` directory, these functions assist with date-time operations.

#### Functions

- `add_days(date: datetime, days: int) -> datetime`: Add a specified number of days to a date.
- `days_between(date1: datetime, date2: datetime) -> int`: Return the number of days between two dates.

### API Wrapper

Located in the `api_wrapper` directory, this class simplifies making API requests.

#### Class

- `APIWrapper(api_key: str)`: Initialize with an API key.
- `get(endpoint: str, params: dict = None) -> dict`: Make a GET request to the specified endpoint.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/<your-username>/open-source-utilities.git
   cd open-source-utilities
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate # On Windows use `venv\Scripts\activate`
   
3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   
## Running Tests
Each utility has its own test suite located in its respective tests directory. To run all tests:
  ```sh
python -m unittest discover
```
## Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b new-feature).
3. Make your changes and commit them (git commit -am 'Add new feature').
4. Push to the branch (git push origin new-feature).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

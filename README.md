# WhatsAppBot

This project is a WhatsApp bot built using FastAPI.

## Features

- Send and receive messages
- Automated responses
- Integration with WhatsApp API

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- WhatsApp API

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/WhatsAppApi.git
    cd WhatsAppApi
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the FastAPI server:
    ```bash
    uvicorn src.main:app --reload
    ```

2. Access the API documentation at `http://127.0.0.1:8000/docs`.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
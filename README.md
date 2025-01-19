

# Ollama Model Performance Tester

This tool is designed to test the performance of Ollama models by measuring the speed of token generation. It provides a user-friendly web interface for conducting performance tests on locally installed Ollama models.

## Features

- Select from installed Ollama models on your local machine
- Customize the input prompt or use the default
- Specify the number of tokens to generate
- Run performance tests and view detailed results
- Display generated text and performance metrics

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/liubinby/ollama-performance-tester.git
   cd ollama-performance-tester
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app with:

```
streamlit run ollama_performance_test.py
```

This will open a web interface where you can:

1. Select an installed Ollama model from your local machine
2. Edit the default prompt or input your own
3. Specify the number of tokens to generate
4. Run the performance test
5. View the results, including:
   - Selected model
   - Number of tokens generated
   - Time taken
   - Tokens per second
   - Generated text

## Note on Accuracy

Please note that this tool provides a rough estimate of performance. Token counting is performed by splitting on spaces, which may not be entirely accurate for all models. For more precise measurements, consider using a proper tokenizer specific to the model you're testing.

## Requirements

See `requirements.txt` for a list of required Python packages.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License


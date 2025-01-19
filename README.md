
This is a performance test tool for Ollama models, it test the speed of the token generation.

Run the Streamlit app with:

streamlit run ollama_performance_test.py
This will open a web interface where you can:

Select from the installed models on your local machine.
Edit the default prompt or use your own.
Specify the number of tokens to generate.
Run the performance test and see the results, including the generated text and performance metrics.
The app will display the selected model, the number of tokens generated, time taken, tokens per second, and the generated text.

Note that this is a rough estimate of performance, as token counting is done by splitting on spaces, which isn't entirely accurate. For more precise measurements, you might need to use a proper tokenizer for the specific model you're using.

To install the dependent modules:
  pip install -r requirements.txt
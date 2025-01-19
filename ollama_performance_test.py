import streamlit as st
import time
from ollama import Client

def get_installed_models():
    client = Client()
    try:
        models = client.list()
        return [{
            'name': model.model,
            'size': model.size,
            'modified_at': model.modified_at,
            'family': model.details.family,
            'parameter_size': model.details.parameter_size,
            'quantization_level': model.details.quantization_level
        } for model in models.models]
    except Exception as e:
        st.error(f"Error fetching models: {str(e)}")
        return []

def run_performance_test(model, prompt, num_tokens):
    client = Client()
    
    start_time = time.time()
    response = client.generate(model=model, prompt=prompt, stream=False, options={'num_predict': num_tokens})
    end_time = time.time()

    generated_text = response['response']
    tokens_generated = len(generated_text.split())  # This is a rough estimate
    time_taken = end_time - start_time
    tokens_per_second = tokens_generated / time_taken

    return {
        "generated_text": generated_text,
        "tokens_generated": tokens_generated,
        "time_taken": time_taken,
        "tokens_per_second": tokens_per_second
    }

st.title("Ollama Model Performance Tester")

installed_models = get_installed_models()
selected_model = st.selectbox("Select a model", [model['name'] for model in installed_models])

# Display additional info about the selected model
selected_model_info = next((model for model in installed_models if model['name'] == selected_model), None)
if selected_model_info:
    st.write(f"Model: {selected_model_info['name']}")
    st.write(f"Size: {selected_model_info['size']} bytes")
    st.write(f"Modified at: {selected_model_info['modified_at']}")
    st.write(f"Family: {selected_model_info['family']}")
    st.write(f"Parameter size: {selected_model_info['parameter_size']}")
    st.write(f"Quantization level: {selected_model_info['quantization_level']}")

# Prompt input
default_prompt = "Write a short story about a robot learning to paint."
prompt = st.text_area("Enter your prompt", value=default_prompt)

# Number of tokens to generate
num_tokens = st.number_input("Number of tokens to generate", min_value=1, value=100)

if st.button("Run Test"):
    with st.spinner("Running performance test..."):
        results = run_performance_test(selected_model, prompt, num_tokens)
    
    st.subheader("Test Results")
    st.write(f"Model: {selected_model}")
    st.write(f"Tokens generated: {results['tokens_generated']}")
    st.write(f"Time taken: {results['time_taken']:.2f} seconds")
    st.write(f"Tokens per second: {results['tokens_per_second']:.2f}")
    
    st.subheader("Generated Text")
    st.write(results['generated_text'])

st.sidebar.info("This app tests the performance of Ollama models installed on your local machine.")
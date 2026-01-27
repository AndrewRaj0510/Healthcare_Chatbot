import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/chat"

def chat_with_bot(user_input, history):
    if not user_input or not user_input.strip():
        return history, ""

    response = requests.post(API_URL, json={"question": user_input})
    response.raise_for_status()
    bot_reply = response.json()["answer"]

    history = history or []
    history.append({"role": "user", "content": user_input})
    history.append({"role": "assistant", "content": bot_reply})

    return history, ""

with gr.Blocks(title="Healthcare Information Assistant") as demo:
    gr.Markdown("""
    # Healthcare Information Assistant

    This chatbot provides **educational healthcare information only**.
    It does **not confirm diagnoses** and is **not a substitute for professional medical advice**.
                 
    ⚠️ This chatbot does NOT confirm diagnoses. Always consult a doctor.
    """)

    chatbot = gr.Chatbot()
    state = gr.State([])

    with gr.Row():
        txt = gr.Textbox(
            placeholder="Describe your symptoms or ask a health-related question (e.g., headache, blurred vision)...",
            show_label=False,
            lines=1
        )

    with gr.Row():
        submit_btn = gr.Button("Send")

    # ENTER key
    txt.submit(
        chat_with_bot,
        inputs=[txt, state],
        outputs=[chatbot, txt],
    )

    # Button click
    submit_btn.click(
        chat_with_bot,
        inputs=[txt, state],
        outputs=[chatbot, txt],
    )

demo.launch()
import streamlit as st
from streamlit_chatbox import ChatBox, Markdown, Image, Video, Audio
import time
import simplejson as json

# Add FakeLLM class for demo purposes
class FakeLLM:
    def chat(self, query):
        # Simulate a chat response
        return f"This is a response to: {query}", ["Reference 1", "Reference 2"]
    
    def chat_stream(self, query):
        # Simulate a streaming response
        text = f"This is a streaming response to: {query}"
        for char in text:
            yield char, []
            time.sleep(0.05)

# Configuration
DEFAULT_THEMES = {
    "user": "green",
    "assistant": "blue"
}

class ChatInterface:
    def __init__(self):
        self.llm = FakeLLM()
        self.chat_box = ChatBox(
            use_rich_markdown=True,
            user_theme=DEFAULT_THEMES["user"],
            assistant_theme=DEFAULT_THEMES["assistant"]
        )
        self.chat_box.use_chat_name("chat1")
        self.setup_sidebar()
        self.initialize_chat()

    def setup_sidebar(self):
        with st.sidebar:
            st.subheader('Streamlit Chat Interface')
            self.chat_name = st.selectbox(
                "Chat Session:", 
                ["default", "chat1"], 
                key="chat_name", 
                on_change=self.on_chat_change
            )
            self.streaming = st.checkbox('Enable Streaming', key="streaming")
            self.in_expander = st.checkbox('Show Messages in Expander', key="in_expander")
            self.show_history = st.checkbox('Show Session State', key="show_history")
            
            self.setup_file_upload()
            self.setup_action_buttons()

    def setup_file_upload(self):
        st.divider()
        file = st.file_uploader("Chat History JSON", type=["json"])
        if st.button("Load JSON") and file:
            data = json.load(file)
            self.chat_box.from_dict(data)

    def setup_action_buttons(self):
        btns = st.container()
        btns.download_button(
            "Export Markdown",
            "".join(self.chat_box.export2md()),
            file_name="chat_history.md",
            mime="text/markdown",
        )
        btns.download_button(
            "Export JSON",
            self.chat_box.to_json(),
            file_name="chat_history.json",
            mime="text/json",
        )
        if btns.button("Clear History"):
            self.chat_box.init_session(clear=True)
            st.experimental_rerun()

    def on_chat_change(self):
        self.chat_box.use_chat_name(st.session_state["chat_name"])
        self.chat_box.context_to_session()

    def on_feedback(self, feedback, chat_history_id="", history_index=-1):
        score_int = self.chat_box.set_feedback(
            feedback=feedback, 
            history_index=history_index
        )
        st.session_state["need_rerun"] = True

    def handle_chat_input(self):
        if query := st.chat_input('Enter your question here'):
            self.chat_box.user_say(query)
            if self.streaming:
                self.handle_streaming_response(query)
            else:
                self.handle_normal_response(query)

    def handle_streaming_response(self, query):
        generator = self.llm.chat_stream(query)
        elements = self.chat_box.ai_say([
            Markdown("Thinking...", in_expander=self.in_expander, expanded=True, title="Answer"),
            Markdown("", in_expander=self.in_expander, title="References"),
        ])
        
        text = ""
        for x, docs in generator:
            text += x
            self.chat_box.update_msg(text, element_index=0, streaming=True)
            
        self.chat_box.update_msg(text, element_index=0, streaming=False, state="complete")
        self.chat_box.update_msg("\n\n".join(docs), element_index=1, streaming=False, state="complete")

    def handle_normal_response(self, query):
        text, docs = self.llm.chat(query)
        self.chat_box.ai_say([
            Markdown(text, in_expander=self.in_expander, expanded=True, title="Answer"),
            Markdown("\n\n".join(docs), in_expander=self.in_expander, title="References"),
        ])

    def initialize_chat(self):
        self.chat_box.init_session()
        self.chat_box.output_messages()
        self.handle_chat_input()

def main():
    st.set_page_config(page_title="Chat Interface", layout="wide")
    chat_interface = ChatInterface()
    
    # Create columns for multimedia and agent buttons
    col1, col2 = st.columns(2)
    
    if col1.button('Show Multimedia Examples'):
        chat_interface.chat_box.ai_say(Image(
            'https://tse4-mm.cn.bing.net/th/id/OIP-C.cy76ifbr2oQPMEs2H82D-QHaEv?w=284&h=181&c=7&r=0&o=5&dpr=1.5&pid=1.7'))
        time.sleep(0.5)
        chat_interface.chat_box.ai_say(
            Video('https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4'))
        time.sleep(0.5)
        chat_interface.chat_box.ai_say(
            Audio('https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4'))

    if chat_interface.show_history:
        st.write(st.session_state)

if __name__ == "__main__":
    main()
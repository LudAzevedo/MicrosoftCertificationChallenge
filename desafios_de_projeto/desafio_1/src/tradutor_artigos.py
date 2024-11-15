# main.py
import logging
import os
from datetime import datetime

import requests
import streamlit as st
from bs4 import BeautifulSoup
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()


class ArticleTranslator:
    """
    A class to handle article extraction and translation using Azure OpenAI API.

    Attributes:
        api_key (str): Azure OpenAI API key
        endpoint (str): Azure OpenAI endpoint URL
    """

    def __init__(self):
        """Initialize the ArticleTranslator with API credentials."""
        self.api_key = os.getenv("AZURE_OPENAI_KEY")
        self.endpoint = "https://openai-dio-boot-east1.openai.azure.com/openai/deployments/gpt-4o-mini/chat/completions?api-version=2024-02-15-preview"

        if not self.api_key:
            raise ValueError("AZURE_OPENAI_KEY not found in environment variables")

    def extract_text(self, url: str) -> str:
        """
        Extract text content from a given URL.

        Args:
            url (str): The URL to extract text from

        Returns:
            str: Extracted text content

        Raises:
            requests.RequestException: If the URL fetch fails
        """
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            for script in soup(["script", "style"]):
                script.decompose()

            return soup.get_text(" ", strip=True)

        except requests.RequestException as e:
            logger.error(f"Failed to fetch URL: {e}")
            raise

    def translate_text(self, text: str, target_lang: str) -> str:
        """
        Translate text using Azure OpenAI API.

        Args:
            text (str): Text to translate
            target_lang (str): Target language for translation

        Returns:
            str: Translated text in markdown format

        Raises:
            requests.RequestException: If the API request fails
        """
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key,
        }

        payload = {
            "messages": [
                {
                    "role": "system",
                    "content": [
                        {"type": "text", "text": "Você atua como tradutor de textos"}
                    ],
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": f"traduza: {text} para o idioma {target_lang} e responda apenas com a tradução no formato markdown",
                        }
                    ],
                },
            ],
            "temperature": 0.7,
            "top_p": 0.95,
            "max_tokens": 900,
        }

        try:
            response = requests.post(self.endpoint, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"]

        except requests.RequestException as e:
            logger.error(f"Translation API request failed: {e}")
            raise


def save_markdown(content: str, filename: str) -> str:
    """
    Save content to a markdown file.

    Args:
        content (str): Content to save
        filename (str): Base filename without extension

    Returns:
        str: Path to saved file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_filename = f"{filename}_{timestamp}.md"

    with open(safe_filename, "w", encoding="utf-8") as f:
        f.write(content)

    return safe_filename


def main():
    """Main Streamlit application."""
    st.set_page_config(page_title="Article Translator", layout="wide")

    # Application header
    st.markdown(
        """
    # 📚 Article Translator
    ### Transform and translate web articles with ease
    This application allows you to extract content from web articles and translate them into various languages
    while maintaining markdown formatting.
    """
    )

    # Sidebar with about information
    with st.sidebar:
        st.markdown(
            """
        ## About
        This tool helps you:
        - Extract content from web articles
        - Translate to multiple languages
        - Save translations in markdown format
        ### Technologies Used
        - Streamlit
        - Azure OpenAI API
        - BeautifulSoup4
        - Python Requests
        ### Developer
        Created with ❤️ by Your Name
        """
        )

    # Main application layout
    url = st.text_input("📎 Enter Article URL")

    languages = {
        "Portuguese": "português",
        "English": "english",
        "Spanish": "español",
        "French": "français",
        "German": "deutsch",
        "Italian": "italiano",
    }

    target_lang = st.selectbox("🌍 Select Target Language", list(languages.keys()))

    if st.button("🔄 Translate Article"):
        try:
            with st.spinner("Processing article..."):
                translator = ArticleTranslator()

                # Extract and translate
                text = translator.extract_text(url)
                translated = translator.translate_text(text, languages[target_lang])

                # Display result
                st.markdown("### Translation Result")
                st.markdown(translated)

                # Save button
                if st.button("💾 Save as Markdown"):
                    filename = save_markdown(translated, "translated_article")
                    st.success(f"Saved translation to {filename}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            logger.error(f"Application error: {e}", exc_info=True)


if __name__ == "__main__":
    main()

import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain_openai.chat_models.azure import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from typing import Optional

load_dotenv("DIOLab01.env")

# Constants
MAX_CHARS = 6000


class ArticleTranslator:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            azure_endpoint=os.getenv("AZURE_ENDPOINT"),
            api_key=os.getenv("AZURE_API_KEY"),
            api_version="2024-02-15-preview",
            deployment_name="gpt-5-nano"
        )
    
    def extract_text_from_url(self, url: str) -> Optional[str]:
        """Extract clean text from HTML URL."""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for element in soup(["script", "style", "nav", "footer", "header"]):
                element.decompose()
            
            content = soup.find('article') or soup.body
            
            text = content.get_text(separator=' ')
            lines = (line.strip() for line in text.splitlines())
            return "\n".join(line for line in lines if line)

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None

    def translate(self, text: str, target_lang: str) -> Optional[str]:
        """Translates text using a structured ChatPromptTemplate."""
        try:
            prompt = ChatPromptTemplate.from_messages([
                ("system", (
                    "You are an expert technical translator. "
                    "Translate the provided text to {language}. "
                    "Maintain the technical terms in English where appropriate. "
                    "Output the result strictly in valid Markdown format."
                )),
                ("user", "{article_text}")
            ])

            chain = prompt | self.llm
            
            response = chain.invoke({
                "language": target_lang,
                "article_text": text
            })
            
            return response.content
        except Exception as e:
            print(f"Translation error: {e}")
            return None

if __name__ == "__main__":
    translator = ArticleTranslator()
    target_url = 'https://dev.to/gde/gemini-cli-google-developer-knowledge-api-and-mcp-server-equipping-your-ai-assistant-with-an-3gee'

    try:
        print("--- Extracting Content ---")
        clean_text = translator.extract_text_from_url(target_url)
        
        if not clean_text:
            print("Failed to extract content from URL")
            exit(1)
        
        print(f"--- Translating (Target: pt-br) ---")
        # Limiting text length to avoid Token Limit Errors
        final_article = translator.translate(clean_text[:MAX_CHARS], "Portuguese (Brazil)")
        
        if not final_article:
            print("Translation failed")
            exit(1)
        
        print("\nRESULT:\n")
        print(final_article)
        
    except Exception as error:
        print(f"Workflow failed: {error}")
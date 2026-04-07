from typing import List, Dict, Optional
from app.logger import setup_logger

logger = setup_logger()

class AIService:
    """
    AI features for text summarization, and analysis
    """

    def __init__(self, provider: str="openai", model: str="gpt-4o-mini"):
        self.provider=provider
        self.model=model

        if provider=="openai":
            from openai import OpenAI
            self.model=OpenAI()
        else:
            raise ValueError(f"unsuported provider: {provider}")
        
    # -----------------------------
    # PUBLIC METHODS
    # -----------------------------
    def summarize(self, text: str, max_length: int=150) -> str:
        """
        Single text summarization.
        """
        if not text:
            return ""
        
        prompt = self._build_summary_prompt(text, max_length)
        return self._call_model(prompt)
    
    def summarize_batch(self, texts: List[str]) -> List[str]:
        """
        Batch text summarization.
        """
        results = []

        for text in texts:
            try:
                summary = self.summarize(text)
                results.append(summary)
            except Exception as e:
                logger.error(f"failed to summarize: {e}")
        
        return results
    

    def analyze_articles(self, articles: List[Dict]) -> List[Dict]:
        """
        Enrich articles with AI summaries.
        """
        enrich = []

        for article in articles:
            content = (
                article.get("title", "") + "" + article.get("description", "")
            )
            summary = self.summarize(content)
            article["summary"] = summary

            enrich.append(article)
        
        return enrich
    
    
    # -----------------------------
    # INTERNAL METHODS
    # -----------------------------
    def _build_summary_prompt(self, text: str, max_length: str) -> str:
        return f"""
        Summarize the following text in a concise and informative way.
        Limit to {max_length} charcters.

        TEXT:
        {text}
        
        """
    
    def _call_model(self, prompt: str) -> str:
        """
        Main model call
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                message=[
                    {"role": "system", "content": "you are a precise summarizer"},
                    {"role": "user", "content": prompt}
                ],
                temperature = 0.3
            )

            return response.choice[0].message.content.strip()
        except Exception as e:
            logger.error(f"api call failed: {e}")
            return ""
        
        

        








    



        
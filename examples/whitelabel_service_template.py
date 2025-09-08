#!/usr/bin/env python3
"""
Template for creating new whitelabel services in Structify Python client.

This demonstrates how to extend the client with new services using the
whitelabel infrastructure.
"""

from typing import Any, Dict, List, Optional

from structify.resources.whitelabel import WhitelabelResource, whitelabel_method


# Example 1: Simple Image Generation Service
class ImageGenerationResource(WhitelabelResource):
    """Resource for AI image generation service."""
    
    @whitelabel_method("/external/generate-image", method="POST")
    def generate(
        self,
        prompt: str,
        style: str = "realistic",
        size: str = "1024x1024",
        num_images: int = 1
    ) -> Dict[str, Any]:
        """Generate an AI image from a text prompt."""
        return {
            "prompt": prompt,
            "style": style,
            "size": size,
            "num_images": num_images
        }
    
    @whitelabel_method("/external/generate-image", method="POST", response_key="image_urls")
    def generate_urls_only(
        self,
        prompt: str,
        style: str = "realistic",
        size: str = "1024x1024"
    ) -> List[str]:
        """Generate images and return only the URLs."""
        return {
            "prompt": prompt,
            "style": style,
            "size": size,
            "num_images": 1
        }


# Example 2: Translation Service
class TranslationResource(WhitelabelResource):
    """Resource for text translation service."""
    
    @whitelabel_method("/external/translate", method="POST")
    def translate(
        self,
        text: str,
        target_language: str,
        source_language: Optional[str] = None
    ) -> Dict[str, Any]:
        """Translate text to target language."""
        request = {
            "text": text,
            "target_language": target_language
        }
        if source_language:
            request["source_language"] = source_language
        return request
    
    @whitelabel_method("/external/translate/batch", method="POST")
    def translate_batch(
        self,
        texts: List[str],
        target_language: str,
        source_language: Optional[str] = None
    ) -> Dict[str, Any]:
        """Translate multiple texts in a single request."""
        request = {
            "texts": texts,
            "target_language": target_language
        }
        if source_language:
            request["source_language"] = source_language
        return request
    
    @whitelabel_method("/external/translate/detect", method="POST", response_key="language")
    def detect_language(self, text: str) -> str:
        """Detect the language of the given text."""
        return {"text": text}


# Example 3: Document Processing Service
class DocumentProcessingResource(WhitelabelResource):
    """Resource for document processing and analysis."""
    
    @whitelabel_method("/external/documents/extract", method="POST")
    def extract_text(
        self,
        document_url: str,
        format: str = "pdf"
    ) -> Dict[str, Any]:
        """Extract text from a document."""
        return {
            "document_url": document_url,
            "format": format
        }
    
    @whitelabel_method("/external/documents/summarize", method="POST")
    def summarize(
        self,
        document_url: str,
        max_length: int = 500,
        style: str = "bullets"
    ) -> Dict[str, Any]:
        """Generate a summary of a document."""
        return {
            "document_url": document_url,
            "max_length": max_length,
            "style": style
        }
    
    @whitelabel_method("/external/documents/analyze", method="POST")
    def analyze_sentiment(
        self,
        text: str,
        granularity: str = "document"
    ) -> Dict[str, Any]:
        """Analyze sentiment of text."""
        return {
            "text": text,
            "granularity": granularity
        }


# Example 4: Weather Service (GET method example)
class WeatherResource(WhitelabelResource):
    """Resource for weather data service."""
    
    @whitelabel_method("/external/weather/current", method="GET")
    def get_current(
        self,
        location: str,
        units: str = "metric"
    ) -> Dict[str, Any]:
        """Get current weather for a location."""
        return {
            "location": location,
            "units": units
        }
    
    @whitelabel_method("/external/weather/forecast", method="GET")
    def get_forecast(
        self,
        location: str,
        days: int = 7,
        units: str = "metric"
    ) -> Dict[str, Any]:
        """Get weather forecast for a location."""
        return {
            "location": location,
            "days": days,
            "units": units
        }


# How to integrate these into the main client:
# 
# 1. Add to src/structify/resources/__init__.py:
#    from .image_generation import ImageGenerationResource
#    from .translation import TranslationResource
#    # etc.
#
# 2. Add to src/structify/_client.py class definition:
#    image_generation: image_generation.ImageGenerationResource
#    translation: translation.TranslationResource
#    # etc.
#
# 3. Add to src/structify/_client.py __init__ method:
#    self.image_generation = image_generation.ImageGenerationResource(self)
#    self.translation = translation.TranslationResource(self)
#    # etc.
#
# Usage example:
def example_usage():
    """Show how these services would be used."""
    from structify import Structify
    
    client = Structify(api_key="...")
    
    # Image generation
    result = client.image_generation.generate(
        prompt="A futuristic city at sunset",
        style="cyberpunk"
    )
    
    # Translation
    translated = client.translation.translate(
        text="Hello, world!",
        target_language="es"
    )
    
    # Document processing
    summary = client.document_processing.summarize(
        document_url="https://example.com/report.pdf",
        style="bullets"
    )
    
    # Weather
    weather = client.weather.get_current(
        location="San Francisco, CA"
    )
    
    print("Services called successfully!")


if __name__ == "__main__":
    print("This is a template file showing how to create whitelabel services.")
    print("See the source code for implementation examples.")
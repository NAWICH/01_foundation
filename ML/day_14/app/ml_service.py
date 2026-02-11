"""
ML Service for Sentiment Analysis
"""

from transformers import pipeline
from typing import Dict

# Global variable to cache the model
_classifier = None

def get_classifier():
    """Load and cache the sentiment classifier"""
    global _classifier
    if _classifier is None:
        print("Loading sentiment analysis model...")
        _classifier = pipeline(
            "text-classification",
            model="tabularisai/multilingual-sentiment-analysis"
        )
        print("Model loaded successfully!")
    return _classifier

def analyze_sentiment(text: str) -> Dict[str, any]:
    """
    Analyze sentiment of text
    
    Returns:
        dict with 'sentiment' and 'score' keys
    """
    if not text or not text.strip():
        return {
            "sentiment": "NEUTRAL",
            "score": 0.0
        }
    
    try:
        # Get classifier
        classifier = get_classifier()
        
        # Analyze text
        results = classifier(text)
        
        # Extract first result
        result = results[0]
        
        # Return in correct format
        return {
            "sentiment": result['label'],  # This is the key!
            "score": float(result['score'])
        }
        
    except Exception as e:
        print(f"Error in analyze_sentiment: {e}")
        import traceback
        traceback.print_exc()
        
        # Return default on error
        return {
            "sentiment": "NEUTRAL",
            "score": 0.0
        }
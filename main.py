import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import google.generativeai as genai

# AI model configuration
genai.configure(api_key=os.getenv("GENAI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# FastAPI app initialisation
app = FastAPI()

# Request model
class TranscriptRequest(BaseModel):
    company_name: str
    transcript_text: str

# Response model
class TranscriptResponse(BaseModel):
    company_name: str
    financial_performance: Optional[str]
    market_dynamics: Optional[str]
    expansion_plans: Optional[str]
    environmental_risks: Optional[str]
    regulatory_or_policy_changes: Optional[str]

# AI summarization using Gemini 1.5 Flash
def summarize_with_ai(text: str, category: str) -> str:
    try:
        prompt = f"Summarize the following transcript for the category '{category}': {text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error in AI summarization for {category}: {str(e)}"

@app.post("/earnings_transcript_summary", response_model=TranscriptResponse)
async def summarize_transcript(request: TranscriptRequest):
    # Input validations
    if not request.transcript_text.strip():
        raise HTTPException(status_code=400, detail="Transcript text is required")
    if len(request.transcript_text) > 20000:
        raise HTTPException(status_code=400, detail="Transcript text exceeds the maximum allowed length of 20,000 tokens")

    # Transcript summary categories
    categories = [
        "financial performance",
        "market dynamics",
        "expansion plans",
        "environmental risks",
        "regulatory or policy changes"
    ]

    summaries = {}
    for category in categories:
        summaries[category.replace(" ", "_")] = summarize_with_ai(request.transcript_text, category)

    return {
        "company_name": request.company_name,
        **summaries
    }

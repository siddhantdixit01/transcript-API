# Transcript API

The Transcript API is designed to process company earnings transcripts and provide categorized summaries for key topics such as financial performance, market dynamics, expansion plans, environmental risks, and regulatory or policy changes. The API leverages Google's Gemini 1.5 Flash generative AI model for summarization.

---

## Base URL
The API runs on a FastAPI server with the base URL:
```
https://transcript-api-29zo.onrender.com
```

---

## Endpoints

### 1. `POST /earnings_transcript_summary`

#### **Description**
This endpoint accepts an earnings transcript and generates a summarized response for five predefined categories using AI.

---

### **Request**

#### **Headers**
- `Content-Type`: `application/json`

#### **Body Parameters**
The request body should be a JSON object containing the following fields:

| Field Name      | Type   | Required | Description                                            |
|------------------|--------|----------|--------------------------------------------------------|
| `company_name`   | string | Yes      | The name of the company related to the transcript.     |
| `transcript_text`| string | Yes      | The full text of the earnings transcript.              |

#### **Example Request**
```json
{
    "company_name": "Dr. Lal PathLabs",
    "transcript_text": "Thank you, Siddharth and good evening, ladies and gentlemen and a very warm welcome to all the participants on today's call to discuss our Q2 FY25 performance. I will commence by discussing the evolving market dynamics and our key achievements. Our ability to maintain our market position in the highly fragmented and competitive Indian diagnostics industry is a testament to our strong brand, exceptional service, and extensive network. We are leveraging these strengths to penetrate deeper into underserved Tier-3 and Tier-4 regions by offering affordable high-quality diagnostics to the patients. Digital integration has become imperative, and we are actively leveraging technology to enhance patient experience and operational efficiency. Currently, we are also expanding our home diagnostic services to meet the growing demand from patients who value convenience. India has a vast unserved and underserved population in terms of healthcare and diagnostics. Together, with policy impetus, tech innovation, and growing propensity to avail of quality and accurate diagnostics, the share of national brands like ours is rising. Thank you."
}
```

---

### **Response**

#### **Body**
The response will be a JSON object containing the summarized categories.

| Field Name                     | Type   | Description                                            |
|--------------------------------|--------|--------------------------------------------------------|
| `company_name`                 | string | The name of the company from the request.              |
| `financial_performance`        | string | Summary of financial performance from the transcript.   |
| `market_dynamics`              | string | Summary of market dynamics.                            |
| `expansion_plans`              | string | Summary of expansion plans.                            |
| `environmental_risks`          | string | Summary of environmental risks.                        |
| `regulatory_or_policy_changes` | string | Summary of regulatory or policy changes.               |

#### **Example Response**
```json
{
    "company_name": "Dr. Lal PathLabs",
    "financial_performance": "The company maintained its market position in a competitive Indian diagnostics market due to strong brand recognition, service, and network reach. They are expanding into underserved regions with affordable services and leveraging technology to improve patient experience and operational efficiency, including expanding home diagnostic services. The company's growth is attributed to a combination of policy support, technological innovation, and increasing demand for quality diagnostics in a large, underserved market.",
    "market_dynamics": "The Indian diagnostics market is highly fragmented and competitive. The company maintains its market position through strong branding, excellent service, and a wide network, expanding into underserved regions (Tier 3 and 4) with affordable, high-quality diagnostics. Digital integration and home diagnostic services are key growth strategies, driven by increasing patient demand for convenience and a large underserved population. Government policy, technological advancements, and a rising preference for quality diagnostics are contributing to the increased market share of national brands.",
    "expansion_plans": "The company plans to expand its reach into underserved Tier-3 and Tier-4 regions of India by offering affordable, high-quality diagnostic services. They are also expanding their home diagnostic services to meet growing consumer demand and leveraging digital integration to improve efficiency and patient experience. This expansion is driven by a large underserved market and a rising preference for national brands.",
    "environmental_risks": "The transcript does not mention any specific environmental risks. The discussion focuses on market performance within the Indian diagnostics industry, highlighting competitive advantages, market penetration strategies (including expansion into underserved areas and home diagnostics), and the role of digital integration.",
    "regulatory_or_policy_changes": "The transcript highlights the impact of policy impetus on the growth of national diagnostic brands in India. The company is leveraging this positive regulatory environment (along with technological advancements and increased patient demand) to expand its reach into underserved areas and offer affordable, high-quality diagnostics."
}
```

---

### **Error Handling**

#### **Common Errors**

| HTTP Code | Error Description                                    |
|-----------|-----------------------------------------------------|
| 400       | Bad Request: Occurs when the request body is invalid or a required field is missing. |
| 400       | Transcript text exceeds the maximum allowed length of 20,000 tokens. |
| 500       | Internal Server Error: An unexpected error occurred during summarization or processing. |

#### **Example Error Response**
```json
{
    "detail": "Transcript text is required"
}
```

---

## AI Summarization Process

### **Categories**
The API generates summaries for the following categories:
1. **Financial Performance** - Insights into the company’s financial achievements and metrics.
2. **Market Dynamics** - Observations on market trends, competition, and positioning.
3. **Expansion Plans** - Information about future plans for growth and expansion.
4. **Environmental Risks** - Potential environmental challenges impacting operations.
5. **Regulatory or Policy Changes** - Legal or policy changes affecting the company.

### **AI Prompting**
For each category, the API constructs a custom prompt:
```
Summarize the following transcript for the category '<CATEGORY>': <TRANSCRIPT_TEXT>
```
The Google Gemini 1.5 Flash model generates the summary.

---

## Deployment and API Key Management

### **Environment Variable**
The AI model requires an API key, which should be securely stored as an environment variable:
```
GENAI_API_KEY=<your_api_key>
```
Make sure to set the environment variable in your deployment environment.

---

## Limitations
- **Text Length**: The API supports transcript text up to 20,000 tokens. Requests exceeding this limit will return an error.
- **Categories**: Summarization is limited to the predefined categories.

---

## Development and Testing

### **Running Locally**
Use the following commands to run the API locally:
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn google-generativeai
   ```
2. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
   Replace `main` with the filename of your FastAPI app.

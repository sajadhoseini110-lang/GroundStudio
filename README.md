# GroundStudio

Early-stage grounding-system engineering web app.

## Run frontend
Install Node.js 20+, then in `frontend`: `npm install` and `npm run dev`.

## Run backend
Install Python 3.11+. In `backend`, create/activate a virtual environment, run `pip install -r requirements.txt`, then `uvicorn main:app --reload`. API docs: `/docs`.

## Engineering warning
This prototype is not a certified design tool. The displayed single-rod resistance is a simplified estimate. Group resistance, mutual coupling, layered soil, GPR, touch/step voltage and standard compliance are not yet validated or implemented. Do not use for final design or safety approval.

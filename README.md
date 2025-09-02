# Quick Start


## 1) Setup
```
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
export JWT_SECRET="dev-secret" # change in prod
export KONNECT_API_URL="https://sandbox.konnect.example/checkout"
export KONNECT_API_KEY="sandbox-key"
export PREMIUM_PRODUCT_ID="premium_monthly"
uvicorn app.main:app --reload --port 8000
```


## 2) Issue JWT (MVP)
```
curl -s -X POST http://127.0.0.1:8000/auth/token \
-H 'Content-Type: application/json' \
-d '{"email":"user@example.com","name":"مريم"}' | jq
```
Copy `access_token`.


## 3) Freemium Horoscope (Arabic fields)
```
curl -s -X POST http://127.0.0.1:8000/horoscope \
-H 'Content-Type: application/json' \
-d '{"الاسم":"مريم","تاريخ_الميلاد":"1993-05-11","مجالات_الاهتمام":"💼 عمل"}' | jq
```


## 4) Create Konnect Checkout (sandbox)
```
curl -s -X POST http://127.0.0.1:8000/billing/checkout \
-H 'Content-Type: application/json' \
-d '{"email":"user@example.com","return_url":"https://example.com/return"}' | jq
```
Open the returned `checkout_url` in browser (in real flow).


## 5) Simulate Konnect Webhook (activate premium)
```
curl -s -X POST http://127.0.0.1:8000/billing/webhook \
-H 'Content-Type: application/json' \
-d '{
"type":"checkout.session.completed",
"data":{
"customer_email":"user@example.com",
"status":"active",
"period_end":"2099-12-31T23:59:59Z"
}
}' | jq
```


## 6) Premium Horoscope
```
TOKEN=$(curl -s -X POST http://127.0.0.1:8000/auth/token \
-H 'Content-Type: application/json' \
-d '{"email":"user@example.com","name":"مريم"}' | jq -r '.access_token')


curl -s -X POST http://127.0.0.1:8000/horoscope \
-H "Authorization: Bearer $TOKEN" \
-H 'Content-Type: application/json' \
-d '{"الاسم":"مريم","تاريخ_الميلاد":"1993-05-11","مجالات_الاهتمام":"🌍 عام"}' | jq
```


Troubleshooting
---------------
- If `/health` shows degraded: ensure `astronomy-engine` installed and time sync OK.
- SQLite DB `horoscope.db` is created on first run; delete to reset.
- Verify Arabic JSON keys exactly as above.




─────────────────────────────────────────────────────────────────────────────
End of updated codebase
─────────────────────────────────────────────────────────────────────────────
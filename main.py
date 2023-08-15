from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def get_payment_page():
    return """
    <html>
    <head>
        <title>Fake Payment Page</title>
        <link rel="stylesheet" href="/static/styles.css">
        <script src="/static/htmx.js"></script>
    </head>
    <body>
        <h1>Enter Your Payment Details</h1>
        <form hx-post="/submit" hx-post="#payment-form" hx-swap="outerHTML">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" placeholder="JOHN DOE" required><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" placeholder="example@example.com" required><br>
            <label for="card_number">Card Number:</label>
            <input type="text" id="card_number" name="card_number" placeholder="0000 0000 0000 0000" required><br>
            <label for="expiry">Expiry:</label>
            <input type="text" id="expiry" name="expiry" required pattern="\d{2}/\d{2}" maxlength="5" placeholder="MM/YY" hx-trigger="keyup" hx-post="/auto_format_expiry" oninput="formatExpiry(this)" required><br>
            <label for="cvv">CVV:</label>
            <input type="tel" id="cvv" name="cvv" required pattern="\d{3}" maxlength="3" placeholder="123" required><br>
            <button type="submit">Submit</button>
            <script>
                function formatExpiry(input) {
                    let value = input.value;
                    value = value.replace(/[^\d]/g, ''); // Remove non-numeric characters

                    if (value.length > 2) {
                        value = value.slice(0, 2) + '/' + value.slice(2);
                    }

                    input.value = value;
                }
            </script>

        </form>
        <div id="payment-form"></div>
    </body>
    </html>
    """

@app.post("/submit", response_class=HTMLResponse)
async def submit_payment():
    return """
    <html>
    <head>
        <title>Fake Payment Page</title>
    </head>
    <body>
        <h1>Sorry, We're Not Live Yet</h1>
        <p>Don't worry, we haven't saved your credit card information. We're just testing the demand.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

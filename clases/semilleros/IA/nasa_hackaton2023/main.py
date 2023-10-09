from fastapi import FastAPI
app = FastAPI()
"""
def chat(data):
	return answer
"""
@app.get("/{data}")
async def process_data(data: str):
    # Print the data extracted from the URL
    print(f"{data}")

    # Define your custom message
    message = f"whatsapp {data}"

    # Return the custom message as a JSON response
    return {"message": message}
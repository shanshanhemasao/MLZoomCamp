"""
Here is a simple example showing how to convert the ping function to a web app.
"""


from fastapi import FastAPI
import uvicorn

#define the application
app = FastAPI(title='ping') 

# the ping function is not just function, it is also an endpoint - you can access this function using a url.
# here slash ping is the url to acess to this function, and when you set a get request to this url,you will get response.
# here at app dot get means hey app, when you receive a GET request to slash ping, run the function directly below.

@app.get("/ping") # Basically this line means when someone vist this url, run ping function
def ping():
    return "Pong"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
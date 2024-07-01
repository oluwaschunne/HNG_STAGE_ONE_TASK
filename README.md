# STAGE ONE - BACKEND TRACK

A simple basic web server cretaed with **Python-flask** to be hosted on **Vercel**, exposing an API endpoints that conforms to the criteria below:

**Endpoint:** [GET]<example.com>/api/hello?visitor_name="Mark" (Where <example.com> is your server origin)

## Response
```
{
    "client_ip": "127.0.0.1", // The IP address of the requester
    "location": "New York"', // The city of the requester
    "greeting": "Hello, Mark!, the temperature is 11 degree Celcius in New York"
}
```
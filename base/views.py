from django.shortcuts import render
import openai, os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY")

def bot(request): 
    bot_response = None 
    if api_key is not None and request.method=="POST":
        openai.api_key = api_key
        energy = request.POST.get('energy')
        cars = request.POST.get('cars')
        food = request.POST.get('food')
        plastics = request.POST.get('plastics')
        planes = request.POST.get('planes')
        prompt = (f"I understand that this is a difficult task but please don't mention that in the response. Please do your best to estimate how bad or good my carbon footprint is then give me suggestions if needed based on the information below: I drive my car {cars}. I eat dairy and meat products {food}. I use plastic bottles and straws {plastics}. I take planes and travel long distance {planes}. {energy} use renewable energy and or solar panels")
        response = openai.Completion.create(
            model = 'text-davinci-003', 
            prompt = prompt, 
            max_tokens = 256, 
            temperature = 0.2
        )
        print(response)
        bot_response = response["choices"][0]["text"]
    return render(request, 'base/calculator.html', {
        "response": bot_response
    })
  
def landing(request): 
  return render (request, "base/landing.html")

def causes(request):
  return render (request, "base/causes.html")

def calculator(request):
  return render (request, "base/calculator.html")





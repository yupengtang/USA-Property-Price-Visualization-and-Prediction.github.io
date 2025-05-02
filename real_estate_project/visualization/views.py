# visualization/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Realtor
from django.conf import settings
import joblib
import os
import numpy as np
import pandas as pd

# Define the directory where models are stored
MODEL_DIR = os.path.join(settings.BASE_DIR, "visualization", "models")

# Define model file names
MODEL_FILES = {
    "decision_tree": "decision_tree_regressor.joblib",
    "random_forest": "random_forest_regressor.joblib",
    "linear_regression": "linear_regression_model.joblib",
    "mlp": "neural_net_regressor.joblib",
}

# Load models at startup
loaded_models = {}
for model_key, model_file in MODEL_FILES.items():
    model_path = os.path.join(MODEL_DIR, model_file)
    try:
        loaded_models[model_key] = joblib.load(model_path)
        print(f"Loaded model: {model_key} from {model_path}")
    except FileNotFoundError:
        loaded_models[model_key] = None
        print(f"Model file not found: {model_path}")
    except Exception as e:
        loaded_models[model_key] = None
        print(f"Error loading model {model_key}: {e}")


def visualization_view(request):
    """
    Render the visualization page.
    """
    return render(request, "visualization.html")


# def choropleth_view(request):
#     """
#     Render the choropleth map page.
#     """
#     return render(request, "visualization.html")


def get_data(request):
    """
    Provide JSON data for realtors.
    """
    realtors = Realtor.objects.all().values(
        "brokered_by",
        "status",
        "price",
        "bed",
        "bath",
        "acre_lot",
        "street",
        "city",
        "state",
        "zip_code",
        "house_size",
        "prev_sold_date",
    )
    data = list(realtors)
    return JsonResponse(data, safe=False)


def price_query_view(request):
    """
    Handle property price prediction based on user input.
    """
    price = None
    error = None
    if request.method == "POST":
        bed = request.POST.get("bed")
        bath = request.POST.get("bath")
        zip_code = request.POST.get("zip_code")
        status = request.POST.get("status")
        acre_lot = request.POST.get("acre_lot")
        city = request.POST.get("city")
        state = request.POST.get("state")
        house_size = request.POST.get("house_size")
        selected_model = request.POST.get("model")

        if not bed or not bath or not selected_model:
            error = "Please fill in all required fields and select a model."
            return render(request, "price_query.html", {"price": price, "error": error})

        if selected_model not in loaded_models:
            error = "Invalid model selected."
            return render(request, "price_query.html", {"price": price, "error": error})

        model = loaded_models.get(selected_model)
        if model is None:
            error = "The selected model is not available."
            return render(request, "price_query.html", {"price": price, "error": error})

        try:
            bed = float(bed)
            bath = float(bath)
            acre_lot = float(acre_lot) if acre_lot else 0.0
            house_size = float(house_size) if house_size else 0.0
            zip_code = float(zip_code) if zip_code else 0.0
            status = float(status) if status else 0.0
            city = float(city) if city else 0.0
            state = float(state) if state else 0.0
            features = np.array(
                [[acre_lot, bath, bed, city, house_size, state, status, zip_code]]
            )
            predicted_log_price = model.predict(features)[0]
            predicted_price = np.expm1(predicted_log_price)
            price = round(predicted_price, 2)

        except ValueError:
            error = "Please enter valid numerical values for the fields."
        except Exception as e:
            error = f"An error occurred during prediction: {str(e)}"

    return render(request, "price_query.html", {"price": price, "error": error})

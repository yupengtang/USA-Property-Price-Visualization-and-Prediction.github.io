# USA-Property-Price-Visualization

## TODO List

- <del>Optional: Add new visualization plot to the left-down area (by taking advantage of the drag-and-pass features) if needed. Adding analytical plots (e.g., Correlation Heatmap of Key Features) by attaching images directly in this area may be a potential idea for LLMs interpretation.<del>
- <del>Implement backend to integrate machine learning models for prediction. [Linhao Bai]<del>
- <del>Incorporate LLM models to generate summaries from the existing visualization. [Yupeng Tang]<del>
- <del>Review poster.<del>
- <del>Review final report.<del>
- <del>Write documentation for code.<del>


## Steps to Run the Visualization Demo Locally

- Download all missing GeoJSON files from https://github.com/OpenDataDE/State-zip-code-GeoJSON.
- Place them in the GeoJSON directory.
- Open a terminal window.
- Navigate to the project directory.
- Run the command 'python -m http.server 8000' to start the local server.
- Open a web browser at http://localhost:8000/.
- Open and run "visualization_v4.html".

## Implemented Functionalities

### Visualization [Dongsheng Yao]

- Select between radio options to swith between USA choropleth map based on median property price and number of listing by state.
- Drag a state from the USA choropleth map to the right-top area of the page, a separate state map (breakdown by zipcode) will be generated for visualization. We currently only support to visualize median price by each zipcode area.
- Both USA and state map will show detail information via a orange tooltip when moveing the cursor of mouse over a state/zipcode.
- Drag a state from the USA choropleth map to the right-top area of the page will also generate a multi-dimensional view plot at the right-down area of the page. When moving the cursor through different zipcode areas, the corresponding line from the multi-dimensional view plot will be highlighted in orange color.
- We can visualize a differnt state by simply dragging it to the right-top area to replace the current map.
- Notes #1: The current implementation fetches all the geojson data when running for the first time, so it may take several seconds to load the state map.
- Notes #2: Dragging a zipcode area from the state map to the left-down area of the page will pass all the data to it for future functionalities (it only console.log the data currently).


## How to use the LLM functionality
- Obtain an LLM API key from GitHub Marketplace
  - Go to 'https://github.com/marketplace/models/azure-openai/gpt-4o'.
  - Click 'Get API key' at the right corner.
  - Click 'Get developer key'.
  - Click 'Generate new token' to create a token, make sure it's classic.
  - Follow the instructions from the page to set up the local environment variable.
- Install node.js and npm.
- Navigate to the express directory.
- Run 'npm install' to read the 'package.json' file to install all required dependiencies.
- Run 'node server.js' to start the express server on port 3000 of local host.
- Now run the Django project and the LLM functionality should work as expected.

## How to run Django
- All the joblib files are here: https://drive.google.com/drive/folders/1j0TUMN69nD3dIKsSSOjNMGj4u8WSHRPB?usp=drive_link
- Install all the required python library such as Django, pandas...
- Enter the real_estate_project
```
python manage.py runserver

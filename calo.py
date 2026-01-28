import cv2
from ultralytics import YOLO
import numpy as np

# Load the YOLOv8 model
model = YOLO("best.pt")


# Define class names (ensure these match your trained model's classes)
class_names = model.names

# Define calorie density for each class (calories per 100 pixels)
calorie_density = {
    'Apple': 0.3,         # 0.5 calories per 100 pixels
    'Chapathi': 0.2,      # 1.2 calories per 100 pixels
    'Chicken Gravy': 0.5, # 1.8 calories per 100 pixels
    'Fries': 0.1,         # 3.1 calories per 100 pixels
    'Idli': 0.12,         # 0.58 calories per 100 pixels
    'Pizza': 0.7,         # 2.8 calories per 100 pixels
    'Rice': 0.2,          # 1.3 calories per 100 pixels
    'Soda': 0.6,          # 1.4 calories per 100 pixels
    'Tomato': 0.18,       # 0.18 calories per 100 pixels
    'Vada': 0.3,          # 0.3 calories per 100 pixels
    'banana': 0.10,       # 0.89 calories per 100 pixels
    'burger': 0.3         # 2.5 calories per 100 pixels
}

def calculate_area(mask):
    """Calculate the area of the segmented region from a mask."""
    return np.sum(mask > 0)  # Count non-zero pixels

def predcalo(path):
    
    clslist=[]
    arelis=[]
    calolis=[]
    
    image = cv2.imread(path)
    results = model(image)

    # Visualize the results on the frame
    annotated_frame = results[0].plot()

    # Loop through the results to calculate segmented areas and calories
    for i, result in enumerate(results[0].masks.data):
        # Convert mask to numpy array
        mask = result.cpu().numpy()

        # Get the class ID and name for the current mask
        class_id = int(results[0].boxes.cls[i])  # Class ID for the object
        class_name = class_names[class_id]  # Map class ID to class name

        # Calculate the segmented area
        area = calculate_area(mask)
        print(f"Object: {class_name}, Segmented Area: {area} pixels")
       
        clslist.append(class_name)
        arelis.append(area)
        # Calculate the food calories
        if class_name in calorie_density:
            calories = (area / 100) * calorie_density[class_name]
            print(f"Estimated Calories: {calories:.2f} kcal")
            calolis.append(calories)
           
        else:
            print(f"Calorie information not available for {class_name}")
           
        
    # Save the annotated frame with predictions
    cv2.imwrite("img.jpg", annotated_frame)
    
    return clslist,arelis,calolis

    # Wait for keypress to close (if necessary)
    cv2.waitKey(0)

#val=predcalo("1_jpg.rf.0a7939e80c8e6a80da6e7dbf4bfd856f.jpg")
#print(val)
# Phone Catalogue Program

# Define a dictionary to hold phone specifications
phone_catalogue = {
    "Samsung A15": {
        "Processor": "Helio G99",
        "Screen size": "6.5 inches",
        "Battery capacity": "5000 mAh",
        "Camera": "50 MP main, 5 MP ultrawide and 2MP macro"
    },
    "Xiaomi Redmi Note 8": {
        "Processor": "Snapdragon 665",
        "Screen size": "6.3 inches",
        "Battery capacity": "4000 mAh",
        "Camera": "48 MP main, 8 MP ultrawide, 2MP macro and 2MP depth"
    },
    "Xiaomi 13T": {
        "Processor": "Dimensity 8200",
        "Screen size": "6.67 inches",
        "Battery capacity": "5000 mAh",
        "Camera": "50 MP main, 50 MP telephoto and 12 MP ultrawide"
    }
}

def display_phone_models():
    """Display the available phone models to the user."""
    print("\nAvailable phone models:")
    for phone in phone_catalogue.keys():
        print(f"- {phone}")

def get_specification(phone_model, spec):
    """Return the requested specification for the given phone model."""
    # Check if the phone model and specification exist in the catalogue
    if phone_model in phone_catalogue and spec in phone_catalogue[phone_model]:
        return phone_catalogue[phone_model][spec]
    else:
        return "Specification not found."

def main():
    """Main function to run the phone catalogue program."""
    while True:  # Loop to allow multiple inquiries
        # Display the phone models
        display_phone_models()
        
        # Ask the user to input a phone model or exit
        phone_model = input("\nPlease enter the phone model you want to see specifications for (or type 'exit' to quit): ").strip()
        
        # Check for exit condition
        if phone_model.lower() == 'exit':  # Normalize input for exit
            print("Thank you for using the phone dictionary. Goodbye!")
            break
        
        # Normalize the phone model input to match the keys (case insensitive)
        normalized_phone_model = phone_model.lower()  # Convert to lowercase for comparison
        
        # Find the actual phone model key by checking lowercase versions
        matched_phone_model = next((key for key in phone_catalogue.keys() if key.lower() == normalized_phone_model), None)

        # Check if the phone model is valid
        if matched_phone_model is None:
            print("Invalid phone model. Please try again.")
            continue  # Restart the loop for another inquiry

        # Ask the user for the specification they want to see
        print("\nAvailable specifications: Processor, Screen size, Battery capacity, Camera")
        spec = input("Please enter the specification you want to see: ").strip()  # No normalization here

        # Check if the specification is valid by matching it directly
        # Normalize the specification input for comparison
        normalized_spec = spec.lower()  # Convert specification input to lowercase
        matched_spec = next((key for key in phone_catalogue[matched_phone_model].keys() if key.lower() == normalized_spec), None)

        # Get and display the requested specification
        if matched_spec:
            specification = phone_catalogue[matched_phone_model][matched_spec]
            print(f"\n{matched_phone_model} - {matched_spec}: {specification}")
        else:
            print("Specification not found.")

# Run the main function
if __name__ == "__main__":
    main()

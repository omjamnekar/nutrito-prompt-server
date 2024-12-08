class Prompts:


    _initialJSONdataFramePrompt = """
            Provide the product's composition and quantities as structured JSON with the following keys. Do not include any additional text or explanations, only the JSON and dont mention ```json ```` :

            {
                "allergenInformation": " // allergen information //",
                "barcode": " // barcode //",
                "certifications": ["FSSAI"],
                "countryOfOrigin": " // country of origin //",
                "dietaryInformation": " // dietary information //",
                "expiryDate": " // expiry date //",
                "ingredients": [
                    {"name": "wheat flour", "quantity": "70g"},
                    {"name": "palm oil", "quantity": "13g"}
                ],
                "isAddictive": true,
                "price": " // price of the product //",
                "manufacturer": {"name": " // manufacturer name //", "address": " // address //"},
                "name": " // product name //",
                "nutritionalInformation": {
                    "calcium": "180 mg",
                    "carbohydrates": "59.1 g",
                    "cholesterol": "0 mg",
                    "dietary fiber": "3.6 g"
                },
                "productType": " // product type //",
                "servingSize": " // serving size //",
                "storageInstructions": " // storage instructions //",
                "usageInstructions": " // usage instructions //",
                "weight": " // weight //",
                "warnings": " // warnings //",
                "additionalInformation": " // additional information //",
                "link": " // product link //",
                "website": " // product website //"
            }
            """

    
    _ratioSpecifiedPrompt = '''
    I need a nutritional analysis of this data to determine if it is healthy to eat. Provide the data in pure JSON format no other text like ```json (important), this is the format:
     {
   
        "ingredientAnalysis": [
            {
                "comment": "Whole grain wheat is a good source of fiber and other nutrients.",
                "healthRating": 10,
                "ingredient": "Whole Grain Wheat"
            },
            {
                "comment": "Sugar is a source of empty calories and can contribute to weight gain.",
                "healthRating": 5,
                "ingredient": "Sugar"
            },
          
        ],
        "nutritionalAnalysis": {
            "calcium": {
                "feedbackRatio": 9,
                "value": "15%"
            },
            "calories": {
                "feedbackRatio": 7,
                "value": "240 calories"
            },
            "protein": {
                "feedbackRatio": 7,
                "value": "4g"
            },
            "saturatedFat": {
                "feedbackRatio": 9,
                "value": "2.5g"
            },
            "vitaminC": {
                "feedbackRatio": 3,
                "value": "2%"
            }
        }
      }
     '''
    
    _otherPrompt = '''
   Collect all data available in the image regarding the product composition and its quantities. Provide the data in **strict JSON format** with the following keys and no additional text:

{
    "allergenInformation": "// Information about allergens //",
    "conclusion": "// Your conclusion about the product from a nutritional perspective //",
    "overallHealthRating": "// A number between 1-10 indicating healthiness //",
    "recommendations": "// Buy or not based on health concerns //",
    "servingSize": "// Quantity per serving size in appropriate units //"
}
    '''

    _healthPrompt = '''
        Collect all data available in the image regarding the product composition and its quantities. Provide the data in JSON format with the following consistent keys and  dont add ```json```:

        {
            "health_considerations": [
                {
                    "ingredient": "// ingredient name //",
                    "negative": [
                        "// negative health impact //",
                        "// negative health impact //"
                    ],
                    "positive": [
                        "// positive health impact //",
                        "// positive health impact //"
                    ]
                },
                {
                    "ingredient": " //second ingredient name //",
                    "negative": [
                        "// negative health impact //",
                        "// negative health impact //"
                    ],
                    "positive": [
                        "// positive health impact //",
                        "// positive health impact //"
                    ]
                }
            ]
        
        }
    '''
   
    @property
    def initialJSONdataFramePrompt(self):
        return self._initialJSONdataFramePrompt
    @property
    def ratioSpecifiedPrompt(self):
        return self._ratioSpecifiedPrompt
    @property
    def otherPrompt(self):
        return self._otherPrompt
    @property
    def healthPrompt(self):
        return self._healthPrompt

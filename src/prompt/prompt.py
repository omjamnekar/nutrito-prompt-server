class Prompts:


    _initialJSONdataFramePrompt ="""
    Collect all data available in the image regarding the product composition and its quantities. Provide the data in JSON format with the following consistent keys. Do not include any extraneous text or explanations, only the JSON formatted data as specified below and dont add ```json```:

{
    "allergenInformation": " // allergen information //",
    "barcode": " // barcode //",
    "certifications": [
        "FSSAI"
    ],
    "countryOfOrigin": " // country of origin //",
    "dietaryInformation": " // dietary information //",
    "expiryDate": " // expiry date //",
    "ingredients": [
        {
            "name": "wheat flour",
            "quantity": "70g"
        },
        { 
            "name": "palm oil",
            "quantity": "13g"
        }
    ],
    "isAddictive": in true or false format,
    "price": " // price of the product //",
    "manufacturer": //manufacturer datails in dictionary//,
    "name": //product name//,
    "nutritionalInformation": {
        "calcium": "180 mg",
        "carbohydrates": "59.1 g",
        "cholesterol": "0 mg",
        "dietary fiber": "3.6 g"
        // add more keys as per the image //
    },
    "productType": " // product type //",
    "servingSize": " // serving size in any measure value e.g cup, spoon , no of chips //",
    "storageInstructions": " // storage instructions //",
    "usageInstructions": " // usage instructions //",
    "weight": " // weight of the product //",
    "warnings": " // warnings //"
    "additionalInformation": " // additional information //"
    "link": " // link to the product //"
    "website": " // website of the product //"

    }

Take the time to pull the maximum amount of data. Ensure that the keys remain consistent in subsequent runs to prevent inconsistencies.
        """
    
    _ratioSpecifiedPrompt = '''
    I have data for a product, and I need a nutritional analysis of this data to determine if it is healthy to eat. Provide the data in JSON format with the following consistent keys and dont write anything other then format not even ```JSON ``` 
        this is the format:
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
    Collect all data available in the image regarding the product composition and its quantities. Provide the data in JSON format with the following consistent keys: dont write anything other then format not even ```JSON ```
        this is the format:
    {
    
        "allergenInformation": "// //",
        "conclusion": " // provide me your conclusion for this app as nutritioniest or healthcarer //",
        "overallHealthRating": //ratio number between 1-10 on the bases of you opinion about this product as per human health consideration//,
        "recommendations": " //any recommendations that leads to buy the product or not if product is unhealthy for human //",
        "servingSize": " // serving size in any measure as per product to give idea for how long product will long last//",   
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

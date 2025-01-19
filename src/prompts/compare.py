class ComparisionPrompts:
    _compareProductsPrompt = """
        Compare the following two products based on their details.  differences, similarities, and provide an overall comparison conclusion. provide all data in json fromat every thing in key value structure even comment,notes products as well no extra text or sprecial character, give me data in below structure

{
        "starting_comment": "give your starting comment ",
        product 1:
       {
        "Name": {product1_name}
        "Price": {product1_price}
        "Manufacturer": {product1_manufacturer}
        "Composition": {product1_composition}
        "NutritionalInformation": {product1_nutritional_info}
        "AllergenInformation": {product1_allergen_info}
        "Certifications": {product1_certifications}
        "SustainabilityScore": {product1_sustainability_score}
        "CustomerRatings": {product1_customer_ratings}
        "Packaging": {product1_packaging}
        "DietarySuitability": {product1_dietary_suitability}
        "AdditionalInformation": {product1_additional_info}
       }

        product 2:
        {
        "Name": {product2_name}
        "Price": {product2_price}
        "Manufacturer": {product2_manufacturer}
        "Composition": {product2_composition}
        "NutritionalInformation": {product2_nutritional_info}
        "AllergenInformation": {product2_allergen_info}
        "Certifications": {product2_certifications}
        "SustainabilityScore": {product2_sustainability_score}
        "CustomerRatings": {product2_customer_ratings}
        "Packaging": {product2_packaging}
        "DietarySuitability": {product2_dietary_suitability}
        "AdditionalInformation": {product2_additional_info}
        }

       /// Please provide a comparison summary with the following structure:///
        {
            "keyDifferences": [
                {"aspect": "Aspect name", "product1": "value for product 1", "product2": "value for product 2"}
            ],
            "keySimilarities": [
                {"aspect": "Aspect name", "value": "shared value"}
            ],
            "overallComparisonConclusion": "Summary of which product is better and why, based on the provided data."
       // so on

          }

    }
    """
    @property
    def compareProductsPrompt(self):
        return self._compareProductsPrompt

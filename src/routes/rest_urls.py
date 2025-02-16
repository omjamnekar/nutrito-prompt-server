class Prompt_Url:
    #auth
    login = "/v1/login"
    check_Server = "/v1/gen/checkServerRunning"
    
    # nutrilizs
    initial_prompt ="/v1/gen/nutrilization/initialPrompt"
    ratio_prompt = "/v1/gen/nutrilization/ratioPrompt"
    health_prompt = "/v1/gen/nutrilization/healthPrompt"
    conclusion_prompt ="/v1/gen/nutrilization/conclusionPrompt"



    #compare product
    com_initial_prompt ="/v1/gen/compareProduct/initialPrompt"
    com_ratio_prompt = "/v1/gen/compareProduct/ratioPrompt"
    com_health_prompt = "/v1/gen/compareProduct/healthPrompt"
    com_conclusion_prompt ="/v1/gen/conclusionPrompt/conclusionPrompt"
    com_compare_product= "/v1/gen/conpareProduct/provideData"

    #Suggest alternative 
    suggestAlternative ="/v1/gen/alternative/suggestalternative"


    #alternative products
    alternativeSuggestion="/api/suggestions"



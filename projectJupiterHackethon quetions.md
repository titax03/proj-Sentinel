* how to detect fake news as there are many fake things 
* how people will get benefit from this . 





###### ollam problem

* The Hallucination Loop:
* The Problem: Smaller local models (like Llama 3 8B) are faster but slightly less "smart" than the giant Gemini/GPT-4 models. If your prompt isn't extremely strict, the model might invent fake locations instead of extracting them from the text. The Reality: You will need to spend time "Prompt Engineering"—writing very specific instructions like: "Extract ONLY the location name. Do not add any conversational text."



* The Streamlit Reload Trap:
* Problem: Streamlit (the dashboard framework) re-runs your entire Python script from top to bottom every time you click a button on the screen. If it re-runs the LLM classification on 50 tweets every time you click "Filter Map," your app will freeze for 5 minutes. The Reality: You will have to learn a Streamlit trick called @st.cache\_data to save the AI's results so it only does the heavy lifting once


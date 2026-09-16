import gradio as gr
import pandas as pd
import joblib

# Load trained model

model = joblib.load("student_dropout_model.pkl")

# Get the original feature names

feature_names = list(model.named_steps["preprocessor"].feature_names_in_)

# Identify numerical and categorical columns

preprocessor = model.named_steps["preprocessor"]

numeric_features = list(
preprocessor.transformers_[0][2]
)

categorical_features = list(
preprocessor.transformers_[1][2]
)

# Create input components

inputs = []

for column in feature_names:

```
if column in numeric_features:
    component = gr.Number(
        label=column
    )

else:
    component = gr.Textbox(
        label=column,
        placeholder=f"Enter {column}"
    )

inputs.append(component)
```

def predict_student(*values):

```
student_data = {}

for column, value in zip(feature_names, values):
    student_data[column] = value

student_df = pd.DataFrame([student_data])

# Prediction
prediction = model.predict(student_df)[0]

# Probability
probabilities = model.predict_proba(student_df)[0]
classes = list(model.classes_)

# Find dropout probability
if 1 in classes:
    dropout_probability = probabilities[classes.index(1)]
elif "Yes" in classes:
    dropout_probability = probabilities[classes.index("Yes")]
elif "Dropout" in classes:
    dropout_probability = probabilities[classes.index("Dropout")]
else:
    dropout_probability = probabilities[-1]

# Prediction text
if prediction == 1:
    prediction_text = "Dropout"
elif prediction == 0:
    prediction_text = "No Dropout"
else:
    prediction_text = str(prediction)

# Risk category
if dropout_probability < 0.30:
    risk = "🟢 Low Risk"
    message = "The student has a low predicted dropout probability."

elif dropout_probability < 0.60:
    risk = "🟡 Medium Risk"
    message = "The student has a medium predicted dropout probability."

else:
    risk = "🔴 High Risk"
    message = "The student has a high predicted dropout probability."

return (
    prediction_text,
    f"{dropout_probability * 100:.2f}%",
    risk,
    message
)
```

# ---------- Custom CSS ----------

custom_css = """
.gradio-container {
max-width: 1150px !important;
margin: auto !important;
}

.header {
text-align: center;
padding: 30px 10px;
}

.header h1 {
font-size: 34px;
font-weight: 800;
}

.header p {
opacity: 0.65;
}

.card {
border-radius: 20px !important;
padding: 25px !important;
}

.result {
text-align: center;
padding: 20px;
border-radius: 15px;
margin-bottom: 12px;
}

.result-value {
font-size: 28px;
font-weight: 800;
margin-top: 8px;
}

.predict-btn {
margin-top: 18px;
border-radius: 12px !important;
font-size: 16px !important;
font-weight: 700 !important;
}
"""

# ---------- Gradio Application ----------

with gr.Blocks(
title="Student Dropout Prediction",
css=custom_css,
theme=gr.themes.Soft(
primary_hue="indigo",
secondary_hue="slate"
)
) as demo:

```
gr.HTML("""
<div class="header">
    <h1>🎓 Student Dropout Prediction</h1>
    <p>Student Risk Assessment using Machine Learning</p>
</div>
""")

with gr.Row():

    with gr.Column(
        scale=1,
        elem_classes="card"
    ):

        gr.Markdown("## 👤 Student Information")
        gr.Markdown(
            "Enter the student's information below."
        )

        for component in inputs:
            component.render()

        predict_button = gr.Button(
            "🔍 Predict Dropout Risk",
            variant="primary",
            size="lg",
            elem_classes="predict-btn"
        )

    with gr.Column(
        scale=1,
        elem_classes="card"
    ):

        gr.Markdown("## 📊 Risk Assessment")

        prediction_result = gr.Textbox(
            label="Prediction",
            interactive=False
        )

        probability_result = gr.Textbox(
            label="Dropout Probability",
            interactive=False
        )

        risk_result = gr.Textbox(
            label="Risk Category",
            interactive=False
        )

        message_result = gr.Textbox(
            label="Assessment",
            lines=3,
            interactive=False
        )

predict_button.click(
    fn=predict_student,
    inputs=inputs,
    outputs=[
        prediction_result,
        probability_result,
        risk_result,
        message_result
    ]
)
```

demo.launch()

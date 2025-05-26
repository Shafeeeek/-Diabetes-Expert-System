from experta import *
import tkinter as tk
from tkinter import messagebox


def create_diabetes_questions():
    return {
        "Pre-Diabetes": sorted([
            {"question": "What is responsible for destroying insulin-producing cells in Type 1 diabetes?","choices": {"A": "The liver", "B": "The immune system", "C": "The kidneys", "D": "The pancreas"},"weight": 1, "correct_answer": "B"},
            {"question": "What does insulin regulate in the body?","choices": {"A": "Blood pressure", "B": "Heart rate", "C": "Blood sugar levels", "D": "Body temperature"},"weight": 2, "correct_answer": "C"},
            {"question": "Which of the following is a common symptom of diabetes?","choices": {"A": "Frequent urination", "B": "Blurred vision", "C": "Joint pain", "D": "Hair loss"},"weight": 1, "correct_answer": "A"}
        ], key=lambda x: x['weight']),

        "Type 1 Diabetes": sorted([
            {"question": "What is insulin resistance?", "choices": {"A": "When the body produces too much insulin","B": "When the body's cells do not respond properly to insulin","C": "When the pancreas stops producing insulin","D": "When insulin is destroyed by the immune system"},"weight": 3, "correct_answer": "B"},
            {"question": "Which factor increases the risk of developing diabetes?","choices": {"A": "Obesity", "B": "Low blood pressure", "C": "High cholesterol","D": "Vitamin D deficiency"}, "weight": 4, "correct_answer": "A"},
            {"question": "Which organ produces insulin?", "choices": {"A": "Liver", "B": "Kidneys", "C": "Pancreas", "D": "Spleen"}, "weight": 3,"correct_answer": "C"}
        ], key=lambda x: x['weight']),

        "Type 2 Diabetes": sorted([
            {"question": "What distinguishes Type 1 from Type 2 diabetes?","choices": {"A": "Type 1 is caused by diet, while Type 2 is genetic.","B": "Type 1 is an autoimmune reaction, while Type 2 is related to lifestyle.","C": "Type 1 occurs in adults, while Type 2 occurs in children.","D": "Type 1 requires oral medication, while Type 2 requires insulin."}, "weight": 5, "correct_answer": "B"},
            {"question": "Which complication can result from uncontrolled diabetes?","choices": {"A": "Heart disease and kidney failure", "B": "Improved vision", "C": "Weight loss","D": "Increased energy"}, "weight": 6, "correct_answer": "A"},
            {"question": "How does regular exercise affect blood sugar levels?","choices": {"A": "It has no effect.", "B": "It increases blood sugar levels.","C": "It lowers blood sugar levels.", "D": "It causes hypoglycemia permanently."}, "weight": 5,"correct_answer": "C"}
        ], key=lambda x: x['weight']),

        " Insulin Resistance": sorted([
            {"question": "What does the HbA1c test measure?","choices": {"A": "Daily blood sugar levels", "B": "Average blood sugar levels over 2-3 months","C": "Insulin production", "D": "Cholesterol levels"}, "weight": 7, "correct_answer": "B"},
            {"question": "Which of these are types of oral medications for diabetes?","choices": {"A": "Metformin, sulfonylureas, and DPP-4 inhibitors", "B": "Insulin injections only","C": "Vitamins and supplements", "D": "Antibiotics"}, "weight": 8, "correct_answer": "A"},
            {"question": "What is diabetic ketoacidosis (DKA)?","choices": {"A": "A mild form of diabetes", "B": "A life-threatening complication of diabetes","C": "A dietary supplement", "D": "A type of insulin pump"}, "weight": 7,"correct_answer": "B"}
        ], key=lambda x: x['weight']),

        "Gestational Diabetes": sorted([
            {"question": "What type of diet is recommended for people with diabetes?","choices": {"A": "High-sugar, low-fiber", "B": "Low-sugar, high-fiber", "C": "High-fat, low-protein","D": "Unrestricted diet"}, "weight": 9, "correct_answer": "B"},
            {"question": "How does stress affect blood sugar levels?","choices": {"A": "It has no effect.", "B": "It decreases blood sugar levels.","C": "It increases blood sugar levels.", "D": "It stabilizes blood sugar levels."},"weight": 10, "correct_answer": "C"},
            {"question": "Why is glucose monitoring important for managing diabetes?","choices": {"A": "To track daily calorie intake", "B": "To adjust insulin doses and manage blood sugar levels","C": "To monitor cholesterol levels", "D": "To measure blood pressure"}, "weight": 9,"correct_answer": "B"}
        ], key=lambda x: x['weight']),

        "Diabetic Complications": sorted([
            {"question": "What is the benefit of using an insulin pump?","choices": {"A": "It eliminates the need for glucose monitoring.","B": "It provides more precise insulin delivery.", "C": "It cures diabetes.","D": "It reduces the need for dietary restrictions."}, "weight": 11, "correct_answer": "B"},
            {"question": "What does the glycemic index measure?","choices": {"A": "The speed at which a food raises blood sugar levels", "B": "The fat content of food","C": "The protein content of food", "D": "The vitamin content of food"}, "weight": 12,"correct_answer": "A"},
            {"question": "How is poor sleep associated with diabetes?","choices": {"A": "It has no association.", "B": "It decreases diabetes risk.","C": "It increases diabetes risk.", "D": "It improves insulin sensitivity."}, "weight": 11,"correct_answer": "C"}
        ], key=lambda x: x['weight']),

        "Diabetes Management": sorted([
            {"question": "Do genetics play a significant role in diabetes risk?", "choices": {"A": "Yes", "B": "No"},"weight": 13, "correct_answer": "A"},
            {"question": "Is gestational diabetes a temporary form of diabetes during pregnancy?","choices": {"A": "Yes", "B": "No"}, "weight": 14, "correct_answer": "A"},
            {"question": "Is hypoglycemia associated with low blood sugar levels?", "choices": {"A": "Yes", "B": "No"},"weight": 13, "correct_answer": "A"}
        ], key=lambda x: x['weight']),

        "Advanced Diabetes Research": sorted([
            {"question": "Is artificial pancreas technology an advancement in diabetes research?","choices": {"A": "Yes", "B": "No"}, "weight": 15, "correct_answer": "A"},
            {"question": "Can artificial intelligence help predict blood sugar trends?","choices": {"A": "Yes", "B": "No"}, "weight": 16, "correct_answer": "A"},
            {"question": "Are accessibility and affordability concerns related to advanced diabetes treatments?","choices": {"A": "Yes", "B": "No"}, "weight": 15, "correct_answer": "A"}
        ], key=lambda x: x['weight'])
    }
    return questions


def give_recommendations(diagnosis, family_history=None, activity_level=None, smoking_status=None, diet_type=None):
    recommendations = f"Diagnosis: {diagnosis}\n"
    if diagnosis == "No Diabetes":
        recommendations += (
            "✅ You are not diabetic. Here's how to stay that way:\n"
            "- Maintain a healthy diet.\n"
            "- Exercise regularly.\n"
            "- Monitor your weight and blood sugar occasionally.\n"
            "- Get enough sleep and avoid stress.\n"
        )
    elif diagnosis == "Prediabetes":
        recommendations += (
            "⚠️ You are at risk (Prediabetes). Take action:\n"
            "- Adopt a low-sugar, high-fiber diet.\n"
            "- Lose 5-10% of your body weight.\n"
            "- Get regular blood sugar tests.\n"
            "- Exercise at least 30 mins/day.\n"
        )
    elif diagnosis == "Type 2 Diabetes":
        recommendations += (
            "❗ You have Type 2 Diabetes. Management tips:\n"
            "- Monitor blood sugar daily.\n"
            "- Take prescribed medications or insulin.\n"
            "- Control carbs and sugars in your diet.\n"
            "- Get regular checkups and foot exams.\n"
        )
    elif diagnosis == "Type 1 Diabetes":
        recommendations += (
            "❗ You have Type 1 Diabetes. This requires medical support:\n"
            "- Insulin therapy is necessary.\n"
            "- Continuous glucose monitoring is advised.\n"
            "- Meal planning and carb counting are important.\n"
            "- Stay in touch with your doctor regularly.\n"
        )
    if family_history == "Yes":
        recommendations += "\n⚠️ Family history of diabetes detected. Regular screening is critical."
    if activity_level == "Sedentary":
        recommendations += "\n⚠️ Sedentary lifestyle: Aim for 30+ mins of daily exercise."
    if smoking_status == "Yes":
        recommendations += "\n⚠️ Smoking increases diabetes complications. Seek cessation support."
    if diet_type == "High-Sugar":
        recommendations += "\n⚠️ High-sugar diet: Switch to low-sugar, high-fiber meals."
    recommendations += (
        "\n💡 General Prevention Tips:\n"
        "- Avoid smoking & alcohol.\n"
        "- Manage stress through meditation or hobbies.\n"
        "- Keep a regular sleep schedule.\n"
    )
    return recommendations

class ResultFact(Fact):
    score = Field(int, mandatory=True)
    family_history = Field(str, mandatory=True)      # "Yes" or "No"
    activity_level = Field(str, mandatory=True)      # "Active", "Moderate", "Sedentary"
    diet_type = Field(str, mandatory=True)           # "Healthy", "Moderate", "High-Sugar"
    smoking_status = Field(str, mandatory=True)      # "Yes" or "No"



class DiabetesExpertSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.diagnosis = ""

    # RULE 1: Very Low Risk
    @Rule(ResultFact(score=P(lambda s: s <= 15)))
    def rule_very_low(self):
        print("✅ Very low risk. Keep up the healthy habits.")
        self.diagnosis = "Healthy"

    # RULE 2: Low Risk
    @Rule(ResultFact(score=P(lambda s: 16 <= s <= 30)))
    def rule_low(self):
        print("✅ Low risk. Maintain a good lifestyle.")
        self.diagnosis = "Low Risk"

    # RULE 3: Moderate Risk (Prediabetes)
    @Rule(ResultFact(score=P(lambda s: 31 <= s <= 50)))
    def rule_moderate(self):
        print("⚠️ Prediabetes risk. Recommend lifestyle changes.")
        self.diagnosis = "Prediabetes"

    # RULE 4: High Risk – Type 1
    @Rule(ResultFact(score=P(lambda s: 51 <= s <= 70)))
    def rule_type1(self):
        print("❗ Possible Type 1 Diabetes. Seek medical advice.")
        self.diagnosis = "Type 1 Diabetes"

    # RULE 5: Very High Risk – Type 2
    @Rule(ResultFact(score=P(lambda s: s > 70)))
    def rule_type2(self):
        print("❗ High likelihood of Type 2 Diabetes.")
        self.diagnosis = "Type 2 Diabetes"

    # RULE 6: Sedentary lifestyle increases risk
    @Rule(ResultFact(activity_level="Sedentary"))
    def rule_sedentary(self):
        print("⚠️ Sedentary lifestyle contributes to diabetes risk.")

    # RULE 7: Family history increases concern
    @Rule(ResultFact(family_history="Yes", score=P(lambda s: s > 50)))
    def rule_family_risk(self):
        print("⚠️ High score + family history = critical risk.")
        self.diagnosis = "Type 2 Diabetes (Family Risk)"

    # RULE 8: Unhealthy diet and smoking
    @Rule(ResultFact(diet_type="High-Sugar", smoking_status="Yes"))
    def rule_diet_smoking(self):
        print("⚠️ High-sugar diet + smoking = increased complications.")


class DiabetesGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Diabetes Expert System")
        self.root.geometry("600x600")
        self.root.configure(bg="#e6f2ff")  # Light blue background for a clean look

        self.question_data = create_diabetes_questions()
        self.questions = []
        for level in self.question_data.values():
            self.questions.extend(level)

        self.current_index = 0
        self.total_score = 0
        self.setup_widgets()

    def setup_widgets(self):
        self.q_frame = tk.Frame(self.root, bg="#e6f2ff")
        self.q_frame.pack(pady=20)

        self.question_label = tk.Label(
            self.q_frame,
            text="",
            font=("Arial", 15, "bold"),
            wraplength=500,
            justify="left",
            fg="#003366",  # Darker blue for contrast
            bg="#e6f2ff"
        )
        self.question_label.pack(pady=15)

        self.selected_option = tk.StringVar()

        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(
                self.q_frame,
                text="",
                variable=self.selected_option,
                value="",
                font=("Arial", 12),
                bg="#ffffff",  # White buttons
                fg="#003366",
                selectcolor="#cce0ff",  # Light blue highlight on selection
                activebackground="#d9eaff",
                activeforeground="#003366",
                anchor="w",
                padx=10,
                indicatoron=0,  # Makes it look like a button
                relief="raised",
                bd=2,
                width=50,
                height=2
            )
            btn.pack(pady=5, fill="x")
            self.option_buttons.append(btn)

        self.next_btn = tk.Button(
            self.root,
            text="Next ➡",
            command=self.next_question,
            state="disabled",
            font=("Helvetica", 12, "bold"),
            bg="#007acc",
            fg="white",
            padx=10,
            pady=5,
            activebackground="#005f99",
            activeforeground="white",
            relief="groove",
            bd=3
        )
        self.next_btn.pack(pady=20)

        self.display_question()

    def display_question(self):
        if self.current_index >= len(self.questions):
            self.finish_result()
            return

        q_data = self.questions[self.current_index]
        self.question_label.config(text=f"Q{self.current_index + 1}: {q_data['question']}")
        choices = list(q_data["choices"].items())
        for i, (key, val) in enumerate(choices):
            self.option_buttons[i].config(text=f"{key}. {val}", value=key)
        self.selected_option.set("")
        self.selected_option.trace("w", self.enable_next_button)

    def enable_next_button(self, *args):
        if self.selected_option.get():
            self.next_btn.config(state="normal")
        else:
            self.next_btn.config(state="disabled")

    def next_question(self):
        if not self.selected_option.get():
            messagebox.showwarning("Incomplete", "Please select an option before proceeding.")
            return
        selected = self.selected_option.get()
        correct = self.questions[self.current_index]["correct_answer"]
        weight = self.questions[self.current_index]["weight"]
        if selected == correct:
            self.total_score += weight
        self.current_index += 1
        self.display_question()

    def finish_result(self):
        engine = DiabetesExpertSystem()  # Use DiabetesExpertSystem instead of DiabetesExpert
        engine.reset()

        # Ensure all mandatory fields are declared
        engine.declare(ResultFact(
            score=self.total_score,
            family_history="Yes",  # Provide value for family_history
            activity_level="Sedentary",  # Provide value for activity_level
            diet_type="High-Sugar",  # Provide value for diet_type
            smoking_status="No"  # Provide value for smoking_status
        ))

        engine.run()

        if self.total_score <= 30:
            risk_level = "Low Risk"
        elif 31 <= self.total_score <= 70:
            risk_level = "Moderate Risk"
        elif 71 <= self.total_score <= 100:
            risk_level = "High Risk"
        else:
            risk_level = "Very High Risk"

        full_recommendation = give_recommendations(
            engine.diagnosis,
            family_history="Yes",
            activity_level="Sedentary",
            smoking_status="No",
            diet_type="High-Sugar"
        )

        messagebox.showinfo(
            "Diabetes Assessment Result",
            f"🩺 Your Diabetes Result Score: {self.total_score}/144\n"
            f"📉 Risk Category: {risk_level}\n\n"
            f"{full_recommendation}"
        )
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = DiabetesGUI(root)
    root.mainloop()
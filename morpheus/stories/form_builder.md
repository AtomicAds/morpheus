# Hackathon PRD: Form Builder Application

You are building a Form Builder like [Google Forms](https://forms.new). The application must allow **Admins** to create forms, **Users** to submit responses, and both parties to access analytics. Deliver the complete application in one submission.

---

## Functional Requirements

### **Admin User**
Admins should be able to:
1. **Create Forms:**
   - Create unlimited forms.
   - Add a maximum of **100 questions** per form.
   - Select a [type](#question-types) for each question.
   - Order the questions in a form.
   - Configure every question type with relevant details (e.g., ordering options for checkbox/dropdown questions).

2. **View Forms:**
   - See a list of all forms they have created.

---

### **End User**
End Users should be able to:
1. **Submit Responses:**
   - Respond to any form anonymously (no authentication required).
   - Submit responses an unlimited number of times.

---

### **Shared Features**
All users (Admins and End Users) should be able to:
1. **View Analytics:**
   - Access analytics for every form at a **public URL**.
   - See total response count at the form level.
   - View question-specific analytics for the [**MVP question types**](#mvp-required-for-submission):
     - **Text Field:** Distribution of the top 5 most common words (≥5 characters). Aggregate the rest under "Others."
     - **Checkbox:** Distribution of the top 5 option combinations. Aggregate the rest under "Others."
     - **Dropdown:** Distribution of the top 5 selected options. Aggregate the rest under "Others."

---

## Question Types

### **MVP (Required for Submission):**
1. **Text**: Open-ended text input field.
	Example: "What is your name?"
2. **Dropdown**: Single-choice from a predefined list of options.
	Example: "What is your gender?" (Options: Male, Female, Other)
3. **Checkbox**: Multiple-choice from a predefined list of options.
	Example: "Which fruits do you like?" (Options: Apple, Banana, Cherry)

### **Future:**
**Note: These are not required, but your solution should be modular to allow for adding these later.**
1. **Ranking**: Rank options in a specific order. 
	Example: "Rank your favorite cuisines: Italian, Indian, Chinese."
2. **Linear Scale**: Respond with a value on a numerical scale.
	Example: "Rate our service on a scale of 1 to 10."
3. **Date Picker**: Select a date from a calendar interface.
	Example: "When is your birthdate?"
4. **Time Picker**: Select a time from a clock interface.
	Example: "What time do you usually wake up?"
5. **File Upload**: Upload a file as part of the response.
	Example: "Upload your resume."
6. **Matrix/Grid**: Respond to a grid of options with multiple rows and columns.
	Example: "Rate the following on satisfaction: Food, Cleanliness, Service."
7. **Image Choice**: Select one or more images from a set.
	Example: "Choose your preferred logo design."
8. **Slider**: Drag a slider to indicate a value.
	Example: "Set your monthly budget: $0 - $10,000."
9. **Signature Capture**: Capture a digital signature.
	Example: "Sign below to confirm your agreement."
10. **Color Picker**: Choose a color.
	Example: "Select your favorite color."
11. **Geolocation**: Submit location data.
	Example: "Share your current location."
12. **Percentage Allocation**: Allocate percentages across predefined categories.
	Example: "Allocate your budget: Food (30%), Entertainment (20%), Savings (50%)."

---

## Key Notes

1. **Code Structure:**
   - Follow **DRY** (Don’t Repeat Yourself) and **SRP** (Single Responsibility Principle).
   - Use modular design to enable easy addition of future question types.

2. **Technical Excellence:**
   - Apply Object-Oriented Programming (OOP) effectively for clean, extensible, and maintainable code.
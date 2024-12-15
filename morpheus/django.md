## Django challenge assignment for AtomicAds

### Introduction
The goal of this challenge is to test your familiarity with concepts in Django.
To read more about the recruitment process and open opportunities at AtomicAds, click [here](https://rtba.notion.site/Careers-at-RTBAnalytica-65dbc349de6b4b3e9ac9f63a9242f290)

*Note: This is a public submission. Any work on this assignment does not bring AtomicAds or its employees any moat; and by design, is made to assess skills we need. Stories provided are unrelated to AtomicAds's core business.* 

### Assignment

*   Unless a specific story is assigned to you, you can select any one of the stories mentioned in the [stories](/stories/) folder
*   Develop an API-driven application in Django that fulfills the requirements outlined in the story.
*   Follow [Instructions](#instructions) and [Submission Process](#submission-process) to ensure your submission is complete and adheres to expectations.
*   Expect evaluation within **5 working days** after submission.
*   Deliver the assignment as a **single submission**.
*   For success, ensure you get as many checks as in our [Assessment Criteria](#assessment-criteria)


### Instructions

1.  **Model**: Design database schema and implement using Django ORM with validations
    - Design the database schema and implement it using Django ORM with appropriate validations.
    - Modular design is encouraged to ensure extensibility.
2.  **View**: API Design
    - Develop the application with a strong emphasis on being API-driven.
    - Use [**Django Rest Framework (DRF)**](https://www.django-rest-framework.org/) for creating RESTful APIs.
    - Document APIs in a [**Postman collection**](https://www.postman.com/collection/).
    - All functionality described in the [story](../stories/) should be executable through the API.
3.  **View**: Optional Frontend (Bonus Points)
    - Build a sample UI for Admins and End Users.
    - You can use any frontend framework or render views using Django templates.
    - More brownie points for an API-driven UI.
4. **Documentation**:
   - Include **docstrings** for all classes and functions.
   - Document a **list of assumptions** for any features or behaviors not explicitly defined in the story.
5. **Database**:
   - Use **SQLite**, **PostgreSQL**, or **MySQL** as the database for the prototype.
6. **Clean Code**:
   - Follow **DRY** (Don’t Repeat Yourself) and **SRP** (Single Responsibility Principle).
   - Ensure proper organization and maintainability of your code.

### Assessment Criteria

Your submission will be evaluated on the following parameters:

1. Adherence to the [Instructions](#instructions).
2. **Code Quality**:
   - Maintainable and modular code.
   - Balance between speed and quality — document any trade-offs made.
3. **Ownership**:
   - Go beyond the story requirements (e.g., provide a sample UI interacting with the API).
4. **Version Control**:
   - Follow best practices for pull requests and commit message [guidelines](https://gist.github.com/turbo/efb8d57c145e00dc38907f9526b60f17).
   - Ability to demonstrate proficiency with Git.
5. **Documentation**:
   - Clear setup and usage instructions in the README file.
   - Comprehensive API documentation (Postman collection).
6. **Communication**:
   - Actively communicating with our team during the submission process for clarifications or updates.

### Submission Process
1. Fork this repository to your personal GitHub profile.
2. Delete all files and folders in the forked repository. Start your project from scratch within this repository.
3. Add a **README** at the root level with:
   - Setup instructions.
   - Detailed usage guide.
4. Raise a Pull Request to the original repository:
   - Use the provided [Pull Request template](https://github.com/AtomicAds/morpheus/blob/main/.github/pull_request_template.md).
   - Answer all questions and check relevant boxes in the template.

### Code of Ethics
- Be original. Submissions are public via GitHub and will be reviewed thoroughly. In cases of plagiarism, the work will be deemed invalid and disregarded.
- Cite any external code you use, including the source and its licensing terms.

### Learning Resources
1. [The Official Django Tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/)
2. [Version control with git](https://try.github.io/)
3. [Pull Request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request)
4. [Django Rest Framework Documentation](https://www.django-rest-framework.org/)

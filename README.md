<p align="center">
    <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" align="center" width="30%">
</p>
<p align="center"><h1 align="center">TASK_AI</h1></p>
<p align="center">
	<em>Empowering tasks with AI intelligence effortlessly.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/vishvas-10/Task_AI?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/vishvas-10/Task_AI?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/vishvas-10/Task_AI?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/vishvas-10/Task_AI?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

##  Table of Contents

- [ Overview](#-overview)
- [ Features](#-features)
- [ Project Structure](#-project-structure)
  - [ Project Index](#-project-index)
- [ Getting Started](#-getting-started)
  - [ Prerequisites](#-prerequisites)
  - [ Installation](#-installation)
  - [ Usage](#-usage)
  - [ Testing](#-testing)
- [ Project Roadmap](#-project-roadmap)
- [ Contributing](#-contributing)
- [ License](#-license)
- [ Acknowledgments](#-acknowledgments)

---

##  Overview

TaskAI is a cutting-edge project that streamlines task management with AI integration. It simplifies user authentication, task tracking, and productivity insights. Ideal for professionals seeking efficient task organization and enhanced productivity. Experience seamless task management and insightful statistics with TaskAI.

---

##  Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes **Flask** framework for web application development.</li><li>Follows **MVC** design pattern for separation of concerns.</li><li>Integrates **SQLAlchemy** for database ORM operations.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent code formatting using **Black**.</li><li>Includes **type hints** for improved code readability and maintainability.</li><li>Follows **PEP 8** guidelines for Python code styling.</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive **Python** documentation with **16 .py files** and **1 .txt file**.</li><li>Includes **7 HTML files** for frontend templates.</li><li>Utilizes **Flask-WTF** for form handling and validation.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integrates with **OpenAI** for AI capabilities.</li><li>Uses **Flask-SQLAlchemy** for seamless database integration.</li><li>Utilizes **WTForms** for form creation and validation.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Organized codebase with **separate modules** for routes, forms, models, and services.</li><li>Encapsulates functionality within **Flask Blueprints** for modular routing.</li><li>**Decorator functions** ensure code reusability and maintainability.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes **pytest** for automated testing.</li><li>Implements test cases for **route functions**, **form validations**, and **service functions**.</li><li>Ensures **test coverage** for critical components.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimizes performance with **Gunicorn** as the web server.</li><li>Utilizes **asyncio** for asynchronous operations.</li><li>Efficiently handles **task generation** and **subtask processing** for improved responsiveness.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Implements **password hashing** for user authentication.</li><li>Utilizes **Flask-Login** for user session management.</li><li>Ensures **secure routes** with authentication checks.</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Manages dependencies using **pip** and **requirements.txt**.</li><li>Includes essential packages like **Flask**, **SQLAlchemy**, and **OpenAI**.</li><li>Ensures compatibility with specified versions for smooth operation.</li></ul> |

---

##  Project Structure

```sh
└── Task_AI/
    ├── Dockerfile
    ├── README.md
    ├── app
    │   ├── __init__.py
    │   ├── decorators.py
    │   ├── forms
    │   │   ├── __init__.py
    │   │   ├── auth_form.py
    │   │   ├── logout_form.py
    │   │   ├── password_form.py
    │   │   ├── register_form.py
    │   │   └── task_form.py
    │   ├── models.py
    │   ├── routes
    │   │   ├── __init__.py
    │   │   ├── auth.py
    │   │   ├── dashboard.py
    │   │   ├── home.py
    │   │   ├── profile.py
    │   │   ├── register.py
    │   │   └── tasks.py
    │   ├── services
    │   │   ├── __init__.py
    │   │   ├── llm_client.py
    │   │   └── subtask_generator.py
    │   ├── static
    │   │   ├── css
    │   │   │   ├── auth.css
    │   │   │   ├── landing.css
    │   │   │   ├── profile.css
    │   │   │   └── tasks.css
    │   │   └── images
    │   │       └── favicon.png
    │   └── templates
    │       ├── _stats_partial.html
    │       ├── change_password.html
    │       ├── dashboard.html
    │       ├── landing.html
    │       ├── login.html
    │       ├── profile.html
    │       └── register.html
    ├── requirements.txt
    └── run.py
```


###  Project Index
<details open>
	<summary><b><code>TASK_AI/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/run.py'>run.py</a></b></td>
				<td>- Initializes and runs the application by creating an app instance from the app module<br>- The code sets the host to '0.0.0.0' and the port to 8000.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/requirements.txt'>requirements.txt</a></b></td>
				<td>- Manages project dependencies for a Flask-based application, including SQLAlchemy, WTForms, and Gunicorn<br>- Facilitates integration with OpenAI, Groq, and other libraries for enhanced functionality<br>- Ensures compatibility and smooth operation by specifying required versions of essential packages.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/Dockerfile'>Dockerfile</a></b></td>
				<td>- Facilitates Docker containerization for a Python application<br>- Sets up a lightweight Python environment, installs dependencies, and configures Gunicorn for web server functionality<br>- Optimizes resource usage with low process count and thread support<br>- Streamlines deployment and scalability by exposing port 8000 for external access.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- app Submodule -->
		<summary><b>app</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/decorators.py'>decorators.py</a></b></td>
				<td>- Ensure user authentication for Flask routes by redirecting unauthenticated users to the login page<br>- The code in decorators.py checks if a user is logged in using Flask-Login and redirects them if not<br>- This decorator helps secure routes that require authentication, enhancing the overall project's security and user experience.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/models.py'>models.py</a></b></td>
				<td>- Defines database models for users, tasks, subtasks, and stats with relationships to manage task-related data efficiently<br>- Establishes user attributes and task details, enabling seamless tracking and organization of tasks and subtasks<br>- Facilitates user-specific statistics storage for enhanced productivity insights within the application.</td>
			</tr>
			</table>
			<details>
				<summary><b>templates</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/templates/register.html'>register.html</a></b></td>
						<td>- Render a user registration form in HTML for the project's authentication system, allowing users to create accounts with their name, email, and password<br>- The form includes validation for each input field and a link to log in for existing users<br>- The HTML file is structured to provide a seamless account creation experience within the project's authentication flow.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/templates/_stats_partial.html'>_stats_partial.html</a></b></td>
						<td>Display statistics for active tasks, completed tasks, and productivity in a visually appealing format using HTML elements.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/templates/profile.html'>profile.html</a></b></td>
						<td>- Generates a user profile page with dynamic content like user name, email, and avatar initials<br>- Provides options to update password and logout<br>- Renders a visually appealing layout with a gradient background and CSS styling<br>- Enhances user experience by offering interactive elements for profile management.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/templates/landing.html'>landing.html</a></b></td>
						<td>- Defines the landing page layout and content for TaskAI, showcasing its features and benefits to visitors<br>- It presents the brand, key messaging, and a demo of AI capabilities, aiming to attract users to explore further and engage with the platform.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/templates/login.html'>login.html</a></b></td>
						<td>- Render a login page template with form fields for email and password, allowing users to log in and manage tasks<br>- Display alerts for messages, and provide a link to register for new users<br>- The template includes styling and references to external CSS and image files for a cohesive user experience within the project architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/templates/change_password.html'>change_password.html</a></b></td>
						<td>- Enables users to change their password securely through a user-friendly web interface<br>- Displays feedback messages and validation errors for a seamless user experience<br>- Integrates with the project's CSS and image assets for consistent styling.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/templates/dashboard.html'>dashboard.html</a></b></td>
						<td>- The code in the dashboard.html file orchestrates the user interface for TaskAI's dashboard, displaying tasks, user information, and interactive elements like task completion toggles<br>- It integrates with backend functionality to update task statuses and statistics dynamically, providing a seamless user experience for managing tasks efficiently.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>forms</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/forms/password_form.py'>password_form.py</a></b></td>
						<td>Implements a FlaskForm for changing passwords with validation rules for old password, new password length, and password confirmation.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/forms/register_form.py'>register_form.py</a></b></td>
						<td>- Defines a FlaskForm class for user registration with fields for name, email, password, and confirmation<br>- Validators ensure required data, valid email format, password length, and matching passwords<br>- The form includes a submission button for user sign-up.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/forms/task_form.py'>task_form.py</a></b></td>
						<td>Defines a FlaskForm class for task input with validation rules.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/forms/auth_form.py'>auth_form.py</a></b></td>
						<td>- Defines a FlaskForm class for user authentication, including fields for email, password, and a submit button<br>- Validators ensure required data and proper email format for the email field, and enforce password length constraints<br>- This form facilitates secure user login functionality within the project's architecture.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/forms/logout_form.py'>logout_form.py</a></b></td>
						<td>Implements a Flask form for user logout functionality, ensuring data is required before submission.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>routes</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/routes/dashboard.py'>dashboard.py</a></b></td>
						<td>- Generates dashboard data for rendering the user's tasks, stats, and greeting based on the time of day<br>- Retrieves and filters tasks based on completion status<br>- Calculates productivity based on completed subtasks<br>- Displays the dashboard template with user information, statistics, tasks, and a personalized greeting.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/routes/tasks.py'>tasks.py</a></b></td>
						<td>- Improve task management by adding, deleting, and toggling tasks and subtasks<br>- Enhance user productivity with real-time stats updates<br>- Ensure data security and user authorization throughout task interactions<br>- Maintain a seamless user experience by dynamically updating task statuses and statistics on the dashboard.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/routes/home.py'>home.py</a></b></td>
						<td>Defines a route for the home page using Flask Blueprint to render the landing page template.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/routes/register.py'>register.py</a></b></td>
						<td>- Registers new users by validating form data, checking for existing emails, hashing passwords, and creating new user entries in the database<br>- Flash messages provide feedback on successful or failed user creation<br>- The route renders the registration form and handles form submission for user registration.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/routes/profile.py'>profile.py</a></b></td>
						<td>- Enables user profile management and password change functionality<br>- Utilizes Flask Blueprint for routing and authentication checks<br>- Renders profile and password change forms, updating user passwords securely in the database<br>- Flash messages provide feedback to users.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/routes/auth.py'>auth.py</a></b></td>
						<td>- Manages user authentication and session handling for the Flask application<br>- Validates user login credentials, sets session data upon successful login, and clears session data upon logout<br>- Implements password hashing for secure authentication.</td>
					</tr>
					</table>
				</blockquote>
			</details>
			<details>
				<summary><b>services</b></summary>
				<blockquote>
					<table>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/services/llm_client.py'>llm_client.py</a></b></td>
						<td>Creates an OpenAI client for the project, utilizing environment variables for authentication.</td>
					</tr>
					<tr>
						<td><b><a href='https://github.com/vishvas-10/Task_AI/blob/master/app/services/subtask_generator.py'>subtask_generator.py</a></b></td>
						<td>- Generates subtasks by breaking down a task into 5 actionable steps, following specific rules<br>- Utilizes an external service to process input and return valid JSON output<br>- Ensures the output format includes task details and success/failure status<br>- Maintains consistency in output structure for successful processing.</td>
					</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---
##  Getting Started

###  Prerequisites

Before getting started with Task_AI, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker


###  Installation

Install Task_AI using one of the following methods:

**Build from source:**

1. Clone the Task_AI repository:
```sh
❯ git clone https://github.com/vishvas-10/Task_AI
```

2. Navigate to the project directory:
```sh
❯ cd Task_AI
```

3. Install the project dependencies:


**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t vishvas-10/Task_AI .
```




###  Usage
Run Task_AI using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


###  Testing
Run the test suite using the following command:
**Using `pip`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pytest
```


---
##  Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

##  Contributing

- **💬 [Join the Discussions](https://github.com/vishvas-10/Task_AI/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/vishvas-10/Task_AI/issues)**: Submit bugs found or log feature requests for the `Task_AI` project.
- **💡 [Submit Pull Requests](https://github.com/vishvas-10/Task_AI/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/vishvas-10/Task_AI
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/vishvas-10/Task_AI/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=vishvas-10/Task_AI">
   </a>
</p>
</details>

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---

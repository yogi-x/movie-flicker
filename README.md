
# Flask-in-Docker: Fetch Latest Movies with Ease

  
This project provides a streamlined workflow to build and deploy a Flask application that fetches and displays the latest movie data. It leverages Docker for a containerized development environment and utilizes the TMDB API (The Movie Database) for movie information.

  **Key Benefits:**
  
-   **Reusable Template:** Use this project as a base for further Flask and Docker exploration.
-   **Simplified Setup:** Get started quickly with pre-configured Docker development environment.
-   **Easy Deployment:** Deploy your Flask app as a container for production or sharing.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Ensure you have the following installed on your local development machine:

- Python3

- Docker

### Installation

1. Clone the repository to your local machine.
```bash
git clone https://github.com/your-username/flask-movie-docker.git
```
2. Navigate to the project directory.

3. Install the required Python packages using pip:

```bash
pip  install  -r  requirements.txt
```
4. Run the application
#### For Windows Users:
```bash
python3 app.py
```

#### For Docker:

```bash
docker  build  -t  moviesapp  .
```

```bash
docker run -v ${pwd}:/app -p 5000:5000 moviesapp
```

Now, your application should be running at localhost:5000.# movie-flicker

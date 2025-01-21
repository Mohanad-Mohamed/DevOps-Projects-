# Project 1 - Deploy A Simple HTML Web Page Using Nginx

## Description
This project demonstrates how to deploy a simple HTML web page using Nginx. The web page can be accessed via a web browser on port 8080.

## Setup and Installation
1. Create a directory named `website` and navigate into it:
   ```bash
   mkdir website
   cd website
   ```
2. Create an `index.html` file with your desired content.

## Running the Application
To run the application using Docker:
1. Run the Nginx container:
   ```bash
   docker run -it -d --name html -p 8080:80 --name web -v ~/website:/usr/share/nginx/html nginx
   ```
2. Access the application from the browser at `http://localhost:8080`.

## Requirements
- Docker
- Nginx

## License
This project is licensed under the MIT License.

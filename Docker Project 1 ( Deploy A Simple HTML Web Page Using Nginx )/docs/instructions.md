# Deployment Instructions

## Objective
1. Create a host directory.
2. Create an `index.html` file inside this directory.
3. Run an Nginx container and expose it using port 8080.
4. Access the container from a browser.

## Steps
1. Create a directory named `website` and navigate into it:
   ```bash
   mkdir website
   cd website
   ```

2. Create an `index.html` file with the following content:
   ```html
   <!doctype html>
   <html lang="en">
   <head>
     <meta charset="utf-8">
     <title>Home page</title>
   </head>
   <body>
     <h1>Hello from Course Docker Mastery</h1>
     <p>Regards,</p>
     <p>Mena Magdy Halem</p>
     <a href="https://www.linkedin.com/in/mena-magdy-halem/" target="_blank">Connect with Me</a>
   </body>
   </html>
   ```

3. Run the Nginx container:
   ```bash
   docker run -it -d --name html -p 8080:80 --name web -v ~/website:/usr/share/nginx/html nginx
   ```

4. Access the application from the browser at `http://localhost:8080`.

5. You can edit anything in `index.html` and save it to see the changes immediately in the browser.

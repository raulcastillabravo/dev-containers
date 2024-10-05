# Usuful commands

- Create Docker volume: *docker volume create data_volume*
- Build Docker image: *docker build -t [image_name] .*
- Run Docker Compose: *docker compose up*
- Run API container alone: *docker run -d -p 5000:5000 api_image*
- Test API: *curl -X GET http://localhost:5000/api/[name]*
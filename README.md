# warpdrive-template
Warpdrive template for Django to create Docker image and deploy to OpenShift3. Inlcudes Vue.js Webpack application.

# Development
```bash
git clone https://github.com/djstein/warpdrive-template.git
virtualenv -p python3 venv
pip install -Ur requirements.txt
npm run install     # in vueapp/

# Do not add warpdrive to requirements.txt
pip install warpdrive

# In two terminals for hot reloading
python manage.py runserver
npm run dev     # in vueapp/

# For development, node is serving on 8080, django on 8000
localhost:8000

# Check build
eval "$(warpdrive activate project)"

npm run install    # in vueapp/
npm run build     # in vueapp/

# To collect static files
warpdrive build

# To server site and static files
warpdrive start
```

#Deployment
For warpdrive build to work Docker and s2i must be installed
```bash
npm run build
warpdrive build
warpdrive image <docker.hub username>/<repo>:<tag>

# Check build
docker run --rm -p 8080:8080 <docker.hub username>/<repo>:<tag>

# Push to hub.docker
docker login
docker push <docker.hub username>/<repo>:<tag>

# Create OC app after project is created
oc new-app <docker.hub username>/<repo>:<tag>
```

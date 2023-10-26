from django.shortcuts import render
import subprocess
import docker
import docker.errors
import re
from django.http import JsonResponse

def default_view(request):
    client = docker.from_env()
    available_images = client.images.list()
    image_tags = [image.tags for image in available_images]
    client.close()
    return render(request, 'geoapp/user_interface.html', {'available_images': image_tags})

def run_docker_container(request):
    
    if request.method == 'POST':
         
         action = request.POST.get('action')
         image_tag = request.POST.get('image')
         container_name = image_tag.split(':')[0]  
         USERNAME = request.POST.get('var1')
         PASSWORD = request.POST.get('var2')
         VAR1 = request.POST.get('var3')
         VAR2 = request.POST.get('var4')
         VAR3 = request.POST.get('var5')
         VAR4 = request.POST.get('var6')
         VAR5 = request.POST.get('var7')
         VAR6 = request.POST.get('var8')
         command = f"docker run -v /home/nikos/geoproject3/geoapp/shared_files:/shared_files -v /var/run/docker.sock:/var/run/docker.sock -p 8888:8888 -e USERNAME={USERNAME} -e PASSWORD={PASSWORD} -e VAR1={VAR1} -e VAR2={VAR2} -e VAR3={VAR3} -e VAR4={VAR4} -e VAR5={VAR5} -e VAR6={VAR6} {image_tag}"
         
         subprocess.Popen(command, shell=True)
         message = "Container is now running! "
         
        
         return render(request, 'geoapp/user_interface.html', {'message': message})

def check_error_messages(request):
    try:
        with open('geoapp/shared_files/error_message.txt', 'r+') as error_file:
            error_message = error_file.read().strip()
            error_file.seek(0)
            error_file.truncate(0)
    except FileNotFoundError:
        error_message = 'Not Found'
       
    print("Error:", error_message)  

    return JsonResponse({'error_message': error_message})
    
    
def check_jupyterlab_status(request):
    try:
        with open('geoapp/shared_files/jupyterlab_status.txt', 'r+') as status_file:
            status = status_file.read().strip()
            status_file.seek(0)
            status_file.truncate(0)
    except FileNotFoundError:
        status = 'Not Found'
       
    print("Status:", status)  

    return JsonResponse({'status': status})

def get_container_id_by_image(image_name):
    command = f"docker ps -a --filter ancestor={image_name} -q"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, _ = process.communicate()
    container_ids = output.decode().strip().split('\n')
    return container_ids


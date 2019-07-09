from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import files

# Create your views here.

def notes(request):
	if request.user.is_authenticated:
			print('check user status')
			print(request.user)
			uploads = files.objects.all().order_by('-uploaded_at')
			if request.method == 'POST':
				if request.FILES.get('doc'):
					myfile = request.FILES.get('doc')
					print(myfile.name)

					#USING FILESYSTEMSTORAGE API OF DJANGO
					#fs = FileSystemStorage()
					#filename = fs.save(myfile.name, myfile)
					#uploaded_file_url = fs.url(filename)
					#print(uploaded_file_url)

					note = request.POST['note']
					author = request.user
					a=files.objects.create(note=note,document=myfile,author=author)
					return redirect('notes')

				else:
					messages.info(request,'please select file')
					return redirect('notes')
						


			else:

				return render(request,'notes.html', {'show': uploads})


	else:

		messages.info(request,'Login Required')
		return render(request,'index.html')			
	
			
				










	    

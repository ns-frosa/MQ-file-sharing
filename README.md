#Installation Steps 

>docker build -t essential_file_sharing .

>docker run -d -p 5000:5000 -v /local/path/to/files:/opt/files essential_file_sharing

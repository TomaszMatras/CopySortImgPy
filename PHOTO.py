
# import modułów
import os
import shutil
import datetime
from pathlib import Path
import hashlib
# sciezka z kąd i dokąd
dIr = 'E:\\tempPhone'
dEst = 'E:\\zdjecia'

ImgArr = [
	"ase",
	"art",
	"bmp",
	"blp",
	"cd5",
	"cit",
	"cpt",
	"cr2",
	"cut",
	"dds",
	"dib",
	"djvu",
	"egt",
	"exif",
	"gif",
	"gpl",
	"grf",
	"icns",
	"ico",
	"iff",
	"jng",
	"jpeg",
	"jpg",
	"jfif",
	"jp2",
	"jps",
	"lbm",
	"max",
	"miff",
	"mng",
	"msp",
	"nef",
	"nitf",
	"ota",
	"pbm",
	"pc1",
	"pc2",
	"pc3",
	"pcf",
	"pcx",
	"pdn",
	"pgm",
	"PI1",
	"PI2",
	"PI3",
	"pict",
	"pct",
	"pnm",
	"pns",
	"ppm",
	"psb",
	"psd",
	"pdd",
	"psp",
	"px",
	"pxm",
	"pxr",
	"qfx",
	"raw",
	"rle",
	"sct",
	"sgi",
	"rgb",
	"int",
	"bw",
	"tga",
	"tiff",
	"tif",
	"vtf",
	"xbm",
	"xcf",
	"xpm",
	"3dv",
	"amf",
	"ai",
	"awg",
	"cgm",
	"cdr",
	"cmx",
	"dxf",
	"e2d",
	"egt",
	"eps",
	"fs",
	"gbr",
	"odg",
	"svg",
	"stl",
	"vrml",
	"x3d",
	"sxd",
	"v2d",
	"vnd",
	"wmf",
	"emf",
	"art",
	"xar",
	"png",
	"webp",
	"jxr",
	"hdp",
	"wdp",
	"cur",
	"ecw",
	"iff",
	"lbm",
	"liff",
	"nrrd",
	"pam",
	"pcx",
	"pgf",
	"sgi",
	"rgb",
	"rgba",
	"bw",
	"int",
	"inta",
	"sid",
	"ras",
	"sun",
	"tga",
	"heic",
	"heif",
    "dng"]
VidArr = [
	"3g2",
	"3gp",
	"aaf",
	"asf",
	"avchd",
	"avi",
	"drc",
	"flv",
	"m2v",
	"m3u8",
	"m4p",
	"m4v",
	"mkv",
	"mng",
	"mov",
	"mp2",
	"mp4",
	"mpe",
	"mpeg",
	"mpg",
	"mpv",
	"mxf",
	"nsv",
	"ogg",
	"ogv",
	"qt",
	"rm",
	"rmvb",
	"roq",
	"svi",
	"vob",
	"webm",
	"wmv",
	"yuv"]
#counter
i =0 

#zmień nazwe pliku na podstawie daty (numer dnia) (nazwa dnia tygodnia)  (godzina)
def renameFile(cTime, file , add):
    file_name, file_extension = os.path.splitext(file)
    add = str(add)
    newName = str(cTime.strftime('%d_%A_%H-%M-%S') + ' ' + add + file_extension)
    return(newName)
    
    
#skopjuj plik i zmień jego nazwe
def moveFile(file, name, ctime, end):
    year = ctime.strftime('%G')
    month = ctime.strftime('%B')
    dest = os.path.join(dEst, year , month, end)
    if os.path.exists(dest):
        pass
    else:
        os.makedirs(dest)
    dest = os.path.join(dEst, year , month, end, name)
    j = 0
    while os.path.exists(dest):
          j += 1
          name =  renameFile(ctime, file, j)
          dest = os.path.join(dEst, year , month, end, name)
    shutil.copy(file, dest)
  
        
        
#extract metadanych
#zwróci fatetime    
def meta(file):

  file = Path(file)
  print(file.stat())
  date = datetime.datetime.fromtimestamp(file.stat().st_mtime)
  return date
  
    
def extent(file):
    if file.endswith(tuple(ImgArr)):
        return 'img'
    elif file.endswith(tuple(VidArr)):
        return 'vid'
    else:
        return 'other'
        
    

end = 'a'   
#crawler     
for root, dirs, files in os.walk(dIr):
#    print("\n ********************* \n size: " + str(len(files)))
 #   print(" root: " + str(root) + " dirs: " + str(dirs) + "files: "+ str(files) + '\n \n *********************')
    for filename in files:
      #weź tylko jpg
  #    print(str(os.path.join(root, filename)))
      filepath = os.path.join(root, filename)
      if os.path.isfile(filepath):
          end = extent(filepath)
   #       print(end)
          date = meta(filepath)
   #       print(date)
          name = renameFile(date, filepath, " ")
    #      print(name)
          moveFile(filepath, name, date, end)
    #      print('---------------------------------------------')
  
#usuń duplikaty    
hashes = {}
delete = []
# Iterate through all files in the directory
for root, dirs, files in os.walk(dEst):
    for file in files:
        # Get the full path of the file
        full_path = os.path.join(root, file)
       
    
        # Open the file in read-binary mode
        with open(full_path, 'rb') as f:
            # Calculate the SHA-1 hash of the file
            file_hash = hashlib.sha1(f.read()).hexdigest()

         
            if file_hash in hashes:
            
                 delete.append(full_path)     
       #          print("added duplicate image:", full_path)
            else:
                # If the file is not in the dictionary, add it
                hashes[file_hash] = full_path

# Call the function with the path to the directory containing the images
#print(delete)
for file in delete:
    os.remove(file)
  

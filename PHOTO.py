
# import modułów
import os
import shutil
import datetime
from pathlib import Path
# sciezka z kąd i dokąd
DIR = 'E:\\tempPhone'
DEST = 'E:\\zdjecia'

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
    dest = os.path.join(DEST, year , month, end)
#    print("dest:" + str(dest))
    if os.path.exists(dest):
        pass
    else:
        os.makedirs(dest)
    dest = os.path.join(DEST, year , month, end, name)
    j = 0
    while os.path.exists(dest):
          j += 1
          name =  renameFile(ctime, file, j)
          dest = os.path.join(DEST, year , month, end, name)
        #  print("destI:" + str(dest))
         
   # print("dest2:" + str(dest))
    shutil.copy(file, dest) #skopjuj zmień nazwe
  
        
        
#extract metadanych
#zwróci fatetime    
def meta(file):
 #   time = os.path.getctime(file)
 #   date = datetime.fromtimestamp(time)
#     file_stats = os.stat(file)
  #   print(file_stats)
  #   date = datetime.datetime.fromtimestamp(file_stats.st_ctime)

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
for root, dirs, files in os.walk(DIR):
    print("\n ********************* \n size: " + str(len(files)))
    print(" root: " + str(root) + " dirs: " + str(dirs) + "files: "+ str(files) + '\n \n *********************')
    for filename in files:
      #weź tylko jpg
      print(str(os.path.join(root, filename)))
      filepath = os.path.join(root, filename)
      if os.path.isfile(filepath):
          end = extent(filepath)
          print(end)
          date = meta(filepath)
          print(date)
          name = renameFile(date, filepath, " ")
          print(name)
          moveFile(filepath, name, date, end)
          print('---------------------------------------------')
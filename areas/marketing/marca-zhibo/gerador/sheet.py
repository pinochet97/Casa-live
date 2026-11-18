import sys,glob
from PIL import Image
fs=sorted(glob.glob(sys.argv[1])); cols=int(sys.argv[3]) if len(sys.argv)>3 else 4
ims=[Image.open(f).convert('RGB') for f in fs]; w=int(sys.argv[4]) if len(sys.argv)>4 else 400
ims=[i.resize((w,int(i.height*w/i.width))) for i in ims]; h=max(i.height for i in ims)
rows=(len(ims)+cols-1)//cols; out=Image.new('RGB',(cols*(w+6),rows*(h+6)),'#777')
for k,i in enumerate(ims): out.paste(i,((k%cols)*(w+6),(k//cols)*(h+6)))
out.save(sys.argv[2]); print(len(ims),out.size)

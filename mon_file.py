修改一个目录里面的文件名
cwd_img = "D:\Radio image2\SkyCut"
for i,name in enumerate(os.listdir(cwd_img)):
    new_cwd_img = cwd_img+'\%d.tif'%(i)
    os.rename(os.path.join(cwd_img,name),new_cwd_img)

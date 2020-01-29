import os
import time
import shutil

class XBM_Converter():

    def __init__(self):
        print("Beginning procedure")
        self.main()
        time.sleep(3)

    def main(self):
        self.cpp_syntax = """#ifndef _GxBitmapExamples_H_\n#define _GxBitmapExamples_H_\n#if defined(ESP8266) || defined(ESP32)\n#include <pgmspace.h>\n#else\n#include <avr/pgmspace.h>\n#endif\nconst unsigned char BitmapExample1[] PROGMEM =\n{"""
        self.remove_old_syntax = """#define image_width 640\n#define image_height 384\nstatic char image_bits[] = {"""
        self.hexcode_path = "C:/Users/Administrator/Documents/Arduino/libraries/GxEPD/src/GxGDEW075Z09/BitmapExamples.h"
        self.hfile = "BitmapExamples.h"

        if os.path.exists('image.png'):
            os.system('xbm_convert.bat')
            os.rename("image.xbm", self.hfile)
            current_time = time.strftime("%Y%m%d-%H%M%S")
            os.rename("image.png", "image_backup/image_"+current_time+".png")

            with open(self.hfile,"r") as xbm_r:
                x = xbm_r.read()
                if self.remove_old_syntax in x:
                    print("Image format validated")
                    y = x.replace(self.remove_old_syntax, "").replace("};", "").replace(" ","").replace("\n","")
                    with open(self.hfile, "w") as xbm_w:
                        xbm_w.write(y)

                        with open(self.hfile, "r+") as x:
                            y = x.read()
                            z = y.split(",")
                            z.reverse()
                            z2 = ",".join(z)
                            z2.replace("'", "").replace("[", "").replace("]", "")
                            x.seek(0, 0)
                            x.write(str(z2[1:]))
                            x.close()
                        xbm_w.close()
                        with open(self.hfile, "r+") as xbm_a:
                            content = xbm_a.read()
                            xbm_a.seek(0, 0)
                            xbm_a.write(self.cpp_syntax+"\n"+content)
                            xbm_a.seek(0, 2)
                            xbm_a.write("}; \n#endif")
                            xbm_a.close()
                    xbm_r.close()
                    print("Adjusted code to C++ Syntax")
                    if os.path.exists(self.hexcode_path):
                        os.remove(self.hexcode_path)
                    shutil.copyfile(self.hfile,"image_code_backup/BitmapExample"+current_time+".h")
                    print("Backup of imagecode saved")
                    #os.rename(hfile,hexcode_path)
                    print("File ready to upload!")
                    if os.path.exists(self.hfile):
                        os.remove(self.hfile)
                else:
                    print("Image does not have the right resolution!")



if __name__ == '__main__':
    while True:
        XBM_Converter()
import os
import time
import shutil

cpp_syntax = """#ifndef _GxBitmapExamples_H_
#define _GxBitmapExamples_H_
#if defined(ESP8266) || defined(ESP32)
#include <pgmspace.h>
#else
#include <avr/pgmspace.h>
#endif
const unsigned char BitmapExample1[] PROGMEM =
{"""

remove_old_syntax = """#define image_width 640
#define image_height 384
static char image_bits[] = {
  """

hexcode_path = "C:/Users/Administrator/Documents/Arduino/libraries/GxEPD/src/GxGDEW075Z09/BitmapExamples.h"
hfile = "BitmapExamples.h"


def main():
    if os.path.exists('image.png'):
        os.system("xbm_convert.bat")
        os.rename("image.xbm", hfile)
        current_time = time.strftime("%Y%m%d-%H%M%S")
        os.rename("image.png", "image_backup/image_"+current_time+".png")

        with open(hfile,"r") as xbm_r:
            x = xbm_r.read()
            if remove_old_syntax in x:
                y = x.replace(remove_old_syntax, "").replace("};", "").replace(" ","").replace("\n","")
                with open(hfile, "w") as xbm_w:
                    xbm_w.write(y)

                    with open(hfile, "r+") as x:
                        y = x.read()
                        z = y.split(",")
                        z.reverse()
                        z2 = ",".join(z)
                        z2.replace("'", "").replace("[", "").replace("]", "")
                        x.seek(0, 0)
                        x.write(str(z2[1:]))
                        x.close()
                    xbm_w.close()
                    with open(hfile, "r+") as xbm_a:
                        content = xbm_a.read()
                        xbm_a.seek(0, 0)
                        xbm_a.write(cpp_syntax+"\n"+content)
                        xbm_a.seek(0, 2)
                        xbm_a.write("}; \n#endif")
                        xbm_a.close()
                xbm_r.close()
                if os.path.exists(hexcode_path):
                    os.remove(hexcode_path)
                shutil.copyfile(hfile,"image_code_backup/BitmapExample"+current_time+".h")
                os.rename(hfile,hexcode_path)
                print("Datei bereit zum Upload!")
                if os.path.exists(hfile):
                    os.remove(hfile)
            else:
                print("Image does not have the right resolution!")



if __name__ == '__main__':
    while True:
        main()
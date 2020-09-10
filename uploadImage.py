import cv2
import dropbox
import time
import random
startTime = time.time()

def takeSnapshot():
    number = random.randint(0, 100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while (result):
        ret, frame = videoCaptureObject.read()
        imgName = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return imgName
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_files(imgName):
    accessToken = "sl.AhfWGQzbz91YxZNv1Hmh0Kf_XP4BPnaUBMiA5vVTnUZ4hBTsLDjYHzEADJswq_ukG8DRSuKi26OJyi2VJVYCC73M6seh70Cxee7ZGbd8u8XYmoPezzZXYkpD6X_ufaZKkmhxgug"
    file = img_counter
    file_from = file
    file_to = "/newfolder" + (imgName)
    dbx = dropbox.dropbox(accessToken)
    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")


def main():
    while (True):
        if((time.time()-startTime)>= 300):
            name = takeSnapshot()
            upload_files(name)




main()
